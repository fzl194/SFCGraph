# 命令图谱 Schema

> 版本: v0.1
> 定位: 云核心网 MML 命令的配置数字孪生本体，表达命令、参数、配置对象、规则及其关系。
> 用途: 支撑配置生成、语法核查、语义核查、关系追溯。
> 约束: 本文档定义对象、关系和核心属性结构。枚举范围（如 rule_type、object_kind 等）随场景扩展逐步补充。

---

## 1. 设计原则

1. 命令图谱分两层理解：**配置对象层**（配了什么）和**命令语法层**（怎么配），但统一为一套图谱。
2. 对象层级从上到下：**配置对象 → 命令 → 参数**。
3. 跨层只有相邻层有关系：配置对象 ↔ 命令，命令 ↔ 参数。配置对象与参数之间没有直接关系。
4. 同层内部对象之间可以有关系。
5. 配置对象的属性直接复用命令参数的定义，不做两套。
6. 规则可以自由挂载在任意层任意粒度上：命令、参数、配置对象、关系、属性。
7. 命令、参数从产品文档中提取；配置对象从命令脚本执行结果中提取；规则从注意事项和参数说明中提取。

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

配置对象是命令脚本执行后产生的稳定配置实体。

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `object_id` | string | 是 | 唯一标识 |
| `object_name` | string | 是 | 对象名称，如 `URR`、`URRGROUP`、`RULE` |
| `object_kind` | enum | 是 | 对象种类（见 3.2.1） |
| `identifier_parameters` | list[string] | 否 | 标识参数名列表，如 URR 的 `[URRNAME, URRID]` |
| `attributes` | list[object] | 否 | 属性列表（复用 CommandParameter 定义，见 3.2.2） |
| `applicable_nf` | list[string] | 否 | 适用网元，如 `[PGW-U, UPF]` |
| `description` | string | 否 | 说明 |
| `source_evidence_ids` | list[string] | 否 | 来源证据 |

#### 3.2.1 object_kind 枚举

> 随场景扩展逐步补充，初始版本：

| 值 | 说明 | 示例 |
| --- | --- | --- |
| `entity` | 独立实体对象 | URR、RULE、USERPROFILE、FLOWFILTER |
| `group` | 组合/聚合对象 | URRGROUP、PCCPOLICYGRP、FLOWFILTERGRP |
| `binding` | 绑定关系对象 | RULEBINDING、FLTBINDFLOWF |
| `global_setting` | 全局配置（无独立标识参数） | UPAPNCHARGE、UPGLBCHGPARA |
| `profile` | 配置档案/属性集 | PCCACTIONPROP、QOSPROP、EXTENDPROP |
| `action` | 动作型（不创建对象） | REFRESHSRV |
| `filter` | 过滤器 | FILTER、L7FILTER |

#### 3.2.2 attributes 子对象

配置对象的属性直接复用命令参数的定义。每个属性包含：

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `parameter_name` | string | 是 | 参数名 |
| `data_type` | string | 否 | 数据类型 |
| `required_mode` | enum | 是 | `required / optional / conditional_required / conditional_optional` |
| `default_value` | string | 否 | 默认值 |
| `enum_values` | list[string] | 否 | 枚举值列表 |
| `condition` | string | 否 | 条件表达式，如 `USAGERPTMODE=ONLINE` |
| `description` | string | 否 | 说明 |
| `config_principle` | string | 否 | 配置原则（来自参数说明中的"配置原则"段落） |

### 3.3 MMLCommand

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `command_id` | string | 是 | 唯一标识 |
| `command_name` | string | 是 | 命令全称，如 `ADD URR` |
| `verb` | enum | 是 | 动作类型（见 3.3.1） |
| `object_keyword` | string | 是 | 命令对象关键字，如 `URR` |
| `applicable_nf` | list[string] | 否 | 适用网元 |
| `command_summary` | string | 否 | 命令功能说明 |
| `notes` | list[string] | 否 | 注意事项列表（从"注意事项"章节提取） |
| `max_records` | integer | 否 | 最大记录数规格 |
| `immediate_effect` | boolean | 否 | 是否立即生效 |
| `permission_level` | string | 否 | 操作用户权限 |
| `is_dangerous` | boolean | 否 | 是否高危命令 |
| `category_path` | list[string] | 否 | 分类路径，如 `["业务控制策略", "计费控制", "使用率上报规则"]` |
| `usage_examples` | list[string] | 否 | 使用实例 |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 是 | 来源证据 |

#### 3.3.1 verb 枚举

| 值 | 说明 |
| --- | --- |
| `ADD` | 增加 |
| `MOD` | 修改 |
| `DEL` | 删除 |
| `SET` | 设置 |
| `LST` | 查询 |
| `RMV` | 删除（另一种） |

