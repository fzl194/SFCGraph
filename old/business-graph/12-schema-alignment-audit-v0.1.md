# 业务感知 Schema 对齐审计 v0.1

## 1. 本页定位

本页只回答一个问题：

```text
当前 business-graph/data 里的提取结果，
是否按照 work/business-awareness-result/01-schema-binding.md
当初定义的 schema 在落地。
```

这里不讨论“方向是否合理”，只逐项核对：

1. schema 对象类型是否已落表
2. schema 关系类型是否已落表
3. 是否被降级成字段、说明文字或候选视图
4. 哪些地方已经偏离原设计

审计基线文件：

- [work/business-awareness-result/01-schema-binding.md](../work/business-awareness-result/01-schema-binding.md)
- [work/business-awareness-result/03-business-graph-instances.md](../work/business-awareness-result/03-business-graph-instances.md)
- [work/business-awareness-result/04-feature-graph-instances.md](../work/business-awareness-result/04-feature-graph-instances.md)
- [work/business-awareness-result/05-command-graph-instances.md](../work/business-awareness-result/05-command-graph-instances.md)
- [work/business-awareness-result/06-cross-layer-mapping.md](../work/business-awareness-result/06-cross-layer-mapping.md)

结论标准：

| 状态 | 含义 |
| --- | --- |
| `已对齐` | 已有正式 CSV 实体表或关系表承载 |
| `部分对齐` | 只落了一部分，或退化成字段/说明/视图 |
| `未对齐` | schema 中有定义，但当前没有正式承载 |
| `有偏差` | 有数据，但和原 schema 的承载方式不一致 |

## 2. 总结结论

当前 `business-graph/data` 不是对原 schema 的完整实现，而是：

```text
基于原 schema 主干做出的第一版可落表子集。
```

更准确地说：

1. 业务层、语义层、能力/特性层、配置对象层、证据层的主干已经对齐。
2. 原 schema 中较细的特性过程层、命令参数层、运行态对象层，目前大多还没有正式落表。
3. 一部分原 schema 关系被降级成了：
   - 实体表中的 JSON 字段
   - Markdown 说明
   - `11-source-and-views/` 下的候选视图

所以当前结果应判断为：

```text
主框架对齐；
细粒度对象和关系还没有完全按原设计落地。
```

## 3. 业务图谱对象对齐

| 原 schema 对象 | 当前承载 | 状态 | 判断 |
| --- | --- | --- | --- |
| `BusinessDomain` | `01-business-entities/business_domains.csv` | `已对齐` | 已正式落表 |
| `NetworkScenario` | `01-business-entities/network_scenarios.csv` | `已对齐` | 已正式落表 |
| `ReferencePattern` | `01-business-entities/reference_patterns.csv` | `已对齐` | 已正式落表 |
| `DeliverySolution` | `01-business-entities/delivery_solutions.csv` | `已对齐` | 已正式落表 |
| `EngineeringTask` | `01-business-entities/engineering_tasks.csv` | `已对齐` | 已正式落表 |
| `BusinessGoal` | `network_scenarios.csv.business_goal` | `部分对齐` | 目前只是字段，不是独立对象 |
| `Participant` | 无 | `未对齐` | 只在早期 md 中定义，没有 CSV |
| `Scope` | 无 | `未对齐` | 当前主要隐含在 SubjectSemantics 和 task/solution 描述中 |
| `DecisionPoint` | 无 | `未对齐` | 目前只存在于方案说明和风险说明里 |
| `RuntimeFlow` | `09-runtime-validation-risk/runtime_flows.csv` | `已对齐` | 后续补进来，已正式落表 |
| `ValidationPlan` | `09-runtime-validation-risk/validation_plans.csv` | `已对齐` | 已正式落表 |
| `DiagnosisRule` | `09-runtime-validation-risk/diagnosis_rules.csv` | `已对齐` | 已正式落表 |
| `RiskConstraint` | `09-runtime-validation-risk/risk_constraints.csv` | `已对齐` | 已正式落表 |

结论：

```text
业务图谱对象主干基本对齐；
BusinessGoal/Participant/Scope/DecisionPoint 仍然没有按原 schema 独立对象化。
```

