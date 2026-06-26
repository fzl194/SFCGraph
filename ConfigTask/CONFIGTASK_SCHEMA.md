# ConfigTask 图层 Schema

> 定位：三层图谱的**任务原子层**——最小可复用配置原子，解耦特性层与命令层。
> 权威基准：`业务图谱体系/三层图谱Schema-最终版-v0.1.md` §10；形式参照 `command-graph/COMMAND_GRAPH_SCHEMA.md`。
> 构建策略：自底向上，先于特性层构建。
> 完整实例：`样例-内容计费@20.15.2-任务层实例.md`（多阶段=5 task）、`样例-IPSec@20.15.2-任务层实例.md`（多场景同骨架=1 task）。

---

## 1. 设计原则

1. `ConfigTask` = **最小可复用配置原子 = (配置意图, 命令组)**。特性不直接落命令，先拆成 task；命令通过 task 被引用。
2. **task 颗粒度 = 阶段级**：一个 task = 一个连贯的配置动作（操作流程的一个阶段，或一份独立子配置），共同产出一个可命名的配置对象集。一个特性可有 0~N 个 task。
3. **merge key = (task_goal, 核心命令集)**：同意图 + 同命令集的动作，无论来自哪个特性，归为同一可复用 task。
4. **相同命令 ≠ 一个 task**：命令是 task 的零件，task 是命令的意图聚合。
5. **命令参数不影响 task 身份**，只影响 task 内变体（由 DecisionPoint + 命令图谱参数依赖承接）。
6. **多场景同骨架 = 1 个 task**（如 IPSec 9 变体），场景差异由 DecisionPoint 表达，不建多 task、不加 variant_dimensions 字段。
7. **协议底座型特性 = 0 task**（如 SA-Basic，配置被打散到上层特性）。
8. **命令顺序 = `commands` 有序列表**（列表即执行序列），不单建编排边对象。
9. **参数三类**：固参 fixed / 变参 variable / 引用 reference（详见 §4）。
10. **关系只在子/正向侧存一次**：归属关系用子对象 FK（`TaskRule.task_ref`、`DecisionPoint.owner_ref`），父对象不存反向列表。
11. **边/字段/对象判据**：纯隶属/顺序无每实例属性 → 字段（`commands`）；有独立富属性需被规则治理 → 对象（命令图谱 `CommandRule`）；决策多分支影响扇出 → 结构化字段（`options[].impacts[]`）。

---

## 2. ID 与版本治理（方案G）

| 维度 | 约定 |
| --- | --- |
| 分层键 | `网元 × 版本`，如 `UDG@20.15.2`。每层是一份完整 task 资产集，跨版本/跨网元**当下不去重合并**，演进靠 diff。 |
| 实例键 | 统一 `网元@版本@对象类型@编号`（`@` 分隔），对象类型进 ID 确保跨类型唯一，不带场景前缀。编号层内同类型顺序递增。 |
| 跨层锚点 | `task_logical_name`（语义名，层内唯一）做跨层标识；上层（Feature）通过语义名 `decomposes_to`，路由到目标 `网元@版本` 的实例。 |

**实例键示例：**
- ConfigTask：`UDG@20.15.2@ConfigTask@00001`
- TaskRule：`UDG@20.15.2@TaskRule@00001`
- DecisionPoint：`UDG@20.15.2@DecisionPoint@00001`
- 命令/参数引用（命令图谱对象）：`UDG@20.15.2@MMLCommand@ADD URR`、`UDG@20.15.2@CommandParameter@ADD URR:URRNAME`

---

## 3. 对象总表

| 对象 | 定位 |
| --- | --- |
| `ConfigTask` | 配置任务——最小可复用配置原子 |
| `TaskRule` | 任务规则——task 内跨命令协同约束 |
| `DecisionPoint` | 决策点——跨层通用决策结构，表达 task 内变体 |

---

## 4. ConfigTask

**字段：**

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `task_id` | string | 是 | 实例键 `UDG@20.15.2@ConfigTask@00001` |
| `task_logical_name` | string | 是 | 语义名（层内唯一，跨层锚点），如 `配置计费动作链` |
| `nf` | string | 是 | 网元，如 `UDG` |
| `version` | string | 是 | 版本，如 `20.15.2` |
| `raw_steps_text` | string | 否 | "操作步骤"原文（commands 的源头） |
| `task_goal` | string | 是 | 配置意图（归一化），如 `配置业务费率` |
| `task_summary` | string | 是 | 一句话说明 |
| `commands` | list[object] | 是 | 有序命令列表（**列表顺序=执行顺序**），结构见下 |
| `task_category` | enum | 否 | `配置 / 验证`（验证类来自调测文档，下一步纳入） |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 否 | 来源证据/文件路径 |

**`commands` 子结构（命令 + 参数一体）：**

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `command_ref` | string | 是 | 命令图谱实例键 `UDG@20.15.2@MMLCommand@ADD URR`（可下探取命令详情） |
| `parameters` | list[object] | 是 | 该命令在本 task 下的参数规划，结构见下 |

