# Batch-25: UNC SM策略 — 调测方法与业务拆解配置

## 1. 概述

本知识文档涵盖"5G PCC之SM策略解决方案"业务专题（UNC侧）中的**SM策略配置与调测**主题，共涉及10个源文档，按内容可分为四大板块：

- **调测方法概述与原则**：不同规则类型（动态规则、预定义规则/规则组、本地规则）在PCF/SMF/UPF三侧各自的调测关注点差异。
- **调测实操**：预定义规则/规则组调测（信令调测法 + 快速调测法）、本地PCC策略调测（信令调测法 + 快速调测法），涵盖完整的调测步骤、MML命令和信令码流解读。
- **N7接口与N4接口信令映射**：PCF经N7接口下发SM策略给SMF，SMF经N4接口转化为PFCP消息下发UPF执行，重点解析两类消息的关键信元映射关系（PDR/QER/FAR/URR的生成规则）。
- **业务拆解与动态规则配置**：单业务拆解方法（5步）、多业务拆解方法（6步，增加业务关系判断），以及动态PCC策略配置的业务配置逻辑和4G/5G差异。

这批文档是理解**SM策略从需求拆解到配置下发再到调试验证**全链路的核心方法论。

---

## 2. 核心知识点

### KP-01: 调测方法总框架 — 三种规则类型、两套调测方法

SM策略调测按规则类型分为三大场景，每种场景下PCF/SMF/UPF三侧调测关注点不同：

| 规则类型 | PCF侧关注点 | SMF侧关注点 | UPF侧关注点 |
|---------|------------|------------|------------|
| **动态规则** | 规则名(pccRuleId/sessRuleId)、QoS参数(5QI/ARP/MFBR/GFBR)是否按"If条件Then动作"逻辑正确下发 | 本地安装规则名、规则优先级(以PCF为准)、QoS Flow信息(5QI/ARP)、协商QoS(取PCF值与UDM签约值的最小值) | SMF仅下发QoS参数，**不下发动态规则名**；UPF无法查询到动态规则名，需关注用户会话上下文是否与PCF配置一致 |
| **预定义规则/规则组** | 规则名是否正确下发(pccRuleId携带预定义规则名) | 本地安装规则名(以PCF下发为准)、规则优先级(**以SMF本地定义为准**) | SMF将预定义规则名下发至UPF，UPF可查询到已激活的预定义规则名，需验证是否与SMF下发一致 |
| **本地规则** | **不涉及PCF** | SMF作为策略生成网元，根据规则下发条件判断是否激活本地预定义规则；规则优先级以SMF配置为准 | 同预定义规则场景，UPF侧需验证规则名和会话上下文 |

两套调测方法：
- **信令调测法**：基于网元间信令交互的详细分析，需在PCF/SMF/UPF三侧建立用户消息跟踪，通过N7/N4接口信令码流逐信元验证策略下发与执行的正确性。适用于深度问题定位。
- **快速调测法**：通过MML命令快速、直观判断PCC策略配置、下发与执行是否符合预期。适用于日常快速验证。

### KP-02: 信令调测法的三类消息流程

信令调测需跟踪三类核心消息流程：

1. **初始下发流程**：
   - PCF侧：用户PDU会话建立请求到达后，PCF通过"Npcf_SMPolicyControl_Create Response"消息下发SM策略。
   - SMF侧：收到PCF策略后，通过N4接口"PFCP Session Establishment Request"消息下发UPF。

2. **策略更新流程（PCF发起）**：
   - PCF修改签约信息后，通过"Npcf_SMPolicyControl_UpdateNotify Request"消息向SMF推送更新。
   - SMF收到后通过"PFCP Session Modification Request"消息向UPF更新。
   - 码流中体现为：安装新规则名 + 删除旧规则名(null)。

3. **事件上报流程（UPF/SMF发起）**：
   - UPF通过"PFCP Session Report Request"消息向SMF上报事件（如配额分片耗尽）。
   - SMF通过"Npcf_SMPolicyControl_Update Request"消息将事件内容上报PCF。
   - PCF再根据策略逻辑判断是否在"Npcf_SMPolicyControl_Update Response"中更新策略。

