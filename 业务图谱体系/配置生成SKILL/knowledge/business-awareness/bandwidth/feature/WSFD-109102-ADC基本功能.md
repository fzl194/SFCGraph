# WSFD-109102 ADC基本功能 - 特性知识文档

> **场景归属**: 业务感知 → 带宽控制子场景（辅助特性：ADC应用检测，UNC侧）
> **产品**: UNC (SMF网元)
> **场景定位**: SMF接收ADC规则 → 下发UPF执行 → 识别结果上报 → 触发带宽控制
> **对应UDG特性**: GWFD-020357 增强的ADC基本功能

---

## 1. 特性概述

### 1.1 基本信息

| 属性 | 取值 |
|------|------|
| 特性ID | WSFD-109102 |
| 特性名称 | ADC基本功能 |
| 适用NF | GGSN-C、PGW-C、SMF |
| 涉及NF（配合网元） | PGW-U/UPF (UDG 20.2.0+), PCRF/PCF (无特殊要求), GGSN-C/PGW-C/SMF (UNC 20.5.0+) |
| License控制项 | `82200BNK LKV2BADCF01 ADC基本功能` |
| 首次发布版本 | UNC 20.5.0（特性版本01） |
| 遵循标准 | 3GPP 23501/23502/23503/29.244/29507/29512/29513 |

### 1.2 核心能力

ADC（Application Detection and Control）基本功能是UNC（GGSN-C/PGW-C/SMF）侧的应用检测与控制功能。PCC基本功能的动态规则只能对L3/L4的业务进行动态控制，不能对L7的业务动态控制。ADC基本功能使PCRF/PCF能够通过L7感知业务的变化，实现应用级精细化策略控制。

本特性中，PGW-U/UPF支持检测应用并向PCRF/PCF上报应用标识（Application Identifier）、流信息以及应用的起始或结束事件。PCRF/PCF根据上报的信息，结合用户签约信息、网络状态等信息，下发PCC策略；PGW-U/UPF基于PCC策略进行业务控制、流量上报等；GGSN-C/PGW-C/SMF执行承载/QoS Flow管理（创建新的承载/QoS Flow、更新已有承载/QoS Flow或删除旧的承载/QoS Flow）。

### 1.3 在带宽控制场景中的定位（辅助：控制面应用检测通道）

ADC基本功能是带宽控制场景中的**应用级策略触发通道**，UNC侧承担控制面中继角色。其关键作用链路：

```
PGW-U/UPF检测应用 → GGSN-C/PGW-C/SMF（UNC）转发检测信息给PCRF/PCF
→ PCRF/PCF根据应用类型 + 签约 + 网络状况下发PCC策略（含带宽/QoS）
→ GGSN-C/PGW-C/SMF下发到PGW-U/UPF
→ PGW-U/UPF执行业务控制、流量上报、带宽限速/整形
→ GGSN-C/PGW-C/SMF执行承载/QoS Flow管理
```

典型带宽控制应用场景：
- **业务流控**: PGW-U/UPF实时监测并上报用户使用的业务信息，PCRF/PCF综合用户签约信息、当前网络状况（如小区拥塞状况）下发指定业务的流控策略给PGW-U/UPF，实现对指定业务流量的带宽控制（如VoIP业务限速）。
- **高价值业务QoS保障**: PGW-U/UPF识别高价值业务（自营VoIP、视频共享、Mobile TV等），上报后PCRF/PCF下发携带不同QCI/ARP的PCC策略，GGSN-C/PGW-C/SMF触发专有承载/专有QoS Flow创建，为高价值业务提供差异化QoS保障。
- **页面重定向**: 当用户访问没有签约的业务时，PGW-U/UPF可将用户访问页面重定向到提醒页面，通知用户不可访问。用户访问重定向的页面进行业务订购，PCRF/PCF实时授权后用户可访问业务。

### 1.4 与GWFD-020357（UDG侧增强的ADC基本功能）的对应关系

WSFD-109102（UNC侧ADC基本功能）与GWFD-020357（UDG侧增强的ADC基本功能）构成ADC功能的控制面与用户面两半：

| 维度 | WSFD-109102（UNC侧） | GWFD-020357（UDG侧） |
|------|---------------------|---------------------|
| **网元** | GGSN-C/PGW-C/SMF（控制面） | PGW-U/UPF（用户面） |
| **核心职责** | 转发检测信息给PCRF/PCF；转发PCC策略给PGW-U/UPF；执行承载/QoS Flow管理 | 执行业务数据流检测（SA/DPI引擎）；上报应用标识/流信息/事件；执行PCC策略（业务控制/流量上报/带宽限速/整形） |
| **License控制项** | `LKV2BADCF01 ADC基本功能` | `LKV3G5ADCF01 增强的ADC基本功能` |
| **接口** | 与PCRF/PCF交互（Gx/N7）；与PGW-U/UPF交互（N4/PFCP） | 与GGSN-C/PGW-C/SMF交互（N4/PFCP） |
| **首发版本** | UNC 20.5.0 | UDG 20.1.0 |

两者配合：PGW-U/UPF负责检测和执行，GGSN-C/PGW-C/SMF负责转发和承载管理。

### 1.5 与BWM（WSFD-211005）的协作关系

在UNC侧，ADC基本功能与BWM（带宽管理）特性存在间接协作关系：
- ADC负责向PCRF/PCF**上报**应用识别结果，PCRF/PCF根据上报信息**决策**下发新的PCC策略（含带宽控制参数），策略经由GGSN-C/PGW-C/SMF转发给PGW-U/UPF。
- PGW-U/UPF的BWM模块负责**执行**带宽控制动作（限速、整形、门控）。
- 在UNC侧，ADC触发带宽控制策略的体现是GGSN-C/PGW-C/SMF发起专有承载/二次上下文/专有QoS Flow的创建、更新或去激活，从而调整用户面带宽。

### 1.6 与PCC基本功能（WSFD-109101）的依赖关系

ADC基本功能**依赖**PCC基本功能（License控制项 `82207979 PCC 基本功能`）。
- PCRF/PCF通过Gx/N7接口向PGW-C/SMF下发携带Application ID的PCC规则。
- PGW-C/SMF通过N4接口（PFCP协议）向PGW-U/UPF传递Application ID等信息。
- 开通ADC基本功能**必须同时开启**PCC基本功能。

