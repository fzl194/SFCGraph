# GWFD-020357 增强的ADC基本功能 - 特性知识文档

> **场景归属**: 业务感知 → 带宽控制子场景（辅助特性：ADC应用检测）
> **产品**: UDG (UPF网元)
> **场景定位**: ADC识别应用 → 触发BWM/Shaping等带宽控制策略
> **辅助特性说明**: 本身不做带宽控制，但提供应用级识别能力

---

## 1. 特性概述

### 1.1 基本信息

| 属性 | 取值 |
|------|------|
| 特性ID | GWFD-020357 |
| 特性名称 | 增强的ADC基本功能 |
| 适用NF | PGW-U、UPF |
| 涉及NF（配合网元） | PGW-C/SMF (UNC 20.1.0+), PCRF/PCF (无特殊要求), PGW-U/UPF (UDG 20.2.0+) |
| License控制项 | `82200AFK LKV3G5ADCF01 增强的ADC基本功能` |
| 首次发布版本 | UDG 20.1.0 (特性版本01) |
| 遵循标准 | 3GPP 23501/23502/23503/29.244/29507/29512/29513 |

### 1.2 核心能力

UDG支持ADC（Application Detection and Control）功能，即 UDG 支持检测应用并向PCRF/PCF上报应用标识（Application Identifier）、流信息以及应用的起始或者结束事件。PCRF/PCF根据上报信息，结合用户签约信息、网络状态等信息，下发PCC策略，UDG基于PCC策略进行业务控制、流量上报等；PGW-C/SMF执行承载/QoS Flow管理。

### 1.3 在带宽控制场景中的定位（辅助：识别能力提供者）

ADC是带宽控制场景中的**应用识别能力提供者**，本身不做带宽控制动作。其关键作用链路：

```
UDG/ADC识别应用 → 上报Application Identifier + Flow信息给PGW-C/SMF
→ PGW-C/SMF转发给PCRF/PCF
→ PCRF/PCF根据应用类型 + 签约 + 网络状况下发PCC策略（含带宽/QoS）
→ PGW-C/SMF下发到UDG
→ UDG执行BWM/Shaping/Policing等带宽控制策略
```

典型带宽控制应用场景：
- **业务流控**: UDG实时监测并上报用户使用的业务信息，PCRF/PCF综合用户签约、当前网络状况（如小区拥塞）下发指定业务的流控策略给UDG，实现对指定业务流量的带宽控制（如VoIP业务限速）。
- **高价值业务QoS保障**: UDG识别高价值业务（自营VoIP、视频共享、Mobile TV等），上报后PCRF/PCF下发携带不同QCI/ARP的PCC策略，PGW-C/SMF触发专有承载创建，为高价值业务提供差异化QoS。
- **页面重定向**: 当用户访问未签约业务时，UDG可将页面重定向到提醒页面。

### 1.4 与SA（GWFD-110101）的差异

ADC**依赖**SA相关特性（包含SA-Basic及SA-HTTP Pipeline、SA-Web Browsing、SA-File Access、SA-Mobile、SA-Others、SA-Streaming、SA-P2P、SA-VOIP、SA-Email、SA-IM、SA-Game、SA-Network Administration、SA-Remote Connectivity、SA-Network Storage、SA-Tunneling、SA-Stock、SA-Database、SA-QUIC等共19个SA子特性）。

- **SA**负责执行业务检测，是底层业务感知引擎（DPI、协议解析等）。
- **ADC**基于SA的检测结果，向PCRF/PCF**上报**应用标识、流信息和起始/结束事件，是SA与PCC策略体系之间的**上报桥梁**。
- 开通增强的ADC基本功能**必须同时开启**SA功能。

### 1.5 与BWM（GWFD-110311）的协作关系

- ADC负责**识别**应用并上报，PCRF/PCF负责**决策**下发PCC策略（含带宽控制参数），BWM/Shaping/Policing负责**执行**带宽控制动作。
- ADC识别结果通过PCC规则传递给BWM：ADC上报 → PCRF生成动态规则 → 下发到UDG → UDG的BWM模块执行限速/整形。
- 三者构成"识别 - 决策 - 执行"的完整链路，ADC是这一链路的**入口环节**。

### 1.6 与PCC基本功能（GWFD-020351）的关系

ADC**依赖**PCC基本功能（License控制项 `82209825 PCC 基本功能`）。PCRF/PCF下发携带Application ID的PCC规则给UDG，所以开通增强的ADC基本功能**必须同时开启**PCC基本功能。

---

## 2. 核心概念

### 2.1 ADC（Application Detection and Control）

ADC是本特性的核心机制，包含三个动作：
- **Detection（检测）**: UDG检测应用数据流（L7），基于SA引擎完成应用识别。
- **Reporting（上报）**: UDG将检测到的应用标识、流信息以及应用起始/结束事件，通过PGW-C/SMF上报给PCRF/PCF。
- **Control（控制）**: PCRF/PCF根据上报信息下发PCC策略，UDG执行策略（业务控制、流量上报、QoS保障等）。

### 2.2 应用识别技术

ADC本身不实现识别算法，识别能力由SA引擎提供，ADC负责将SA的识别结果结构化上报。识别技术包括：
- **深度包检测（DPI）**: 基于特征码匹配报文负载。
- **协议分析**: 解析协议字段（如HTTP URL、Host头部）。
- **行为分析**: 基于流量行为模式识别应用类型。

### 2.3 关键名词定义

