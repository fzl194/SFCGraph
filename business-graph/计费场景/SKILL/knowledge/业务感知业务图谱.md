# 业务图谱定义与业务感知业务图谱

## 1. 文档目标

本文只回答两个问题：

1. `业务图谱的定义是什么`
2. `业务感知对应的业务图谱是什么`

因此本文分成两部分：

### Part A

先定义：

- 什么叫业务图谱
- 业务图谱有哪些 schema
- schema 之间是什么关系

### Part B

再实例化：

- 在 `BusinessDomain = 业务感知` 下
- 这些 schema 分别对应什么内容
- 它们如何组成一张完整的业务感知业务图谱

## 2. 原始语料范围

本文结论来自七组主题化原始语料，而不是来自某一轮中间稿：

1. `定义与原理语料`
   - 业务感知定义、过程、相关概念
   - SA 识别、协议识别、协议特征库、协议解析库
   - 策略、规则、过滤条件
2. `场景与样板语料`
   - 业务感知场景举例
   - 计费、带宽控制、访问限制套餐样板
   - 七层/三四层阻塞、重定向、用户 Portal
3. `分流与边缘卸载语料`
   - Why/What/How 分流
   - 基于预定义规则、位置、动态规则、漫游地动态签约的分流策略控制
   - 公网私网业务独立计费
4. `计费与配额主线语料`
   - 内容计费、融合计费、计费解决方案概述
   - 标准计费流程、计费事件触发条件、计费用量搜集、多 UPF 配额管理
   - 一望5G 计费解决方案总览
5. `PCC 与 QoS 编排语料`
   - PCC 基本功能、PCC 静态规则原理
   - E2E QoS 管理机制、QoS 生成/下发/更新
   - PCF 发起和 SMF 发起的策略更新
6. `调测与故障语料`
   - UDG 业务感知调测、七层/三四层阻塞与重定向调测
   - UNC 计费故障案例、欠费重定向、default quota、融合计费/内容计费调测
7. `产品能力与边界语料`
   - UNC/UDG 产品描述、5G Core 解决方案、UDG 典型组网
   - UDG License 资源控制项

这些原始材料共同支撑本文中的定义层、场景层、方案层、运行层、支撑层和边界层结论。

---

## Part A. 业务图谱的定义

## 3. 什么是业务图谱

业务图谱不是功能目录、特性目录、命令目录或配置步骤索引。

业务图谱是：

```text
把某一业务域中的稳定业务问题、方案闭包、工程任务、支撑对象，
以及它们与下层语义对象、特性、配置对象的连接关系，
组织成一套结构化对象网络。
```

它回答的不是“命令怎么敲”，而是：

1. 这个业务域里有哪些稳定问题空间
2. 这些问题如何归类为现网场景
3. 每类场景如何收敛成方案
4. 方案如何拆成可实施、可验证的工程任务
5. 方案与参与方、范围、决策、验收、规则之间是什么关系
6. 这些业务结构如何向下连接到语义对象、特性与配置对象

对 `业务感知` 而言，业务图谱表达的是一套稳定的业务组织结构：

- 一级入口是 `计费场景 / 带宽控制场景 / 访问限制场景 / 本地分流场景`
- 每个场景继续收敛为 `DeliverySolution`
- 每个方案再拆成 `EngineeringTask`
- 同时由 `Participant / Scope / DecisionPoint / ValidationPlan / BusinessRule` 补足支撑信息
- 最后向下桥接到 `DomainSemanticObject / Feature / ConfigObject`

因此，业务图谱本质上是一张“业务组织图”，而不是一条“运行流程图”。

## 4. 业务图谱的 schema

业务图谱的 schema 分三层：

1. `业务层主链 schema`
2. `第二层支撑 schema`
3. `向下桥接 schema`

### 4.1 schema 总表

| schema对象 | 中文对象名 | 所属层 | 定义 | 在图谱中的作用 | 需要重点展开的业务含义 |
| --- | --- | --- | --- | --- | --- |
| `BusinessDomain` | 业务域 | 业务层 | 表示一类长期存在的工程知识空间 | 作为整张图谱的根对象，限定讨论边界 | 不是某篇文档，而是一类稳定业务空间 |
| `NetworkScenario` | 现网场景 | 业务层 | 表示一线遇到的需求类型或问题情境 | 作为图谱的一级业务入口 | 不是命令，不是参数，而是“现场到底在解决什么问题” |
| `DeliverySolution` | 交付方案 | 业务层 | 表示针对某个场景形成的可落地方案闭包 | 把场景推进到“怎么组织落地” | 要表达一组机制如何一起工作 |
| `EngineeringTask` | 工程任务 | 业务层 | 表示方案中的可执行或可检查任务 | 把方案拆成可执行工作项 | 要说明规划什么、绑定什么、验证什么 |
| `Participant` | 参与方 | 第二层 | 表示方案形成、生效、更新、计费、验证过程中承担稳定职责的参与方 | 说明方案涉及哪些角色 | 谁负责决策、编排、执行、计费、接入协同 |
| `Scope` | 生效范围 | 第二层 | 表示方案或策略对谁、哪类接入、哪类位置、哪类会话条件生效 | 表达作用边界 | 用户级、APN/DNN、切片、位置/PRA、DNAI 等范围差异 |
| `DecisionPoint` | 决策点 | 第二层 | 表示场景或方案中会引起后续结构分支的稳定选择点 | 表达同一场景/方案下的分支 | 计费方式、配额动作、分流来源、访问动作 |
| `ValidationPlan` | 验收计划 | 第二层 | 表示针对方案的验收检查模板 | 提供“验什么”的组织结构 | 观察哪些对象、通过条件是什么 |
| `BusinessRule` | 业务规则 | 第二层 | 表示业务级校验、约束断言和异常定位逻辑的统一规则对象 | 提供规则治理 | 校验规则、诊断规则、约束规则 |
| `DomainSemanticObject` | 领域语义对象 | 桥接层 | 表示某个业务域内部用于表达业务含义的语义对象 | 防止业务图谱直接坠落成命令图 | 先把业务问题翻成识别、计费、配额等语义单元 |
| `Feature` | 特性 | 桥接层 | 表示产品文档中的特性条目 | 承接业务语义背后的能力载体 | 说明哪类正式能力在支撑业务场景 |
| `ConfigObject` | 配置对象 | 桥接层 | 表示 MML 命令创建、修改、引用的对象 | 说明图谱最终会落到哪些对象链 | 不展开所有参数，但要说明对象链长什么样 |

## 5. schema 之间的关系

业务图谱不是对象平铺，而是有固定主链、支撑关系和桥接关系。

### 5.1 schema 关系总表

| 起点schema | 终点schema | 关系标识 | 中文关系名 | 业务含义 |
| --- | --- | --- | --- | --- |
| `BusinessDomain` | `NetworkScenario` | `contains` | 包含 | 一个业务域由若干稳定业务场景组成；这一层对应产品文档中的场景分组入口 |
| `NetworkScenario` | `DeliverySolution` | `instantiated_as` | 实例化为 | 一个场景可收敛为一个或多个方案闭包；依据来自套餐、解决方案概述和分流方案说明等原始产品文档 |
| `DeliverySolution` | `EngineeringTask` | `uses_task` | 使用任务 | 一个方案通过规划、执行、验证三类工程任务落地；这一关系来自套餐文档的数据段、脚本段和调测段的结构化归纳 |
| `DeliverySolution` | `Participant` | `involves` | 涉及 | 一个方案会涉及若干稳定参与方协同完成；依据来自业务感知过程、计费方案、分流流程等产品文档中的网元与外部系统分工 |
| `DeliverySolution` | `Scope` | `applies_to` | 作用于 | 一个方案对谁、在哪些接入/位置/导向边界下生效；依据来自套餐中的 UserProfile/APN 绑定以及分流文档中的 DNN/PRA/DNAI 条件 |
| `NetworkScenario` | `DecisionPoint` | `has_decision` | 包含决策点 | 某些场景天然存在稳定分支，例如计费方式选择、分流策略来源选择；这是产品文档直接表达的场景级选择 |
| `DeliverySolution` | `DecisionPoint` | `has_decision` | 包含决策点 | 某些方案内部存在关键分支，例如配额耗尽动作、访问限制动作、分流触发与 UPF 选择 |
| `DecisionPoint` | `Scope` | `conditioned_by` | 受范围条件约束 | 部分决策点只有在特定边界下才成立，尤其体现在 DNN、位置、PRA、DNAI 等分流触发条件上 |
| `DeliverySolution` | `ValidationPlan` | `validated_by` | 由其验收 | 一个方案需要有对应的验收模板来判断是否真正生效；依据来自调测文档和套餐后的验证链 |
| `ValidationPlan` | `EngineeringTask` | `executed_by` | 由其执行 | 验收计划通过验证态任务具体落地，这是图谱内部的执行组织关系；其依据来自调测步骤与 verify Task 的对应 |
| `ValidationPlan` | `BusinessRule` | `uses_rule` | 使用规则 | 验收计划内部依赖判断规则来形成可执行检查条件；这些规则由调测、故障案例和约束材料归纳而来 |
| `DeliverySolution` | `BusinessRule` | `governed_by` | 受规则治理 | 方案在落地和核查时会受校验规则、约束规则和诊断规则治理；这些规则来源于 License、告警、Trigger、配额和一致性等产品文档材料 |
| `NetworkScenario` | `DomainSemanticObject` | `uses_semantic_object` | 使用领域语义对象 | 场景先关联稳定语义对象，再下钻实现 |
| `DeliverySolution` | `DomainSemanticObject` | `instantiates_semantic_object` | 实例化领域语义对象 | 方案把抽象语义落实为可交付的语义组合 |
| `DeliverySolution` | `Feature` | `requires_capability` | 需要能力 | 方案依赖正式能力载体 |
| `DeliverySolution` | `ConfigObject` | `realized_by_config` | 由配置对象实现 | 方案最终要收敛到关键对象链 |

### 5.2 业务主链

```text
BusinessDomain
  -> NetworkScenario
  -> DeliverySolution
  -> EngineeringTask
```

含义：

- 先定义业务域
- 再识别这个业务域下有哪些典型场景
- 再把场景收敛成方案
- 再把方案拆成工程任务

这一条主链是产品文档最稳定的抽象结果：

- `BusinessDomain -> NetworkScenario` 对应产品文档的场景组织入口
- `NetworkScenario -> DeliverySolution` 对应套餐、解决方案概述和分流方案中的可落地方案闭包
- `DeliverySolution -> EngineeringTask` 对应“数据规划 -> 脚本执行 -> 调测验证”的实施结构

### 5.3 支撑关系

```text
DeliverySolution
  -> Participant
  -> Scope
  -> DecisionPoint
  -> ValidationPlan
  -> BusinessRule

NetworkScenario
  -> DecisionPoint

DecisionPoint
  -> Scope

ValidationPlan
  -> EngineeringTask(verify)
  -> BusinessRule
```

含义：

- 一个方案不是孤立存在
- 它必须说明由谁参与、对谁生效、哪些地方需要决策、如何验收、受哪些业务规则治理

这里要区分两类关系来源：

1. `产品文档直接支撑的关系`
   - `involves`
   - `applies_to`
   - `has_decision`
   - `validated_by`

2. `基于产品文档抽象出来的图谱组织关系`
   - `executed_by`
   - `uses_rule`
   - `governed_by`

第二类关系不是产品文档里的原生对象边，而是为了把调测步骤、故障案例、License/约束说明组织成可维护图谱而引入的关系。

### 5.4 向下桥接关系

```text
NetworkScenario / DeliverySolution
  -> DomainSemanticObject
  -> Feature
  -> ConfigObject
```

含义：

- 场景和方案不会直接跳成命令
- 中间要先经过语义桥，再连接正式特性和配置对象

## 6. 一张抽象的业务图谱

如果不带任何具体业务域，一张抽象业务图谱长这样：

```text
BusinessDomain
└─ 某业务域
   ├─ NetworkScenario
   │  ├─ 场景A
   │  ├─ 场景B
   │  └─ 场景C
   │
   ├─ DeliverySolution
   │  ├─ 方案1
   │  └─ 方案2
   │
   ├─ EngineeringTask
   │  ├─ 任务1
   │  ├─ 任务2
   │  └─ 任务3
   │
   ├─ Participant / Scope / DecisionPoint / ValidationPlan / BusinessRule
   └─ DomainSemanticObject / Feature / ConfigObject
```

这就是“业务图谱的定义”。

---

## Part B. 业务感知的业务图谱

## 7. `BusinessDomain = 业务感知`

这里的 `BusinessDomain` 对应中文对象名是 `业务域`。

### 7.1 `BusinessDomain` 的 schema 定义

**定位**：图谱的轻量根节点，只做一件事：限定讨论边界，并指向它包含的现网场景。

#### 属性

| 字段 | 类型 | 说明 |
|---|---|---|
| `domain_id` | `string` | 唯一标识，语义化命名，不绑定产品缩写 |
| `domain_name` | `string` | 域名称 |
| `domain_summary` | `string` | 一句话定义 |
| `status` | `string` | 数据状态 |

#### 边

```text
BusinessDomain --contains--> NetworkScenario
```

### 7.2 `BusinessDomain` 的实例

`业务感知` 可直接实例化为一个 `BusinessDomain`，最终结果如下：

| 字段 | 值 |
|---|---|
| `domain_id` | `service-awareness` |
| `domain_name` | `业务感知` |
| `domain_summary` | `在用户会话过程中，对用户的数据报文进行解析，从而区分出用户使用的不同业务，以实现策略控制和计费控制` |
| `status` | `accepted` |

因此这里最终写成：

```text
BusinessDomain
  domain_id      = service-awareness
  domain_name    = 业务感知
  domain_summary = 在用户会话过程中，对用户的数据报文进行解析，从而区分出用户使用的不同业务，以实现策略控制和计费控制
  status         = accepted
```

## 8. 业务感知的 `NetworkScenario`

这里的 `NetworkScenario` 对应中文对象名是 `现网场景`。

### 8.1 `NetworkScenario` 的 schema 定义

#### 属性

| 字段 | 类型 | 说明 |
|---|---|---|
| `scenario_id` | `string` | 唯一标识 |
| `scenario_name` | `string` | 场景名称 |
| `scenario_summary` | `string` | 一句话描述 |
| `judgment_basis` | `string` | 判断基础：什么情况下属于该场景 |
| `typical_outcome` | `string` | 典型结果 |
| `source_evidence_ids` | `list[string]` | 证据来源 |
| `status` | `string` | 数据状态 |

#### 边

```text
BusinessDomain --contains--> NetworkScenario
NetworkScenario --instantiated_as--> DeliverySolution
  属性: dependency_type (required/optional/none)
NetworkScenario --uses_semantic_object--> DomainSemanticObject
NetworkScenario --has_decision--> DecisionPoint
```

### 8.2 `NetworkScenario` 的实例

业务感知主图最终收敛为 4 类一级场景，结果如下：

