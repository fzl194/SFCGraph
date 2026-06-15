# 三层图谱 Schema 最终版

> 版本: v0.1
> 目标: 从本体角度构建云核心网 MML 配置数字孪生，明确业务图谱、特性图谱、任务原子层、命令图谱与证据层的边界。
> 说明: 本文档仅保留最终定义，不保留中间讨论过程。

---

## 1. 先看这张图

```text
业务域
  -> 场景
  -> 配置方案
  -> 特性 / 子特性
  -> 配置任务
  -> 命令
  -> 参数 / 配置对象
```

这条链回答的是：

- 业务层在解决什么问题
- 这个问题通常落到哪些正式能力
- 这些能力如何拆成可复用的配置任务
- 这些任务最终由哪些 MML 命令完成

如果只记一句话：

```text
业务图谱管“为什么配”
特性图谱管“靠什么能力配”
任务原子层管“具体做哪些可复用动作”
命令图谱管“命令、参数、对象到底是什么”
证据层管“这些结论从哪篇原始文档来”
```

---

## 2. 总体结构

```text
业务图谱 Business Graph
  回答: 为什么配、在什么现网场景下配、采用什么配置方案

特性图谱 Feature Graph
  回答: 产品能力是什么、能力如何细分、能力依赖什么

任务原子层 Task Layer
  回答: 哪些可复用配置动作可以持续积累、复用于多个特性和方案

命令图谱 Command Graph
  回答: MML 命令、参数、配置对象、命令级规则是什么

证据层 Evidence Layer
  回答: 哪些原始 md/excel/pdf/txt 材料支撑这些对象和关系
```

如果对外仍使用“三层图谱”表述，可理解为：

- 业务图谱
- 特性图谱
- 命令图谱

其中 `ConfigTask` 是业务与特性之间共享的公共原子层，建模上独立存在。

---

## 3. 核心原则

1. 图谱按本体层级解耦，不按文档来源解耦。
2. 稳定可复用对象建成 `Canonical Entity`，只在个别方案上下文中成立的对象不轻易实体化。
3. `Feature` 是能力本体，`SubFeature` 是单个正式特性内部的稳定细分形态。
4. `ConfigTask` 是最小可复用配置原子，不强制隶属于某个 Feature，也不强制隶属于某个业务方案。
5. task 的差异优先通过 `DecisionPoint + 关系边 + TaskRule` 表达，不单独抽象 `TaskVariant`。
6. 如果 `ConfigTask` 已经是最小复用原子，就不再单独建 `ConfigStep`。
7. 配置对象、参数、对象关系、命令约束全部归命令图谱。
8. `Rule` 和 `DecisionPoint` 都是跨层同构结构，只是作用层级不同。
9. `SemanticObject`、`License`、`EvidenceSource` 是跨层共享本体，不归属于某一层独占。
10. 业务图谱不直接拥有 `ConfigObject`、`CommandParameter`、`MMLCommand` 本体。
11. 稳定顺序、依赖、兜底、最后执行等编排信息优先由带属性的边承载。

---

## 4. 对象分层

### 4.1 Canonical Entity

稳定知识对象，可跨方案复用、长期积累、可被多次引用：

- `BusinessDomain`
- `NetworkScenario`
- `ConfigurationSolution`
- `Feature`
- `SubFeature`
- `ConfigTask`
- `DecisionPoint`
- `MMLCommand`
- `CommandParameter`
- `ConfigObject`
- `SemanticObject`
- `License`
- `BusinessRule`
- `FeatureRule`
- `TaskRule`
- `CommandRule`

### 4.2 全局共享本体

不归属于某一层独占：

- `SemanticObject`
- `License`
- `EvidenceSource`

### 4.3 子对象

作为宿主对象的子对象存在，不单独建一级实体：

- `Scope`
- `Participant`

---

## 5. 顺序关系怎么承载

这是最容易混的地方，单独说明。

当前 schema 里，顺序不是都挂在一个地方，而是按层级分三种理解：

### 5.1 task 内部顺序

这是最稳定的一层，表达“一个 task 内部，哪些命令先做、后做、依赖做、最后做”。

由：

- `TaskCommandOrderEdge`

