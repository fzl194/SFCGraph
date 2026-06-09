# GWFD-020351 PCC基本功能 知识文档

## 概述

### 定义

PCC（Policy and Charging Control）是策略和计费控制。PCC基本功能用于在用户的业务流程中实现UE策略、移动性策略、会话策略和计费控制，通过区分业务并进行实时QoS控制，合理利用网络资源，提升数据业务流量的经营价值，丰富数据业务市场营销手段。

### 适用NF

PGW-U、UPF。

### 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|----------|----------|----------|
| 01 | 20.0.0 | 首次发布。 |

### License要求

本特性只有获得了License许可后才能获得该特性的服务，对应的License控制项为：**82209825 LKV3G5PCCB01 PCC 基本功能**。

### 前置条件

- 完成业务感知配置。
- 完成加载License。
- PGW-U/UPF与PGW-C/SMF配合作为策略执行实体，PGW-C/SMF的配置参见UNC的初始配置手册和PCC基本功能的配置资料。

### 客户价值

| 受益方 | 受益描述 |
|--------|----------|
| 运营商 | 采用PCC基本功能，运营商可以在网络运营中进行统一的、多维度的策略部署和控制，包括实现业务级的QoS控制和计费、重定向、动态调整策略。在优化网络资源使用和提升网络用户体验的同时，提升管道的智能化水平，增强竞争力。 |
| 用户 | 终端用户可以选择更为多样化的资费方案；终端用户能够体会到更灵活的带宽控制带来的良好上网感受。 |

### 遵循标准

| 标准类别 | 标准编号 | 标准名称 |
|----------|----------|----------|
| 3GPP | 23501 v15.2.0 | System Architecture for the 5G System; Stage 2 |
| 3GPP | 23502 v15.2.0 | Procedures for the 5G System; Stage 2 |
| 3GPP | 23503 v15.2.0 | Policy and Charging Control Framework for the 5G System; Stage 2 |
| 3GPP | 29507 v15.2.0 | 5G System; Access and Mobility Policy Control Service; Stage 3 |
| 3GPP | 29512 v15.2.0 | 5G System; Session Management Policy Control Service; Stage 3 |
| 3GPP | 29513 v15.2.0 | 5G System; Policy and Charging Control signalling flows and QoS parameter mapping; Stage 3 |

---

## 核心概念

### PCC架构角色

PCC架构主要由以下功能实体组成：

| 功能角色 | 网元 | 功能说明 |
|----------|------|----------|
| 策略控制功能 | PCRF/PCF | 完成策略决策。提供基于业务的QoS策略、计费规则，绑定AF会话。包含会话管理相关功能和非会话管理相关功能。 |
| 策略控制执行功能 | PGW-C/SMF | 根据从PCRF/PCF收到的会话管理策略，将SDF与QoS流绑定；进行QoS、计费、门控、包路由和转发、流量转向等策略决策；执行计费控制，向CHF上报话单。未部署PCRF/PCF时，根据本地配置策略进行会话策略控制。 |
| 用户面策略执行 | PGW-U/UPF | 根据PGW-C/SMF传递的PCC策略，执行业务数据流检测、统计业务流量/时长等使用量、执行流量上报、QoS控制、带宽管理、重定向等策略控制。 |
| 接入和移动策略执行 | AMF | 执行接入和移动性策略。 |
| 业务策略提供功能 | AF | 应用功能实体，可由运营商或第三方业务提供商提供。向PCRF/PCF传送应用级别的会话信息；向PCRF/PCF订阅PDU会话事件通知以及DNAI改变通知。 |
| 用户签约数据存储 | SPR/UDR | 存储用户信息和业务签约信息，为PCF提供策略决策所需的签约输入。 |

### PCRF/PCF功能详解

**会话管理相关功能：**
- 对SDF的策略和计费控制：完成策略授权，为PCC规则选择QoS参数，并向PGW-C/SMF下发规则。
- PDU会话相关策略控制：将AF会话信息和适用的PCC规则关联到一个PDU会话上。
- 向AF上报PDU会话事件：根据AF的请求向AF上报接入类型、RAT Type、UE所在PLMN ID等接入网信息。

**非会话管理相关功能：**
- 接入和移动性策略控制。
- UE接入选择和UE路由选择策略控制。

### 策略分类