| 字段 | `NS-01` | `NS-02` | `NS-03` | `NS-04` |
|---|---|---|---|---|
| `scenario_id` | `NS-01` | `NS-02` | `NS-03` | `NS-04` |
| `scenario_name` | `计费场景` | `带宽控制场景` | `访问限制场景` | `本地分流场景` |
| `scenario_summary` | `对不同业务流采用不同计费方式，结合默认计费、免费业务和配额动作完成计费闭环` | `对不同业务、用户或范围域施加差异化带宽控制，落实到QoS策略和QoS Flow` | `对指定业务流实施阻塞、重定向、头增强或Portal处理` | `将访问本地业务的数据导向本地DN/边缘DN，必要时公网/专网独立计费` |
| `judgment_basis` | `用户访问了可识别的业务流，或会话需要按规则进入默认计费、免费业务或配额处理` | `识别出特定业务、用户属性、时段或TOS，或根据签约/位置等条件生成不同SM策略` | `三四层、协议、七层条件命中，或命中导向类规则` | `满足DNN、位置、PRA、DNAI、selectedDnn、预定义规则或动态规则等分流触发条件` |
| `typical_outcome` | `专项业务单独计费、免费业务不计费、普通业务默认计费，必要时额度变化后切换到重定向或其他处理路径` | `某类业务限速、保障优先级、整形、映射到不同QoS Flow，获得差异化体验` | `业务被阻塞、被重定向到目标地址、被附加头增强，或进入Portal处理路径` | `UL CL/辅锚点分流，导向本地DN/边缘DN，公网/专网分别计量` |
| `status` | `active` | `active` | `active` | `active` |

## 10. 业务感知的 `DeliverySolution`

这里的 `DeliverySolution` 对应中文对象名是 `交付方案`。

### 10.1 `DeliverySolution` 的 schema 定义

#### 属性

| 字段 | 类型 | 说明 |
|---|---|---|
| `solution_id` | `string` | 唯一标识 |
| `solution_name` | `string` | 方案名称 |
| `solution_summary` | `string` | 一句话描述，概括方案闭包核心 |
| `core_mechanism_combo` | `string` | 核心机制组合 |
| `source_evidence_ids` | `list[string]` | 证据来源 |
| `status` | `string` | 数据状态 |

#### 边

```text
NetworkScenario --instantiated_as--> DeliverySolution
  属性: dependency_type (required/optional/none)
DeliverySolution --uses_task--> EngineeringTask (M:N)
DeliverySolution --involves--> Participant
DeliverySolution --applies_to--> Scope
DeliverySolution --has_decision--> DecisionPoint
DeliverySolution --validated_by--> ValidationPlan
DeliverySolution --governed_by--> BusinessRule
DeliverySolution --instantiates_semantic_object--> DomainSemanticObject
DeliverySolution --requires_capability--> Feature
DeliverySolution --realized_by_config--> ConfigObject
```

### 10.2 `DeliverySolution` 的实例

业务感知域下最终收敛为 4 个方案对象，结果如下：

| 字段 | `DS-01` | `DS-02` | `DS-03` | `DS-04` |
|---|---|---|---|---|
| `solution_id` | `DS-01` | `DS-02` | `DS-03` | `DS-04` |
| `solution_name` | `差异化计费组合方案（含配额分支）` | `访问限制组合方案` | `带宽控制与QoS编排方案` | `本地分流与独立计费方案` |
| `solution_summary` | `通过过滤条件识别业务流，按优先级裁决Rule，绑定PCC/URR计费链实现差异化计费、免费业务与默认计费，并在配额耗尽后通过DecisionPoint切换用户体验` | `通过过滤条件识别目标业务流，按Rule裁决命中后执行阻塞、头增强、IP重定向或URL重定向等处理路径，实现多维访问管控` | `通过过滤条件识别业务流，绑定BWM带宽控制策略实现限速/保障/整形，必要时与QoS Flow映射结合实现端到端体验保障` | `在满足分流触发条件时，通过UL CL/辅锚点UPF将业务流导向本地DN/边缘DN，主/辅锚点各自独立执行计费，实现公网/专网会话分离计量与计费` |
| `core_mechanism_combo` | `过滤条件(IPLIST/FILTER/L7FILTER/FLOWFILTER) + Rule优先级裁决 + PCC/URR计费链(PCCPOLICYGRP-URRGROUP-URR) + 默认URR组兜底 + Trigger驱动计费会话更新 + 配额耗尽动作切换(BLOCK/REDIRECT/FORWARD)` | `过滤条件(FILTER/L7FILTER/FLOWFILTER) + Rule裁决 + 多策略类型处理路径(PCC阻塞/HEADEN头增强/IPREDIR重定向/PCC重定向) + 优先级控制(高优先级Rule优先匹配)` | `过滤条件(FILTER/L7FILTER/FLOWFILTER) + BWM带宽控制策略(CATEGORYPROP→BWMSERVICE→BWMCONTROLLER) + Rule优先级 + 例外黑名单(BLACKLISTRULE) + QoS Flow映射（静态/动态规则） + 端到端QoS编排(PCF→SMF→UPF/RAN/UE)` | `分流策略来源(PCF下发/SMF下发/PCF经SMF下发/MPF下发) + UL CL/辅锚点UPF选择与插入 + 会话修改(UE-基站-ULCL-主/辅锚点) + 本地DN导向 + 主/辅锚点独立计费(各UPF独享配额)` |
| `source_evidence_ids` | `["套餐1_93112148","计费解决方案概述_90776649","融合计费概述_42995681"]` | `["套餐3_94838086"]` | `["套餐2_94838085"]` | `["How分流_58273329","MEC计费流程_52284255","GWFD-020531特性概述_57047936"]` |
| `status` | `active` | `active` | `active` | `active` |


## 11. 业务感知的 `EngineeringTask`（工程任务）

### 11.1 Schema 定义

**定位**：原子动作单元，可被多个 DS 或 Feature 复用。不再绑定单一 DS。Task 不是“配置步骤”的同义词，而是覆盖 `plan / execute / verify` 三类工程动作的更高层单元；其中只有 execute 类 Task 才会在需要时下沉到特性图谱中的 `ConfigStep`。

**属性**：

| 字段 | 类型 | 必选 | 说明 |
|------|------|------|------|
| task_id | string | 是 | 唯一标识 |
| task_name | string | 是 | 任务名称 |
| task_summary | string | 是 | 一句话描述 |
| phase | string | 是 | 阶段：plan / execute / verify |
| input_artifacts | list[string] | 是 | 需要的输入 |
| output_artifacts | list[string] | 是 | 产出的输出 |
| command | string | 否 | 命令示例（`ADD`/`SET`/`LST`/`DSP`，plan 阶段为 `-`） |
| config_object | string | 否 | 涉及的配置对象（plan 阶段为 `-`） |
| source_evidence_ids | list[string] | 是 | 证据来源文档 ID 列表 |
| status | string | 是 | 数据状态 |

**边**：

```
DeliverySolution --uses_task--> EngineeringTask (M:N)
Feature --contains--> EngineeringTask (M:N，后续Feature定义时启用)
EngineeringTask --creates_config--> ConfigObject (execute phase)
EngineeringTask --verifies_config--> ConfigObject (verify phase)
EngineeringTask --realized_by_config_step--> ConfigStep (0:N, execute phase，可选)
EngineeringTask --supported_by--> Evidence
```

> 决策依据：D5（phase 字段）、D6（Task 不等于配置步骤；特性图谱保留 `ProcedureVariant → ConfigStep`，业务 execute Task 在需要时映射到 `ConfigStep`）、M:N 共享模型（Task 是原子单元，可被 DS 和 Feature 复用）

### 11.2 方案到任务的映射表

#### 共享任务（多个 DS 共用）

| 原子 Task ID | Task 名称 | phase | 涉及 ConfigObject | DS-01 | DS-02 | DS-03 | DS-04 |
|-------------|-----------|-------|-------------------|-------|-------|-------|-------|
| T-PLAN-001 | 规划生效范围 | plan | - | ✓ | ✓ | ✓ | ✓ |
| T-PLAN-002 | 规划识别条件 | plan | - | ✓ | ✓ | ✓ | ✓ |
| T-PLAN-003 | 规划 Rule 与优先级 | plan | - | ✓ | ✓ | ✓ | ✓ |
| T-EXEC-001 | 配置 IP 地址列表 | execute | IPLIST | ✓ | - | - | - |
| T-EXEC-002 | 配置三四层过滤条件 | execute | FILTER | ✓ | ✓ | ✓ | - |
| T-EXEC-003 | 配置七层过滤条件 | execute | L7FILTER | ✓ | ✓ | ✓ | - |
| T-EXEC-004 | 配置流过滤器与绑定 | execute | FLOWFILTER, FLTBINDFLOWF, PROTBINDFLOWF | ✓ | ✓ | ✓ | - |
| T-EXEC-008 | 配置 Rule | execute | RULE | ✓ | ✓ | ✓ | - |
| T-EXEC-010 | 配置 UserProfile 与 Rule 绑定 | execute | USERPROFILE, RULEBINDING, REFRESHSRV | ✓ | ✓ | ✓ | - |

#### 方案特有任务

| 原子 Task ID | Task 名称 | phase | 涉及 ConfigObject | 所属 DS |
|-------------|-----------|-------|-------------------|---------|
| T-PLAN-004 | 规划计费对象与费率标识 | plan | - | DS-01 |
| T-PLAN-005 | 规划配额耗尽动作 | plan | - | DS-01 |
| T-PLAN-006 | 规划导向与增强动作 | plan | - | DS-02 |
| T-PLAN-007 | 规划 BWM 策略 | plan | - | DS-03 |
| T-PLAN-008 | 规划分流触发与锚点插入 | plan | - | DS-04 |
| T-PLAN-009 | 规划计费 Trigger 与多 UPF 配额 | plan | - | DS-04 |
| T-EXEC-005 | 配置计费动作链 | execute | URR, URRGROUP, PCCPOLICYGRP | DS-01 |
| T-EXEC-006 | 配置策略动作链 | execute | PCCACTIONPROP, HEADEN, REDIRECT, PCCPOLICYGRP | DS-02 |
| T-EXEC-007 | 配置 BWM 带宽控制链 | execute | CATEGORYPROP, BWMSERVICE, BWMCONTROLLER, BWMUSERGROUP, BWMRULE | DS-03 |
| T-EXEC-009 | 配置 BlacklistRule | execute | BLACKLISTRULE | DS-03 |
| T-VERIFY-001 | 验证 License 开关 | verify | LICENSESWITCH | DS-01 |
| T-VERIFY-002 | 验证配置链逐层回查 | verify | RULEBINDING→RULE→...→FILTER 全链路 | DS-01, DS-02 |
| T-VERIFY-003 | 验证 PFCP 会话上报与计费流量 | verify | PFCP Session Report | DS-01 |
| T-VERIFY-004 | 验证三四层阻塞生效 | verify | RULEBINDING→RULE→PCCPOLICYGRP→PCCACTIONPROP→FILTER | DS-02 |
| T-VERIFY-005 | 验证七层配置链 | verify | RULEBINDING→RULE→...→L7FILTER→FILTER 全链路 | DS-02 |
| T-VERIFY-006 | 验证带宽控制策略生效 | verify | BWM 全链路 | DS-03 |

#### 各方案任务编排顺序

**DS-01 差异化计费组合方案**：

```
T-PLAN-001 → T-PLAN-002 → T-PLAN-003 → T-PLAN-004 → T-PLAN-005
→ T-EXEC-001 → T-EXEC-002 → T-EXEC-003 → T-EXEC-004 → T-EXEC-005 → T-EXEC-008 → T-EXEC-010
→ T-VERIFY-001 → T-VERIFY-002 → T-VERIFY-003
```

**DS-02 访问限制组合方案**：

```
T-PLAN-001 → T-PLAN-002 → T-PLAN-003 → T-PLAN-006
→ T-EXEC-002 → T-EXEC-003 → T-EXEC-004 → T-EXEC-006 → T-EXEC-008 → T-EXEC-010
→ T-VERIFY-004 → T-VERIFY-005
```

**DS-03 带宽控制与 QoS 编排方案**：

```
T-PLAN-001 → T-PLAN-002 → T-PLAN-003 → T-PLAN-007
→ T-EXEC-002 → T-EXEC-003 → T-EXEC-004 → T-EXEC-007 → T-EXEC-009 → T-EXEC-008 → T-EXEC-010
→ T-VERIFY-006
```

**DS-04 本地分流与独立计费方案**（源文档无完整脚本实例，仅规划态）：

```
T-PLAN-001 → T-PLAN-008 → T-PLAN-009
```

### 11.3 原子 Task 详情

> 以下逐个 Task 列出完整字段。plan 态 Task 无 ConfigObject 和命令映射；execute/verify 态 Task 需列明 ConfigObject 和命令示例。内容来源于原始产品文档，逐个 Task 从源文档提取。

（待填充——逐个 Task 从产品文档提取 ConfigObject 和命令示例）

#### T-PLAN-001 规划生效范围

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-001 |
| task_name | 规划生效范围 |
| task_summary | 确定策略对谁生效：定义用户范围、业务边界、DNN/APN 和默认兜底策略，最终体现为 UserProfile 的名称、结构与规则绑定规划 |
| phase | plan |
| input_artifacts | ["用户范围定义", "业务边界", "DNN/APN 规划", "默认兜底策略要求"] |
| output_artifacts | ["UserProfile 名称与结构规划", "默认策略绑定规划（如 DFTURRGRPNAME）", "规则绑定分配方案"] |
| command | - |
| config_object | - |
| source_evidence_ids | ["套餐1_93112148", "套餐2_94838085", "套餐3_94838086"] |
| status | active |

> 证据：三个套餐各创建一个 UserProfile（up_charging / up_bwmcontrol / up_policy）作为范围边界。套餐1 数据段："业务4作为兜底策略...计费策略可以直接配置在User Profile中"。套餐1 步骤7："配置User Profile，并绑定普通策略"——`ADD USERPROFILE` + `SET URRGRPBINDING`（设置默认 URR 组）。UserProfile 是生效范围的载体，所有规则通过 RULEBINDING 绑定到同一个 UserProfile 下，形成最终业务套餐。

#### T-PLAN-002 规划识别条件

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-002 |
| task_name | 规划识别条件 |
| task_summary | 将业务描述翻译成可匹配的过滤条件：L3/L4 过滤器（FILTER）、协议绑定（PROTBINDFLOWF）、L7 URL 过滤器（L7FILTER），并组合成流过滤器（FLOWFILTER/FLOWFILTERGRP） |
| phase | plan |
| input_artifacts | ["业务描述（协议、URL、地址、端口）", "过滤条件与识别逻辑"] |
| output_artifacts | ["过滤条件规划表：FILTER/L7FILTER/PROTBINDFLOWF 的对应关系与参数"] |
| command | - |
| config_object | - |
| source_evidence_ids | ["套餐1_93112148", "套餐2_94838085", "套餐3_94838086"] |
| status | active |

> 证据：套餐1 数据段将"用户访问 www.huawei.com 网站"翻译为 FILTER(filterA, ANY) + L7FILTER(l7filterA, URL=www.huawei.com/\*) + PROTOCOL=HTTPS → flowfilterA。套餐1 业务3 是两种条件的并集（IP 地址 OR RTSP 协议），需要 FLOWFILTERGRP 组合。套餐3 业务3 使用端口范围 MSSTARTPORT=1000, MSENDPORT=20000。套餐2 业务3 例外情况通过 BLACKLISTRULE 排除。核心翻译模式：特定 URL → L7FILTER；特定协议 → PROTBINDFLOWF；特定 IP → FILTER+IPLIST；"任意" → FILTER(ANY)。

