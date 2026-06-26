# GWFD-020357 增强的ADC基本功能 知识文档

> 访问限制场景 ADC 核心特性 | UDG | 来源：特性概述 + 实现原理 + 激活 + 调测 + 参考信息 | 2026-06-22

---

## 0. 元数据（三层图谱Schema §9.3 对齐）

| 字段 | 取值 |
|------|------|
| feature_id | GWFD-020357 |
| feature_name | 增强的ADC基本功能 |
| feature_group | ADC核心 |
| parent_feature_id | GWFD-020351 PCC基本功能（功能父节点，ADC 在 PCC 基础上扩展 L7 检测能力） |
| applicable_nf_map | `{"UDG": ["PGW-U", "UPF"], "UNC": ["PGW-C", "SMF"], "PCF": ["PCRF", "PCF"]}` |
| variant_dimensions | ["检测事件(APP_STA/APP_STO)", "动作策略组(策略类型为ADC的独立rule / 复用策略类型为PCC的rule)", "PCRF规则下发方式(预定义规则 / 动态规则携带TDF-Application-Identifier)", "协议类型(HTTP / FTP / RTSP等SA支持的协议)", "流信息上报开关(FLOWINFORPT=ENABLE/DISABLE)"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-AC-01, EV-FK-AC-02, EV-FK-AC-03, EV-FK-AC-04, EV-FK-AC-05] |
| license_required | 82200AFK LKV3G5ADCF01 增强的ADC基本功能（必须获得 License 许可） |

---

## 1. 概述

### 1.1 特性定义（是什么）

增强的 ADC（Application Detection and Control）基本功能是指：**UDG 支持检测 L7 应用，并通过 PGW-C/SMF 将应用标识（Application Identifier）、流信息以及应用的起始/结束事件上报给 PCRF/PCF**，由 PCRF/PCF 结合用户签约、网络状态等下发 PCC 策略，UDG 执行该 PCC 策略进行业务控制、流量上报等。

**与 PCC 基本功能的差异**：PCC 基本功能（GWFD-020351）只能对 L3/L4 业务进行动态控制，不能对 L7 业务动态控制，且 PCRF/PCF 无法感知业务变化。ADC 在 PCC 基础上引入 L7 应用检测能力，解决业务精细化控制的问题。

> 来源：`GWFD-020357 增强的ADC基本功能特性概述_84866818.md`（定义、原理概述章节）

### 1.2 适用NF（UDG/UNC网元）

| 涉及NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| PGW-U / UPF | 用户面（UDG） | UDG 20.2.0 及后续版本 | 执行业务数据流检测；将获取的应用标识（Application Identifier）、流信息以及应用起始/结束事件发送给 PGW-C/SMF；安装并执行 PGW-C/SMF 传递的会话策略 |
| PGW-C / SMF | 控制面（UNC） | UNC 20.1.0 及后续版本 | 将 PGW-U/UPF 收到的应用标识、流信息及起始/结束事件转发给 PCRF/PCF；根据 PCRF/PCF 下发的策略完成 SDF 与 QoS Flow 绑定；将策略转发给 PGW-U/UPF |
| PCRF / PCF | 策略决策 | 无特殊要求 | 根据应用标识、流信息及起始/结束事件，结合签约信息下发携带不同 QCI/ARP 的 PCC 策略给 PGW-C/SMF |

> 说明：PGW-U/UPF 与 PCRF/PCF 不能直接互传数据，必须通过 PGW-C/SMF 转发。产品文档原理图为突出 ADC 实现省略了 PGW-C/SMF。
> 来源：`GWFD-020357 增强的ADC基本功能特性概述_84866818.md`（可获得性章节）

### 1.3 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | 基于业务检测和上报的策略控制增强了网络对业务的感知和控制能力；为不同业务应用提供不同策略控制，吸引用户使用自营业务；PCRF/PCF 可掌握用户当前使用的业务，更灵活实施 PCC 策略；通过业务上报可基于业务进行资源分配，提升资源利用效率 |
| 用户 | 根据应用获得差异化服务，提升业务体验，减少时延 |

> 来源：`GWFD-020357 增强的ADC基本功能特性概述_84866818.md`（客户价值章节）

### 1.4 应用场景（三大典型场景）

| 场景 | 工作机制 | 访问限制视角 |
|------|---------|-------------|
| 页面重定向 | 用户访问未签约业务时，UDG 将访问页面重定向到提醒页面，通知用户不可访问；用户在重定向页面订购后，PCRF/PCF 实时授权，用户即可访问 | ADC 检测是重定向的触发源（应用 START 事件） |
| 业务流控 | UDG 实时监测上报用户业务信息，PCRF/PCF 综合用户签约、网络状况（小区拥塞）下发指定业务的流控策略给 UDG，实现对指定业务流量的带宽控制（如 VoIP） | ADC 检测为流量整形提供触发条件 |
| 高价值业务 QoS 保障 | UDG 识别高价值业务并上报，PCRF/PCF 结合签约、网络状态下发携带不同 QCI/ARP 的 PCC 策略，触发专有承载创建，提供差异化 QoS 保障 | 高价值业务典型包括自营业务（VoIP、视频共享、文件传输、聊天）、签约用户服务、基于 Internet 网络架构的自营视频业务（如 Mobile TV） |

> 来源：`GWFD-020357 增强的ADC基本功能特性概述_84866818.md`（应用场景章节）

### 1.5 License

- **License 控制项**：`82200AFK LKV3G5ADCF01 增强的ADC基本功能`
- **必须获得 License 许可后才能使用**该特性服务

> 来源：`GWFD-020357 增强的ADC基本功能特性概述_84866818.md`（License 支持）

### 1.6 前置条件与依赖

| 依赖类型 | 相关特性 / 控制项 | 说明 |
|---------|-----------------|------|
| 依赖 | SA 相关特性（82209749 SA-Basic 等 21 个 SA 子特性） | UDG 基于 SA 执行业务检测，把检测结果上报给 PCRF/PCF。开通 ADC 必须同时开启 SA 功能 |
| 依赖 | GWFD-020351 PCC基本功能（82209825 PCC基本功能） | PCRF/PCF 下发携带 Application ID 的 PCC 规则给 UDG。开通 ADC 必须同时开启 PCC 基本功能 |
| 数据前置 | 完成激活 PCC 基本功能；完成加载 License；完成协议识别库和解析库的加载（参见"激活业务感知"） | 调测前置 |

> 来源：`GWFD-020357 增强的ADC基本功能特性概述_84866818.md`（与其他特性的交互）、`激活增强的ADC基本功能_84866820.md`（必备事项）、`调测增强的ADC基本功能_84866921.md`（必备事项）

### 1.7 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|---------|---------|---------|
| 01 | 20.1.0 | 首次发布 |

> 来源：`GWFD-020357 增强的ADC基本功能特性概述_84866818.md`（发布历史）

### 1.8 特性规格

| 规格名称 | 规格指标 |
|---------|---------|
| 允许配置自定义协议 | 5000 个 |
| 允许配置预定义支持 ADC 上报的 PCC 规则 | 5000 个 |
| 支持上报的并发 Flow 信息数 | 16 个 |