---

## 2. 核心概念

### 2.1 ADC（Application Detection and Control）

ADC是本特性的核心机制，包含三个动作：
- **Detection（检测）**: PGW-U/UPF检测应用数据流（L7层），基于SA引擎（协议识别库和解析库）完成应用识别。
- **Reporting（上报）**: PGW-U/UPF将检测到的应用标识、流信息以及应用起始/结束事件，通过GGSN-C/PGW-C/SMF上报给PCRF/PCF。GGSN-C/PGW-C/SMF承担**透传/中继**角色。
- **Control（控制）**: PCRF/PCF根据上报信息下发PCC策略，GGSN-C/PGW-C/SMF执行承载/QoS Flow管理，PGW-U/UPF执行业务控制、流量上报等。

### 2.2 应用（Application）

"应用"是ADC功能中定义的名词，等同于PCC基本功能（WSFD-109101）中的"业务"。ADC围绕"应用"维度对业务数据流进行检测、上报和策略控制。

### 2.3 业务分类

| 业务类型 | 定义 | 特征 | 示例 |
|----------|------|------|------|
| **自营业务** | 运营商提供的业务 | 用户量占比低，与互联网类似应用相比没有竞争优势；通过差异化QoS保障吸引用户、提高收入 | 手机音乐下载、手机视频浏览、VoIP、视频共享、Mobile TV |
| **可推论业务** | 应用的流信息可识别，且业务持续时间长、并发业务流数量少的业务 | 推荐持续时间不小于3分钟，推荐并发业务流数量不超过16个；可上报Flow-Information | FTP、RTSP |
| **不可推论业务** | 五元组老化快、并发业务流数量多的业务 | 不上报Flow-Information（因流信息量大且老化快） | P2P、HTTP |

> 注意：很难简单通过协议名称判定某种业务是否为可推论业务，只有基于对协议的理解和分析才能判定和识别能否有效利用应用的流信息。

### 2.4 Gx接口ADC规则（4G/5G融合）

GGSN-C/PGW-C/SMF通过Gx接口与PCRF交互时，ADC规则通过Gx接口的Diameter AVP传递：

| Gx AVP / 信元 | 说明 |
|----------------|------|
| **PCC规则中的Application ID** | PCRF在CCA_Initial或CCA_Update消息中下发携带Application ID的PCC规则 |
| **APPLICATION_START Event-Trigger** | 应用数据流开始时触发上报 |
| **APPLICATION_STOP Event-Trigger** | 应用数据流终止时触发上报 |
| **Application-Detection-Information** | GGSN-C/PGW-C/SMF通过CCR_Update消息上报给PCRF的应用检测信息 |
| **TDF-Application-Identifier** | 应用标识（应用名），在Application-Detection-Information中携带 |
| **TDF-Application-Instance-Identifier** | 应用实例标识（可推论业务），与Flow-Information对应；使用后GGSN-C/PGW-C/SMF无需每次上报Flow-Information |
| **Flow-Information** | 流信息（五元组），仅可推论业务上报 |

### 2.5 N7接口ADC规则（纯5G）

GGSN-C/PGW-C/SMF通过N7接口与PCF交互时，ADC规则通过N7接口的服务化消息传递：

| N7信元 | 说明 |
|---------|------|
| **PCC规则中的application ID** | PCF在Npcf_SMPolicyControl_Create Response或Update Response/UpdateNotify Request中下发携带application ID的PCC规则 |
| **APP_STA Event-Trigger** | 应用数据流开始时触发上报（对应Gx的APPLICATION_START） |
| **APP_STO Event-Trigger** | 应用数据流终止时触发上报（对应Gx的APPLICATION_STOP） |
| **AppDetectionInfo** | GGSN-C/PGW-C/SMF通过Npcf_SMPolicyControl_Update Request向PCF上报的应用检测信息 |
| **appId** | 应用标识，在AppDetectionInfo中携带 |
| **instanceId** | 应用实例标识 |
| **sdfDescriptions** | SDF描述信息（流信息），对应Gx的Flow-Information |

### 2.6 Gx与N7接口关键差异对照

| 维度 | Gx接口（4G/5G融合） | N7接口（纯5G） |
|------|---------------------|----------------|
| **交互协议** | Diameter | 服务化接口（HTTP/JSON） |
| **策略请求消息** | CCR_Initial / CCR_Update | Npcf_SMPolicyControl_Create Request / Update Request |
| **策略响应消息** | CCA_Initial / CCA_Update | Npcf_SMPolicyControl_Create Response / Update Response / UpdateNotify Request |
| **应用开始触发器** | APPLICATION_START | APP_STA |
| **应用停止触发器** | APPLICATION_STOP | APP_STO |
| **检测信息信元** | Application-Detection-Information（含TDF-Application-Identifier/TDF-Application-Instance-Identifier/Flow-Information） | AppDetectionInfo（含appId/instanceId/sdfDescriptions） |
| **下发时机** | CCA_Initial或CCA_Update | Create Response或Update Response或UpdateNotify Request |

### 2.7 ADC特征库

ADC的识别能力依赖协议识别库和解析库，这些特征库需要加载到PGW-U/UPF侧。特征库管理属于SA业务感知专题范畴。GGSN-C/PGW-C/SMF不直接使用特征库，而是通过PCC规则中的Application ID间接关联到PGW-U/UPF本地配置的FlowFilter。

### 2.8 识别结果上报机制

在UNC侧，GGSN-C/PGW-C/SMF承担**透传角色**：
1. PGW-U/UPF检测到应用后，通过PFCP Session Report Request将检测信息发送给GGSN-C/PGW-C/SMF。
2. GGSN-C/PGW-C/SMF通过CCR_Update（Gx）或Npcf_SMPolicyControl_Update Request（N7）将应用检测信息及对应的Event-Trigger转发给PCRF/PCF。
3. GGSN-C/PGW-C/SMF从PCRF/PCF收到更新后的PCC策略后，通过PFCP消息下发给PGW-U/UPF。

### 2.9 Application ID与FlowFilter的映射

