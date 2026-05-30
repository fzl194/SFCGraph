# 业务感知业务图谱合并审查与演进方案 v0.2

## 1. 本页定位

本页合并两份审查意见：

1. 构建 Agent 自查：关注业务图谱构建逻辑、当前闭包质量、运行/验收/诊断/风险缺口。
2. 独立审查 Agent 报告：关注 schema 落地完整性、CSV 可消费性、MD 与 CSV 不一致、证据悬空和对象粒度问题。

本页目标不是证明当前结果正确，而是形成一个可执行的判断：

```text
当前 business-graph 到底处于什么状态，
哪些东西可以保留，
哪些是明确错误，
哪些需要你做设计决策，
下一轮应该先做什么。
```

## 2. 总体结论

当前方向是对的，但当前结果还不能称为完整三层闭包。

更准确的状态是：

```text
business-graph 已经形成了“业务感知业务图谱”的方法框架、
两条业务主线的关系骨架、
以及部分场景、方案、能力、任务、证据实例。

但核心桥接实体还没有完全 CSV 化，
运行/验收/诊断/风险对象还没有实例化，
证据还停留在页面摘要级别。
```

所以当前不是：

```text
已经完成业务感知业务图谱 MVP
```

而是：

```text
完成了业务感知业务图谱 MVP 的第一版骨架，
下一步必须把骨架补成可程序消费、可审查、可迭代的闭包。
```

## 3. 已确认正确的部分

### 3.1 分层方向正确

当前采用的主链是合理的：

```text
BusinessDomain
  -> NetworkScenario
  -> DeliverySolution
  -> EngineeringTask
  -> ConfigObject

DeliverySolution
  -> Capability
  -> Feature

NetworkScenario / DeliverySolution
  -> DomainSemanticObject

Evidence
  -> 支撑对象和关系
```

这避免了一个常见错误：

```text
业务直接连特性，业务直接连命令，最后所有关系都变成“相关”。
```

当前通过 `Capability` 和 `EngineeringTask` 过渡，是正确方向：

| 关系 | 判断 |
| --- | --- |
| `DeliverySolution -> Capability -> Feature` | 正确 |
| `DeliverySolution -> EngineeringTask -> ConfigObject` | 正确 |
| `NetworkScenario -> DomainSemanticObject` | 正确 |
| `Evidence -> Object/Relation` | 正确，但粒度还不够 |

### 3.2 业务图谱不是业务专题重述

当前已经明确：

```text
业务专题只是原料之一，
业务图谱要从一线工程师视角跨业务专题、特性、命令、运行流程归纳。
```

这点必须保留。  
特别是“配额耗尽后重定向”这种场景，本来就不是单页产品文档完整给出的标准模板，而是多文档学习后的候选方案。

### 3.3 第一条计费闭包较稳

第一条闭包覆盖：

- 差异化计费
- 免费业务
- 默认兜底计费

其证据来源比较直接：

- UDG 套餐1计费场景给了完整业务套餐样板
- UDG 规则配置全景给了业务感知配置结构
- UNC 配置融合计费费率标识给了 SMF 侧对象链
- UDG/UNC 内容计费、融合计费特性可支撑能力映射

当前判断：

```text
第一条闭包业务主链较稳，但工程化验收还不足。
```

### 3.4 第二条配额耗尽重定向闭包可审，但证据强度低于第一条

第二条闭包覆盖：

- 配额耗尽动作
- 配额耗尽后重定向
- 七层重定向

其证据来自多个文档：

- `ADD QUOTAEXHAUSTACT` 支撑配额耗尽动作
- `ADD CCT` 和 CCT 配置支撑配额阈值和绑定粒度
- UDG 七层重定向专题支撑用户面重定向链
- UDG/UNC PCC 基本功能支撑策略控制和策略执行
- UDG 业务感知场景举例支撑“耗尽后 Rule 切换”

当前判断：

```text
第二条闭包是多文档归纳方案候选，
不是产品文档单页给出的标准配置模板。
```

后续必须给 `DeliverySolution` 增加来源类型或置信度字段。

## 4. 明确错误与必须修复的问题

### E-01：核心桥接实体缺少 CSV 落地

这是当前最重要的问题。

`07`、`10` 和 `data/*mapping.csv` 中已经大量使用：

- `DomainSemanticObject`
- `Feature`
- `ConfigObject`
- `MMLCommand`

但 `data/` 下没有对应实体表：