> 来源：`GWFD-020357 增强的ADC基本功能特性概述_84866818.md`（特性规格）

### 1.9 遵循标准

| 标准类别 | 标准编号 | 标准名称 |
|---------|---------|---------|
| 3GPP | 23501 | System Architecture for the 5G System; Stage 2 |
| 3GPP | 23502 | Procedures for the 5G System; Stage 2 |
| 3GPP | 23503 | Policy and Charging Control Framework for the 5G System; Stage 2 |
| 3GPP | 29.244 | Interface between the Control Plane and the User Plane nodes |
| 3GPP | 29507 | 5G System; Access and Mobility Policy Control Service; Stage 3 |
| 3GPP | 29512 | 5G System; Session Management Policy Control Service; Stage 3 |
| 3GPP | 29513 | 5G System; Policy and Charging Control signalling flows and QoS parameter mapping; Stage 3 |

> 来源：`GWFD-020357 增强的ADC基本功能特性概述_84866818.md`（遵循标准）

### 1.10 对系统的影响

- 使能 ADC 后会对**所有业务进行解析**，报文转发性能和吞吐量将下降（具体程度需基于话务模型评估）
- ADC 应用上报会导致 **N4/N7 接口信令增多**
- ADC 应用上报触发 PCRF/PCF 更新承载控制，会导致 **GnGp/S11/S5/S8 接口 GTP 信令数增多**

> 来源：`GWFD-020357 增强的ADC基本功能特性概述_84866818.md`（对系统的影响）

### 1.11 应用限制

1. **PCRF/PCF 异常场景处理**：考虑到 N4/N7 接口信令流控以及链路故障等因素，PCRF/PCF 可能没有收到 UDG 上报的应用 Stop 事件，而收到 UDG 重复上报的同一个应用的 Start 事件，或 PCRF/PCF 只收到 UDG 上报的某个应用的 Stop 事件。PCRF/PCF 要能够正确处理这些情况。
2. **动态规则生成要求**：如果要根据 UDG 上报的流信息进行基于应用的策略控制和承载保障，要求 PCRF/PCF 能基于 UDG 上报的指定应用的所有流信息生成一个动态规则，通过该动态规则下发指定应用的 QoS。
3. **缺省规则建议**：UDG 会丢弃匹配不到所有 PCC rule 的报文，因此**建议配置一个三四层为 any、七层协议为 any 的 rule 作为缺省配置**。

> 来源：`GWFD-020357 增强的ADC基本功能特性概述_84866818.md`（应用限制）

### 1.12 计费与话单

在应用识别完成之前，信令报文或业务报文的临时流量会优先选择使用匹配到优先级最高的 rule 的 L3/4 中的计费信息，其次选择使用 common-policy（对应 UserProfile 中的配置）中配置的缺省计费信息。由于配置可选，如果上述配置无法获取，为了应用识别能够正常完成，UDG 允许临时流量通过，不进行计费。

> 来源：`GWFD-020357 增强的ADC基本功能特性概述_84866818.md`（计费与话单）

---

## 2. 原理（深度：事件触发 + 协议交互 + 三策略组动态切换）

### 2.1 相关概念

| 概念 | 说明 |
|------|------|
| 应用 | ADC 功能中定义的新名词，等同于 PCC 基本功能的"业务" |
| 自营业务 | 运营商提供的业务（如手机音乐下载、手机视频浏览等），通过差异化 QoS 保障提高竞争力 |
| 可推论业务 | 流信息可识别、业务持续时间长（推荐 ≥ 3 分钟）、并发流数量少（推荐 ≤ 16 个）的业务，如 FTP、RTSP。注意：很难简单通过协议名称判定，只有基于对协议的理解和分析才能判定 |
| 不可推论业务 | 与可推论业务相对，指五元组老化快、并发流数量多的业务，如 P2P、HTTP |

> 来源：`实现原理_84866819.md`（相关概念）

### 2.2 事件触发机制（APP_STA / APP_STO）

ADC 的核心是两类事件的检测与上报，由 PCRF/PCF 通过 Event-Trigger 订阅：

| 事件 | 协议信元 | 触发条件 | UDG 上报行为 |
|------|---------|---------|-------------|
| **APPLICATION_START**（APP_STA） | Npcf_SMPolicyControl_Update Request 携带 Application-Detection-Information + APPLICATION_START Event-Trigger | UDG 检测到 PCRF/PCF 订阅的 Application ID 对应的数据流开始 | 经 PGW-C/SMF 上报给 PCRF/PCF；可由 ADCHYSTIMER 延迟上报 |
| **APPLICATION_STOP**（APP_STO） | 同上，Event-Trigger 替换为 APPLICATION_STOP | UDG 检测到应用数据流终止 | 同上；若携带 Application ID 的 PCC 规则被删除或失效，后续业务停止后不再上报 APPLICATION_STOP |

**Application-Detection-Information AVP 携带的子信元**：

| 子信元 | 上报控制 | 决定方 |
|-------|---------|-------|
| TDF-Application-Identifier（应用标识） | 是否上报由 ADD PCCPOLICYGRP 的 ADCMUTEFLAG 参数 + 动态 PCC 规则是否携带 Mute-Notification AVP 决定 | UDG 本地配置 / PCRF/PCF 动态下发 |
| TDF-Application-Instance-Identifier（应用实例标识，可推论业务） | 由 ADD ADCPARA 命令控制 | UDG 本地配置 |
| Flow-Information（流信息，可推论业务） | 由 ADD ADCPARA 命令控制；与 TDF-Application-Instance-Identifier 对应，使用 Instance Identifier 后 PGW-C/SMF 无需每次上报 Flow-Information | UDG 本地配置 |

> 来源：`实现原理_84866819.md`（业务流程第 2.c、第 3.b 步）

### 2.3 ADCPARA 检测参数

| 参数 | 取值 | 控制行为 |
|------|------|---------|
| FLOWFILTERNAME | 已配置的流过滤器名 | 关联到本参数所属的流过滤器 |
| FLOWINFORPT | ENABLE / DISABLE（默认） | 流信息上报开关。ENABLE 时向 PCRF/PCF 上报流信息，便于 PCRF/PCF 获取应用与流的对应关系，从而下发更精确的策略 |
| ADCHYSTTIMER | 0 ~ 3600（秒） | 应用级上报迟滞时间。取值 0 表示关闭延迟上报；当单用户一个应用的 Start/Stop 消息上报过于频繁时，可调大此参数延迟上报 |

> 说明：PCRF/PCF 通过动态规则下发 appid 时，**流信息上报开关以 SMF 下发的为准**。
> 来源：`激活增强的ADC基本功能_84866820.md`（表 3 流信息上报开关）、`实现原理_84866819.md`（业务流程注释）

### 2.4 三策略组动态切换原理（访问限制视角的关键）

ADC 上报后，PCRF/PCF 下发新 PCC 策略。**同一应用在不同阶段对应不同的 PCC 策略组**，UDG 根据事件动态切换：