在GGSN-C/PGW-C/SMF上，PCRF/PCF通过动态规则下发的appid与本地配置的FlowFilter名称（FLOWFILTERNAME）必须一致。GGSN-C/PGW-C/SMF、PGW-U/UPF、PCRF/PCF三个网元上的该参数必须一致，否则无法正常上报。

---

## 3. 实现原理与流程

### 3.1 Gx接口ADC实现原理

当GGSN-C/PGW-C/SMF通过Gx接口与PCRF交互时，ADC基本功能的工作原理如下：

**核心机制**: PCRF下发Application ID → GGSN-C/PGW-C/SMF转发给PGW-U/UPF → PGW-U/UPF根据Application ID关联业务报文的特征（Filter/L7 Filter） → 实现PCRF对L7业务的动态控制。

**数据流向**:
1. PCRF向GGSN-C/PGW-C/SMF下发携带Application ID的PCC规则及应用起始/结束的事件触发器。
2. GGSN-C/PGW-C/SMF向PGW-U/UPF传递携带Application ID的PCC规则及应用起始/结束的事件触发器。
3. PGW-U/UPF进行业务识别，并向PCRF/PCF上报检测到的应用信息及起始/结束事件。
4. PCRF根据PGW-U/UPF上报的应用信息及应用的起始或结束事件进行策略决策，下发更新后的PCC策略。
5. GGSN-C/PGW-C/SMF和PGW-U/UPF根据更新后的PCC策略进行处理。

### 3.2 N7接口ADC实现原理

当GGSN-C/PGW-C/SMF通过N7接口与PCF交互时，ADC基本功能的工作原理与Gx接口完全对应，区别仅在于接口协议和信元命名：

**核心机制**: PCF下发application ID → GGSN-C/PGW-C/SMF转发给PGW-U/UPF → PGW-U/UPF根据application ID关联业务报文的特征 → 实现PCF对L7业务的动态控制。

**数据流向**:
1. PCF向GGSN-C/PGW-C/SMF下发携带application ID的PCC规则及APP_STA/APP_STO事件触发器。
2. GGSN-C/PGW-C/SMF向PGW-U/UPF传递携带application ID的PCC规则及APP_STA/APP_STO事件触发器。
3. PGW-U/UPF进行业务识别，上报检测结果给GGSN-C/PGW-C/SMF。
4. GGSN-C/PGW-C/SMF通过Npcf_SMPolicyControl_Update Request向PCF上报。
5. PCF下发更新后的PCC策略。

### 3.3 Gx接口完整业务流程

#### 阶段1: 初始激活

1. 用户发起IP-CAN Session建立。
2. GGSN-C/PGW-C/SMF向PCRF发送CCR_Initial消息请求策略。
3. PCRF在CCA_Initial响应消息中下发携带application ID的PCC规则，并向GGSN-C/PGW-C/SMF下发APPLICATION_START和APPLICATION_STOP Event-Trigger，要求检测到application ID对应的数据流时需上报给PCRF。
   - PCRF也可以在任何CCA_Update消息中下发这两个Event-Trigger或携带application ID的PCC规则。
4. GGSN-C/PGW-C/SMF向PGW-U/UPF发送PFCP Session Establishment Request消息，携带application ID的PCC规则及APPLICATION_START和APPLICATION_STOP Event-Trigger。
5. PGW-U/UPF安装规则等并向GGSN-C/PGW-C/SMF返回PFCP Session Establishment Response消息。

#### 阶段2: 用户开始使用应用（触发带宽控制策略）

1. PGW-U/UPF检测到该应用数据流已经开始。
2. PGW-U/UPF将检测信息发送给GGSN-C/PGW-C/SMF。
3. GGSN-C/PGW-C/SMF通过CCR_Update消息向PCRF上报应用检测信息Application-Detection-Information，以及APPLICATION_START Event-Trigger。
4. PCRF根据GGSN-C/PGW-C/SMF上报的应用检测信息，结合用户签约数据，下发更新后的PCC策略。
5. GGSN-C/PGW-C/SMF根据PCRF下发的新PCC策略，可能发起以下操作：
   - **专有承载（或二次上下文）/专有QoS Flow创建**: 当PCRF对应用数据流分配GBR（QCI/ARP和带宽，或5QI/ARP和带宽），且当前不存在对应的上下文或专有承载/专有QoS Flow时。
   - **更新承载/上下文的带宽或QoS Flow的带宽**: 调整已有承载的QoS参数。
   - GGSN-C/PGW-C/SMF将新的PCC策略下发给PGW-U/UPF。
6. PGW-U/UPF对后续业务流执行新的PCC策略。

#### 阶段3: 用户停止使用应用（带宽控制恢复）

1. 用户使用一段时间业务后，停止使用该业务。PGW-U/UPF检测到应用数据流终止，向GGSN-C/PGW-C/SMF发送应用检测信息和APPLICATION_STOP Event-Trigger。
2. GGSN-C/PGW-C/SMF向PCRF发送应用检测信息和APPLICATION_STOP Event-Trigger。
   - Application-Detection-Information中携带TDF-Application-Identifier/TDF-Application-Instance-Identifier（可推论业务）。
   - TDF-Application-Instance-Identifier与Flow-Information对应，使用TDF-Application-Instance-Identifier后，GGSN-C/PGW-C/SMF无需每次上报Flow-Information。
   - **重要**: 如果用户业务匹配的携带Application ID的PCC规则被删除或失效，后续业务停止后**不再向PCRF上报APPLICATION_STOP事件**。
3. PCRF根据GGSN-C/PGW-C/SMF上报的应用检测信息，结合用户签约业务，下发新的PCC策略。
4. GGSN-C/PGW-C/SMF根据PCRF下发的新PCC策略，可能发起二次上下文/专有承载/专有QoS Flow的去激活，或发起上下文/承载/QoS Flow的更新。
   - 例如PCRF可能删除之前下发的PCC规则，GGSN-C/PGW-C/SMF发起二次上下文/专有承载/专有QoS Flow的去激活。

### 3.4 N7接口完整业务流程

#### 阶段1: 初始激活

