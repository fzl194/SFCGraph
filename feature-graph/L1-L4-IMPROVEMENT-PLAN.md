# L1-L4 改进计划

> 审计日期: 2026-06-08
> 范围: feature-graph/ 目录下 step4_extract_l1.py 的 L1-L4 层级抽取
> 基线: 898个特性, 673条依赖, 412条License, 3194条DocAsset

---

## 一、依赖关系（L3）改进

### 1.1 表头变体格式误入数据行

**问题**: 部分概述md的交互表表头用了 `**交互类型**`（粗体markdown），当前过滤条件 `parts[0] in ("交互类型", "交互")` 无法匹配，导致约15行表头被当作数据行处理（碰巧因不含特性ID而被丢弃，但逻辑不正确）。

**修复**: `extract_feature_dependencies` 中增加去粗体后的表头判断。

```python
# 当前:
if parts[0] in ("交互类型", "交互"):
    continue

# 改为:
header0 = parts[0].strip("*").strip()
header1 = parts[1].strip("*").strip() if len(parts) > 1 else ""
if header0 in ("交互类型", "交互") or header1 in ("相关特性",):
    continue
```

**影响范围**: 约15行不再误处理。结果不变（之前也碰巧被过滤了），但逻辑正确化。

---

### 1.2 "相关特性"列只写功能名无特性ID

**问题**: 约15行交互关系的"相关特性"列只写了功能名称（如"NAT功能"、"SA相关特性"、"移动VPN解决方案"），没有特性ID编号，导致 `FEATURE_ID_SEARCH_RE` 匹配不到，`target_fid` 为空，被丢弃。

典型案例:
- `互斥 | NAT功能 | 无 | ...`
- `依赖 | SA相关特性 | ... | ...`
- `依赖 | 移动VPN解决方案 | ... | ...`
- `依赖 | NA | ... | ...` (占位符)

**修复**: 在特性ID正则匹配失败后，用功能名去 features 清单做模糊匹配:

```python
if not target_fid:
    target_fid = lookup_feature_by_name(related_feature_raw, features_dict)
```

`lookup_feature_by_name` 逻辑:
1. 从 `related_feature_raw` 中去掉链接标记 `[xxx](yyy)`，取链接文本
2. 在 features_dict 中按 `feature_name` 做子串匹配
3. 匹配到唯一结果则返回 feature_id，多个或零个则返回空
4. 特殊值 "NA"、"-"、"无" 直接跳过

**前置依赖**: `extract_feature_dependencies` 函数需要接收 `features_dict` 参数。

---

### 1.3 SFFD 等跨体系特性ID不匹配

**问题**: 约5行交互关系引用了 Service Fabric 特性（如 `SFFD-010010`），当前正则只匹配 `GWFD|WSFD|IPFD|NPFD`，SFFD 被丢弃。

**修复**: 扩展正则:

```python
# 当前:
FEATURE_ID_SEARCH_RE = re.compile(r"((?:GWFD|WSFD|IPFD|NPFD)-\d{3,6})")

# 改为:
FEATURE_ID_SEARCH_RE = re.compile(r"((?:GWFD|WSFD|IPFD|NPFD|SFFD)-\d{3,6})")
```

**注意**: SFFD 特性不在 xlsx 特性清单中，提取后 target_fid 有效但无法关联到 Feature 节点。需在依赖表中保留，后续可标记为 `external_feature`。

---

### 1.4 description 含 HTML 残留

**问题**: 依赖关系 description 列中保留了 `<br>`、`<br/>`、`UDG<br>向SMF上报...` 等HTML标签。

**修复**: 在输出 description 前清理:

```python
description = re.sub(r"<br\s*/?>", " ", description)
description = re.sub(r"<[^>]+>", "", description)  # 清理其他HTML标签
description = description.strip()
```

---

### 1.5 dependency_type 语义收敛（P2，可选）

**问题**: 当前6种类型中 `affects`(126条)、`interacts_with`(25条)、`other`(10条) 语义模糊，对下游配置生成无明确指导。