PCC中的策略分为AM策略、UE策略、SM策略三种。AM策略和UE策略为5G新增策略类型，适用于5G用户；SM策略适用于2/3/4/5G用户。

| 策略类型 | 内容项 | 详细内容 | 作用 |
|----------|--------|----------|------|
| AM策略（接入和移动性策略） | SAR（服务区限制） | UE允许接入的TAI列表、不允许接入的TAI列表、最大允许接入的TAI数 | 用于决策可以接入的区域 |
| AM策略 | RFSP索引（无线频率选择优先级） | 一组无线频段及其优先级 | 用于无线侧的无线资源管理，传递到无线侧后可定制频率选择策略 |
| UE策略（选网和路由选择策略） | ASNDP（UE接入选网策略） | 辅助UE选择WLAN接入网的规则 | 辅助UE选择WLAN接入网 |
| UE策略 | URSP（UE路由选择策略） | 切片选择策略、SSC模式选择策略、DNN选择策略、PDU会话类型选择策略、非无缝卸载指示、接入类型偏好 | 辅助UE选择合适的PDU会话 |
| SM策略（会话管理策略） | 会话规则 | 与PDU会话相关的信息元素：会话规则ID、授权的会话AMBR、授权的默认QoS、用量监控数据、条件数据 | 用于PDU会话粒度的策略控制 |
| SM策略 | PCC规则 | 提供策略控制或计费控制的参数集：5QI、ARP、SDF模板、计费信息、策略控制信息、用量监控控制信息、流量转向控制信息等 | 用于SDF粒度的策略控制 |

策略由**触发器**和**规则**组成。

### 触发器概念

- **对PCF/PCRF/PGW-C来说**：触发器定义了策略的决策时机。当策略下的任一触发器定义的事件发生时，PCF/PCRF/PGW-C才会进行相应的规则匹配并下发规则给UPF/PGW-U。
- **对UPF/PGW-U来说**：触发器定义了发起上报流程的条件。当检测到流量/时长等达到触发器定义的条件时，发起上报流程。

### 规则概念

规则即PDR（Packet Detection Rule），对满足哪些条件的报文，执行哪些动作。规则由条件和动作组成。

会话管理策略中，规则包括**会话规则**和**PCC规则**。

#### PCC规则来源

1. **PCRF/PCF下发**：用户激活过程中PGW-C/SMF与PCRF/PCF交互，通过N7接口获取策略和计费控制相关的授权信息，并将其处理后提供给PGW-U/UPF。PCRF/PCF可下发动态规则、预定义规则给PGW-C/SMF，并由PGW-C/SMF通过N4接口传递给PGW-U/UPF。
2. **SMF/PGW-C下发**：网络中未部署PCRF/PCF时，策略由SMF/PGW-C定义，SMF/PGW-C仅下发规则名称，不下发具体的规则内容。

#### 规则分类与各网元职责

| 规则类别 | PCF | SMF | UPF |
|----------|-----|-----|-----|
| **动态规则** | 定义规则名称和具体内容，将规则名称和内容下发给SMF | 将PCF下发的规则内容传递给UPF | 根据接收的规则，对用户数据进行处理 |
| **预定义规则（单条）** | 定义的规则名称与SMF上的一致，将规则名称下发给SMF | 定义规则名称，将一致的规则名称传递给UPF | 定义具体的规则内容，根据规则名称匹配本地配置的规则并执行 |
| **预定义规则组（一组规则）** | 定义的规则名称与SMF上的UserProfile名称一致，将规则名称下发给SMF | 定义UserProfile名称，定义多条规则并绑定到一个UserProfile中，将一致的规则名称传递给UPF | 定义具体的规则内容，根据UserProfile名称匹配本地配置，按规则优先级处理 |
| **本地规则** | 与PCF无关 | 定义UserProfile名称，将UserProfile名称传递给UPF | 定义具体的规则内容，根据UserProfile名称匹配并执行 |

#### 规则优先级

规则的优先级值越小，优先级越高。对于SMF来说，当优先级相同时：**动态规则 > 预定义规则 > 本地规则**。

### 条件与动作

- **条件（PDI，Packet Detection Information）**：UPF/PGW-U检测报文时，满足哪些条件才执行对应动作。
- **动作（PA，Packet Action）**：包括FAR（Forwarding Action Rule）、URR（Usage Reporting Rule）和QER（QoS Enforcement Rule）等。具体动作包括QoS控制、计费、带宽管理、重定向、头增强和URL过滤，触发专有QoS flow（对应4G的专有承载）的建立、修改、删除等。