承载。

例如：

```text
配置计费动作链
  ADD URR
  -> ADD URRGROUP
  -> ADD PCCPOLICYGRP
```

### 5.2 特性下 task 的顺序

这是第二层，表达“一个 Feature 或 SubFeature 通常按什么 task 顺序展开”。

由：

- `FeatureTaskOrderEdge`

承载。

例如：

```text
内容计费特性
  先配置计费动作链
  再配置 Rule
  再配置 UserProfile 绑定
  最后配置缺省费率和刷新
```

### 5.3 方案级顺序

方案层也可能有顺序，但它最依赖场景、决策点和当前实施上下文。

因此当前最终版的原则是：

- `ConfigurationSolution -> uses_feature / uses_task` 进入主 schema
- 方案级完整顺序链 **暂不进入主 schema**

原因：

- 方案级顺序通常强依赖 `DecisionPoint`
- 不同方案下同一批 task 的编排顺序可能不同
- 这类顺序更接近实例编排，而不是稳定能力本体

### 5.4 当前主 schema 里正式保留的顺序边

最终只保留两类稳定顺序边：

1. `FeatureTaskOrderEdge`
2. `TaskCommandOrderEdge`

---

## 6. 跨层共享结构

### 6.1 Rule

`Rule` 在不同层级都存在，只是约束对象不同：

- `BusinessRule`
- `FeatureRule`
- `TaskRule`
- `CommandRule`

统一属性：

- `rule_expression_mode`: `explicit / implicit`
- `rule_source_kind`: `principle / config / design / ops / case / restriction`

### 6.2 DecisionPoint

`DecisionPoint` 也是跨层同构对象：

- 业务层: 选择方案、特性、task
- 特性层: 选择 `SubFeature`、语义对象、task
- task 层: 选择命令集合、参数值模式、下游 task 分支
- 命令层: 不单独建 `DecisionPoint` 本体，最终由 `CommandRule` 和参数定义承接

### 6.3 SemanticObject

`SemanticObject` 是跨层统一语义对象，用来承接“业务意图先翻成语义单元，再落到特性、task、命令对象”。

统一关系：

- `NetworkScenario / ConfigurationSolution --uses_semantic_object--> SemanticObject`
- `Feature / SubFeature --uses_semantic_object--> SemanticObject`
- `ConfigTask --targets_semantic_object--> SemanticObject`
- `SemanticObject --realized_by--> ConfigObject`

### 6.4 License

`License` 是跨层共享本体，由 `Feature / SubFeature --requires_license--> License` 关联。

### 6.5 EvidenceSource

`EvidenceSource` 是独立证据层对象，用于统一承接原始 md、excel、pdf、txt 等材料。

统一关系：

- `AnyEntity --supported_by--> EvidenceSource`

---

## 7. 端到端链路

```text
BusinessDomain
  -> NetworkScenario
  -> ConfigurationSolution
  -> Feature / SubFeature
  -> ConfigTask
  -> MMLCommand
  -> ConfigObject / CommandParameter
```

必须成立的四条路径：

1. 业务方案可以先选特性，再展开 task。
2. 业务方案也可以直接选 task，不强制先选特性。
3. 特性可以拆成多个 task。
4. task 通过命令图谱落到底层命令、参数、配置对象。

---

## 8. 业务图谱 Schema

### 8.1 定位

业务图谱用于表达：

- 哪些业务域存在稳定的现网场景
- 某个场景采用什么配置方案
- 方案选择哪些特性、哪些通用 task
- 方案受哪些业务规则约束
- 方案在什么 scope 下成立
- 方案有哪些关键决策分叉

业务图谱不表达：

- 命令语法
- 参数定义
- 配置对象本体
- 逐条命令展开

### 8.2 保留对象

| 对象 | 中文名 | 定位 |
| --- | --- | --- |
| `BusinessDomain` | 业务域 | 业务知识空间根对象 |
| `NetworkScenario` | 现网场景 | 一类稳定需求/问题情境 |
| `ConfigurationSolution` | 配置方案 | 某场景下的一套方案闭包 |
| `DecisionPoint` | 决策点 | 业务层稳定选择点 |
| `BusinessRule` | 业务规则 | 业务层约束、选择逻辑、诊断和验收规则 |
| `SemanticObject` | 语义对象 | 业务语义桥接对象 |
| `EvidenceSource` | 原始证据 | 跨层复用的原始材料 |