#### T-PLAN-003 规划 Rule 与优先级

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-003 |
| task_name | 规划 Rule 与优先级 |
| task_summary | 决定多业务重叠时谁先生效，按业务语义分配 PRIORITY 数值（数值越小优先级越高），覆盖型规则优先于常规规则，兜底规则最低 |
| phase | plan |
| input_artifacts | ["多类业务目标和动作关系", "过滤条件是否有交集"] |
| output_artifacts | ["Rule 层次与优先级排序"] |
| command | - |
| config_object | - |
| source_evidence_ids | ["套餐1_93112148", "套餐2_94838085", "套餐3_94838086"] |
| status | active |

> 证据：套餐1 数据段——"当多个业务出现重合时，业务编号越小，优先级越高"，PRIORITY=100/200/300/400 简单递增。套餐2 业务5（累计流量超50GB时限速）需覆盖所有其他业务，PRIORITY=50 最高优先级，业务4 兜底 PRIORITY=200。套餐3 业务4（话费耗尽重定向）PRIORITY=400 覆盖业务1-3（500/550/700）。优先级按业务语义分配，非简单编号顺序。

#### T-PLAN-004 规划计费对象与费率标识

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-004 |
| task_name | 规划计费对象与费率标识 |
| task_summary | 根据资费模型（单价/免费/兜底）和在线/离线要求，规划 URR→URRGROUP→PCCPOLICYGRP 计费对象链，将每条业务的费率落到可执行的控制面对象 |
| phase | plan |
| input_artifacts | ["资费模型（如 1元/GB、免费、0.1元/GB）", "在线/离线计费方式要求", "业务粒度"] |
| output_artifacts | ["URR 及 URRID 规划表", "URRGROUP 规划", "PCCPOLICYGRP 规划", "默认 URR 组绑定方案"] |
| command | - |
| config_object | - |
| source_evidence_ids | ["套餐1_93112148"] |
| status | active |

> 证据：套餐1 数据段——"业务1、2、4都涉及到了计费，URRID 分别为 urrA=1000、urrB=2000、urrD=3000"。业务3 免费："设置 urrC=4000, OFFMETERINGTYPE=FREE"。业务4 兜底："SET URRGRPBINDING: DFTURRGRPNAME='urrgD'"。

#### T-PLAN-005 规划配额耗尽动作

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-005 |
| task_name | 规划配额耗尽动作 |
| task_summary | 规划在线计费配额耗尽后用户体验如何变化：阻断(BLOCK)、重定向(REDIRECT)还是放行(FORWARD)，并设计对应的动作策略 |
| phase | plan |
| input_artifacts | ["配额控制要求", "用户体验要求（耗尽后是否允许继续访问）"] |
| output_artifacts | ["配额耗尽动作策略（BLOCK/REDIRECT/FORWARD）"] |
| command | - |
| config_object | - |
| source_evidence_ids | ["计费解决方案概述_90776649", "融合计费概述_42995681", "套餐3_94838086"] |
| status | active |

> 证据：套餐3 业务4——"话费余额耗尽场景下，用户访问任何网站都会重定向到充值页面"。计费解决方案概述——"在线计费：进行配额管理...在配额不足时，SMF 可以停止业务使用"。

#### T-PLAN-006 规划导向与增强动作

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-006 |
| task_name | 规划导向与增强动作 |
| task_summary | 规划访问限制场景中除简单阻断外的多种动作：阻塞(DISCARD)、头增强(HEADEN+MSISDN+防欺诈)、IP重定向(IPREDIR)、URL重定向(REDIRECT)，确定参数和优先级 |
| phase | plan |
| input_artifacts | ["导向目标（阻塞/重定向 IP/URL）", "安全增强需求（ANTIFRAUD）", "Portal 约束"] |
| output_artifacts | ["PCCACTIONPROP/HEADEN/REDIRECT/IPREDIR 动作设计"] |
| command | - |
| config_object | - |
| source_evidence_ids | ["套餐3_94838086"] |
| status | active |

> 证据：套餐3——业务1"流动作是阻塞，通过配置 PCC 动作属性完成"（DISCARD 四方向门控）。业务2"插入 MSISDN 号和防欺诈"（HEADEN+ANTIFRAUD=ENABLE）。业务3"IP 重定向"（IPREDIRECTIP=10.100.111.222）。业务4"URL 重定向到充值页面"。

#### T-PLAN-007 规划 BWM 策略

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-007 |
| task_name | 规划 BWM 策略 |
| task_summary | 根据带宽控制目标（CIR 保障/PIR 限速/RATE 整形）为每条业务规划 BWMCONTROLLER 参数，处理例外黑名单和 FUP 限额后限速场景 |
| phase | plan |
| input_artifacts | ["每条业务的带宽目标（保障/限速/整形）", "速率参数（10M/8M/20M/2M）", "例外情况需求"] |
| output_artifacts | ["BWMCONTROLLER 参数表（CIR/PIR/RATE）", "CATEGORYPROP/BWMSERVICE 链规划", "黑名单规划"] |
| command | - |
| config_object | - |
| source_evidence_ids | ["套餐2_94838085"] |
| status | active |

> 证据：套餐2——"bwmcontrolerA:CIR=10240(最低保障)、bwmcontrolerB:PIR=8192(限速)、bwmcontrolerC:RATE=10240(整形)、bwmcontrolerD:PIR=20480(兜底限速)、bwmcontrolerE:PIR=2048(限额后限速)"。业务3 例外："需要配置黑名单规则"。

#### T-PLAN-008 规划分流触发与锚点插入

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-008 |
| task_name | 规划分流触发与锚点插入 |
| task_summary | 规划本地分流何时触发（DNN+位置/PRA/DNAI/动态规则），SMF 如何选择 UL CL UPF 和辅锚点 UPF，以及如何通过 PFCP 会话修改将常规 PDU 会话更新为分流 PDU 会话 |
| phase | plan |
| input_artifacts | ["DNN/位置/PRA/DNAI/触发方式", "UPF 能力和切片信息"] |
| output_artifacts | ["UL CL 触发条件", "主/辅锚点选择方案", "PFCP 会话建立方案"] |
| command | - |
| config_object | - |
| source_evidence_ids | ["How分流_58273329"] |
| status | active |

> 证据：How分流——"SMF 会实时检测用户的位置（TAI 区或小区），一旦 DNN+位置组合满足分流触发条件便触发分流"。UL CL UPF 决策条件："是否支持 UL CL 功能、用户切片信息、用户位置区信息"。辅锚点决策条件："DNAI 信息、DNN 与切片信息"。

#### T-PLAN-009 规划计费 Trigger 与多 UPF 配额

| 字段 | 值 |
|------|-----|
| task_id | T-PLAN-009 |
| task_name | 规划计费 Trigger 与多 UPF 配额 |
| task_summary | 规划本地分流场景下主/辅锚点各自的计费规则下发、Trigger 驱动的配额申请机制，以及 SMF 按 UPF 向 CHF 独立申请配额的多 UPF 配额管理策略 |
| phase | plan |
| input_artifacts | ["计费方式", "RG 粒度", "Trigger 类别", "锚点 UPF 数量"] |
| output_artifacts | ["Trigger 策略", "多 UPF 配额策略", "计费规则下发方案"] |
| command | - |
| config_object | - |
| source_evidence_ids | ["MEC计费流程_52284255", "融合计费概述_42995681"] |
| status | active |

> 证据：MEC 计费流程——"SMF 按 UPF 向 CHF 申请配额（消息中 Multiple Unit Usage 字段携带 UPF ID），哪个 UPF 申请就向哪个 UPF 下发配额"。"UL CL UPF 没有计费规则，不计费。通常 UL CL UPF 与辅锚点合设"。

#### T-EXEC-002 配置三四层过滤条件

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-002 |
| task_name | 配置三四层过滤条件 |
| task_summary | 创建三四层过滤器，定义协议类型、源/目的 IP 地址或 IP 列表等匹配条件 |
| phase | execute |
| input_artifacts | ["规划态输出的过滤条件规划表"] |
| output_artifacts | ["FILTER 配置"] |
| command | `ADD FILTER:FILTERNAME="filterA",L34PROTTYPE=STRING,L34PROTOCOL=ANY;`<br>`ADD FILTER:FILTERNAME="filterC",L34PROTTYPE=STRING,L34PROTOCOL=TCP,SVRIPMODE=IPLIST,SVRIPLISTNAME="iplistB";` |
| config_object | `FILTER` |
| source_evidence_ids | ["套餐1_93112148", "套餐2_94838085", "套餐3_94838086"] |
| status | active |

**各方案参数差异**：

| 方案 | 过滤器名 | 关键参数 | 来源 |
|------|---------|---------|------|
| DS-01 计费 | filterA(ANY), filterC(TCP+IPLIST) | L34PROTOCOL=ANY/TCP, SVRIPMODE=IPLIST | 套餐1 步骤2 |
| DS-02 访问限制 | filterA(ANY), filterC(端口范围) | MSSTARTPORT=1000, MSENDPORT=20000 | 套餐3 步骤1 |
| DS-03 带宽控制 | filterA(ANY), filterC1(指定IP) | SVRIP="10.11.12.13" | 套餐2 步骤1 |

#### T-EXEC-001 配置 IP 地址列表

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-001 |
| task_name | 配置 IP 地址列表 |
| task_summary | 创建 IP 地址列表（IPLIST），供三四层过滤器引用以匹配特定服务器 IP 地址范围 |
| phase | execute |
| input_artifacts | ["规划态输出的 IP 地址规划表"] |
| output_artifacts | ["IPLIST 配置"] |
| command | `ADD IPLIST:IPLISTNAME="iplistB",IPVERSION=IPV4,IPV4ADDR="10.123.234.10",MASKVALUE=32;`<br>`ADD IPLIST:IPLISTNAME="iplistB",IPVERSION=IPV4,IPV4ADDR="10.123.234.11",MASKVALUE=32;`<br>`ADD IPLIST:IPLISTNAME="iplistB",IPVERSION=IPV4,IPV4ADDR="10.123.234.12",MASKVALUE=32;`<br>`ADD IPLIST:IPLISTNAME="iplistB",IPVERSION=IPV4,IPV4ADDR="10.123.234.13",MASKVALUE=32;` |
| config_object | `IPLIST` |
| source_evidence_ids | ["套餐1_93112148"] |
| status | active |

**说明**：IPLIST 仅在计费场景（DS-01）中使用，用于业务3中 filterC 匹配 10.123.234.10~10.123.234.13 范围内的服务器 IP 地址。同名的多条 ADD IPLIST 命令向同一列表追加不同 IP 条目。

#### T-EXEC-003 配置七层过滤条件

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-003 |
| task_name | 配置七层过滤条件 |
| task_summary | 创建七层过滤器，定义应用层 URL 匹配条件或协议绑定关系，用于识别特定网站访问或应用协议流量 |
| phase | execute |
| input_artifacts | ["规划态输出的七层过滤条件规划表"] |
| output_artifacts | ["L7FILTER 配置"] |
| command | `ADD L7FILTER:L7FILTERNAME="l7filterA",SUBL7FLTNAME="sl7A",URLTYPE=URL,URL="www.huawei.com/*";` |
| config_object | `L7FILTER` |
| source_evidence_ids | ["套餐1_93112148", "套餐2_94838085", "套餐3_94838086"] |
| status | active |

**各方案参数差异**：

| 方案 | 过滤器名 | 关键参数 | 来源 |
|------|---------|---------|------|
| DS-01 计费 | l7filterA | URLTYPE=URL, URL="www.huawei.com/*" | 套餐1 步骤3 |
| DS-02 带宽控制 | l7filterA, l7filterB, l7filterC | l7filterA: URL="www.huawei.com"; l7filterB: 无 URL（仅协议绑定）；l7filterC: URL="www.example.com*/*" | 套餐2 步骤2 |
| DS-03 访问限制 | l7filterA, l7filterB | l7filterA: URL="www.huawei.com"; l7filterB: URL="www.vmall.com" | 套餐3 步骤2 |

#### T-EXEC-004 配置流过滤器与绑定

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-004 |
| task_name | 配置流过滤器与绑定 |
| task_summary | 配置流过滤器（组），并将三四层、七层过滤条件与流过滤器绑定——流过滤器是三四层过滤条件与七层过滤条件的组合 |
| phase | execute |
| input_artifacts | ["FILTER对象", "L7FILTER对象", "IPLIST对象(可选)", "协议识别规划"] |
| output_artifacts | ["FLOWFILTER对象", "FLOWFILTERGRP对象(可选)", "FLTBINDFLOWF绑定关系", "PROTBINDFLOWF绑定关系"] |
| command | `ADD FLOWFILTER:FLOWFILTERNAME="flowfilterA";`<br>`ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilterA",FILTERNAME="filterA";`<br>`ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilterA",PROTOCOLNAME="HTTPS",L7FILTERNAME="l7filterA";`<br>`ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilterB",PROTOCOLNAME="HTTP";`<br>`ADD FLOWFILTERGRP:FLWFLTRGRPNAME="flowfiltergroupC",FLOWFILTERNAME="flowfilterC1";`<br>`ADD FLOWFILTERGRP:FLWFLTRGRPNAME="flowfiltergroupC",FLOWFILTERNAME="flowfilterC2";` |
| config_object | `FLOWFILTER`, `FLOWFILTERGRP`, `FLTBINDFLOWF`, `PROTBINDFLOWF` |
| source_evidence_ids | ["套餐1_93112148", "套餐2_94838085", "套餐3_94838086"] |
| status | active |

**各方案参数差异**：

| 方案 | FLOWFILTER 数量 | 绑定模式 | FLOWFILTERGRP | 来源 |
|------|----------------|---------|---------------|------|
| DS-01 计费 | 4 个 (A/B/C1+C2/D) | FLTBINDFLOWF + PROTBINDFLOWF | 是 (groupC 含 C1+C2) | 套餐1 步骤4 |
| DS-02 带宽控制 | 5 个 (A/B/C/C1/D) | FLTBINDFLOWF + PROTBINDFLOWF | 否 | 套餐2 步骤3 |
| DS-03 访问限制 | 4 个 (A/B/C/D) | FLTBINDFLOWF + PROTBINDFLOWF | 否 | 套餐3 步骤3 |

**绑定模式说明**：
- **FLTBINDFLOWF**：将三四层 FILTER 绑定到 FLOWFILTER（每个 FLOWFILTER 必须绑定至少一个 FILTER）
- **PROTBINDFLOWF**：将协议 + 可选七层过滤器绑定到 FLOWFILTER；仅协议识别时可省略 L7FILTERNAME
- **FLOWFILTERGRP**：多条件组合（或关系）时使用，将多个 FLOWFILTER 编入同一组

