# 三层图谱收敛 Schema 草案

> 草案版本: v0.8
> 目标: 从本体角度构建云核心网 MML 配置数字孪生，明确业务图谱、特性图谱、任务原子、命令图谱的边界，避免重复建模。
> 适用范围: SFCGraph 当前业务图谱、特性图谱、命令图谱的统一 schema 收敛讨论。

---

## 1. 总体定位

当前最需要解决的不是“文档来自哪里”，而是“对象在知识世界里处于哪一层”。

结合现有业务图谱、计费统一知识库、计费特性文档、命令文档，建议把配置数字孪生拆成四个稳定层次：

```text
业务图谱 Business Graph
  回答: 为什么配、在什么现网场景下配、采用什么配置方案

特性图谱 Feature Graph
  回答: 产品能力是什么、能力在不同模式/代际/子场景下如何细分

任务原子层 Task Graph
  回答: 哪些可复用配置动作可以持续积累、复用于多个特性和方案

命令图谱 Command Graph
  回答: MML 命令、参数、配置对象、命令级规则是什么

证据层 Evidence Layer
  回答: 哪些原始 md/excel/pdf/txt 材料支撑这些对象和关系
```

如果对外仍然坚持“三层图谱”表述，可以理解为：

- 业务图谱
- 特性图谱
- 命令图谱

其中 `ConfigTask` 作为跨业务/特性的公共原子层，建模上独立存在，但可视为特性图谱与业务图谱之间的共享层。

---

## 2. 核心原则

1. 图谱按“本体层级”解耦，不按“文档来源”解耦。
2. 稳定可复用对象建成 `Canonical Entity`，只在某个方案上下文里成立的对象不轻易实体化。
3. `Feature` 是能力本体，`SubFeature` 是该能力在特定维度下的细分形态，不再单独引入 `FeatureVariant`。
4. `ConfigTask` 是最小可复用配置原子，不强制隶属于某个 Feature，也不强制隶属于某个业务方案。
5. task 的差异优先通过 `DecisionPoint + 关系边 + TaskRule` 表达，不单独抽象 `TaskVariant`。
6. 如果 `ConfigTask` 已经是最小复用原子，就不再单独建 `ConfigStep`。
7. 配置对象、参数、对象关系、命令约束全部归命令图谱。
8. `Rule` 和 `DecisionPoint` 都是跨层同构结构，只是作用层级不同。
9. `SemanticObject`、`License`、`EvidenceSource` 是跨层共享本体，不归属于某一层独占。
10. 业务图谱不直接拥有 `ConfigObject`、`CommandParameter`、`MMLCommand` 本体。
11. 顺序、依赖、兜底、最后执行等稳定编排信息优先由带属性的边承载，而不是回填为节点属性。

---

## 3. 跨层同构结构

这一版明确两个从上到下贯穿的结构：`Rule` 和 `DecisionPoint`。

### 3.1 Rule

`Rule` 从上到下都存在，只是约束对象不同：

- `BusinessRule`: 约束场景、方案、业务验收和业务选择
- `FeatureRule`: 约束能力适用条件、能力差异、能力组合
- `TaskRule`: 约束 task 选择、输入输出依赖、命名和复用边界
- `CommandRule`: 约束命令、参数、对象、引用、删除和运行时合法性

统一属性建议：

- `rule_expression_mode`: `explicit / implicit`
- `rule_source_kind`: `principle / config / design / ops / case / restriction`

### 3.2 DecisionPoint

`DecisionPoint` 也不是业务层独有，而是跨层结构：

- 业务层 DecisionPoint: 选择方案、特性、task
- 特性层 DecisionPoint: 选择 SubFeature、SemanticObject、task
- task 层 DecisionPoint: 选择命令集合、参数值模式、下游 task 分支
- 命令层不单独建 DecisionPoint 本体；命令层的可选项通常收敛为 `CommandRule`、参数枚举、条件参数依赖

`DecisionPoint` 的本体含义不是“选特性”本身，而是：

```text
在某个 owner 上下文中，
面对一组候选配置结构，
根据条件选择其中一部分，
并把影响向下传递。
```