| 概念 | 定义 |
|------|------|
| **应用（Application）** | ADC功能中定义的名词，等同于PCC基本功能的"业务"。 |
| **自营业务** | 运营商提供的业务（如手机音乐下载、手机视频浏览）。通过差异化QoS保障提升竞争力。 |
| **可推论业务** | 应用的流信息可识别，且业务持续时间长（推荐不小于3分钟）、并发业务流数量少（推荐不超过16个）的业务。如FTP、RTSP。需基于协议理解判定，不能简单通过协议名称判定。 |
| **不可推论业务** | 五元组老化快、并发业务流数量多的业务，如P2P、HTTP。 |
| **Application ID** | 应用标识，PCRF/PCF在PCC规则中携带，映射到UDG本地配置的FlowFilter。 |
| **FlowFilter（流过滤器）** | UDG中定义的L3/L4/L7过滤条件，Application ID通过TDF-Application-Identifier AVP映射到FlowFilter。 |
| **L7Filter（七层过滤器）** | 基于URL、协议等七层信息定义的过滤条件。 |

### 2.4 识别结果上报机制

UDG向PCRF/PCF上报的内容通过 **Application-Detection-Information AVP** 携带，包含：

| 信元 | 说明 |
|------|------|
| **TDF-Application-Identifier** | 应用标识（应用名），是否上报由ADCMUTEFLAG或动态PCC规则中的Mute-Notification AVP决定。 |
| **TDF-Application-Instance-Identifier** | 应用实例标识，用于标识同一应用的不同实例，避免重复上报Flow-Information。 |
| **Flow-Information** | 流信息（五元组），仅可推论业务上报。是否上报由ADCPARA命令控制。 |

上报的事件触发类型：
- **APPLICATION_START**: 应用数据流开始时触发。
- **APPLICATION_STOP**: 应用数据流终止时触发。

### 2.5 ADC特征库

ADC的识别能力依赖**协议识别库和解析库**，需通过`LOD SIGNATUREDB`命令加载。特征库管理属于SA业务感知专题范畴，本特性调测前提之一是完成协议识别库和解析库的加载。

### 2.6 与SA、BWM、PCC的关系全景

```
┌─────────────────────────────────────────────────────────────────┐
│                     PCRF/PCF（策略决策中心）                       │
│  接收ADC上报 → 结合签约/网络状态 → 生成PCC策略（含带宽/QoS）        │
└──────────────┬──────────────────────────▲──────────────────────┘
               │ Npcf_SMPolicyControl       │ Npcf_SMPolicyControl
               │ _Update Request            │ _Create/UpdateNotify
               ▼                            │
┌─────────────────────────────────────────────────────────────────┐
│                    PGW-C/SMF（控制面转发）                        │
│  转发应用检测信息 ← 转发PCC策略（PFCP Session）→                   │
└──────────────┬──────────────────────────▲──────────────────────┘
               │ PFCP Session Report       │ PFCP Session
               │ Request                   │ Establishment
               ▼                            │
┌─────────────────────────────────────────────────────────────────┐
│                     UDG / PGW-U / UPF                           │
│  ┌──────────┐   ┌──────────┐   ┌────────────────────────────┐  │
│  │ SA引擎   │ → │ ADC模块  │ → │ PCC执行（含BWM/Shaping/    │  │
│  │（DPI识别）│   │（上报）  │   │ Policing/计费/QoS）         │  │
│  └──────────┘   └──────────┘   └────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. 实现原理与流程

### 3.1 应用识别机制

ADC应用识别由SA引擎完成，ADC负责结构化上报。识别过程：
1. 报文到达UDG。
2. SA引擎对报文进行DPI检测，匹配特征库中的协议/应用特征。
3. SA将识别结果（应用名、协议、流信息）返回给ADC模块。
4. ADC模块根据PCC规则中的Application ID与本地FlowFilter的映射关系，判断是否需要上报。

### 3.2 ADC特征库匹配流程

```
报文 → SA引擎DPI检测 → 匹配特征库
                          │
           ┌──────────────┼──────────────┐
           ▼              ▼              ▼
      匹配到应用      匹配到协议       未匹配
           │              │              │
           ▼              ▼              ▼
     检查PCC规则     检查FlowFilter    使用缺省rule
     是否携带该       的L7过滤条件      （L3/4=L7=any）
     Application ID
           │
     ┌─────┴─────┐
     ▼           ▼
  需要上报     不需要上报
     │           │
     ▼           ▼
  上报ADC     仅本地执行
  事件给      PCC策略
  PCRF/PCF