#### T-EXEC-005 配置计费动作链

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-005 |
| task_name | 配置计费动作链 |
| task_summary | 配置离线计费的流动作链：创建 URR 定义计费方式与上报模式，创建 URRGROUP 组合上下行 URR，创建 PCCPOLICYGRP 将 URRGROUP 绑定到 PCC 策略组 |
| phase | execute |
| input_artifacts | ["FILTER 配置", "FLOWFILTER 配置"] |
| output_artifacts | ["URR 配置", "URRGROUP 配置", "PCCPOLICYGRP 配置"] |
| command | `ADD URR:URRNAME="urrA",URRID=1000,USAGERPTMODE=OFFLINE;`<br>`ADD URRGROUP:URRGROUPNAME="urrgA",UPURRNAME1="urrA",DOWNURRNAME1="urrA";`<br>`ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccgA",URRGROUPNAME="urrgA";`<br>`ADD URR:URRNAME="urrC",URRID=4000,USAGERPTMODE=OFFLINE,OFFMETERINGTYPE=FREE;`<br>`ADD URRGROUP:URRGROUPNAME="urrgC",UPURRNAME1="urrC",DOWNURRNAME1="urrC";`<br>`ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccgC",URRGROUPNAME="urrgC";` |
| config_object | `URR`, `URRGROUP`, `PCCPOLICYGRP` |
| source_evidence_ids | ["套餐1_93112148"] |
| status | active |

**说明**：计费动作链为三层嵌套结构：URR（定义计费规则/URRID/上报模式）→ URRGROUP（组合上下行 URR）→ PCCPOLICYGRP（封装为 PCC 策略组，供 RULE 引用）。免费业务通过 `OFFMETERINGTYPE=FREE` 实现零计费。此任务仅用于 DS-01（计费场景）。

#### T-EXEC-006 配置策略动作链

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-006 |
| task_name | 配置策略动作链 |
| task_summary | 为访问限制场景配置策略动作链，包括 PCC 阻塞动作属性、HTTP 头增强（插入 MSISDN+防欺诈）、URL 重定向三种动作类型 |
| phase | execute |
| input_artifacts | ["FLOWFILTER 配置", "策略类型规划"] |
| output_artifacts | ["PCCACTIONPROP 配置", "HEADEN 配置", "REDIRECT 配置", "PCCPOLICYGRP 配置"] |
| command | `ADD PCCACTIONPROP:PCCACTPROPNAME="pccactA",UPINITUPGATE=DISCARD,UPINITDNGATE=DISCARD,DNINITUPGATE=DISCARD,DNINITDNGATE=DISCARD;`<br>`ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccgrpA",PCCACTPROPNAME="pccactA";`<br>`ADD HEADEN:HEADERENNAME="headenB",DATATYPE=MSISDN1,ANTIFRAUD=ENABLE;`<br>`ADD REDIRECT:REDIRECTNAME="redirectD",URL="www.huawei.com";`<br>`ADD PCCACTIONPROP:PCCACTPROPNAME="pccactD",UPINITREDIRNM="redirectD";`<br>`ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccgrpD",PCCACTPROPNAME="pccactD";` |
| config_object | `PCCACTIONPROP`, `HEADEN`, `REDIRECT`, `PCCPOLICYGRP` |
| source_evidence_ids | ["套餐3_94838086"] |
| status | active |

**说明**：访问限制场景包含三种策略动作类型：**PCC 阻塞**（PCCACTIONPROP 四向门控置 DISCARD）→ PCCPOLICYGRP 包装；**头增强**（HEADEN 插入 MSISDN+防欺诈）可直接被 RULE 引用；**URL 重定向**（REDIRECT 指定目标 URL → PCCACTIONPROP 引用 REDIRECT → PCCPOLICYGRP 包装）。此任务仅用于 DS-02（访问限制）。

#### T-EXEC-007 配置 BWM 带宽控制链

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-007 |
| task_name | 配置 BWM 带宽控制链 |
| task_summary | 创建带宽管理控制链：配置 CATEGORYPROP → BWMSERVICE → BWMCONTROLLER → BWMUSERGROUP → BWMRULE，支持最低速率保障（CAR+CIR）、最高速率限制（CAR+PIR）、流量整形（SHAPING+RATE）三种模式 |
| phase | execute |
| input_artifacts | ["FLOWFILTER 配置"] |
| output_artifacts | ["CATEGORYPROP 配置", "BWMSERVICE 配置", "BWMCONTROLLER 配置", "BWMUSERGROUP 配置", "BWMRULE 配置"] |
| command | `ADD CATEGORYPROP:CATEPROPNAME="catropA";`<br>`ADD BWMSERVICE:BWMSERVICENAME="bwmservA",BWMSERVICETYPE=NONTOS,NONTOSSRVTYPE=CATEGORY_PROP,CATEPROPNAME="catropA";`<br>`ADD BWMCONTROLLER:BWMCNAME="bwmcontrolA",CTRLTYPE=CAR,CIR=10240;`<br>`ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpA",USERGROUPPRI=100,USERLEVSRVTYPE=NONTOS;`<br>`ADD BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpA",BWMRULETYPE=SUBSCRIBER_SPECIFIC,BWMRULENAME="bwmruleA",BWMSERVICENAME="bwmservA",UPBWMCTRLNAME1="bwmcontrolA",DNBWMCTRLNAME1="bwmcontrolA",BWMRULEPRI=100;`<br>`ADD CATEGORYPROP:CATEPROPNAME="catropB";`<br>`ADD BWMCONTROLLER:BWMCNAME="bwmcontrolB",CTRLTYPE=CAR,PIR=8192;`<br>`ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpB",USERGROUPPRI=110,USERLEVSRVTYPE=NONTOS;`<br>`ADD BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpB",BWMRULETYPE=SUBSCRIBER_SPECIFIC,BWMRULENAME="bwmruleB",BWMSERVICENAME="bwmservB",UPBWMCTRLNAME1="bwmcontrolB",DNBWMCTRLNAME1="bwmcontrolB",BWMRULEPRI=110;`<br>`ADD CATEGORYPROP:CATEPROPNAME="catropC";`<br>`ADD BWMCONTROLLER:BWMCNAME="bwmcontrolC",CTRLTYPE=SHAPING,RATE=10240;`<br>`ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpC",USERGROUPPRI=120,USERLEVSRVTYPE=NONTOS;`<br>`ADD BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpC",BWMRULETYPE=SUBSCRIBER_SPECIFIC,BWMRULENAME="bwmruleC",BWMSERVICENAME="bwmservC",UPBWMCTRLNAME1="bwmcontrolC",DNBWMCTRLNAME1="bwmcontrolC",BWMRULEPRI=120;` |
| config_object | `CATEGORYPROP`, `BWMSERVICE`, `BWMCONTROLLER`, `BWMUSERGROUP`, `BWMRULE` |
| source_evidence_ids | ["套餐2_94838085"] |
| status | active |

**说明**：BWM 控制链为五层结构：CATEGORYPROP（命名锚点）→ BWMSERVICE（绑定类别属性）→ BWMCONTROLLER（定义带宽参数，三种模式：CAR+CIR 保障/CA+PIR 限速/SHAPING+RATE 整形）→ BWMUSERGROUP（用户组+优先级）→ BWMRULE（绑定用户组+服务+控制器）。速率单位 Kbps。此任务仅用于 DS-03（带宽控制）。

#### T-EXEC-008 配置 Rule

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-008 |
| task_name | 配置 Rule |
| task_summary | 创建规则对象，将流过滤器（匹配条件）与策略动作（执行动作）绑定，并设定优先级——Rule 是 SA 配置链路的核心汇聚点 |
| phase | execute |
| input_artifacts | ["FLOWFILTER 配置", "策略动作配置（PCCPOLICYGRP/HEADEN/CATEGORYPROP）"] |
| output_artifacts | ["RULE 配置"] |
| command | `ADD RULE:RULENAME="ruleA",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterA",POLICYNAME="pccgA",PRIORITY=100;`<br>`ADD RULE:RULENAME="ruleC",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTERGRP,FLWFLTRGRPNAME="flowfiltergroupC",POLICYNAME="pccgC",PRIORITY=300;`<br>`ADD RULE:RULENAME="ruleB",POLICYTYPE=HEADEN,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterB",POLICYNAME="headenB",PRIORITY=550;`<br>`ADD RULE:RULENAME="ruleC",POLICYTYPE=IPREDIR,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterC",REDIRIPVERFLAG=IPV4,IPREDIRECTIP=10.100.111.222;`<br>`ADD RULE:RULENAME="ruleA",POLICYTYPE=BWM,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterA",POLICYNAME="catropA",PRIORITY=100;`<br>`ADD RULE:RULENAME="ruleE",POLICYTYPE=BWM,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterD",POLICYNAME="catropE",PRIORITY=50;` |
| config_object | `RULE`, `BLACKLISTRULE` |
| source_evidence_ids | ["套餐1_93112148", "套餐2_94838085", "套餐3_94838086"] |
| status | active |

**各方案参数差异**：

**各方案参数差异**：

| 方案 | POLICYTYPE | POLICYNAME 指向 | FILTERINGMODE | 来源 |
|------|-----------|----------------|---------------|------|
| DS-01 计费 | PCC | PCCPOLICYGRP (pccgX) | FLOWFILTER / FLOWFILTERGRP | 套餐1 步骤6 |
| DS-02 访问限制 | PCC / HEADEN / IPREDIR | PCCPOLICYGRP / HEADEN / 内联 IP | FLOWFILTER | 套餐3 步骤5 |
| DS-03 带宽控制 | BWM | CATEGORYPROP (catropX) | FLOWFILTER | 套餐2 步骤5 |

**核心语义**：Rule = flowfilter（匹配什么流量）+ POLICYTYPE + POLICYNAME（对流量做什么动作）+ PRIORITY（同类型规则间的匹配顺序）。IPREDIR 类型特殊：动作内联在 RULE 中（REDIRIPVERFLAG + IPREDIRECTIP），无需引用外部策略对象。

#### T-EXEC-009 配置 BlacklistRule

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-009 |
| task_name | 配置 BlacklistRule |
| task_summary | 为带宽控制场景中的例外流量创建黑名单规则，使特定流不受 BWM 策略限制——BlacklistRule 是 Rule 的例外豁免机制 |
| phase | execute |
| input_artifacts | ["FLOWFILTER 配置（例外流过滤器）"] |
| output_artifacts | ["BLACKLISTRULE 配置"] |
| command | `ADD BLACKLISTRULE:RULENAME="ruleC1",POLICYTYPE=BWM,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterC1";` |
| config_object | `BLACKLISTRULE` |
| source_evidence_ids | ["套餐2_94838085"] |
| status | active |

**说明**：BlacklistRule 无需指定 POLICYNAME 和 PRIORITY——其语义是"匹配到此流量的流量不做策略处理"，即豁免而非执行。需先为例外流量单独配置 FILTER + FLOWFILTER，再通过 BLACKLISTRULE 声明豁免。此任务仅用于 DS-03（带宽控制）。

#### T-EXEC-010 配置 UserProfile 与 Rule 绑定

| 字段 | 值 |
|------|-----|
| task_id | T-EXEC-010 |
| task_name | 配置 UserProfile 与 Rule 绑定 |
| task_summary | 创建 USERPROFILE 作为业务套餐容器，将 RULE 逐条绑定到其下，最后刷新服务使配置生效——UserProfile 是 SA 配置链路的最终汇聚与生效点 |
| phase | execute |
| input_artifacts | ["RULE 配置", "BLACKLISTRULE 配置（可选）", "URRGROUP 配置（DS-01）"] |
| output_artifacts | ["USERPROFILE 配置", "RULEBINDING 配置", "REFRESHSRV 生效"] |
| command | `ADD USERPROFILE:USERPROFILENAME="up_charging";`<br>`SET URRGRPBINDING:USERPROFILENAME="up_charging",DFTURRGRPNAME="urrgD",DFTSIGURRGNAME="urrgD";`<br>`ADD RULEBINDING:USERPROFILENAME="up_charging",RULENAME="ruleA",POLICYTYPE=PCC;`<br>`ADD RULEBINDING:USERPROFILENAME="up_charging",RULENAME="ruleB",POLICYTYPE=PCC;`<br>`ADD RULEBINDING:USERPROFILENAME="up_charging",RULENAME="ruleC",POLICYTYPE=PCC;`<br>`ADD RULEBINDING:USERPROFILENAME="up_charging",RULENAME="ruleD",POLICYTYPE=PCC;`<br>`SET REFRESHSRV:REFRESHTYPE=USERPROFILE;` |
| config_object | `USERPROFILE`, `RULEBINDING`, `REFRESHSRV`, `URRGRPBINDING` |
| source_evidence_ids | ["套餐1_93112148", "套餐2_94838085", "套餐3_94838086"] |
| status | active |

**各方案参数差异**：

| 方案 | UserProfile 名 | URRGRPBINDING | RULEBINDING 类型 | 绑定 Rule 数 | 来源 |
|------|---------------|---------------|-----------------|-------------|------|
| DS-01 计费 | up_charging | 有（默认 URRGROUP） | PCC | 4 条 | 套餐1 步骤7-8 |
| DS-02 访问限制 | up_policy | 无 | PCC / HEADEN / IPREDIR | 4 条 | 套餐3 步骤6 |
| DS-03 带宽控制 | up_bwmcontrol | 无 | BWM | 6 条（含 BlacklistRule） | 套餐2 步骤6 |

**核心语义**：ADD USERPROFILE（创建空容器）→ SET URRGRPBINDING（仅 DS-01，绑定默认计费组）→ 多条 ADD RULEBINDING（将 Rule 逐一绑定）→ SET REFRESHSRV（刷新生效）。RULEBINDING 的 POLICYTYPE 必须与对应 RULE 一致。

#### T-VERIFY-001 验证 License 开关

| 字段 | 值 |
|------|-----|
| task_id | T-VERIFY-001 |
| task_name | 验证 License 开关 |
| task_summary | 验证 SA 基础 License 开关已开启，确保业务感知功能可用；同时验证内容计费基本功能 License 已启用 |
| phase | verify |
| input_artifacts | ["所需 License 控制项列表"] |
| output_artifacts | ["License 开关状态查询结果"] |
| command | `LST LICENSESWITCH:LICITEM="LKV3G5SABS01";`<br>`LST LICENSESWITCH:LICITEM="LKV3G5BCBC01";` |
| config_object | `LICENSESWITCH` |
| source_evidence_ids | ["EVID-SA-BASIC-LICENSE", "EVID-CONTENT-BILLING-LICENSE"] |
| status | active |

**说明**：本任务在执行任何 SA 配置之前运行。SA-Basic（LKV3G5SABS01）是必须开启的基础 License；计费场景还需内容计费基本功能（LKV3G5BCBC01）。查询返回"开关=ENABLE"表示已开启。此任务仅用于 DS-01（计费场景）。

#### T-VERIFY-002 验证配置链逐层回查