**`parameters` 子结构（每参数三类）：**

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `parameter_ref` | string | 是 | 命令图谱实例键 `UDG@20.15.2@CommandParameter@ADD URR:URRNAME`（下探取参数定义/类型/枚举/依赖/跨命令引用） |
| `binding_type` | enum | 是 | `fixed（固参）/ variable（变参）/ reference（引用）` |
| `fixed_value` | string | 否 | `fixed` 时的固定配法，如 `POLICYTYPE=PCC`（本 task 下总不变） |
| `variable_source` | enum | 否 | `variable` 时的来源（命令图谱权威 3 值 + 聚合发现 1 值，**可扩展**） |
| `source_ref` | string | 否 | `decision_driven` 时 → DecisionPoint；`reference` 时 → 源命令.参数 |

> **variable_source 枚举**（基于三视角交叉验证，命令图谱"数据来源"为权威）：
> - `local_planned`（本端规划）：工程师本地命名/策略/地址/阈值。命令图谱权威值。
> - `global_planned`（全网规划）：跨网元协调的 ID/地址/路由标识。命令图谱权威值。
> - `peer_planned`（对端规划）：必须与对端一致的算法/协议参数。命令图谱权威值。
> - `decision_driven`（决策驱动）：**跨案例聚合后**发现取值变化，由 DecisionPoint 驱动。非命令图谱字段，Phase B 聚合时判定。
>
> 此字段为**可扩展枚举**——未来如有新的参数来源类型（如 `auto_generated`/`inherited`），追加值即可，不破坏已有数据。

> **三类参数**：
> - **固参 fixed**：跨所有配置案例**零例外**地稳定不变（给 `fixed_value`，如 `FILTERINGMODE=FLOWFILTER`）。
> - **变参 variable**：随配置实例变化，标 `variable_source`。**不记具体取值**（如 `URRID=12500`）。若跨案例取值有差异 → `decision_driven`（暗示 DecisionPoint）。
> - **引用 reference**：值**必须来源于已有配置**。跨命令引用关系（如 `UPURRNAME1`↔`URR.URRNAME`）由命令图谱 CommandParameter 在下层定义；被引用命令**不一定在本 task 内**，引用关系与 task 内命令顺序相关但不完全对应。

---

## 5. TaskRule

只管一类：**task 内部、跨多条命令、离开此配置动作即失效的协同约束**（不是 CommandRule 的单命令语法，也不是 FeatureRule 的跨网元/跨特性）。

**字段：**

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `rule_id` | string | 是 | 实例键 `UDG@20.15.2@TaskRule@00001` |
| `task_ref` | string | 是 | 所属 ConfigTask（子侧 FK，关系只存这一处） |
| `rule_name` | string | 是 | 规则名称 |
| `rule_type` | enum | 是 | 4 类，见下 |
| `rule_logic` | string | 是 | 规则逻辑（自然语言） |
| `violation_effect` | string | 否 | 违反影响（如"否则 Rule 无效""否则业务不通"） |
| `severity` | enum | 否 | `critical / warning / info` |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 否 | 来源证据 |

**`rule_type` 4 类（基于真实文档）：**

| rule_type | 管什么 | 实例 |
| --- | --- | --- |
| `binding_rule` | task 内跨命令引用绑定强制 | FLOWFILTER 必须绑定 filter/l7filter 否则 Rule 无效 |
| `relative_value_rule` | task 内多同类对象相对取值约束 | 只绑 L34 的 RULE 优先级 < 绑 L7 的；any RULE 最低 |
| `conditional_param_rule` | task 上下文条件→参数必填/固定值 | 需计费→URRGROUPNAME 必填；ADC task 下 ADCMUTEFLAG=DISABLE |
| `consistency_rule` | task 内跨命令一致性/配对 | IPSec VNRS↔IPsec 微服务双配原则；VoLTE PRIORITY1/2+PROTOCOL6/17 配对 |

> **归口判据**：涉及 ≥2 条不同命令 + 不跨特性/不跨网元 + 离开当前 task 语境即失效 → TaskRule。否则单命令语法→CommandRule，跨网元/跨特性→FeatureRule。

---

## 6. DecisionPoint

跨层通用决策结构（`owner_layer` 可为 business/feature/task，本层实例=task）。一个决策点 = 一个问题 + 若干分支，每个分支扇出**多个影响**，影响可落在任意层的任意对象上。

**字段：**

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `decision_id` | string | 是 | 实例键 `UDG@20.15.2@DecisionPoint@00001` |
| `owner_layer` | enum | 是 | `business / feature / task` |
| `owner_ref_type` | string | 是 | 宿主对象类型（ConfigTask） |
| `owner_ref` | string | 是 | 宿主对象实例键（子侧 FK） |
| `decision_name` | string | 是 | 如 `计费方式选择` |
| `decision_question` | string | 是 | 该决策回答什么问题 |
| `trigger_condition` | string | 否 | 何时需要做该决策 |
| `options` | list[object] | 是 | 分支集合，结构见下 |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 否 | 来源证据 |