1. 用户发起IP-CAN Session建立。
2. GGSN-C/PGW-C/SMF向PCF发送Npcf_SMPolicyControl_Create Request消息请求策略。
3. PCF在Npcf_SMPolicyControl_Create Response响应消息中下发携带application ID的PCC规则，并向GGSN-C/PGW-C/SMF下发APP_STA和APP_STO Event-Trigger，要求检测到application ID对应的数据流时需上报给PCF。
   - PCF也可以在任何Npcf_SMPolicyControl_Update Response消息或Npcf_SMPolicyControl_UpdateNotify Request消息中下发这两个Event-Trigger或携带application ID的PCC规则。
4. GGSN-C/PGW-C/SMF向PGW-U/UPF发送PFCP Session Establishment Request消息，携带application ID的PCC规则及APP_STA和APP_STO Event-Trigger。
5. PGW-U/UPF安装规则等并向GGSN-C/PGW-C/SMF返回PFCP Session Establishment Response消息。

#### 阶段2: 用户开始使用应用

1. PGW-U/UPF检测到该应用数据流已经开始。
2. PGW-U/UPF将检测信息发送给GGSN-C/PGW-C/SMF。
3. GGSN-C/PGW-C/SMF通过Npcf_SMPolicyControl_Update Request消息向PCF上报应用检测信息Application-Detection-Information，以及APP_STA Event-Trigger。
4. PCF根据GGSN-C/PGW-C/SMF上报的应用检测信息，结合用户签约数据，下发更新后的PCC策略。
5. GGSN-C/PGW-C/SMF根据PCF下发的新PCC策略，可能发起专有承载（或二次上下文）/专有QoS Flow创建，或者更新承载/上下文的带宽或QoS flow的带宽。
   - 例如PCF可能对应用数据流分配GBR（QCI/ARP和带宽，或5QI/ARP和带宽），如当前不存在对应的上下文或专有承载/专有QoS Flow，GGSN-C/PGW-C/SMF发起新的二次上下文/专有承载/专有QoS Flow的创建。
   - GGSN-C/PGW-C/SMF将新的PCC策略下发给PGW-U/UPF。
6. PGW-U/UPF对后续业务流执行新的PCC策略。

#### 阶段3: 用户停止使用应用

1. 用户使用一段时间业务后停止使用。PGW-U/UPF检测到应用数据流终止，向GGSN-C/PGW-C/SMF发送应用检测信息和APP_STO Event-Trigger。
2. GGSN-C/PGW-C/SMF向PCF发送应用检测信息和APP_STO Event-Trigger。
   - AppDetectionInfo中携带appId、instanceId和sdfDescriptions。
   - **重要**: 如果用户业务匹配的携带Application ID的PCC规则被删除或失效，后续业务停止后**不再向PCF上报APPLICATION_STOP事件**。
3. PCF根据GGSN-C/PGW-C/SMF上报的应用检测信息，结合用户签约业务，下发新的PCC策略。
4. GGSN-C/PGW-C/SMF根据PCF下发的新PCC策略，可能发起二次上下文/专有承载/专有QoS Flow的去激活或更新。

### 3.5 端到端完整流程图（文字版）

```
[Gx接口 - 4G/5G融合场景]

[初始激活阶段]
UE ──IP-CAN Session建立──> GGSN-C/PGW-C/SMF ──CCR_Initial──> PCRF
PCRF ──CCA_Initial（携带App ID的PCC规则 + APPLICATION_START/STOP）──> GGSN-C/PGW-C/SMF
GGSN-C/PGW-C/SMF ──PFCP Session Establishment Request──> PGW-U/UPF
PGW-U/UPF ──PFCP Session Establishment Response──> GGSN-C/PGW-C/SMF

[应用开始阶段]
UE ──应用数据流──> PGW-U/UPF（检测到应用）
PGW-U/UPF ──PFCP Session Report Request──> GGSN-C/PGW-C/SMF
GGSN-C/PGW-C/SMF ──CCR_Update（Application-Detection-Information + APPLICATION_START）──> PCRF
PCRF ──新PCC策略（含QoS/带宽）──> GGSN-C/PGW-C/SMF
GGSN-C/PGW-C/SMF ──创建专有承载/二次上下文/专有QoS Flow──> PGW-U/UPF
PGW-U/UPF ──执行新的PCC策略──> 后续业务流

[应用停止阶段]
UE ──应用数据流终止──> PGW-U/UPF
PGW-U/UPF ──PFCP Session Report Request（APPLICATION_STOP）──> GGSN-C/PGW-C/SMF
GGSN-C/PGW-C/SMF ──CCR_Update（Application-Detection-Information + APPLICATION_STOP）──> PCRF
PCRF ──新PCC策略（可能删除PCC规则）──> GGSN-C/PGW-C/SMF
GGSN-C/PGW-C/SMF ──去激活专有承载/二次上下文/专有QoS Flow──> PGW-U/UPF
```

```
[N7接口 - 纯5G场景]

[初始激活阶段]
UE ──PDU Session建立──> SMF ──Npcf_SMPolicyControl_Create Request──> PCF
PCF ──Create Response（携带app ID的PCC规则 + APP_STA/APP_STO）──> SMF
SMF ──PFCP Session Establishment Request──> UPF
UPF ──PFCP Session Establishment Response──> SMF

[应用开始阶段]
UE ──应用数据流──> UPF（检测到应用）
UPF ──PFCP Session Report Request──> SMF
SMF ──Npcf_SMPolicyControl_Update Request（AppDetectionInfo + APP_STA）──> PCF
PCF ──新PCC策略（含QoS/带宽）──> SMF
SMF ──创建专有QoS Flow──> UPF
UPF ──执行新的PCC策略──> 后续业务流

[应用停止阶段]
UE ──应用数据流终止──> UPF
UPF ──PFCP Session Report Request（APP_STO）──> SMF
SMF ──Npcf_SMPolicyControl_Update Request（AppDetectionInfo + APP_STO）──> PCF
PCF ──新PCC策略（可能删除PCC规则）──> SMF
SMF ──去激活专有QoS Flow──> UPF
```

### 3.6 UNC侧在ADC链路中的核心职责

