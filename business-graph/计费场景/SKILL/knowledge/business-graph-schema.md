# 业务图谱最终 Schema 定义

## 文档说明

本文档是业务图谱的**权威 Schema 定义**，包含所有对象类型、属性、关系，不包含任何实例化数据。

**合并来源**：
- 基础 Schema：`06-business-awareness-business-graph-final.md` Part A
- 扩展 Schema：`07a-schema-extension-decision-driven.md`（5 条新边、2 个新属性）

**不包含**：07b（决策驱动边的计费实例）、06 Part B（计费场景实例）

---

## 1. 什么是业务图谱

```text
把某一业务域中的稳定业务问题、方案闭包、工程任务、支撑对象，
以及它们与下层语义对象、特性、配置对象的连接关系，
组织成一套结构化对象网络。
```

业务图谱本质上是一张"业务组织图"，而不是一条"运行流程图"。

---

## 2. Schema 分层

| 层 | 包含的 Schema | 层间关系 |
|---|---|---|
| 业务层主链 | BusinessDomain, NetworkScenario, DeliverySolution, EngineeringTask | 自上而下逐层分解 |
| 支撑层 | Participant, Scope, DecisionPoint, ValidationPlan, BusinessRule | 挂载在 DS/NS 上 |
| 桥接层 | DomainSemanticObject, Feature, ConfigObject | 向下桥接到特性图谱 |

---

## 3. 对象类型总表（12 种）

| Schema | 中文对象名 | 所属层 | 定义 | 在图谱中的作用 |
| --- | --- | --- | --- | --- |
| `BusinessDomain` | 业务域 | 业务层 | 表示一类长期存在的工程知识空间 | 图谱根对象，限定讨论边界 |
| `NetworkScenario` | 现网场景 | 业务层 | 表示一线遇到的需求类型或问题情境 | 图谱的一级业务入口 |
| `DeliverySolution` | 交付方案 | 业务层 | 表示针对某个场景形成的可落地方案闭包 | 把场景推进到"怎么组织落地" |
| `EngineeringTask` | 工程任务 | 业务层 | 表示方案中的可执行或可检查任务 | 把方案拆成可执行工作项 |
| `Participant` | 参与方 | 支撑层 | 表示方案过程中承担稳定职责的参与方 | 说明方案涉及哪些角色 |
| `Scope` | 生效范围 | 支撑层 | 表示方案或策略的生效边界 | 表达作用边界 |
| `DecisionPoint` | 决策点 | 支撑层 | 表示会引起后续结构分支的稳定选择点 | 表达同一场景/方案下的分支 |
| `ValidationPlan` | 验收计划 | 支撑层 | 表示针对方案的验收检查模板 | 提供"验什么"的组织结构 |
| `BusinessRule` | 业务规则 | 支撑层 | 表示业务级校验、约束断言和异常定位逻辑的统一规则对象 | 提供规则治理 |
| `DomainSemanticObject` | 领域语义对象 | 桥接层 | 表示业务域内部用于表达业务含义的语义对象 | 防止业务图谱直接坠落成命令图 |
| `Feature` | 特性 | 桥接层 | 表示产品文档中的特性条目 | 承接业务语义背后的能力载体 |
| `ConfigObject` | 配置对象 | 桥接层 | 表示 MML 命令创建、修改、引用的对象 | 说明图谱最终会落到哪些对象链 |

---

## 4. 对象属性定义

### 4.1 BusinessDomain（业务域）

**定位**：图谱的轻量根节点，只做一件事：限定讨论边界，并指向它包含的现网场景。

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `domain_id` | `string` | 是 | 唯一标识，语义化命名，不绑定产品缩写 |
| `domain_name` | `string` | 是 | 域名称 |
| `domain_summary` | `string` | 是 | 一句话定义 |
| `status` | `string` | 是 | 数据状态 |

### 4.2 NetworkScenario（现网场景）

**定位**：一线遇到的需求类型或问题情境，作为图谱的一级业务入口。

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `scenario_id` | `string` | 是 | 唯一标识 |
| `scenario_name` | `string` | 是 | 场景名称 |
| `scenario_summary` | `string` | 是 | 一句话描述 |
| `judgment_basis` | `string` | 是 | 判断基础：什么情况下属于该场景 |
| `typical_outcome` | `string` | 是 | 典型结果 |
| `source_evidence_ids` | `list[string]` | 是 | 证据来源 |
| `status` | `string` | 是 | 数据状态 |