## 4. 业务图谱关系对齐

| 原 schema 关系 | 当前承载 | 状态 | 判断 |
| --- | --- | --- | --- |
| `contains` (`BusinessDomain -> NetworkScenario`) | `02-business-relations/business_domain_scenario_mapping.csv` | `已对齐` | 已正式落表 |
| `has_pattern` (`NetworkScenario -> ReferencePattern`) | `02-business-relations/scenario_pattern_mapping.csv` | `已对齐` | 已正式落表 |
| `instantiated_as` (`NetworkScenario -> DeliverySolution`) | `02-business-relations/scenario_solution_mapping.csv` | `已对齐` | 已正式落表 |
| `decomposes_to` (`DeliverySolution -> EngineeringTask`) | `02-business-relations/delivery_solution_task_mapping.csv` | `已对齐` | 已正式落表 |
| `has_goal` (`DeliverySolution -> BusinessGoal`) | 无 | `未对齐` | 只在说明字段中存在 |
| `applies_to` (`DeliverySolution -> Scope`) | 无 | `未对齐` | 只写在方案描述里 |
| `involves` (`DeliverySolution -> Participant`) | 无 | `未对齐` | 未正式建表 |
| `has_decision` (`DeliverySolution -> DecisionPoint`) | 无 | `未对齐` | 未正式建表 |
| `has_runtime_flow` (`DeliverySolution -> RuntimeFlow`) | `09-runtime-validation-risk/delivery_solution_runtime_mapping.csv` | `已对齐` | 已正式落表 |
| `validated_by` (`DeliverySolution -> ValidationPlan`) | `09-runtime-validation-risk/delivery_solution_validation_mapping.csv` | `已对齐` | 已正式落表 |
| `diagnosed_by` (`DeliverySolution -> DiagnosisRule`) | `09-runtime-validation-risk/delivery_solution_diagnosis_mapping.csv` | `已对齐` | 已正式落表 |
| `constrained_by` (`DeliverySolution -> RiskConstraint`) | `09-runtime-validation-risk/delivery_solution_risk_mapping.csv` | `已对齐` | 已正式落表 |

结论：

```text
业务图谱关系链已经能跑通最小闭包，
但“目标/范围/参与方/决策点”四类业务关系还没有正式落表。
```

## 5. 领域语义层对齐

### 5.1 语义对象

| 原 schema 对象 | 当前承载 | 状态 | 判断 |
| --- | --- | --- | --- |
| `DomainSemanticProfile` | 无独立 CSV | `未对齐` | 当前默认固定为“业务感知领域语义模型”，只存在于 md 设计里 |
| `DomainSemanticObject` | `03-semantic-entities/domain_semantic_objects.csv` | `已对齐` | 已正式落表 |

### 5.2 语义关系

| 原 schema 关系 | 当前承载 | 状态 | 判断 |
| --- | --- | --- | --- |
| `has_semantic_profile` (`BusinessDomain -> DomainSemanticProfile`) | 无 | `未对齐` | 目前隐含成立，没有独立表 |
| `defines_semantic_object` (`DomainSemanticProfile -> DomainSemanticObject`) | 无 | `未对齐` | 当前由 `domain_semantic_objects.csv` 直接承载对象，缺 profile 关系 |
| `uses_semantic_object` (`NetworkScenario -> DomainSemanticObject`) | `04-semantic-bridges/scenario_semantic_mapping.csv` | `已对齐` | 已正式落表 |
| `instantiates_semantic_object` (`DeliverySolution -> DomainSemanticObject`) | `04-semantic-bridges/delivery_solution_semantic_mapping.csv` | `已对齐` | 已正式落表 |
| `semantic_requires_capability` | `04-semantic-bridges/semantic_capability_mapping.csv` | `已对齐` | 已正式落表 |
| `semantic_realized_by_config` | `04-semantic-bridges/semantic_config_mapping.csv` | `已对齐` | 已正式落表 |
| `semantic_materializes_as` | 无 | `未对齐` | 当前缺 `RuntimeObject` 实体层 |
| `semantic_verified_by` | `04-semantic-bridges/semantic_evidence_mapping.csv` | `已对齐` | 已正式落表 |

