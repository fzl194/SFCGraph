# 业务感知第一条完整闭包 v0.2（严格按 Schema）

## 1. 本页定位

本页只处理业务感知的第一条完整闭包：

```text
差异化计费
+ 免费业务
+ 默认兜底计费
```

它是业务感知全景中的第一条主线，不是全景本身。

本页目标不是再讲一遍产品案例，而是把这条主线严格落回已定义的 schema：

- `BusinessDomain`
- `NetworkScenario`
- `ReferencePattern`
- `DeliverySolution`
- `EngineeringTask`
- `DomainSemanticObject`
- `Capability`
- `Feature`
- `ConfigObject`
- `Evidence`

## 2. 直接学习的原始语料

### 2.1 UDG 业务专题

- `output\UDG_Product_Documentation_CH_20.15.2\特性部署\业务专题\UDG业务感知专题\业务感知配置\激活业务感知\基于业务套餐的配置实例\套餐1：计费场景_93112148.md`
- `output\UDG_Product_Documentation_CH_20.15.2\特性部署\业务专题\UDG业务感知专题\业务感知配置\激活业务感知\规则配置\规则配置全景_92882615.md`

### 2.2 UDG 特性

- `output\UDG_Product_Documentation_CH_20.15.2\特性部署\特性指南\UDG特性指南\业务感知功能\GWFD-110101 SA-Basic\GWFD-110101 SA-Basic特性概述_73565837.md`
- `output\UDG_Product_Documentation_CH_20.15.2\特性部署\特性指南\UDG特性指南\业务感知功能\GWFD-110101 SA-Basic\GWFD-110101 SA-Basic参考信息_90197552.md`
- `output\UDG_Product_Documentation_CH_20.15.2\特性部署\特性指南\UDG特性指南\计费功能\GWFD-020301 内容计费基本功能\GWFD-020301 内容计费基本功能特性概述_66863837.md`

### 2.3 UNC 特性与业务专题

- `output\UNC 20.15.2 产品文档(裸机容器) 05\网络部署\特性部署\UNC特性指南\计费管理功能\WSFD-109002 内容计费基本功能\特性概述_66402110.md`
- `output\UNC 20.15.2 产品文档(裸机容器) 05\网络部署\特性部署\UNC特性指南\计费管理功能\WSFD-109002 内容计费基本功能\激活内容计费_74013177.md`
- `output\UNC 20.15.2 产品文档(裸机容器) 05\网络部署\特性部署\UNC特性指南\计费管理功能\WSFD-011206 支持融合计费\特性概述_67655715.md`
- `output\UNC 20.15.2 产品文档(裸机容器) 05\网络部署\业务专题\5G Core 计费解决方案\计费解决方案概述\计费方案部署与调测\方案四：部署NCG且基于服务化接口的离线+在线计费组网方案\SMF配置\配置融合计费费率标识_90679673.md`

## 3. 当前闭包的对象实例

### 3.1 `BusinessDomain`

| Schema类型 | 实例ID | 中文名称 |
| --- | --- | --- |
| `BusinessDomain` | `BD-BA` | 业务感知 |

### 3.2 `NetworkScenario`

| Schema类型 | 实例ID | 中文名称 | 说明 |
| --- | --- | --- | --- |
| `NetworkScenario` | `NS-BA-001` | 差异化计费 | 对不同业务类型实施不同费率 |
| `NetworkScenario` | `NS-BA-002` | 免费业务 | 对命中特定业务的流量不收费 |
| `NetworkScenario` | `NS-BA-003` | 默认兜底计费 | 未命中特殊业务时进入默认计费路径 |

### 3.3 `ReferencePattern`

| Schema类型 | 实例ID | 中文名称 | 说明 |
| --- | --- | --- | --- |
| `ReferencePattern` | `RP-BA-001` | 套餐1：计费场景 | UDG 侧完整套餐样板 |
| `ReferencePattern` | `RP-BA-002` | 融合计费费率标识配置 | UNC/SMF 侧业务粒度计费对象链样板 |

### 3.4 `DeliverySolution`

| Schema类型 | 实例ID | 中文名称 | 说明 |
| --- | --- | --- | --- |
| `DeliverySolution` | `DS-BA-001` | 差异化计费 + 免费业务 + 默认兜底计费 | 当前第一条闭包对应的方案候选 |