### 4.3 DeliverySolution（交付方案）

**定位**：针对某个场景形成的可落地方案闭包。

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `solution_id` | `string` | 是 | 唯一标识 |
| `solution_name` | `string` | 是 | 方案名称 |
| `solution_summary` | `string` | 是 | 一句话描述，概括方案闭包核心 |
| `core_mechanism_combo` | `string` | 是 | 核心机制组合——方案区别于场景名称的关键差异化信息 |
| `source_evidence_ids` | `list[string]` | 是 | 证据来源文档ID列表 |
| `status` | `string` | 是 | 数据状态 |

### 4.4 EngineeringTask（工程任务）

**定位**：原子动作单元，可被多个 DS 或 Feature 复用。覆盖 `plan / execute / verify` 三类工程动作；其中只有 execute 类 Task 才会在需要时下沉到特性图谱中的 `ConfigStep`。

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `task_id` | `string` | 是 | 唯一标识 |
| `task_name` | `string` | 是 | 任务名称 |
| `task_summary` | `string` | 是 | 一句话描述 |
| `phase` | `string` | 是 | 阶段：`plan` / `execute` / `verify` |
| `input_artifacts` | `list[string]` | 是 | 需要的输入 |
| `output_artifacts` | `list[string]` | 是 | 产出的输出 |
| `command` | `string` | 否 | 命令示例（`ADD`/`SET`/`LST`/`DSP`，plan 阶段为 `-`） |
| `config_object` | `string` | 否 | 涉及的配置对象（plan 阶段为 `-`） |
| `output_cardinality` | `string` | 否 | execute 阶段：输出 ConfigObject 的数量公式，如 `2N+2(融合)/N+2(单一模式)`，含输入变量说明。plan/verify 阶段为 `-` |
| `source_evidence_ids` | `list[string]` | 是 | 证据来源文档 ID 列表 |
| `status` | `string` | 是 | 数据状态 |

### 4.5 Participant（参与方）

**定位**：在某个 `DeliverySolution` 的形成、生效、更新、计费、验证过程中承担稳定职责的参与方。

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `participant_id` | `string` | 是 | 唯一标识 |
| `participant_name` | `string` | 是 | 参与方名称 |
| `participant_type` | `string` | 是 | 类型：`endpoint / network_function / external_system / service_endpoint / access_side` |
| `responsibility_summary` | `string` | 是 | 一句话说明其稳定职责 |
| `plane_or_side` | `string` | 否 | 所在侧：`control_plane / user_plane / external / terminal_side / service_side` |
| `source_evidence_ids` | `list[string]` | 是 | 证据来源 |
| `status` | `string` | 是 | 数据状态 |

### 4.6 Scope（生效范围）

**定位**：描述某个 `DeliverySolution` 或某类策略对"谁、哪类接入、哪类位置、哪类会话条件"生效的边界对象。

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `scope_id` | `string` | 是 | 唯一标识 |
| `scope_name` | `string` | 是 | 范围名称 |
| `scope_summary` | `string` | 是 | 一句话说明该范围含义 |
| `scope_type` | `string` | 是 | 范围类别：`subscriber / subscription / access / location / slice / service-selection` |
| `scope_expression` | `string` | 否 | 原始表达或归一化表达 |
| `source_evidence_ids` | `list[string]` | 是 | 证据来源 |
| `status` | `string` | 是 | 数据状态 |

### 4.7 DecisionPoint（决策点）

**定位**：在某个 `NetworkScenario` 或 `DeliverySolution` 中，会导致后续任务、动作路径或方案实现方式发生分支变化的稳定选择点。

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `decision_id` | `string` | 是 | 唯一标识 |
| `decision_name` | `string` | 是 | 决策点名称 |
| `decision_question` | `string` | 是 | 该决策实际在回答什么问题 |
| `option_set` | `list[string]` | 是 | 可选分支集合 |
| `trigger_condition` | `string` | 否 | 在什么条件下需要做该决策 |
| `impact_summary` | `string` | 是 | 不同分支会影响哪些后续任务或方案结构 |
| `source_evidence_ids` | `list[string]` | 是 | 证据来源 |
| `status` | `string` | 是 | 数据状态 |