- 没有 `domain_semantic_objects.csv`
- 没有 `features.csv`
- 没有 `config_objects.csv`
- 没有 `mml_commands.csv`

这会导致：

```text
关系表能看，
但图谱实体不完整；
MD 文档能读，
但程序无法完整消费；
跨层映射没有可验证实体端点。
```

修复要求：

| 表 | 目的 | 优先级 |
| --- | --- | --- |
| `domain_semantic_objects.csv` | 落地业务感知语义对象 | P0 |
| `features.csv` | 落地业务感知相关特性实体 | P0 |
| `config_objects.csv` | 落地业务感知相关配置对象实体 | P0 |
| `mml_commands.csv` | 落地业务感知相关命令实体 | P1 |

### E-02：MD 中的跨层关系没有完全落 CSV

当前 MD 中描述了：

- `semantic_realized_by_config`
- `semantic_requires_capability`
- `semantic_verified_by`

但 CSV 中主要只落了：

- `scenario_semantic_mapping.csv`
- `delivery_solution_semantic_mapping.csv`
- `delivery_solution_capability_mapping.csv`
- `feature_capability_mapping.csv`
- `engineering_task_config_mapping.csv`

缺口是：

```text
DomainSemanticObject 到 Capability / ConfigObject / Evidence 的桥接关系没有完整数据化。
```

建议新增：

| 表 | 关系 |
| --- | --- |
| `semantic_capability_mapping.csv` | `DomainSemanticObject -> Capability` |
| `semantic_config_mapping.csv` | `DomainSemanticObject -> ConfigObject` |
| `semantic_evidence_mapping.csv` | `DomainSemanticObject -> Evidence` |

### E-03：部分证据存在悬空或状态不清

独立审查指出，有些 `evidence.csv` 条目没有被正式引用。  
其中一类是遗漏引用，另一类是为后续主线预留。

必须区分：

| 状态 | 含义 |
| --- | --- |
| `accepted` | 已支撑当前对象或关系 |
| `reserved` | 已收录，但用于后续主线 |
| `candidate` | 可能相关，尚未确认 |
| `deprecated` | 不再使用 |

特别是：

- `EVI-UDG-FEAT-90197552` 在 MD 中被列入第一条闭包证据，但 CSV 支撑关系不足，应补引用。
- `EVI-UDG-BA-94838085` 是带宽控制后续主线证据，应标成 `reserved` 或进入候选表。

## 5. 重要建模问题与当前判断

### 5.1 SubjectSemantics 应进入 Phase1

独立审查指出 Phase1 缺少 `BA.SubjectSemantics`，这是对的。

一线工程师做业务感知首先会问：

```text
这条策略对谁生效？
```

它可能对应：

- 用户
- 用户组
- DNN/APN
- UserProfile
- UserProfileGroup
- RuleBinding
- 缺省 URR 组绑定

之前把它隐含在 `BindingSemantics` 中是不够清晰的。

修正判断：

```text
Phase1 和 Phase2 都应该显式使用 BA.SubjectSemantics。
```

需要补：

- `scenario_semantic_mapping.csv`
- `delivery_solution_semantic_mapping.csv`
- `semantic_config_mapping.csv`

### 5.2 场景拆分是临时可审结构，不是最终业务真相

当前拆分：

- `NS-BA-001` 差异化计费
- `NS-BA-002` 免费业务
- `NS-BA-003` 默认兜底计费

从检索角度有价值。  
例如用户问“免流怎么做”，可以直接命中 `NS-BA-002`。

但从业务逻辑上看：

```text
免费业务和默认兜底计费更像差异化计费套餐中的策略切片，
不是完全独立的现网业务。
```

当前判断：

```text
短期保留三拆分，
但必须标注为“场景切片”。
```

后续应考虑新增关系：

| 关系 | 用途 |
| --- | --- |
| `scenario_part_of` | 表示某个场景切片属于更大的业务场景 |
| `scenario_refines` | 表示一个场景是另一个场景的细化 |

类似问题也存在于：

- `NS-BA-004` 配额耗尽动作
- `NS-BA-005` 配额耗尽后重定向
- `NS-BA-006` 七层重定向

当前更成熟的理解是：

```text
NS-BA-005 配额耗尽后重定向
  包含配额耗尽动作
  复用七层重定向动作范式
```

### 5.3 ConfigObject 需要分型

独立审查指出 Phase1 漏了：

- `FLTBINDFLOWF`
- `PROTBINDFLOWF`
- `REFRESHSRV`

这个问题成立，但补法不能一刀切。