它的影响对象可以是：

- `Feature / SubFeature`
- `ConfigTask`
- `MMLCommand`
- `CommandParameter`
- 参数值或值模式

但向下传递的方式应该分层：

- 业务层尽量只影响 feature/task 选择
- 特性层可以影响 task 选择
- task 层可以影响命令集合和参数值模式
- 命令层用 `CommandRule` 承接最终的参数约束

### 3.3 SemanticObject

原 `DomainSemanticObject` 和 `FeatureSemanticObject` 在本体上合并为统一对象：

- `SemanticObject`

原因：

- 它们本质上都是“配置数字孪生中的语义对象”
- 区别主要在于被哪一层引用，而不是对象本体不同
- 用关系表达层级归属，比拆两套对象更干净

统一关系方式：

- `NetworkScenario / ConfigurationSolution --uses_semantic_object--> SemanticObject`
- `Feature / SubFeature --uses_semantic_object--> SemanticObject`
- `ConfigTask --targets_semantic_object--> SemanticObject`
- `SemanticObject --realized_by--> ConfigObject`

### 3.4 EvidenceSource

`DocAsset` 不再作为特性层专属资产对象保留。

原始 md 文档、原始表格、原始说明材料更适合作为跨层统一证据本体：

- `EvidenceSource`: 原始证据对象

它独立于业务、特性、task、命令四层之外，作为统一证据层存在，避免每层各自维护一套“文档资产”。

### 3.5 Orchestration Edge

这一版基于计费场景实例，正式补充两类稳定编排边：

1. `FeatureTaskOrderEdge`
2. `TaskCommandOrderEdge`

结论边界：

- `Feature/SubFeature -> ConfigTask` 的稳定配置顺序，可以进入主 schema
- `ConfigTask -> MMLCommand` 的稳定调用顺序，可以进入主 schema
- `ConfigurationSolution -> ConfigTask` 的完整方案级编排，当前案例中条件分支过强，暂不进入主 schema

设计原则：

- 这些边是 `canonical edge`
- 但不是“无主全局边”
- 它们必须显式挂在所属 `Feature/SubFeature` 或 `ConfigTask` 上

---

## 4. 两类对象

### 4.1 Canonical Entity

稳定知识对象，可跨方案复用、长期积累、可被多次引用。

典型对象：

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

这些对象不属于某一层独占：

- `SemanticObject`
- `License`
- `EvidenceSource`

### 4.3 子对象

这一版把 `Scope`、`Participant` 从一级实体降为宿主对象下的子对象。

原因：

- 它们更像方案、特性、task 的限定上下文
- 独立生命周期较弱
- 作为子对象更贴近当前知识密度

### 4.4 不再单独建模的弱对象

这一版明确删除以下对象：

- `SolutionFeatureUse`
- `SolutionTaskUse`
- `AcceptanceCriterion`
- `ProducedArtifact`
- `ConfigStep`
- `TaskVariant`

原因：

- 只是多对多边的实体化包装
- 语义边界不稳
- 当前增益不足，容易制造重复

---

## 5. 端到端链路

```text
BusinessDomain
  -> NetworkScenario
  -> ConfigurationSolution
  -> Feature / SubFeature
  -> ConfigTask
  -> MMLCommand
  -> ConfigObject / CommandParameter
```

其中有四条必须成立的路径：

1. 业务方案可以先选特性，再展开 task
2. 业务方案也可以直接选 task，不强制先选特性
3. 特性可以拆为多个 task
4. task 的差异通过决策点、规则和关系边映射到底层命令

---

## 6. 业务图谱 Schema

### 6.1 业务图谱定位

业务图谱用于表达：

- 哪些业务域存在稳定的现网场景
- 某个场景采用什么配置方案
- 方案选择哪些特性、哪些通用 task
- 方案受哪些业务规则约束
- 方案在什么 scope 下成立
- 方案有哪些关键决策分叉

业务图谱不用于表达：

- 命令语法
- 参数定义
- 配置对象本体
- 对象组合关系
- 逐条命令展开