**建议**: 保留原始映射不变，但在 CSV 中增加 `dependency_strength` 字段:
- `strong`: depends_on, conflicts_with
- `weak`: affects, interacts_with, other, supports, cooperates_with

下游使用时可按 `dependency_strength` 过滤。此改动为 Schema 扩展，不影响现有逻辑。

---

## 二、License（L4）改进

### 2.1 多 NF License 漏提取

**问题**: 部分特性的 License 按 NF 区分（如 WSFD-106101 有3条License: AMF/SMF/SMSF），但 CSV 中完全缺失。

**根因**: `extract_licenses` 函数的三种格式解析未覆盖所有"可获得性"section 的实际格式变体。

**修复方案**:
1. 增强格式2（NF表格）的解析: 当前 `in_table` 状态在遇到非匹配行时立即 `in_table = False`，如果表格中间有空行或格式行就会提前终止
2. 增加格式4: 按NF分段的纯文本（每个NF一小节，列出License编号）

```python
# 增加表格解析的容错
if in_table and len(parts) >= 2:
    # ... 正常解析
elif in_table:
    # 空行不一定意味着表格结束，只有遇到非表格内容且下一行也不是表格行才结束
    pass  # 保持 in_table 状态
```

---

### 2.2 license_name 脏数据

**问题**: 部分行的 `license_name` 末尾带 `|` 或引号（如 `IPv6承载上下文-UAM |`），`applicable_nf` 为空。

**根因**: 表格解析把格式行或分隔符当成数据行。

**修复**: 增加输出过滤:

```python
# 清理脏数据
name = license_name.strip().rstrip("|").rstrip('"').rstrip("'").strip()
if not name or len(name) < 2:
    continue
# 跳过 name 与表头相同的行
if name in ("License控制项", "License支持"):
    continue
```

---

### 2.3 License 正则表达式不兼容部分编码格式

**问题**: 当前正则 `([A-Za-z0-9]{8,10})\s+(\w+)\s+(.+?)` 限制 License 编码长度为8-10字符，且 `\w+` 不匹配含 `-` 的编码。

**修复**:

```python
# 当前:
lm = re.match(r"([A-Za-z0-9]{8,10})\s+(\w+)\s+(.+)", license_text)

# 改为:
lm = re.match(r"([A-Za-z0-9]{6,12})\s+([A-Za-z0-9_\-]+)\s+(.+)", license_text)
```

---

### 2.4 系统性补扫缺失 License（P0）

**问题**: UDG 80个、UNC 193个 `has_overview=yes` 但无 License 记录的特性中，部分原文实际有 License（如 WSFD-106101、WSFD-104401），被漏提取。

**修复方案**: 写补扫脚本，对无 License 的特性逐个重新检查"可获得性"section:
1. 原文含 `无需` + `License` → 标记 `no_license_required`
2. 原文含 License 编码模式但未被提取 → 用增强正则补抽
3. 产出差异报告供人工审核

---

## 三、L1 属性改进

### 3.1 applicable_nf 解析脆弱

**问题**: "适用 N F"（N和F之间有空格）导致 WSFD-227102 的 NF 完全缺失。

**修复**:

```python
# 当前:
text = sections.get("适用NF", "") or sections.get("适用 N F", "")

# 改为: 容忍各种空格/换行变体
nf_text = ""
for key in sections:
    if re.match(r"适\s*用\s*N\s*F", key):
        nf_text = sections[key]
        break
```

---

### 3.2 customer_value 含原始 Markdown 表格

**问题**: CSV 中 `customer_value` 列保留了 `| 受益方 | 受益描述 |` 格式。

**修复**: 提取时转为纯文本:

```python
def extract_customer_value(sections):
    text = sections.get("客户价值", "")
    # 去掉表格行，只保留纯文本段落
    lines = text.split("\n")
    result = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") or stripped == "---" or stripped.startswith(">"):
            continue
        if stripped:
            result.append(stripped)
    return " ".join(result) if result else text
```