```
┌────────────────────────────────────────────────────────────────┐
│ 三策略组动态切换时序（对应 APP_STA → 业务执行 → APP_STO）          │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  [Normal 策略组]   ← 初始激活时 PCRF/PCF 下发，携带 Application   │
│      │              ID 的 PCC 规则 + APP_STA/STO Event-Trigger    │
│      │              (此时仅做检测订阅，未触发动作)                │
│      │                                                         │
│      │ 用户开始使用应用，UDG 检测到数据流开始                    │
│      ▼                                                         │
│  APP_STA 上报 ──→ PCRF/PCF 决策 ──→ 下发 [Start 策略组]          │
│                                      (可能分配 GBR/QCI/ARP、    │
│                                       触发专有承载创建、        │
│                                       或下发 BLOCK/REDIRECT)   │
│      │                                                         │
│      │ 业务执行期，UDG 执行新 PCC 策略                          │
│      │                                                         │
│      │ 用户停止使用应用，UDG 检测到数据流终止                   │
│      ▼                                                         │
│  APP_STO 上报 ──→ PCRF/PCF 决策 ──→ 下发 [Stop 策略组]           │
│                                      (可能删除原 PCC 规则、     │
│                                       触发专有承载去激活、      │
│                                       或恢复 Normal 策略)      │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

**关键点**：访问限制场景中，ADC 是**动作触发的源头**——通过 APP_STA/APP_STO 上报，PCRF/PCF 可下发携带 BLOCK/REDIRECT 的 PCC 策略组，实现"检测到特定应用即阻塞或重定向"的访问限制动作。

> 来源：`实现原理_84866819.md`（业务流程第 2.e、第 3.d 步）；三策略组时序基于 ADC 事件 + PCRF/PCF 动态下发机制归纳

### 2.5 业务流程（端到端 ASCII 图）

```
┌─────────────────────────────────────────────────────────────────┐
│ 阶段 1：初始激活（PCRF/PCF 下发订阅规则）                          │
├─────────────────────────────────────────────────────────────────┤
│  a. 用户发起 IP-CAN Session 建立                                  │
│  b. PGW-C/SMF → PCRF/PCF：Npcf_SMPolicyControl_Create Request   │
│  c. PCRF/PCF → PGW-C/SMF：Npcf_SMPolicyControl_Create Response  │
│     携带：application ID 的 PCC 动态规则                          │
│           APPLICATION_START + APPLICATION_STOP Event-Trigger     │
│     （也可在任何 UpdateNotify 消息中下发）                        │
│  d. PGW-C/SMF → PGW-U/UPF：PFCP Session Establishment Request   │
│     携带 application ID 的 PCC 规则 + 两个 Event-Trigger          │
│  e. PGW-U/UPF 安装规则 → 返回 PFCP Session Establishment Resp   │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 阶段 2：用户开始使用应用（APP_STA 触发）                          │
├─────────────────────────────────────────────────────────────────┤
│  a. PGW-U/UPF 检测到该应用数据流已经开始                          │
│  b. PGW-U/UPF → PGW-C/SMF：检测信息                              │
│     （ADCHYSTTIMER ≠ 0 时延迟上报 APPLICATION_START）             │
│  c. PGW-C/SMF → PCRF/PCF：Npcf_SMPolicyControl_Update Request   │
│     携带 Application-Detection-Information + APPLICATION_START   │
│     - TDF-Application-Identifier（受 ADCMUTEFLAG 控制）          │
│     - TDF-Application-Instance-Identifier/Flow-Information       │
│       （受 ADCPARA 控制）                                         │
│  d. PCRF/PCF 结合用户签约数据 → 下发更新后的 PCC 策略              │
│  e. PGW-C/SMF：可能发起专有承载/二次上下文/专有 QoS Flow 创建      │
│     或更新承载/上下文带宽（分配 GBR、QCI/ARP、5QI/ARP）            │
│     将新 PCC 策略下发给 PGW-U/UPF                                │
│  f. PGW-U/UPF 对后续业务流执行新的 PCC 策略                       │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 阶段 3：用户停止使用应用（APP_STO 触发）                          │
├─────────────────────────────────────────────────────────────────┤
│  a. PGW-U/UPF 检测到应用数据流终止                                │
│     → 向 PGW-C/SMF 发送应用检测信息 + APPLICATION_STOP            │
│     （ADCHYSTTIMER ≠ 0 时延迟上报）                               │
│     注意：若携带 Application ID 的 PCC 规则已被删除/失效，          │
│           后续业务停止后不再上报 APPLICATION_STOP                  │
│  b. PGW-C/SMF → PCRF/PCF：应用检测信息 + APPLICATION_STOP         │
│     携带 TDF-Application-Identifier/TDF-Application-Instance-Id  │
│  c. PCRF/PCF 结合签约业务 → 下发新的 PCC 策略                     │
│  d. PGW-C/SMF：可能发起专有承载/二次上下文/专有 QoS Flow 去激活    │
│     或发起上下文/承载/QoS Flow 更新（如删除之前下发的 PCC 规则）    │
└─────────────────────────────────────────────────────────────────┘
```

> 来源：`实现原理_84866819.md`（业务流程完整 3 阶段）

### 2.6 规则匹配原则（引入携带 Application ID 的 PCC 规则后）

| # | 原则 | 说明 |
|---|------|------|
| 1 | 全局优先级匹配 | 预定义规则、动态规则、携带 Application ID 的动态规则按全局优先级从高到低顺序匹配 |
| 2 | 优先级相同时的选择顺序 | 携带 Application ID 的动态规则 > 动态规则 > 预定义规则 |
| 3 | Application ID 映射 | 携带 Application ID 的动态规则中，ApplicationID 映射到 UDG 中配置的 FlowFilter，支持 L3/4/7 过滤条件，与预定义规则匹配方式相同 |
| 4 | TDF-Application-Identifier 映射 | PCC 动态规则中携带的 TDF-Application-Identifier AVP 映射到本地配置的 FlowFilter |
| 5 | 动态规则优先级 | 携带 Application ID 的动态规则的优先级由 PCRF/PCF 动态指定；未指定时 UDG 使用默认优先级 |
| 6 | L7 全部失败的兜底 | 所有 rule 的 L7 都匹配失败时，UDG 使用匹配到 L3/4、优先级最高的 rule；**建议规划一个优先级最低、L3/4 和 L7 均为 any 的 rule 作为缺省** |
| 7 | 匹配不上的阻塞行为 | 对于 PCRF/PCF 下发的预定义规则和动态规则，若用户业务流匹配不上所有规则，则**阻塞用户当前业务流**（访问限制的兜底阻塞机制） |

> 来源：`实现原理_84866819.md`（规则匹配原则）

### 2.7 协议交互汇总

| 接口 | 交互网元 | 关键信元 / AVP | 用途 |
|------|---------|---------------|------|
| N7（5G）/ Gx（4G） | PCRF/PCF ↔ PGW-C/SMF | Npcf_SMPolicyControl_Create/Update/UpdateNotify；Application-Detection-Information；APPLICATION_START/APPLICATION_STOP Event-Trigger；TDF-Application-Identifier；TDF-Application-Instance-Identifier；Flow-Information；Mute-Notification | PCRF/PCF 订阅事件、UDG 上报检测结果、PCRF/PCF 下发新 PCC 策略 |
| N4（5G）/ Sxa（4G） | PGW-C/SMF ↔ PGW-U/UPF | PFCP Session Establishment/Modification Request；携带 application ID 的 PCC 规则；APPLICATION_START/APPLICATION_STOP Event-Trigger；PFCP Session Report Request（上报应用检测信息） | C 面下发规则与订阅；U 面上报检测事件 |
| GnGp/S11/S5/S8（4G） | PGW-C/SMF ↔ SGW | GTP-C 信令 | ADC 上报触发 PCRF/PCF 更新承载控制，导致 GTP 信令数增多 |

> 来源：综合 `实现原理_84866819.md`、`GWFD-020357 增强的ADC基本功能特性概述_84866818.md`（对系统的影响）

---

## 3. 配置对象体系

### 3.1 配置对象层级

```
┌─────────────────────────────────────────────────────────────┐
│ ADC 配置对象体系                                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [三四层过滤层]                                               │
│   FILTER ──┐                                                │
│            ├→ FLTBINDFLOWF ──→ FLOWFILTER                   │
│  [七层过滤层]                                                │
│   L7FILTER (URL/protocol) ──→ PROTBINDFLOWF ──→ FLOWFILTER  │
│                                                             │
│                          FLOWFILTER                         │
│                              │                              │
│            ┌─────────────────┼─────────────────┐            │
│            ▼                 ▼                 ▼            │
│      [ADC 参数层]      [动作策略组层]      [规则层]            │
│       ADCPARA         URR/URRGROUP        RULE              │
│      (FLOWINFORPT,    → PCCPOLICYGRP      (POLICYTYPE=      │
│       ADCHYSTTIMER)   (ADCMUTEFLAG,         ADC 或 PCC)      │
│                        URRGROUPNAME)                         │
│                                  │                          │
│                                  ▼                          │
│                          USERPROFILE                        │
│                              │                              │
│                              ▼                              │
│                          RULEBINDING                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 关键配置对象

