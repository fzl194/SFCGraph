# Batch-30: UNC E2E方案 - 用户等级资费差异化与SM策略总览

## 1. 概述

本批次涵盖来自UNC侧"5G PCC之SM策略解决方案"业务专题的9篇文档，内容可归为三大主题模块：

**模块一：SM策略解决方案纲领性文档（3篇）**
- SM策略整体介绍：定位SM策略在5G PCC架构中的角色，说明SM策略的QoS控制、计费参数、短信/重定向三大内容组成，梳理PCF/SMF/UDM/AMF/UPF/RAN六大网元职责。
- 遵循标准：列出SM策略实现所遵循的3GPP标准协议清单（TS 23.501系列、TS 23.203、TS 23.107等）。
- 阅读指引：提供整个"5G PCC之SM策略解决方案"专题的文档结构导览图。

**模块二：基于用户等级的资费差异化控制方案（动态）E2E方案（5篇）**
- 需求描述：不同用户等级（金牌/银牌/普通）对应不同费率和上下行带宽。
- 整体方案设计：业务拆解逻辑（抽取-合并-排查-规则类型判断-触发器选择），PCF侧业务设计。
- PCF侧业务配置：条件组、5G动作组、规则、策略、业务的完整配置步骤及MML开户脚本。
- 信令调测方法：基于网元间信令交互的详细调测流程。
- 快速调测方法：通过MML命令快速验证PCC策略下发与执行是否符合预期。

**模块三：多业务场景策略控制需求（1篇）**
- 基于多业务场景的策略控制（动态）需求描述：以假期流量包套餐为例，说明包月流量+假期流量包的多业务场景下的配额使用优先级、带宽差异化和配额耗尽行为。

这9篇文档共同构成了SM策略从"整体介绍"到"E2E方案落地"的完整知识链，其中用户等级资费差异化方案是SM策略在"按用户等级差异化"维度的典型E2E实现案例。

---

## 2. 核心知识点

### KP-01: SM策略在5G PCC架构中的定位

5G PCC架构定义了三种策略：SM策略、AM策略、UE策略。

| 策略类型 | 全称 | 核心职责 |
|----------|------|----------|
| SM策略 | Session Management策略 | 差异化QoS服务：灵活带宽控制、网络资源使用优先级、计费方式 |
| AM策略 | Access and Mobility策略 | 用户接入控制、用户级带宽统一控制（5G新引入） |
| UE策略 | User Equipment策略 | 辅助终端选择切片资源、网络、PDU会话类型（5G新引入） |

与4G PCC架构相比，5G新增了AM策略和UE策略两种类型。SM策略对应4G中的PCC策略功能，但能力更为丰富。

### KP-02: SM策略下发组网与网元职责

SM策略下发涉及6个核心网元：

| 网元 | 在SM策略中的职责 |
|------|------------------|
| PCF | 拥有PCC策略最高决策权，决定下发策略内容；若PCF未下发，SMF按本地配置决定 |
| SMF | 处理PCF下发的SM Policy，根据QoS参数和业务信息确定QoS Flow，控制其建立/修改/删除 |
| UDM | 用户数据签约，分配默认QoS Flow的ARP/5QI，提供Session-AMBR和UE-AMBR |
| AMF | 对信令建立提供通道，信息透传 |
| UPF | SM策略执行网元，处理SMF的PFS和QoS信息，下行QFI标记和控制，上行QFI验证 |
| RAN | 处理信令面策略内容，将QoS参数映射到用户面，实现空口QoS控制 |

### KP-03: SM策略的三大内容组成

SM策略主要包含以下三方面内容：

1. **QoS控制**：对UE访问DN网络使用的带宽（Session-AMBR、MBR）、用户在无线侧的调度优先级（ARP、5QI）等进行控制。
2. **计费参数**：对UE访问不同应用类型、不同套餐余量、不同上网位置区域等进行差异化资费控制（Rating Group、Service ID、在线/离线计费）。
3. **短信或重定向**：对UE不同套餐余量变更、上网位置区域变更、漫游状态等进行短信通知或网页重定向（如重定向到充值页面）。

### KP-04: SM策略遵循的3GPP标准

SM策略的QoS和PCC实现遵循以下3GPP标准：