建议将配置相关对象分成三类：

| 类型 | 例子 | 是否进 `ConfigObject` |
| --- | --- | --- |
| 持久配置对象 | `Rule`、`URR`、`UserProfile`、`CCT` | 是 |
| 绑定关系对象 | `RuleBinding`、`FLTBINDFLOWF`、`PROTBINDFLOWF` | 是，或标记 `object_category=binding` |
| 操作型命令 | `SET REFRESHSRV`、`LST USERPROFILE`、`DSP xxx` | 不一定作为 ConfigObject，应进入 `MMLCommand` / `ProcedureStep` / `ValidationPlan` |

当前判断：

```text
FLTBINDFLOWF / PROTBINDFLOWF 应补为绑定型 ConfigObject。
REFRESHSRV 更适合补为操作型 MMLCommand 或激活步骤，不应和 Rule/URR 同级。
```

### 5.4 Capability 粒度需要收敛，但不是 P0

当前能力命名存在粒度混合：

- `PccPolicyControlCP` 按网元和控制面命名
- `PccPolicyExecutionUP` 按网元和用户面命名
- `QuotaExhaustAction` 按业务功能命名
- `RedirectActionUP` 按动作和用户面命名

短期可以保留，因为它支撑当前闭包审查。  
中期应统一成：

```text
能力名称 = 动作/控制能力 + 可选网元侧后缀
```

例如：

- `Capability:BA:PccPolicyControl`
- `Capability:BA:PccPolicyExecution`
- `Capability:BA:QuotaExhaustActionControl`
- `Capability:BA:RedirectActionExecution`

但这一项不应阻塞 P0。

### 5.5 DeliverySolution 需要来源类型和置信度

当前 `DS-BA-001` 和 `DS-BA-002` 的证据强度不同：

| 方案 | 来源类型 | 判断 |
| --- | --- | --- |
| `DS-BA-001` | 产品文档标准样板 + 跨文档对齐 | 较稳 |
| `DS-BA-002` | 多文档归纳候选 | 可审但需标记 |

建议给 `delivery_solutions.csv` 增加字段：

| 字段 | 说明 |
| --- | --- |
| `source_type` | `product_template` / `multi_doc_inferred` / `expert_curated` |
| `confidence_level` | `high` / `medium` / `low` |
| `evidence_strength_notes` | 为什么可信，哪里是推断 |

## 6. 当前最小闭包边界判断

当前最小闭包不应该继续只包含：

- BusinessDomain
- NetworkScenario
- ReferencePattern
- DeliverySolution
- EngineeringTask
- Capability
- Feature
- ConfigObject
- Evidence

要成为一线工程可用闭包，至少还需要补：

| 对象 | 是否进入下一轮 | 原因 |
| --- | --- | --- |
| `RuntimeFlow` | 是 | Phase2 的核心就是运行时规则切换 |
| `ValidationPlan` | 是 | 没有验收就不是工程闭包 |
| `DiagnosisRule` | 是 | Agent 需要能定位失败原因 |
| `RiskConstraint` | 是 | 新激活用户生效、刷新、性能影响、继承优先级都必须显式化 |
| `DecisionPoint` | 可选但建议 | 配额耗尽动作、CCT 粒度、重定向/阻断/放行都需要选择 |
| `Scope` | 可选但建议 | 可先由 SubjectSemantics 承载，后续独立落表 |
| `Participant` | 后续 | 当前先不阻塞 |
| `BusinessGoal` | 后续 | 可先保留在场景/方案字段 |

因此下一轮不是扩第三条业务主线，而是：

```text
修复实体表 + 补桥接关系 + 补工程闭环对象。
```

## 7. 下一步执行方案

### P0：补齐可程序消费的三层闭包实体

目标：

```text
让当前两条闭包中的所有关系端点都有实体表。
```

新增或更新：

1. `data/domain_semantic_objects.csv`
2. `data/features.csv`
3. `data/config_objects.csv`
4. `data/semantic_config_mapping.csv`
5. `data/semantic_capability_mapping.csv`

同时修复：

1. Phase1 / Phase2 显式加入 `BA.SubjectSemantics`
2. 补 `FLTBINDFLOWF`、`PROTBINDFLOWF` 为绑定型 ConfigObject
3. 明确 `REFRESHSRV` 为操作型命令或激活步骤，不放入持久配置对象
4. 修复 `EVI-UDG-FEAT-90197552` 的支撑关系
5. 将后续主线证据标为 `reserved`