| 对象类型 | 对象名称（示例） | 用途 |
|----------|-----------------|------|
| FILTER | filter_test1 | 三四层过滤条件 |
| FLOWFILTER | flowfilter_ADC01 | 流过滤器；PCRF/PCF 下发动态规则时，TDF-Application-Identifier 映射到此 |
| L7FILTER | l7filter_test | 七层过滤器（URL） |
| ADCPARA | — | ADC 参数（流信息上报开关、延迟定时器） |
| URR | urr01 | 使用量上报规则 |
| URRGROUP | cp_test | 使用量上报规则组 |
| PCCPOLICYGRP | pg_ADC01 | PCC 策略组（含 ADCMUTEFLAG） |
| RULE | rule_test2 | 规则（POLICYTYPE=ADC 或 PCC） |
| USERPROFILE | up_test | 用户模板（与 SMF 上配置一致） |
| RULEBINDING | — | 规则与用户模板的绑定关系 |

### 3.3 关键参数说明

| 参数 | 取值 | 说明 |
|------|------|------|
| ADCMUTEFLAG | DISABLE / ENABLE | **DISABLE=允许 ADC 上报**；ENABLE=静默。配置 ADC 时**必须为 DISABLE** |
| FLOWINFORPT | ENABLE / DISABLE（默认） | 流信息上报开关；ENABLE 时向 PCRF/PCF 上报流信息 |
| ADCHYSTTIMER | 0 ~ 3600 | 应用级上报迟滞时间（秒），0=关闭延迟上报 |
| POLICYTYPE | ADC / PCC | 规则策略类型。ADC 独立 rule 或复用 PCC rule |
| PRIORITY | 整数（如 15、20） | 全局优先级，仅对 PCC 用户生效；值越小优先级越高 |
| FILTERINGMODE | FLOWFILTER / FLOWFILTERGRP | 流过滤器或流过滤器组选择 |

> 来源：`激活增强的ADC基本功能_84866820.md`（表 3/4/5/6 参数说明）

### 3.4 约束条件

| 约束类型 | 约束内容 |
|---------|---------|
| FLOWFILTERNAME 三网元一致 | PCRF/PCF 下发动态规则携带 appid 时，PGW-C/SMF、PGW-U/UPF、PCRF/PCF 三个网元上的 FlowFilter 名称必须一致，否则无法正常上报 |
| 预定义规则场景 FlowFilter 与 ADC 无关 | PCRF/PCF 通过预定义规则下发 APPLICATION_START/STOP 时，FlowFilter 与 ADC 功能无关 |
| ADCMUTEFLAG 必配 | 配置 ADC 时必须将 ADCMUTEFLAG 设置为 DISABLE |
| SA + PCC 双依赖 | 必须同时开启 SA 相关特性和 GWFD-020351 PCC 基本功能 |
| 协议识别库加载 | 调测前必须完成协议识别库和解析库的加载 |
| 兜底缺省规则 | 建议配置 L3/4=any、L7=any 的缺省 rule，避免业务流被丢弃 |
| USERPROFILE 一致性 | 用户模板名称必须与 SMF 上配置的用户模板名称保持一致 |

> 来源：`激活增强的ADC基本功能_84866820.md`（数据表说明）

---

## 4. 配置流程

### 4.1 通用激活步骤骨架

```
步骤1：打开 License 配置开关
   SET LICENSESWITCH:LICITEM="LKV3G5ADCF01",SWITCH=ENABLE;

步骤2：配置三四层过滤条件
   ADD FILTER → ADD FLOWFILTER → ADD FLTBINDFLOWF → SET REFRESHSRV

步骤3：配置七层过滤条件
   ADD L7FILTER → ADD PROTBINDFLOWF → SET REFRESHSRV
   （注：L7Filter 配置后系统自动 60s 生效；如需立即生效执行 SET REFRESHSRV）

步骤4：配置 ADC 参数（仅预定义规则场景）
   ADD ADCPARA:FLOWFILTERNAME=...,FLOWINFORPT=ENABLE,ADCHYSTTIMER=0;
   （注：动态规则场景流信息上报开关以 SMF 下发为准，不需要本步骤）

步骤5：配置规则（两种方式二选一）
   方式 A：独立策略类型为 ADC 的 rule
      ADD RULE:POLICYTYPE=ADC,...,ADCMUTEFLAG=DISABLE;
   方式 B：复用 PCC rule（需先配 URR/URRGROUP/PCCPOLICYGRP）
      ADD URR → ADD URRGROUP → ADD PCCPOLICYGRP(ADCMUTEFLAG=DISABLE)
      → ADD RULE:POLICYTYPE=PCC,...,POLICYNAME=pg_ADC01;

步骤6：配置规则与用户模板绑定
   ADD USERPROFILE → ADD RULEBINDING
```

> 来源：`激活增强的ADC基本功能_84866820.md`（操作步骤）

### 4.2 MML 命令清单（参考信息）