结论：

```text
领域语义层已经对齐到“语义对象 + 场景/方案桥接 + 能力/配置/证据桥接”；
但 DomainSemanticProfile 和语义到运行态的这两段还没落。
```

## 6. 特性图谱对齐

### 6.1 特性对象

| 原 schema 对象 | 当前承载 | 状态 | 判断 |
| --- | --- | --- | --- |
| `Capability` | `05-feature-entities/capabilities.csv` | `已对齐` | 已正式落表 |
| `Feature` | `05-feature-entities/features.csv` | `已对齐` | 已正式落表 |
| `FeatureAvailability` | 无 CSV，仅 md 中有实例 | `未对齐` | 原 schema 有，当前 data 未落表 |
| `FeatureProcedure` | 无 CSV，仅 md 中有实例 | `未对齐` | 原 schema 有，当前 data 未落表 |
| `ProcedureVariant` | 无 CSV，仅 md 中有实例 | `未对齐` | 原 schema 有，当前 data 未落表 |
| `ProcedureStep` | 无 | `未对齐` | 尚未落表 |
| `ApplicabilityCondition` | 无 | `未对齐` | 尚未落表 |
| `FeatureDependency` | 无 | `未对齐` | 只在 md 关系说明中出现 |
| `ApplicableNF` | 无 | `未对齐` | 尚未落表 |
| `FeatureLimit` | 无 | `未对齐` | 尚未落表 |

### 6.2 特性关系

| 原 schema 关系 | 当前承载 | 状态 | 判断 |
| --- | --- | --- | --- |
| `provides` (`Feature -> Capability`) | `06-feature-relations/feature_capability_mapping.csv` | `已对齐` | 已正式落表 |
| `depends_on` (`Feature -> FeatureDependency`) | 无 | `未对齐` | 只在 md 中列举 |
| `applies_to_nf` (`Feature -> ApplicableNF`) | 无 | `未对齐` | 当前缺实体和关系 |
| `limited_by` (`Feature -> FeatureLimit`) | 无 | `未对齐` | 当前缺实体和关系 |
| `available_as` (`Feature -> FeatureAvailability`) | 无 | `未对齐` | md 有，CSV 无 |
| `has_procedure` (`Feature -> FeatureProcedure`) | 无 | `未对齐` | md 有，CSV 无 |
| `procedure_has_variant` | 无 | `未对齐` | md 有，CSV 无 |
| `variant_has_step` | 无 | `未对齐` | 未落表 |
| `applies_when` | 无 | `未对齐` | 未落表 |
| `step_uses_object` | 无 | `未对齐` | 未落表 |
| `step_uses_command` | 无 | `未对齐` | 未落表 |

结论：

```text
特性图谱当前只实现了 Capability 和 Feature 这一层；
原设计中的“可获得性、流程、变体、步骤”基本还停留在 md，没有数据化。
```

这是当前和原始设计差距最大的层之一。

## 7. 命令图谱对齐

### 7.1 命令对象

| 原 schema 对象 | 当前承载 | 状态 | 判断 |
| --- | --- | --- | --- |
| `ConfigObject` | `07-command-entities/config_objects.csv` | `已对齐` | 已正式落表 |
| `MMLCommand` | `07-command-entities/mml_commands.csv` | `已对齐` | 已正式落表 |
| `CommandParameter` | 无 | `未对齐` | 当前没有参数实体表 |

### 7.2 命令关系

| 原 schema 关系 | 当前承载 | 状态 | 判断 |
| --- | --- | --- | --- |
| `acts_on` (`MMLCommand -> ConfigObject`) | `mml_commands.csv.primary_object_id` | `部分对齐` | 目前是字段，不是独立关系表 |
| `has_parameter` (`MMLCommand -> CommandParameter`) | 无 | `未对齐` | 参数层尚未落表 |
| `references` (`ConfigObject -> ConfigObject`) | 无正式关系表 | `部分对齐` | 只在 `business_related_object_chains.csv` 和 md 中有 |
| `binds` (`ConfigObject -> ConfigObject`) | 无正式关系表 | `部分对齐` | 只在 object chain 和 task/config 映射中隐含 |
| `contains` (`ConfigObject -> ConfigObject`) | 无正式关系表 | `部分对齐` | 只在 object chain 和文字说明中存在 |
| `supported_by` (`ObjectOrRelation -> Evidence`) | `10-evidence/evidence_support_mapping.csv` | `已对齐` | 已正式落表，但 target_type 仍较粗 |

