# 按 final_v2 schema 实例化一个业务感知案例

## 1. 文档目标

这份文档只做“实例化”，不改模型。

模型以 [19-business-awareness-business-graph-final_v2.md](D:/mywork/KnowledgeBase/Graph/myoutput/business-awareness-graph/19-business-awareness-business-graph-final_v2.md) 为准，因此本文只沿用其中已经定义的 schema：

- `BusinessDomain`
- `NetworkScenario`
- `ReferencePattern`
- `DeliverySolution`
- `EngineeringTask`
- `Participant`
- `Scope`
- `DecisionPoint`
- `RuntimeFlow`
- `ValidationPlan`
- `DiagnosisRule`
- `RiskConstraint`
- `Evidence`
- `DomainSemanticObject`
- `Feature`
- `ConfigObject`

## 2. 原始依据

本文实例化的案例，直接依据以下原始文档：

1. [业务感知场景举例_92407896.md](D:/mywork/KnowledgeBase/Graph/output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知功能描述/业务感知场景举例_92407896.md)
2. [套餐1：计费场景_93112148.md](D:/mywork/KnowledgeBase/Graph/output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/激活业务感知/基于业务套餐的配置实例/套餐1：计费场景_93112148.md)
3. [GWFD-110101 SA-Basic特性概述_73565837.md](D:/mywork/KnowledgeBase/Graph/output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110101%20SA-Basic/GWFD-110101%20SA-Basic特性概述_73565837.md)
4. [配置架构_92957237.md](D:/mywork/KnowledgeBase/Graph/output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110101%20SA-Basic/实现原理/配置架构_92957237.md)
5. [UNC和UDG配置映射_92963580.md](D:/mywork/KnowledgeBase/Graph/output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110101%20SA-Basic/实现原理/UNC和UDG配置映射_92963580.md)
6. [GWFD-020351 PCC基本功能特性概述_47011385.md](D:/mywork/KnowledgeBase/Graph/output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351%20PCC基本功能/GWFD-020351%20PCC基本功能特性概述_47011385.md)
7. [WSFD-109002 内容计费基本功能特性概述_66402110.md](D:/mywork/KnowledgeBase/Graph/output/UNC%2020.15.2%20产品文档(裸机容器)%2005/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-109002%20内容计费基本功能/特性概述_66402110.md)
8. [WSFD-011206 支持融合计费特性概述_67655715.md](D:/mywork/KnowledgeBase/Graph/output/UNC%2020.15.2%20产品文档(裸机容器)%2005/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206%20支持融合计费/特性概述_67655715.md)
9. [配置融合计费费率标识_93360308.md](D:/mywork/KnowledgeBase/Graph/output/UNC%2020.15.2%20产品文档(裸机容器)%2005/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206%20支持融合计费/激活支持融合计费/配置融合计费费率标识_93360308.md)
10. [配置融合计费模板_93400212.md](D:/mywork/KnowledgeBase/Graph/output/UNC%2020.15.2%20产品文档(裸机容器)%2005/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206%20支持融合计费/激活支持融合计费/配置融合计费模板_93400212.md)
11. [配置计费属性CC_90776700.md](D:/mywork/KnowledgeBase/Graph/output/UNC%2020.15.2%20产品文档(裸机容器)%2005/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206%20支持融合计费/激活支持融合计费/配置计费属性CC_90776700.md)
12. [计费会话创建流程_01_10001.md](D:/mywork/KnowledgeBase/Graph/output/UNC%2020.15.2%20产品文档(裸机容器)%2005/网络部署/特性部署/UNC特性指南/计费管理功能/WSFD-011206%20支持融合计费/实现原理/计费会话创建流程_01_10001.md)

## 3. 案例本身

本文选用的案例就是原始文档中的这一条：

```text
普通用户访问视频业务时，
访问A网站的视频不计入流量，
A网站以外的视频按1元/Gb计费，
每月最多100G，
流量耗尽时重定向到充值页面。
```

这个案例在模型中首先属于 `计费场景`，同时包含“配额耗尽后动作切换”这一组交叉行为。

## 4. 按 schema 实例化

### 4.1 `BusinessDomain`

| schema | 本案例实例 | 说明 |
| --- | --- | --- |
| `BusinessDomain` | `业务感知` | 这个案例的根问题不是“单独计费”或“单独重定向”，而是先识别业务，再实施不同计费和控制策略，因此属于业务感知域 |

### 4.2 `NetworkScenario`