| 命令 | 用途 |
|------|------|
| ADD FLOWFILTER | 增加流过滤器 |
| ADD FILTER | 增加过滤器 |
| ADD FLTBINDFLOWF | 增加流过滤器与过滤器的绑定关系 |
| ADD L7FILTER | 增加七层过滤器 |
| ADD PROTBINDFLOWF | 增加流过滤器协议绑定关系 |
| ADD WELLKNOWNPORT | 增加知名端口 |
| LOD SIGNATUREDB | 加载协议特征库文件 |
| ADD URR | 增加使用量上报规则 |
| ADD URRGROUP | 增加使用量上报规则组 |
| ADD PCCPOLICYGRP | 增加PCC策略组 |
| ADD RULE | 增加规则 |
| ADD USERPROFILE | 增加用户模板 |
| ADD RULEBINDING | 增加用户模板和规则的绑定关系 |
| ADD ADCPARA | 增加ADC参数 |
| SET LICENSESWITCH | 设置License开关 |
| SET REFRESHSRV | 业务刷新 |

> 来源：`GWFD-020357 增强的ADC基本功能参考信息_84866922.md`（命令）

---

## 5. 配置案例（多场景变体）

### 5.1 场景一：PCRF/PCF 下发预定义规则 — 独立 ADC rule 方式

**场景描述**：使能增强的 ADC 基本功能，PCRF/PCF 下发携带 APPLICATION_START/STOP Event-Trigger 的预定义规则给 UDG，UDG 本地配置需要识别的 URL、具体规则内容及上报的应用，开启流信息上报开关，采用**独立策略类型为 ADC 的 rule** 实现对 HTTP 业务的 QoS 保障。

**MML 命令序列（原样保留产品文档脚本）**：

```
// 打开本特性的 License 配置开关。
SET LICENSESWITCH:LICITEM="LKV3G5ADCF01",SWITCH=ENABLE;

// 配置 ADC 业务使用的三四层过滤条件。
ADD FILTER: FILTERNAME="filter_test1", L34PROTTYPE=STRING, L34PROTOCOL=ANY;
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_ADC01";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_ADC01",FILTERNAME="filter_test1";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 配置 ADC 业务的七层过滤条件（URL）。
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="sl7_test_1",URL="www.huawei.com/*";
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="sl7_test_2",URL="www.example.com";
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_ADC01",PROTOCOLNAME="http",L7FILTERNAME="l7filter_test";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 配置 ADC 参数（开启流信息上报开关 + 关闭延迟上报）。
ADD ADCPARA: FLOWFILTERNAME="flowfilter_ADC01",FLOWINFORPT=ENABLE,ADCHYSTTIMER=0;

// （方式 A：独立 ADC rule）配置 ADC 业务使用的规则。
ADD RULE:RULENAME="rule_test2",POLICYTYPE=ADC,
  FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilter_ADC01",
  PRIORITY=15,ADCMUTEFLAG=DISABLE;

// 配置业务策略组合（规则与用户模板的绑定关系）。
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test2";
```

> 来源：`激活增强的ADC基本功能_84866820.md`（任务实例一脚本 - 仅方式 A 部分）

### 5.2 场景二：PCRF/PCF 下发预定义规则 — 复用 PCC rule 方式

**场景描述**：与场景一前置条件相同，但采用**复用策略类型为 PCC 的 rule** 实现 ADC 功能。此方式需额外配置计费属性（URR/URRGROUP）和 PCC 策略组（PCCPOLICYGRP），并把 ADCMUTEFLAG 置于 PCCPOLICYGRP 上。

**MML 命令序列（仅展示与场景一差异部分）**：

```
// 步骤 1~4（License / 三四层 / 七层 / ADCPARA）与场景一完全相同，此处省略。

// 配置 ADC 业务使用的计费属性（URR + URRGROUP）。
ADD URR:URRNAME="urr01",URRID=1000,USAGERPTMODE=OFFLINE;
ADD URRGROUP:URRGROUPNAME="cp_test", UPURRNAME1="urr01", DOWNURRNAME1="urr01";

// 配置 ADC 业务使用的 PCC 动作策略组（ADCMUTEFLAG=DISABLE 必配）。
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pg_ADC01",
  ADCMUTEFLAG=DISABLE,
  URRGROUPNAME="cp_test";

// （方式 B：复用 PCC rule）配置 ADC 业务使用的规则。
// 注意：与场景一 RULENAME 同为 rule_test2，但 POLICYTYPE=PCC 且引用 POLICYNAME=pg_ADC01。
ADD RULE:RULENAME="rule_test2",POLICYTYPE=PCC,
  FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilter_ADC01",
  PRIORITY=20,POLICYNAME="pg_ADC01";

// 配置业务策略组合（同场景一）。
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test2";
```

> 来源：`激活增强的ADC基本功能_84866820.md`（任务实例一脚本 - 方式 B 部分及表 5/6 计费规则规划数据）

### 5.3 场景三：PCRF/PCF 下发动态规则（携带 TDF-Application-Identifier）

**场景描述**：PCRF/PCF 下发携带 Application ID 的动态规则给 UDG，UDG 本地配置需要识别的 URL 和上报的应用。**与预定义规则场景的关键差异**：

1. 流信息上报开关以 SMF 下发的为准（不配置 ADCPARA）
2. TDF-Application-Identifier AVP 由 PCRF/PCF 动态下发，映射到 UDG 本地配置的 FlowFilter
3. UDG 本地无需单独配置 ADC rule，由 PCRF/PCF 动态规则接管

**MML 命令序列（核心差异：仅配置过滤器，不下发 ADCPARA/ADC rule）**：

```
// 打开本特性的 License 配置开关。
SET LICENSESWITCH:LICITEM="LKV3G5ADCF01",SWITCH=ENABLE;

// 配置 ADC 业务使用的三四层过滤条件。
// 关键：FLOWFILTERNAME 必须与 PCRF/PCF 下发的 TDF-Application-Identifier 值一致，
//       且 PGW-C/SMF、PGW-U/UPF、PCRF/PCF 三网元一致。
ADD FILTER: FILTERNAME="filter_test1", L34PROTTYPE=STRING, L34PROTOCOL=ANY;
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_ADC01";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_ADC01",FILTERNAME="filter_test1";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 配置 ADC 业务的七层过滤条件（URL）。
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="sl7_test_1",URL="www.huawei.com/*";
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="sl7_test_2",URL="www.example.com";
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_ADC01",PROTOCOLNAME="http",L7FILTERNAME="l7filter_test";

// 注意：动态规则场景不需要 ADD ADCPARA、ADD ADCRULE；
// PCRF/PCF 通过 N7 接口动态下发携带 application ID 的 PCC 规则。
```

> 来源：`激活增强的ADC基本功能_84866820.md`（任务实例二脚本 + 说明"流信息上报开关以 SMF 下发的为准"）

### 5.4 场景四：访问限制触发场景（APP_STA 触发 PCRF 下发 BLOCK/REDIRECT）

**场景描述**：运营商希望"当用户开始使用特定应用（如某 P2P 应用）时，立即阻塞该应用"。UDG 检测到应用 START 事件后上报，PCRF/PCF 下发携带 BLOCK 动作的新 PCC 规则。