### KP-03: 预定义规则调测 vs 本地PCC策略调测的核心差异

| 对比维度 | 预定义规则/规则组调测 | 本地PCC策略调测 |
|---------|---------------------|----------------|
| **涉及网元** | PCF + SMF + UPF 三侧 | SMF + UPF 两侧（**不涉及PCF**） |
| **策略来源** | PCF根据签约信息下发预定义规则名，SMF接收后安装并下发UPF | SMF本地配置生成，根据规则下发条件（APN匹配等）激活 |
| **QoS参数来源** | SMF本地配置下发（非PCF下发） | SMF本地配置下发 |
| **消息跟踪建立** | 需在PCF/SMF/UPF三侧建立跟踪 | 仅需在SMF/UPF两侧建立跟踪 |
| **前提配置** | 需在PCF侧完成预定义规则配置 + UPCF PGW Web LMT开户签约 | 仅需在SMF侧完成本地PCC策略配置 |
| **用户上线APN** | 无特殊APN要求 | 正式上线前须调整终端上线APN为SMF本地PCC规则中绑定的目标APN |

### KP-04: N7接口与N4接口的信令映射（核心重点）

SM策略的执行链路为：PCF生成策略 → N7接口下发SMF → SMF转化 → N4接口下发UPF → UPF执行。信令映射的本质是确定N7接口"PccRules"信元内容与N4接口PDR/QER/FAR/URR的映射关系。

**N7接口消息（Npcf_SMPolicyControl_Create Response）关键信元**：

| 信元类别 | 信元名 | 说明 |
|---------|--------|------|
| 业务级QoS | pccRules | 流信息(flowInfos)、流控制(refTcData)、QoS(refQosData)、规则标识(pccRuleId)、规则优先级(precedence) |
| 会话级QoS | sessRules | 会话级5qi、arp、会话AMBR(authSessAmbr) |
| QoS定义 | qosDecs | 5qi、arp、maxbrUl/maxbrDl(MFBR) |
| 流控制 | traffContDecs | flowStatus(ENABLED/DISABLED等)、重定向信息(redirectInfo) |
| 计费定义 | chgDecs | 在线/离线计费、ratingGroup、meteringMethod |
| 触发器 | policyCtrlReqTriggers | PCF订阅的事件(US_RE/PLMN_CH/APP_STA等) |

**N4接口消息（PFCP Session Establishment Request）关键信元**：

| 信元 | 全称 | 必选性 | 作用 |
|------|------|--------|------|
| Create PDR | Packet Detection Rule | M(必选) | 流检测规则，由**流规则(PDI)** + **流动作**组成 |
| Create FAR | Forwarding Action Rule | M(必选) | 转发类动作：转发(forw)、丢弃(drop)、缓存(buff)、复制(dupl)等 |
| Create URR | Usage Reporting Rule | C(条件必选) | 统计上报类动作：流量统计、计费上报 |
| Create QER | QoS Enforcement Rule | C(条件必选) | QoS流控类动作：MFBR、GFBR等 |
| Create BAR | Buffering Action Rule | O(可选) | 缓存动作 |

### KP-05: N7到N4信令映射的三大数量关系

**PDR数量计算**：
- PDR数量 = N7接口所有PCC Rule中FlowInfos数量 x 流方向系数（单向流=1，双向流=2）
- 动态规则场景：一条PDR表示一条流策略，一个动态PCC Rule一般对应2个PDR（上行+下行）
- 预定义规则场景：PCF只下发预定义名称时，无论几个预定义规则，只生成**一对PDR**（双向）

**QER数量计算**：
- QER数量 = 指示Session-AMBR的QER（1个PDU Session对应1个）+ QFI对应的QER + PCC Rule自身对应的QER
- Session-AMBR的QER：一个PDU Session只有1个，所有Non-GBR QoS Flow的PDR都关联它
- QFI的QER：5QI+ARP相同的PCC Rule可复用同一个QFI QER
- PCC Rule自身的QER：每个PCC Rule须独立创建，即使QoS参数相同也不复用