### 4.8 ValidationPlan（验收计划）

**定位**：针对某个 `DeliverySolution` 或某类关键业务目标的验收检查模板。回答"验什么"，不直接回答"怎么逐条执行检查"。

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `validation_id` | `string` | 是 | 唯一标识 |
| `validation_name` | `string` | 是 | 验收计划名称 |
| `validation_goal` | `string` | 是 | 验收目标 |
| `target_objects` | `list[string]` | 是 | 需要观察/检查的对象集合 |
| `pass_condition` | `string` | 是 | 通过条件 |
| `expected_result` | `string` | 是 | 预期现象或结果 |
| `source_evidence_ids` | `list[string]` | 是 | 证据来源 |
| `status` | `string` | 是 | 数据状态 |

### 4.9 BusinessRule（业务规则）

**定位**：用于表达业务级核查、约束断言和异常定位逻辑的统一规则对象。

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `rule_id` | `string` | 是 | 唯一标识 |
| `rule_name` | `string` | 是 | 规则名称 |
| `rule_type` | `string` | 是 | `validation_rule / diagnosis_rule / constraint_rule` |
| `rule_purpose` | `string` | 是 | 规则用途 |
| `trigger_condition` | `string` | 否 | 何时触发该规则 |
| `check_target` | `string` | 是 | 检查对象或观察对象 |
| `check_logic` | `string` | 是 | 判断逻辑 |
| `expected_result` | `string` | 否 | 满足时的预期结果（适用于 validation_rule） |
| `violation_effect` | `string` | 否 | 违反后的影响（适用于 constraint_rule） |
| `next_action` | `string` | 否 | 下一步排查动作（适用于 diagnosis_rule） |
| `source_evidence_ids` | `list[string]` | 是 | 证据来源 |
| `status` | `string` | 是 | 数据状态 |

### 4.10 DomainSemanticObject（领域语义对象）

**定位**：表示某个业务域内部用于表达业务含义的语义对象。防止业务图谱直接坠落成命令图，先把业务问题翻成识别、计费、配额等语义单元。

> DomainSemanticObject 在图谱层面为轻量引用对象，其完整定义在特性图谱中展开。图谱层面仅使用其标识和语义描述。

### 4.11 Feature（特性）

**定位**：表示产品文档中的特性条目，承接业务语义背后的能力载体。

> Feature 在图谱层面为轻量引用对象，其完整定义在特性图谱中展开。图谱层面仅使用其标识和能力定位。

### 4.12 ConfigObject（配置对象）

**定位**：表示 MML 命令创建、修改、引用的对象。图谱层面不展开所有命令参数，但要说明关键对象链。

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `object_name` | `string` | 是 | 对象名称（如 URR, URRGROUP, RULE） |
| `object_chain_position` | `string` | 是 | 对象链位置（如识别层/计费对象层/规则层） |
| `side` | `string` | 是 | 所属侧别（UDG/UPF / UNC/SMF / 双侧） |
| `business_role` | `string` | 是 | 业务作用 |
| `naming_pattern` | `string` | 否 | 对象命名模式，如 `{业务}_{模式}` |
| `priority_pattern` | `string` | 否 | 优先级模式（可选），如 `特定100+, 兜底65000+` |

---

## 5. 关系定义

### 5.1 关系总表（26 条边）

#### 业务主链（3 条）

| 起点schema | 终点schema | 关系标识 | 中文关系名 | 业务含义 |
| --- | --- | --- | --- | --- |
| `BusinessDomain` | `NetworkScenario` | `contains` | 包含 | 一个业务域由若干稳定业务场景组成 |
| `NetworkScenario` | `DeliverySolution` | `instantiated_as` | 实例化为 | 一个场景可收敛为一个或多个方案闭包 |
| `DeliverySolution` | `EngineeringTask` | `uses_task` | 使用任务 | 一个方案通过规划、执行、验证三类工程任务落地 |

