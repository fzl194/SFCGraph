# 命令图谱 Schema

> 版本: v0.8
> 定位: 云核心网 MML 命令的配置数字孪生本体，表达命令、参数、配置对象、规则及其关系。
> 用途: 支撑配置生成、语法核查、语义核查、关系追溯。
> 约束: 本文档定义对象、关系和核心属性结构。枚举范围（如 rule_type、object_kind 等）随场景扩展逐步补充。

---

## 1. 设计原则

1. 命令图谱分两层理解：**配置对象层**（配了什么）和**命令语法层**（怎么配），但统一为一套图谱。
2. 对象层级从上到下：**配置对象 → 命令 → 参数**。
3. 跨层只有相邻层有关系：配置对象 ↔ 命令，命令 ↔ 参数。配置对象与参数之间没有直接关系。
4. 同层内部对象之间可以有关系。
5. 配置对象的属性细节不在 ConfigObject 上重复存储，通过图关系（`creates` → `has_parameter`）从 CommandParameter 获取，不做两套定义。
6. 规则可以自由挂载在任意层任意粒度上：命令、参数、配置对象、关系、属性。
7. 命令、参数从产品文档中提取；配置对象从命令脚本执行结果中提取；规则从注意事项和参数说明中提取。

---

## 1A. 版本治理模型（方案 G）

命令/参数/关系在不同网元、不同版本下会有差异（新增、废弃、关系变化、取值漂移）。不采用"跨版本抽象合并"的复杂模型，改为**物理分层 + 逻辑同名**：

| 维度 | 约定 |
| --- | --- |
| 分层键 | `网元类型 × 版本`，如 `UDG@20.13.2`、`UNC@20.15.2`。每层是一份**完整的命令图谱实例**（命令、参数、对象、规则、关系全部原样进，不做跨层合并去重）。 |
| 逻辑锚点 | 节点用**命令本文名**做跨层标识，如 `ADD URR`、`ADD_URR.URRNAME`。同一逻辑名在不同层是不同实例，但可被上层用同一个名字引用。 |
| 上层关联 | `ConfigTask` / `Feature` / 业务方案**不版本化、不网元化**，通过命令本文名 `invokes`。核查/生成时按当前目标 `网元@版本` 路由到对应实例层。 |
| 跨层共性 | 当下不去重合并；版本演进分析（某参数哪版新增）靠层间 diff 工具，不靠 schema。 |

**实例键格式**：`{nf}@{version}@{ObjectType}@{local_name}`（四段带类型，全 `@` 分隔），如 `UDG@20.15.2@MMLCommand@ADD URR`、`UDG@20.15.2@CommandParameter@ADD URR:URRNAME`、`UDG@20.15.2@ConfigObject@URR`（参数 local_name 内部用 `:` 分命令/参数名）。这是图谱主键，也是与传统表关联的连接键。

---

## 1B. 存储模型

图谱采用**图（对象/属性/关系）+ 传统表混合存储**，两者用同一稳定键连接。

| 存储方式 | 承载内容 |
| --- | --- |
| **图谱（节点/边属性）** | 默认存储方式。对象身份、语义、结构性归属、取值约束、关系及其边属性；核查执行细节（脚本/表达式/错误提示）归 CommandRule（见 §3.5）。 |
| **传统表** | 仅当数据是"一对多、子记录结构复杂、不适合建模为关系边"时使用。用实例键连回图谱。 |

> 关键判断：**能作为节点/边属性的全部作为属性**，不要无谓拆表。例如参数的枚举值是 list 属性、默认值是 string 属性、参数依赖的**触发条件**（触发参数/取值/逻辑）挂在 `depends_on` 边属性上；而**核查执行**（脚本/表达式/错误提示）属 CommandRule，由 `CommandRule --governs--> 该边` 承载（见 §3.5）。表只用于如软参数（SOFTPARA 一命令对应几十条 BITNUM 记录）这类一对多长表。

---

## 2. 两个视图

看板提供两个视图，从不同角度切入同一套知识：

### 2.1 命令视图

以命令为中心，展开参数和参数依赖。

```
ADD URR
  ├─ URRNAME (必选)
  ├─ URRID (必选)
  ├─ USAGERPTMODE (必选)
  │    └─ ONLMETERINGTYPE (条件可选: USAGERPTMODE=ONLINE)
  ├─ RG (条件可选)
  └─ ...
  operates_on → ConfigObject URR
```

### 2.2 配置对象视图

以配置对象为中心，展开属性和对象间关系。

```
ConfigObject URR
  ├─ URRNAME (标识)
  ├─ URRID
  ├─ USAGERPTMODE
  ├─ ONLMETERINGTYPE (条件出现: USAGERPTMODE=ONLINE)
  └─ RG
  ← contained_by ── URRGROUP
  ← refers_to ───── PCCPOLICYGRP (via URRGROUPNAME)
```

---

## 3. 对象定义

### 3.1 对象总表