**MML 命令序列（基础过滤器配置与场景一相同，此处重点展示触发机制）**：

```
// 前置：按场景一或场景二完成 ADC 基础配置。
// 关键：UDG 仅负责"检测+上报"，"阻塞动作"由 PCRF/PCF 在 APP_STA 上报后动态下发。

// UDG 侧典型配置（识别特定应用）：
ADD L7FILTER:L7FILTERNAME="l7filter_p2p",SUBL7FLTNAME="sl7_p2p",URL="*p2papp*";
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_ADC01",PROTOCOLNAME="http",L7FILTERNAME="l7filter_p2p";

// 阻塞动作不在 UDG 本地配置，而是依赖 PCRF/PCF 下发：
//   PCRF/PCF 收到 APP_STA → 下发携带 Flow-Status=DISABLED 的新 PCC 规则
//   UDG 执行新规则 → 该应用后续报文被阻塞
```

> 说明：本场景为访问限制视角的归纳。UDG 产品文档主要强调 QoS 保障场景，阻塞/重定向动作由 PCRF/PCF 决策下发。本场景用于说明 ADC 在访问限制中的角色。
> 来源：基于 `实现原理_84866819.md` 业务流程第 2.e 步 + 访问限制场景 cross-feature-analysis.md 归纳

### 5.5 场景变体对照表

| 变体 | 规则下发方 | rule 策略类型 | ADCPARA 是否必配 | ADCMUTEFLAG 配置位置 | UDG 本地是否配 rule | 关键差异 |
|------|----------|--------------|----------------|---------------------|-------------------|---------|
| 预定义规则 + 独立 ADC rule | PCRF/PCF 预定义 | ADC | 是（开启流信息上报） | ADD RULE.ADCMUTEFLAG | 是（POLICYTYPE=ADC） | rule 单独承载 ADC 检测订阅 |
| 预定义规则 + 复用 PCC rule | PCRF/PCF 预定义 | PCC | 是 | ADD PCCPOLICYGRP.ADCMUTEFLAG | 是（POLICYTYPE=PCC，引用 PCCPOLICYGRP） | ADC 与计费/QoS 共用 rule，需配 URR/URRGROUP/PCCPOLICYGRP |
| 动态规则（携带 TDF-Application-Identifier） | PCRF/PCF 动态 | — | 否（SMF 下发为准） | 动态 PCC 规则携带 Mute-Notification AVP | 否（仅配 FlowFilter 映射） | 三网元 FlowFilter 名称必须一致 |
| 访问限制触发（APP_STA→BLOCK） | PCRF/PCF 动态 | PCC | 视场景 | 动态 PCC 规则 | 仅检测订阅 | 阻塞动作由 PCRF/PCF 在收到 APP_STA 后下发 |

---

## 6. 验证与调测

### 6.1 调测前提与目的

运营商部署增强的 ADC 基本功能时，需要调测以确保本功能可以正常使用。

> 适用：PGW-U、UPF

### 6.2 调测数据准备

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
|------|---------|---------|---------|------|
| 用户信息查询 | IMSI 号码（IMSI） | 460000123456789 | 测试终端自带 | - |
| 测试终端使用的 APN | APN 名称（APN） | apn-test | 已配置数据中获取；可用 `LST APN` 查询 | 用户激活使用的 APN，取自接入配置中的 APN 实例名 |

> 说明：本调测以 ADCPARA.ADCHYSTIMER=0 进行。当 ADCHYSTTIMER ≠ 0 时，PGW-U/UPF 会延迟 ADCHYSTTIMER 秒后向 PGW-C/SMF 上报 APPLICATION-START/STOP 事件。
> 来源：`调测增强的ADC基本功能_84866921.md`（数据 + 说明）

### 6.3 调测执行步骤（含预期输出样例）

**步骤 1**：查询 License 配置开关是否打开。

```
LST LICENSESWITCH:LICITEM="LKV3G5ADCF01";
```

预期输出（关键字段）：
```
-------------------------
   License Item  =  LKV3G5ADCF01
   Switch        =  ENABLE
-------------------------
```

判断：
- `SWITCH=ENABLE` → 执行步骤 2
- `SWITCH=DISABLE` → 执行 `SET LICENSESWITCH:LICITEM="LKV3G5ADCF01",SWITCH=ENABLE;` 打开开关

**步骤 2**：在 PGW-U/UPF 上创建 UDG N4 接口跟踪任务（通过 OM Portal 跟踪工具）。

**步骤 3**：测试终端使用 `apn-test` APN 接入网络。
- 接入成功 → 执行步骤 4
- 接入失败 → 调测 UDG 的接入功能

**步骤 4**：测试终端浏览 Web 业务，访问 `www.huawei.com` 网页。

**步骤 5**：检查 PGW-U/UPF 是否立即向 PGW-C/SMF 发送 PFCP Session Report Request 消息，**上报的 Event-Trigger 为 APPLICATION-START**，携带 Application-Detection-Information AVP，且其中包含 TDF-Application-Identifier（值为检测到的应用名）。

预期 PFCP Session Report Request 关键信元：
```
PFCP Session Report Request:
  Report Type  =  URR / Application Detection
  Application-Detection-Information:
    TDF-Application-Identifier  =  "www.huawei.com"  (检测到的应用名)
    (可选) TDF-Application-Instance-Identifier  =  ...
    (可选) Flow-Information  =  ...
  Event-Trigger  =  APPLICATION_START
```

判断：
- PGW-U/UPF 上报信元正确 → ADC 功能生效，执行步骤 6
- PGW-U/UPF 没有上报或上报信元不全 → ADC 功能未正常生效，执行步骤 8

**步骤 6**：测试终端停止访问 `www.huawei.com` 网页。

**步骤 7**：检查 PGW-U/UPF 是否立即向 PGW-C/SMF 发送 PFCP Session Report Request 消息，**上报的 Event-Trigger 为 APPLICATION-STOP**，携带 Application-Detection-Information AVP，其中包含 TDF-Application-Identifier。

判断：
- 上报了应用的终止事件 → 调测完成
- 未上报应用终止事件 → 执行步骤 8

**步骤 8**：查看 PFCP Session Establishment Request 消息，检查 PCRF/PCF 是否下发了 APPLICATION_START 和 APPLICATION_STOP Event-Trigger。

判断：
- 是 → 执行步骤 9
- 否 → 联系 PCRF/PCF 工程师处理后重新调测

**步骤 9**：执行 `LST RULE` 命令，检查"流过滤器名称"是否与 TDF-Application-Identifier 值相同。

```
LST RULE:;
```

预期输出（关键字段）：
```
-------------------------
   Rule Name            =  rule_test2
   Policy Type          =  ADC
   Filtering Mode       =  FLOWFILTER
   Flow Filter Name     =  flowfilter_ADC01   ← 必须与 TDF-Application-Identifier 值相同
   Priority             =  15
   ADC Mute Flag        =  DISABLE
-------------------------
```

可通过 `LST RULEBINDING:` 查询规则名称与用户模板绑定关系。

判断：
- 相同 → 执行步骤 10
- 不相同 → 修改为相同后重新调测