**QFI数量计算**：
- QFI数量 = N7中5QI/ARP去重后的数量
- 前提：PCF下发策略优先级高于UDM签约默认策略

### KP-06: N7接口流策略到N4接口PDR的映射细节

PCF侧flowInfos中的`flowDirection`（BIDIRECTIONAL/UPLINK/DOWNLINK）决定PDR数量：
- 双向流：同时创建access(上行)和core(下行)两个PDR
- 单向流：只创建一个PDR

PDR中的`source-interface`信元：
- access(0) = 上行流
- core(1) = 下行流

PCF侧traffContDecs中的`flowStatus`映射到FAR的`apply-action`：
- ENABLED → forw=1(转发)
- DISABLED → drop=1(丢弃)
- 重定向 → forw=1 + redirection-information携带重定向地址

PCF侧qosDecs中的MFBR/GFBR映射到QER的对应字段。

**特别说明**：Session Rule（会话级规则）不单独生成PDR，即无PDR映射关系。

### KP-07: 业务拆解方法 — 单业务5步法

单业务拆解是将原始用户诉求转化为一个独立SM策略（动态PCC规则）的方法，分为5步：

1. **抽取**：将原始需求按"在XX条件下，实现XX控制"的逻辑拆解为多条"规则=条件+动作"语句。
   - 常见条件：用户签约信息(用户类别/状态/等级)、用户位置信息(小区/服务区/漫游)、用户上网时间(时段)、用户会话信息(配额状态/DNN)。
   - 常见动作：控制上下行带宽、建立专有QoS Flow、短信/邮件通知、重定向。
   - 注意：用户访问的"业务类别"不属于条件，属于动作组中的业务流识别。

2. **合并**：将动作相同或条件组相同的逻辑语句合并，简化策略关系。
   - 合并原则：**动作相同一定能合并**，但**条件相同不一定能合并**（动作互斥时不可合并）。

3. **排查**：排查条件完备性，确保覆盖用户上网行为的所有场景，避免边缘场景未覆盖导致用户无法正常上网。
   - 方法：分别计算每种条件类型是否覆盖全集（如配额未耗尽+耗尽=全部使用量状态）。

4. **规则类型判断**：根据是否涉及业务流识别（定向流量判断）选择规则类型。
   - 不涉及业务流识别 → 可使用动态规则（条件+动作全在PCF配置）
   - 涉及业务流识别 → 须使用预定义规则/规则组（规则名在PCF配置，规则内容在SMF/UPF侧配置，因UPCF不具备业务流识别能力）

5. **触发器选择**：配置触发器配合规则进行策略匹配。
   - IPCAN_EST：会话建立（5G所有策略须关联）
   - US_RE：使用量状态上报
   - 位置类：SAREA_CH、PRA_CH、SCELL_CH、PLMN_CH
   - 应用类：APP_STA、APP_STP
   - 时间类：TimeRangeChange

### KP-08: 业务拆解方法 — 多业务6步法

多业务拆解在单业务5步基础上增加第6步**业务关系判断**，对应套餐级配置（多个业务组合）。

**步骤1-5**：与单业务拆解相同，每个子业务独立完成抽取→合并→排查→规则类型→触发器。

**步骤6：业务关系判断**：确定各子业务之间的互斥关系。

互斥关系两大类型：
- **订购互斥**（订购时不允许同时订购）：
  - 订购+拒绝 / 订购+替换 / 订购+覆盖
  - 订购+有效期延长 / 订购+有效期合并
  - 订购+配额累积+余额 / 订购+配额累积+使用量
  - 订购+延迟删除时覆盖 / 订购+配额耗尽时覆盖
  - 组合型：有效期延长和配额累积等

- **激活互斥**（使用时不允许同时激活）：
  - 激活+拒绝（仅优先级高的激活）
  - 激活+替换（按优先级判断激活顺序）
  - 激活+失效时间 / 激活+配额复位时间 / 激活+订购时间
  - 组合型：失效时间和配额复位时间

### KP-09: 动态PCC策略配置 — 5G业务配置架构

5G动态规则配置的核心架构（UPCF WebUI）：