```

### 3.3 识别结果上报PCRF/SMF流程

#### 3.3.1 上报路径

```
UDG/UPF → PFCP Session Report Request → PGW-C/SMF
→ Npcf_SMPolicyControl_Update Request → PCRF/PCF
```

#### 3.3.2 上报内容控制因素

| 控制点 | 命令/参数 | 作用 |
|--------|-----------|------|
| **ADCHYSTTIMER** | `ADD ADCPARA` | 应用级上报迟滞时间（0~3600秒）。取值0表示关闭延迟上报。不为0时，UDG延迟该值后上报APPLICATION_START/STOP。用于防止单用户单应用的Start/Stop消息上报过于频繁。 |
| **FLOWINFORPT** | `ADD ADCPARA` | 流信息上报开关。ENABLE=上报Flow-Information，DISABLE=不上报（默认）。 |
| **ADCMUTEFLAG** | `ADD PCCPOLICYGRP` 或 `ADD RULE` | ADC静默通知标识。DISABLE=允许上报（检测到事件时上报），ENABLE=静默不上报。也可由动态PCC规则中的Mute-Notification AVP控制。 |
| **Mute-Notification AVP** | 动态PCC规则携带 | PCRF/PCF动态下发的静默通知标识，优先级与ADCMUTEFLAG等同。 |

#### 3.3.3 上报内容的决定逻辑

- **TDF-Application-Identifier（应用名）是否上报**：由 `ADCMUTEFLAG` 是否为 `DISABLE`，或动态PCC规则中是否携带Mute-Notification AVP共同决定。
- **TDF-Application-Instance-Identifier / Flow-Information（可推论业务）是否上报**：由 `ADD ADCPARA` 命令控制。
- **Flow-Information仅对可推论业务上报**：不可推论业务（P2P、HTTP等）因其五元组老化快、并发流多，不上报流信息。

### 3.4 触发带宽控制策略的完整端到端流程

#### 阶段1: 初始激活

1. 用户发起IP-CAN Session建立。
2. PGW-C/SMF向PCRF/PCF发送 `Npcf_SMPolicyControl_Create Request` 消息请求策略。
3. PCRF/PCF在 `Npcf_SMPolicyControl_Create Response` 中下发**携带application ID的PCC动态规则**，并下发 `APPLICATION_START` 和 `APPLICATION_STOP` Event-Trigger，要求检测到application ID对应数据流时上报。
   - PCRF/PCF也可在任何 `Npcf_SMPolicyControl_Create Response` 或 `Npcf_SMPolicyControl_UpdateNotify Request` 消息中下发这两个Event-Trigger或携带application ID的PCC规则。
4. PGW-C/SMF向PGW-U/UPF发送 `PFCP Session Establishment Request`，携带application ID的PCC规则及APPLICATION_START和APPLICATION_STOP Event-Trigger。
5. PGW-U/UPF安装规则，返回 `PFCP Session Establishment Response`。

#### 阶段2: 用户开始使用应用（触发带宽控制）

1. PGW-U/UPF检测到应用数据流开始（SA引擎识别）。
2. PGW-U/UPF将检测信息发送给PGW-C/SMF。
   - 若 `ADCHYSTTIMER` 不为0，PGW-U/UPF**延迟**该值后上报APPLICATION_START事件。
3. PGW-C/SMF通过 `Npcf_SMPolicyControl_Update Request` 向PCRF/PCF上报应用检测信息（Application-Detection-Information）及APPLICATION_START Event-Trigger。
   - Application-Detection-Information中携带 TDF-Application-Instance-Identifier / Flow-Information（可推论业务）。
4. PCRF/PCF根据上报信息，结合用户签约数据，**下发更新后的PCC策略**。
5. PGW-C/SMF根据新PCC策略，可能发起：
   - **专有承载/二次上下文/专有QoS Flow创建**（当需要GBR保障时）
   - **更新已有承载/上下文的带宽**（QoS调整）
   - PCRF/PCF可能对应用数据流分配GBR（QCI/ARP和带宽，或5QI/ARP和带宽）
6. PGW-C/SMF将新PCC策略下发给PGW-U/UPF。
7. PGW-U/UPF对后续业务流**执行新的PCC策略**（带宽控制、QoS保障等）。

#### 阶段3: 用户停止使用应用（带宽控制恢复）

1. 用户停止使用业务，PGW-U/UPF检测到应用数据流终止。
   - 若 `ADCHYSTTIMER` 不为0，延迟上报APPLICATION_STOP事件。
2. PGW-C/SMF向PCRF/PCF发送应用检测信息和APPLICATION_STOP Event-Trigger。
   - Application-Detection-Information中携带 TDF-Application-Identifier / TDF-Application-Instance-Identifier。
   - **注意**: 如果用户业务匹配的携带Application ID的PCC规则被删除或失效，后续业务停止后**不再上报**APPLICATION_STOP事件。
3. PCRF/PCF根据上报信息，结合签约业务，下发新的PCC策略。
4. PGW-C/SMF可能发起专有承载/二次上下文/专有QoS Flow的去激活，或更新上下文/承载/QoS Flow（如删除之前下发的PCC规则）。

### 3.5 完整端到端流程图（文字版）

```
[初始激活阶段]
UE ──IP-CAN Session建立──> PGW-C/SMF ──Create Request──> PCRF/PCF
PCRF/PCF ──Create Response（携带App ID的PCC规则 + START/STOP触发）──> PGW-C/SMF
PGW-C/SMF ──PFCP Session Establishment Request──> PGW-U/UPF
PGW-U/UPF ──PFCP Session Establishment Response──> PGW-C/SMF

[应用开始阶段]
UE ──应用数据流──> PGW-U/UPF（SA检测到应用）
PGW-U/UPF ──PFCP Session Report Request（APP_START + App-Detection-Info）──> PGW-C/SMF
PGW-C/SMF ──Npcf_SMPolicyControl_Update Request──> PCRF/PCF
PCRF/PCF ──新PCC策略（含QoS/带宽）──> PGW-C/SMF
PGW-C/SMF ──可能创建专有承载/更新QoS Flow──> PGW-U/UPF
PGW-U/UPF ──执行新的带宽控制策略──> 后续业务流