### 6.2 保留对象

| 对象 | 中文名 | 定位 |
| --- | --- | --- |
| `BusinessDomain` | 业务域 | 业务知识空间根对象 |
| `NetworkScenario` | 现网场景 | 一类稳定需求/问题情境 |
| `ConfigurationSolution` | 配置方案 | 某场景下的一套方案闭包 |
| `DecisionPoint` | 决策点 | 业务层稳定选择点 |
| `BusinessRule` | 业务规则 | 业务层约束、选择逻辑、诊断和验收规则 |
| `EvidenceSource` | 原始证据 | 跨层复用的原始文档/表格/说明材料 |

### 6.3 BusinessDomain

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `domain_id` | string | 是 | 唯一标识 |
| `domain_name` | string | 是 | 业务域名称 |
| `domain_summary` | string | 是 | 一句话定义 |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 否 | 来源证据 |

### 6.4 NetworkScenario

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `scenario_id` | string | 是 | 唯一标识 |
| `scenario_name` | string | 是 | 场景名称 |
| `scenario_summary` | string | 是 | 一句话描述 |
| `judgment_basis` | string | 是 | 什么情况下属于该场景 |
| `typical_outcome` | string | 否 | 典型配置目标或问题结果 |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 是 | 来源证据 |

### 6.5 ConfigurationSolution

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

### 6.6 Scope 子对象

> `Scope` 不再单独建模为一级实体，作为方案、特性、task 的子对象使用。

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `scope_name` | string | 是 | 范围名称 |
| `scope_summary` | string | 是 | 一句话说明该范围含义 |
| `scope_type` | enum | 是 | `subscriber / subscription / access / location / slice / service_selection / user_profile / other` |
| `scope_expression` | string | 否 | 原始表达或归一化表达 |

### 6.7 Participant 子对象

> `Participant` 不再单独建模为一级实体，作为方案级子对象使用。

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `participant_name` | string | 是 | 参与方名称 |
| `participant_type` | enum | 是 | `endpoint / network_function / external_system / service_endpoint / access_side / other` |
| `responsibility_summary` | string | 是 | 稳定职责 |
| `plane_or_side` | string | 否 | 所在侧 |

### 6.8 DecisionPoint

> `DecisionPoint` 用统一 schema 跨层复用。业务层只是它的一种 owner。

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `decision_id` | string | 是 | 唯一标识 |
| `owner_layer` | enum | 是 | `business / feature / task` |
| `owner_ref_type` | string | 是 | 所属对象类型 |
| `owner_ref` | string | 是 | 所属对象 |
| `decision_name` | string | 是 | 决策点名称 |
| `decision_question` | string | 是 | 该决策实际在回答什么问题 |
| `option_set` | list[string] | 是 | 可选分支集合 |
| `trigger_condition` | string | 否 | 在什么条件下需要做该决策 |
| `impact_summary` | string | 是 | 不同分支会影响哪些下层对象 |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 是 | 来源证据 |

### 6.9 BusinessRule

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

### 6.10 SemanticObject

> 这是从原业务图谱补回来的关键桥接对象。它承接“业务意图先翻成语义单元，再落到特性和 task”，避免业务直接坠落到底层命令对象。

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `semantic_object_id` | string | 是 | 唯一标识 |
| `semantic_object_name` | string | 是 | 语义对象名称 |
| `semantic_summary` | string | 是 | 一句话语义说明 |
| `semantic_layer_hint` | enum | 否 | `business / feature / task / cross_layer` |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 否 | 来源证据 |

### 6.11 EvidenceSource

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `evidence_id` | string | 是 | 唯一标识 |
| `evidence_type` | enum | 是 | `markdown / excel / pdf / txt / other` |
| `title` | string | 是 | 原始材料标题 |
| `path` | string | 否 | 文件路径或逻辑定位 |
| `source_system` | string | 否 | 来源系统或来源目录 |
| `status` | enum | 是 | `draft / active / deprecated` |

### 6.12 业务图谱关系

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

## 7. 特性图谱 Schema