| 配置层级 | 参数 | 必选/可选 | 说明 |
|---------|------|----------|------|
| 套餐级 | Package | 可选 | 一个或多个业务组成，用户可直接签约 |
| 业务级 | Service | 必选 | 用户签约对象的最小粒度 |
| 策略级 | Policy | 必选 | 由一个或多个规则组成 |
| 规则级 | Rule | 必选 | 一条"If条件Then动作"逻辑 |

5G动作组必配内容（蓝色底纹）：
- **Arp**：抢占优先级、抢占能力、被抢占能力
- **Ambr**：会话级上下行最大比特率
- **DefaultQosInformation**：5qi + Arp引用
- **SessionRuleAction**：会话规则动作（缺省QoS Flow建立）
- **QoSData**：业务级QoS（5qi、maxbrUl、maxbrDl、arp）
- **FlowDescription** + **FlowInformation**：流描述和流方向
- **TcData**（TrafficControlData）：流状态控制
- **DynamicPccRule**：动态PCC规则标识（pccRuleId、precedence、refQosData等）
- **UsageMonitoringData**：配额监控键（关联配额时必须下发）

可选内容（灰色底纹）：配额（Quota），涉及流量扣减时必须配置。

### KP-10: 4G/5G业务配置关键差异

| 配置场景 | 4G | 5G |
|---------|-----|-----|
| **缺省承载/QoS Flow** | 至少配置DefaultBearerQoS + DynamicPccRule，QCI和ARP须相等 | 方法1：SessionRuleAction + DynamicPccRule，5QI和ARP须相等；**方法2（推荐）**：仅配置DynamicPccRule，5QI/ARP与用户上线请求一致 |
| **专有承载/QoS Flow** | 单独创建QCI或ARP不同的DynamicPccRule | 单独创建5QI或ARP不同的DynamicPccRule |
| **缺省QoS动作** | 直接在Action Group添加DefaultBearerQoS | 需在5G Action Group添加Arp + Ambr + DefaultQosInformation + SessionRuleAction |
| **动态规则动作** | QoSAction + ChargingAction + Service Flow（流过滤器） | Arp + QoSData + FlowDescription + FlowInformation + TcData + DynamicPccRule（共7个动作类型） |
| **预定义规则** | 规则页面选择"Predefined"类型，输入PCEF侧规则名 | 5G Action Group中的PredefinedPccRule动作，PccRuleId填入SMF侧规则名 |
| **条件组Object** | IPSession（Gx会话参数） | SmfSession（N7会话参数） |
| **策略类型** | Gx Policy | N7 Policy |

---

## 3. 配置调测要点

### 3.1 预定义规则/规则组调测 — 信令调测法（6步）

**前提条件**：已完成预定义规则配置 + UDM开户签约 + UPCF PGW Web LMT签约业务。

**步骤**：

1. **建立消息跟踪**：在PCF/SMF/UPF三侧分别建立用户消息跟踪（PCF选N7接口）。
2. **用户上线**：打开终端移动数据开关。
3. **观察PCF侧信令**：
   - 初始下发：检查"Npcf_SMPolicyControl_Create Response"中pccRules的pccRuleId是否为预定义规则名。
   - PCF发起更新：检查"Npcf_SMPolicyControl_UpdateNotify Request"中新旧规则名的增删。
   - SMF发起上报：检查"Npcf_SMPolicyControl_Update Request"中触发器名称和事件内容。
4. **观察SMF/UPF侧信令**：
   - 初始下发：检查"PFCP Session Establishment Request"中`activate-Predefined-Rules`信元值是否与PCF下发的规则名一致。URR-ID取值为"1"表示下发的是预定义规则。
   - PCF发起更新：检查"PFCP Session Modification Request"中规则名变更。
   - UPF发起上报：检查"PFCP Session Report Request"中事件上报内容。

**关键检查信元**：
- PCF侧码流：`pccRuleId`（预定义规则名）、`policyCtrlReqTriggers`（触发器）、`sessRules`中的5qi/arp/AMBR
- N4侧码流：`activate-Predefined-Rules`（激活的预定义规则名）、`urr-id`（取值1=预定义规则）、`measurement-method`（计量方式）、`reporting-triggers`（上报触发条件）