### P1：补齐工程闭环对象

目标：

```text
让当前两条闭包不仅知道“怎么配”，还知道“运行时怎么生效、怎么验、怎么查、有什么风险”。
```

新增：

1. `data/runtime_flows.csv`
2. `data/validation_plans.csv`
3. `data/diagnosis_rules.csv`
4. `data/risk_constraints.csv`
5. 对应关系表：
   - `delivery_solution_runtime_mapping.csv`
   - `delivery_solution_validation_mapping.csv`
   - `delivery_solution_diagnosis_mapping.csv`
   - `delivery_solution_risk_mapping.csv`

优先实例：

| 对象 | 首批实例 |
| --- | --- |
| `RuntimeFlow` | 计费链运行流程、配额耗尽后规则切换流程 |
| `ValidationPlan` | 计费命中验收、默认兜底验收、重定向验收 |
| `DiagnosisRule` | 未命中 Rule、命中但未计费、耗尽后未重定向、CP/UP 不一致 |
| `RiskConstraint` | 新激活用户生效、刷新要求、CCT 粒度继承、PCC 性能影响 |

### P2：证据升级到字段级

目标：

```text
让每个关键字段和推断都能回到原文或明确标记为推断。
```

新增：

- `data/evidence_claims.csv`

建议字段：

| 字段 | 说明 |
| --- | --- |
| `claim_id` | 断言 ID |
| `evidence_id` | 来源页 |
| `target_type` | 对象或关系类型 |
| `target_id` | 对象或关系 ID |
| `target_field` | 支撑哪个字段 |
| `claim_text` | 断言摘要 |
| `support_level` | `direct` / `inferred` / `weak` |
| `raw_quote_hint` | 原文关键短句 |
| `notes` | 说明 |

P2 不是为了堆证据，而是为了控制 Agent 归纳边界。

### P3：再扩第三条业务主线

当 P0/P1 完成后，再进入第三条主线。

建议优先：

```text
套餐2：带宽控制
```

原因：

1. 产品文档中已有直接业务专题。
2. 可复用现有流量识别、Rule、UserProfile、PCC 策略组结构。
3. 会新增 `BA.BandwidthSemantics`，能检验当前语义和能力模型是否能承载非计费动作。

## 8. 对当前审查报告的统一回应

| 问题 | 采纳情况 | 处理方式 |
| --- | --- | --- |
| E-01 桥接实体缺 CSV | 完全采纳 | P0 补实体表 |
| W-01 SubjectSemantics 缺失 | 完全采纳 | P0 加入 Phase1/Phase2 |
| W-02 ConfigObject 遗漏 | 部分采纳 | 补绑定型对象，REFRESHSRV 归为操作型命令/步骤 |
| W-03 场景粒度不一致 | 采纳 | 标注当前为场景切片，后续加 `scenario_part_of` |
| W-04 工程任务缺生效范围 | 采纳 | 用 SubjectSemantics + 后续 Scope/DecisionPoint 补齐 |
| W-05 ID 命名不一致 | 采纳 | business-graph 采用类型前缀，work/ 标历史命名 |
| W-06 Evidence 悬空 | 采纳 | P0 修引用和状态 |
| W-07 证据粒度浅 | 采纳 | P2 加 evidence_claims |
| Q-01 最小闭包边界 | 已决策 | RuntimeFlow/Validation/Risk 下一轮进入 |
| Q-02 Capability 粒度 | 采纳但不阻塞 | P3 前统一 |
| Q-03 方案证据强度 | 采纳 | 加 source_type/confidence |
| Q-04 MD/CSV 边界 | 已决策 | 核心实体和关系必须 CSV 化，MD 负责解释 |

## 9. 最终结论

当前 `business-graph/` 的价值在于：

```text
已经证明“业务感知”可以按场景、语义、方案、能力、任务、对象链和证据来组织，
而不是简单重述业务专题。
```

当前 `business-graph/` 的不足在于：

```text
核心桥接实体和部分跨层关系还只存在于 MD 或隐含在关系表中，
导致图谱还不够可程序消费；
运行、验收、诊断、风险还没有形成工程闭环；
证据还不足以支撑字段级审查。
```

下一步的唯一正确方向是：

```text
先修复当前两条闭包的结构完整性和工程闭环，
再扩展新的业务感知主线。
```

也就是：

```text
P0：补实体表和语义桥接
P1：补运行、验收、诊断、风险
P2：补字段级证据
P3：扩带宽控制主线
```