### 7.1 特性图谱定位

特性图谱用于表达：

- 产品能力本体
- 能力之间的依赖和 license
- 能力在不同代际、模式、子场景下的细分形态
- 某能力或其细分形态可以拆成哪些可复用 `ConfigTask`
- 特性级规则、决策和语义对象

### 7.2 关于 `FeatureVariant` 与 `SubFeature`

这一版明确做一个收敛：

1. 不单独保留 `FeatureVariant` 这个名字。
2. 特性的“变体”如果具备稳定语义身份、会被任务/规则/方案单独引用，就建成 `SubFeature`。
3. 特性的“变体”如果只是轻量差异，不需要独立引用，可以作为 `Feature` 的属性表达。

### 7.3 保留对象

| 对象 | 中文名 | 定位 |
| --- | --- | --- |
| `Feature` | 特性 | 产品能力根对象 |
| `SubFeature` | 子特性 | 特性在代际、模式、子场景下的细分能力 |
| `FeatureRule` | 特性规则 | 特性级限制、编排规则、校验规则 |
| `DecisionPoint` | 决策点 | 特性层稳定选择点 |
| `FeatureTaskOrderEdge` | 特性到任务编排边 | 承载特性下 task 的稳定顺序与依赖 |
| `License` | License | 跨层共享 license 本体 |
| `SemanticObject` | 语义对象 | 跨层共享语义对象 |
| `EvidenceSource` | 原始证据 | 跨层复用的原始文档/表格/说明材料 |

### 7.4 Feature

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

### 7.5 SubFeature

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

### 7.6 License

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `license_id` | string | 是 | 唯一标识 |
| `license_name` | string | 是 | License 名称 |
| `license_summary` | string | 否 | 说明 |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 否 | 来源证据 |

### 7.7 FeatureRule

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

### 7.8 FeatureTaskOrderEdge

> 用于承载某个 `Feature` 或 `SubFeature` 下 task 的稳定配置顺序、依赖和兜底关系。

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

### 7.9 特性图谱关系

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `Feature` | `has_subfeature` | `SubFeature` | 特性包含子特性 |
| `Feature / SubFeature` | `depends_on` | `Feature / SubFeature` | 特性依赖关系 |
| `Feature / SubFeature` | `requires_license` | `License` | 特性依赖 License |
| `Feature / SubFeature` | `decomposes_to` | `ConfigTask` | 特性或其变体拆成 task |
| `Feature / SubFeature` | `uses_semantic_object` | `SemanticObject` | 使用语义对象 |
| `Feature / SubFeature` | `constrained_by` | `FeatureRule` | 受规则约束 |
| `Feature / SubFeature` | `has_decision` | `DecisionPoint` | 包含特性层决策点 |
| `Feature / SubFeature` | `orchestrates` | `FeatureTaskOrderEdge` | 特性层 task 编排边 |
| `Feature / SubFeature` | `supported_by` | `EvidenceSource` | 对象由原始证据支撑 |

---

## 8. 任务原子层 Schema

### 8.1 任务原子层定位

`ConfigTask` 是最小可复用配置原子，满足三种情况：

1. 某个特性可以拆成多个 task
2. 某个业务方案可以由多个特性组成
3. 某些 task 没有明确单一特性归属，但可以被多个特性、多个方案直接复用

这一版明确：

- `ConfigTask` 保留
- `TaskVariant` 删除
- `ConfigStep` 删除

### 8.2 保留对象

| 对象 | 中文名 | 定位 |
| --- | --- | --- |
| `ConfigTask` | 配置任务原子 | 可复用配置动作单元 |
| `TaskRule` | 任务规则 | task 级选择、依赖、输入输出、复用约束 |
| `DecisionPoint` | 决策点 | task 层稳定选择点 |
| `TaskCommandOrderEdge` | 任务到命令编排边 | 承载 task 内部命令调用顺序与依赖 |
| `SemanticObject` | 语义对象 | 跨层共享语义对象 |
| `EvidenceSource` | 原始证据 | 跨层复用的原始文档/表格/说明材料 |