| 对象 | 中文名 | 定位 | 层级 |
| --- | --- | --- | --- |
| `ConfigObject` | 配置对象 | 命令脚本执行后产生的稳定配置对象 | 配置对象层 |
| `MMLCommand` | MML 命令 | 一条正式 MML 命令 | 命令语法层 |
| `CommandParameter` | 命令参数 | 命令的参数 | 命令语法层 |
| `CommandRule` | 命令规则 | 命令层约束，可挂载在任意粒度 | 跨层 |

### 3.2 ConfigObject

配置对象是命令族共同操作的稳定语义实体，是命令图谱的**配置语义层锚点**。它是轻量节点——只承载身份、标识、唯一性与分类；属性细节不在此存储，通过图遍历从 CommandParameter 获取。

**对象集边界**：所有 `MMLCommand.object_keyword` 都建 ConfigObject（按 object_keyword 聚合命令族，一族一对象）——含配置实体、查询目标、动作，一律纳入，用 `object_kind` 区分，不靠"是否配置命令"筛除。

**实例键**：`{nf}@{version}@ConfigObject@{object_name}`（四段带类型，见 §1A），如 `UDG@20.15.2@ConfigObject@URR`。

**节点属性：**

| 分组 | 字段 | 类型 | 必选 | 标签空间 / 来源 |
| --- | --- | --- | --- | --- |
| 身份 | `object_id` | string | 是 | 实例键 `{nf}@{version}@ConfigObject@{object_name}`，派生 |
| | `object_name` | string | 是 | 对象英文标识 = 命令族 `object_keyword`（按它聚合，空值跳过） |
| | `object_name_zh` | string | 否 | 中文名 = `command_name_zh` 去动词前缀（增加/修改/删除/查询/显示/设置/配置/激活/清除/刷新/加载…最长匹配）；标 `_auto` 待校准 |
| 分类 | `object_kind` | enum | 是 | 行为结构种类，枚举 `{entity, global_setting, query_target, action, binding}`（判定见 3.2.1） |
| | `applicable_nf` | list[string] | 否 | 适用网元 = 族命令 `applicable_nf` 并集（NF 名开放枚举） |
| 标识 | `identifier_parameters` | list[string] | 否 | **定位参数** = 内网 **MOD 规则"索引参数"列**（MOD 缺失时用 RMV 规则"索引参数"列）；MOD/RMV/LST 用它定位一条记录 |
| | `uniqueness_keys` | list[list[string]] | 否 | **唯一性键** = 内网 **重复规则"重复检查"列**（按 ADD 命令名关联），如 `[[RULENAME,POLICYTYPE]]`；支持多组 |
| 属性 | `attribute_names` | list[string] | 否 | 可配置属性名清单 = 族内 ADD∪MOD∪SET 命令参数名，**去重**；不含 LST/DSP `output_fields`（查询输出结构，留命令层，非配置属性）|
| 元数据 | `description` | string | 否 | 对象说明 = 族内 ADD 命令 `command_function` 优先（无 ADD → MOD → 任意配置类命令） |
| | `status` | enum | 是 | `{draft, active, deprecated}`（builder 默认 active，不推断废弃） |
| | `source_evidence_ids` | list[string] | 否 | 来源证据 = 族命令 `source_evidence_ids` 并集去重 |

> **属性细节不在 ConfigObject 存储。** 类型、取值范围、默认值、枚举、约束等，通过图遍历从 CommandParameter 获取，避免两套定义（见 §1 第 5 条）。`attribute_names` 只存**名清单**（复用已抽的 `command_parameters.parameter_name` 聚合，不重新抽；**不含** LST/DSP 输出字段——那是查询输出结构，不是配置属性，留在 `MMLCommand.output_fields`）；配置生成时按名知道对象由哪些属性构成，再沿关系到参数层取每个属性的细节。
>
> **`identifier_parameters` 与 `uniqueness_keys` 都来自内网规则专门表**（非从参数 required_mode 推断）：identifier ← MOD 规则"索引参数"，uniqueness ← 重复规则"重复检查"。前者回答"如何定位一条记录"，后者回答"两条记录算不算重复"。多数对象两者一致；RULE 等不同——identifier 可能是 `RULENAME`，uniqueness 是 `[RULENAME, POLICYTYPE]`。
>
> **数据现实**（builder 照实产出，不编造）：`applicable_nf` 命令层覆盖率 UDG 35% / UNC 66%，未覆盖的对象为空 list；`attribute_names` / `identifier_parameters` / `uniqueness_keys` 依赖参数表 + 内网规则表（MOD/重复/RMV），全量内网规则文件接入后才完整，子集数据时部分对象为空 list。

#### 3.2.1 object_kind 枚举（数据驱动：按命令族行为模式 + 命名判定）

判定按优先级从上到下，命中即停（不按对象名后缀猜）：