| schema | 本案例实例 | 说明 |
| --- | --- | --- |
| `NetworkScenario` | `计费场景` | 原始语料里最直接的一级场景名就是“计费场景” |

### 4.3 `ReferencePattern`

| schema | 本案例实例 | 说明 |
| --- | --- | --- |
| `ReferencePattern` | `业务感知定义、规则与运行链样板` | 说明这是“识别 -> 匹配 -> 执行”的业务域 |
| `ReferencePattern` | `复合业务套餐样板` | 同一套餐里同时组织免费、收费、耗尽后动作 |
| `ReferencePattern` | `计费场景样板` | 套餐1说明了差异化计费、免费业务、默认计费如何组织 |
| `ReferencePattern` | `融合计费会话闭环样板` | 场景举例和计费流程说明了配额、Trigger、会话更新闭环 |

### 4.4 `DeliverySolution`

| schema | 本案例实例 | 说明 |
| --- | --- | --- |
| `DeliverySolution` | `差异化计费、免费业务与默认计费组合方案` | 负责把免费业务、专项计费、默认计费组织在同一套餐里 |
| `DeliverySolution` | `配额耗尽后体验切换方案` | 负责把“100G耗尽后重定向到充值页面”这段运行态切换组织起来 |

### 4.5 `EngineeringTask`

| schema | 本案例实例 | 原始语料里的对应内容 |
| --- | --- | --- |
| `EngineeringTask` | `规划生效范围` | `APN1 / User Profile1 / User Profile Group1` |
| `EngineeringTask` | `规划识别条件` | `FlowFilter1` 识别A网站视频，`FlowFilter2` 识别非A网站视频 |
| `EngineeringTask` | `规划Rule与优先级` | `Rule1 > Rule2 > Rule3` |
| `EngineeringTask` | `规划计费对象与费率标识` | `PCCGroup1 + URR1` 承接 1元/Gb 计费 |
| `EngineeringTask` | `规划配额耗尽动作` | `PCCGroup3` 承接充值页重定向动作 |
| `EngineeringTask` | `规划计费Trigger与多UPF配额` | 这里主要体现为 `UPF上报用量 -> CHF通知 -> SMF请求更新 -> PCF下发Rule3` |

### 4.6 `Participant`

| schema | 本案例实例 | 作用 |
| --- | --- | --- |
| `Participant` | `用户/终端` | 发起视频业务访问 |
| `Participant` | `PCF` | 决策并下发 `Rule1 / Rule2`，额度耗尽后再下发 `Rule3` |
| `Participant` | `SMF` | 承接 PCF 规则、向 CHF 申请配额/上报用量、向 UPF 下发规则 |
| `Participant` | `UPF` | 识别业务、匹配规则、执行免费/计费/重定向 |
| `Participant` | `CHF` | 管理配额并在额度耗尽时通知 SMF |

### 4.7 `Scope`

| schema | 本案例实例 | 说明 |
| --- | --- | --- |
| `Scope` | `APN1` | 规则挂在 APN 侧组织 |
| `Scope` | `User Profile1` | 规则、默认计费和模板组织的核心载体 |
| `Scope` | `普通用户` | 原始场景明确是普通用户的视频业务 |

### 4.8 `DecisionPoint`

| schema | 本案例实例 | 说明 |
| --- | --- | --- |
| `DecisionPoint` | `规则优先级选择` | `Rule1 > Rule2 > Rule3`，决定免费优先于收费，收费优先于耗尽后动作 |
| `DecisionPoint` | `计费方式选择` | `A网站视频免费`，`其他视频按1元/Gb` |
| `DecisionPoint` | `配额耗尽动作选择` | 流量耗尽后选择 `REDIRECT` 到充值页面 |

### 4.9 `RuntimeFlow`

| schema | 本案例实例 | 说明 |
| --- | --- | --- |
| `RuntimeFlow` | `PCF/SMF按场景生成并下发策略 -> SMF翻译策略并建立规则上下文 -> 报文到达UPF -> UPF解析与识别 -> 规则匹配 -> 执行绑定策略 -> 用量上报 -> 计费会话更新 -> 重定向生效` | 这个案例最关键的是它不是静态套餐，而是会在运行中切换 `Rule2` 和 `Rule3` |

### 4.10 `ValidationPlan`