[应用停止阶段]
UE ──应用数据流终止──> PGW-U/UPF（SA检测到终止）
PGW-U/UPF ──PFCP Session Report Request（APP_STOP + App-Detection-Info）──> PGW-C/SMF
PGW-C/SMF ──Npcf_SMPolicyControl_Update Request──> PCRF/PCF
PCRF/PCF ──新PCC策略（可能删除PCC规则）──> PGW-C/SMF
PGW-C/SMF ──可能去激活专有承载/恢复QoS Flow──> PGW-U/UPF
```

### 3.6 规则匹配原则

引入携带Application ID的PCC规则后，PCC规则匹配遵循以下原则：

1. **全局优先级匹配**: 预定义规则、动态规则、携带Application ID的动态规则按照全局优先级从高到低顺序匹配。
2. **相同优先级时**: 如果三者优先级相同，选择优先级从高到低依次为：
   - 携带Application ID的动态规则 > 动态规则 > 预定义规则
3. **Application ID映射**: Application ID映射到UDG中配置的FlowFilter，可支持L3/L4/L7过滤条件，与预定义规则的匹配方式相同。PCC动态规则中携带的TDF-Application-Identifier AVP映射到本地配置的FlowFilter。
4. **动态规则优先级**: 携带Application ID的动态规则优先级由PCRF/PCF动态指定。若PCRF/PCF未指定，UDG使用默认优先级。
5. **L7匹配失败回退**: 所有rule的L7都匹配失败时，UDG使用匹配到L3/L4、优先级最高的rule。建议规划一个优先级最低、L3/L4和L7均为any的rule作为缺省配置。
6. **全匹配失败阻塞**: 对于PCRF/PCF下发的预定义规则和动态规则，如果用户业务流匹配不上所有规则，则**阻塞**该业务流。UDG会丢弃匹配不到所有PCC rule的报文。

### 3.7 临时流量的计费处理

在应用识别完成之前，信令报文或业务报文的临时流量处理：
1. 优先选择匹配到优先级最高的rule的L3/L4中的计费信息。
2. 其次选择使用common-policy（对应UserProfile中的配置）中配置的缺省计费信息。
3. 如果上述配置均无法获取，为使应用识别能正常完成，UDG允许临时流量通过，**不进行计费**。

---

## 4. 配置规则

### 4.1 涉及的MML命令总览

本特性涉及以下15条MML命令（按配置逻辑分组）：

| 分组 | 命令 | 用途 |
|------|------|------|
| **License管理** | `SET LICENSESWITCH` | 打开LKV3G5ADCF01 License开关 |
| **License查询** | `LST LICENSESWITCH` | 查询License开关状态 |
| **三四层过滤** | `ADD FILTER` | 配置三四层过滤条件 |
| **三四层过滤** | `ADD FLOWFILTER` | 创建流过滤器（PCRF动态规则App ID映射目标） |
| **三四层过滤** | `ADD FLTBINDFLOWF` | 绑定过滤器到流过滤器 |
| **三四层过滤** | `ADD WELLKNOWNPORT` | 配置知名端口 |
| **七层过滤** | `ADD L7FILTER` | 配置七层过滤器（URL等） |
| **七层过滤** | `ADD PROTBINDFLOWF` | 绑定协议+七层过滤器到流过滤器 |
| **配置生效** | `SET REFRESHSRV` | 将新配置置为生效（L7Filter有60s延迟） |
| **特征库** | `LOD SIGNATUREDB` | 加载协议特征库文件 |
| **ADC参数** | `ADD ADCPARA` | 配置ADC参数（流信息上报开关、迟滞时间） |
| **计费控制** | `ADD URR` | 配置使用量上报规则 |
| **计费控制** | `ADD URRGROUP` | 配置URR组（上下行URR绑定） |
| **PCC策略** | `ADD PCCPOLICYGRP` | 配置PCC策略组（含ADC静默通知标识） |
| **业务规则** | `ADD RULE` | 配置规则（策略类型ADC或PCC） |
| **用户绑定** | `ADD USERPROFILE` | 创建用户模板 |
| **用户绑定** | `ADD RULEBINDING` | 绑定规则到用户模板 |

### 4.2 License开关配置

**命令**: `SET LICENSESWITCH`

```
SET LICENSESWITCH:LICITEM="LKV3G5ADCF01",SWITCH=ENABLE;
```

- License控制项: `LKV3G5ADCF01`
- 必须先打开此开关，才能配置ADC相关功能。
- 查询命令: `LST LICENSESWITCH:LICITEM="LKV3G5ADCF01";`

### 4.3 三四层过滤条件配置

#### 4.3.1 创建过滤器

**命令**: `ADD FILTER`

关键参数：
| 参数 | 说明 |
|------|------|
| FILTERNAME | 过滤器名称，不能重复 |
| L34PROTTYPE | 三四层IPv4协议输入类型（如ANY） |
| L34PROTOCOL | 三四层协议 |

```
ADD FILTER: FILTERNAME="filter_test1", L34PROTTYPE=STRING, L34PROTOCOL=ANY;
```

#### 4.3.2 创建流过滤器

**命令**: `ADD FLOWFILTER`

关键参数：
| 参数 | 说明 |
|------|------|
| FLOWFILTERNAME | 流过滤器名称，不能重复 |

> **重要**: PCRF/PCF下发动态规则携带appid时，PGW-C/SMF、PGW-U/UPF、PCRF/PCF三个网元上的FlowFilter名称**必须一致**，否则无法正常上报。PCRF/PCF通过预定义规则下发APPLICATION_START和APPLICATION_STOP Event-Trigger时，FlowFilter与ADC功能无关。

```
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_ADC01";
```

#### 4.3.3 绑定过滤器到流过滤器

**命令**: `ADD FLTBINDFLOWF`

```
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_ADC01",FILTERNAME="filter_test1";
```

#### 4.3.4 知名端口配置

**命令**: `ADD WELLKNOWNPORT` — 用于配置三四层知名端口（辅助配置，按需使用）。

### 4.4 七层过滤条件配置

#### 4.4.1 创建七层过滤器

**命令**: `ADD L7FILTER`

关键参数：
| 参数 | 说明 |
|------|------|
| L7FILTERNAME | 七层过滤器名称，不能相同 |
| SUBL7FLTNAME | 子七层过滤器名称，同一七层过滤器内不能相同 |
| URL | URL地址（如 `www.huawei.com/*`），基于HTTP协议时可不规划 |

```
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="sl7_test_1",URL="www.huawei.com/*";
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="sl7_test_2",URL="www.example.com";
```

#### 4.4.2 绑定七层过滤信息到流过滤器

**命令**: `ADD PROTBINDFLOWF`

关键参数：
| 参数 | 说明 |
|------|------|
| FLOWFILTERNAME | 流过滤器名称 |
| PROTOCOLNAME | 协议名称（如http） |
| L7FILTERNAME | 七层过滤器名称（仅基于URL时需要规划） |

```
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_ADC01",PROTOCOLNAME="http",L7FILTERNAME="l7filter_test";
```

#### 4.4.5 配置生效

**命令**: `SET REFRESHSRV`

```
SET REFRESHSRV:REFRESHTYPE=ALL;
```

> 系统自动在60s后将配置的L7Filter置为生效。执行此命令可立即生效。REFRESHSRV必须是三四层和七层配置后的最后一步。

### 4.5 ADC参数配置

**命令**: `ADD ADCPARA`

关键参数：
| 参数 | 说明 | 取值 |
|------|------|------|
| FLOWFILTERNAME | 流过滤器名称 | 使用已配置的FlowFilter名称 |
| FLOWINFORPT | 流信息上报开关 | ENABLE（上报）/ DISABLE（不上报，默认）。PCRF/PCF需要获取流信息时设为ENABLE。 |
| ADCHYSTTIMER | 应用级上报迟滞时间（秒） | 0~3600。0=关闭延迟上报。单用户单应用Start/Stop频繁时调大。 |

```
ADD ADCPARA: FLOWFILTERNAME="flowfilter_ADC01",FLOWINFORPT=ENABLE,ADCHYSTTIMER=0;
```

> **仅PCRF/PCF通过预定义规则下发时需要配置ADCPARA**。动态规则模式下流信息上报开关以SMF下发的为准。

### 4.6 ADC特征库加载

**命令**: `LOD SIGNATUREDB`

用于加载协议特征库文件。特征库加载属于SA业务感知专题的配置范畴，本特性调测前提是已完成特征库加载。

### 4.7 规则配置（两种方式）

PCRF/PCF通过预定义规则下发时，可以选择单独的ADC类型rule或复用PCC类型rule。

#### 方式一: 策略类型为ADC的rule

**命令**: `ADD RULE`

关键参数：
| 参数 | 说明 | 取值样例 |
|------|------|---------|
| RULENAME | 规则名称 | rule_test2 |
| POLICYTYPE | 策略类型 | **ADC** |
| FILTERINGMODE | 过滤模式 | FLOWFILTER |
| FLOWFILTERNAME | 流过滤器名称 | flowfilter_ADC01 |
| PRIORITY | 全局优先级（值越小优先级越高，仅对PCC用户生效） | 15 |
| ADCMUTEFLAG | ADC静默通知标识 | DISABLE（允许上报） |

```
ADD RULE:RULENAME="rule_test2",POLICYTYPE=ADC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilter_ADC01",PRIORITY=15,ADCMUTEFLAG=DISABLE;
```

#### 方式二: 策略类型为PCC的rule（复用计费体系）

需配置完整的计费属性链路：URR → URRGROUP → PCCPOLICYGRP → RULE。

**步骤1: 配置URR**

```
ADD URR:URRNAME="urr01",URRID=1000,USAGERPTMODE=OFFLINE;
```

**步骤2: 配置URR组**

```
ADD URRGROUP:URRGROUPNAME="cp_test", UPURRNAME1="urr01", DOWNURRNAME1="urr01";
```

**步骤3: 配置PCC策略组**

关键参数：
| 参数 | 说明 |
|------|------|
| PCCPOLICYGRPNM | PCC策略组名称 |
| ADCMUTEFLAG | ADC静默通知标识，必须设为DISABLE |
| URRGROUPNAME | 绑定的URR组名称 |

```
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pg_ADC01",ADCMUTEFLAG=DISABLE,URRGROUPNAME="cp_test";
```

**步骤4: 配置PCC类型rule**

关键参数：
| 参数 | 说明 | 取值样例 |
|------|------|---------|
| RULENAME | 规则名称 | rule_test2 |
| POLICYTYPE | 策略类型 | **PCC** |
| FILTERINGMODE | 过滤模式 | FLOWFILTER |
| FLOWFILTERNAME | 流过滤器名称 | flowfilter_ADC01 |
| PRIORITY | 全局优先级 | 20 |
| POLICYNAME | 策略名称（PCC策略组名称） | pg_ADC01 |

```
ADD RULE:RULENAME="rule_test2",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilter_ADC01",PRIORITY=20,POLICYNAME="pg_ADC01";
```

### 4.8 用户模板与规则绑定

**命令**: `ADD USERPROFILE` + `ADD RULEBINDING`

```
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test2";
```

> 用户模板名称需与SMF上配置的用户模板名称保持一致。

---

## 5. 配置案例

### 5.1 案例一: PCRF/PCF下发预定义规则 — 识别HTTP应用后触发QoS保障

**场景描述**: 使能增强的ADC基本功能，PCRF/PCF下发携带APPLICATION_START和APPLICATION_STOP Event-Trigger的预定义规则给UDG。UDG本地配置需要识别的URL（www.huawei.com 和 www.example.com）、具体的规则内容及上报的应用，并开启流信息上报开关，实现对HTTP业务的QoS保障（进而可触发带宽控制）。

**完整命令序列**:

```mml
// === 步骤1: 打开License开关 ===
SET LICENSESWITCH:LICITEM="LKV3G5ADCF01",SWITCH=ENABLE;

// === 步骤2: 配置三四层过滤条件 ===
ADD FILTER: FILTERNAME="filter_test1", L34PROTTYPE=STRING, L34PROTOCOL=ANY;
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_ADC01";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_ADC01",FILTERNAME="filter_test1";
SET REFRESHSRV:REFRESHTYPE=ALL;

// === 步骤3: 配置七层过滤条件（URL匹配） ===
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="sl7_test_1",URL="www.huawei.com/*";
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="sl7_test_2",URL="www.example.com";
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_ADC01",PROTOCOLNAME="http",L7FILTERNAME="l7filter_test";
SET REFRESHSRV:REFRESHTYPE=ALL;

// === 步骤4: 配置ADC参数（开启流信息上报，关闭延迟上报） ===
ADD ADCPARA: FLOWFILTERNAME="flowfilter_ADC01",FLOWINFORPT=ENABLE,ADCHYSTTIMER=0;

// === 步骤5（方式A）: 配置策略类型为ADC的rule ===
ADD RULE:RULENAME="rule_test2",POLICYTYPE=ADC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilter_ADC01",PRIORITY=15,ADCMUTEFLAG=DISABLE;

// === 步骤5（方式B）: 配置策略类型为PCC的rule（含完整计费链路） ===
// 步骤5B-1: 配置URR
ADD URR:URRNAME="urr01",URRID=1000,USAGERPTMODE=OFFLINE;
// 步骤5B-2: 配置URR组
ADD URRGROUP:URRGROUPNAME="cp_test", UPURRNAME1="urr01", DOWNURRNAME1="urr01";
// 步骤5B-3: 配置PCC策略组
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pg_ADC01",ADCMUTEFLAG=DISABLE,URRGROUPNAME="cp_test";
// 步骤5B-4: 配置PCC类型rule
ADD RULE:RULENAME="rule_test2",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilter_ADC01",PRIORITY=20,POLICYNAME="pg_ADC01";

// === 步骤6: 配置用户模板与规则绑定 ===
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test2";
```

**执行效果**:
- 当用户访问 www.huawei.com 或 www.example.com 时，UDG识别到HTTP应用匹配FlowFilter。
- UDG立即向PGW-C/SMF上报APPLICATION_START事件（因ADCHYSTTIMER=0）。
- 携带TDF-Application-Identifier（应用名）和Flow-Information（因FLOWINFORPT=ENABLE）。
- PCRF/PCF收到后，可下发携带QoS/带宽参数的PCC策略，触发带宽控制。
- 用户停止访问后，UDG上报APPLICATION_STOP事件，PCRF/PCF可恢复原有策略。

### 5.2 案例二: PCRF/PCF下发动态规则 — 基于Application ID触发带宽控制

**场景描述**: 使能增强的ADC基本功能，PCRF/PCF下发携带Application ID的动态规则给UDG。UDG本地配置需要识别的URL和上报的应用，实现对HTTP业务的QoS保障。流信息上报开关以SMF下发的为准。

**完整命令序列**:

```mml
// === 步骤1: 打开License开关 ===
SET LICENSESWITCH:LICITEM="LKV3G5ADCF01",SWITCH=ENABLE;

// === 步骤2: 配置三四层过滤条件 ===
// 注意: PCRF/PCF动态规则携带appid时，FlowFilter名称在三网元(PGW-C/SMF, PGW-U/UPF, PCRF/PCF)上必须一致
ADD FILTER: FILTERNAME="filter_test1", L34PROTTYPE=STRING, L34PROTOCOL=ANY;
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_ADC01";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_ADC01",FILTERNAME="filter_test1";
SET REFRESHSRV:REFRESHTYPE=ALL;

// === 步骤3: 配置七层过滤条件 ===
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="sl7_test_1",URL="www.huawei.com/*";
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="sl7_test_2",URL="www.example.com";
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_ADC01",PROTOCOLNAME="http",L7FILTERNAME="l7filter_test";
SET REFRESHSRV:REFRESHTYPE=ALL;

// === 步骤4: 用户模板与规则绑定 ===
// 动态规则模式下不需要本地配置ADCPARA（流信息上报开关以SMF下发为准）
// 也不需要本地配置RULE（规则由PCRF/PCF动态下发）
// 但需要配置用户模板以建立用户与策略的关联
ADD USERPROFILE:USERPROFILENAME="up_test";
```

**动态规则与预定义规则的关键差异**:

| 对比维度 | 预定义规则模式 | 动态规则模式 |
|----------|---------------|-------------|
| 规则下发方 | PCRF/PCF下发Event-Trigger，UDG本地配置rule | PCRF/PCF直接下发携带App ID的PCC动态规则 |
| FlowFilter名称 | 与ADC功能无关 | 三网元必须一致 |
| ADCPARA配置 | 需要本地配置（FLOWINFORPT/ADCHYSTIMER） | 流信息上报开关以SMF下发为准，不需本地配置 |
| 本地RULE | 需要配置（ADC类型或PCC类型） | 不需要本地配置RULE |

### 5.3 带宽控制联动场景: ADC识别P2P应用后限速

**场景描述**: UDG通过ADC识别P2P应用流量，上报给PCRF/PCF后，PCRF/PCF下发限速策略。这是一个典型的ADC与BWM联动的带宽控制场景。

**配置思路**（基于案例一扩展）:

```mml
// 1. License与基础过滤配置（同案例一）
SET LICENSESWITCH:LICITEM="LKV3G5ADCF01",SWITCH=ENABLE;

// 2. 配置P2P应用的七层过滤（依赖SA-P2P特征库）
ADD FILTER: FILTERNAME="filter_p2p", L34PROTTYPE=STRING, L34PROTOCOL=ANY;
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_p2p";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_p2p",FILTERNAME="filter_p2p";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 3. P2P协议绑定（基于SA-P2P识别的协议）
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_p2p",PROTOCOLNAME="p2p",L7FILTERNAME="l7filter_p2p";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 4. ADC参数（开启上报，设置迟滞时间避免频繁上报）
ADD ADCPARA: FLOWFILTERNAME="flowfilter_p2p",FLOWINFORPT=DISABLE,ADCHYSTTIMER=60;
// 注: P2P为不可推论业务，Flow-Information不上报，FLOWINFORPT设为DISABLE
// ADCHYSTTIMER=60，避免P2P应用频繁Start/Stop导致信令风暴

// 5. 配置rule和策略绑定（由PCRF/PCF根据上报信息下发限速PCC策略）
ADD RULE:RULENAME="rule_p2p",POLICYTYPE=ADC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilter_p2p",PRIORITY=15,ADCMUTEFLAG=DISABLE;
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_p2p";
```

**联动效果**: UDG识别P2P → 上报APPLICATION_START（延迟60s） → PCRF/PCF下发限速PCC规则 → UDG BWM执行限速。

---

## 6. 验证与调测

### 6.1 调测前提

1. 已完成License加载（如有需求联系华为技术支持）。
2. 已完成PCC基本功能激活（GWFD-020351）。
3. 已完成协议识别库和解析库加载（SA业务感知配置）。
4. 已完成增强的ADC基本功能激活。

### 6.2 调测数据准备

| 类别 | 参数名称 | 取值样例 | 说明 |
|------|----------|---------|------|
| 用户信息 | IMSI | 460000123456789 | 测试终端自带 |
| APN | APN名称 | apn-test | 用户激活使用的APN，可用 `LST APN` 查询 |

### 6.3 调测步骤（以ADCHYSTTIMER=0为例）

**步骤1: 检查License开关**

```
LST LICENSESWITCH:LICITEM="LKV3G5ADCF01";
```
- SWITCH为ENABLE → 继续。
- SWITCH为DISABLE → 执行 `SET LICENSESWITCH:LICITEM="LKV3G5ADCF01",SWITCH=ENABLE;`

**步骤2: 创建N4接口跟踪任务**

在PGW-U/UPF上创建UDG N4接口跟踪任务，用于捕获PFCP信令。

**步骤3: 测试终端接入网络**

测试终端使用配置的APN接入网络。
- 成功接入 → 继续。
- 无法接入 → 调测UDG接入功能。

**步骤4: 触发应用识别**

测试终端浏览Web业务，访问 **www.huawei.com** 网页。

**步骤5: 验证APPLICATION_START上报**

检查PGW-U/UPF是否**立即**向PGW-C/SMF发送 `PFCP Session Report Request`：
- Event-Trigger为 **APPLICATION-START**
- 携带 **Application-Detection-Information AVP**
- Application-Detection-Information中包含 **TDF-Application-Identifier**（值为检测到的应用名）

验证结果：
- 上报信元正确 → ADC功能生效，继续步骤6。
- 未上报或信元不全 → ADC功能未生效，跳转步骤8排查。

**步骤6: 触发应用停止**

测试终端停止访问 www.huawei.com。

**步骤7: 验证APPLICATION_STOP上报**

检查PGW-U/UPF是否**立即**向PGW-C/SMF发送 `PFCP Session Report Request`：
- Event-Trigger为 **APPLICATION-STOP**
- 携带 **Application-Detection-Information AVP**（含TDF-Application-Identifier）

验证结果：
- 上报了应用终止事件 → 调测完成。
- 未上报 → 跳转步骤8排查。

### 6.4 ADC功能未生效的排查步骤

**步骤8: 检查PCRF/PCF是否下发了Event-Trigger**

查看 `PFCP Session Establishment Request` 消息，检查PCRF/PCF是否下发了APPLICATION-START和APPLICATION-STOP Event-Trigger。
- 是 → PCRF/PCF要求上报，继续步骤9。
- 否 → 联系PCRF/PCF工程师处理后重新调测。

**步骤9: 检查FlowFilter名称匹配**

```
LST RULE:;
LST RULEBINDING:USERPROFILENAME="up_test";
```
检查"流过滤器名称"是否与TDF-Application-Identifier值相同。
- 相同 → 继续步骤10。
- 不相同 → 修改为相同后重新调测。

> 可通过 `LST RULEBINDING` 查询规则名称，再通过 `LST RULE` 查询具体规则内容。

**步骤10: 检查PCC规则是否允许上报**

```
LST PCCPOLICYGRP:PCCPOLICYGRPNM="pg_ADC01";
```
检查"ADC静默通知标识"：
- **不使能（DISABLE）** → 允许上报，继续步骤11。
- **使能（ENABLE）** → 不允许上报，执行修改：
  ```
  MOD PCCPOLICYGRP:PCCPOLICYGRPNM="pg_ADC01",ADCMUTEFLAG=DISABLE;
  ```
  修改后重新调测。

**步骤11: 收集信息并寻求技术支持**

若以上步骤均未解决问题：
1. 执行 `EXP MML` 命令导出当前配置数据为MML脚本文件。
2. 收集并保存上述所有查询信息。
3. 收集N4接口跟踪数据。
4. 联系华为技术支持。

### 6.5 常见问题排查

| 问题 | 可能原因 | 排查方法 |
|------|---------|---------|
| ADC不上报应用事件 | License未打开 | `LST LICENSESWITCH:LICITEM="LKV3G5ADCF01";` |
| ADC不上报应用事件 | PCRF/PCF未下发Event-Trigger | 检查PFCP Session Establishment Request |
| ADC不上报应用事件 | FlowFilter名称不匹配 | `LST RULE` 检查流过滤器名称 |
| ADC不上报应用事件 | ADCMUTEFLAG=ENABLE | `LST PCCPOLICYGRP` 检查静默标识 |
| 上报延迟过长 | ADCHYSTTIMER过大 | `LST ADCPARA` 检查迟滞时间 |
| 流信息未上报 | FLOWINFORPT=DISABLE | `LST ADCPARA` 检查流信息上报开关 |
| 三网元FlowFilter不一致 | 动态规则模式下名称不匹配 | 检查PGW-C/SMF、PGW-U/UPF、PCRF/PCF配置 |
| 业务流被阻塞 | 缺少缺省rule | 配置L3/4=any、L7=any的rule |
| SA识别不到应用 | 特征库未加载 | `LOD SIGNATUREDB` 加载协议特征库 |

### 6.6 关键查询命令汇总

| 命令 | 用途 |
|------|------|
| `LST LICENSESWITCH:LICITEM="LKV3G5ADCF01";` | 查询ADC License开关 |
| `LST APN:;` | 查询APN配置 |
| `LST RULE:;` | 查询规则配置（含流过滤器名称） |
| `LST RULEBINDING:USERPROFILENAME="up_test";` | 查询用户模板与规则绑定 |
| `LST PCCPOLICYGRP:PCCPOLICYGRPNM="pg_ADC01";` | 查询PCC策略组（含ADC静默标识） |
| `LST ADCPARA:;` | 查询ADC参数配置 |
| `EXP MML:;` | 导出当前配置数据 |

---

## 7. 参考信息

### 7.1 接口与协议标准

| 标准类别 | 标准编号 | 标准名称 |
|----------|---------|---------|
| 3GPP | 23501 | System Architecture for the 5G System; Stage 2 |
| 3GPP | 23502 | Procedures for the 5G System; Stage 2 |
| 3GPP | 23503 | Policy and Charging Control Framework for the 5G System; Stage 2 |
| 3GPP | 29.244 | Interface between the Control Plane and the User Plane nodes |
| 3GPP | 29507 | 5G System; Access and Mobility Policy Control Service; Stage 3 |
| 3GPP | 29512 | 5G System; Session Management Policy Control Service; Stage 3 |
| 3GPP | 29513 | 5G System; Policy and Charging Control signalling flows and QoS parameter mapping; Stage 3 |

### 7.2 特性规格

| 规格名称 | 规格指标 |
|----------|---------|
| 允许配置自定义协议 | 5000个 |
| 允许配置预定义支持ADC上报的PCC规则 | 5000个 |
| 支持上报的并发Flow信息数 | 16个 |

### 7.3 License要求

- **本特性License**: `82200AFK LKV3G5ADCF01 增强的ADC基本功能`
- **依赖License**: `82209825 PCC 基本功能`（GWFD-020351）
- **依赖License**: SA相关特性License（共19个SA子特性，License控制项从82209749到82209771）

### 7.4 特性交互

| 交互类型 | 相关特性 | 控制项 | 交互说明 |
|----------|---------|--------|---------|
| **依赖** | SA相关特性（GWFD-110101 SA-Basic等19个子特性） | 82209749~82209771 | UDG基于SA执行业务检测，把检测结果上报给PCRF/PCF。开通ADC必须同时开启SA。 |
| **依赖** | GWFD-020351 PCC基本功能 | 82209825 | PCRF/PCF下发携带Application ID的PCC规则给UDG。开通ADC必须同时开启PCC。 |

### 7.5 对系统的影响

1. **性能影响**: 使能ADC后会对所有业务进行解析，报文转发性能和吞吐量将下降，具体下降程度需根据话务模型评估。
2. **信令负荷影响（N4/N7）**: ADC应用上报导致N4/N7接口信令增多，影响需根据话务模型评估。
3. **GTP信令负荷影响**: ADC应用上报触发PCRF/PCF更新承载控制，导致GnGp/S11/S5/S8接口GTP信令数增多。

### 7.6 应用限制

1. **重复Start事件处理**: 考虑N4/N7接口信令流控及链路故障等因素，PCRF/PCF可能未收到Stop事件而收到重复的Start事件，或只收到Stop事件。PCRF/PCF需能正确处理这些情况。
2. **动态规则要求**: 如果要根据UDG上报的流信息进行基于应用的策略控制和承载保障，要求PCRF/PCF能基于上报的指定应用的所有流信息生成一个动态规则。
3. **缺省rule建议**: UDG会丢弃匹配不到所有PCC rule的报文，建议配置一个三四层为any、七层协议为any的rule作为缺省配置。

### 7.7 发布历史

| 特性版本 | 发布版本 | 发布说明 |
|----------|---------|---------|
| 01 | 20.1.0 | 首次发布 |

---

## 8. 知识来源

| 序号 | 文档名称 | 原始路径 |
|------|---------|---------|
| 1 | GWFD-020357 增强的ADC基本功能参考信息 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020357 增强的ADC基本功能/GWFD-020357 增强的ADC基本功能参考信息_84866922.md` |
| 2 | GWFD-020357 增强的ADC基本功能特性概述 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020357 增强的ADC基本功能/GWFD-020357 增强的ADC基本功能特性概述_84866818.md` |
| 3 | 实现原理 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020357 增强的ADC基本功能/实现原理_84866819.md` |
| 4 | 激活增强的ADC基本功能 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020357 增强的ADC基本功能/激活增强的ADC基本功能_84866820.md` |
| 5 | 调测增强的ADC基本功能 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020357 增强的ADC基本功能/调测增强的ADC基本功能_84866921.md` |