**步骤 10**：执行 `LST PCCPOLICYGRP` 命令，检查 PCC 规则是否允许上报应用信息（仅复用 PCC rule 场景）。

```
LST PCCPOLICYGRP:PCCPOLICYGRPNM="pg_ADC01";
```

预期输出（关键字段）：
```
-------------------------
   PCC Policy Group Name  =  pg_ADC01
   ADC Mute Flag          =  DISABLE   ← "不使能"=允许上报应用信息
   URR Group Name         =  cp_test
-------------------------
```

判断：
- `ADC 静默通知标识 = 不使能（DISABLE）` → 允许上报应用信息，执行步骤 11
- `ADC 静默通知标识 = 使能（ENABLE）` → 执行 `MOD PCCPOLICYGRP` 修改为允许上报后重新调测

**步骤 11**：收集信息并寻求技术支持。
- a. 执行 `EXP MML` 命令将当前配置数据导出为 MML 脚本文件并保存
- b. 收集并保存上述所有查询信息
- c. 收集归纳所有信息并联系华为技术支持解决

> 来源：`调测增强的ADC基本功能_84866921.md`（操作步骤完整 11 步）

### 6.4 调测查询命令

| 命令 | 用途 |
|------|------|
| LST LICENSESWITCH | 查询 License 配置项开关 |
| LST RULE | 查询规则配置 |
| LST RULEBINDING | 查询用户模板和规则的绑定关系 |
| LST PCCPOLICYGRP | 查询 PCC 策略组配置 |
| LST APN | 查询 APN 配置（获取 APN 实例名） |
| EXP MML | 导出 MML 配置文件（故障收集） |

### 6.5 告警参考

**本特性无相关告警**。

> 来源：`GWFD-020357 增强的ADC基本功能参考信息_84866922.md`（告警）

### 6.6 软参

**本特性无相关软参**。

> 来源：`GWFD-020357 增强的ADC基本功能参考信息_84866922.md`（软参）

### 6.7 测量指标

**本特性无相关测量指标**。

> 来源：`GWFD-020357 增强的ADC基本功能参考信息_84866922.md`（测量指标）

### 6.8 故障排查表

| # | 问题现象 | 可能原因 | 排查方法 |
|---|---------|---------|---------|
| 1 | APP_STA 事件未上报 | License 开关未打开 | `LST LICENSESWITCH:LICITEM="LKV3G5ADCF01";` 确认 SWITCH=ENABLE |
| 2 | APP_STA 事件未上报 | PCRF/PCF 未下发 APPLICATION_START Event-Trigger | 查看 PFCP Session Establishment Request 消息；联系 PCRF/PCF 工程师 |
| 3 | APP_STA 上报但 TDF-Application-Identifier 缺失 | ADCMUTEFLAG 被误置为 ENABLE | `LST PCCPOLICYGRP` 或 `LST RULE` 检查 ADCMUTEFLAG；应为 DISABLE |
| 4 | APP_STA 上报但 Flow-Information 缺失 | ADCPARA.FLOWINFORPT=DISABLE（预定义规则场景） | `LST ADCPARA` 检查 FLOWINFORPT；应为 ENABLE（动态规则场景以 SMF 下发为准） |
| 5 | 上报事件延迟过长 | ADCHYSTTIMER 设置过大 | `LST ADCPARA` 检查 ADCHYSTTIMER；频繁上报场景建议调小或置 0 |
| 6 | 动态规则场景 Flow-Filter 名称不匹配 | PGW-C/SMF、PGW-U/UPF、PCRF/PCF 三网元 FlowFilter 名称不一致 | `LST FLOWFILTER` 对照三网元配置；修改为一致 |
| 7 | APP_STO 事件未上报 | 携带 Application ID 的 PCC 规则已被删除或失效 | 预期行为；检查 PCRF/PCF 是否已下发规则删除指令 |
| 8 | 匹配不上所有规则的报文被丢弃 | 未配置缺省兜底 rule | 配置 L3/4=any、L7=any 的缺省 rule |
| 9 | 协议识别不生效 | 协议识别库和解析库未加载 | 执行 `LOD SIGNATUREDB`；参见"激活业务感知" |
| 10 | 业务无法接入 | SA 或 PCC 基本功能未开启 | 确认 SA 相关特性 + GWFD-020351 PCC 基本功能均已激活 |

---

## 7. 特性关系网

### 7.1 访问限制场景中的角色

在访问限制场景（NS-03）中，GWFD-020357 作为 **ADC 核心特性**，是访问限制动作的**触发源**：

- **阻塞动作（DISCARD）**：UDG 检测到匹配不上任何 PCC rule 的业务流时，**直接阻塞**（兜底阻塞机制）；或 APP_STA 上报后由 PCRF/PCF 下发 BLOCK 策略
- **重定向动作（REDIRECT）**：ADC 检测的 APP_STA 事件触发 PCRF/PCF 下发重定向 PCC 策略；ADC 是重定向族（GWFD-110281/282/283/284）的前置检测能力
- **头增强基础（HEADEN）**：ADC 检测为头增强（GWFD-110261/262/263，插入 MSISDN/IMSI/防欺诈信息）提供业务识别基础
- **QoS 保障**：APP_STA 触发 PCRF/PCF 下发携带 QCI/ARP 的 PCC 策略，建立专有承载

### 7.2 与其他特性的关系

| 关联特性 | 特性ID | 关系 | 说明 |
|---------|--------|------|------|
| PCC 基本功能 | GWFD-020351 | 依赖（父节点） | ADC 在 PCC 基础上扩展 L7 检测；PCRF/PCF 下发携带 Application ID 的 PCC 规则；必须同时开启 |
| SA 相关特性（21个） | GWFD-110101 SA-Basic 等 | 依赖 | UDG 基于 SA 执行业务检测；必须同时开启 SA 功能 |
| 业务触发的 QoS 保证 | GWFD-020358 | 协同 | ADC 上报应用 START 事件触发 QoS 保障（专有承载创建） |
| HTTP 智能重定向 | GWFD-110284 | 协同 | ADC 检测是 HTTP 重定向的前置业务识别能力 |
| 用户 Portal | GWFD-110281 | 协同 | Portal 重定向场景中，ADC 检测未签约业务触发重定向到 Portal |
| URL 过滤基本功能 | GWFD-110471 | 协同 | URL 过滤（轨道B）与 ADC（轨道A）互补：ADC 走 PCC 体系，URL 过滤走 ICAP Server |
| HTTP/RTSP/HTTPS 头增强 | GWFD-110261/262/263 | 协同 | ADC 检测为头增强提供业务识别基础 |

### 7.3 PCC 体系承载（轨道 A）

ADC 属于访问限制场景的**轨道 A（PCC 体系）**：通过 RULE.POLICYTYPE=ADC 或 PCC 引用 PCCPOLICYGRP，所有动作（检测、阻塞、重定向）都承载在 PCC 规则体系上，由 PCRF/PCF 集中决策。

---

## 8. 文档一致性自检（feature-doc-list 描述 vs 产品文档实际）