GGSN-C/PGW-C/SMF在ADC链路中承担以下核心职责：
1. **转发应用检测信息**: 将从PGW-U/UPF收到的应用标识（Application Identifier）、流信息以及应用的起始或结束事件，转发给PCRF/PCF。
2. **SDF与QoS流绑定**: 根据从PCRF/PCF收到的会话管理策略，将SDF（Service Data Flow）与QoS流绑定。
3. **转发会话管理策略**: 将从PCRF/PCF收到的会话管理策略，转发给PGW-U/UPF。
4. **承载/QoS Flow管理**: 根据PCC策略变化，发起专有承载/二次上下文/专有QoS Flow的创建、更新或去激活。

---

## 4. 配置规则

### 4.1 涉及的MML命令总览

本特性涉及以下MML命令（按配置逻辑分组）：

| 分组 | 命令 | 用途 |
|------|------|------|
| **License管理** | `SET LICENSESWITCH` | 打开LKV2BADCF01 License开关 |
| **License查询** | `LST LICENSESWITCH` | 查询License开关状态 |
| **流过滤器配置** | `ADD FLOWFILTER` | 创建流过滤器（定义ADC业务使用的appid） |
| **ADC参数配置** | `ADD ADCPARA` | 配置ADC参数（流信息上报开关等） |
| **规则配置** | `ADD RULE` | 配置预定义规则（策略类型为ADC） |
| **用户模板配置** | `ADD USERPROFILE` | 配置用户模板 |
| **用户模板组配置** | `ADD USRPROFGROUP` | 配置用户模板组 |
| **规则绑定** | `ADD RULEBINDING` | 将规则绑定到用户模板 |
| **APN用户模板组绑定** | `ADD APNUSRPROFG` | 配置APN与用户模板组的绑定关系 |
| **PCC功能查询** | `LST APNPCCFUNC` | 查询APN PCC功能配置 |
| **PCC功能查询** | `LST PCCFUNC` | 查询PCC公共参数配置 |
| **规则查询** | `LST RULE` | 查询规则配置 |
| **规则绑定查询** | `LST RULEBINDING` | 查询用户模板和规则的绑定关系 |
| **APN查询** | `LST APN` | 查询APN配置 |
| **配置导出** | `EXP MML` | 导出当前配置数据为MML脚本文件 |

### 4.2 配置前置条件

- 完成UNC初始配置。
- 完成加载License。
- 完成激活PCC基本功能（WSFD-109101）。
- GGSN-C/PGW-C/SMF与PCRF/PCF之间通信正常。
- GGSN-C/PGW-C/SMF与PGW-U/UPF之间通信正常。

### 4.3 配置路径一：PCRF/PCF通过动态规则下发appid

当PCRF/PCF通过动态规则下发appid时（PCRF/PCF负责下发应用Start和Stop的Event-Trigger），UNC侧需要：

**步骤1: 打开License配置开关**

```
SET LICENSESWITCH:LICITEM="LKV2BADCF01",SWITCH=ENABLE;
```

**步骤2: 配置ADC业务使用的appid（流过滤器）**

```
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_ADC01";
```

- `FLOWFILTERNAME`: 流过滤器名称，不同流过滤器之间不能重复。
- **关键约束**: GGSN-C/PGW-C/SMF、PGW-U/UPF、PCRF/PCF三个网元上的该参数必须一致，否则无法正常上报。

**步骤3: 配置ADC参数**

```
ADD ADCPARA:FLOWFILTERNAME="flowfilter_ADC01",FLOWINFORPT=ENABLE;
```

- `FLOWFILTERNAME`: 使用`ADD FLOWFILTER`命令定义的流过滤器名称。
- `FLOWINFORPT`: 流信息上报开关。`ENABLE`=PCRF/PCF需要获取流信息时设置；默认取值为`DISABLE`。

### 4.4 配置路径二：PCRF/PCF不通过动态规则下发appid

当PCRF/PCF通过预定义规则下发APPLICATION_START和APPLICATION_STOP Event-Trigger时（不通过动态规则下发appid），UNC侧需要：

**步骤1: 打开License配置开关**

```
SET LICENSESWITCH:LICITEM="LKV2BADCF01",SWITCH=ENABLE;
```

**步骤2: 配置SMF上的本地rule（可选）**

```
ADD RULE:RULENAME="rule_test",POLICYTYPE=ADC;
```

- `RULENAME`: 规则名称，存在多条数据时，该参数+策略类型不能完全相同。
- `POLICYTYPE`: 策略类型，ADC场景固定取值为`ADC`。

**步骤3: 配置UserProfile并将rule绑定到UserProfile（可选）**

```
ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC;
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
```

- `USERPROFILENAME`: 用户模板名称，全网规划。
- `UPTYPE`: 用户模板类型，PCC场景固定取值为`PCC`。
- `ADD RULEBINDING`: 将本地rule或预定义规则rule绑定到UserProfile上。

### 4.5 两条配置路径的对比

| 维度 | 动态规则下发appid | 预定义规则下发Event-Trigger |
|------|------------------|---------------------------|
| **规则来源** | PCRF/PCF通过动态规则下发 | 本地预定义规则 |
| **UNC侧配置** | FLOWFILTER + ADCPARA | RULE(POLICYTYPE=ADC) + USERPROFILE + RULEBINDING |
| **appid来源** | PCRF/PCF动态下发 | PCRF/PCF下发Event-Trigger，appid由预定义规则指定 |
| **流信息上报** | 由ADCPARA的FLOWINFORPT控制 | UPF决定是否上报流信息，GGSN-C/PGW-C/SMF负责透传 |
| **三网元一致性要求** | FLOWFILTERNAME在GGSN-C/PGW-C/SMF、PGW-U/UPF、PCRF/PCF上必须一致 | 规则标识/规则组标识在UPF/SMF/PCF上必须一致 |

### 4.6 相关软件参数

| 软参 | 说明 |
|------|------|
| **BIT1916** | 控制Gx接口ADC上报时，同一应用已经产生但尚未上报的start和stop事件是否仍然上报。用于处理信令流控或链路故障场景下的事件可靠性。 |

### 4.7 计费与临时流量处理

在应用识别完成之前，信令报文或业务报文的临时流量处理规则：
1. 优先选择使用匹配到优先级最高的rule的L3/L4中的计费信息。
2. 其次选择使用common-policy（对应UserProfile中的配置）中配置的缺省计费信息。
3. 由于配置可选，如果上述配置无法获取，为了应用识别能够正常完成，允许临时流量通过，**不进行计费**。

