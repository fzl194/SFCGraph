# 业务图谱数据工作区

本目录现在不再采用“所有 CSV 平铺在一个目录下”的方式。  
原因很直接：

```text
平铺后无法一眼看出：
哪些是业务对象，
哪些是语义对象，
哪些是特性/命令实体，
哪些是层内关系，
哪些是跨层桥接，
哪些只是审查视图。
```

所以当前 `data/` 已按“实体 / 层内关系 / 跨层桥接 / 工程闭环 / 证据 / 视图”重组。

## 当前覆盖范围

当前仍只覆盖两条主线：

```text
差异化计费
+ 免费业务
+ 默认兜底计费
```

```text
配额耗尽动作
+ 配额耗尽后重定向
+ 七层重定向
```

这些数据不是最终全景，而是当前两条闭包的可审产物。

## 目录结构

### `01-business-entities`

业务层实体。

- `business_domains.csv`
- `network_scenarios.csv`
- `reference_patterns.csv`
- `delivery_solutions.csv`
- `engineering_tasks.csv`

这一层只回答：

```text
业务感知里有哪些核心业务对象。
```

### `02-business-relations`

业务层内部关系。

- `business_domain_scenario_mapping.csv`
- `scenario_pattern_mapping.csv`
- `scenario_solution_mapping.csv`
- `delivery_solution_task_mapping.csv`

这一层只回答：

```text
业务对象之间怎么连。
```

例如：

- `BusinessDomain -> NetworkScenario`
- `NetworkScenario -> ReferencePattern`
- `NetworkScenario -> DeliverySolution`
- `DeliverySolution -> EngineeringTask`

### `03-semantic-entities`

领域语义实体。

- `domain_semantic_objects.csv`

这一层只定义：

```text
业务感知有哪些稳定语义对象。
```

例如：

- `BA.SubjectSemantics`
- `BA.TrafficRecognitionSemantics`
- `BA.RuleSemantics`
- `BA.ChargingSemantics`

### `04-semantic-bridges`

语义桥接关系。

- `scenario_semantic_mapping.csv`
- `delivery_solution_semantic_mapping.csv`
- `semantic_capability_mapping.csv`
- `semantic_config_mapping.csv`
- `semantic_evidence_mapping.csv`

这一层是：

```text
业务层 <-> 语义层
语义层 <-> 能力层
语义层 <-> 配置对象层
语义层 <-> 证据层
```

它不是“层内关系”，而是业务图谱里最核心的解释层。

### `05-feature-entities`

特性层实体。

- `capabilities.csv`
- `features.csv`

这里把两类东西放在一起：

1. `Capability`
2. `Feature`

原因是当前业务图谱里，特性层最重要的是：

```text
业务方案需要什么能力，
这些能力由哪些特性实现。
```

### `06-feature-relations`

特性层内部关系。

- `feature_capability_mapping.csv`

当前只保留真正属于特性层内部的关系：

```text
Capability -> Feature
```

### `07-command-entities`

命令层实体。

- `config_objects.csv`
- `mml_commands.csv`

这里不再把命令和配置对象混在业务视图表中。

这一层只回答：

```text
业务感知当前涉及哪些配置对象，
以及哪些 MML 命令是正式对象。
```

### `08-cross-layer-relations`

跨层桥接关系。

- `delivery_solution_capability_mapping.csv`
- `engineering_task_config_mapping.csv`

这里专门放：

```text
业务方案 -> 能力
工程任务 -> 配置对象
```

这些关系不属于某一层内部，所以单独放。

### `09-runtime-validation-risk`

工程闭环对象和关系。

- `runtime_flows.csv`
- `validation_plans.csv`
- `diagnosis_rules.csv`
- `risk_constraints.csv`
- `delivery_solution_runtime_mapping.csv`
- `delivery_solution_validation_mapping.csv`
- `delivery_solution_diagnosis_mapping.csv`
- `delivery_solution_risk_mapping.csv`

这一层回答：

```text
配置之后怎么运行，
怎么验，
怎么查，
有什么约束。
```

这是当前两条闭包从“能抽出来”走向“一线可用”的关键层。

### `10-evidence`

证据层。

- `evidence.csv`
- `evidence_support_mapping.csv`
- `evidence_claims.csv`

这一层专门承载：

1. 证据来源页
2. 证据支撑对象/关系
3. 字段级证据断言

### `11-source-and-views`

原料池和审查视图。

- `business_source_index.csv`
- `business_related_features.csv`
- `business_related_commands.csv`
- `business_related_object_chains.csv`
- `business_related_commands_candidates.csv`
- `business_related_object_chains_candidates.csv`
- `network_scenario_candidates.csv`

这一层不是正式图谱主数据。  
它的定位是：

```text
原料索引
候选集
审查视图
```

这些表的作用是辅助抽取、审查和扩展，不应和正式实体表混看。

## 现在怎么看数据

建议顺序：

1. 先看 `01-business-entities`
2. 再看 `02-business-relations`
3. 再看 `03-semantic-entities`
4. 再看 `04-semantic-bridges`
5. 再看 `05/06` 特性层
6. 再看 `07` 命令层
7. 再看 `08` 跨层桥接
8. 最后看 `09/10/11`

这样你能先看清“业务感知业务图谱在讲什么”，再看“它怎么落到特性、命令、运行和证据”。

## 一个简单判断规则

如果你在看某张表，不知道它属于哪一类，可以用下面规则：

| 目录 | 代表含义 |
| --- | --- |
| `01` | 业务对象 |
| `02` | 业务对象之间的关系 |
| `03` | 语义对象 |
| `04` | 语义和其他层的桥接 |
| `05` | 特性/能力实体 |
| `06` | 特性层内部关系 |
| `07` | 命令/配置对象实体 |
| `08` | 业务、能力、配置对象之间的跨层桥接 |
| `09` | 运行、验收、诊断、风险 |
| `10` | 证据 |
| `11` | 原料和视图 |

## 当前未做的事

这次重组只调整“承载结构”，没有继续扩业务内容。

还没做的是：

1. 带宽控制主线扩展
2. 更细的命令层层内关系拆分
3. 业务图谱总览 HTML / Mermaid 视图
4. 更完整的字段级证据全覆盖