#### 方案到支撑对象（7 条）

| 起点schema | 终点schema | 关系标识 | 中文关系名 | 业务含义 |
| --- | --- | --- | --- | --- |
| `DeliverySolution` | `Participant` | `involves` | 涉及 | 一个方案会涉及若干稳定参与方协同完成 |
| `DeliverySolution` | `Scope` | `applies_to` | 作用于 | 一个方案对谁、在哪些接入/位置/导向边界下生效 |
| `NetworkScenario` | `DecisionPoint` | `has_decision` | 包含决策点 | 某些场景天然存在稳定分支 |
| `DeliverySolution` | `DecisionPoint` | `has_decision` | 包含决策点 | 某些方案内部存在关键分支 |
| `DecisionPoint` | `Scope` | `conditioned_by` | 受范围条件约束 | 部分决策点只有在特定边界下才成立 |
| `DeliverySolution` | `ValidationPlan` | `validated_by` | 由其验收 | 一个方案需要有对应的验收模板 |
| `DeliverySolution` | `BusinessRule` | `governed_by` | 受规则治理 | 方案受校验规则、约束规则和诊断规则治理 |

#### 验收内部（2 条）

| 起点schema | 终点schema | 关系标识 | 中文关系名 | 业务含义 |
| --- | --- | --- | --- | --- |
| `ValidationPlan` | `EngineeringTask` | `executed_by` | 由其执行 | 验收计划通过验证态任务具体落地；约束：EngineeringTask.phase = verify |
| `ValidationPlan` | `BusinessRule` | `uses_rule` | 使用规则 | 验收计划内部依赖判断规则来形成可执行检查条件 |

#### 向下桥接（4 条）

| 起点schema | 终点schema | 关系标识 | 中文关系名 | 业务含义 |
| --- | --- | --- | --- | --- |
| `NetworkScenario` | `DomainSemanticObject` | `uses_semantic_object` | 使用领域语义对象 | 场景先关联稳定语义对象，再下钻实现 |
| `DeliverySolution` | `DomainSemanticObject` | `instantiates_semantic_object` | 实例化领域语义对象 | 方案把抽象语义落实为可交付的语义组合 |
| `DeliverySolution` | `Feature` | `requires_capability` | 需要能力 | 方案依赖正式能力载体 |
| `DeliverySolution` | `ConfigObject` | `realized_by_config` | 由配置对象实现 | 方案最终要收敛到关键对象链 |

#### Task 相关（4 条）

| 起点schema | 终点schema | 关系标识 | 中文关系名 | 业务含义 |
| --- | --- | --- | --- | --- |
| `Feature` | `EngineeringTask` | `contains` | 包含任务 | 特性可包含工程任务（后续Feature定义时启用） |
| `EngineeringTask` | `ConfigObject` | `creates_config` | 创建配置 | execute 阶段任务创建配置对象 |
| `EngineeringTask` | `ConfigObject` | `verifies_config` | 验证配置 | verify 阶段任务验证配置对象 |
| `EngineeringTask` | `ConfigStep` | `realized_by_config_step` | 由配置步骤实现 | execute 阶段任务可选映射到特性图谱 ConfigStep |

#### 决策驱动扩展（5 条）

| 起点schema | 终点schema | 关系标识 | 中文关系名 | 业务含义 |
| --- | --- | --- | --- | --- |
| `DecisionPoint` | `ConfigObject` | `parameter_binding` | 参数绑定 | 每个DP选项如何影响特定ConfigObject的特定参数值 |
| `DecisionPoint` | `EngineeringTask` | `gates` | 门控 | 每个DP选项下哪些Task应该执行(active)或跳过(skip) |
| `ConfigObject` | `ConfigObject` | `composes` | 组合 | 配置对象之间的组合关系和基数 |
| `Feature` | `ConfigObject` | `differentiates` | 差异化 | 该Feature相对于基准Feature在ConfigObject参数上的差异 |
| `EngineeringTask` | `EngineeringTask` | `output_propagates_to` | 输出传播 | 上游Task创建的对象名称如何传播到下游Task的引用参数 |

---

### 5.2 带属性的边

以下边的属性是结构化的，每条边必须携带明确的属性值。

