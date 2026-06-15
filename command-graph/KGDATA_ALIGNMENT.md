# kgdata 对齐分析

## 数据源发现

**UDG**: `output/extracted_UDG_Product_Documentation_CH_20.15.2/resources/infocenter_service/kgdata/entity/`
- `MML命令_1.csv` + `MML命令_2.csv` → **4,576 条命令**
- `命令参数_1.csv` ~ `命令参数_5.csv` → **15,970 条参数**

**UNC**: 无 kgdata（`infocenter_service/` 下只有 map/metadata/profile.xml，无 entity 目录）

已拷贝至 `command-graph/data/kgdata/` 目录。

---

## kgdata 命令属性（MML命令_*.csv）

CSV 格式：长表（每行一个属性），列：`Name, Attribute Name, Attribute Value, Entity Type`

| Attribute Name | 含义 | 覆盖率 | 值格式 |
|---|---|---|---|
| `命令码` | 英文命令名 | 100% | `VERB+KEYWORD`（如 `ADD+URR`） |
| `命令名称` | 中文名 | 100% | URL 编码中文 |
| `命令功能` | 功能描述 | 100% | URL 编码 HTML（含 NF 信息） |
| `注意事项` | 注意事项 | 100% | URL 编码 HTML |
| `使用实例` | 使用示例 | 100% | URL 编码 HTML |
| `操作用户权限` | 权限级别 | 95% | URL 编码文本 |
| `输出结果说明` | 输出说明 | 49% | URL 编码 HTML |
| `_topic_id` | 唯一ID | 100% | `CONCEPT_xxxxx` 或 `MMLREF_xxxxx` |
| `_topic_path` | HTML源文件路径 | 100% | `pid_bookmap_xxx##MML/Document/add_urr.html` |
| `_synonyms` | 同义词 | 100% | `##` 分隔的列表 |
| `self_name` | 全名 | 100% | `VERB+KEYWORD（中文名）` |

---

## kgdata 参数属性（命令参数_*.csv）

| Attribute Name | 含义 | 覆盖率 | 值格式 |
|---|---|---|---|
| `参数标识` | 英文参数名 | 99% | 如 `URRNAME` |
| `参数名称` | 中文参数名 | 99% | URL 编码 |
| `参数说明` | 完整参数说明 | 99% | URL 编码 HTML（含可选必选、前提条件、取值范围等） |
| `MML命令` | 所属命令 | 100% | `VERB+KEYWORD`（如 `ADD+URR`） |
| `参数ID` | 命令:参数 | 100% | `VERB+KEYWORD：PARAMNAME` |
| `_topic_id` | 唯一ID | 100% | 同命令的 topic_id |
| `_topic_path` | HTML源文件路径 | 100% | 同命令的 topic_path |
| `_synonyms` | 同义词 | 100% | `##` 分隔 |

---

## 与 MD 文件的映射

kgdata 的 `_topic_path` 指向 HTML 源文件：`MML/Document/add_urr.html`
MD 文件名格式：`增加URR（ADD URR）_82837629.md`

映射关系：kgdata `_topic_id` ↔ MD 文件名中的数字 ID（如 `CONCEPT_0182837629` → `_82837629`）

**绑定方式**: 通过 `_topic_id` 的后缀数字匹配 MD 文件名中的 `_数字` 部分。

---

## 与我们的 schema 对齐方案

### Step 1 命令表对齐

| schema 字段 | kgdata 来源 | 对齐逻辑 |
|---|---|---|
| `product` | 无 | 硬编码 `"UDG"` |
| `version` | 无 | 从目录名提取 `"20.15.2"` |
| `command_name` | `命令码` | `ADD+URR` → 替换 `+` 为空格 → `ADD URR` |
| `verb` | `命令码` | 拆分第一部分 |
| `object_keyword` | `命令码` | 拆分第二部分 |
| `command_name_zh` | `命令名称` | URL decode |
| `category_path` | `_topic_path` | HTML 路径中无分类，需从 `mml_index_ch.html` 或目录结构补充 |
| `file_path` | `_topic_id` | 通过 topic_id 数字后缀匹配到 MD 文件路径 |

**新增可绑定字段**（从 kgdata 直接获取，不再自己解析正文）：

| 字段 | kgdata 来源 | 说明 |
|---|---|---|
| `topic_id` | `_topic_id` | 唯一标识 |
| `command_function` | `命令功能` | URL decode + strip HTML tags |
| `notes` | `注意事项` | URL decode + strip HTML tags |
| `permission` | `操作用户权限` | URL decode |
| `examples` | `使用实例` | URL decode + strip HTML tags |
| `html_source_path` | `_topic_path` | 原始 HTML 路径 |

### Step 2 参数表对齐

| schema 字段 | kgdata 来源 | 对齐逻辑 |
|---|---|---|
| `parameter_name` | `参数标识` | 直接用 |
| `parameter_name_zh` | `参数名称` | URL decode |
| `description_raw` | `参数说明` | URL decode + strip HTML tags → 得到与 MD 相同的纯文本 |
| `command_name` | `MML命令` | `ADD+URR` → `ADD URR` |
| `topic_id` | `_topic_id` | 唯一标识 |

参数说明的子字段拆分（可选必选、前提条件、取值范围等）逻辑与 MD 版本完全一致，因为文本内容相同。

---

## 建议执行方案

1. **UDG**: 重写 step1 从 kgdata CSV 直接加载，不再扫描 MD 文件
2. **UNC**: 保持从 MD 文件解析（因为无 kgdata）
3. **file_path 绑定**: UDG 通过 `_topic_id` 数字后缀 → 匹配 MD 文件名中的数字 ID
4. 两者输出统一格式的 CSV，字段对齐

## 待确认

- UDG 的 `category_path` 用目录结构还是 `mml_index_ch.html` 的官方分类？
- `command_function` / `notes` / `examples` 这些正文类字段是否需要？还是保持 step1 只做元数据？