| 优先级 | kind | 判定条件 | 典型 verb 画像 |
| --- | --- | --- | --- |
| 1 | `binding` | 命名含 `BIND` **且** 族内有 ADD/RMV（增删行为） | ADD/RMV/LST（±MOD） |
| 2 | `query_target` | 族内命令仅 LST/DSP（纯查询运行态：会话/统计/计数） | LST/DSP |
| 3 | `action` | verb 既非配置(ADD/MOD/DEL/SET)也非查询(LST/DSP)——动作/操作兜底 | CLR/SYN/RTR/STP/LOD/SWP/ACT/DEA/SAV/ULD… |
| 4 | `global_setting` | 有 SET 且无 ADD/MOD/DEL/RMV（全局开关/参数，多单例） | SET（±LST/DSP） |
| 5 | `entity` | 含 ADD/MOD/DEL/RMV（**默认兜底**） | ADD/MOD/RMV/LST |

**5 个枚举值**：`entity` / `global_setting` / `query_target` / `action` / `binding`。

> - `batch_op`（命名 `xxxALL` 的批量清理/查询）**不独立成 kind**，挂对应 entity 做"批量命令"标记。
> - `binding` 双条件：命名含 BIND 但只 SET / 只查询的（如 `URRGRPBINDING`=SET、`LBTNBINDPLY`=DSP）按行为归 `global_setting` / `query_target`，不强归 binding。
> - 旧版的 `group` / `profile` / `filter` **取消**——它们行为上就是 entity，"组/档案/过滤器"的层级用对象间关系（contains/refers_to，见 §4.5）表达，不靠 kind。
> - 实测分布（UDG+UNC 5818 个对象族）：entity 34% / global_setting 24% / query_target 32% / action 8% / binding 2%。

### 3.3 MMLCommand

基于真实产品 MML 命令文档构建，覆盖七大章节板块：**命令功能 / 注意事项 / 操作用户权限 / 参数说明 / 使用实例 / 输出结果说明 / 参考信息**。字段分两层：
- **原始**（章节级）= builder 直接从 md 章节抽取的整段/派生键，是知识的源头；
- **派生**（章节内）= 从原始字段的非结构化文本中解析出的结构化字段，初始可空，逐步填充。

**节点属性：**

| # | 字段 | 层级 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- | --- | --- |
| 1 | `nf` | 原始 | string | 是 | 网元类型，命令行 `--nf` 参数，如 `UDG` |
| 2 | `version` | 原始 | string | 是 | 产品文档版本，命令行 `--version` 参数，如 `20.15.2` |
| 3 | `command_id` | 原始 | string | 是 | 实例键 `{nf}@{version}@MMLCommand@{command_name}`，如 `UDG@20.15.2@MMLCommand@ADD URR` |
| 4 | `command_name` | 原始 | string | 是 | 命令全称，如 `ADD URR` |
| 5 | `command_name_zh` | 原始 | string | 否 | 命令中文名，如"增加URR" |
| 6 | `verb` | 原始 | string | 是 | 动词，开放枚举（约 56 种），如 `ADD/MOD/SET/RMV/LST/DSP` |
| 7 | `object_keyword` | 原始 | string | 是 | 命令对象关键字，如 `URR` |
| 8 | `command_function` | 原始 | string | 否 | "命令功能"章节全文 |
| 9 | `notes` | 原始 | list[string] | 否 | "注意事项"章节原文 |
| 10 | `permission_text` | 原始 | string | 否 | "操作用户权限"章节整段（含网管/本地权限） |
| 11 | `parameter_description` | 原始 | string | 否 | "参数说明"章节整段（CommandParameter 从此派生） |
| 12 | `usage_examples` | 原始 | list[string] | 否 | "使用实例"章节 |
| 13 | `output_description` | 原始 | string | 否 | "输出结果说明"章节整段 |
| 14 | `reference_info` | 原始 | string | 否 | "参考信息"章节整段 |
| 15 | `category_path` | 原始 | list[string] | 否 | md 目录分类路径 |
| 16 | `status` | 原始 | enum | 是 | `draft/active/deprecated` |
| 17 | `source_evidence_ids` | 原始 | list[string] | 否 | 来源证据（md 相对项目根路径，兼作追溯） |
| 18 | `command_category` | 派生 | enum | 否 | verb→`配置/查询/动作/调测类`，决定是否承载 ConfigObject 关系 |
| 19 | `applicable_nf` | 派生 | list[string] | 否 | 适用 NF，从 command_function 提取 |
| 20 | `max_records` | 派生 | integer | 否 | 最大记录数规格（如 URR `65000`），从 notes 提取 |
| 21 | `permission_groups` | 派生 | list[string] | 否 | 权限组 `G_1/G_2/G_3`，从 permission_text 解析 |
| 22 | `output_ref_command` | 派生 | string | 否 | 输出引用命令，从 output_description 解析 |
| 23 | `is_dangerous` | 派生 | boolean | 否 | 是否高危命令，从 notes/功能提取 |
| 24 | `effect_mode` | 派生 | enum | 否 | 生效方式 `立即/对新流/对新用户/延迟/其他`，从 notes 提取 |
| 25 | `spec_threshold` | 派生 | object | 否 | 超阈值告警 `{alarm_id, ratio, recover_ratio, modify_command}`，从 notes 提取 |
| 26 | `initial_values` | 派生 | map | 否 | 系统初始记录（参数名→初始值），从 notes 提取（SET 特有） |
| 27 | `output_fields` | 派生 | list[object] | 否 | 输出字段表 `{field, description}`，从 output_description 解析 |

