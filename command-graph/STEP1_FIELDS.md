# Step 1: 命令扫描 — 字段抽取说明

## 数据源

| 产品 | 扫描路径 |
|------|----------|
| UDG | `output/UDG_Product_Documentation_CH_20.15.2/OM参考/命令/UDG MML命令/` |
| UNC | `output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/` |

- 扫描所有 `.md` 文件，跳过文件名含 `命令申明` / `声明` 的文件
- **不解析文件正文**，仅从文件名和目录结构提取元数据

输出文件：`command-graph/data/raw_commands.csv`

---

## 唯一键

`product` + `version` + `command_name` 三字段组合唯一确定一条命令。

---

## 字段说明

### 1. `product` — 产品

**来源**: 硬编码，由扫描目录决定
**逻辑**: UDG 目录 → `"UDG"`，UNC 目录 → `"UNC"`
**示例**: `UDG`、`UNC`

---

### 2. `version` — 版本

**来源**: 硬编码
**逻辑**: 当前写死 `"20.15.2"`
**问题**: 多版本时需从目录名正则提取

---

### 3. `command_name` — 命令名

**来源**: 文件名
**逻辑**: 拼接 `{verb} {object_keyword}`
**示例**: `ADD URR`、`MOD PCCPOLICYGRP`

---

### 4. `verb` — 动词

**来源**: 文件名，括号内第一个英文单词
**逻辑**: 正则 `(.+?)[（(]\s*([A-Z]+)\s+([A-Z0-9_]+)\s*[）)]` → group(2)
**文件名格式**: `中文名（VERB KEYWORD）_数字ID.md`
**示例**:
- `增加URR（ADD URR）_82837629.md` → `ADD`
- `修改CSDB(MOD DBRUMEM)_04873821.md` → `MOD`（半角括号）
- `NGPING（NGPING）_09587930.md` → `EXC`（单字命令 fallback）

---

### 5. `object_keyword` — 对象关键词

**来源**: 文件名，括号内 VERB 后的英文单词
**逻辑**: 同上正则 → group(3)
**示例**: `URR`、`URRGROUP`、`PCCPOLICYGRP`
**覆盖**: 4241 个不同的 object_keyword

---

### 6. `command_name_zh` — 命令中文名

**来源**: 文件名，括号前的中文部分
**逻辑**: 同上正则 → group(1)
**示例**: `增加URR`、`修改CSDB RU内存信息`

---

### 7. `category_path` — 分类路径

**来源**: 目录结构
**逻辑**: 去掉 src_root 前缀，取中间目录层级，输出 JSON 数组
**src_root**:
- UDG: `.../UDG MML命令/`
- UNC: `.../UNC MML命令/`
**示例**: `["用户面服务管理", "业务控制策略", "计费控制", "使用率上报规则"]`

---

### 8. `file_path` — 源文件相对路径

**来源**: 文件系统
**逻辑**: 相对于 `output/` 目录的路径
**示例**: `UDG_Product_Documentation_CH_20.15.2/OM参考/命令/UDG MML命令/用户面服务管理/.../增加URR（ADD URR）_82837629.md`

---

## 文件名解析规则

**标准格式**: `中文名（VERB KEYWORD）_数字ID.md`

| 变体 | 示例 | 处理 |
|------|------|------|
| 全角括号 | `增加URR（ADD URR）_xxx.md` | 正常 |
| 半角括号 | `修改CSDB(MOD DBRUMEM)_xxx.md` | 正常 |
| 括号内尾空格 | `设置信息(SET INFO )_xxx.md` | 容错 |
| 单字命令 | `NGPING（NGPING）_xxx.md` | verb=EXC, keyword=原名 |
| 非命令文件 | `集中配置命令列表_xxx.md` | 跳过（9个） |

---

## 统计

- 总计: 13,075 条命令（UDG 4,577 + UNC 8,498）
- 解析失败: 9 条（均为说明性文件，不是命令）
- 重复: 0
- 动词种类: 56 种

## 已知问题

1. **version 硬编码** — 多版本需扩展
2. **单字命令 verb=EXC** — 是否有更合理的分类？
3. **UDG/UNC 分类体系不同** — 同一命令的 category_path 不同