结论：

```text
命令图谱当前对齐到了“对象 + 命令”这一层；
原设计中的参数层和对象间细关系层还没有正式数据化。
```

## 8. 运行与证据层对齐

### 8.1 对象

| 原 schema 对象 | 当前承载 | 状态 | 判断 |
| --- | --- | --- | --- |
| `RuntimeObject` | 无 | `未对齐` | 当前只有 `RuntimeFlow`，没有运行态对象实体 |
| `RuntimeEvent` | 无 | `未对齐` | 当前没有运行态事件实体 |
| `Evidence` | `10-evidence/evidence.csv` | `已对齐` | 已正式落表 |
| `AgentAction` | 无 | `未对齐` | 当前未进入 data |
| `KnowledgeArtifact` | 无 | `未对齐` | 当前未进入 data |

### 8.2 关系

| 原 schema 关系 | 当前承载 | 状态 | 判断 |
| --- | --- | --- | --- |
| `materializes_as` (`ConfigObject -> RuntimeObject`) | 无 | `未对齐` | 当前缺 RuntimeObject |
| `emits_event` (`RuntimeObject -> RuntimeEvent`) | 无 | `未对齐` | 当前缺 RuntimeEvent |
| `verifies` (`ValidationPlan -> RuntimeObject`) | 无 | `未对齐` | 目前只到 `DeliverySolution -> ValidationPlan` |
| `checks` (`DiagnosisRule -> ConfigObject`) | 无 | `未对齐` | 只在 md 中有说明 |
| `checks_runtime` (`DiagnosisRule -> RuntimeObject`) | 无 | `未对齐` | 当前缺 RuntimeObject |
| `supported_by` (`ObjectOrRelation -> Evidence`) | `10-evidence/evidence_support_mapping.csv` | `已对齐` | 已正式落表 |
| `performed_by` (`AgentAction -> EngineeringTask`) | 无 | `未对齐` | 当前未落 |

结论：

```text
运行与证据层当前只落了“流程/验收/诊断/风险 + 证据”；
原设计中的运行态对象、运行态事件、AgentAction 还没有进入数据层。
```

## 9. 跨层关系对齐

| 原 schema 关系 | 当前承载 | 状态 | 判断 |
| --- | --- | --- | --- |
| `requires_capability` (`DeliverySolution -> Capability`) | `08-cross-layer-relations/delivery_solution_capability_mapping.csv` | `已对齐` | 已正式落表 |
| `implemented_by_feature` (`Capability -> Feature`) | `06-feature-relations/feature_capability_mapping.csv` | `已对齐` | 用反向关系承载，语义等价 |
| `pattern_requires_capability` (`ReferencePattern -> Capability`) | 无 | `未对齐` | 当前没有 pattern 到 capability 的正式桥接 |
| `pattern_uses_config` (`ReferencePattern -> ConfigObject`) | 无 | `未对齐` | 当前没有 pattern 到 config 的正式桥接 |
| `selects_pattern` (`DeliverySolution -> ReferencePattern`) | 无 | `未对齐` | 当前只有 `Scenario -> Pattern` |
| `adapts_pattern` (`DeliverySolution -> ReferencePattern`) | 无 | `未对齐` | 未落表 |
| `selects_variant` (`DeliverySolution -> ProcedureVariant`) | 无 | `未对齐` | 依赖 ProcedureVariant 未落表 |
| `adapts_variant` (`DeliverySolution -> ProcedureVariant`) | 无 | `未对齐` | 未落表 |
| `realized_by_config` (`EngineeringTask -> ConfigObject`) | `08-cross-layer-relations/engineering_task_config_mapping.csv` | `已对齐` | 已正式落表 |
| `uses_command` (`ConfigObject -> MMLCommand`) | `config_objects.csv.supporting_command_ids_json` + `mml_commands.csv.primary_object_id` | `有偏差` | 有数据，但没有正式关系表 |
| `semantic_requires_capability` | `04-semantic-bridges/semantic_capability_mapping.csv` | `已对齐` | 已正式落表 |
| `semantic_realized_by_config` | `04-semantic-bridges/semantic_config_mapping.csv` | `已对齐` | 已正式落表 |
| `semantic_materializes_as` | 无 | `未对齐` | 依赖 RuntimeObject 未落 |
| `semantic_verified_by` | `04-semantic-bridges/semantic_evidence_mapping.csv` | `已对齐` | 已正式落表 |