### 3.4 CommandParameter

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `parameter_id` | string | 是 | 唯一标识 |
| `command_ref` | string | 是 | 所属命令 |
| `parameter_name` | string | 是 | 参数名 |
| `parameter_name_zh` | string | 否 | 参数中文名 |
| `data_type` | string | 否 | 数据类型 |
| `required_mode` | enum | 是 | `required / optional / conditional_required / conditional_optional` |
| `condition_expression` | string | 否 | 条件表达式，如 `USAGERPTMODE=ONLINE` |
| `value_range` | string | 否 | 取值范围描述 |
| `default_value` | string | 否 | 默认值 |
| `enum_values` | list[string] | 否 | 枚举值列表 |
| `description` | string | 否 | 说明 |
| `config_principle` | string | 否 | 配置原则 |
| `reference_target` | string | 否 | 该参数值引用的配置对象名（如 `UPURRNAME1` 引用 `URR`） |
| `source_evidence_ids` | list[string] | 否 | 来源证据 |

### 3.5 CommandRule

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `rule_id` | string | 是 | 唯一标识 |
| `rule_name` | string | 是 | 规则名称 |
| `rule_type` | enum | 是 | 规则类型（见 3.5.1） |
| `scope_type` | enum | 是 | 规则作用粒度（见 3.5.2） |
| `scope_ref` | string | 是 | 作用对象引用 |
| `rule_logic` | string | 是 | 规则逻辑描述 |
| `violation_effect` | string | 否 | 违反影响 |
| `severity` | enum | 是 | `critical / warning / info` |
| `source_evidence_ids` | list[string] | 是 | 来源证据 |

#### 3.5.1 rule_type 枚举

> 随场景扩展逐步补充，初始版本：

| 值 | 说明 | 示例 |
| --- | --- | --- |
| `uniqueness` | 唯一性约束 | URRID 全局唯一、RULENAME+POLICYTYPE 联合唯一 |
| `existence_precondition` | 存在性前置 | FLOWFILTERNAME 必须引用已存在对象 |
| `delete_constraint` | 删除保护 | 被绑定的 PCCPOLICYGRP 不允许删除 |
| `consistency` | 一致性约束 | UPF 与 SMF 的 RG/SID 必须一致 |
| `cardinality` | 数量/规格约束 | URR 最大 65000 条、PCCPOLICYGRP 最多 11 个组合 |
| `effect_scope` | 生效范围 | SET UPAPNCHARGE 只对新激活用户生效 |
| `parameter_dependency` | 参数条件依赖 | USAGERPTMODE=ONLINE 时 ONLMETERINGTYPE 出现 |
| `parameter_mutex` | 参数互斥 | 某些参数不能同时配置 |
| `ordering` | 顺序约束 | REFRESHSRV 必须最后执行 |
| `cross_nf_sync` | 跨网元同步 | SMF 和 UPF 关键参数必须一致 |
| `performance` | 性能影响 | 事件计费开启对性能有影响 |

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

### 4.4 参数 → 参数（层内）

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `CommandParameter` | `depends_on` | `CommandParameter` | 参数条件依赖，带条件值 |

`depends_on` 边需要携带条件属性：

| 边属性 | 类型 | 说明 |
| --- | --- | --- |
| `condition_value` | string | 触发条件值，如 `ONLINE` |
| `condition_expression` | string | 完整条件表达式，如 `USAGERPTMODE=ONLINE` |

示例：

```text
CommandParameter USAGERPTMODE (值=ONLINE)
  --depends_on [condition=USAGERPTMODE=ONLINE]--> CommandParameter ONLMETERINGTYPE

CommandParameter TOKENFUNCFLAG (值=ENABLE)
  --depends_on [condition=TOKENFUNCFLAG=ENABLE]--> CommandParameter TOKENSECRETKEY
```

跨命令参数依赖示例：

```text
[ADD URR] CommandParameter URRNAME
  --depends_on--> [ADD URRGROUP] CommandParameter UPURRNAME1 (值必须来自已存在的 URR)
```

### 4.5 配置对象 → 配置对象（层内）

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `ConfigObject` | `contains` | `ConfigObject` | 包含关系（如 URRGROUP 包含 URR） |
| `ConfigObject` | `refers_to` | `ConfigObject` | 引用关系（如 RULE 引用 PCCPOLICYGRP） |
| `ConfigObject` | `depends_on` | `ConfigObject` | 依赖关系（如 PCCPOLICYGRP 依赖 URRGROUP） |
| `ConfigObject` | `conflicts_with` | `ConfigObject` | 冲突/互斥 |
| `ConfigObject` | `composed_by` | `ConfigObject` | 组合关系（如 PCCPOLICYGRP 由多个子对象组合） |

> 关系边需要携带额外属性来描述关系的具体语义（如引用通过哪个参数、包含的数量约束等）。边属性按需扩展。

### 4.6 命令 → 命令（层内）

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `MMLCommand` | `must_precede` | `MMLCommand` | 执行顺序约束（如 ADD URR 必须在 ADD URRGROUP 之前） |
| `MMLCommand` | `must_be_last` | `MMLCommand` | 必须最后执行（如 SET REFRESHSRV） |

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