---

### 3.3 Definition 仅取首段

**问题**: 部分特性原文有多段定义，只取了第一段。

**当前逻辑**: `extract_definition` 已经取了所有非表格、非图片的纯文本行并用空格连接。如果实际只取了首段，可能是 section 切分时被下一个 `####` 截断了——这是 `parse_overview_sections` 的正常行为。

**评估**: 这是正确行为——"定义"section 的边界由 `####` 标题决定。多段定义如果在同一个 section 内会被完整提取。无需修改。

---

## 四、通用改进

### 4.1 缺失字段补齐

| 表 | 缺失字段 | 当前状态 | 修复方式 |
|----|---------|---------|---------|
| DocAsset | `id` | 代码已生成但Schema对照表标注缺失 | 已有，确认即可 |
| DocAsset | `doc_title` | 代码已生成 | 已有，确认即可 |
| FeatureDependency | `id` | 代码已拼接 | 已有 |
| FeatureDependency | `source_type` | 统一填 `overview_explicit` | 已有 |

**结论**: 代码实际已经补了这些字段，Schema对照表中的"缺失"标注是过时的。更新 `FEATURE_GRAPH_SCHEMA.md` 中的状态即可。

---

## 五、实施优先级

| 优先级 | 改进项 | 改动文件 | 预估工作量 |
|--------|--------|---------|-----------|
| **P0** | 1.1 表头变体过滤 | step4_extract_l1.py | 3行 |
| **P0** | 1.4 HTML残留清理 | step4_extract_l1.py | 3行 |
| **P0** | 2.2 license_name脏数据过滤 | step4_extract_l1.py | 5行 |
| **P0** | 2.3 License正则增强 | step4_extract_l1.py | 2行 |
| **P1** | 1.2 功能名模糊匹配 | step4_extract_l1.py + 新增函数 | 30行 |
| **P1** | 1.3 SFFD前缀扩展 | step4_extract_l1.py | 1行 |
| **P1** | 3.1 applicable_nf空格兼容 | step4_extract_l1.py | 5行 |
| **P1** | 3.2 customer_value清理 | step4_extract_l1.py | 10行 |
| **P1** | 2.4 License补扫脚本 | 新文件 step4b_license_scan.py | 80行 |
| **P2** | 2.1 多NF License解析增强 | step4_extract_l1.py | 20行 |
| **P2** | 1.5 dependency_strength字段 | step4_extract_l1.py + Schema | 10行 |
| **P2** | 4.1 Schema状态更新 | FEATURE_GRAPH_SCHEMA.md | 文档 |

---

## 六、验证方案

每个改进项实施后需验证:

1. **P0项**: 重新运行 `python step4_extract_l1.py`，对比改进前后的CSV行数变化
2. **依赖关系**: 检查改进后总行数是否从673增长（预期增加约15-20行）
3. **License**: 检查改进后总行数是否从412增长，特别是 WSFD-106101、WSFD-104401 等已知缺失的特性
4. **脏数据**: grep 检查 `<br>` 和 `| ` 后缀是否消失
5. **回归**: 抽检 GWFD-020301、GWFD-020300、GWFD-010105、WSFD-109001 等已知正确的特性，确认没有引入错误

---

## 七、审计数据摘要

### 依赖关系审计统计
- 总交互行数: 778
- 成功提取: 736 (94.6%)
- 丢弃: 42 (5.4%)
  - 表头变体误入: ~15行
  - 功能名无ID: ~15行
  - 跨体系(SFFD等): ~5行
  - 占位符(NA/-): ~3行
  - 链接无ID: ~4行

### License缺失统计
- UDG: 80个 `has_overview=yes` 无License (其中部分确认无需License)
- UNC: 193个 `has_overview=yes` 无License (其中部分确认无需License)
- 已确认漏提取: WSFD-106101(3条)、WSFD-104401(2条)、WSFD-225003(1条)