结论：

```text
跨层桥接当前只实现了“方案到能力、任务到配置、语义到能力/配置/证据”；
原设计里 pattern/variant/runtime 这几段桥还没有真正落地。
```

## 10. 当前最关键的偏差

如果只看“有没有业务、语义、特性、命令、证据”，当前已经基本对齐。  
但如果按照你最初设计去严格审计，当前最关键偏差有四个：

### P-01：特性过程层几乎没有进 CSV

原设计里特性层不是只有 `Feature`。

真正承载“一个特性有多种配置方式、产品文档只给典型范式”的，是：

- `FeatureAvailability`
- `FeatureProcedure`
- `ProcedureVariant`
- `ProcedureStep`

而当前这些都还停留在 md。  
这意味着：

```text
当前 data 里的特性层，还不足以承载“同一特性多种现网做法”。
```

### P-02：命令参数层还没有落

原设计里命令图谱不仅有：

- `ConfigObject`
- `MMLCommand`

还有：

- `CommandParameter`

而且命令依赖、绑定、包含，有一部分到底建模在参数还是建模在对象关系上，本来就是最初重点讨论的问题。  
当前这一层还没有正式 CSV 化，所以只能说：

```text
命令图谱当前只是对象级，不是完整参数级。
```

### P-03：运行态对象层还没有落

最初设计里明确有：

- `RuntimeObject`
- `RuntimeEvent`

但当前只补了：

- `RuntimeFlow`
- `ValidationPlan`
- `DiagnosisRule`
- `RiskConstraint`

这说明现在能表达“有一条运行流程”，但还不能表达：

```text
哪个配置对象物化成哪个运行态对象，
哪个运行态对象产生什么事件，
验收和诊断到底查哪一个运行态点。
```

### P-04：不少原设计关系被降级成字段或视图

当前有些信息不是没有，而是承载层级降了：

| 原设计关系 | 当前降级方式 |
| --- | --- |
| `uses_command` | `config_objects.csv.supporting_command_ids_json` |
| `acts_on` | `mml_commands.csv.primary_object_id` |
| `references/binds/contains` | `business_related_object_chains.csv` + md 说明 |
| `has_goal` / `applies_to` | 业务实体里的说明字段 |

这会导致：

```text
人能看懂，
但程序不能把它当一等关系处理。
```

## 11. 最终判断

对“是不是按照我当初设计来的”这个问题，当前最准确的回答是：

```text
是按照你当初设计的主骨架来的，
但只实现了主骨架和一部分关键桥接，
并没有把原 schema 的全部对象和关系完整落地。
```

换句话说：

1. `business-graph/data` 不是偏离原设计另起炉灶。
2. 但它现在只是原设计的第一版子集实现，不是完整实现。
3. 当前最缺的是：
   - 特性过程层
   - 命令参数层
   - 运行态对象层
   - 若干正式关系表

## 12. 下一步建议

如果接下来要继续沿“严格回到原 schema”推进，建议顺序不是再扩新业务，而是：

1. 先补 `FeatureAvailability / FeatureProcedure / ProcedureVariant / ProcedureStep`
2. 再补 `CommandParameter` 和对象细关系表
3. 再补 `RuntimeObject / RuntimeEvent`
4. 最后补 `Pattern / Variant / Command` 相关的正式桥接关系

这样之后你再审“业务感知完整闭包”，才真正是在审你最初那套 schema，而不是审一个缩水版中间态。