| 字段 | 值 |
|------|-----|
| task_id | T-VERIFY-002 |
| task_name | 验证配置链逐层回查 |
| task_summary | 从 User Profile 出发，通过 LST 命令逐层回查 RULEBINDING→RULE→FLOWFILTER→FILTER 全链路配置，核实每一层的对象名称、绑定关系和过滤参数是否与规划值一致 |
| phase | verify |
| input_artifacts | ["UserProfile 名称", "规划参数表"] |
| output_artifacts | ["各层 LST 查询结果", "逐层一致性校验结论"] |
| command | `LST RULEBINDING:USERPROFILENAME="up_charging";`<br>`LST RULE:RULENAME="ruleA",POLICYTYPE=PCC;`<br>`LST PCCPOLICYGRP:PCCPOLICYGRPNM="pccgA";`<br>`LST FLOWFILTER:FLOWFILTERNAME="flowfilterA";`<br>`LST FLTBINDFLOWF:FLOWFILTERNAME="flowfilterA";`<br>`LST FILTER:FILTERNAME="filterA";` |
| config_object | `RULEBINDING`, `RULE`, `FLOWFILTER`, `FILTER`, `PCCPOLICYGRP`, `PCCACTIONPROP`, `PROTBINDFLOWF`, `L7FILTER` |
| source_evidence_ids | ["套餐1_93112148", "套餐3_94838086"] |
| status | active |

**各方案参数差异**：

| 对比维度 | DS-01 计费 | DS-02 访问限制 |
|----------|-----------|---------------|
| POLICYTYPE | 全部 PCC | 混合 PCC / HEADEN / IPREDIR |
| 策略层回查 | PCCPOLICYGRP→URRGROUP→URR | PCCPOLICYGRP→PCCACTIONPROP / HEADEN |
| 七层回查 | PROTBINDFLOWF→L7FILTER | 同左 |
| 来源 | 套餐1 步骤9 | 套餐3 步骤7 |

#### T-VERIFY-003 验证 PFCP 会话上报与计费流量

| 字段 | 值 |
|------|-----|
| task_id | T-VERIFY-003 |
| task_name | 验证 PFCP 会话上报与计费流量 |
| task_summary | 验证 UPF 向 SMF 发送的 PFCP Session Report 中 Usage Report 的 URR ID 与业务规则绑定一致，确认计费流量被正确识别和上报 |
| phase | verify |
| input_artifacts | ["T-VERIFY-002 配置链回查通过", "OM Portal N4 接口跟踪任务"] |
| output_artifacts | ["PFCP Session Report 验证结果", "URR ID 匹配确认"] |
| command | `LST RULEBINDING:USERPROFILENAME="up_charging";`<br>`LST RULE:RULENAME="ruleA";`<br>`LST PCCPOLICYGRP:PCCPOLICYGRPNM="pccgA";`<br>`LST URRGROUP:URRGROUPNAME="urrgA";`<br>`LST URR:URRNAME="urrA";`<br>`LST PROTBINDFLOWF:FLOWFILTERNAME="flowfilterA";`<br>`LST L7FILTER:L7FILTERNAME="l7filterA";` |
| config_object | `RULEBINDING`, `RULE`, `PCCPOLICYGRP`, `URRGROUP`, `URR`, `PROTBINDFLOWF`, `FLOWFILTER`, `L7FILTER` |
| source_evidence_ids | ["调测内容计费_08957400"] |
| status | active |

**操作步骤**：

1. 在 OM Portal 创建 N4 接口跟踪任务
2. 测试终端使用已配置 DNN 接入网络
3. 终端访问目标业务（如 www.huawei.com），浏览至满足上报条件
4. 查看 UPF 向 SMF 发送的 PFCP Session Report Request，检查 Usage Report 中 URR ID

**说明**：本任务是 DS-01（计费场景）的最终验收步骤。通过 OM Portal 的 N4 接口跟踪功能抓取 PFCP Session Report，核心判断标准：URR ID 是否与 ADD URR 配置一致。此任务仅用于 DS-01。

#### T-VERIFY-004 验证三四层阻塞生效

| 字段 | 值 |
|------|-----|
| task_id | T-VERIFY-004 |
| task_name | 验证三四层阻塞生效 |
| task_summary | 逐层回查 RULEBINDING→RULE→PCCPOLICYGRP→PCCACTIONPROP→FLTBINDFLOWF→FILTER 全链路，验证阻塞规则已正确绑定且门控动作为 DISCARD |
| phase | verify |
| input_artifacts | ["UserProfile 名称", "规划参数表"] |
| output_artifacts | ["各层 LST 查询结果", "阻塞验证结论"] |
| command | `LST RULEBINDING:USERPROFILENAME="up_policy";`<br>`LST RULE:RULENAME="ruleA";`<br>`LST PCCPOLICYGRP:PCCPOLICYGRPNM="pccgrpA";`<br>`LST PCCACTIONPROP:PCCACTPROPNAME="pccactA";`<br>`LST FLTBINDFLOWF:FLOWFILTERNAME="flowfilterA";`<br>`LST FILTER:FILTERNAME="filterA";` |
| config_object | `RULEBINDING`, `RULE`, `PCCPOLICYGRP`, `PCCACTIONPROP`, `FLTBINDFLOWF`, `FILTER` |
| source_evidence_ids | ["套餐3_94838086"] |
| status | active |

**验证要点**：PCCACTIONPROP 的四个门控字段（UPINITUPGATE/UPINITDNGATE/DNINITUPGATE/DNINITDNGATE）必须全部为 DISCARD。

**说明**：此任务仅用于 DS-02（访问限制）。

#### T-VERIFY-005 验证七层配置链

| 字段 | 值 |
|------|-----|
| task_id | T-VERIFY-005 |
| task_name | 验证七层配置链 |
| task_summary | 逐层回查 DS-02 中涉及七层过滤的完整配置链，验证 RULEBINDING→RULE→PCCPOLICYGRP→PCCACTIONPROP→FLOWFILTER→PROTBINDFLOWF→L7FILTER→FLTBINDFLOWF→FILTER 全链路 |
| phase | verify |
| input_artifacts | ["UserProfile 名称", "七层过滤条件规划值"] |
| output_artifacts | ["七层配置链全链路查询结果"] |
| command | `LST RULEBINDING:USERPROFILENAME="up_policy";`<br>`LST RULE:RULENAME="ruleA",POLICYTYPE=PCC;`<br>`LST PCCPOLICYGRP:PCCPOLICYGRPNM="pccgrpA";`<br>`LST PCCACTIONPROP:PCCACTPROPNAME="pccactA";`<br>`LST FLOWFILTER:FLOWFILTERNAME="flowfilterA";`<br>`LST PROTBINDFLOWF:FLOWFILTERNAME="flowfilterA";`<br>`LST L7FILTER:L7FILTERNAME="l7filterA";`<br>`LST FLTBINDFLOWF:FLOWFILTERNAME="flowfilterA";`<br>`LST FILTER:FILTERNAME="filterA";`<br>`DSP SIGNATUREDB;` |
| config_object | `RULEBINDING`, `RULE`, `PCCPOLICYGRP`, `PCCACTIONPROP`, `FLOWFILTER`, `PROTBINDFLOWF`, `L7FILTER`, `FLTBINDFLOWF`, `FILTER`, `SIGNATUREDB` |
| source_evidence_ids | ["套餐3_94838086"] |
| status | active |

**说明**：与 T-VERIFY-004 相比增加了两个关键环节：(1) 通过 LST PROTBINDFLOWF 确认七层过滤条件（URL）已正确挂载；(2) 通过 DSP SIGNATUREDB 确认协议特征库已加载完成。此任务仅用于 DS-02（访问限制），在 T-VERIFY-004 之后执行。

#### T-VERIFY-006 验证带宽控制策略生效

| 字段 | 值 |
|------|-----|
| task_id | T-VERIFY-006 |
| task_name | 验证带宽控制策略生效 |
| task_summary | 通过 LST 查询 BWM 全链路配置，从 RULEBINDING→RULE→CATEGORYPROP→BWMSERVICE→BWMCONTROLLER→BWMUSERGROUP→BWMRULE 逐层回查，验证带宽控制策略完整且绑定关系正确 |
| phase | verify |
| input_artifacts | ["UserProfile 名称", "BWM 对象名称列表"] |
| output_artifacts | ["BWM 全链路回查结果"] |
| command | `LST RULEBINDING:USERPROFILENAME="up_bwmcontrol",POLICYTYPE=BWM;`<br>`LST RULE:RULENAME="ruleA";`<br>`LST CATEGORYPROP:CATEPROPNAME="catropA";`<br>`LST BWMSERVICE:BWMSERVICENAME="bwmservA";`<br>`LST BWMCONTROLLER:BWMCNAME="bwmcontrolA";`<br>`LST BWMUSERGROUP:QRYUSRGRPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpA";`<br>`LST BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpA",BWMRULETYPE=SUBSCRIBER_SPECIFIC,BWMRULENAME="bwmruleA";` |
| config_object | `USERPROFILE`, `RULEBINDING`, `RULE`, `CATEGORYPROP`, `BWMSERVICE`, `BWMCONTROLLER`, `BWMUSERGROUP`, `BWMRULE` |
| source_evidence_ids | ["套餐2_94838085"] |
| status | active |

**说明**：回查路径共八层对象。验证要点：(1) RULEBINDING 中 POLICYTYPE=BWM 的规则均已绑定；(2) RULE 的 POLICYNAME 指向的 CATEGORYPROP 存在；(3) BWMSERVICE 的 CATEPROPNAME 与 RULE 引用一致；(4) BWMCONTROLLER 的 CTRLTYPE 与速率参数符合规划；(5) BWMUSERGROUP 优先级正确；(6) BWMRULE 将 USERGROUP+SERVICE+CONTROLLER 正确关联。此任务仅用于 DS-03（带宽控制）。



## 12. 业务感知的 `Participant`

### 12.1 Schema 定义

**定位**：在某个 `DeliverySolution` 的形成、生效、更新、计费、验证过程中承担稳定职责的参与方。

**属性**：

| 字段 | 类型 | 必选 | 说明 |
|------|------|------|------|
| participant_id | string | 是 | 唯一标识 |
| participant_name | string | 是 | 参与方名称 |
| participant_type | string | 是 | 类型：`endpoint / network_function / external_system / service_endpoint / access_side` |
| responsibility_summary | string | 是 | 一句话说明其稳定职责 |
| plane_or_side | string | 否 | 所在侧：`control_plane / user_plane / external / terminal_side / service_side` |
| source_evidence_ids | list[string] | 是 | 证据来源 |
| status | string | 是 | 数据状态 |

**边**：

```text
DeliverySolution --involves--> Participant
```

### 12.2 实例

| participant_id | participant_name | participant_type | plane_or_side | responsibility_summary | status |
|------|------|------|------|------|------|
| P-01 | PCF | network_function | control_plane | 生成或选择策略，并向 SMF 下发策略控制信息 | active |
| P-02 | SMF | network_function | control_plane | 编排会话、翻译策略、协调控制面与用户面 | active |
| P-03 | UPF | network_function | user_plane | 识别业务流、执行策略、上报使用信息 | active |
| P-04 | CHF | external_system | external | 处理计费、配额、重授权触发 | active |
| P-05 | UE/用户 | endpoint | terminal_side | 发起会话与业务访问，产生待识别业务流 | active |
| P-06 | AMF | network_function | control_plane | 在分流和会话修改场景中承接接入侧信令协同 | active |
| P-07 | UL CL UPF | network_function | user_plane | 在本地分流场景中承接分流规则并执行上行分类转发 | active |
| P-08 | 主锚点UPF | network_function | user_plane | 承接中心 DN 业务和分流前常规 PDU 会话 | active |
| P-09 | 辅锚点UPF | network_function | user_plane | 承接本地 DN 业务和分流后本地业务转发 | active |
| P-10 | 中心DN/本地DN/业务服务器 | service_endpoint | service_side | 作为业务目的地接收业务流量 | active |

## 13. 业务感知的 `Scope`

### 13.1 Schema 定义

**定位**：描述某个 `DeliverySolution` 或某类策略对“谁、哪类接入、哪类位置、哪类会话条件”生效的边界对象。

**属性**：

| 字段 | 类型 | 必选 | 说明 |
|------|------|------|------|
| scope_id | string | 是 | 唯一标识 |
| scope_name | string | 是 | 范围名称 |
| scope_summary | string | 是 | 一句话说明该范围含义 |
| scope_type | string | 是 | 范围类别，如 `subscriber / subscription / access / location / slice / service-selection` |
| scope_expression | string | 否 | 原始表达或归一化表达 |
| source_evidence_ids | list[string] | 是 | 证据来源 |
| status | string | 是 | 数据状态 |

**边**：

```text
DeliverySolution --applies_to--> Scope
DecisionPoint --conditioned_by--> Scope
```

### 13.2 实例

| scope_id | scope_name | scope_type | scope_expression | scope_summary | status |
|------|------|------|------|------|------|
| S-01 | 用户级范围 | subscriber | 普通用户 / 特定用户 | 方案按用户粒度生效 | active |
| S-02 | APN/DNN范围 | access | APN1 / 指定DNN | 方案按接入点或数据网名称生效 | active |
| S-03 | 切片范围 | slice | 用户切片信息 | 方案按切片粒度生效 | active |
| S-04 | 位置/PRA范围 | location | 位置区 / PRA | 方案按位置或指定区域生效 | active |
| S-05 | DNAI/本地DN导向范围 | service-selection | DNAI / 本地DN | 方案按本地业务导向条件生效 | active |
| S-06 | UserProfile承载范围 | subscription | UserProfile1 | 用于承载规则绑定和最终生效边界 | active |

## 14. 业务感知的 `DecisionPoint`

### 14.1 Schema 定义

**定位**：在某个 `NetworkScenario` 或 `DeliverySolution` 中，会导致后续任务、动作路径或方案实现方式发生分支变化的稳定选择点。

**属性**：

| 字段 | 类型 | 必选 | 说明 |
|------|------|------|------|
| decision_id | string | 是 | 唯一标识 |
| decision_name | string | 是 | 决策点名称 |
| decision_question | string | 是 | 该决策实际在回答什么问题 |
| option_set | list[string] | 是 | 可选分支集合 |
| trigger_condition | string | 否 | 在什么条件下需要做该决策 |
| impact_summary | string | 是 | 不同分支会影响哪些后续任务或方案结构 |
| source_evidence_ids | list[string] | 是 | 证据来源 |
| status | string | 是 | 数据状态 |

**边**：

```text
NetworkScenario --has_decision--> DecisionPoint
DeliverySolution --has_decision--> DecisionPoint
DecisionPoint --conditioned_by--> Scope
```

### 14.2 实例

| decision_id | decision_name | 挂载层级 | decision_question | option_set | trigger_condition | status |
|------|------|------|------|------|------|------|
| DP-01 | 计费方式选择 | NetworkScenario(NS-01) | 当前计费场景采用哪种计费方式 | `["离线计费","在线计费","融合计费"]` | 进入计费场景时 | active |
| DP-02 | 配额耗尽后动作选择 | DeliverySolution(DS-01) | 用户配额耗尽后如何处理业务体验 | `["BLOCK","REDIRECT","FORWARD"]` | 在线计费配额耗尽 | active |
| DP-03 | 分流策略来源选择 | NetworkScenario(NS-04) | 分流策略最终由谁下发给 UL CL UPF | `["PCF下发","SMF下发","PCF经SMF下发","MPF下发"]` | 进入本地分流场景时 | active |
| DP-04 | 分流触发与 UPF 选择 | DeliverySolution(DS-04) | 何时触发分流，以及选择哪类 UPF | `["仅主锚点","插入UL CL","插入辅锚点","UL CL+辅锚点"]` | 满足 DNN/位置/PRA/DNAI/能力条件时 | active |
| DP-05 | 访问限制动作选择 | DeliverySolution(DS-02) | 命中目标业务流后采用哪种处理路径 | `["DISCARD","HEADEN","IPREDIR","REDIRECT"]` | 规则命中后 | active |