---

## 5. 配置案例

### 5.1 案例一：PCRF通过动态规则下发appid并获取流信息

**场景描述**: 运营商希望对特定应用（如某VoIP应用）实施差异化带宽控制。PCRF通过动态规则下发appid，当UPF检测到该应用开始/结束时上报给PCRF，且PCRF需要获取流信息用于生成动态QoS规则。

**数据规划**:

| 参数 | 取值 | 说明 |
|------|------|------|
| License控制项 | LKV2BADCF01 | ADC基本功能License开关 |
| 流过滤器名称 | flowfilter_ADC01 | 三网元必须一致 |
| 流信息上报开关 | ENABLE | PCRF需要获取流信息 |
| APN名称 | apn-test | 测试终端使用的APN |
| IMSI | 460000123456789 | 测试终端IMSI |

**完整命令序列**:

```bash
// 步骤1: 打开ADC基本功能License开关
SET LICENSESWITCH:LICITEM="LKV2BADCF01",SWITCH=ENABLE;

// 步骤2: 配置ADC业务使用的appid（流过滤器）
// 注意: flowfilter_ADC01在GGSN-C/PGW-C/SMF、PGW-U/UPF、PCRF/PCF上必须一致
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_ADC01";

// 步骤3: 配置ADC参数，开启流信息上报
ADD ADCPARA:FLOWFILTERNAME="flowfilter_ADC01",FLOWINFORPT=ENABLE;
```

**后续流程说明**:
1. PCRF在CCA_Initial或CCA_Update中下发携带`flowfilter_ADC01`对应appid的PCC规则和APPLICATION_START/STOP触发器。
2. GGSN-C/PGW-C/SMF将PCC规则和触发器通过PFCP Session消息传递给PGW-U/UPF。
3. 当用户开始使用该VoIP应用时，PGW-U/UPF检测到应用数据流开始，上报检测信息给GGSN-C/PGW-C/SMF。
4. GGSN-C/PGW-C/SMF通过CCR_Update消息向PCRF上报Application-Detection-Information（含TDF-Application-Identifier、TDF-Application-Instance-Identifier和Flow-Information）及APPLICATION_START Event-Trigger。
5. PCRF根据上报信息下发新的PCC策略（如分配GBR、创建专有承载）。
6. GGSN-C/PGW-C/SMF发起专有承载/二次上下文/专有QoS Flow创建，并将策略下发给PGW-U/UPF执行。
7. 用户停止使用应用后，PGW-U/UPF检测到终止，触发APPLICATION_STOP上报链路，PCRF可能删除PCC规则，GGSN-C/PGW-C/SMF发起去激活。

### 5.2 案例二：PCF通过预定义规则下发APP_STA/APP_STO（N7接口）

**场景描述**: 运营商在纯5G场景下，PCF通过预定义规则下发APP_STA和APP_STO Event-Trigger。当UPF检测到appid对应的业务开始/结束时上报给PCF。UPF决定是否上报流信息，GGSN-C/PGW-C/SMF负责透传流信息。

**数据规划**:

| 参数 | 取值 | 说明 |
|------|------|------|
| License控制项 | LKV2BADCF01 | ADC基本功能License开关 |
| 规则名称 | rule_test | 预定义规则名称 |
| 策略类型 | ADC | 固定取值 |
| 用户模板名称 | up_test | UserProfile名称 |
| 用户模板类型 | PCC | 固定取值 |
| APN名称 | apn-test | 测试终端使用的APN |

**完整命令序列**:

```bash
// 步骤1: 打开ADC基本功能License开关
SET LICENSESWITCH:LICITEM="LKV2BADCF01",SWITCH=ENABLE;

// 步骤2: 配置预定义规则（策略类型为ADC）
ADD RULE:RULENAME="rule_test",POLICYTYPE=ADC;

// 步骤3: 配置UserProfile
ADD USERPROFILE:USERPROFILENAME="up_test",UPTYPE=PCC;

// 步骤4: 将rule绑定到UserProfile
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
```

**后续流程说明**:
1. PCF在Npcf_SMPolicyControl_Create Response或Npcf_SMPolicyControl_UpdateNotify Request中下发APP_STA和APP_STO Event-Trigger。
2. SMF将规则和触发器通过PFCP Session消息传递给UPF。
3. 当用户开始使用应用时，UPF检测到应用数据流开始，上报检测信息给SMF。
4. SMF通过Npcf_SMPolicyControl_Update Request向PCF上报AppDetectionInfo（含appId、instanceId和sdfDescriptions）及APP_STA Event-Trigger。
5. PCF下发更新后的PCC策略，SMF发起专有QoS Flow创建或更新。
6. 用户停止使用应用后，UPF检测到终止，触发APP_STO上报链路。

### 5.3 案例三：Gx接口高价值自营业务QoS保障

**场景描述**: 运营商为自营VoIP业务提供高价值QoS保障。PCRF通过Gx接口下发携带appid的PCC规则，当PGW-U/UPF检测到自营VoIP业务时上报给PCRF，PCRF下发携带GBR的PCC策略，GGSN-C/PGW-C/SMF创建专有承载/专有QoS Flow。

**数据规划**:

| 参数 | 取值 | 说明 |
|------|------|------|
| License控制项 | LKV2BADCF01 | ADC基本功能License开关 |
| 流过滤器名称 | flowfilter_self_voip | 自营VoIP应用标识 |
| 流信息上报开关 | ENABLE | PCRF需要获取流信息生成动态规则 |

**完整命令序列**:

```bash
// 步骤1: 打开ADC基本功能License开关
SET LICENSESWITCH:LICITEM="LKV2BADCF01",SWITCH=ENABLE;

// 步骤2: 配置自营VoIP业务的appid
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_self_voip";

// 步骤3: 配置ADC参数，开启流信息上报
ADD ADCPARA:FLOWFILTERNAME="flowfilter_self_voip",FLOWINFORPT=ENABLE;
```