### 8.3 ConfigTask

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
| `command_refs` | list[string] | 否 | 该 task 在当前定义下关联的底层命令集合 |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 是 | 来源证据 |

### 8.4 TaskRule

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

### 8.5 TaskCommandOrderEdge

> 用于承载某个 `ConfigTask` 内部命令调用的稳定顺序、依赖、最后执行约束和关键上下文传播。

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

### 8.6 任务原子层关系

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

## 9. 命令图谱 Schema

### 9.1 命令图谱定位

命令图谱用于表达：

- MML 命令本体
- 参数本体
- 配置对象本体
- 绑定对象本体
- 对象关系
- 命令级约束

### 9.2 保留对象

| 对象 | 中文名 | 定位 |
| --- | --- | --- |
| `MMLCommand` | MML 命令 | 命令本体 |
| `CommandParameter` | 命令参数 | 参数本体 |
| `ConfigObject` | 配置对象 | 稳定配置对象本体 |
| `CommandRule` | 命令规则 | 语法、语义、删除、依赖、引用约束 |

### 9.3 MMLCommand

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `command_id` | string | 是 | 唯一标识 |
| `command_name` | string | 是 | 命令名称，如 `ADD URR` |
| `verb` | string | 是 | 动作，如 `ADD / SET / DEL / MOD / LST` |
| `object_keyword` | string | 是 | 命令对象关键字 |
| `command_summary` | string | 否 | 命令说明 |
| `status` | enum | 是 | `draft / active / deprecated` |
| `source_evidence_ids` | list[string] | 是 | 来源证据 |

### 9.4 CommandParameter

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

### 9.5 ConfigObject

| 字段 | 类型 | 必选 | 说明 |
| --- | --- | --- | --- |
| `object_id` | string | 是 | 唯一标识 |
| `object_name` | string | 是 | 对象名称 |
| `identifier_parameters` | list[string] | 否 | 标识参数 |
| `object_kind` | enum | 否 | `entity / binding / composite / other` |
| `description` | string | 否 | 说明 |
| `source_evidence_ids` | list[string] | 否 | 来源证据 |

### 9.6 CommandRule

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

### 9.7 命令图谱关系

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `MMLCommand` | `has_parameter` | `CommandParameter` | 命令包含参数 |
| `MMLCommand` | `operates_on` | `ConfigObject` | 命令操作对象 |
| `CommandParameter` | `references` | `ConfigObject` | 参数引用对象 |
| `ConfigObject` | `contains / refers_to / depends_on / conflicts_with / composed_by / activates` | `ConfigObject` | 对象关系直接作为边 |
| `CommandRule` | `governs` | `MMLCommand / CommandParameter / ConfigObject` | 命令规则治理 |

---

## 10. 跨层映射

### 10.1 业务图谱 -> 特性图谱

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `ConfigurationSolution` | `uses_feature` | `Feature / SubFeature` | 方案使用特性 |
| `BusinessRule` | `refined_by` | `FeatureRule` | 业务规则细化为特性规则 |
| `SemanticObject` | `realized_by` | `Feature / SubFeature` | 语义对象由能力承接 |

### 10.2 业务图谱 -> 任务原子层

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `ConfigurationSolution` | `uses_task` | `ConfigTask` | 方案直接使用 task |
| `BusinessRule` | `refined_by` | `TaskRule` | 业务规则可细化为 task 使用规则 |
| `SemanticObject` | `realized_by` | `ConfigTask` | 语义对象由 task 落地 |

### 10.3 特性图谱 -> 任务原子层

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `Feature / SubFeature` | `decomposes_to` | `ConfigTask` | 特性拆成 task |
| `FeatureRule` | `constrains_task` | `ConfigTask` | 特性规则约束 task 使用方式 |

### 10.4 任务原子层 -> 命令图谱

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `ConfigTask` | `invokes` | `MMLCommand` | task 调用命令 |
| `ConfigTask` | `targets` | `SemanticObject / ConfigObject` | task 操作目标 |
| `ConfigTask` | `orchestrates` | `TaskCommandOrderEdge` | task 内部命令编排边 |
| `TaskRule` | `refined_by` | `CommandRule` | task 规则落到底层命令约束 |