**QoS相关标准（TS 23.501系列）：**
- TS 23.501 5.7.1: QoS总览（QoS Flow、QoS属性、AMBR/MFBR等概念）
- TS 23.501 5.7.2: QoS参数（5QI、ARP、RQA、FBR、ABR、MPLR等）
- TS 23.501 5.7.3: QoS特征
- TS 23.501 5.7.4: 标准化5QI到QoS特征的映射
- TS 23.501 5.7.5: 反射式QoS
- TS 23.501 5.7.6: 包过滤集（Packet Filter Set）

**PCC架构与信令标准：**
- TS 23.107: QoS概念和应用架构
- TS 23.203: PCC架构定义
- TS 23.207: 端到端QoS概念和应用架构
- TS 29.208: 端到端QoS消息流程
- TS 29.211: Rx接口和Rx/Gx信令流程
- TS 29.212: Gx接口上的PCC应用
- TS 29.213: PCC信令流程和QoS参数映射
- TS 29.214: Rx接口上的PCC应用

### KP-05: 基于用户等级的资费差异化需求模型

该E2E方案的核心需求是：用户等级越高，计费费率越高，同时享受更高的带宽。

| 用户等级 | 费率 | 上下行带宽 |
|----------|------|------------|
| 金牌用户（Gold） | A | 100 Mbps |
| 银牌用户（Silver） | B | 50 Mbps |
| 普通用户（Normal） | C | 10 Mbps |

关键特征：
- 不涉及消息通知（与重定向/短信方案不同）。
- 使用**动态规则**配置方法（PCF动态下发PCC Rule到SMF/UPF，SMF/UPF侧无需预配置）。
- 金牌+银牌+普通=全部用户等级，场景条件完备。

### KP-06: 业务拆解方法论（抽取-合并-排查-判类型-选触发器）

整体方案设计给出了标准化的SM策略业务拆解五步法：

1. **抽取**：将需求按"在XX条件下，实现XX控制"的逻辑抽取。本场景条件为用户等级（Gold/Silver/Normal）。
2. **合并**：将"动作"相同或"条件组"相同的逻辑语句合并。本场景中费率和带宽绑定同一条件，可合并为三条规则。
3. **排查**：检查条件完备性，确认无边缘场景遗漏。
4. **规则类型判断**：根据动作类型选择动态规则或静态（预定义）规则。本场景使用动态规则。
5. **选择触发器**：
   - IPCAN_EST触发器：用户从N7接口上线时触发PCF策略计算。
   - 用户等级变更：由业务发放系统（营帐侧）修改变更，变更后通过订阅通知触发UPCF主动更新策略，无需配置额外触发器。

### KP-07: PCF侧业务配置层次（条件组>动作组>规则>策略>业务）

UPCF业务配置遵循严格的层次引用关系：

```
业务（Usr_Category_Service）
  └── 策略（Policy_Category, N7 Policy）
        ├── 触发器（IPCAN_EST）
        ├── 规则1（Rule_Gold）── 条件组: CG_Gold ── 动作组: AG_Gold
        ├── 规则2（Rule_Silver）── 条件组: CG_Silver ── 动作组: AG_Silver
        └── 规则3（Rule_Normal）── 条件组: CG_Normal ── 动作组: AG_Normal
```

每个5G动作组（DynamicPccRule类型）引用多个子动作：
- **FlowDescription + FlowInformation**：流描述和流信息（permit out ip from any to any, BIDIRECTIONAL）
- **TrafficControlData**：门限控制（flowStatus=ENABLED，表示放通）
- **QoSData**：带宽控制（maxbrUl/maxbrDl按等级区分）
- **ChargingData**：计费控制（ratingGroup/serviceId按等级区分）
- **Arp**：ARP参数（取用户上线请求的值，即SmfSession.SubsDefQos*）

### KP-08: 多业务场景策略控制需求（假期流量包案例）

多业务场景的策略控制需求描述了更复杂的业务组合：

**场景一（包月流量）：**
- 每月10GB，配额未耗尽时上下行10 Mbps。
- 配额耗尽后短信通知并限速到1 Mbps。

**场景二（假期流量包）：**
- 20GB，仅周末可用，配额未耗尽时上下行100 Mbps。
- 配额耗尽后终止使用并通知用户。

**资源使用优先级：**
- 周末上网时，优先使用假期流量包（场景二），耗尽后再使用包月套餐（场景一）。

此需求展示了SM策略在多业务叠加、配额优先级管理、差异化带宽控制方面的综合能力。

### KP-09: 信令调测方法论