### 8.3 BusinessDomain

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `domain_id` | string | 是 | 唯一标识 |
| `domain_name` | string | 是 | 业务域名称 |
| `domain_summary` | string | 是 | 一句话定义 |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 否 | 来源证据 |

### 8.4 NetworkScenario

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `scenario_id` | string | 是 | 唯一标识 |
| `scenario_name` | string | 是 | 场景名称 |
| `scenario_summary` | string | 是 | 一句话描述 |
| `judgment_basis` | string | 是 | 什么情况下属于该场景 |
| `typical_outcome` | string | 否 | 典型配置目标或问题结果 |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 是 | 来源证据 |

### 8.5 ConfigurationSolution

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `solution_id` | string | 是 | 唯一标识 |
| `solution_name` | string | 是 | 配置方案名称 |
| `solution_summary` | string | 是 | 方案闭包描述 |
| `design_intent` | string | 是 | 方案要解决什么问题 |
| `core_mechanism_combo` | string | 否 | 核心机制组合，保持业务语义，不写命令清单 |
| `scopes` | list[object] | 否 | 方案级 scope 子对象集合 |
| `participants` | list[object] | 否 | 方案级 participant 子对象集合 |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 是 | 来源证据 |

### 8.6 Scope 子对象

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `scope_name` | string | 是 | 范围名称 |
| `scope_summary` | string | 是 | 一句话说明该范围含义 |
| `scope_type` | enum | 是 | `subscriber / subscription / access / location / slice / service_selection / user_profile / other` |
| `scope_expression` | string | 否 | 原始表达或归一化表达 |

### 8.7 Participant 子对象

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `participant_name` | string | 是 | 参与方名称 |
| `participant_type` | enum | 是 | `endpoint / network_function / external_system / service_endpoint / access_side / other` |
| `responsibility_summary` | string | 是 | 稳定职责 |
| `plane_or_side` | string | 否 | 所在侧 |

### 8.8 DecisionPoint

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `decision_id` | string | 是 | 唯一标识 |
| `owner_layer` | enum | 是 | `business / feature / task` |
| `owner_ref_type` | string | 是 | 所属对象类型 |
| `owner_ref` | string | 是 | 所属对象 |
| `decision_name` | string | 是 | 决策点名称 |
| `decision_question` | string | 是 | 该决策实际回答什么问题 |
| `option_set` | list[string] | 是 | 可选分支集合 |
| `trigger_condition` | string | 否 | 在什么条件下需要做该决策 |
| `impact_summary` | string | 是 | 不同分支会影响哪些下层对象 |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 是 | 来源证据 |

### 8.9 BusinessRule

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `rule_id` | string | 是 | 唯一标识 |
| `rule_name` | string | 是 | 规则名称 |
| `rule_type` | enum | 是 | `selection_rule / scope_rule / design_rule / acceptance_rule / diagnosis_rule` |
| `rule_expression_mode` | enum | 是 | `explicit / implicit` |
| `rule_source_kind` | enum | 是 | `principle / config / design / ops / case / restriction` |
| `rule_logic` | string | 是 | 业务层规则逻辑 |
| `violation_effect` | string | 否 | 违反影响 |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 是 | 来源证据 |

### 8.10 SemanticObject

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `semantic_object_id` | string | 是 | 唯一标识 |
| `semantic_object_name` | string | 是 | 语义对象名称 |
| `semantic_summary` | string | 是 | 一句话语义说明 |
| `semantic_layer_hint` | enum | 否 | `business / feature / task / cross_layer` |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 否 | 来源证据 |

### 8.11 EvidenceSource

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `evidence_id` | string | 是 | 唯一标识 |
| `evidence_type` | enum | 是 | `markdown / excel / pdf / txt / other` |
| `title` | string | 是 | 原始材料标题 |
| `path` | string | 否 | 文件路径或逻辑定位 |
| `source_system` | string | 否 | 来源系统或来源目录 |
| `status` | enum | 是 | `draft / active / deprecated` |