> **层级原则**：`原始`字段是源头（builder 章节/派生键），`派生`字段从原始字段解析、初始可空逐步填充。经审视保留 **10 个派生字段**（见下），删去 `command_summary`/`effect_delay`/`danger_warning`/`performance_impact`/`applicability_constraints`（原始整段 notes/command_function 已承载，下游无需结构化直接用）。10 个派生字段**已全部抽取入 jsonl**（command_category/applicable_nf/max_records/permission_groups/output_ref_command/is_dangerous/effect_mode/spec_threshold/initial_values/output_fields）。
>
> **10 个派生字段含义**：
> - `command_category`（verb→配置/查询/动作/调测类）：决定命令是否承载 ConfigObject 关系（配置类才 creates/modifies）；用于对象推导与检索分类。
> - `applicable_nf`（command_function→适用网元）：按 NF 过滤命令（如 PGW-U/UPF vs SMF），配置生成只处理本 NF 命令。
> - `effect_mode`（notes→生效方式）：配置后核查"立即/对新流/对新用户/延迟生效"。
> - `max_records`（notes→最大记录数）：配置生成防超规格上限。
> - `spec_threshold`（notes→超阈值告警）：运维核查告警 ID/比例/修改命令。
> - `initial_values`（notes→系统初始值）：SET 全局参数的初始值，配置/回退参考。
> - `is_dangerous`（notes/功能→高危标记）：高危命令配置时警告/二次确认。
> - `permission_groups`（permission_text→G_x 权限组）：权限核查（某操作需哪级权限）。
> - `output_fields`（output_description→输出字段表）：查询类命令的输出结构，程序解析查询结果。
> - `output_ref_command`（output_description→引用命令）：建立命令间"参见 XXX"引用关系。
>
> 命令分类与对象关系：配置类命令（ADD/MOD/DEL/SET/RMV）有 `creates/modifies/deletes/sets/binds` 关系；查询类（LST/DSP）用 `queries`；动作类（SWP/RST）与调测类通常无 ConfigObject 关系。

### 3.4 CommandParameter

命令参数是命令图谱的最小粒度节点。存储原则见 §1B：默认全部作为节点/边属性，能挂属性的全挂上。

> 设计取舍：在方案 G（§1A）下，每层 `网元@版本` 是完整实例快照，参数的取值/约束随版本原样落到该层属性中，无需跨版本抽象或外挂拆分。内网参数表的字段几乎全部作为节点属性收下。

| 字段 | 类型 | 必选 | 说明 / 来源 |
| --- | --- | --- | --- |
| `parameter_id` | string | 是 | 参数实例键，规则为 `{nf}@{version}@CommandParameter@{command_name}:{parameter_name}`，如 `UDG@20.15.2@CommandParameter@ADD URR:URRNAME` |
| `nf` | string | 是 | 网元类型，取自内网参数表 `网元类型` 列，如 `UDG` |
| `version` | string | 是 | 网元版本，取自内网参数表 `网元版本` 列，如 `20.13.2` |
| `native_parameter_id` | integer | 否 | 参数在命令中的顺序号（内网参数ID），如 `1`、`3` |
| `command_id` | string | 是 | 所属命令实例键，规则为 `{nf}@{version}@MMLCommand@{command_name}`，如 `UDG@20.15.2@MMLCommand@ADD URR` |
| `parameter_name` | string | 是 | 参数标识，取自内网参数表 `参数标识` 列，如 `URRNAME` |
| `parameter_name_zh` | string | 否 | 参数中文名，取自内网参数表 `参数名称` 列 |
| `data_type` | string | 否 | 数据类型内网原值，取自内网参数表 `参数类型` 列 |
| `required_mode` | enum | 否 | `必选 / 可选 / 条件必选 / 条件可选`，取自内网参数表 `可必选` 列 |
| `condition_for_required` | string | 否 | 可必选性的前提条件，取自内网参数表 `条件` 列 |
| `enum_values` | list[string] | 否 | 枚举值列表，取自内网参数表 `枚举` 列 |
| `default_value` | string | 否 | 默认值，取自内网参数表 `默认值` 列 |
| `max_value` | string | 否 | 最大值，取自内网参数表 `最大值` 列 |
| `min_value` | string | 否 | 最小值，取自内网参数表 `最小值` 列 |
| `range_interval` | string | 否 | 取值区间，取自内网参数表 `区间` 列 |
| `max_length` | integer | 否 | 最大长度，取自内网参数表 `最大长度` 列 |
| `min_length` | integer | 否 | 最小长度，取自内网参数表 `最小长度` 列 |
| `length` | integer | 否 | 固定长度，取自内网参数表 `长度` 列 |
| `value_range` | string | 否 | 取值范围描述，取自内网参数表 `取值范围` 列 |
| `bitfield` | string | 否 | 位域说明，取自内网参数表 `位域` 列 |
| `string_format` | string | 否 | 字符串格式，取自内网参数表 `字符串格式` 列 |
| `regex_id` | string | 否 | 正则 id，取自内网参数表 `正则id` 列 |
| `case_sensitive` | boolean | 否 | 是否区分大小写，取自内网参数表 `是否区分大小写` 列 |
| `comparison_operator` | string | 否 | 比较关系，取自内网参数表 `比较关系` 列 |
| `forbidden_values` | list[string] | 否 | 禁输值，取自内网参数表 `禁输值` 列 |
| `conditional_range` | string | 否 | 条件区间，取自内网参数表 `条件区间` 列 |
| `inheritance` | enum | 否 | `新增 / 继承`，取自内网参数表 `继承关系` 列 |
| `description` | string | 否 | 参数说明原文，取自内网参数表 `说明` 列 |