### 3.5 `DomainSemanticObject`

| Schema类型 | 实例ID | 当前闭包中的作用 |
| --- | --- | --- |
| `DomainSemanticObject` | `BA.TrafficRecognitionSemantics` | 识别 URL / 协议 / 指定 IP |
| `DomainSemanticObject` | `BA.RuleSemantics` | 将识别条件、计费动作和优先级绑定成 Rule |
| `DomainSemanticObject` | `BA.ChargingSemantics` | 表达独立费率、免费和兜底费率 |
| `DomainSemanticObject` | `BA.BindingSemantics` | 表达 RuleBinding 和缺省 URR 组绑定 |
| `DomainSemanticObject` | `BA.PrioritySemantics` | 表达多业务重叠时的优先级裁决 |
| `DomainSemanticObject` | `BA.ValidationDiagnosisSemantics` | 表达 CP/UP 一致性和计费链核查 |

### 3.6 `Capability`

| Schema类型 | 实例ID | 中文名称 | 说明 |
| --- | --- | --- | --- |
| `Capability` | `Capability:BA:TrafficRecognition` | 业务流识别能力 | 提供三四层、协议、七层识别底座 |
| `Capability` | `Capability:BA:ContentChargingUP` | UDG侧内容计费能力 | UDG/UPF 侧承接业务粒度计费执行 |
| `Capability` | `Capability:BA:ContentChargingCP` | UNC侧内容计费能力 | SMF 侧组织业务粒度计费规则和标识 |
| `Capability` | `Capability:BA:ConvergedCharging` | 融合计费控制能力 | 统一承接 RG/RG+SID 计费控制框架 |

### 3.7 `Feature`

| Schema类型 | 特性编号 | 中文名称 |
| --- | --- | --- |
| `Feature` | `GWFD-110101` | SA-Basic |
| `Feature` | `GWFD-020301` | 内容计费基本功能 |
| `Feature` | `WSFD-109002` | 内容计费基本功能 |
| `Feature` | `WSFD-011206` | 支持融合计费 |

### 3.8 `EngineeringTask`

| Schema类型 | 实例ID | 中文名称 | 说明 |
| --- | --- | --- | --- |
| `EngineeringTask` | `TASK-BA-001` | 划分业务类别和优先级 | 明确专项业务、免费业务、兜底业务 |
| `EngineeringTask` | `TASK-BA-002` | 设计识别条件 | 设计 Filter / L7Filter / Protocol / FlowFilter |
| `EngineeringTask` | `TASK-BA-003` | 设计计费动作 | 设计 URR / URRGroup / PCCPolicyGrp |
| `EngineeringTask` | `TASK-BA-004` | 设计 Rule 与优先级 | 建立匹配与策略绑定关系 |
| `EngineeringTask` | `TASK-BA-005` | 设计套餐绑定 | 建立 UserProfile / RuleBinding / 缺省 URR 组绑定 |
| `EngineeringTask` | `TASK-BA-006` | 做 CP/UP 一致性与计费链验收 | 核查关键对象和关键参数一致性 |

### 3.9 `ConfigObject`

| Schema类型 | 实例ID | 中文名称 | 厂商侧 |
| --- | --- | --- | --- |
| `ConfigObject` | `ConfigObject:UDG:IPList` | IP地址列表 | UDG |
| `ConfigObject` | `ConfigObject:UDG:Filter` | 三四层过滤器 | UDG |
| `ConfigObject` | `ConfigObject:UDG:L7Filter` | 七层过滤器 | UDG |
| `ConfigObject` | `ConfigObject:UDG:FlowFilter` | 流过滤器 | UDG |
| `ConfigObject` | `ConfigObject:UDG:FlowFilterGroup` | 流过滤器组 | UDG |
| `ConfigObject` | `ConfigObject:UDG:URR` | 使用量上报规则 | UDG |
| `ConfigObject` | `ConfigObject:UDG:URRGroup` | URR组 | UDG |
| `ConfigObject` | `ConfigObject:UDG:PccPolicyGrp` | PCC策略组 | UDG |
| `ConfigObject` | `ConfigObject:UDG:Rule` | 规则 | UDG |
| `ConfigObject` | `ConfigObject:UDG:UserProfile` | 用户模板 | UDG |
| `ConfigObject` | `ConfigObject:UDG:RuleBinding` | 规则绑定 | UDG |
| `ConfigObject` | `ConfigObject:UNC:URR` | 使用量上报规则 | UNC |
| `ConfigObject` | `ConfigObject:UNC:URRGroup` | URR组 | UNC |
| `ConfigObject` | `ConfigObject:UNC:PccPolicyGrp` | PCC策略组 | UNC |
| `ConfigObject` | `ConfigObject:UNC:Rule` | 规则 | UNC |
| `ConfigObject` | `ConfigObject:UNC:UserProfile` | 用户模板 | UNC |
| `ConfigObject` | `ConfigObject:UNC:RuleBinding` | 规则绑定 | UNC |