### 8.12 业务图谱关系

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `BusinessDomain` | `contains` | `NetworkScenario` | 业务域包含场景 |
| `NetworkScenario` | `instantiated_as` | `ConfigurationSolution` | 场景收敛为方案 |
| `ConfigurationSolution` | `uses_feature` | `Feature / SubFeature` | 方案使用特性 |
| `ConfigurationSolution` | `uses_task` | `ConfigTask` | 方案使用 task |
| `NetworkScenario / ConfigurationSolution` | `has_decision` | `DecisionPoint` | 场景或方案包含决策点 |
| `NetworkScenario / ConfigurationSolution` | `constrained_by` | `BusinessRule` | 场景或方案受业务规则约束 |
| `NetworkScenario / ConfigurationSolution` | `uses_semantic_object` | `SemanticObject` | 场景或方案使用语义对象 |
| `BusinessDomain / NetworkScenario / ConfigurationSolution` | `supported_by` | `EvidenceSource` | 对象由原始证据支撑 |

---

## 9. 特性图谱 Schema

### 9.1 定位

特性图谱用于表达：

- 产品能力本体
- 能力之间的依赖和 license
- 单个能力在不同代际、模式、子场景下的稳定细分形态
- 某能力或其细分形态可以拆成哪些可复用 `ConfigTask`
- 特性级规则、决策和语义对象

这一版不单独引入 `FeatureVariant`。

如果某种差异只是轻量属性差异，不需要独立引用，则留在 `Feature` 属性中；  
如果某种差异需要单独挂 task、规则或决策，则建成 `SubFeature`。

### 9.2 保留对象

| 对象 | 中文名 | 定位 |
| --- | --- | --- |
| `Feature` | 特性 | 产品能力根对象 |
| `SubFeature` | 子特性 | 单个正式特性内部的稳定细分能力 |
| `FeatureRule` | 特性规则 | 特性级限制、编排规则、校验规则 |
| `DecisionPoint` | 决策点 | 特性层稳定选择点 |
| `FeatureTaskOrderEdge` | 特性到任务编排边 | 承载特性下 task 的稳定顺序与依赖 |
| `License` | License | 跨层共享 license 本体 |
| `SemanticObject` | 语义对象 | 跨层共享语义对象 |
| `EvidenceSource` | 原始证据 | 跨层复用的原始材料 |

### 9.3 Feature

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `feature_id` | string | 是 | 唯一标识 |
| `feature_name` | string | 是 | 特性名称 |
| `feature_summary` | string | 是 | 一句话定义 |
| `feature_group` | string | 否 | 特性分组 |
| `parent_feature_id` | string | 否 | 父特性 |
| `applicable_nf_map` | map | 否 | 支持 NF |
| `variant_dimensions` | list[string] | 否 | 常见细分维度 |
| `scopes` | list[object] | 否 | 特性级 scope 子对象集合 |
| `first_release` | string | 否 | 首发版本 |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 是 | 来源证据 |

### 9.4 SubFeature

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `subfeature_id` | string | 是 | 唯一标识 |
| `feature_id` | string | 是 | 所属 Feature |
| `subfeature_name` | string | 是 | 子特性名称 |
| `subfeature_dimension` | enum | 是 | `generation / deployment_mode / charging_mode / traffic_type / protocol / scenario / other` |
| `variant_condition` | string | 否 | 适用条件 |
| `subfeature_summary` | string | 否 | 说明 |
| `scopes` | list[object] | 否 | 子特性级 scope 子对象集合 |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 否 | 来源证据 |

### 9.5 License

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `license_id` | string | 是 | 唯一标识 |
| `license_name` | string | 是 | License 名称 |
| `license_summary` | string | 否 | 说明 |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 否 | 来源证据 |