**关系边（边属性随边存储）：**

`CommandParameter --depends_on--> CommandParameter`：参数间依赖与引用，含跨命令引用。内网参数表的"关联命令/关联参数"、第 3 类"参数和参数关系"表，均转化为此边。

| 边属性 | 类型 | 说明 / 来源 |
| --- | --- | --- |
| `condition_ref` | string | 触发参数名，如 `USAGERPTMODE` |
| `condition_logic` | enum | `等于 / 大于 / 小于 / 不等于 / 包含…`（默认等于） |
| `condition_value` | string | 触发取值，如 `ONLINE` |

**外挂表（仅一对多长表）：**

| 表 | 内容 | 连接键 |
| --- | --- | --- |
| 软参数表（SP 规则） | SOFTPARA / APNSOFTPARA 的 BITNUM 长表（一命令对应数十条记录） | `{nf}@{version}@MMLCommand@{命令名}` |

> 说明：`reference_target`（旧版参数引用配置对象的简写）已合并进 `depends_on` 边的语义，不再单列为节点字段。

### 3.5 CommandRule

命令图谱的**核查规则层**。把散落在对象/边里的静态知识激活为"配置生成/核查时要检验的规则"，并补充严重度、违反处置、核查表达式。来源：产品文档注意事项（notes）+ 内网重复规则 + 删除保护等约束。

**节点属性：**

| 分组 | 字段 | 类型 | 必选 | 说明 / 来源 |
| --- | --- | --- | --- | --- |
| 身份 | `rule_id` | string | 是 | 实例键 `{nf}@{version}@CommandRule@{rule_id}` |
| | `rule_name` | string | 是 | 规则名称 |
| 分类 | `rule_type` | enum | 是 | 规则类型（见 3.5.1） |
| | `scope_type` | enum | 是 | 作用粒度（见 3.5.2） |
| | `scope_ref` | string | 是 | 作用对象引用 |
| 逻辑 | `rule_logic` | string | 是 | 规则逻辑（自然语言） |
| | `check_expression` | string | 否 | 核查表达式，如 `equalsIgnoreCase` |
| | `check_script` | string | 否 | 核查脚本（groovy/JEXL） |
| 来源 | `rule_source_kind` | enum | 否 | `principle / config / design / ops / case / restriction` |
| | `rule_expression_mode` | enum | 否 | `explicit / implicit` |
| 处置 | `violation_effect` | string | 否 | 违反影响 |
| | `severity` | enum | 是 | `critical / warning / info` |
| | `error_msg_zh` | string | 否 | 违反提示（中文） |
| | `error_msg_en` | string | 否 | 违反提示（英文） |
| 元数据 | `status` | enum | 是 | `draft / active / deprecated` |
| | `source_evidence_ids` | list[string] | 否 | 来源证据 |

> **与对象/边属性的去重原则**：当某规则已由对象固有属性或边属性自然承载时，CommandRule **不重复存数值**，仅在需要独立的 severity / 核查逻辑 / 违反处置时建立。CommandRule 主要**独占**无自然归属的约束：`delete_constraint`、`consistency`、`parameter_mutex`、`cross_nf_sync`、`performance`。
>
> 关系：`CommandRule --governs--> MMLCommand / CommandParameter / ConfigObject / 关系边 / 属性`（见 §4.7）。

#### 3.5.1 rule_type 枚举（含主承载）

| 值 | 说明 | 主承载 | CommandRule 角色 |
| --- | --- | --- | --- |
| `uniqueness` | 唯一性约束 | `ConfigObject.uniqueness_keys` | 补核查/违反处置 |
| `existence_precondition` | 存在性前置 | `depends_on` 边强绑定 | 补核查 |
| `delete_constraint` | 删除保护 | — | **独占**（被引用对象禁删） |
| `consistency` | 一致性约束 | — | **独占**（多对象/多网元一致） |
| `cardinality` | 数量/规格约束 | `max_records` | 补超阈值告警 |
| `effect_scope` | 生效范围 | `effect_mode` | 补范围限定 |
| `parameter_dependency` | 参数条件依赖 | `depends_on` 边 | 一般不重复建 |
| `parameter_mutex` | 参数互斥 | — | **独占**（不能同时配置） |
| `ordering` | 顺序约束 | `must_precede/must_be_last` 边 | 一般不重复建 |
| `cross_nf_sync` | 跨网元同步 | — | **独占**（SMF/UPF 关键参数一致） |
| `performance` | 性能影响 | — | **独占**（如事件计费性能） |