### 3.10 `Evidence`

当前第一条闭包正式使用的证据对象：

- `EVI-UDG-BA-93112148`
- `EVI-UDG-BA-92882615`
- `EVI-UDG-FEAT-73565837`
- `EVI-UDG-FEAT-90197552`
- `EVI-UDG-FEAT-66863837`
- `EVI-UNC-FEAT-66402110`
- `EVI-UNC-FEAT-74013177`
- `EVI-UNC-FEAT-67655715`
- `EVI-UNC-TOPIC-90679673`

## 4. 当前闭包的关系实例

### 4.1 通用业务图谱关系

| 关系标识 | 起点 | 终点 | 说明 |
| --- | --- | --- | --- |
| `contains` | `BD-BA` | `NS-BA-001` | 业务感知包含差异化计费场景 |
| `contains` | `BD-BA` | `NS-BA-002` | 业务感知包含免费业务场景 |
| `contains` | `BD-BA` | `NS-BA-003` | 业务感知包含默认兜底计费场景 |
| `has_pattern` | `NS-BA-001` | `RP-BA-001` | 差异化计费可参考套餐1计费样板 |
| `has_pattern` | `NS-BA-001` | `RP-BA-002` | 差异化计费可参考 SMF 侧费率标识对象链 |
| `has_pattern` | `NS-BA-002` | `RP-BA-001` | 免费业务在套餐1计费场景中有直接样板 |
| `has_pattern` | `NS-BA-003` | `RP-BA-001` | 默认兜底计费在套餐1中有直接样板 |
| `has_pattern` | `NS-BA-003` | `RP-BA-002` | 默认兜底计费在 SMF 侧通过缺省 URR 组落地 |
| `instantiated_as` | `NS-BA-001` | `DS-BA-001` | 当前方案覆盖差异化计费 |
| `instantiated_as` | `NS-BA-002` | `DS-BA-001` | 当前方案覆盖免费业务 |
| `instantiated_as` | `NS-BA-003` | `DS-BA-001` | 当前方案覆盖默认兜底计费 |
| `decomposes_to` | `DS-BA-001` | `TASK-BA-001` | 方案拆为工程任务 |
| `decomposes_to` | `DS-BA-001` | `TASK-BA-002` | 方案拆为工程任务 |
| `decomposes_to` | `DS-BA-001` | `TASK-BA-003` | 方案拆为工程任务 |
| `decomposes_to` | `DS-BA-001` | `TASK-BA-004` | 方案拆为工程任务 |
| `decomposes_to` | `DS-BA-001` | `TASK-BA-005` | 方案拆为工程任务 |
| `decomposes_to` | `DS-BA-001` | `TASK-BA-006` | 方案拆为工程任务 |

### 4.2 领域语义关系