## 16. 业务感知的 `ValidationPlan`

### 16.1 Schema 定义

**定位**：针对某个 `DeliverySolution` 或某类关键业务目标的验收检查模板。

它回答“验什么”，不直接回答“怎么逐条执行检查”。

**属性**：

| 字段 | 类型 | 必选 | 说明 |
|------|------|------|------|
| validation_id | string | 是 | 唯一标识 |
| validation_name | string | 是 | 验收计划名称 |
| validation_goal | string | 是 | 验收目标 |
| target_objects | list[string] | 是 | 需要观察/检查的对象集合 |
| pass_condition | string | 是 | 通过条件 |
| expected_result | string | 是 | 预期现象或结果 |
| source_evidence_ids | list[string] | 是 | 证据来源 |
| status | string | 是 | 数据状态 |

**边**：

```text
DeliverySolution --validated_by--> ValidationPlan
ValidationPlan --executed_by--> EngineeringTask
  约束: EngineeringTask.phase = verify
ValidationPlan --uses_rule--> BusinessRule
```

### 16.2 实例

| validation_id | validation_name | 对应方案 | validation_goal | target_objects | pass_condition | expected_result | status |
|------|------|------|------|------|------|------|------|
| VP-01 | 差异化计费验收 | DS-01 | 确认计费链、URR 绑定与 PFCP 上报符合预期 | `["LICENSESWITCH","RULEBINDING","RULE","URR","PFCP Session Report"]` | License 开启、配置链正确、URR ID 与上报一致 | 业务流被正确识别并按预期计费/上报 | active |
| VP-02 | 访问限制验收 | DS-02 | 确认阻塞、头增强、重定向链路生效 | `["RULEBINDING","RULE","PCCPOLICYGRP","PCCACTIONPROP","HEADEN","L7FILTER","FILTER"]` | 配置链完整、动作参数正确、门控/导向符合预期 | 业务被阻塞、增强或重定向到指定目标 | active |
| VP-03 | 带宽控制验收 | DS-03 | 确认 BWM 策略链和速率参数生效 | `["RULEBINDING","RULE","CATEGORYPROP","BWMSERVICE","BWMCONTROLLER","BWMRULE"]` | 策略链完整、控制器参数符合规划、绑定关系正确 | 业务获得预期限速/保障/整形效果 | active |
| VP-04 | 本地分流与独立计费验收 | DS-04 | 确认分流触发、UPF 选择和独立计费链符合规划 | `["DNN/位置条件","UL CL/辅锚点选择结果","UPF配额行为"]` | 触发条件命中、分流路径符合规划、多 UPF 计费行为正确 | 业务被导向本地DN/中心DN，计费路径与 UPF 分工一致 | planned |

## 17. 业务感知的 `BusinessRule`

### 17.1 Schema 定义

**定位**：用于表达业务级核查、约束断言和异常定位逻辑的统一规则对象。

**属性**：

| 字段 | 类型 | 必选 | 说明 |
|------|------|------|------|
| rule_id | string | 是 | 唯一标识 |
| rule_name | string | 是 | 规则名称 |
| rule_type | string | 是 | `validation_rule / diagnosis_rule / constraint_rule` |
| rule_purpose | string | 是 | 规则用途 |
| trigger_condition | string | 否 | 何时触发该规则 |
| check_target | string | 是 | 检查对象或观察对象 |
| check_logic | string | 是 | 判断逻辑 |
| expected_result | string | 否 | 满足时的预期结果，适用于 validation_rule |
| violation_effect | string | 否 | 违反后的影响，适用于 constraint_rule |
| next_action | string | 否 | 下一步排查动作，适用于 diagnosis_rule |
| source_evidence_ids | list[string] | 是 | 证据来源 |
| status | string | 是 | 数据状态 |

**边**：

```text
ValidationPlan --uses_rule--> BusinessRule
DeliverySolution --governed_by--> BusinessRule
```

### 17.2 实例

| rule_id | rule_name | rule_type | 对应方案/计划 | check_target | check_logic | expected_result / violation_effect / next_action | status |
|------|------|------|------|------|------|------|------|
| BR-01 | SA基础License开启断言 | constraint_rule | DS-01 / VP-01 | LICENSESWITCH | SA-Basic 与相关内容计费能力开关必须为 ENABLE | violation_effect: 业务感知能力不可用 | active |
| BR-02 | 配置链逐层一致性校验 | validation_rule | VP-01 / VP-02 / VP-03 | RULEBINDING→RULE→对象链 | 各层对象名称、绑定关系、关键参数与规划值一致 | expected_result: 配置链完整且参数一致 | active |
| BR-03 | PFCP Usage Report一致性校验 | validation_rule | VP-01 | PFCP Session Report / URR ID | Usage Report 中 URR ID 应与业务规则绑定一致 | expected_result: 计费流量被正确识别和上报 | active |
| BR-04 | CP/UP URR一致性诊断 | diagnosis_rule | DS-01 | CP/UP URR 配置 | 如果计费结果异常，先比对两侧 URR 名称和关键属性是否一致 | next_action: 回查 CP/UP URR 配置与绑定链 | active |
| BR-05 | Trigger未上报排查规则 | diagnosis_rule | DS-01 / DS-04 | Trigger / 会话更新 | 若未触发预期计费或配额更新，检查 Trigger 上报和会话更新链路 | next_action: 检查 Trigger 条件、会话更新与 CHF 交互 | active |
| BR-06 | N40计费流量一致性校验 | diagnosis_rule | DS-01 | N40 / CHF 结果 | 若业务被放通但未形成预期计费结果，检查 N40 侧计费流量与实际流量是否一致 | next_action: 检查 CHF / N40 流量上报链 | active |
| BR-07 | UL CL仅支持融合计费约束 | constraint_rule | DS-04 | 分流模式与计费方式 | UL CL 方案与计费方式必须满足产品约束 | violation_effect: UL CL 分流功能无法正常使用 | active |
| BR-08 | default quota异常处理规则 | diagnosis_rule | DS-01 | default quota 行为 | 当默认配额路径异常时，先检查 default quota 参数与配额更新行为 | next_action: 回查 default quota 相关配置和更新链 | active |
- 静态规则、QoS Flow映射和策略更新链会影响体验控制闭环表现
- 资源和License控制项会影响业务感知能力可开通范围、会话规模和吞吐边界

这里同样需要强调适用边界。`重定向缺省行为约束` 主要属于 `NS-03` 的 HTTP 导向链，`QoS编排约束` 主要属于 `NS-02`，而 `多UPF配额约束`、`计费可靠性约束` 则主要作用于计费和分流计费旁支。下面统一显式标出适用场景。


## 20. 业务感知的 `DomainSemanticObject`

这里的 `DomainSemanticObject` 对应中文对象名是 `领域语义对象`。

业务感知域中的语义对象不是“识别+计费+导向”的简单累加，而是进一步收敛为 16 个关键语义对象。

其中最需要注意的是：`BA.TrafficRecognition` 被去掉了。

原因不是识别不重要，而是它在原始语料里已经被拆开成更稳定的三个层次：

1. `报文解析`
2. `协议/应用识别`
3. `识别知识底座`

如果继续保留一个总括性的 `BA.TrafficRecognition`，反而会和 `PacketParsing / ProtocolRecognition / 协议库` 这组对象重叠。

本文保留的关键语义对象为：

- `BA.PacketParsing`
- `BA.ProtocolRecognition`
- `BA.FilterCondition`
- `BA.ProtocolFeatureLibrary`
- `BA.ProtocolParserLibrary`
- `BA.Rule`
- `BA.Policy`
- `BA.Priority`
- `BA.Binding`
- `BA.Charging`
- `BA.Quota`
- `BA.ChargingTrigger`
- `BA.Runtime`
- `BA.ValidationDiagnosis`
- `BA.LocalBreakout`
- `BA.QoSOrchestration`

这些对象的作用不是替代场景，而是把场景和下层实现连接起来。

### 20.1 `DomainSemanticObject` 实例表

| 语义对象 | 定义 | 在业务感知中的业务含义 | 典型落点 |
| --- | --- | --- | --- |
| `BA.PacketParsing` | 如何把原始报文拆解成可读字段 | 表达三四层解析、七层解析和字段提取的过程 | 三四层解析、七层解析、字段内容提取 |
| `BA.ProtocolRecognition` | 如何从报文和连接行为中识别协议/应用 | 表达知名端口、特征字、关联识别、行为识别等识别方式 | 协议识别引擎、端口识别、特征字识别、关联识别、行为识别 |
| `BA.FilterCondition` | 如何把已解析的报文特征组织成可匹配条件 | 表达 3/4 层过滤、7 层过滤、协议过滤以及它们组合成 Flow Filter 的方式 | Filter、FilterGroup、L7Filter、Protocol、ProtocolGroup、FlowFilter、FlowFilterGroup |
| `BA.ProtocolFeatureLibrary` | 协议特征如何被组织和更新 | 表达新业务识别能力来自特征库而非总是来自软件升级 | 协议特征库、规则库更新 |
| `BA.ProtocolParserLibrary` | 协议解析能力的固定基础集合 | 表达广泛协议的基础解析能力是业务识别的前置底座 | 协议解析库、基础协议解析能力 |
| `BA.Rule` | 业务感知的最小组织单元 | 把过滤条件、策略、优先级以及其他参数组织成一个可下发、可匹配、可执行的单元 | Rule、预定义规则、动态规则、本地规则 |
| `BA.Policy` | 规则命中后要执行的策略类型与目标 | 表达 PCC、BWM、HEADEN、IPREDIR、WEBPROXY、SMARTREDIRECT 以及 Portal 处理路径等不同策略目标 | PCC策略组、BWM分类策略、头增强策略、IP重定向、WebProxy、智能重定向、Portal 动作 |
| `BA.Priority` | 多规则同时命中时如何裁决 | 解决专项业务和默认业务冲突 | Rule Priority |
| `BA.Binding` | 规则和范围对象如何绑定 | 表达业务套餐、生效对象、默认策略承载方式 | UserProfile、RuleBinding、默认URR组绑定 |
| `BA.Charging` | 如何按业务收费 | 表达差异化计费、免费业务、默认计费 | URR、URRGroup、RG、PCCPolicyGrp |
| `BA.Quota` | 如何处理配额 | 表达在线配额、额度耗尽、后续动作 | QuotaExhaustAct、CHF交互、RG |
| `BA.ChargingTrigger` | 什么事件会驱动计费会话更新、重授权或释放 | 表达 Session级/RG级 Trigger、立即/延迟上报以及会话创建/更新/释放条件 | PDUTRIGGER、RGTRIGGER、Trigger优先级、Charging Data Request |
| `BA.Runtime` | 场景如何动态生效 | 表达策略建立、更新、释放和 Trigger 驱动切换 | PDR/FAR/Usage/Trigger |
| `BA.ValidationDiagnosis` | 如何验证和回查 | 表达生效校验、一致性核查和异常定位 | CP/UP一致性、运行现象、上报链路 |
| `BA.LocalBreakout` | 如何把本地业务流从中心路径导向本地DN/边缘DN | 表达基于 DNN、位置、PRA、DNAI、selectedDnn 或外部触发建立 UL CL 分流路径的能力 | UL CL UPF、辅锚点UPF、本地DN导向、边缘卸载 |
| `BA.QoSOrchestration` | 如何把业务意图翻译成 QoS Flow、PFS/QFI 映射和端到端体验保障 | 表达静态/动态规则、SM策略生成、QoS Flow建立、RAN映射和PCF/SMF发起更新这条控制面-用户面编排链 | QFI、PFS、QER、QoS Flow、Radio Bearer 映射、QoS策略更新 |

### 20.2 为什么必须有语义对象

如果没有这一层，图谱会变成：

- 场景名
- 特性名
- 命令名

三堆名词之间直接相连。

而加入语义对象后，才能表达：

```text
业务问题
-> 解析语义/识别语义/过滤条件语义/计费语义/配额语义
-> 正式特性
-> 配置对象链
```

这才是“图谱”，而不是“目录汇总”。

这一层至少已经能稳定表达出下面这条桥接链：

```text
业务问题
-> 报文解析
-> 协议/应用识别
-> 过滤条件组织
-> 规则匹配与策略执行
-> 计费/配额/转发结果
-> 正式特性
-> 配置对象链
```

## 21. 业务感知的 `Feature`

这里的 `Feature` 对应中文对象名是 `特性`。

业务感知不是挂在某一个孤立特性目录下就能成立的能力。对 UDG/UPF 一侧，它始终与 `业务感知功能 / 智能策略控制功能 / 计费功能 / QoS功能 / 分布式网络功能` 并列存在并组合生效；对 UNC/SMF 一侧，它则依托 `PCC / 计费管理 / 分流策略控制` 等控制面能力完成规则编排、计费会话和会话导向。因此，下面这些特性在图谱中不是“平铺目录”，而是这套产品能力版图中的关键锚点。

### UDG/UPF 侧

- `GWFD-110101 SA-Basic`
- `GWFD-020351 PCC基本功能`
- `GWFD-110311 基于业务感知的带宽控制`
- `GWFD-110281 用户Portal`

### UNC/SMF 侧

- `WSFD-109101 PCC基本功能`
- `WSFD-109002 内容计费基本功能`
- `WSFD-011206 支持融合计费`
- `WSFD-108002 基于预定义规则的分流策略控制`
- `WSFD-223001 基于位置信息的分流策略控制`
- `WSFD-223003 基于漫游地动态签约的分流策略控制`
- `WSFD-223004 基于动态规则的分流策略控制`
- `WSFD-228003 公网私网业务独立计费`

### 21.1 `Feature` 实例表