#### 3.5.2 scope_type 枚举

| 值 | 说明 |
| --- | --- |
| `command` | 规则作用在命令上 |
| `parameter` | 规则作用在参数上 |
| `config_object` | 规则作用在配置对象上 |
| `relationship` | 规则作用在关系上 |
| `attribute` | 规则作用在属性上 |

---

## 4. 关系定义

### 4.1 关系层级原则

```text
配置对象层  ── 层内关系 ──→  配置对象层
    │
    │ (相邻层关系)
    ↓
命令层      ── 层内关系 ──→  命令层
    │
    │ (相邻层关系)
    ↓
参数层      ── 层内关系 ──→  参数层

规则层      ── governs ──→  任意层任意粒度
```

### 4.2 命令 → 参数（相邻层）

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `MMLCommand` | `has_parameter` | `CommandParameter` | 命令包含参数 |

### 4.3 配置对象 → 命令（相邻层）

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `MMLCommand` | `operates_on` | `ConfigObject` | 命令操作配置对象 |
| `MMLCommand` | `creates` | `ConfigObject` | ADD 命令创建对象 |
| `MMLCommand` | `modifies` | `ConfigObject` | MOD 命令修改对象 |
| `MMLCommand` | `deletes` | `ConfigObject` | DEL/RMV 命令删除对象 |
| `MMLCommand` | `sets` | `ConfigObject` | SET 命令设置对象属性 |
| `MMLCommand` | `binds` | `ConfigObject` | 绑定型命令建立对象间绑定 |
| `MMLCommand` | `queries` | `ConfigObject` | 查询类命令（LST/DSP）查询对象，不修改 |

### 4.4 参数 → 参数（层内，两类不同语义）

参数间有**两类不同**的依赖关系，语义不同，**不混用**（原 schema 都叫 depends_on，现拆开）：

#### 4.4.1 conditional_required（命令内条件依赖）

同一命令内，参数 P1 的**取值**决定参数 P2 的**必选性**（P2 是否要填）。

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `CommandParameter` | `conditional_required` | `CommandParameter` | 同命令内：P1=值 → P2 必选 |

边属性：

| 边属性 | 类型 | 说明 |
| --- | --- | --- |
| `condition_value` | string | 触发条件值，如 `ONLINE` |
| `condition_expression` | string | 完整条件表达式，如 `USAGERPTMODE=ONLINE` |
| `required_mode` | enum | 触发后 P2 必选性：`必选 / 条件必选` |

示例：

```text
[ADD URR] USAGERPTMODE (值=ONLINE) --conditional_required [USAGERPTMODE=ONLINE]--> ONLMETERINGTYPE (必选)
```

数据源：内网参数表的"条件"列（如 `{"3=IPV4": "必选"}`）；当前产物 `parameter_depends_on.jsonl`（建议 relation_type 由 depends_on 改为 conditional_required）。

#### 4.4.2 references（跨命令值引用）

跨命令，命令 A 的参数 X 的**值**必须**引用**命令 B 的参数 Y 的已存在值（外键 / 存在性约束）。

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `CommandParameter` | `references` | `CommandParameter` | 跨命令：A.X 的值引用 B.Y 的已存在值 |

边属性：

| 边属性 | 类型 | 说明 |
| --- | --- | --- |
| `source_condition` | string | 源参数触发条件（如 `ADD_FLTBINDFLOWF.FILTERNAME != null`）|
| `check_expression` | string | 核查逻辑（如 `.equalsIgnoreCase(...)`）|
| `binding_strength` | enum | `强绑定 / 弱绑定`（1 强 / 0 弱）|
| `cascade_delete` | boolean | 是否联动删除（删目标时联动删源）|

示例：

```text
[ADD FLTBINDFLOWF] FILTERNAME --references--> [ADD FILTER] FILTERNAME (值必须 = 已存在的 FILTER.FILTERNAME)
[ADD URRGROUP] UPURRNAME1/2/3、DOWNURRNAME1/2/3 --references--> [ADD URR] URRNAME
```

数据源：内网**参数引用规则**（`内网-参数引用规则.csv`，海量、按网元版本、可能是 excel）；产物 `parameter_references.jsonl`。

> **两类区别**：conditional_required 回答"P2 什么时候必填"（同命令，P1 取值改 P2 必选性）；references 回答"X 的值从哪来"（跨命令，X 引用 Y 的已存在值）。
>
> **推导对象关系**：把 references 的源/目标参数聚合到所属 ConfigObject，可得 §4.5 的 `refers_to`（FLTBINDFLOWF.FILTERNAME→FILTER.FILTERNAME ⇒ ConfigObject `FLTBINDFLOWF refers_to FILTER`，via_parameter=FILTERNAME）。