**带宽控制触发链路**:
1. PCRF下发携带`flowfilter_self_voip`对应appid的PCC规则 + APPLICATION_START/STOP。
2. GGSN-C/PGW-C/SMF转发给PGW-U/UPF。
3. 用户使用自营VoIP时，PGW-U/UPF检测到应用 → 上报 → GGSN-C/PGW-C/SMF转发给PCRF。
4. PCRF下发携带GBR（QCI/ARP和带宽）的PCC策略。
5. GGSN-C/PGW-C/SMF发起新的专有承载/二次上下文/专有QoS Flow创建（因为当前不存在对应的上下文或专有承载/专有QoS Flow）。
6. PGW-U/UPF对后续业务流执行QoS保障策略。
7. 用户停止使用后，APPLICATION_STOP上报 → PCRF删除PCC规则 → GGSN-C/PGW-C/SMF发起去激活。

---

## 6. 验证与调测

### 6.1 调测前提条件

- 已完成激活ADC基本功能（配置License开关、FlowFilter/ADCPARA或Rule/UserProfile/RULEBINDING）。
- 已完成激活PCC基本功能（WSFD-109101）。
- GGSN-C/PGW-C/SMF与PCRF/PCF之间通信正常。
- GGSN-C/PGW-C/SMF与PGW-U/UPF之间通信正常。

### 6.2 调测数据准备

| 类别 | 参数名称 | 取值样例 | 获取方法 |
|------|----------|----------|----------|
| 用户信息查询 | IMSI号码 | 460000123456789 | 测试终端自带 |
| 测试终端APN | APN名称 | apn-test | 已配置数据中获取，可用`LST APN`命令查询 |

### 6.3 调测操作步骤

**步骤1: 进入MML命令行窗口**

进入"MML命令行-UNC"窗口。

**步骤2: 验证License开关**

```
LST LICENSESWITCH:LICITEM="LKV2BADCF01";
```

- 如果`SWITCH`为`ENABLE`，继续步骤3。
- 如果`SWITCH`为`DISABLE`，执行`SET LICENSESWITCH:LICITEM="LKV2BADCF01",SWITCH=ENABLE;`打开开关。

**步骤3: 创建用户跟踪任务**

创建用户跟踪任务，消息类型选择**N4、Gx和N7**。

> 以SMF与PCF之间是N7接口为例进行描述。如实际使用的是Gx接口，触发器为APPLICATION_START和APPLICATION_STOP，交互消息为CCR和CCA。

**步骤4: 验证SMF是否从PCF获取到ADC规则**

测试终端使用`apn-test`接入网络，观测SMF是否从PCF获取到ADC规则：
- **动态规则**: appid / APP_STA / APP_STO
- **预定义规则**: APP_STA / APP_STO

- 是 → 继续步骤5。
- 否 → 跳转故障排查（步骤8）。

**步骤5: 验证SMF是否向UPF正确下发ADC规则**

观测SMF是否向UPF正确下发了从PCF获取的ADC规则。

- 是 → 继续步骤6。
- 否 → 跳转故障排查（步骤8）。

**步骤6: 验证应用检测上报**

测试终端访问appid对应的业务（如URL为www.example.com），观测SMF是否收到UPF上报的应用检测信息及APP_STA trigger。

- 是 → 继续步骤7。
- 否 → 跳转故障排查（步骤8）。

**步骤7: 验证应用停止上报**

测试终端结束appid对应的业务，观测SMF是否向PCF上报应用检测信息及APP_STO trigger。

- 是 → 调测结束。
- 否 → 跳转故障排查（步骤8）。

### 6.4 故障排查流程

当步骤4-7中出现异常时，执行以下排查步骤：

**排查步骤8a: 检查PCC功能是否开启**

```
LST APNPCCFUNC:;
LST PCCFUNC:;
```

- 检查是否开启PCC功能。
  - 是（动态规则） → 继续排查步骤8b。
  - 是（预定义规则组） → 继续排查步骤8c。
  - 是（预定义规则） → 继续排查步骤8d。
  - 否 → 参考激活PCC基本功能（WSFD-109101）重新配置。

**排查步骤8b: 检查PCF下发的appid与UPF/SMF上的FLOWFILTER名称是否一致**

- PCF通过动态规则下发appid/APP_STA/APP_STO时，PCF上的appid和UPF/SMF上的FLOWFILTER名称**必须一致**。
  - 是 → 跳转步骤9。
  - 否 → 修改为相同后重新测试。

**排查步骤8c: 检查UserProfile绑定的Rule是否正确**

```
LST RULEBINDING:;
```

- PCF通过预定义规则组下发APP_STA/APP_STO时，UPF/SMF/PCF上的规则组标识**必须一致**。
  - 是 → 继续排查步骤8d。
  - 否 → 执行`RMV RULEBINDING`后重新执行`ADD RULEBINDING`。

**排查步骤8d: 检查Rule配置是否正确**

```
LST RULE:;
```

- PCF通过预定义规则下发APP_STA/APP_STO时，UPF/SMF/PCF上的规则标识**必须一致**。
  - 是 → 跳转步骤9。
  - 否 → 执行`RMV RULEBINDING` + `RMV RULE`后重新执行`ADD RULE` + `ADD RULEBINDING`。

**排查步骤9: 联系华为技术支持**

如果上述排查均无法解决问题：
1. 重新执行上述步骤并保存报文。
2. 执行`EXP MML`命令将当前配置数据导出为MML脚本文件并保存。
3. 收集并保存上述所有查询信息。
4. 收集归纳所有信息并联系华为技术支持解决。

### 6.5 常见问题排查

| 问题现象 | 可能原因 | 排查方法 |
|----------|----------|----------|
| SMF未从PCF获取ADC规则 | PCC功能未开启 | 执行`LST APNPCCFUNC`和`LST PCCFUNC`检查PCC功能 |
| SMF收到ADC规则但未下发UPF | PFCP Session建立失败 | 检查SMF与UPF之间的通信状态 |
| UPF未上报应用检测信息 | appid与FLOWFILTER名称不一致 | 检查PCF上的appid与UPF/SMF上的FLOWFILTER名称是否一致 |
| UPF未上报应用检测信息 | 预定义规则/规则组标识不一致 | 执行`LST RULE`和`LST RULEBINDING`检查规则配置 |
| APPLICATION_STOP未上报 | PCC规则已被删除或失效 | 检查携带Application ID的PCC规则是否仍有效 |
| 重复收到Start事件或仅收到Stop事件 | N4/N7接口信令流控或链路故障 | PCRF/PCF需要能够正确处理这些情况 |