信令调测以用户消息跟踪为基础，关注三个维度：
- **策略内容验证完备性**：动作组下发时须满足的"条件"场景需全量覆盖测试。
- **消息流程正确性**：策略下发、执行、更新、事件上报等消息流程符合协议要求。
- **消息内容正确性**：策略下发消息携带内容与策略逻辑定义一致。

调测关键路径：PCF侧Npcf_SMPolicyControl接口 -> SMF侧N4 PFCP接口 -> UPF侧策略执行。

### KP-10: 快速调测验证链条

快速调测提供了一套基于MML命令的端到端验证方法，验证链条为：

1. UPCF PGW Web LMT验证签约（LST PSRV）和用户等级（LST PSUB）
2. SMF侧验证动态规则安装（DSP PCCSESSINFO）
3. SMF侧验证QoS参数（DSP SESSIONQOSINFO）
4. SMF侧验证计费参数（DSP CPPDPCHGINFO / DSP PDUSESSION）
5. UPF侧验证QoS上下文（DSP SESSIONINFO）
6. 终端实测体验验证（测速软件验证实际带宽）

---

## 3. 配置调测要点

### 3.1 用户等级资费差异化PCF侧配置清单

**条件组配置（3个）：**

| 条件组 | 条件对象.属性 | 操作符 | 右值 |
|--------|---------------|--------|------|
| CG_Gold | Subscriber.Category | Equal | Gold |
| CG_Silver | Subscriber.Category | Equal | Silver |
| CG_Normal | Subscriber.Category | Equal | Normal |

> 右值须与UPCF PGW Web LMT上ADD PSUB命令开户的"用户类别"一致。

**5G动作组配置（13个，按层级）：**

| 动作组 | 类型 | 关键参数 |
|--------|------|----------|
| AG_FlowDesc | FlowDescription | PERMIT, OUT, ANY, any, any |
| AG_FlowInfo | FlowInformation | 引用AG_FlowDesc, BIDIRECTIONAL |
| AG_TraCtrl | TrafficControlData | tcId=AG_TraCtrl, flowStatus=ENABLED |
| AG_arp | Arp | 引用SmfSession.SubsDefQos*（取用户上线请求值） |
| AG_Qos_Gold | QoSData | maxbrUl/Dl=100 Mbps, 5qi取SubsDefQos5qi |
| AG_Qos_Silver | QoSData | maxbrUl/Dl=50 Mbps, 5qi取SubsDefQos5qi |
| AG_Qos_Normal | QoSData | maxbrUl/Dl=10 Mbps, 5qi取SubsDefQos5qi |
| AG_ChargingData_Gold | ChargingData | ratingGroup=11, serviceId=11, offline=True |
| AG_ChargingData_Silver | ChargingData | ratingGroup=22, serviceId=22, offline=True |
| AG_ChargingData_Normal | ChargingData | ratingGroup=33, serviceId=33, offline=True |
| AG_Gold | DynamicPccRule | 引用AG_FlowInfo+AG_Qos_Gold+AG_TraCtrl+AG_ChargingData_Gold |
| AG_Silver | DynamicPccRule | 引用AG_FlowInfo+AG_Qos_Silver+AG_TraCtrl+AG_ChargingData_Silver |
| AG_Normal | DynamicPccRule | 引用AG_FlowInfo+AG_Qos_Normal+AG_TraCtrl+AG_ChargingData_Normal |

**规则配置（3个）：** Rule_Gold/Rule_Silver/Rule_Normal，操作类型Change Rule，类型5G Smf Pcc Rule。

**策略配置（1个）：** Policy_Category，类型N7 Policy，触发器IPCAN_EST，关联3条规则。

**业务配置（1个）：** Usr_Category_Service，类型VALUE_ADDED_SERVICE，激活方式PCEF，QoS模式替换。

### 3.2 开户与签约MML命令

```
// 增加金牌用户
ADD PSUB: USRIDENTIFIER="46000120010****", USRMSISDN="861390010****", USRSTATE=Normal, USRPAIDTYPE=NULL, USRCATEGORY="Gold", USRSTATION=Master, USRCONTACTMETHOD=SMS, USRBILLCYCLEDATE=NULL, USRSUBNETTYPE=eMBB-SA, USRLANGUAGE=NULL, USRSMSRECEIVEFLAG=All, USRVERSTATUS=Normal;

// 签约业务
ADD PSRV: USRIDENTIFIER="46000120010****", SRVNAME="Usr_Category_Service", SRVUSAGESTATE=Normal, SRVROAMINGTYPE=NULL;

// 修改用户等级
MOD PSUB: USRIDENTIFIER="46000120010****", USRCONTACTMETHOD=SMS, USRCATEGORY="Silver";
```