### SDF

SDF（Service Data Flow）：业务数据流。一个SDF是一组IP数据流，该组数据流具有相同的QoS。

---

## 原理与流程

### 实现原理

PCC基本功能的组网及接口关系：用户使用5G业务时，通过LTE或(R)AN接入网络，PCRF/PCF根据用户签约信息、业务信息或用户状态信息等进行决策，生成控制策略。PCRF/PCF通过N7接口将QoS及计费策略下发给PGW-C/SMF，PGW-C/SMF通过N4接口再下发给PGW-U/UPF，PGW-U/UPF基于用户和业务类型进行限速和门控，并且将QoS信息传递给无线、核心网共同进行端到端资源管理。

### PCC业务流程

当用户发起注册流程接入5G网络时：

1. AMF和PGW-C/SMF分别发起PCRF/PCF发现和选择流程。
2. 选定PCRF/PCF后，发起AM策略关联建立和SM策略关联建立流程。
3. 获取相应的策略（含PCC规则）及策略事件上报触发器。
4. 部署执行策略。
5. PGW-C/SMF在收到SM策略后进行QoS映射，将相应的QoS信息下发给PGW-U/UPF、RAN和UE，进行端到端的QoS控制。

#### PDU会话建立

- PGW-C/SMF基于QoS及业务需求，将SDF映射到QoS流上。
- PGW-C/SMF通过N4接口将QoS计费策略下发给PGW-U/UPF并且建立会话。
- PGW-U/UPF基于收到的SDF将用户面数据和QoS流匹配。
- PGW-U/UPF对下行数据包进行传输层标记（QFI），对PDU会话集合的最大速率进行控制，对PDU进行流量统计以支持计费。

#### PDU会话修改

- 当满足触发器条件时（如用户签约信息更改或用户接入位置改变），PCRF/PCF或AMF/PGW-C/SMF可分别发起AM策略关联更新或SM策略关联更新流程。
- PGW-C/SMF通过N4接口将更新的QoS信息传递给PGW-U/UPF，完成PDU会话修改。
- PDU会话修改过程中，PGW-U/UPF会对上行数据包进行检测，确保上行数据包的QFI和相应的QoS流匹配。
- **重要规则**：一条消息中存在对同一个预定义rule的安装和删除操作时，UPF对该rule进行安装操作（安装优先于删除）。
- 触发器定义了引起PGW-C/SMF发起策略更新请求的事件，决定PCRF/PCF策略的决策时机。可以由PCRF/PCF在`Npcf_SMPolicyControl_Update response`或`Npcf_SMPolicyControl_UpdateNotify request`消息中下发给PGW-C/SMF。

#### PDU会话释放

- 当PCRF/PCF检测到UE签约信息删除、UE从网络去注册或满足其他触发器条件时，发起策略关联释放流程。
- PGW-U/UPF将丢弃与该PDU会话相关的数据包，并释放与N4会话相关的所有隧道资源和上下文。

### Event Trigger机制

PCC架构中定义了Event Trigger，当相应事件发生时，PGW-C/SMF触发对应Event Trigger，并向PCRF/PCF申请更新策略。PGW-C/SMF支持通过URR（使用量上报规则）设置PGW-U/UPF的上报事件触发点。