| 关系标识 | 起点 | 终点 | 说明 |
| --- | --- | --- | --- |
| `uses_semantic_object` | `NS-BA-001` | `BA.TrafficRecognitionSemantics` | 差异化计费依赖业务流识别 |
| `uses_semantic_object` | `NS-BA-001` | `BA.RuleSemantics` | 差异化计费依赖 Rule 与优先级 |
| `uses_semantic_object` | `NS-BA-001` | `BA.ChargingSemantics` | 差异化计费依赖多费率路径 |
| `uses_semantic_object` | `NS-BA-001` | `BA.BindingSemantics` | 差异化计费依赖套餐绑定 |
| `uses_semantic_object` | `NS-BA-001` | `BA.PrioritySemantics` | 差异化计费依赖优先级裁决 |
| `uses_semantic_object` | `NS-BA-001` | `BA.ValidationDiagnosisSemantics` | 差异化计费需要验收和回查 |
| `uses_semantic_object` | `NS-BA-002` | `BA.ChargingSemantics` | 免费业务属于特殊计费语义 |
| `uses_semantic_object` | `NS-BA-002` | `BA.RuleSemantics` | 免费业务仍依赖 Rule 命中 |
| `uses_semantic_object` | `NS-BA-003` | `BA.BindingSemantics` | 默认兜底计费依赖缺省 URR 组绑定 |
| `uses_semantic_object` | `NS-BA-003` | `BA.PrioritySemantics` | 默认兜底计费依赖低优先级兜底 Rule |
| `instantiates_semantic_object` | `DS-BA-001` | `BA.TrafficRecognitionSemantics` | 实例化为三四层过滤、协议识别、七层 URL/Host 识别 |
| `instantiates_semantic_object` | `DS-BA-001` | `BA.RuleSemantics` | 实例化为多条 Rule 和优先级裁决 |
| `instantiates_semantic_object` | `DS-BA-001` | `BA.ChargingSemantics` | 实例化为专项业务费率、免费业务和默认兜底费率 |
| `instantiates_semantic_object` | `DS-BA-001` | `BA.BindingSemantics` | 实例化为 UserProfile、RuleBinding 和缺省 URR 组绑定 |
| `instantiates_semantic_object` | `DS-BA-001` | `BA.PrioritySemantics` | 实例化为业务编号越小优先级越高 |
| `instantiates_semantic_object` | `DS-BA-001` | `BA.ValidationDiagnosisSemantics` | 实例化为 CP/UP 一致性和计费链核查 |
| `semantic_realized_by_config` | `BA.TrafficRecognitionSemantics` | `ConfigObject:UDG:Filter` | 三四层过滤实现流量识别 |
| `semantic_realized_by_config` | `BA.TrafficRecognitionSemantics` | `ConfigObject:UDG:IPList` | 指定服务器 IP 范围通过 IPList 承接 |
| `semantic_realized_by_config` | `BA.TrafficRecognitionSemantics` | `ConfigObject:UDG:L7Filter` | 七层过滤实现 URL/Host 识别 |
| `semantic_realized_by_config` | `BA.TrafficRecognitionSemantics` | `ConfigObject:UDG:FlowFilter` | 组合识别条件 |
| `semantic_realized_by_config` | `BA.RuleSemantics` | `ConfigObject:UDG:Rule` | Rule 承载匹配与优先级 |
| `semantic_realized_by_config` | `BA.ChargingSemantics` | `ConfigObject:UDG:URR` | UDG 侧计费语义对象 |
| `semantic_realized_by_config` | `BA.ChargingSemantics` | `ConfigObject:UNC:URR` | UNC 侧费率标识对象 |
| `semantic_realized_by_config` | `BA.BindingSemantics` | `ConfigObject:UDG:UserProfile` | UDG 侧套餐绑定对象 |
| `semantic_realized_by_config` | `BA.BindingSemantics` | `ConfigObject:UNC:UserProfile` | UNC 侧默认绑定对象 |

### 4.3 能力、特性和方案关系

| 关系标识 | 起点 | 终点 | 说明 |
| --- | --- | --- | --- |
| `requires_capability` | `DS-BA-001` | `Capability:BA:TrafficRecognition` | 需要先识别业务流 |
| `requires_capability` | `DS-BA-001` | `Capability:BA:ContentChargingUP` | 需要 UDG/UPF 侧业务粒度计费执行 |
| `requires_capability` | `DS-BA-001` | `Capability:BA:ContentChargingCP` | 需要 SMF 侧业务粒度计费编排 |
| `requires_capability` | `DS-BA-001` | `Capability:BA:ConvergedCharging` | 需要统一计费控制框架 |
| `implemented_by_feature` | `Capability:BA:TrafficRecognition` | `GWFD-110101` | SA-Basic 实现识别底座 |
| `implemented_by_feature` | `Capability:BA:ContentChargingUP` | `GWFD-020301` | UDG 内容计费特性实现 UDG 侧内容计费能力 |
| `implemented_by_feature` | `Capability:BA:ContentChargingCP` | `WSFD-109002` | UNC 内容计费特性实现 SMF 侧内容计费能力 |
| `implemented_by_feature` | `Capability:BA:ConvergedCharging` | `WSFD-011206` | 融合计费特性实现统一计费框架 |

### 4.4 工程任务到配置对象关系