### 9.6 FeatureRule

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `rule_id` | string | 是 | 唯一标识 |
| `owner_ref_type` | enum | 是 | `feature / subfeature` |
| `owner_ref` | string | 是 | 所属 Feature 或 SubFeature |
| `rule_name` | string | 是 | 规则名称 |
| `rule_type` | enum | 是 | `dependency_rule / task_selection_rule / naming_rule / consistency_rule / validation_rule / restriction_rule / scope_rule` |
| `rule_expression_mode` | enum | 是 | `explicit / implicit` |
| `rule_source_kind` | enum | 是 | `principle / config / design / ops / case / restriction` |
| `rule_logic` | string | 是 | 特性层规则逻辑 |
| `violation_effect` | string | 否 | 违反影响 |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 是 | 来源证据 |

### 9.7 FeatureTaskOrderEdge

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `edge_id` | string | 是 | 唯一标识 |
| `owner_ref_type` | enum | 是 | `feature / subfeature` |
| `owner_ref` | string | 是 | 所属 Feature 或 SubFeature |
| `from_task_ref` | string | 是 | 起点 task |
| `to_task_ref` | string | 是 | 终点 task |
| `relation_type` | enum | 是 | `precedes / depends_on / fallback_to / must_be_last` |
| `condition_ref` | string | 否 | 条件决策点引用 |
| `requiredness` | enum | 否 | `required / optional` |
| `priority_hint` | string | 否 | 优先级提示 |
| `propagated_context` | string | 否 | 从前一个 task 向后传播的关键上下文 |
| `source_evidence_ids` | list[string] | 是 | 来源证据 |

### 9.8 特性图谱关系

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `Feature` | `has_subfeature` | `SubFeature` | 特性包含子特性 |
| `Feature / SubFeature` | `depends_on` | `Feature / SubFeature` | 特性依赖关系 |
| `Feature / SubFeature` | `requires_license` | `License` | 特性依赖 License |
| `Feature / SubFeature` | `decomposes_to` | `ConfigTask` | 特性或其细分形态拆成 task |
| `Feature / SubFeature` | `uses_semantic_object` | `SemanticObject` | 使用语义对象 |
| `Feature / SubFeature` | `constrained_by` | `FeatureRule` | 受规则约束 |
| `Feature / SubFeature` | `has_decision` | `DecisionPoint` | 包含特性层决策点 |
| `Feature / SubFeature` | `orchestrates` | `FeatureTaskOrderEdge` | 特性层 task 编排边 |
| `Feature / SubFeature` | `supported_by` | `EvidenceSource` | 对象由原始证据支撑 |

---

## 10. 任务原子层 Schema

### 10.1 定位

`ConfigTask` 是最小可复用配置原子，满足三种情况：

1. 某个特性可以拆成多个 task。
2. 某个业务方案可以由多个特性组成。
3. 某些 task 没有明确单一特性归属，但可被多个特性、多个方案直接复用。

### 10.2 保留对象

| 对象 | 中文名 | 定位 |
| --- | --- | --- |
| `ConfigTask` | 配置任务原子 | 可复用配置动作单元 |
| `TaskRule` | 任务规则 | task 级选择、依赖、输入输出、复用约束 |
| `DecisionPoint` | 决策点 | task 层稳定选择点 |
| `TaskCommandOrderEdge` | 任务到命令编排边 | 承载 task 内部命令调用顺序与依赖 |
| `SemanticObject` | 语义对象 | 跨层共享语义对象 |
| `EvidenceSource` | 原始证据 | 跨层复用的原始材料 |

### 10.3 ConfigTask

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `task_id` | string | 是 | 唯一标识 |
| `task_name` | string | 是 | 任务名称 |
| `task_summary` | string | 是 | 一句话说明 |
| `task_scope_type` | enum | 是 | `feature_specific / cross_feature / generic` |
| `task_goal` | string | 是 | 该 task 要完成什么配置意图 |
| `input_contract` | string | 否 | 需要哪些输入 |
| `output_contract` | string | 否 | 产出哪些语义结果 |
| `scopes` | list[object] | 否 | task 级 scope 子对象集合 |
| `command_refs` | list[string] | 否 | 关联的底层命令集合 |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 是 | 来源证据 |

### 10.4 TaskRule

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `rule_id` | string | 是 | 唯一标识 |
| `task_ref` | string | 是 | 所属 task |
| `rule_name` | string | 是 | 规则名称 |
| `rule_type` | enum | 是 | `selection_rule / input_output_rule / naming_rule / dependency_rule / validation_rule / reuse_rule / scope_rule` |
| `rule_expression_mode` | enum | 是 | `explicit / implicit` |
| `rule_logic` | string | 是 | 规则逻辑 |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 否 | 来源证据 |