| Event Trigger | 含义 | 关联IE |
|---------------|------|--------|
| PERIO (Periodic Reporting) | UPF基于URR中定义的测量周期定时发起上报流程 | Measurement Period |
| VOLTH (Volume Threshold) | UPF基于URR中定义的流量阈值，在业务使用量超过阈值时发起上报流程 | Volume Threshold |
| TIMTH (Time Threshold) | UPF基于URR中定义的时长阈值，在业务使用时长超过阈值时发起上报流程 | Time Threshold |
| QUHTI (Quota Holding Time) | UPF基于URR中定义的配额保持时间，在配额下发时长超过阈值时发起上报流程 | Quota Holding Time |
| START (Start of Traffic) | UPF基于URR中定义的业务开始Trigger，在感知到业务开始时发起上报流程 | NA |
| STOPT (Stop of Traffic) | UPF基于URR中定义的业务结束Trigger，在感知到业务结束时发起上报流程 | NA |
| DROTH (Dropped DL Traffic Threshold) | UPF基于URR中定义的下行业务丢包阈值，在因下行缓存超规格丢包数超过阈值时发起上报流程 | Dropped DL Traffic Threshold |
| LIUSA (Linked Usage Reporting) | UPF基于URR中定义的关联URR ID，在关联URR因故发起上报时协同触发上报 | Linked URR ID |
| VOLQU (Volume Quota) | UPF基于URR中定义的流量配额，在业务使用量配额耗尽时发起上报流程 | Volume Quota |
| TIMQU (Time Quota) | UPF基于URR中定义的时长配额，在业务使用时长配额耗尽时发起上报流程 | Time Quota |
| ENVCL (Envelope Closure) | UPF基于URR中定义的信封测量周期，在信封关闭时发起上报流程 | NA |
| MACAR (MAC Addresses Reporting) | UPF基于URR中定义的MAC地址上报信息，在检测UE发起的上行报文的源MAC地址时发起上报流程 | NA |
| EVETH (Event Threshold) | UPF基于URR中定义的事件阈值，在业务使用的事件数超过事件阈值时发起上报流程 | Event Information |

### 2/3/4/5G PCC功能差异对比

| 差异点 | 2/3/4G | 5G |
|--------|--------|-----|
| **关键网元** | AF, SPR, PCRF, PGW(PCEF) | AF, UDR, PCF, AMF, PGW-C/SMF, UPF |
| **接口** | Gx | N7, N15, N4 |
| **协议** | 基于Diameter的Gx应用协议 | PFCP协议（N4）、HTTPS（N7, N15） |
| **策略类型** | 会话管理策略 | 会话管理策略（SM策略）、接入和移动性策略（AM策略）、选网和路由策略（UE策略） |
| **漫游支持** | 策略在归属网络生成 | 策略在归属网络生成 + 策略在访问网络生成 |
| **主要流程** | IP-CAN会话流程、专有承载流程 | PCF发现和选择、AM策略关联流程、SM策略关联流程、PFD管理流程 |
| **规则来源** | PCRF下发、AAA Server下发、本地配置 | PCF下发、本地配置 |
| **规则分类** | 动态规则、预定义规则、预定义规则组（即本地UserProfile） | 动态规则、预定义规则（可匹配预定义规则或UserProfile，将4G的预定义规则和预定义规则组统一） |

---

## 配置规则

### 动态PCC vs 本地PCC配置差异

| 对比维度 | 动态PCC功能 | 本地PCC功能 |
|----------|-------------|-------------|
| **前提条件** | 网络中有PCRF/PCF | 网络中无PCRF/PCF，通过特定APN激活 |
| **规则定义方** | PCRF/PCF定义策略，SMF传递 | SMF/PGW-C定义策略，仅下发规则名称 |
| **动态规则** | 支持：PCRF/PCF下发业务流特征及精细化管理动作，SMF和UPF不需要特殊配置 | 不支持 |
| **预定义规则** | UPF/SMF/PCF上需定义相同的规则标识（RULENAME） | 不适用 |
| **预定义规则组** | UPF/SMF/PCF上需定义相同的规则组标识（USERPROFILENAME） | UPF/SMF上需定义相同的规则组标识（USERPROFILENAME） |
| **规则实时更新** | PCF可以随时删除旧规则、安装新规则 | SMF不支持实时更新规则 |
| **License** | 需要LKV3G5PCCB01 | 需要LKV3G5PCCB01 |
| **MML命令序列** | 相同 | 相同 |

### UPF侧PCC相关配置对象

PCC基本功能在UPF侧涉及的配置对象及其层级关系：

```
UserProfile（用户模板）
  └── RULEBINDING（规则绑定）
        └── RULE（规则）
              ├── FILTERINGMODE（匹配模式：FLOWFILTER）
              │     └── FLOWFILTER（流过滤器）
              │           ├── FLTBINDFLOWF（过滤器绑定）
              │           │     └── FILTER（三四层过滤器）或 L7FILTER（七层过滤器）
              │           └── PROTBINDFLOWF（协议绑定）
              └── POLICYNAME（策略名称）
                    └── PCCPOLICYGRP（PCC策略组）
                          └── URRGROUPNAME（URR组名称，计费时需要）
```