---

## 7. 参考信息

### 7.1 遵循标准

| 标准类别 | 标准编号 | 标准名称 |
|----------|----------|----------|
| 3GPP | 23501 | System Architecture for the 5G System; Stage 2 |
| 3GPP | 23502 | Procedures for the 5G System; Stage 2 |
| 3GPP | 23503 | Policy and Charging Control Framework for the 5G System; Stage 2 |
| 3GPP | 29.244 | Interface between the Control Plane and the User Plane nodes |
| 3GPP | 29507 | 5G System; Access and Mobility Policy Control Service; Stage 3 |
| 3GPP | 29512 | 5G System; Session Management Policy Control Service; Stage 3 |
| 3GPP | 29513 | 5G System; Policy and Charging Control signalling flows and QoS parameter mapping; Stage 3 |

### 7.2 特性交互关系

| 交互类型 | 相关特性 | 控制项名称 | 交互说明 |
|----------|----------|------------|----------|
| **依赖** | WSFD-109101 PCC基本功能 | 82207979 PCC 基本功能 | PCRF/PCF通过Gx/N7接口向PGW-C/SMF下发携带Application ID的PCC规则，PGW-C/SMF通过N4接口向PGW-U/UPF传递Application ID等信息，开通ADC基本功能必须同时开启PCC基本功能 |
| **配合（用户面）** | GWFD-020357 增强的ADC基本功能 | LKV3G5ADCF01 增强的ADC基本功能 | UDG侧执行实际应用检测、策略执行和带宽控制；UNC侧负责转发和承载管理 |
| **配合（带宽控制）** | WSFD-211005 / GWFD-110311 基于业务感知的带宽控制 | - | ADC识别应用后触发PCC策略变更，BWM在用户面执行带宽控制动作 |

### 7.3 License要求

| NF | License控制项 | 说明 |
|----|--------------|------|
| GGSN-C/PGW-C/SMF | `82200BNK LKV2BADCF01 ADC基本功能` | 本特性必须获得License许可 |
| PGW-U/UPF | `82200AFK LKV3G5ADCF01 增强的ADC基本功能` | 用户面ADC功能（GWFD-020357） |

### 7.4 对系统的影响

- **N4/N7接口信令负荷**: ADC应用上报会导致N4/N7接口信令增多，对N4/N7接口信令负荷的影响需要根据话务模型来评估。
- **GTP信令负荷**: ADC应用上报触发PCRF/PCF更新承载控制，会导致GnGp/S11/S5/S8接口的GTP信令数增多，对GTP信令负荷的影响需要根据话务模型和实施的业务特性来评估。
- 详细性能影响需要基于流量模型进行评估，请联系华为技术支持获取服务。

### 7.5 应用限制

1. **信令流控容错**: 考虑到N4/N7接口信令流控以及链路故障等因素，PCRF/PCF可能没有收到GGSN-C/PGW-C/SMF发送的应用的Stop事件，而收到GGSN-C/PGW-C/SMF重复发送的同一个应用的Start事件，或者PCRF/PCF只收到GGSN-C/PGW-C/SMF发送的某个应用的Stop事件，PCRF/PCF要能够正确处理这些情况。

2. **基于流信息的策略控制**: 如果要根据PGW-U/UPF上报的流信息进行基于应用的策略控制和承载保障，要求PCRF/PCF能基于PGW-U/UPF上报的指定应用的所有流信息生成一个动态规则，通过该动态规则下发指定应用的QoS。

3. **缺省规则配置**: PGW-U/UPF会丢弃匹配不到所有PCC rule的报文，因此建议在PGW-U/UPF上配置一个三四层为any、七层协议为any的rule作为缺省配置。

### 7.6 软件参数

| 软参 | 作用 |
|------|------|
| **BIT1916** | 控制Gx接口ADC上报时，同一应用已经产生但尚未上报的start和stop事件是否仍然上报 |

### 7.7 发布历史

| 特性版本 | 发布版本 | 发布说明 |
|----------|----------|----------|
| 01 | 20.5.0 | 首次发布 |

### 7.8 特性规格

本特性无特殊规格。

---

## 8. 知识来源

### 8.1 源文档清单

| 序号 | 文档名称 | 文档ID | 内容概述 |
|------|----------|--------|----------|
| 1 | 特性概述_92582134.md | DOC-WSFD-109102-01 | 特性定义、客户价值、应用场景、可获得性、特性交互、对系统影响、应用限制、原理概述、计费与话单、特性规格、遵循标准、发布历史 |
| 2 | 实现原理(Gx)_92855755.md | DOC-WSFD-109102-02 | Gx接口ADC相关概念（应用、自营业务、可推论业务、不可推论业务）、Gx接口完整业务流程（初始激活、应用开始、应用停止） |
| 3 | 实现原理(N7)_92582135.md | DOC-WSFD-109102-03 | N7接口ADC相关概念、N7接口完整业务流程（初始激活、应用开始、应用停止） |
| 4 | 激活ADC基本功能_92582136.md | DOC-WSFD-109102-04 | 操作场景、前提条件、数据规划、操作步骤（License开关、FlowFilter配置、ADCPARA配置、Rule配置、UserProfile配置、RULEBINDING配置）、任务示例 |
| 5 | WSFD-109102 ADC基本功能参考信息_92582138.md | DOC-WSFD-109102-05 | MML命令清单、告警、软件参数（BIT1916）、测量指标 |
| 6 | 调测ADC基本功能_92582137.md | DOC-WSFD-109102-06 | 操作场景、前提条件、调测数据、调测步骤（License验证、用户跟踪、ADC规则验证、应用检测验证、故障排查流程） |

### 8.2 原始文档路径

所有源文档位于：
```
output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109102 ADC基本功能/
```

### 8.3 关联特性文档

| 关联特性 | 文档路径 | 关系 |
|----------|----------|------|
| WSFD-109101 PCC基本功能 | `WSFD-109101 PCC基本功能_60374767.md` | 前置依赖 |
| GWFD-020357 增强的ADC基本功能 | UDG侧对应特性文档 | 控制面/用户面配合 |