| schema | 本案例实例 | 看什么 |
| --- | --- | --- |
| `ValidationPlan` | `差异化计费验证` | 非 A 网站视频是否真正按 1元/Gb 计费 |
| `ValidationPlan` | `免费业务验证` | A 网站视频是否真正不计费 |
| `ValidationPlan` | `Trigger与计费会话验证` | 用量上报后是否触发会话更新 |
| `ValidationPlan` | `配额耗尽动作验证` | 流量耗尽后是否真的切到充值页重定向 |

### 4.11 `DiagnosisRule`

| schema | 本案例实例 | 优先检查点 |
| --- | --- | --- |
| `DiagnosisRule` | `业务流未进入专项计费` | `Rule2 -> PCCPolicyGrp -> URRGroup -> URR` |
| `DiagnosisRule` | `免费业务仍被计费` | `Rule1` 是否优先命中，免费 URR 是否配置正确 |
| `DiagnosisRule` | `配额耗尽后动作不对` | `QUOTA / Trigger / CHF -> SMF -> PCF` 更新链 |
| `DiagnosisRule` | `Trigger未按预期触发` | `ChargingDataCreate / Update`、`TriggerType`、`CTXSTARTRATING / CHFINIT` |

### 4.12 `RiskConstraint`

| schema | 本案例实例 | 说明 |
| --- | --- | --- |
| `RiskConstraint` | `裁决约束` | `Rule1 / Rule2 / Rule3` 优先级错了，免费、计费、重定向顺序就会错 |
| `RiskConstraint` | `对外交互约束` | `SMF <-> CHF` 交互异常会直接影响配额动作链 |
| `RiskConstraint` | `Trigger约束` | Trigger配置不当会导致会话更新和动作切换不发生 |
| `RiskConstraint` | `Default Quota约束` | 正式配额未及时返回时可能影响业务是否被放通 |

### 4.13 `DomainSemanticObject`

| schema | 本案例实例 | 在本案例中的作用 |
| --- | --- | --- |
| `DomainSemanticObject` | `PacketParsing` | 先对报文做三四层和七层解析 |
| `DomainSemanticObject` | `ProtocolRecognition` | 区分视频业务以及访问的具体网站 |
| `DomainSemanticObject` | `FilterCondition` | 把“A网站视频”和“非A网站视频”翻译成可匹配条件 |
| `DomainSemanticObject` | `Rule` | 把条件和动作链组织成 `Rule1/2/3` |
| `DomainSemanticObject` | `Charging` | 负责免费、按流量收费、默认计费 |
| `DomainSemanticObject` | `ChargingTrigger` | 负责额度变化后触发更新 |
| `DomainSemanticObject` | `Quota` | 负责100G配额的运行边界 |
| `DomainSemanticObject` | `Priority` | 决定三条Rule的生效顺序 |

### 4.14 `Feature`



| schema | Feature实例 | 在本案例中的承载职责 | 原始依据 |
| --- | --- | --- | --- |
| `Feature` | `GWFD-110101 SA-Basic` | 承担三四层解析、协议识别和七层解析，是 `FlowFilter`、`Rule` 能命中视频业务的识别底座 | SA-Basic 特性概述、配置架构 |
| `Feature` | `GWFD-020351 PCC基本功能` | 承担策略与计费控制框架，使 `PCF -> SMF -> UPF` 的 PCC 策略下发和执行成立 | PCC基本功能特性概述 |
| `Feature` | `WSFD-109002 内容计费基本功能` | 把“按视频业务粒度差异化收费”正式定义为内容计费能力 | 内容计费基本功能特性概述 |
| `Feature` | `WSFD-011206 支持融合计费` | 把在线/离线计费、配额申请、Trigger、计费会话创建/更新组织成 Nchf 融合计费闭环 | 支持融合计费特性概述、计费会话创建流程 |

这四个 `Feature` 在这个案例里的关系不是并列堆叠，而是一条承载链：

```text
SA-Basic
-> 负责把业务识别出来
-> PCC基本功能
-> 负责把识别结果变成规则与策略
-> 内容计费基本功能
-> 负责把不同视频流变成不同计费路径
-> 支持融合计费
-> 负责把计费路径变成配额、Trigger、会话更新和耗尽后动作
```

### 4.15 `ConfigObject`



#### 4.15.1 UDG/UPF 侧 `ConfigObject`