### 3.2 预定义规则/规则组调测 — 快速调测法（6步）

1. **检查用户签约**：登录UPCF PGW Web LMT，执行`LST PSRV`查询签约业务名。
2. **用户上线**：打开移动数据开关，保持在线。
3. **检查SMF本地规则安装**：执行`DSP PCCSESSINFO`查询SMF本地安装的规则是否与PCF下发一致。
4. **检查SMF会话QoS**：执行`DSP SESSIONQOSINFO`查询协商QoS（重点比较协商值与SMF配置值，排除UDM签约默认值干扰可将UDM签约值改大）。
5. **检查UPF用户QoS上下文**：在UDG执行`DSP SESSIONINFO`查询会话信息（Common Policy Name、PDR/FAR/URR/QER ID及参数、Rule information中激活的预定义规则名）。
6. **检查终端业务体验**：用Speedtest等工具测速验证实际带宽与策略定义一致。

**SMF配置查询顺序**：`LST USERPROFILE` → `LST RULEBINDING` → `LST RULE` → `LST PCCPOLICYGRP` → `LST QOSPROP`

### 3.3 本地PCC策略调测 — 信令调测法（4步）

**前提条件**：已完成本地PCC策略配置（SMF侧） + UDM开户签约。**不涉及PCF**。

1. **建立消息跟踪**：仅在SMF/UPF两侧建立用户消息跟踪。
2. **用户上线**：打开移动数据开关（**需先调整终端上线APN为SMF本地PCC规则绑定的目标APN**）。
3. **观察SMF/UPF侧信令**：
   - 初始下发：SMF通过"PFCP Session Establishment Request"下发策略。码流中`activate-Predefined-Rules`携带本地规则名。
   - SMF发起更新：通过"PFCP Session Modification Request"更新规则名。
   - UPF发起上报：通过"PFCP Session Report Request"上报事件。

### 3.4 本地PCC策略调测 — 快速调测法（5步）

1. **用户上线**：调整终端APN为目标APN后上线。
2. **检查SMF本地规则激活**：执行`DSP PCCSESSINFO`查询规则名。
3. **检查SMF会话QoS**：执行`DSP SESSIONQOSINFO`，协商5QI/ARP为SMF本地配置值，协商AMBR取SMF配置与UDM签约值的最小值。
4. **检查UPF用户QoS上下文**：在UDG执行`DSP SESSIONINFO`查询。
5. **（非必选）终端测速验证**。

### 3.5 N7/N4信令映射关键信元对照表

| N7接口信元（PCF→SMF） | N4接口信元（SMF→UPF） | 映射关系说明 |
|----------------------|----------------------|-------------|
| pccRules.pccRuleId（动态规则名） | PDR中不携带规则名 | 动态规则场景下SMF仅下发QoS参数，不下发规则名 |
| pccRules.pccRuleId（预定义规则名） | PDR的`activate-Predefined-Rules` | SMF将预定义规则名直接传给UPF激活 |
| pccRules.flowInfos.flowDirection | PDR的`source-interface` | access(0)=上行, core(1)=下行; 双向流同时创建两个PDR |
| pccRules.flowInfos.flowDescription | PDR PDI中的`sdf-filter`的`flow-description` | 流过滤描述直接映射 |
| pccRules.precedence | PDR的`precedence` | 规则优先级保持一致 |
| traffContDecs.flowStatus | FAR的`apply-action` | ENABLED→forw=1, DISABLED→drop=1 |
| traffContDecs.redirectInfo | FAR的`redirection-information` | 重定向地址类型和地址直接映射 |
| qosDecs(5qi, maxbrUl/Dl) | QER的QoS参数 | MFBR映射到QER的对应速率字段 |
| sessRules.authSessAmbr | Session-AMBR对应的QER（1个PDU Session 1个） | 所有Non-GBR QoS Flow的PDR关联此QER |
| qosDecs(5qi, arp) | QFI对应的QER | 5QI+ARP去重后生成QFI，相同参数复用QER |
| chgDecs | URR的计费参数 | 计费策略映射到URR的measurement-method、reporting-triggers |
| policyCtrlReqTriggers(US_RE) | URR的reporting-triggers(volth/timth) | 使用量上报触发器映射到URR的门限触发 |