| # | 维度 | feature-doc-list / 文档清单描述 | 产品文档实际内容 | 差异类型 / 处理 |
|---|------|-------------------------------|-----------------|---------------|
| 1 | 特性定位 | 访问限制场景 ADC 核心特性 | 产品文档定位为"智能策略控制功能"下的 L7 检测特性，三大场景为页面重定向/业务流控/高价值业务QoS保障 | 视角差异：访问限制视角聚焦其"检测→动作触发"能力，产品视角聚焦其"检测+QoS上报"。两者均正确 |
| 2 | 适用 NF | UDG | 产品文档明确 PGW-U、UPF（用户面执行检测）；UNC 侧 PGW-C/SMF（转发）；PCRF/PCF（决策）。**三网元协同** | 补全：feature-doc-list 仅标注 UDG，实际涉及三个 NF |
| 3 | 版本支持 | UDG 20.x | 产品文档明确：**UDG 20.2.0 及后续版本**；UNC 20.1.0 及后续版本；PCRF/PCF 无特殊要求 | 补全：版本信息需精确到 UDG=20.2.0、UNC=20.1.0 |
| 4 | 与 PCC 基本功能关系 | ADC 相关 | 产品文档明确"开通增强的 ADC 基本功能**必须同时开启 PCC 基本功能**"，且为依赖关系 | 一致：依赖关系明确 |
| 5 | 与 SA 关系 | ADC 相关 | 产品文档列出 **21 个 SA 子特性**（SA-Basic、SA-HTTP Pipeline和WAP Concatenation、SA-Web Browsing、SA-File Access、SA-Mobile、SA-Others、SA-Streaming、SA-P2P、SA-VOIP、SA-Email、SA-IM、SA-Game、SA-Network Administration、SA-Remote Connectivity、SA-Network Storage、SA-Tunneling、SA-Stock、SA-Database、SA-QUIC 等）作为依赖 | 补全：原 doc-list 描述笼统，实际 SA 依赖清单完整 |
| 6 | 配置方式分支 | 单一配置流程 | 产品文档明确 ADC rule 配置有**两条路径**：方式A（独立 POLICYTYPE=ADC 的 rule）+ 方式B（复用 POLICYTYPE=PCC 的 rule，需配 URR/URRGROUP/PCCPOLICYGRP） | 补全：配置路径需二选一 |
| 7 | 规则下发方式 | 单一 | 产品文档明确 PCRF/PCF 有**两种规则下发方式**：预定义规则 + 动态规则（携带 TDF-Application-Identifier）。两方式的 ADCPARA 配置需求不同 | 补全：预定义规则场景需配 ADCPARA；动态规则场景以 SMF 下发为准 |
| 8 | 调测前置 | 调测步骤 | 产品文档明确调测前置必须"**完成协议识别库和解析库的加载**"（参见"激活业务感知"） | 补全：协议识别库加载是隐藏前置 |
| 9 | 笔误检查 | — | 场景一脚本中 `ADD RULE:POLICYTYPE=ADC,...,ADCMUTEFLAG=DISABLE` 产品文档原文换行处将 DISABLE 单独成行（`ADCMUTEFLAG=\nDISABLE\n;`），为 Markdown 渲染所致，**MML 语义无错** | 已纠正：本文档脚本中合并为一行，不影响实际执行 |
| 10 | 计费与话单 | 未提及 | 产品文档明确"应用识别完成之前，临时流量优先使用 rule 的 L3/4 计费信息，其次使用 common-policy 缺省计费信息；若都不可获取，UDG 允许临时流量通过不进行计费" | 补全：临时流量计费规则 |
| 11 | 参考信息完整性 | 命令清单 | 产品文档参考信息明确**本特性无相关告警、无相关软参、无相关测量指标**（区别于地址分配等特性） | 补全：避免误认为有告警/测量指标 |

---

## 9. 来源文件清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020357 增强的ADC基本功能/GWFD-020357 增强的ADC基本功能特性概述_84866818.md` | 适用NF（PGW-U/UPF、PGW-C/SMF、PCRF/PCF）、定义、客户价值、三大应用场景、可获得性（License LKV3G5ADCF01、UDG 20.2.0+、UNC 20.1.0+）、与其他特性交互（依赖21个SA+PCC基本功能）、对系统影响（性能下降/N4N7信令增多/GTP信令增多）、应用限制（PCRF异常处理、动态规则要求、缺省rule建议）、原理概述、计费与话单（临时流量计费规则）、特性规格（5000自定义协议/5000预定义PCC规则/16并发Flow）、遵循标准（7个3GPP）、发布历史 |
| 2 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020357 增强的ADC基本功能/实现原理_84866819.md` | 相关概念（应用/自营业务/可推论业务/不可推论业务）、3阶段业务流程（初始激活→开始使用应用→停止使用应用）、APPLICATION_START/STOP Event-Trigger机制、Application-Detection-Information AVP（TDF-Application-Identifier/Instance-Identifier/Flow-Information）、ADCMUTEFLAG/ADCPARA控制上报、规则匹配7大原则 |
| 3 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020357 增强的ADC基本功能/激活增强的ADC基本功能_84866820.md` | 操作场景、必备事项（前置：PCC基本功能+License+协议库）、7张数据规划表（三四层/七层/ADCPARA/ADC rule/计费URR/计费PCCPOLICYGRP/RULEBINDING）、9步操作步骤、**任务实例一（预定义规则+独立ADC rule + 复用PCC rule 双方式）**、**任务实例二（动态规则）**、SMF下发流信息开关为准 |
| 4 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020357 增强的ADC基本功能/调测增强的ADC基本功能_84866921.md` | 11步调测流程（License查询→N4跟踪→APN接入→访问www.huawei.com→PFCP Session Report Request检查APP_STA→停止访问→APP_STO检查→Event-Trigger下发检查→LST RULE检查FlowFilter→LST PCCPOLICYGRP检查ADCMUTEFLAG→EXP MML收集） |
| 5 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020357 增强的ADC基本功能/GWFD-020357 增强的ADC基本功能参考信息_84866922.md` | 15条MML命令清单、**本特性无告警、无软参、无测量指标** |

### 9.1 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| ADC | Application Detection and Control | 应用检测与控制 |
| APP_STA | Application Start | 应用起始事件 |
| APP_STO | Application Stop | 应用结束事件 |
| TDF-Application-Identifier | — | 应用标识 AVP，映射到本地 FlowFilter |
| TDF-Application-Instance-Identifier | — | 应用实例标识（可推论业务） |
| Flow-Information | — | 流信息（可推论业务），与 Instance Identifier 对应 |
| Mute-Notification | — | 静默通知 AVP，动态 PCC 规则携带时控制是否上报 |
| ADCMUTEFLAG | — | ADC 静默通知标识（DISABLE=允许上报） |
| ADCHYSTTIMER | — | 应用级上报迟滞定时器（0~3600 秒） |
| FLOWINFORPT | — | 流信息上报开关（ENABLE/DISABLE） |
| 可推论业务 | Inferable Service | 流信息可识别、持续时间长（≥3分钟）、并发流少（≤16）的业务 |