### 3.3 调测验证MML命令

| 验证目标 | 网元 | MML命令 | 关键检查点 |
|----------|------|---------|------------|
| 签约检查 | UPCF | LST PSRV | 业务名为Usr_Category_Service |
| 用户等级 | UPCF | LST PSUB | USRCATEGORY=Gold/Silver/Normal |
| 动态规则安装 | SMF | DSP PCCSESSINFO | pccRuleId=AG_Gold等, RuleSource=PCF created |
| 会话QoS | SMF | DSP SESSIONQOSINFO | Subscribed QoS 5QI, ARP |
| 计费参数 | SMF | DSP CPPDPCHGINFO | Rating Group=11(Gold)/22(Silver)/33(Normal) |
| PDU会话详情 | SMF | DSP PDUSESSION | 计费ID, Session AMBR |
| UPF上下文 | UPF | DSP SESSIONINFO | QER MBR, URR计费规则 |

### 3.4 信令调测详细流程

信令调测在PCF/SMF/UPF三个网元上分别建立消息跟踪任务，完整观察策略下发与执行过程。

**步骤1：用户签约检查**
- 登录UPCF PGW Web LMT，执行LST PSRV确认用户已签约"Usr_Category_Service"业务。
- 执行LST PSUB确认USRCATEGORY取值。

**步骤2：设置用户等级并上线**
- 执行MOD PSUB修改用户等级为目标值（如Gold）。
- 用户打开移动数据开关，发起PDU会话建立请求。

**步骤3：观察PCF侧信令（初始下发）**
用户PDU会话建立请求经SMF送到PCF后，PCF侧消息跟踪流程：
1. SMF -> PCF: Npcf_SMPolicyControl_Create Request
   - 携带：IMSI/MSISDN、dnn、接入网络类型、切片信息（S-NSSAI）
2. PCF查询本地签约，匹配用户等级条件，生成策略决策
3. PCF -> SMF: Npcf_SMPolicyControl_Create Response
   - 携带动态规则（如AG_Gold）、触发器、会话级QoS
   - 策略内容示例（金牌用户）：

```json
{
  "pccRules": {
    "AG_Gold": {
      "pccRuleId": "AG_Gold",
      "precedence": 1,
      "refChgData": ["AG_ChargingData_Gold"],
      "refQosData": ["AG_Qos_Gold"],
      "refTcData": ["AG_TraCtrl"],
      "flowInfos": [{
        "flowDescription": "permit out ip from any to any",
        "flowDirection": "BIDIRECTIONAL"
      }]
    }
  },
  "qosDecs": {
    "AG_Qos_Gold": {
      "5qi": 9,
      "arp": {"preemptCap": "NOT_PREEMPT", "preemptVuln": "PREEMPTABLE", "priorityLevel": 1},
      "maxbrDl": "100000000 bps",
      "maxbrUl": "100000000 bps"
    }
  },
  "chgDecs": {
    "AG_ChargingData_Gold": {
      "meteringMethod": "VOLUME",
      "offline": true, "online": false,
      "ratingGroup": 11, "serviceId": 11
    }
  },
  "sessRules": {
    "defaultSessionRuleId": {
      "authDefQos": {"5qi": 9, "arp": {"priorityLevel": 1, "preemptCap": "NOT_PREEMPT", "preemptVuln": "PREEMPTABLE"}},
      "authSessAmbr": {"downlink": "2000000000 bps", "uplink": "2000000000 bps"}
    }
  }
}
```

**步骤4：观察SMF/UPF侧信令（初始下发）**
- SMF收到PCF策略后，通过N4接口PFCP Session Establishment Request下发给UPF。
- PFCP消息中携带：Create PDR（报文检测规则）、Create FAR（转发动作规则）、Create URR（使用量上报规则）、Create QER（QoS执行规则）。
- URR ID=0表示下发的是动态规则；URR ID=1表示预定义规则。

**步骤5：观察PCF发起的会话更新（用户等级变更）**
当PCF侧修改用户等级为Silver或Normal后：
1. 营帐系统 -> UPCF: 订阅通知触发
2. PCF -> SMF: Npcf_SMPolicyControl_UpdateNotify Request（更新策略内容）
3. SMF -> UPF: PFCP Session Modification Request（更新QER的MBR等参数）
4. UPF基于更新后的策略内容执行新的QoS控制