### 10.5 TaskCommandOrderEdge

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `edge_id` | string | 是 | 唯一标识 |
| `task_ref` | string | 是 | 所属 task |
| `from_command_ref` | string | 是 | 起点命令 |
| `to_command_ref` | string | 是 | 终点命令 |
| `relation_type` | enum | 是 | `precedes / depends_on / must_be_last` |
| `condition_ref` | string | 否 | 条件决策点引用 |
| `requiredness` | enum | 否 | `required / optional` |
| `propagated_context` | string | 否 | 如 `URRGROUPNAME / RULENAME / USERPROFILENAME` 等传播上下文 |
| `value_pattern_summary` | string | 否 | 参数值模式摘要 |
| `source_evidence_ids` | list[string] | 是 | 来源证据 |

### 10.6 任务原子层关系

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `ConfigTask` | `constrained_by` | `TaskRule` | task 受规则约束 |
| `ConfigTask` | `has_decision` | `DecisionPoint` | task 层决策点 |
| `ConfigTask` | `invokes` | `MMLCommand` | task 调用命令 |
| `ConfigTask` | `targets` | `SemanticObject / ConfigObject` | task 操作目标 |
| `ConfigTask` | `orchestrates` | `TaskCommandOrderEdge` | task 内部命令编排边 |
| `ConfigTask` | `may_require_feature` | `Feature / SubFeature` | 某 task 需要某特性前提 |
| `ConfigTask` | `supported_by` | `EvidenceSource` | 对象由原始证据支撑 |

---

## 11. 命令图谱 Schema

### 11.1 定位

命令图谱用于表达：

- MML 命令本体
- 参数本体
- 配置对象本体
- 命令级约束

### 11.2 保留对象

| 对象 | 中文名 | 定位 |
| --- | --- | --- |
| `MMLCommand` | MML 命令 | 命令本体 |
| `CommandParameter` | 命令参数 | 参数本体 |
| `ConfigObject` | 配置对象 | 稳定配置对象本体 |
| `CommandRule` | 命令规则 | 语法、语义、删除、依赖、引用约束 |

### 11.3 MMLCommand

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `command_id` | string | 是 | 唯一标识 |
| `command_name` | string | 是 | 命令名称，如 `ADD URR` |
| `verb` | string | 是 | 动作，如 `ADD / SET / DEL / MOD / LST` |
| `object_keyword` | string | 是 | 命令对象关键字 |
| `command_summary` | string | 否 | 命令说明 |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 是 | 来源证据 |

### 11.4 CommandParameter

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `parameter_id` | string | 是 | 唯一标识 |
| `command_ref` | string | 是 | 所属命令 |
| `parameter_name` | string | 是 | 参数名 |
| `data_type` | string | 否 | 数据类型 |
| `required_mode` | enum | 是 | `required / optional / conditional_required` |
| `default_value` | string | 否 | 默认值 |
| `enum_values` | list[string] | 否 | 枚举值 |
| `description` | string | 否 | 说明 |
| `source_evidence_ids` | list[string] | 否 | 来源证据 |

### 11.5 ConfigObject

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `object_id` | string | 是 | 唯一标识 |
| `object_name` | string | 是 | 对象名称 |
| `identifier_parameters` | list[string] | 否 | 标识参数 |
| `object_kind` | enum | 否 | `entity / binding / composite / other` |
| `description` | string | 否 | 说明 |
| `source_evidence_ids` | list[string] | 否 | 来源证据 |

### 11.6 CommandRule

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `rule_id` | string | 是 | 唯一标识 |
| `rule_name` | string | 是 | 规则名称 |
| `rule_type` | enum | 是 | `syntax_rule / semantic_rule / precondition_rule / delete_constraint / parameter_mutex / parameter_dependency / object_reference_rule / runtime_check_rule` |
| `rule_expression_mode` | enum | 是 | `explicit / implicit` |
| `rule_source_kind` | enum | 是 | `principle / config / design / ops / case / restriction` |
| `scope_type` | enum | 是 | `command / parameter / object / relation` |
| `scope_ref` | string | 是 | 作用对象 |
| `rule_logic` | string | 是 | 命令级规则逻辑 |
| `violation_effect` | string | 否 | 违反影响 |
| `severity` | enum | 是 | `critical / warning / info` |
| `source_evidence_ids` | list[string] | 是 | 来源证据 |