| schema | ConfigObject实例 | 在本案例中的作用 | 原始脚本依据 |
| --- | --- | --- | --- |
| `ConfigObject` | `FILTER` | 承接三四层条件，如 any-to-any | 套餐1脚本中的 `ADD FILTER` |
| `ConfigObject` | `L7FILTER` | 承接 A 网站 URL 条件 | `ADD L7FILTER` |
| `ConfigObject` | `FLOWFILTER / FLOWFILTERGRP` | 把三四层条件、协议、七层条件组合成可用于 Rule 的过滤对象 | `ADD FLOWFILTER`、`ADD FLOWFILTERGRP` |
| `ConfigObject` | `URR` | 定义在线或离线计费统计对象，含免费/计费属性 | `ADD URR` |
| `ConfigObject` | `URRGROUP` | 把上下行 URR 组织成组 | `ADD URRGROUP` |
| `ConfigObject` | `PCCPOLICYGRP` | 把计费策略组和 URR 组绑定起来 | `ADD PCCPOLICYGRP` |
| `ConfigObject` | `RULE` | 把 `FLOWFILTER` 和 `PCCPOLICYGRP` 绑定，并指定优先级 | `ADD RULE` |
| `ConfigObject` | `USERPROFILE` | 把多条 Rule 组织成一个业务模板 | `ADD USERPROFILE` |
| `ConfigObject` | `URRGRPBINDING` | 给 `USERPROFILE` 绑定缺省URR组，实现默认计费 | `SET URRGRPBINDING` |
| `ConfigObject` | `RULEBINDING` | 把 `RULE` 绑定到 `USERPROFILE` | `ADD RULEBINDING` |

#### 4.15.2 UNC/SMF 侧 `ConfigObject`

| schema | ConfigObject实例 | 在本案例中的作用 | 原始依据 |
| --- | --- | --- | --- |
| `ConfigObject` | `URR` | 在SMF侧定义与UPF一致的 URRID、上报模式、RG 等计费对象 | 配置融合计费费率标识 |
| `ConfigObject` | `URRGROUP` | 在SMF侧组织在线/离线 URR | 配置融合计费费率标识 |
| `ConfigObject` | `PCCPOLICYGRP` | 在SMF侧把 URRGROUP 绑定进 PCC 策略组 | 配置融合计费费率标识 |
| `ConfigObject` | `RULE` | 在SMF侧定义与UPF一致的 Rule 名和策略绑定 | 配置融合计费费率标识 |
| `ConfigObject` | `USERPROFILE` | 在SMF侧承接同名业务模板 | 配置融合计费费率标识 |
| `ConfigObject` | `RULEBINDING` | 在SMF侧把 Rule 绑定到 UserProfile | 配置融合计费费率标识 |
| `ConfigObject` | `APN / APNUSRPROFG` | 把 UserProfile 组挂到 DNN/APN | 配置融合计费费率标识 |
| `ConfigObject` | `CCT` | 定义融合计费模板，控制阈值、时长、触发门限等 | 配置融合计费模板 |
| `ConfigObject` | `USRPROFCHARGE / APNCHARGECTRL` | 把 CCT 或 CC 绑定到 UserProfile / DNN | 配置融合计费模板、配置计费属性CC |
| `ConfigObject` | `CHARGECHAR` | 承接用户计费属性 CC | 配置计费属性CC |
| `ConfigObject` | `CTXSTARTRATING` | 决定计费会话创建时携带哪些 RG 去申请初始配额 | 计费会话创建流程 |
| `ConfigObject` | `CHFINIT` | 决定是否在 PDU 会话建立时触发 ChargingDataCreate | 计费会话创建流程 |
| `ConfigObject` | `QUOTAEXHAUSTACT` | 定义 RG 配额耗尽后的动作，例如 `BLOCK / REDIRECT / FORWARD` | 配置融合计费费率标识 |

这一层最重要的不是“列很多对象”，而是看出控制面和用户面的对象链是对应的。原始文档已经明确：

```text
APN/VPN、FlowFilter、Rule、UserProfile、URRID 等参数需要控制面和用户面合一规划。
```

这就是为什么 `ConfigObject` 不是单侧对象清单，而是双侧闭环对象链。

## 5. `Evidence` 如何把命令层带进来

你要求看到“命令层”，但按 `final_v2` 的模型，命令不单独作为 schema。  
因此本文把命令作为 `Evidence` 来承接，也就是：

```text
命令不是新的图谱对象，
而是 ConfigObject 的原始证据。
```

### 5.1 UDG/UPF 侧命令证据