### 动态PCC配置步骤

#### 步骤1：打开License配置开关

```
SET LICENSESWITCH:LICITEM="LKV3G5PCCB01",SWITCH=ENABLE;
```

#### 步骤2：配置PCC策略组

```
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pg_test",URRGROUPNAME="urrgp_test";
```

| 参数 | 说明 | 约束 |
|------|------|------|
| PCCPOLICYGRPNM | PCC策略组名称 | 存在多条数据时，该参数不能相同 |
| URRGROUPNAME | URR组名称 | 当需要计费时必须配置，需已通过ADD URRGROUP命令配置 |

#### 步骤3：配置流过滤器

```
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_test";
```

| 参数 | 说明 | 约束 |
|------|------|------|
| FLOWFILTERNAME | 流过滤器名称 | 不同流过滤器之间不能重复 |

**关键约束**：流过滤器必须至少绑定一个filter或一个l7filter，否则所有报文都匹配不上该流过滤器。

#### 步骤4：配置三四层过滤条件

```
ADD FILTER:FILTERNAME="filter_test",L34PROTTYPE=STRING,L34PROTOCOL=ANY;
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",FILTERNAME="filter_test";
```

| 参数 | 说明 | 约束 |
|------|------|------|
| FILTERNAME | 过滤器名称 | 不同过滤器之间不能重复 |
| L34PROTTYPE | 三四层IPv4协议输入类型 | 如STRING |
| L34PROTOCOL | 三四层协议类型 | 如ANY表示Any to any |

#### 步骤5：配置规则

```
ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,
  FILTERINGMODE=FLOWFILTER,
  FLOWFILTERNAME="flowfilter_test",
  PRIORITY=65535,
  POLICYNAME="pg_test";
```

| 参数 | 说明 | 约束 |
|------|------|------|
| RULENAME | 规则名称 | 与SMF上配置的规则名称相同；存在多条数据时，该参数+策略类型不能完全相同 |
| POLICYTYPE | 策略类型 | PCC基本功能使用PCC |
| FILTERINGMODE | 流过滤器或流过滤器组选择 | FLOWFILTER |
| FLOWFILTERNAME | 流过滤器名称 | 需已通过ADD FLOWFILTER命令定义 |
| PRIORITY | 全局优先级 | 仅对PCC用户生效。优先级值越小，优先级越高 |
| POLICYNAME | 策略名称 | 需已通过ADD PCCPOLICYGRP命令定义 |

若需配置多个规则，需多次执行此步骤。

#### 步骤6：配置规则与用户模板的绑定关系

```
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
```

| 参数 | 说明 | 约束 |
|------|------|------|
| USERPROFILENAME | 用户模板名称 | 预定义规则组/本地规则时，UPF上的UserProfile名称与SMF上的UserProfile名称需要一致 |
| RULENAME | 规则名称 | 需已通过ADD RULE命令定义 |

#### 步骤7：将新配置置为生效

```
SET REFRESHSRV:REFRESHTYPE=ALL;
```

**必须在最后执行**，将新配置的Filter和UserProfile置为生效。

### 本地PCC配置步骤

配置步骤与动态PCC完全相同（步骤1-7），MML命令序列一致。关键区别在于：

- 本地PCC不涉及PCF/PCRF的交互。
- SMF通过规则组标识（UserProfile名称）激活UPF本地静态配置的规则。
- SMF不支持实时更新规则（配置修改后需要通过SET REFRESHSRV刷新）。

---

## 配置案例

### 案例一：动态PCC功能完整配置（Any to Any匹配）

场景：网络中已部署PCRF/PCF，用户需要激活为PCC用户，配置3/4层any to any的filter（所有报文匹配）。

```
// 1. 打开License配置开关
SET LICENSESWITCH:LICITEM="LKV3G5PCCB01",SWITCH=ENABLE;

// 2. 配置流过滤器和三四层过滤条件
ADD FILTER:FILTERNAME="filter_test",L34PROTTYPE=STRING,L34PROTOCOL=ANY;
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_test";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",FILTERNAME="filter_test";

// 3. 配置PCC策略组（需要计费时配置URRGROUPNAME）
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pg_test",URRGROUPNAME="urrgp_test";

// 4. 配置规则
ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,
  FILTERINGMODE=FLOWFILTER,
  FLOWFILTERNAME="flowfilter_test",
  PRIORITY=65535,
  POLICYNAME="pg_test";

// 5. 配置规则与用户模板的绑定关系
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";

// 6. 将新配置的Filter和UserProfile置为生效
SET REFRESHSRV:REFRESHTYPE=ALL;
```