#### 5.2.1 instantiated_as

```text
NetworkScenario --instantiated_as--> DeliverySolution
  属性:
    dependency_type : string   (required / optional / none)
```

**说明**：一个 DS 可同时覆盖多个 NS，`dependency_type` 表示每个 NS 与 DS 的关联强度。`required` 表示该 NS 是方案的必要组成部分，`optional` 表示增强性关联，`none` 表示无直接覆盖。

#### 5.2.2 parameter_binding

```text
DecisionPoint --parameter_binding--> ConfigObject
  属性:
    target_object   : string    (目标ConfigObject类型)
    parameter_name  : string    (参数名)
    value_per_option: [{
      option        : string    (DP选项)
      value         : string    (参数值)
      side_effects  : string    (附带影响)
    }]
```

**解决的问题**：DP选项不再是文字描述，而是结构化地驱动参数赋值。每个DP选项对应一组参数值和附带影响。

#### 5.2.3 gates

```text
DecisionPoint --gates--> EngineeringTask
  属性:
    task_id              : string
    activation_per_option: [{
      option      : string
      activation  : string   (active | skip)
    }]
```

**解决的问题**：每个DP选项下哪些Task应该执行或跳过，不再是隐含的。

#### 5.2.4 composes

```text
ConfigObject --composes--> ConfigObject
  属性:
    multiplicity   : string   (1:1 | 1:N | formula)
    condition_on_dp: string   (条件依赖的DP)
    binding_parameter: string (绑定参数)
```

**解决的问题**：配置对象之间的组合关系和基数不再隐含在命令参数中，而是显式表达。

#### 5.2.5 differentiates

```text
Feature --differentiates--> ConfigObject
  属性:
    parameter_name: string    (差异参数名)
    value         : string    (参数值)
    constraints   : [string]  (额外约束列表)
```

**解决的问题**：同一方案下不同Feature仅少数参数不同，需要显式表达差异。

#### 5.2.6 output_propagates_to

```text
EngineeringTask --output_propagates_to--> EngineeringTask
  属性:
    propagated_entity: string   (传播的ConfigObject名称)
    propagation_type : string   (name_reference | count_correlation)
```

**解决的问题**：上游Task创建的对象名称如何传播到下游Task的引用参数，确保名称在Task间的一致性。

---

### 5.3 关系结构图

```text
业务主链：
  BusinessDomain
    --contains--> NetworkScenario
      --instantiated_as--> DeliverySolution
        --uses_task--> EngineeringTask

支撑关系：
  DeliverySolution
    --involves--> Participant
    --applies_to--> Scope
    --has_decision--> DecisionPoint
    --validated_by--> ValidationPlan
    --governed_by--> BusinessRule

  NetworkScenario
    --has_decision--> DecisionPoint

  DecisionPoint
    --conditioned_by--> Scope

  ValidationPlan
    --executed_by--> EngineeringTask(verify)
    --uses_rule--> BusinessRule

决策驱动（扩展）：
  DecisionPoint
    --parameter_binding--> ConfigObject
    --gates--> EngineeringTask

  ConfigObject
    --composes--> ConfigObject

  Feature
    --differentiates--> ConfigObject

  EngineeringTask
    --output_propagates_to--> EngineeringTask

向下桥接：
  NetworkScenario
    --uses_semantic_object--> DomainSemanticObject
  DeliverySolution
    --instantiates_semantic_object--> DomainSemanticObject
    --requires_capability--> Feature
    --realized_by_config--> ConfigObject
```

---

### 5.4 抽象图谱结构

```text
BusinessDomain
└─ (某业务域)
   ├─ NetworkScenario
   │  ├─ (场景A)
   │  ├─ (场景B)
   │  └─ (场景C)
   │
   ├─ DeliverySolution
   │  ├─ (方案1)
   │  └─ (方案2)
   │
   ├─ EngineeringTask
   │  ├─ (plan态任务)
   │  ├─ (execute态任务)
   │  └─ (verify态任务)
   │
   ├─ Participant / Scope / DecisionPoint / ValidationPlan / BusinessRule
   └─ DomainSemanticObject / Feature / ConfigObject
```