### 3.6 业务拆解决策树

```
原始需求
  │
  ├─ 是否包含业务流识别（定向流量）？
  │    ├─ 是 → 使用预定义规则/规则组（规则名在PCF配置，内容在SMF/UPF配置）
  │    └─ 否 → 使用动态规则（条件+动作全在PCF配置）
  │              │
  │              ├─ 是否需要创建缺省QoS Flow？
  │    │    ├─ 是 → 方法1：SessionRuleAction + DynamicPccRule（5QI/ARP须相等）
  │    │    └─ 否（推荐方法2）→ 仅DynamicPccRule（5QI/ARP与用户上线请求一致）
  │              │
  │              └─ 是否需要专有QoS Flow？
  │                   └─ 是 → 创建5QI或ARP与缺省不同的DynamicPccRule
  │
  ├─ 是否涉及多个业务组合（套餐级）？
  │    ├─ 是 → 多业务6步法：增加业务关系判断（订购互斥/激活互斥）
  │    └─ 否 → 单业务5步法
  │
  └─ 触发器选择
       ├─ IPCAN_EST（必配，会话建立触发策略计算）
       ├─ US_RE（配额监控场景必配）
       ├─ 位置类（PLMN_CH/SAREA_CH/SCELL_CH/PRA_CH，位置相关场景配置）
       ├─ 应用类（APP_STA/APP_STP，应用感知场景配置）
       └─ 时间类（TimeRangeChange，分时段策略场景配置）
```

---

## 4. 与带宽控制的关系

这批文档描述的SM策略调测方法和业务拆解配置是**带宽控制场景的方法论基础**：

1. **调测方法是验证带宽控制配置正确性的工具**：
   - 带宽控制的核心是PCC规则中的QoS参数（MFBR上下行最大速率、Session-AMBR会话级带宽）。
   - 信令调测法通过N7/N4接口信令码流逐信元验证带宽参数是否从PCF正确传递到SMF再到UPF。
   - 快速调测法通过`DSP SESSIONQOSINFO`和`DSP SESSIONINFO`命令验证协商后的实际带宽值，并通过Speedtest等工具验证终端实际体验。
   - 特别注意：协商类上下行比特率取值为**用户在UDM签约值与SMF/PCF下发值中的较小值**，调测时需排除UDM签约默认值的干扰。

2. **业务拆解是把带宽控制需求转化为PCC规则的方法**：
   - 带宽控制的典型场景（如FUP用量阈值降速、分时段限速、套餐配额耗尽限速）都需要通过业务拆解转化为具体的PCC规则。
   - 抽取阶段：将"配额未耗尽时40Mbit/s，耗尽时10Mbit/s"这类需求拆解为条件（配额状态）+动作（带宽控制）。
   - 合并阶段：将相同带宽动作的条件合并，简化策略。
   - 规则类型判断：带宽控制本身不需要业务流识别，可使用动态规则；但若需要定向限速（如只对视频流量限速），则需预定义规则。

3. **N7/N4信令映射是带宽控制策略下发执行的完整链路**：
   - PCF生成的带宽控制策略通过N7接口的pccRules/qosDecs信元下发（maxbrUl/maxbrDl）。
   - SMF转化为N4接口的QER信元下发UPF执行。
   - Session-AMBR对应一个Session级QER，所有Non-GBR Flow共享。
   - PCC Rule自身的MFBR/GFBR对应独立的QER，每规则一个。
   - 带宽限制最终在UPF侧通过QER的Gate状态（Open/Closed）和速率参数执行。

4. **本地PCC策略是带宽控制的简化实现路径**：
   - 不经过PCF，SMF直接根据APN匹配激活本地预定义规则，实现带宽控制。
   - 适用于不需要动态策略决策的固定带宽控制场景。

---

## 5. 关键术语