### 案例二：本地PCC功能完整配置

场景：网络中无PCRF/PCF，通过特定APN激活的用户需要激活为PCC用户。配置命令与动态PCC完全相同。

```
// 命令序列同案例一
SET LICENSESWITCH:LICITEM="LKV3G5PCCB01",SWITCH=ENABLE;
ADD FILTER:FILTERNAME="filter_test",L34PROTTYPE=STRING,L34PROTOCOL=ANY;
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_test";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",FILTERNAME="filter_test";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pg_test",URRGROUPNAME="urrgp_test";
ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,
  FILTERINGMODE=FLOWFILTER,
  FLOWFILTERNAME="flowfilter_test",
  PRIORITY=65535,
  POLICYNAME="pg_test";
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
SET REFRESHSRV:REFRESHTYPE=ALL;
```

---

## 验证与调测

### 验证前置条件

- 完成激活PCC基本功能配置。
- 准备测试终端。
- 准备OM Portal跟踪工具。
- 获取测试终端使用的APN名称（可使用`LST APN`命令查询）。

### 验证流程

1. **查询License开关状态**
   ```
   LST LICENSESWITCH:LICITEM="LKV3G5PCCB01";
   ```
   - 如果SWITCH为ENABLE，继续下一步。
   - 如果SWITCH为DISABLE，执行`SET LICENSESWITCH`命令打开。

2. **检查UPF上的配置是否正确**

   以下为关键一致性检查要求：
   - **预定义规则组或本地规则时**：UPF上的UserProfile名称与SMF上的UserProfile名称需要一致。
   - **预定义规则时**：UPF上的规则名称与SMF上的规则名称需要一致。
   - **同一rule**（rule名称+策略类型唯一标识一条rule）：UPF上的URR标识和SMF上的URR标识需要一致。

   使用以下查询命令验证配置：
   ```
   LST USERPROFILE;
   LST RULEBINDING;
   LST RULE;
   LST FLOWFILTER;
   LST FLTBINDFLOWF;
   LST FILTER;
   LST PROTBINDFLOWF;
   LST L7FILTER;
   LST PCCPOLICYGRP;
   LST URRGROUP;
   LST URR;
   ```

3. **在UDG（PGW-U/UPF）上创建用户跟踪任务**。

4. **激活用户，并跟踪该用户消息**。

5. **检查N4接口消息**
   - 查看消息跟踪中是否存在N4接口的`PFCP Session Establishment Request`消息。
   - 检查激活响应消息`PFCP Session Establishment Response`中的返回码Cause是否为`request-accepted (1)`。
   - SMF通过N4接口向UPF下发PDR/FAR/QER/URR等信息。

   **结果判定**：
   - N4消息存在且返回码为request-accepted (1)：PCC用户PDU会话激活成功，继续下一步。
   - N4消息不存在：UDG未收到PCC用户的PDU会话激活请求，需检查UNC（PGW-C/SMF）上的配置。
   - N4消息存在但返回码不为request-accepted (1)：PDU会话激活失败，基于Cause的失败原因进行分析。

6. **业务验证**：用户终端打开浏览器，访问HTTP业务。UPF根据SMF下发的策略，对业务进行处理（转发/带宽控制/流量统计等）。

### 问题排查

| 问题现象 | 可能原因 | 排查方法 |
|----------|----------|----------|
| N4接口消息不存在 | UNC（PGW-C/SMF）配置问题 | 检查UNC上的配置是否正确 |
| PFCP Session Establishment Response返回码不为request-accepted (1) | UPF配置错误或资源不足 | 基于Cause失败原因进行分析 |
| 配置不一致 | UPF与SMF侧配置不匹配 | 使用LST命令逐项比对UserProfile名称、规则名称、URR标识 |
| 业务策略不生效 | Filter未生效或REFRESHSRV未执行 | 检查SET REFRESHSRV是否已执行 |

### 问题升级

如无法自行解决，执行以下信息收集：
1. 执行`EXP MML`命令将当前配置数据导出为MML脚本文件并保存。
2. 收集并保存所有查询信息。
3. 收集归纳所有信息并联系华为技术支持。