### 11.7 命令图谱关系

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `MMLCommand` | `has_parameter` | `CommandParameter` | 命令包含参数 |
| `MMLCommand` | `operates_on` | `ConfigObject` | 命令操作对象 |
| `CommandParameter` | `references` | `ConfigObject` | 参数引用对象 |
| `ConfigObject` | `contains / refers_to / depends_on / conflicts_with / composed_by / activates` | `ConfigObject` | 对象关系直接作为边 |
| `CommandRule` | `governs` | `MMLCommand / CommandParameter / ConfigObject` | 命令规则治理 |

---

## 12. 跨层映射

### 12.1 业务图谱 -> 特性图谱

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `ConfigurationSolution` | `uses_feature` | `Feature / SubFeature` | 方案使用特性 |
| `BusinessRule` | `refined_by` | `FeatureRule` | 业务规则细化为特性规则 |
| `SemanticObject` | `realized_by` | `Feature / SubFeature` | 语义对象由能力承接 |

### 12.2 业务图谱 -> 任务原子层

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `ConfigurationSolution` | `uses_task` | `ConfigTask` | 方案直接使用 task |
| `BusinessRule` | `refined_by` | `TaskRule` | 业务规则可细化为 task 使用规则 |
| `SemanticObject` | `realized_by` | `ConfigTask` | 语义对象由 task 落地 |

### 12.3 特性图谱 -> 任务原子层

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `Feature / SubFeature` | `decomposes_to` | `ConfigTask` | 特性拆成 task |
| `FeatureRule` | `constrains_task` | `ConfigTask` | 特性规则约束 task 使用方式 |

### 12.4 任务原子层 -> 命令图谱

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `ConfigTask` | `invokes` | `MMLCommand` | task 调用命令 |
| `ConfigTask` | `targets` | `SemanticObject / ConfigObject` | task 操作目标 |
| `ConfigTask` | `orchestrates` | `TaskCommandOrderEdge` | task 内部命令编排边 |
| `TaskRule` | `refined_by` | `CommandRule` | task 规则落到底层命令约束 |

### 12.5 DecisionPoint 影响关系

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `DecisionPoint` | `selects` | `Feature / SubFeature / ConfigTask / MMLCommand / CommandParameter` | 决策点选择作用对象 |
| `DecisionPoint` | `sets_value_pattern` | `CommandParameter` | 决策点影响参数值模式 |
| `DecisionPoint` | `conditioned_by_scope` | `scope sub-object` | 决策点受宿主对象内的范围子对象约束 |

---

## 13. 禁止的关系

| 关系 | 原因 | 替代 |
| --- | --- | --- |
| `ConfigurationSolution -> ConfigObject` | 业务层直接坠落到底层对象 | `ConfigurationSolution -> Feature / Task` |
| `ConfigurationSolution -> MMLCommand` | 业务层直接拥有命令实例 | `ConfigurationSolution -> ConfigTask -> MMLCommand` |
| `BusinessRule -> CommandParameter` 直接写死参数值 | 业务规则过度下沉 | `BusinessRule -> DecisionPoint / TaskRule / CommandRule` |
| `Feature -> MMLCommand` 直接强绑定 | 特性不应跳过 task 层直接落命令 | `Feature / SubFeature -> ConfigTask -> MMLCommand` |
| `Feature -> ConfigObject` 携带参数差异 | 特性差异不是对象本体差异 | `SemanticObject` 或 `FeatureRule` |
| 业务图谱内建 `ConfigObject` 实体 | 业务层没有对象本体所有权 | 由任务层和命令层承接 |
| `ConfigurationSolution -> ConfigTask` 的完整顺序链 | 当前案例中条件分支过强，方案级编排不够稳定 | 暂只保留 `uses_task`，顺序待实例层承接 |