| 关系标识 | 起点 | 终点 | 说明 |
| --- | --- | --- | --- |
| `realized_by_config` | `TASK-BA-002` | `ConfigObject:UDG:Filter` | 三四层过滤条件 |
| `realized_by_config` | `TASK-BA-002` | `ConfigObject:UDG:IPList` | 指定服务器 IP 范围列表 |
| `realized_by_config` | `TASK-BA-002` | `ConfigObject:UDG:L7Filter` | 七层识别条件 |
| `realized_by_config` | `TASK-BA-002` | `ConfigObject:UDG:FlowFilter` | 识别条件组合对象 |
| `realized_by_config` | `TASK-BA-002` | `ConfigObject:UDG:FlowFilterGroup` | 免费业务多条件组合对象 |
| `realized_by_config` | `TASK-BA-003` | `ConfigObject:UDG:URR` | UDG 侧业务计费语义对象 |
| `realized_by_config` | `TASK-BA-003` | `ConfigObject:UDG:URRGroup` | UDG 侧 URR 组对象 |
| `realized_by_config` | `TASK-BA-003` | `ConfigObject:UDG:PccPolicyGrp` | UDG 侧 PCC 策略组对象 |
| `realized_by_config` | `TASK-BA-003` | `ConfigObject:UNC:URR` | UNC 侧费率标识与计费对象 |
| `realized_by_config` | `TASK-BA-003` | `ConfigObject:UNC:URRGroup` | UNC 侧 URR 组对象 |
| `realized_by_config` | `TASK-BA-003` | `ConfigObject:UNC:PccPolicyGrp` | UNC 侧 PCC 策略组对象 |
| `realized_by_config` | `TASK-BA-004` | `ConfigObject:UDG:Rule` | UDG 侧 Rule 和优先级对象 |
| `realized_by_config` | `TASK-BA-004` | `ConfigObject:UNC:Rule` | UNC 侧 Rule 对象 |
| `realized_by_config` | `TASK-BA-005` | `ConfigObject:UDG:UserProfile` | UDG 侧套餐承载对象 |
| `realized_by_config` | `TASK-BA-005` | `ConfigObject:UDG:RuleBinding` | UDG 侧规则绑定对象 |
| `realized_by_config` | `TASK-BA-005` | `ConfigObject:UNC:UserProfile` | UNC 侧用户模板对象 |
| `realized_by_config` | `TASK-BA-005` | `ConfigObject:UNC:RuleBinding` | UNC 侧规则绑定对象 |
| `realized_by_config` | `TASK-BA-005` | `ConfigObject:UDG:URRGroup` | UDG 侧缺省 URR 组绑定目标 |
| `realized_by_config` | `TASK-BA-005` | `ConfigObject:UNC:URRGroup` | UNC 侧缺省 URR 组绑定目标 |

## 5. 当前闭包从原始文档读出的主链

### 5.1 UDG 主链

从 `套餐1：计费场景` 和 `规则配置全景` 可以直接收敛出：

```text
Filter / L7Filter / Protocol
-> FlowFilter / FlowFilterGroup
-> URR
-> URRGroup
-> PCCPolicyGrp
-> Rule
-> UserProfile
-> RuleBinding
```

这条链解决的是：

- 识别条件如何表达
- 计费动作如何组织
- 多条 Rule 如何归到同一业务套餐

### 5.2 UNC/SMF 主链

从 `配置融合计费费率标识` 可以直接收敛出：

```text
URR
-> URRGroup
-> PCCPolicyGrp
-> Rule
-> UserProfile
-> RuleBinding
```

同时文档明确补充：

- `SET URRGRPBINDING` 用于给 `UserProfile` 绑定缺省 URR 组
- `URRID / USAGERPTMODE / OFFMETERINGTYPE` 需要与 UPF 一致

### 5.3 当前闭包的业务结论

这条闭包已经能稳定表达：

```text
业务识别
-> Rule 裁决
-> 差异化计费
-> 免费业务
-> 默认兜底计费
-> UserProfile 绑定闭包
```

## 6. 当前闭包的边界

本闭包当前还没有覆盖：

- 配额耗尽后的动作切换
- 七层重定向
- 带宽控制
- 头增强
- 防欺诈 / 异常流量控制

因此它是业务感知全景中的第一条收费主线，而不是整个业务感知的最终全景。