---

## 参考信息

### 相关MML命令

| 命令 | 用途 |
|------|------|
| ADD QOSPROP | 增加QoS属性 |
| ADD PCCPOLICYGRP | 增加PCC策略组 |
| ADD RULE | 增加规则 |
| ADD FLOWFILTER | 增加流过滤器 |
| ADD USERPROFILE | 增加用户模板 |
| ADD RULEBINDING | 增加用户模板和规则的绑定关系 |
| SET LICENSESWITCH | 设置License项的开关 |
| LST LICENSESWITCH | 查询License配置项开关 |
| ADD FILTER | 增加过滤器 |
| ADD FLTBINDFLOWF | 增加流过滤器的过滤器绑定关系 |
| SET REFRESHSRV | 业务刷新（将Filter和UserProfile置为生效） |
| LST USERPROFILE | 查询用户模板 |
| LST RULEBINDING | 查询规则绑定 |
| LST RULE | 查询规则 |
| LST FLOWFILTER | 查询流过滤器 |
| LST FLTBINDFLOWF | 查询过滤器绑定 |
| LST FILTER | 查询过滤器 |
| LST PROTBINDFLOWF | 查询协议绑定 |
| LST L7FILTER | 查询七层过滤器 |
| LST PCCPOLICYGRP | 查询PCC策略组 |
| LST URRGROUP | 查询URR组 |
| LST URR | 查询URR |
| EXP MML | 导出MML文件 |

### 相关软参

- **BIT440**：控制动态业务签约场景，service-property匹配失败时的报文动作。

### 告警与测量

- 本特性无相关告警。
- 本特性无相关测量指标。

### 对系统的影响

- 使用PCC功能，系统性能将下降，具体下降程度需要根据具体话务模型进行分析。
- 用户激活时，PGW-C/SMF需要与PCRF/PCF进行交互，获取用户策略并转换为N4接口的PDR下发到PGW-U/UPF，用户激活性能将下降。
- PGW-U/UPF需要动态处理PCRF/PCF下发的策略，将影响系统的报文处理过程，增加报文处理时延。

### 与其他特性的关系

本特性不涉及与其他特性的交互。

### 相关特性

- GWFD-010201 QoS与流量管理：PDU会话建立时，PGW-C/SMF基于QoS及业务需求将SDF映射到QoS流上，详细内容参见该特性。

---

## 知识来源

| 序号 | 源文件 | 贡献内容 |
|------|--------|----------|
| 1 | GWFD-020351 PCC基本功能特性概述_47011385.md | 适用NF、定义、客户价值、应用场景、可获得性（涉及NF角色与功能、License）、与其他特性交互、对系统影响、原理概述、遵循标准、发布历史 |
| 2 | GWFD-020351 PCC基本功能参考信息_79592737.md | 相关MML命令清单、软参（BIT440）、告警与测量信息 |
| 3 | 实现原理/相关概念_72244993.md | 策略分类（AM/UE/SM策略详解）、触发器概念、规则分类与各网元职责（动态/预定义/预定义规则组/本地规则）、条件与动作、SDF定义 |
| 4 | 实现原理/业务流程_47013470.md | PCC业务流程（PDU会话建立/修改/释放）、策略关联建立流程、安装与删除操作优先级规则 |
| 5 | 实现原理/Event Trigger_47013472.md | 13种Event Trigger定义、含义与关联IE（PERIO/VOLTH/TIMTH/QUHTI/START/STOPT/DROTH/LIUSA/VOLQU/TIMQU/ENVCL/MACAR/EVETH） |
| 6 | 实现原理/2_3_4_5G PCC功能差异_47013471.md | 2/3/4G与5G PCC差异对比（网元、接口、协议、策略类型、漫游、流程、规则来源、规则分类） |
| 7 | 激活PCC基本功能/配置动态PCC功能_74096530.md | 动态PCC配置场景、规则分类（动态/预定义/预定义规则组）、配置步骤、参数说明、配置案例 |
| 8 | 激活PCC基本功能/配置本地PCC功能_74096529.md | 本地PCC配置场景、与动态PCC差异、配置步骤、参数说明、配置案例 |
| 9 | 调测PCC基本功能_42369277.md | 验证流程、License检查、配置一致性检查、N4接口消息验证、问题排查、信息收集 |