### 4.5 配置对象 → 配置对象（层内）

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `ConfigObject` | `has` | `ConfigObject` | **拥有/聚合**：子依附于父，生命周期绑定，父删则子失效（如 APN has 子配置） |
| `ConfigObject` | `contains` | `ConfigObject` | 结构包含（子可独立存在，无生命周期绑定） |
| `ConfigObject` | `refers_to` | `ConfigObject` | 引用独立对象（如 RULE 引用 PCCPOLICYGRP；URRGROUP 引用 URR）。**数据源：从 §4.4.2 references 聚合推导**（via_parameter）|
| `ConfigObject` | `depends_on` | `ConfigObject` | 依赖关系（如 PCCPOLICYGRP 依赖 URRGROUP） |
| `ConfigObject` | `conflicts_with` | `ConfigObject` | 冲突/互斥 |
| `ConfigObject` | `composed_by` | `ConfigObject` | 组合关系（如 PCCPOLICYGRP 由多个子对象组合） |

**`has` 关系（聚合根 + 依附实体，生命周期级联）边属性：**

| 边属性 | 类型 | 说明 |
| --- | --- | --- |
| `cascade_on_delete` | enum | 父删除时子的处置：`删除 / 失效 / 无影响` |
| `via_parameter` | string | 通过哪个参数建立父子（如父.APN ↔ 子.APN） |
| `cardinality` | string | 数量约束（一父下最多多少子） |

> **`has` 与 `contains`/`refers_to` 的区别**：`has` 是强生命周期绑定——子不能脱离父独立存在，父删子灭（对应 DDD 聚合根 + 依附实体）；`contains` 是结构归属但子可独立；`refers_to` 是引用独立对象。
>
> **配置块 = 以聚合根为顶点、沿 `has` 展开的对象子树**（如 APN 配置块 = APN + 其 has 的全部子配置），不另建对象类型。
>
> 与内网规则呼应：内网"参数和参数关系"表中的 `是否联动删除`（参数级 `cascade_delete`）是对象级 `has` 关系的投影。
>
> 其余对象间关系边按需携带属性描述语义（如引用通过哪个参数、包含的数量约束等）。

### 4.6 命令 → 命令（层内）

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `MMLCommand` | `must_precede` | `MMLCommand` | 执行顺序约束（如 ADD URR 必须在 ADD URRGROUP 之前） |
| `MMLCommand` | `must_be_last` | `MMLCommand` | 必须最后执行（如 SET REFRESHSRV） |
| `MMLCommand` | `refers_to` | `MMLCommand` | 跨命令引用（注意事项/参数说明中"通过 MOD CFGTHRESHOLD 修改""参见 SET XXX"等） |
| `MMLCommand` | `modifies_target_of` | `MMLCommand` | MOD 命令对应的 ADD 命令（来自内网 MOD 规则） |
| `MMLCommand` | `removes_target_of` | `MMLCommand` | RMV 命令对应的 ADD 命令（来自内网 RMV 规则） |

### 4.7 规则挂载

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `CommandRule` | `governs` | `MMLCommand` | 规则约束命令 |
| `CommandRule` | `governs` | `CommandParameter` | 规则约束参数 |
| `CommandRule` | `governs` | `ConfigObject` | 规则约束配置对象 |
| `CommandRule` | `governs` | 关系边 | 规则约束对象间关系 |
| `CommandRule` | `governs` | 属性 | 规则约束属性值 |

---

## 5. 计费场景示例

### 5.1 配置对象

| object_name | object_kind | identifier_parameters | 简要说明 |
| --- | --- | --- | --- |
| URR | entity | [URRNAME, URRID] | 使用量上报规则 |
| URRGROUP | group | [URRGROUPNAME] | 使用量上报规则组 |
| PCCPOLICYGRP | group | [PCCPOLICYGRPNM] | PCC 策略组 |
| PCCACTIONPROP | profile | [PCCACTPROPNAME] | PCC 动作属性 |
| FILTER | filter | [FILTERNAME] | 三四层过滤器 |
| L7FILTER | filter | [L7FILTERNAME] | 七层过滤器 |
| FLOWFILTER | entity | [FLOWFILTERNAME] | 流过滤器 |
| FLOWFILTERGRP | group | [FLOWFILTERGRPNAME] | 流过滤器组 |
| RULE | entity | [RULENAME, POLICYTYPE] | 规则 |
| USERPROFILE | entity | [USERPROFILENAME] | 用户模板 |
| RULEBINDING | binding | [USERPROFILENAME, RULENAME] | 用户模板与规则的绑定 |
| UPAPNCHARGE | global_setting | [APN] | APN 计费配置 |
| UPGLBCHGPARA | global_setting | [] | 全局计费参数 |
| REFRESHSRV | action | [] | 刷新生效 |

### 5.2 配置对象关系