| 特性 | 所属侧别 | 正式能力定位 | 在业务图谱中的作用 |
| --- | --- | --- | --- |
| `GWFD-110101 SA-Basic` | UDG/UPF | 识别底座 | 支撑业务感知域成立，使业务流可被识别 |
| `GWFD-020351 PCC基本功能` | UDG/UPF | 用户面策略执行骨架 | 支撑用户面执行计费、重定向、带宽控制等动作 |
| `GWFD-110311 基于业务感知的带宽控制` | UDG/UPF | 带宽与QoS执行能力 | 把带宽与体验分层稳定为独立业务场景，并承接用户面速率和体验动作 |
| `GWFD-110281 用户Portal` | UDG/UPF | 门户导向正式能力 | 把业务导向从“单次重定向”扩展为带 captive/non-captive 模式切换的门户导向能力 |
| `WSFD-109101 PCC基本功能` | UNC/SMF | 控制面规则、SM策略与QoS框架 | 承接 AM/UE/SM 策略，组织规则供给方式、QoS Flow相关策略和 PCC 规则框架 |
| `WSFD-109002 内容计费基本功能` | UNC/SMF | 基于业务粒度的计费编排能力 | 把业务条件映射成控制面可编排的计费规则和费率结构 |
| `WSFD-011206 支持融合计费` | UNC/SMF | 在线/离线统一计费与配额闭环能力 | 让配额控制、计费上报、规则更新与业务动作切换形成完整控制环 |
| `WSFD-108002 基于预定义规则的分流策略控制` | UNC/SMF | 本地分流基础能力 | 让业务感知的导向能力扩展到 `UL CL -> 本地DN/Internet` 的双路径分流 |
| `WSFD-223001 基于位置信息的分流策略控制` | UNC/AMF/SMF | 精细位置触发分流能力 | 把本地分流从 TAC 粒度推进到 PRA/小区粒度 |
| `WSFD-223003 基于漫游地动态签约的分流策略控制` | UNC/AMF/SMF | 漫游地即时签约分流能力 | 让本地专网业务可以在拜访地即时开通并触发分流 |
| `WSFD-223004 基于动态规则的分流策略控制` | UNC/SMF | 外部应用驱动分流能力 | 让 AF/NEF 可以把分流触发和 DNAI 信息带入网络侧 |
| `WSFD-228003 公网私网业务独立计费` | UNC/SMF | 分流场景下的差异计费能力 | 让本地专网业务与 Internet 业务在分流场景中保持独立计费 |

### 21.2 `Feature` 字段业务含义

| 字段 | 含义 | 为什么重要 |
| --- | --- | --- |
| `所属侧别` | 特性主要承载在哪一侧 | 决定它属于控制面能力还是用户面能力 |
| `正式能力定位` | 该特性到底在产品能力体系中扮演什么角色 | 避免把所有特性当成同一层东西 |
| `在业务图谱中的作用` | 它为什么要被纳入图谱 | 让特性不是简单列名，而是解释其图谱价值 |

## 22. 业务感知的 `ConfigObject`

这里的 `ConfigObject` 对应中文对象名是 `配置对象`。

业务图谱层面不展开所有命令，但必须说明关键对象链。

在计费方案里，`Rule` 不是唯一的控制面骨架，`Trigger` 与 `URR/URRGroup` 一起决定了计费会话何时创建、更新和释放。

### UDG/UPF 侧关键对象

- `Filter`
- `L7Filter`
- `FlowFilter`
- `Rule`
- `PCCActionProp / Redirect / HEADEN / IPFarm`

### UNC/SMF 侧关键对象链

```text
URR
-> URRGroup
-> PCCPolicyGrp
-> Rule
-> UserProfile
-> RuleBinding
-> Default URRGroup Binding
```

### 22.1 `ConfigObject` 实例表

| 对象链位置 | 关键对象 | 所属侧别 | 业务作用 |
| --- | --- | --- | --- |
| 识别层 | `Filter` | UDG/UPF | 表达三四层过滤条件 |
| 识别层 | `L7Filter` | UDG/UPF | 表达七层 URL/Host/Method 等匹配条件 |
| 识别组合层 | `FlowFilter` / `FlowFilterGroup` | UDG/UPF | 把多种识别条件组合成最终匹配入口 |
| 规则层 | `Rule` | UDG/UPF + UNC/SMF | 把条件、动作、优先级绑定成可执行规则 |
| 动作层 | `PCCActionProp` / `Redirect` / `HEADEN` / `IPFarm` | UDG/UPF | 承载阻断、URL导向、头增强、Portal目标池等具体动作 |
| 分流触发层 | `App ID` / `selectedDnn` / `PRA绑定` / `DNAI` | UNC/SMF + AMF/PCF | 表达本地分流何时被触发、导向到哪个本地接入点 |
| 分流执行层 | `PDR` | UNC/SMF + UDG/UPF | 承载 UL CL 分流规则以及主锚点/辅锚点的转发路径控制 |
| QoS编排层 | `QER` / `PFS` / `QFI` | UNC/SMF + UDG/UPF + RAN/UE | 表达业务流如何映射到 QoS Flow，以及端到端体验控制如何被识别和实施 |
| 融合计费模板层 | `CCT` / `CHFINIT` / `CTXSTARTRATING` | UNC/SMF | 表达初始RG个数、RG来源以及激活时优先申请哪些RG配额 |
| 计费方式控制层 | `CHARGECTRL` / `USRPROFCHARGE` / `APNCHARGECTRL` / `CHARGEMETHOD` | UNC/SMF | 表达用户是否启用融合计费、按User Profile/DNN/CC的哪种方式计费，以及RG按在线/离线如何生效 |
| 计费Trigger层 | `PDUTRIGGER` / `RGTRIGGER` / `CNVRGDCHGPARA` | UNC/SMF | 表达会话级、费率组级 Trigger 以及本地对 CHF Trigger 的覆盖策略 |
| 缺省配额控制层 | `UPAPNCHARGE` / `UPDEFAULTQUOTA` / `SRVCOMMONPARA` | UDG/UPF + UNC/SMF | 表达在线计费场景在正式配额返回前是否允许使用 default quota，以及默认流量/时长是多少 |
| 计费对象层 | `URR` | UNC/SMF + UDG/UPF | 表达使用量统计与计费标识 |
| 计费组合层 | `URRGroup` | UNC/SMF + UDG/UPF | 把计费对象组合成上下行或在线/离线计费组 |
| 策略组层 | `PCCPolicyGrp` | UNC/SMF + UDG/UPF | 把 URRGroup 绑定成可被 Rule 调用的策略对象 |
| 特殊流量计费层 | `SPECTRAFURRGRP` / `URRFAILACTION` | UDG/UPF | 表达欠费/特殊流量是否继续统计、丢弃还是继续放通 |
| 绑定层 | `UserProfile` | UNC/SMF + UDG/UPF | 承载一组规则和默认策略，形成业务模板 |
| 绑定层 | `RuleBinding` | UNC/SMF + UDG/UPF | 把具体 Rule 绑定到 UserProfile |
| 默认计费层 | `Default URRGroup Binding` | UNC/SMF + UDG/UPF | 为未命中特殊业务的流量提供默认计费去向 |

### 22.2 `ConfigObject` 字段业务含义

| 字段 | 含义 | 为什么重要 |
| --- | --- | --- |
| `对象链位置` | 该对象位于哪一层 | 帮助理解它在全链路中的职责，而不是只看名字 |
| `所属侧别` | 主要在哪一侧存在或要求一致 | 决定它是控制面编排对象、用户面执行对象，还是两侧一致性对象 |
| `业务作用` | 它对业务目标的贡献 | 把配置对象重新翻译回业务语言 |

## 23. 业务感知业务图谱的实例关系表

### 23.1 业务层关系

| 起点对象 | 终点对象 | 关系标识 | 中文关系名 | 业务解释 |
| --- | --- | --- | --- | --- |
| `业务感知` | `计费场景` | `contains` | 包含 | 业务感知域中存在按业务粒度组织差异化计费、免费业务、默认计费和配额动作的稳定问题空间 |
| `业务感知` | `带宽控制场景` | `contains` | 包含 | 业务感知域中存在基于业务识别实施带宽控制并进一步落实到 QoS 编排的稳定问题空间 |
| `业务感知` | `访问限制场景` | `contains` | 包含 | 业务感知域中存在基于识别条件实施阻断、重定向和头增强的稳定问题空间 |
| `业务感知` | `本地分流场景` | `contains` | 包含 | 业务感知域中存在把业务流导向本地DN/边缘DN并在需要时结合独立计费的稳定问题空间 |
| `计费场景` | `差异化计费组合方案（含配额分支）` | `instantiated_as` | 实例化为 | `业务感知场景举例` 和 `套餐1：计费场景` 共同表明，计费场景会收敛为“差异化计费 + 免费业务 + 默认计费 + 配额动作”的方案闭包 |
| `访问限制场景` | `访问限制组合方案` | `instantiated_as` | 实例化为 | `套餐3：访问限制场景` 直接给出了阻塞、头增强、IP重定向、URL重定向并存的一套访问限制方案结构 |
| `带宽控制场景` | `带宽控制与QoS编排方案` | `instantiated_as` | 实例化为 | `套餐2：带宽控制` 直接给出了基于业务识别的 BWM 对象链；QoS 编排部分来自同一场景的控制面补充材料 |
| `本地分流场景` | `本地分流与独立计费方案` | `instantiated_as` | 实例化为 | `How分流` 与 `MEC计费流程` 共同表明，本地分流场景会收敛为“分流触发 + UPF插入 + 会话修改 + 独立计费”的方案闭包 |
| `计费场景` | `本地分流与独立计费方案` | `instantiated_as` | 实例化为 | 当分流场景要求公网/专网会话分别计费时，该方案同时承担计费场景的交叉落地 |

### 23.2 方案到任务关系

| 起点对象 | 终点对象 | 关系标识 | 中文关系名 | 业务解释 |
| --- | --- | --- | --- | --- |
| `差异化计费组合方案（含配额分支）` | `规划生效范围` | `uses_task` | 使用任务 | 对应 `场景举例` 中“普通用户 + APN1 + User Profile1”的生效边界规划。 |
| `差异化计费组合方案（含配额分支）` | `规划识别条件` | `uses_task` | 使用任务 | 对应 `场景举例` 中 FlowFilter1/2 区分 A 网站视频与非 A 网站视频。 |
| `差异化计费组合方案（含配额分支）` | `规划Rule与优先级` | `uses_task` | 使用任务 | 对应 `场景举例` 中 Rule1 > Rule2 > Rule3 的稳定裁决顺序。 |
| `差异化计费组合方案（含配额分支）` | `规划计费对象与费率标识` | `uses_task` | 使用任务 | 对应套餐1中 URR/URRGROUP/PCCPOLICYGRP 的计费对象链与费率承载。 |
| `差异化计费组合方案（含配额分支）` | `规划配额耗尽动作` | `uses_task` | 使用任务 | 对应 `场景举例` 中流量耗尽后停用 Rule2、启用 Rule3 并重定向到充值页面。 |
| `差异化计费组合方案（含配额分支）` | `配置计费动作链` | `uses_task` | 使用任务 | 对应套餐1脚本中的 URR → URRGROUP → PCCPOLICYGRP 配置链。 |
| `差异化计费组合方案（含配额分支）` | `验证 PFCP 会话上报与计费流量` | `uses_task` | 使用任务 | 对应调测内容计费中 Usage Report 与 URR ID 的最终验收动作。 |
| `访问限制组合方案` | `规划生效范围` | `uses_task` | 使用任务 | 对应套餐3中访问限制业务最终挂载到 `up_policy` 的范围规划。 |
| `访问限制组合方案` | `规划识别条件` | `uses_task` | 使用任务 | 对应套餐3中三四层/七层过滤条件与目标业务识别条件规划。 |
| `访问限制组合方案` | `规划Rule与优先级` | `uses_task` | 使用任务 | 对应套餐3中不同限制动作下 RULE 的组织方式与匹配顺序。 |
| `访问限制组合方案` | `规划导向与增强动作` | `uses_task` | 使用任务 | 对应套餐3中 BLOCK、HEADEN、IPREDIR、URL 重定向四类动作选择。 |
| `访问限制组合方案` | `配置策略动作链` | `uses_task` | 使用任务 | 对应套餐3脚本中的 RULE → PCCPOLICYGRP → PCCACTIONPROP/HEADEN/IPFarm 等动作链。 |
| `访问限制组合方案` | `验证三四层阻塞生效` | `uses_task` | 使用任务 | 对应调测文档中 DISCARD 门控动作的逐层回查。 |
| `访问限制组合方案` | `验证七层配置链` | `uses_task` | 使用任务 | 对应调测文档中 RULEBINDING 到 L7FILTER/FILTER 的完整对象链验证。 |
| `带宽控制与QoS编排方案` | `规划生效范围` | `uses_task` | 使用任务 | 对应套餐2中带宽控制业务最终挂载到 `up_bwmcontrol` 的范围规划。 |
| `带宽控制与QoS编排方案` | `规划识别条件` | `uses_task` | 使用任务 | 对应套餐2中业务流分类与限速对象的识别条件规划。 |
| `带宽控制与QoS编排方案` | `规划Rule与优先级` | `uses_task` | 使用任务 | 对应套餐2中带宽控制规则的组织与优先级规划。 |
| `带宽控制与QoS编排方案` | `规划BWM策略` | `uses_task` | 使用任务 | 对应套餐2中 CATEGORYPROP、BWMSERVICE、BWMCONTROLLER、BWMUSERGROUP、BWMRULE 的策略规划。 |
| `带宽控制与QoS编排方案` | `配置BWM带宽控制链` | `uses_task` | 使用任务 | 对应套餐2脚本中的 BWM 全链路配置。 |
| `带宽控制与QoS编排方案` | `验证带宽控制策略生效` | `uses_task` | 使用任务 | 对应套餐2调测中的 RULEBINDING → BWMRULE 全链路回查。 |
| `本地分流与独立计费方案` | `规划生效范围` | `uses_task` | 使用任务 | 对应 `How分流` 中 DNN、位置区/PRA、DNAI 等边界条件规划。 |
| `本地分流与独立计费方案` | `规划分流触发与锚点插入` | `uses_task` | 使用任务 | 对应 `How分流` 中 UL CL UPF、主锚点 UPF、辅锚点 UPF 的触发与插入决策。 |
| `本地分流与独立计费方案` | `规划计费Trigger与多UPF配额` | `uses_task` | 使用任务 | 对应独立计费下主/辅锚点分别计费、Trigger 驱动更新与多 UPF 配额边界规划。 |

### 23.3 方案到支撑对象关系

