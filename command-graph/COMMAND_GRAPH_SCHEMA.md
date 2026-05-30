# Command Graph Schema — UDG 20.15.2

## 1. 概述

命令图谱是三层配置图谱的底层基础层，将 MML 命令体系建模为可生成、可核查的配置对象网络。

**构建范围**: UDG 20.15.2 产品文档
**构建方法**: 代码抽取（命令/参数/配置对象）+ LLM语义抽取（关系）

## 2. 数据规模

| 数据类型 | 记录数 |
|---------|--------|
| 命令 (Command) | 4580 |
| 参数 (Parameter) | 14941 |
| 枚举值 (EnumValue) | 7930 |
| 配置对象 (ConfigObject) | 2267 |
| 命令组 (CommandGroup) | 4577 |
| 语义关系 (Relationship) | 12617 |

## 3. 节点类型

### 3.1 Command（命令）

每个 MML 命令对应一个节点。

| 字段 | 类型 | 说明 |
|------|------|------|
| command_id | string | 唯一标识 (hash) |
| command_name | string | MML命令名 (如 MOD NGM2MPLCY) |
| operation_verb | enum | 操作动词 |
| command_object_name | string | 命令对象名 |
| command_title_zh | string | 中文标题 |
| applicable_nf | string | 适用NF |
| description | text | 命令功能描述 |
| notes | text | 注意事项 |
| permissions | text | 操作权限 |
| service_category | string | 一级分类 |
| service_domain | string | 二级分类 |
| config_object_area | string | 三级分类 |

**操作动词分布**:
- LST: 1153
- DSP: 967
- RMV: 615
- ADD: 580
- SET: 556
- MOD: 407
- RTR: 89
- ACT: 24
- STR: 19
- RST: 16
- CLR: 14
- LCK: 10
- SYN: 9
- STP: 9
- SWP: 5
- DEA: 5
- DEL: 1
- GET: 1

### 3.2 Parameter（参数）

命令参数节点。

| 字段 | 类型 | 说明 |
|------|------|------|
| param_id | string | 唯一标识 (hash) |
| command_name | string | 所属命令 |
| param_identifier | string | 参数标识 (如 SUBRANGE) |
| param_name_zh | string | 参数中文名 |
| required_type | enum | 必选参数/可选参数/条件必选参数/条件可选参数 |
| condition_raw | text | 条件说明原文 |
| meaning | text | 参数含义 |
| data_source | string | 数据来源 |
| value_range_raw | text | 取值范围原文 |
| value_type | enum | 值类型 |
| default_value_raw | text | 默认值原文 |
| config_principle_raw | text | 配置原则原文 |
| has_enum_values | boolean | 是否有枚举值 |
| condition_deps_raw | json | 条件依赖关系 |

**值类型分布**:
- integer_range: 8819
- enum: 4003
- ip_address: 1039
- boolean: 392
- other: 365
- string: 314
- unknown: 9

**必选/可选分布**:
- 可选参数: 6011
- 必选参数: 5178
- 条件必选参数: 2111
- 条件可选参数: 1641

### 3.3 ConfigObject（配置对象）

通过命令名归纳的配置对象，同对象名的不同操作构成 CRUD 命令族。

| 字段 | 类型 | 说明 |
|------|------|------|
| object_id | string | 唯一标识 (hash) |
| object_name | string | 配置对象名 (如 FILTER) |
| object_name_zh | string | 中文名 |
| command_count | int | 包含的命令数 |
| has_full_crud | boolean | 是否有完整 CRUD |
| parameter_count | int | 参数总数 |
| create/read/update/delete_commands | json | 各角色命令列表 |

### 3.4 EnumValue（枚举值）

枚举型参数的取值选项。

| 字段 | 类型 | 说明 |
|------|------|------|
| param_id | string | 所属参数 |
| enum_value | string | 枚举值 (如 ENABLE) |
| enum_label | string | 中文标签 |
| enum_description | string | 说明 |

## 4. 关系类型

通过 LLM 语义抽取发现的关系，每条关系包含 evidence_text（原文引用）。

| 关系类型 | 数量 | 说明 |
|---------|------|------|
| param_condition | 4610 | 参数条件依赖 |
| cmd_reference | 3319 | 命令引用关系 |
| effect_timing | 2770 | 生效时机 |
| cmd_prerequisite | 973 | 命令前置依赖 |
| risk_level | 552 | 风险等级 |
| config_object_hierarchy | 242 | 配置对象层级 |
| param_exclusion | 151 | 参数互斥 |

## 5. 层级结构

命令图谱的分类层级来自产品文档目录结构：

```
UDG MML命令/
├── ├── 平台服务管理 (2920)
├── 用户面服务管理 (1506)
├── TCP优化服务管理 (48)
├── 业务报表管理 (38)
├── SFIP管理 (33)
├── 智能板管理 (26)
├── CoreMind操作维护命令 (2)
├── NAT服务管理 (2)
├── SAPO服务管理 (2)
├── 集中配置命令说明 (2)
├──  (1)
```

## 6. 构建方法

| 数据 | 方法 | 抽取工具 |
|------|------|---------|
| 命令元数据 | 代码抽取 | step2_parse_commands.py |
| 参数详情 | 代码抽取 | step3_extract_parameters.py |
| 配置对象 | 代码发现 | step4_discover_config_objects.py |
| 语义关系 | LLM抽取+审查 | step5/step6 (DeepSeek) |