**`options` 子结构：**

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `option_name` | string | 是 | 分支名，如 `在线` |
| `impacts` | list[object] | 是 | 该分支造成的所有影响（可多条、跨层跨对象），结构见下 |

**`impacts` 子结构：**

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `target_layer` | enum | 是 | `parameter / command / task / config_object / feature` |
| `target_ref` | string | 是 | 被影响对象实例键（命令/参数用命令图谱键格式） |
| `effect_type` | enum | 是 | `sets_value_pattern / adds / changes_command_set / excludes / skips_task / ...` |
| `effect_detail` | string | 否 | 具体怎么变 |

> DecisionPoint 的作用：表达 task 内变体（配置范式/多场景），**不拆 task**。一个分支可影响多个对象、可跨层（如融合计费分支跨层增加"配置CHF交互"task）。

---

## 7. 关系（存储方向）

| 子/起点 | FK/字段 | 父/终点 |
| --- | --- | --- |
| TaskRule | `task_ref` | ConfigTask |
| DecisionPoint | `owner_ref` | ConfigTask |
| ConfigTask.`commands[].command_ref` / `parameter_ref` | `commands` 字段 | MMLCommand / CommandParameter |
| DecisionPoint.`options[].impacts[].target_ref` | `impacts` | 任意层对象（parameter/command/task/config_object/feature） |

**跨层（上层特性层，待建）：**

| 关系 | 说明 |
| --- | --- |
| Feature `decomposes_to` ConfigTask | 特性引用 task（用 `task_logical_name`，路由到目标网元@版本） |
| FeatureTaskOrderEdge | 特性下 task 的先后（归特性层 schema） |
| FeatureRule `constrains_task` ConfigTask | 特性规则约束 task 使用方式 |

> 归属关系只在子侧 FK 存一次；ConfigTask 不存反向列表（要查 task 的规则/决策，反查 TaskRule.task_ref / DecisionPoint.owner_ref）。

---

## 8. 实例（精简，完整见样例文件）

**ConfigTask `UDG@20.15.2@ConfigTask@00001` 配置计费动作链**

```
task_id: UDG@20.15.2@ConfigTask@00001
task_logical_name: 配置计费动作链
nf/version: UDG / 20.15.2
task_goal: 配置业务费率（计费三件套 URR→URRGROUP→PCCPOLICYGRP）
task_summary: 配置使用量上报规则与规则组并绑定PCC策略组
task_category: 配置
status: active
source_evidence_ids: [部署UPF_28493406.md]
commands（顺序=执行序）:
  1. UDG@20.15.2@MMLCommand@ADD URR
     - ADD URR:URRNAME — variable/planned
     - ADD URR:URRID  — variable/planned
     - ADD URR:USAGERPTMODE — variable/decision_driven → @DecisionPoint@00001
     - ADD URR:OFFMETERINGTYPE / ONLMETERINGTYPE — variable/decision_driven → @DecisionPoint@00001
  2. UDG@20.15.2@MMLCommand@ADD URRGROUP
     - ADD URRGROUP:URRGROUPNAME — variable/planned
     - ADD URRGROUP:UPURRNAME1/DOWNURRNAME1/UPURRNAME2/DOWNURRNAME2 — reference
  3. UDG@20.15.2@MMLCommand@ADD PCCPOLICYGRP
     - ADD PCCPOLICYGRP:PCCPOLICYGRNM — variable/planned
     - ADD PCCPOLICYGRP:URRGROUPNAME — reference
```

**TaskRule `UDG@20.15.2@TaskRule@00001`**（task_ref → ConfigTask@00001）：URRGROUP 必须同时配在线+离线 URR（`consistency_rule`，warning）。

**DecisionPoint `UDG@20.15.2@DecisionPoint@00001` 计费方式选择**（owner_ref → ConfigTask@00001）：

| option | impacts |
| --- | --- |
| 在线 | `@CommandParameter@ADD URR:USAGERPTMODE`=ONLINE(sets_value)；`…:ONLMETERINGTYPE` 条件出现(adds)；`@MMLCommand@SET URRFAILACTION` 加入(adds) |
| 离线 | `…:USAGERPTMODE`=OFFLINE(sets_value)；`…:OFFMETERINGTYPE` 条件出现(adds) |
| 融合 | `…:USAGERPTMODE` 同组在线+离线共存(sets_value)；`@ConfigTask@xxxxx`「配置CHF交互」(adds，跨层) |

---

## 9. task 形态参考（实例佐证）

| 形态 | 例子 | task 数 |
| --- | --- | --- |
| 多阶段 | 内容计费（部署UPF 5 阶段） | N（5） |
| 多场景同骨架 | IPSec（9 变体共享 9 步骨架） | 1（+DecisionPoint 表达场景） |
| 多子配置 | QoS(IP)（复杂/简单流分类/DSCP-VLAN） | N（3） |
| 单动作 | 接入控制 / VoLTE / eDRX / IPv6承载 | 1 |
| 协议底座型 | SA-Basic（无配置流程） | 0 |

> 12 特性审视详见 `审视报告-12特性.md`。