### 3.5 快速调测验证详解

快速调测提供端到端的MML命令验证链条，逐级检查策略下发与执行的正确性。

**验证链条（以金牌用户为例）：**

| 步骤 | 网元 | 验证内容 | 预期结果 |
|------|------|----------|----------|
| 1 | UPCF | LST PSRV查询签约 | 业务名=Usr_Category_Service |
| 2 | UPCF | MOD PSUB设置Gold + LST PSUB确认 | USRCATEGORY=Gold |
| 3 | SMF | DSP PCCSESSINFO查询PCC会话 | RuleName=AG_Gold, RuleSource=PCF created |
| 4 | SMF | DSP SESSIONQOSINFO查询会话QoS | Subscribed QoS 5QI=9, ARP PriorityLevel=1 |
| 5 | SMF | DSP CPPDPCHGINFO查询计费参数 | Rating Group=11, ChargingType=Prepaid |
| 6 | SMF | DSP PDUSESSION查询PDU会话详情 | 计费ID、Session AMBR |
| 7 | UPF | DSP SESSIONINFO查询用户上下文 | QER Uplink/Downlink MBR=100 Mbps(金牌) |
| 8 | 终端 | 测速软件实测 | 实际最高网速约等于100 Mbps |

**UPF侧QER验证关键数据（金牌用户示例）：**
- QER Type=Service: Uplink MBR=50000kbps, Downlink MBR=50000kbps（业务级QoS）
- QER Type=APN Session: Uplink MBR=2000000kbps, Downlink MBR=2000000kbps（会话级QoS）
- URR: Measurement Method=Duration+Volume, Reporting Triggers=Volume Threshold+Time Threshold

**银牌/普通用户验证：**
修改用户等级为Silver/Normal后，重复步骤3-8，验证下发的规则分别为AG_Silver/AG_Normal，对应带宽为50/10 Mbps。

### 3.5 3GPP标准遵循要点

SM策略配置调测中涉及的关键3GPP标准映射：
- **QoS参数定义**：遵循TS 23.501 5.7.2（5QI、ARP、Session-AMBR、MBR）
- **PCC架构**：遵循TS 23.203（PCF/SMF/UPF之间的策略交互架构）
- **Gx接口**：TS 29.212（对应5G中PCF与SMF之间的Npcf_SMPolicyControl接口）
- **QoS特征映射**：TS 23.501 5.7.4（5QI=9对应Non-GBR默认QoS Flow）

---

## 4. 与带宽控制的关系

### 4.1 用户等级资费差异化中的带宽控制

用户等级资费差异化方案是SM策略在"按用户等级差异化"维度的典型E2E实现，其中**带宽控制是核心动作之一**：

- 金牌用户：上下行100 Mbps（maxbrUl=maxbrDl=100 Mbps）
- 银牌用户：上下行50 Mbps（maxbrUl=maxbrDl=50 Mbps）
- 普通用户：上下行10 Mbps（maxbrUl=maxbrDl=10 Mbps）

带宽控制的实现机制：
- PCF在QoSData动作中设置maxbrUl/maxbrDl参数。
- SMF收到后通过PFCP Session Establishment Request下发到UPF。
- UPF在QER（QoS Enforcement Rule）中配置Uplink MBR和Downlink MBR。
- 快速调测中可通过DSP SESSIONINFO查询UPF侧QER的MBR值验证带宽控制是否生效。

### 4.2 SM策略整体介绍作为带宽控制方案的纲领

SM策略整体介绍文档确立了带宽控制在5G PCC架构中的理论框架：
- **QoS控制是SM策略的三大内容之一**，带宽控制是QoS控制的核心组成部分。
- 带宽参数（Session-AMBR、MBR）的定义遵循TS 23.501 5.7.1和5.7.2标准。
- PCF是带宽策略的最高决策者，SMF/UPF是执行者。

### 4.3 多业务场景的带宽控制特征

假期流量包案例展示了更复杂的带宽控制需求：
- 同一用户在不同业务下享受不同带宽（包月10 Mbps vs 假期包100 Mbps）。
- 配额耗尽后带宽降级（10 Mbps -> 1 Mbps）或业务终止。
- 多业务叠加时的优先级管理（周末优先使用假期包的高带宽）。