| Evidence用途 | 对应命令 | 证明了哪个 ConfigObject |
| --- | --- | --- |
| 三四层过滤条件 | `ADD FILTER` | `FILTER` |
| 七层过滤条件 | `ADD L7FILTER` | `L7FILTER` |
| 过滤条件组合 | `ADD FLOWFILTER`、`ADD FLTBINDFLOWF`、`ADD PROTBINDFLOWF`、`ADD FLOWFILTERGRP` | `FLOWFILTER / FLOWFILTERGRP` |
| 计费对象 | `ADD URR` | `URR` |
| 计费对象分组 | `ADD URRGROUP` | `URRGROUP` |
| 策略组 | `ADD PCCPOLICYGRP` | `PCCPOLICYGRP` |
| 规则 | `ADD RULE` | `RULE` |
| 用户模板 | `ADD USERPROFILE` | `USERPROFILE` |
| 缺省URR组绑定 | `SET URRGRPBINDING` | `URRGRPBINDING` |
| 规则绑定模板 | `ADD RULEBINDING` | `RULEBINDING` |

### 5.2 UNC/SMF 侧命令证据

| Evidence用途 | 对应命令 | 证明了哪个 ConfigObject |
| --- | --- | --- |
| 费率标识与URR | `ADD URR` | `URR` |
| 计费对象组 | `ADD URRGROUP` | `URRGROUP` |
| PCC策略组 | `ADD PCCPOLICYGRP` | `PCCPOLICYGRP` |
| 规则对象 | `ADD RULE` | `RULE` |
| 用户模板 | `ADD USERPROFILE` | `USERPROFILE` |
| 规则绑定 | `ADD RULEBINDING` | `RULEBINDING` |
| DNN绑定模板组 | `ADD APN`、`ADD APNUSRPROFG`、`ADD USRPROFGROUP`、`ADD UPBINDUPG` | `APN / APNUSRPROFG` |
| 融合计费模板 | `ADD CCT`、`MOD CCT` | `CCT` |
| UserProfile粒度绑定计费模板 | `SET USRPROFCHARGE` | `USRPROFCHARGE` |
| DNN粒度绑定计费模板或计费属性 | `SET APNCHARGECTRL` | `APNCHARGECTRL` |
| 计费属性 | `ADD CHARGECHAR`、`SET GLBCHARGECHAR` | `CHARGECHAR` |
| 配额耗尽动作 | `ADD QUOTAEXHAUSTACT` | `QUOTAEXHAUSTACT` |

## 6. 最后把整条链压成一条“模型到实例”的闭环

如果严格按 `final_v2` 的 schema 来看，这个案例最终可以压成下面这条链：

```text
BusinessDomain
  = 业务感知
-> NetworkScenario
  = 计费场景
-> ReferencePattern
  = 计费场景样板 + 融合计费会话闭环样板
-> DeliverySolution
  = 差异化计费、免费业务与默认计费组合方案
  + 配额耗尽后体验切换方案
-> EngineeringTask
  = 识别条件规划 / Rule规划 / 计费对象规划 / 配额动作规划
-> DomainSemanticObject
  = FilterCondition / Rule / Charging / ChargingTrigger / Quota / Priority
-> Feature
  = SA-Basic / PCC基本功能 / 内容计费基本功能 / 支持融合计费
-> ConfigObject
  = FILTER / L7FILTER / FLOWFILTER / URR / URRGROUP / PCCPOLICYGRP / RULE / USERPROFILE / CCT / QUOTAEXHAUSTACT
-> Evidence
  = ADD FILTER / ADD FLOWFILTER / ADD URR / ADD RULE / ADD USERPROFILE / ADD CCT / ADD QUOTAEXHAUSTACT ...
```

这条链说明的就是：

```text
同一个业务案例，
如何从业务域，
一路落到场景、方案、任务、特性、配置对象，
最后再被具体命令证明出来。
```

## 7. 一句话总结

如果用 `final_v2` 的 schema 语言来总结这个案例，可以写成：

```text
“A网站视频免费、其他视频按1元/Gb计费、100G耗尽后重定向充值页”
这个案例，是 `BusinessDomain=业务感知` 下 `NetworkScenario=计费场景` 的一次实例化；
它通过 `ReferencePattern` 被组织为 `DeliverySolution`，
再拆为 `EngineeringTask`，
由 `SA-Basic / PCC基本功能 / 内容计费基本功能 / 支持融合计费` 这组 `Feature` 承载，
并最终落到 `Rule / URR / PCCPOLICYGRP / UserProfile / CCT / QUOTAEXHAUSTACT`
这组 `ConfigObject` 上，
命令脚本则作为 `Evidence` 证明这条对象链是真实存在的。
```