| 起点对象 | 终点对象 | 关系标识 | 中文关系名 | 业务解释 |
| --- | --- | --- | --- | --- |
| `差异化计费组合方案（含配额分支）` | `用户级范围` | `applies_to` | 作用于 | `业务感知场景举例` 直接以“普通用户”作为业务对象。 |
| `差异化计费组合方案（含配额分支）` | `APN-DNN范围` | `applies_to` | 作用于 | `业务感知场景举例` 直接出现 APN1 作为策略绑定边界。 |
| `差异化计费组合方案（含配额分支）` | `UserProfile承载范围` | `applies_to` | 作用于 | `业务感知场景举例` 中 Rule1/2/3 最终统一绑定在 User Profile1 下。 |
| `访问限制组合方案` | `UserProfile承载范围` | `applies_to` | 作用于 | `套餐3` 最终通过 `up_policy` 承载全部访问限制规则。 |
| `带宽控制与QoS编排方案` | `UserProfile承载范围` | `applies_to` | 作用于 | `套餐2` 最终通过 `up_bwmcontrol` 承载全部带宽控制规则。 |
| `本地分流与独立计费方案` | `APN-DNN范围` | `applies_to` | 作用于 | `How分流` 将 DNN 作为触发分流和选择主锚点/辅锚点的核心条件之一。 |
| `本地分流与独立计费方案` | `位置-PRA范围` | `applies_to` | 作用于 | `How分流` 将用户位置区信息作为触发分流和 UPF 选择的主要决策条件。 |
| `本地分流与独立计费方案` | `DNAI-本地DN导向范围` | `applies_to` | 作用于 | `How分流` 将 DNAI 作为辅锚点 UPF 选择和本地 DN 导向条件。 |
| `计费场景` | `计费方式选择` | `has_decision` | 包含决策点 | `计费解决方案概述` 直接列出离线计费、在线计费、融合计费三种方式 |
| `差异化计费组合方案（含配额分支）` | `配额耗尽后动作选择` | `has_decision` | 包含决策点 | `业务感知场景举例` 明确给出流量耗尽后停用 Rule2、启用 Rule3 并重定向到充值页面的分支变化 |
| `访问限制组合方案` | `访问限制动作选择` | `has_decision` | 包含决策点 | `套餐3` 明确同时存在 PCC阻塞、HEADEN、IPREDIR、URL重定向四种动作路径 |
| `本地分流场景` | `分流策略来源选择` | `has_decision` | 包含决策点 | `How分流` 明确给出 PCF下发、SMF下发、PCF经SMF下发、MPF下发四种策略来源 |
| `本地分流与独立计费方案` | `分流触发与UPF选择` | `has_decision` | 包含决策点 | `How分流` 明确给出 DNN+位置触发分流，以及 UL CL UPF / 辅锚点UPF 的选择条件 |
| `差异化计费组合方案（含配额分支）` | `PCF` | `involves` | 涉及 | `业务感知场景举例` 中 PCF 负责根据用户/APN信息下发 Rule1、Rule2，并在配额耗尽后下发 Rule3。 |
| `差异化计费组合方案（含配额分支）` | `SMF` | `involves` | 涉及 | `业务感知场景举例` 中 SMF 负责向 PCF 发起会话策略请求、向 UPF 传递规则并接收 CHF 通知。 |
| `差异化计费组合方案（含配额分支）` | `UPF` | `involves` | 涉及 | `业务感知场景举例` 中 UPF 负责规则匹配、执行计费/重定向动作并上报用量。 |
| `差异化计费组合方案（含配额分支）` | `CHF` | `involves` | 涉及 | `业务感知场景举例` 中 CHF 接收用量、判定流量耗尽并通知 SMF 更新会话。 |
| `差异化计费组合方案（含配额分支）` | `UE/用户` | `involves` | 涉及 | `业务感知场景举例` 以普通用户的视频业务会话作为触发主体。 |
| `本地分流与独立计费方案` | `PCF` | `involves` | 涉及 | `How分流` 中 PCF 可以作为分流策略来源，并在建立 SM 策略时参与策略下发。 |
| `本地分流与独立计费方案` | `AMF` | `involves` | 涉及 | `How分流` 中会话修改阶段需经 AMF 完成 N1N2MessageTransfer 与基站交互。 |
| `本地分流与独立计费方案` | `SMF` | `involves` | 涉及 | `How分流` 中 SMF 负责 UPF 选择、PFCP 会话建立和整条分流会话更新。 |
| `本地分流与独立计费方案` | `UL CL UPF` | `involves` | 涉及 | `How分流` 中 UL CL UPF 是触发分流后插入的核心转发节点。 |
| `本地分流与独立计费方案` | `主锚点UPF` | `involves` | 涉及 | `How分流` 中主锚点 UPF 在常规会话阶段即被选择并在分流后继续承担中心 DN 业务。 |
| `本地分流与独立计费方案` | `辅锚点UPF` | `involves` | 涉及 | `How分流` 中辅锚点 UPF 在触发分流后承担本地 DN 业务。 |
| `本地分流与独立计费方案` | `中心DN-本地DN-业务服务器` | `involves` | 涉及 | `How分流` 中最终业务流分别到达中心 DN 或本地 DN。 |
| `本地分流与独立计费方案` | `UE/用户` | `involves` | 涉及 | `How分流` 全流程以 UE 发起 PDU 会话并在移动过程中触发分流为前提。 |
| `差异化计费组合方案（含配额分支）` | `差异化计费验收` | `validated_by` | 由其验收 | 通过 License、配置链和 PFCP 上报核查计费闭环；对应计费调测材料和 verify Task |
| `访问限制组合方案` | `访问限制验收` | `validated_by` | 由其验收 | 通过规则链、动作链和用户面现象核查访问限制是否生效；对应 UDG 调测材料和 verify Task |
| `带宽控制与QoS编排方案` | `带宽控制验收` | `validated_by` | 由其验收 | 通过 BWM 链路和速率结果核查带宽控制是否生效；对应套餐2回查步骤和 verify Task |
| `本地分流与独立计费方案` | `本地分流与独立计费验收` | `validated_by` | 由其验收 | 通过分流触发条件、UPF 选择结果和多 UPF 计费行为核查本地分流是否按规划成立 |
| `差异化计费组合方案（含配额分支）` | `SA基础License开启断言` | `governed_by` | 受规则治理 | 计费方案首先受 SA-Basic 与内容计费相关 License 开关约束。 |
| `差异化计费组合方案（含配额分支）` | `配置链逐层一致性校验` | `governed_by` | 受规则治理 | 计费方案需要保证 RULEBINDING → RULE → URR/PCC 策略链逐层一致。 |
| `差异化计费组合方案（含配额分支）` | `PFCP Usage Report一致性校验` | `governed_by` | 受规则治理 | 计费方案需要保证 PFCP Session Report 中的 URR ID 与规划绑定一致。 |
| `差异化计费组合方案（含配额分支）` | `CP-UP URR一致性诊断` | `governed_by` | 受规则治理 | 当计费异常时，需要优先比对 CP/UP 两侧 URR 名称和关键属性。 |
| `差异化计费组合方案（含配额分支）` | `default quota异常处理规则` | `governed_by` | 受规则治理 | 当默认配额路径异常时，需要按 default quota 相关规则回查参数和更新链。 |
| `访问限制组合方案` | `配置链逐层一致性校验` | `governed_by` | 受规则治理 | 访问限制方案的验收核心依赖规则链、动作链与过滤链的一致性校验 |
| `带宽控制与QoS编排方案` | `配置链逐层一致性校验` | `governed_by` | 受规则治理 | 带宽控制方案的验收核心依赖 RULE 到 BWM 对象链的逐层一致性校验 |
| `本地分流与独立计费方案` | `UL CL仅支持融合计费约束` | `governed_by` | 受规则治理 | 分流独立计费方案受 UL CL 仅支持融合计费这一硬约束治理。 |
| `本地分流与独立计费方案` | `Trigger未上报排查规则` | `governed_by` | 受规则治理 | 分流独立计费方案受 Trigger 上报与会话更新链路规则治理。 |

### 23.4 支撑层内部关系

| 起点对象 | 终点对象 | 关系标识 | 中文关系名 | 业务解释 |
| --- | --- | --- | --- | --- |
| `分流触发与UPF选择` | `APN-DNN范围` | `conditioned_by` | 受范围条件约束 | `How分流` 将 DNN 作为分流触发与锚点选择的主要条件之一。 |
| `分流触发与UPF选择` | `位置-PRA范围` | `conditioned_by` | 受范围条件约束 | `How分流` 将位置区信息作为触发分流和选择 UL CL/辅锚点 UPF 的关键条件。 |
| `分流触发与UPF选择` | `DNAI-本地DN导向范围` | `conditioned_by` | 受范围条件约束 | `How分流` 将 DNAI 作为辅锚点 UPF 与本地 DN 导向的关键条件。 |
| `差异化计费验收` | `验证 License 开关` | `executed_by` | 由其执行 | 差异化计费验收先通过 License 开关检查确认能力已启用。 |
| `差异化计费验收` | `验证配置链逐层回查` | `executed_by` | 由其执行 | 差异化计费验收通过 RULEBINDING → RULE → URR 等配置链逐层回查落地。 |
| `差异化计费验收` | `验证 PFCP 会话上报与计费流量` | `executed_by` | 由其执行 | 差异化计费验收最终通过 PFCP Session Report 与 URR ID 一致性确认。 |
| `访问限制验收` | `验证三四层阻塞生效` | `executed_by` | 由其执行 | 访问限制验收通过 DISCARD 门控动作和过滤链回查验证三四层阻塞是否成立。 |
| `访问限制验收` | `验证七层配置链` | `executed_by` | 由其执行 | 访问限制验收通过 RULEBINDING 到 L7FILTER/FILTER 的全链路回查验证七层限制。 |
| `带宽控制验收` | `验证带宽控制策略生效` | `executed_by` | 由其执行 | 带宽控制验收通过 BWM 全链路回查落地 |
| `差异化计费验收` | `SA基础License开启断言` | `uses_rule` | 使用规则 | 差异化计费验收使用 License 断言判断基础能力是否满足。 |
| `差异化计费验收` | `配置链逐层一致性校验` | `uses_rule` | 使用规则 | 差异化计费验收使用配置链一致性规则核查控制面对象链。 |
| `差异化计费验收` | `PFCP Usage Report一致性校验` | `uses_rule` | 使用规则 | 差异化计费验收使用 PFCP Usage Report 规则核查运行时用量上报。 |
| `访问限制验收` | `配置链逐层一致性校验` | `uses_rule` | 使用规则 | 访问限制验收核心依赖规则链和动作链的一致性校验 |
| `带宽控制验收` | `配置链逐层一致性校验` | `uses_rule` | 使用规则 | 带宽控制验收核心依赖 RULE 到 BWM 对象链的一致性校验 |
| `本地分流与独立计费验收` | `UL CL仅支持融合计费约束` | `uses_rule` | 使用规则 | 分流独立计费验收需要先满足 UL CL 与融合计费的能力边界。 |
| `本地分流与独立计费验收` | `Trigger未上报排查规则` | `uses_rule` | 使用规则 | 分流独立计费验收需要参考 Trigger 上报与会话更新链的排查规则。 |

## 24. 业务感知业务图谱的完整主图

```text
BusinessDomain
└─ 业务感知
   ├─ NetworkScenario
   │  ├─ 计费场景
   │  ├─ 带宽控制场景
   │  ├─ 访问限制场景
   │  └─ 本地分流场景
   │
   ├─ DeliverySolution
   │  ├─ 差异化计费组合方案（含配额分支）
   │  ├─ 访问限制组合方案
   │  ├─ 带宽控制与QoS编排方案
   │  └─ 本地分流与独立计费方案
   │
   ├─ EngineeringTask
   │  ├─ 规划生效范围
   │  ├─ 规划识别条件
   │  ├─ 规划Rule与优先级
   │  ├─ 规划计费对象与费率标识
   │  ├─ 规划配额耗尽动作
   │  ├─ 规划导向与增强动作
   │  ├─ 规划BWM策略
   │  ├─ 规划分流触发与锚点插入
   │  ├─ 规划计费Trigger与多UPF配额
   │  ├─ 配置计费动作链
   │  ├─ 配置策略动作链
   │  ├─ 配置BWM带宽控制链
   │  ├─ 验证PFCP会话上报与计费流量
   │  ├─ 验证三四层阻塞生效
   │  ├─ 验证七层配置链
   │  └─ 验证带宽控制策略生效
   │
   ├─ Participant
   │  ├─ PCF
   │  ├─ SMF
   │  ├─ UPF
   │  ├─ CHF
   │  ├─ UE/用户
   │  ├─ AMF
   │  ├─ UL CL UPF
   │  ├─ 主锚点UPF
   │  ├─ 辅锚点UPF
   │  └─ 中心DN/本地DN/业务服务器
   │
   ├─ Scope
   │  ├─ 用户级范围
   │  ├─ APN/DNN范围
   │  ├─ 切片范围
   │  ├─ 位置/PRA范围
   │  ├─ DNAI/本地DN导向范围
   │  └─ UserProfile承载范围
   │
   ├─ DecisionPoint
   │  ├─ 计费方式选择
   │  ├─ 配额耗尽后动作选择
   │  ├─ 分流策略来源选择
   │  ├─ 分流触发与UPF选择
   │  └─ 访问限制动作选择
   │
   ├─ ValidationPlan
   │  ├─ 差异化计费验收
   │  ├─ 访问限制验收
   │  ├─ 带宽控制验收
   │  └─ 本地分流与独立计费验收
   │
   ├─ BusinessRule
   │  ├─ SA基础License开启断言
   │  ├─ 配置链逐层一致性校验
   │  ├─ PFCP Usage Report一致性校验
   │  ├─ CP/UP URR一致性诊断
   │  ├─ Trigger未上报排查规则
   │  ├─ N40计费流量一致性校验
   │  ├─ UL CL仅支持融合计费约束
   │  └─ default quota异常处理规则
   │
   ├─ DomainSemanticObject
   │  ├─ PacketParsing
   │  ├─ ProtocolRecognition
   │  ├─ FilterCondition
   │  ├─ ProtocolFeatureLibrary
   │  ├─ ProtocolParserLibrary
   │  ├─ Rule
   │  ├─ Policy
   │  ├─ Priority
   │  ├─ Binding
   │  ├─ Charging
   │  ├─ Quota
   │  ├─ ChargingTrigger
   │  ├─ Runtime
   │  ├─ ValidationDiagnosis
   │  ├─ LocalBreakout
   │  └─ QoSOrchestration
   │
   ├─ Feature
   │  ├─ UDG: SA-Basic
   │  ├─ UDG: PCC基本功能
   │  ├─ UDG: 基于业务感知的带宽控制
   │  ├─ UDG: 用户Portal
   │  ├─ UNC: PCC基本功能
   │  ├─ UNC: 内容计费基本功能
   │  ├─ UNC: 支持融合计费
   │  ├─ UNC: 基于预定义规则的分流策略控制
   │  ├─ UNC: 基于位置信息的分流策略控制
   │  ├─ UNC: 基于漫游地动态签约的分流策略控制
   │  ├─ UNC: 基于动态规则的分流策略控制
   │  └─ UNC: 公网私网业务独立计费
   │
   ├─ ConfigObject
   │  ├─ UDG侧: Filter / L7Filter / FlowFilter / Rule / PCCActionProp / Redirect / HEADEN / IPFarm
   │  ├─ UNC侧: PDUTRIGGER / RGTRIGGER / URR -> URRGroup -> PCCPolicyGrp -> Rule -> UserProfile
   │  ├─ 分流旁支: App ID / selectedDnn / PRA绑定 / DNAI / PDR
   │  └─ QoS旁支: Rule / QER / PFS / QFI
```

## 25. 最终结论

“业务图谱的定义”和“业务感知的业务图谱”不是一回事。

二者关系是：

```text
业务图谱定义
  = 一套通用 schema + schema 关系主链

业务感知的业务图谱
  = 在这套 schema 上，对 BusinessDomain=业务感知 的具体实例化
```

所以：

1. `Part A` 解释了什么叫业务图谱
2. `Part B` 给出了业务感知在 4 个一级场景、4 个交付方案、工程任务、第二层支撑对象和桥接对象上的具体实例化
3. 当前最终结构已经收敛为：
   - 第一层：`BusinessDomain / NetworkScenario / DeliverySolution / EngineeringTask`
   - 第二层：`Participant / Scope / DecisionPoint / ValidationPlan / BusinessRule`
   - 第三层：`DomainSemanticObject / Feature / ConfigObject`

这两部分合在一起，才是完整答案。