### 4.4 与本场景其他E2E方案中带宽控制的关系

用户等级资费差异化方案与本场景其他E2E方案（ADC带宽差异化、位置区域带宽控制等）共享同一套SM策略底层机制：
- 同样使用动态规则或预定义规则下发QoS参数。
- 同样通过PCF -> SMF -> UPF的策略下发链条执行。
- 区别在于**条件维度不同**（用户等级 vs 应用 vs 位置区域 vs 套餐余量）。
- 多个维度的带宽控制策略可在同一PCF业务中组合使用。

---

## 5. 关键术语

| 术语 | 简释 |
|------|------|
| SM策略 | Session Management策略，5G PCC架构中处理差异化QoS、计费和通知的策略类型 |
| PCC | Policy and Charging Control，策略与计费控制架构 |
| PCF | Policy Control Function，策略控制功能网元，PCC策略最高决策者 |
| UPCF | 华为对PCF的产品命名，Unified Policy Control Function |
| SMF | Session Management Function，会话管理功能网元 |
| UPF | User Plane Function，用户面功能网元，策略执行点 |
| UDM | Unified Data Management，统一数据管理网元，负责用户签约数据 |
| AMF | Access and Mobility Management Function，接入和移动性管理功能网元 |
| DynamicPccRule | 动态PCC规则，PCF运行时动态生成并下发到SMF/UPF的策略规则 |
| 预定义规则 | 静态PCC规则，预先配置在SMF/UPF本地的规则，由名称引用 |
| IPCAN_EST | IP-CAN Session Establishment触发器，用户N7接口上线时触发策略计算 |
| QoS Flow | 5G中的QoS流，是PDU会话内QoS控制的基本单位 |
| 5QI | 5G QoS Identifier，5G QoS标识符（如5QI=9对应Non-GBR默认QoS） |
| ARP | Allocation and Retention Priority，分配和保留优先级 |
| Session-AMBR | 会话级聚合最大比特速率 |
| MBR | Maximum Bit Rate，最大比特速率 |
| maxbrUl/maxbrDl | 上下行最大带宽参数，QoSData中的带宽控制字段 |
| Rating Group | 费率组，计费控制中标识费率的参数 |
| QER | QoS Enforcement Rule，UPF侧的QoS执行规则 |
| URR | Usage Reporting Rule，UPF侧的使用量上报规则 |
| PDR | Packet Detection Rule，UPF侧的报文检测规则 |
| FAR | Forwarding Action Rule，UPF侧的转发动作规则 |
| PFCP | Packet Forwarding Control Protocol，N4接口控制面协议 |
| N7接口 | PCF与SMF之间的SM策略控制接口（Npcf_SMPolicyControl） |
| N4接口 | SMF与UPF之间的接口（PFCP协议） |
| TRAFFICONTROLDATA | 门限控制数据动作，控制业务流的放通/阻断 |
| Subscriber.Category | 签约用户对象中的类别属性，用于区分用户等级 |
| ADD PSUB | UPCF PGW Web LMT中增加用户的MML命令 |
| ADD PSRV | UPCF PGW Web LMT中签约业务的MML命令 |
| MOD PSUB | UPCF PGW Web LMT中修改用户属性的MML命令 |
| DSP PCCSESSINFO | SMF侧查询PCC会话信息的MML命令 |
| DSP SESSIONINFO | UPF侧查询用户会话上下文的MML命令 |

---

## 6. 知识来源

| 序号 | 源文件 | 内容主题 |
|------|--------|----------|
| 1 | 需求描述_24058834.md | 多业务场景策略控制需求（假期流量包案例） |
| 2 | 信令调测方法_08571739.md | 用户等级资费差异化信令调测方法 |
| 3 | 快速调测方法_93907887.md | 用户等级资费差异化快速调测方法 |
| 4 | PCF侧业务配置_93906534.md | 用户等级资费差异化PCF侧业务配置步骤 |
| 5 | 整体方案设计_93907864.md | 用户等级资费差异化整体方案设计 |
| 6 | 需求描述_08571737.md | 用户等级资费差异化需求描述 |
| 7 | 整体介绍_86483627.md | SM策略解决方案整体介绍 |
| 8 | 遵循标准_11969175.md | SM策略遵循的3GPP标准清单 |
| 9 | 阅读指引_50304906.md | SM策略解决方案文档结构导览 |