```text
URRGROUP --contains--> URR
PCCPOLICYGRP --refers_to--> URRGROUP (via URRGROUPNAME)
PCCPOLICYGRP --refers_to--> PCCACTIONPROP (via PCCACTPROPNAME)
PCCPOLICYGRP --composed_by--> [URRGROUP, PCCACTIONPROP, QOSPROP, EXTENDPROP]
FLOWFILTER --contains--> FILTER (via FLTBINDFLOWF)
FLOWFILTER --contains--> L7FILTER (via FLTBINDFLOWF)
RULE --refers_to--> FLOWFILTER (via FLOWFILTERNAME)
RULE --refers_to--> PCCPOLICYGRP (via POLICYNAME)
USERPROFILE --refers_to--> RULE (via RULEBINDING)
```

### 5.3 命令 → 配置对象

```text
ADD URR --creates--> URR
MOD URR --modifies--> URR
DEL URR --deletes--> URR
LST URR --operates_on--> URR

ADD URRGROUP --creates--> URRGROUP
ADD PCCPOLICYGRP --creates--> PCCPOLICYGRP
ADD FLOWFILTER --creates--> FLOWFILTER
ADD FLTBINDFLOWF --binds--> FLOWFILTER (绑定 FILTER 到 FLOWFILTER)
ADD RULE --creates--> RULE
ADD USERPROFILE --creates--> USERPROFILE
ADD RULEBINDING --binds--> USERPROFILE (绑定 RULE)
SET URRGRPBINDING --sets--> USERPROFILE
SET REFRESHSRV --sets--> REFRESHSRV (动作型)
SET UPAPNCHARGE --sets--> UPAPNCHARGE
```

### 5.4 参数依赖

**同命令内：**

```text
[ADD URR] USAGERPTMODE --depends_on[=ONLINE]--> ONLMETERINGTYPE
[ADD URR] USAGERPTMODE --depends_on[=ONLINE]--> DFTQUOTAVOLUME
[ADD URR] USAGERPTMODE --depends_on[=OFFLINE]--> OFFMETERINGTYPE
[ADD PCCPOLICYGRP] TOKENFUNCFLAG --depends_on[=ENABLE]--> TOKENENCRYALG
[ADD PCCPOLICYGRP] TOKENFUNCFLAG --depends_on[=ENABLE]--> TOKENSECTORKEY
```

**跨命令：**

```text
[ADD URR] URRNAME --depends_on--> [ADD URRGROUP] UPURRNAME1 (值必须来自已存在的 URR)
[ADD URR] URRNAME --depends_on--> [ADD URRGROUP] DOWNURRNAME1
[ADD URRGROUP] URRGROUPNAME --depends_on--> [ADD PCCPOLICYGRP] URRGROUPNAME
[ADD FLOWFILTER] FLOWFILTERNAME --depends_on--> [ADD RULE] FLOWFILTERNAME
[ADD PCCPOLICYGRP] PCCPOLICYGRPNM --depends_on--> [ADD RULE] POLICYNAME
```

### 5.5 规则示例

| rule_id | rule_name | scope_type | scope_ref | severity | rule_logic |
| --- | --- | --- | --- | --- | --- |
| CR-001 | URRID 全局唯一 | config_object | URR | critical | URRID 在所有 URR 内必须唯一 |
| CR-002 | RULENAME+POLICYTYPE 联合唯一 | config_object | RULE | critical | 规则名称和策略类型共同唯一标识一条 Rule |
| CR-003 | FLOWFILTER 必须引用已存在对象 | parameter | FLOWFILTERNAME | critical | FLOWFILTERNAME 必须引用系统已存在的流过滤器 |
| CR-004 | 被绑定的 PCCPOLICYGRP 禁止删除 | config_object | PCCPOLICYGRP | critical | 被 Rule 引用的 PCCPOLICYGRP 不允许直接删除 |
| CR-005 | UPF 与 SMF 的 RG 必须一致 | attribute | URR.RG | critical | UPF 和 SMF 的 RG 参数值必须保持一致 |
| CR-006 | REFRESHSRV 必须最后执行 | command | SET REFRESHSRV | critical | REFRESHSRV 必须在所有 Filter/UserProfile 配置完成后执行 |
| CR-007 | URR 最大记录数 65000 | config_object | URR | warning | URR 配置记录数不能超过 65000 |
| CR-008 | 事件计费影响性能 | command | ADD URR | warning | 开启事件计费对性能有一定影响 |
| CR-009 | SET UPAPNCHARGE 非立即生效 | command | SET UPAPNCHARGE | info | 该命令只对之后发生承载更新的用户或新激活用户生效 |

---

## 6. 跨层映射（命令图谱与上层的关系）

命令图谱通过 `ConfigObject` 被任务原子层引用：

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `ConfigTask` | `invokes` | `MMLCommand` | task 调用命令 |
| `ConfigTask` | `targets` | `ConfigObject` | task 操作的配置对象 |
| `TaskRule` | `refined_by` | `CommandRule` | task 规则落到命令层约束 |

---

## 7. 禁止的关系

| 关系 | 原因 |
| --- | --- |
| `CommandParameter → ConfigObject` 直接关系 | 跨了一层，参数通过所属命令间接关联配置对象 |
| `ConfigObject → CommandParameter` 直接关系 | 同上，反向也不允许 |
| 业务图谱直接引用 `MMLCommand` | 必须经过 ConfigTask 中转 |