### 10.5 DecisionPoint 的影响关系

> 这一版不再把 `DecisionPoint` 限定为“只选 feature/task”。它是通用影响点，但各层应遵守自己的下沉边界。

| 起点 | 关系 | 终点 | 说明 |
| --- | --- | --- | --- |
| `DecisionPoint` | `selects` | `Feature / SubFeature / ConfigTask / MMLCommand / CommandParameter` | 决策点选择作用对象 |
| `DecisionPoint` | `sets_value_pattern` | `CommandParameter` | 决策点影响参数值模式 |
| `DecisionPoint` | `conditioned_by_scope` | `scope sub-object` | 决策点受宿主对象内的范围子对象约束 |

---

## 11. 禁止的关系

以下关系不建议作为主 schema 保留：

| 关系 | 原因 | 替代 |
| --- | --- | --- |
| `ConfigurationSolution -> ConfigObject` | 业务层直接坠落到底层对象 | `ConfigurationSolution -> Feature / Task` |
| `ConfigurationSolution -> MMLCommand` | 业务层直接拥有命令实例 | `ConfigurationSolution -> ConfigTask -> MMLCommand` |
| `BusinessRule -> CommandParameter` 直接写死参数值 | 业务规则过度下沉 | `BusinessRule -> DecisionPoint / TaskRule / CommandRule` |
| `Feature -> MMLCommand` 直接强绑定 | 特性不应跳过 task 层直接落命令 | `Feature / SubFeature -> ConfigTask -> MMLCommand` |
| `Feature -> ConfigObject` 携带参数差异 | 特性差异不是对象本体差异 | `SemanticObject` 或 `FeatureRule` |
| 业务图谱内建 `ConfigObject` 实体 | 业务层没有对象本体所有权 | 由任务层和命令层承接 |
| `ConfigurationSolution -> ConfigTask` 的完整顺序链 | 当前案例中条件分支过强，方案级编排不够稳定 | 暂只保留 `uses_task`，顺序待实例层承接 |

---

## 12. 基于原业务图谱的补充审查

对照 [business-graph-schema-final.md](</D:/mywork/KnowledgeBase/SFCGraph/business-graph/business-graph-schema-final.md>)，这轮补回或重判了三类内容：

### 12.1 补回的关键对象

1. `Scope`
   原因：计费场景里 subscriber/access/location/slice 等范围非常关键，不应丢。
   处理：保留语义，但降为宿主对象下的子对象。

2. `SemanticObject`
   原因：业务语义需要一个桥接层，否则业务会直接跳到底层 Feature 或命令对象。

3. `DecisionPoint`
   原因：原 schema 已经证明它是核心结构，但需要从“业务层对象”升级成“跨层同构对象”。

### 12.2 降级或删除的对象

1. `SolutionFeatureUse / SolutionTaskUse`
   原因：只是多对多边的实体化包装，当前增益不足。

2. `ValidationPlan / AcceptanceCriterion`
   原因：当前阶段增益不足；先把验收收回 `BusinessRule.rule_type=acceptance_rule`。

3. `ProducedArtifact`
   原因：容易变成兜底杂项对象。

### 12.3 待你继续判断的对象

1. `ConfigurationSolution`
   目前仍保留为稳定对象。
   如果你后续判断“方案也只是场景上下文中的实例而非长期知识对象”，还可以继续降。

### 12.4 基于实例得到的顺序结论

当前案例能稳定支持进入主 schema 的顺序只有两类：

1. `Feature/SubFeature -> ConfigTask`
   例如内容计费场景下，计费动作链、Rule配置、UserProfile绑定、缺省费率和刷新生效存在稳定先后关系。

2. `ConfigTask -> MMLCommand`
   例如 `ADD URR -> ADD URRGROUP -> ADD PCCPOLICYGRP`、`ADD USERPROFILE -> ADD RULEBINDING -> SET URRGRPBINDING -> SET REFRESHSRV`。

当前案例不建议进入主 schema 的顺序：