| 术语 | 简释 |
|------|------|
| **PCC（Policy and Charging Control）** | 策略与计费控制架构，实现业务流级别的QoS控制和计费 |
| **SM策略（Session Management Policy）** | 会话管理策略，PCF生成、SMF转发、UPF执行，控制PDU会话的QoS和流量 |
| **动态规则（Dynamic Rule）** | PCF配置生成完整规则内容（条件+动作），经SMF下发的PCC规则 |
| **预定义规则（Predefined Rule）** | PCF仅下发规则名，规则内容（QoS/流动作等）在SMF/UPF侧预配置 |
| **预定义规则组（Predefined Rule Group）** | 通过User Profile绑定的多个预定义规则的集合 |
| **本地规则（Local Rule）** | SMF本地配置生成，不涉及PCF，根据APN等条件直接激活 |
| **PDR（Packet Detection Rule）** | N4接口流检测规则，由流匹配条件(PDI)和流动作组成 |
| **FAR（Forwarding Action Rule）** | N4接口转发动作规则，控制流量转发/丢弃/缓存/重定向 |
| **QER（QoS Enforcement Rule）** | N4接口QoS执行规则，控制MFBR/GFBR/Session-AMBR |
| **URR（Usage Reporting Rule）** | N4接口使用量上报规则，控制流量统计和计费上报 |
| **PFCP（Packet Forwarding Control Protocol）** | N4接口协议，SMF与UPF之间的控制面信令协议 |
| **N7接口** | PCF与SMF之间的接口，传递SM策略 |
| **N4接口** | SMF与UPF之间的接口，传递PFCP会话管理信令 |
| **5QI（5G QoS Identifier）** | 5G QoS标识，对应一组QoS参数（速率、延迟、丢包率等） |
| **AMBR（Aggregate Maximum Bit Rate）** | 聚合最大比特率，Session-AMBR限制PDU会话所有Non-GBR Flow的总带宽 |
| **MFBR（Maximum Flow Bit Rate）** | 最大流比特率，限制单条QoS Flow的上下行最大速率 |
| **GFBR（Guaranteed Flow Bit Rate）** | 保证流比特率，GBR类型QoS Flow的保证速率 |
| **触发器（Trigger）** | PCF订阅的事件类型，如US_RE(使用量上报)、PLMN_CH(PLMN变更)等 |
| **互斥组** | UPCF中定义的业务间互斥关系（订购互斥/激活互斥），用于套餐级多业务管理 |
| **QoS Flow** | 5G中QoS管理的最小粒度，由5QI+ARP唯一标识 |
| **UPCF** | 华为策略控制功能网元产品（对应3GPP PCF） |
| **UNC** | 华为会话管理功能网元产品（对应3GPP SMF） |
| **UDG** | 华为用户面功能网元产品（对应3GPP UPF） |

---

## 6. 知识来源

| 序号 | 源文件名 | 内容主题 |
|------|---------|---------|
| 1 | 信令调测法_67363127.md | 预定义规则/预定义规则组调测 — 信令调测法 |
| 2 | 快速调测法_67920177.md | 预定义规则/预定义规则组调测 — 快速调测法 |
| 3 | 信令调测法_67482083.md | 本地PCC策略调测 — 信令调测法 |
| 4 | 快速调测法_21200422.md | 本地PCC策略调测 — 快速调测法 |
| 5 | N7接口与N4接口的信令映射_30975312.md | N7/N4接口信令映射关系（核心重点） |
| 6 | 调测方法概述_77134835.md | 调测方法概述（三种规则类型调测关注点） |
| 7 | 单业务拆解方法_24232010.md | 单业务场景拆解方法（5步法） |
| 8 | 多业务拆解方法_70951751.md | 多业务场景拆解方法（6步法） |
| 9 | 业务配置逻辑_64569729.md | 动态PCC策略配置 — 业务配置逻辑与4G/5G差异 |
| 10 | 概述_64489687.md | 动态规则配置概述（实现网元说明） |

**原始路径前缀**：`output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/业务专题/5G PCC之SM策略解决方案/SM策略配置与调测/`