1. `ConfigurationSolution -> ConfigTask` 完整顺序链
   原因：受 `DP-00/DP-01/DP-03` 等条件分支影响过强，更像方案实例编排而不是稳定本体顺序。

---

## 13. 计费场景示例映射

### 13.1 业务层

```text
BusinessDomain: 业务感知
  -> NetworkScenario: 计费场景
  -> ConfigurationSolution: 差异化计费配置方案
  -> DecisionPoint:
       - 在线 / 离线 / 融合计费
       - 以 UserProfile / DNN / CC 哪一层生效
  -> SemanticObject:
       - Charging
       - RatingGroup
       - QuotaControl
```

### 13.2 特性层

```text
Feature: GWFD-020301 内容计费基本功能
  -> SubFeature: URL 内容计费
  -> SubFeature: 应用内容计费
  -> FeatureRule:
       - 多 NF 名称一致性
       - 某模式下必须走特定 task 组合
  -> DecisionPoint:
       - 采用哪类识别方式
  -> FeatureTaskOrderEdge:
       - 配置计费动作链 precedes 配置Rule
       - 配置Rule precedes 配置UserProfile与Rule绑定
       - 配置UserProfile与Rule绑定 precedes 刷新生效
```

### 13.3 task 层

```text
ConfigTask: 创建匹配规则
  -> DecisionPoint:
       - 选择 URL 识别还是应用识别
       - 是否下发兜底默认规则
       - 是否绑定默认 URR 组
  -> invokes:
       - ADD FILTER
       - ADD L7FILTER
       - ADD FLOWFILTER
       - ADD RULE
  -> TaskCommandOrderEdge:
       - ADD FILTER precedes ADD FLOWFILTER
       - ADD L7FILTER precedes ADD RULE
       - ADD FLOWFILTER precedes ADD RULE

ConfigTask: 配置计费动作链
  -> TaskCommandOrderEdge:
       - ADD URR precedes ADD URRGROUP
       - ADD URRGROUP precedes ADD PCCPOLICYGRP

ConfigTask: 配置UserProfile与Rule绑定
  -> TaskCommandOrderEdge:
       - ADD USERPROFILE precedes ADD RULEBINDING
       - ADD RULEBINDING precedes SET URRGRPBINDING
       - SET URRGRPBINDING precedes SET REFRESHSRV
       - SET REFRESHSRV relation_type=must_be_last
```

### 13.4 命令层

```text
MMLCommand:
  ADD URR
  ADD URRGROUP
  ADD PCCPOLICYGRP
  ADD RULE
  SET URRGRPBINDING

CommandRule:
  URRID 全局唯一
  URRGROUP 至少包含一个 URR
  PCCPOLICYGRP 被引用时不能直接删除
  未配置默认 URR 组时可能导致不计费
```

---

## 14. 审查清单

审查时建议重点确认这些问题：

1. `SubFeature` 是否足以承接你所说的特性层“变体”，从而不再需要 `FeatureVariant`。
2. `ConfigTask` 是否应明确为最小可复用配置原子。
3. task 层差异是否用 `DecisionPoint + 关系边 + TaskRule` 表达，而不再需要 `TaskVariant / ConfigStep`。
4. `DecisionPoint` 是否应统一为跨层对象，而不是业务层独有对象。
5. `DecisionPoint` 影响到命令/参数/值时，是否仍然坚持通过 task 层转译，而不是业务层直达命令层。
6. `Scope` 作为子对象而非一级实体，是否更符合当前知识密度。
7. `SemanticObject` 是否应作为业务到特性/task 的稳定桥接层保留。
8. `EvidenceSource` 是否应替代原 `DocAsset` 成为跨层统一证据本体。

---

## 15. 一句话收敛

```text
业务图谱组织场景、方案、范围和高层决策；
特性图谱组织能力及其细分形态；
任务原子层组织可复用配置动作，并通过决策点和规则表达差异；
命令图谱组织 MML 配置本体；
Rule 和 DecisionPoint 贯穿各层，但下沉深度受层级约束。
```
