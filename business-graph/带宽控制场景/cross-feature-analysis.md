# 带宽控制场景 - 跨特性横向分析报告

> **分析范围**: 24个带宽控制场景特性（16 UDG + 8 UNC）
> **分析维度**: 分类总览 / 共性分析 / 配置差异 / 依赖关系 / 关键发现
> **文档目的**: 通过横向对比揭示特性间隐藏关系、配置对象复用模式、双产品协作机制

---

## 目录

1. [特性分类总览](#1-特性分类总览)
2. [共性分析](#2-共性分析)
3. [配置差异分析](#3-配置差异分析)
4. [依赖关系分析](#4-依赖关系分析)
5. [关键发现](#5-关键发现)
6. [附录A: 24特性索引表](#附录a-24特性索引表)
7. [附录B: MML命令交叉参考](#附录b-mml命令交叉参考)
8. [附录C: 配置对象复用矩阵](#附录c-配置对象复用矩阵)
9. [附录D: 典型端到端配置流程](#附录d-典型端到端配置流程)
10. [附录E: 版本演进与首发版本分布](#附录e-版本演进与首发版本分布)
11. [附录F: 令牌桶与三色标记体系深度分析](#附录f-令牌桶与三色标记体系深度分析)
12. [附录G: 无线资源优化类特性对比矩阵](#附录g-无线资源优化类特性对比矩阵)

---

## 1. 特性分类总览

### 1.1 按功能层次分类

| 功能层次 | UDG侧特性 | UNC侧特性 | 核心能力 |
|----------|-----------|-----------|----------|
| **基础感知层** | GWFD-110101 SA-Basic | - | L3/L4/L7业务识别，特征库管理 |
| **基础策略层** | GWFD-020351 PCC基本功能 | WSFD-109101 PCC基本功能 | QoS参数传递（MBR/GBR/QCI/5QI/ARP），PCC规则生命周期管理 |
| **核心带宽控制层** | GWFD-110311 基于业务感知的带宽控制 | WSFD-211005 基于业务感知的带宽控制 | SA识别业务 → BWM限速/整形（三级控制） |
| **Shaping整形层** | GWFD-020354 基于业务的Shaping | - | 用户级令牌桶整形，缓冲超额报文 |
| **Shaping增强层** | GWFD-110313 智能Shaping组级带宽控制 | - | 组级智能整形，自动模式调优 |
| **FUP累计流量层** | GWFD-020353 基于累计流量的策略控制 | WSFD-109104 基于累计流量的策略控制 | 会话级FUP，URR流量阈值监控 |
| **FUP业务级层** | GWFD-110312 基于业务累计流量的策略控制 | WSFD-211009 基于业务累计流量的策略控制 | 业务级FUP，per SVC/per APP独立累计 |
| **GBR保证层** | GWFD-020358 业务触发的QoS保证 | WSFD-109107 业务触发的QoS保证 | 专有承载/QoS Flow建立，GBR带宽下限保证 |
| **ADC应用检测层** | GWFD-020357 增强的ADC基本功能 | WSFD-109102 ADC基本功能 | L7应用检测上报，触发PCRF动态策略 |
| **异常检测层** | GWFD-020305 终端异常下行流量检测 | - | 异常流量检测，阻断恶意终端 |
| **无线资源优化层** | GWFD-020359 IM类业务无线资源管控 | - | IM业务DSCP标记，优化无线调度 |
| **无线资源优化层** | GWFD-110301 基于终端系统的码率差异化控制 | - | 按终端OS类型差异化码率 |
| **无线资源优化层** | GWFD-110302 基于上下行解耦的视频承载信令控制 | - | 视频业务上下行解耦 |
| **无线资源优化层** | GWFD-110331 基于业务流标识的无线资源优化 | - | FPI/DSCP标记，无线调度优化 |
| **无线资源优化层** | GWFD-110332 基于小区负荷上报的无线资源优化 | WSFD-211101 基于小区负荷上报的无线资源优化 | 小区负荷感知→PCRF动态调整带宽 |
| **位置感知层** | - | WSFD-109108 基于接入点策略控制 | WiFi用户位置变化感知→差异化策略 |
| **数据维护层** | GWFD-111600 SA特征库更新管控 | - | SA特征库版本License管理 |

### 1.2 按产品归属分类

| 产品 | 特性数量 | 特性ID列表 |
|------|----------|------------|
| **UDG（用户面）** | 16 | GWFD-110101, GWFD-020351, GWFD-110311, GWFD-110312, GWFD-110313, GWFD-020353, GWFD-020354, GWFD-020305, GWFD-020357, GWFD-020358, GWFD-020359, GWFD-110301, GWFD-110302, GWFD-110331, GWFD-110332, GWFD-111600 |
| **UNC（控制面）** | 8 | WSFD-109101, WSFD-109102, WSFD-109104, WSFD-109107, WSFD-109108, WSFD-211005, WSFD-211009, WSFD-211101 |

### 1.3 UDG-UNC配对特性

以下8对特性构成UDG（用户面执行）与UNC（控制面决策）的完整协作：

| 序号 | UDG侧（用户面执行） | UNC侧（控制面决策） | 协作模式 |
|------|---------------------|---------------------|----------|
| 1 | GWFD-020351 PCC基本功能 | WSFD-109101 PCC基本功能 | UNC接收PCRF/PCF QoS策略 → N4下发 → UDG执行限速/整形/门控 |
| 2 | GWFD-110311 基于业务感知的带宽控制 | WSFD-211005 基于业务感知的带宽控制 | UNC配置BWM规则(POLICYTYPE=BWM) → N4下发 → UDG SA识别+BWM执行 |
| 3 | GWFD-020353 基于累计流量的策略控制 | WSFD-109104 基于累计流量的策略控制 | UNC接收PCRF阈值 → N4 URR下发 → UDG流量检测 → 上报 → UNC转发PCRF → QoS变更 |
| 4 | GWFD-110312 基于业务累计流量的策略控制 | WSFD-211009 基于业务累计流量的策略控制 | 同上但粒度为业务级（per SVC/per APP） |
| 5 | GWFD-020358 业务触发的QoS保证 | WSFD-109107 业务触发的QoS保证 | UDG业务识别 → 上报QoS事件 → UNC发起专有承载/QoS Flow建立 |
| 6 | GWFD-020357 增强的ADC基本功能 | WSFD-109102 ADC基本功能 | UDG检测应用 → UNC转发PCRF/PCF → 策略决策 → UNC承载管理 |
| 7 | GWFD-110332 基于小区负荷上报的无线资源优化 | WSFD-211101 基于小区负荷上报的无线资源优化 | UDG检测负荷 → UNC转发PCRF → PCRF下发带宽策略 → UDG执行 |
| 8 | GWFD-110311 SA-Basic (共享) | WSFD-211005 BWM (间接配合) | SA特征库仅驻留UDG，UNC通过N4间接依赖 |

### 1.4 按带宽控制机制分类

| 机制类型 | 特性 | 控制方式 |
|----------|------|----------|
| **CAR限速（Policing）** | GWFD-110311, WSFD-211005 | 令牌桶直接丢弃超额报文 |
| **Shaping整形** | GWFD-020354, GWFD-110313 | 令牌桶缓冲超额报文 + GTS队列 |
| **GBR保证（带宽下限）** | GWFD-020358, WSFD-109107 | 专有承载/QoS Flow分配专用资源 |
| **FUP降速** | GWFD-020353, GWFD-110312, WSFD-109104, WSFD-211009 | 累计流量达阈值后PCRF/PCF下发新QoS（降低MBR） |
| **门控阻断** | GWFD-020305, GWFD-110311 (Gate=Closed) | 关闭门控直接阻断流量 |
| **DSCP标记** | GWFD-020359, GWFD-110331 | 标记报文优先级影响无线调度 |
| **码率差异化** | GWFD-110301 | 按终端OS差异化BWM策略 |
| **位置差异化** | WSFD-109108 | 按WiFi接入点位置差异化策略 |

### 1.5 滚动发布时间线

| 发布批次 | 首发版本 | 特性 | 分析要点 |
|----------|----------|------|----------|
| **第1批（基础平台）** | UDG 20.0.0 / UNC 20.0.0 | GWFD-110101 SA-Basic, GWFD-020351 PCC基本功能, WSFD-109101 PCC基本功能 | 最底层的基础设施特性，没有它们后续特性均无法工作 |
| **第2批（核心控制）** | UDG 20.1.0 ~ 20.2.0 | GWFD-020353 会话FUP, GWFD-020354 Shaping, GWFD-020357 ADC, GWFD-020358 QoS保证, GWFD-020305 异常检测 | 在基础平台上叠加核心带宽控制能力 |
| **第3批（增强扩展）** | UDG 20.5.0 ~ 20.7.0 | GWFD-110312 业务FUP, GWFD-110313 智能Shaping, GWFD-020359 IM管控, GWFD-110331 FPI标记, WSFD-109102 ADC, WSFD-109104 会话FUP, WSFD-109107 QoS保证, WSFD-109108 接入点策略, WSFD-211005 BWM, WSFD-211009 业务FUP, WSFD-211101 小区负荷 | 大规模扩展期，UNC侧特性大量上线，实现CU分离协作 |
| **第4批（精细优化）** | UDG 20.8.2 ~ 20.12.2 | GWFD-110301 码率差异化, GWFD-110302 视频解耦, GWFD-110332 小区负荷, GWFD-111600 SA特征库管控, GWFD-110311 BWM v02 | 面向视频优化、终端系统差异化等垂直场景 |

**时间线规律**: 基础先行（20.0.0），核心控制紧随（20.1~20.2），大规模扩展在20.5~20.7，精细优化在20.8+。UNC侧特性集中在20.5.0~20.7.0发布，说明CU分离是分阶段引入的。

---

## 2. 共性分析

### 2.1 共享的PCC框架架构

**核心发现**: 24个特性中有22个直接或间接依赖PCC框架，PCC是带宽控制场景的统一基础设施。

```
PCRF/PCF (策略决策源)
    │
    ├── Gx接口 (2/3/4G): Diameter协议, CCR/CCA/RAR/RAA
    ├── N7接口 (5G): HTTP/2 JSON, Npcf_SMPolicyControl
    │
    ▼
UNC (控制面 PCEF-C)
    │  WSFD-109101 PCC基本功能（UNC侧基础）
    │  ├── 接收QoS参数: QCI/5QI, MBR-UL/DL, GBR-UL/DL, ARP
    │  ├── 规则生命周期: 建立/更新/终止
    │  ├── Event Triggers: USAGE_REPORT, QOS_CHANGE, APP_STA/STO等
    │  └── PCRF冗余: 主备/轮询/百分比模式
    │
    ▼ (N4/PFCP接口)
    │
UDG (用户面 PCEF-U)
    │  GWFD-020351 PCC基本功能（UDG侧基础）
    │  ├── N4规则: PDR, FAR, QER, URR, BAR
    │  ├── QoS执行: MBR限速, GBR保障, Gate门控
    │  ├── 本地PCC: 无PCRF时使用本地静态规则
    │  └── SET REFRESHSRV: 策略刷新
    │
    ▼
带宽控制效果
```

**PCC框架的共用配置对象**:

| 配置对象 | UDG命令 | UNC命令 | 跨产品一致性要求 |
|----------|---------|---------|------------------|
| RULE（规则） | ADD RULE | ADD RULE | 动态PCC场景RULENAME必须全网一致 |
| USERPROFILE（用户模板） | ADD USERPROFILE | ADD USERPROFILE | 预定义规则组名称必须一致 |
| RULEBINDING（规则绑定） | ADD RULEBINDING | ADD RULEBINDING | - |
| PCCPOLICYGRP（策略组） | ADD PCCPOLICYGRP | ADD PCCPOLICYGRP | - |
| FLOWFILTER（流过滤器） | ADD FLOWFILTER | ADD FLOWFILTER | ADC场景三网元一致 |
| FILTER / L7FILTER | ADD FILTER / L7FILTER | - | UDG独有 |
| QOSPROP（QoS属性） | ADD QOSPROP | ADD QOSPROP | - |
| URR（使用量上报规则） | ADD URR | ADD URR | URRID必须一致 |
| URRGROUP | ADD URRGROUP | ADD URRGROUP | - |
| USRPROFGROUP | ADD USRPROFGROUP | ADD USRPROFGROUP | - |
| UPBINDUPG | ADD UPBINDUPG | ADD UPBINDUPG | - |
| APNUSRPROFG | ADD APNUSRPROFG | ADD APNUSRPROFG | APN/DNN名称必须一致 |
| ADCPARA | ADD ADCPARA | ADD ADCPARA | ADC参数三网元一致 |

**PCC Event Triggers 共用情况**:

| Event Trigger | 触发值 | 使用特性 | 触发场景 |
|---------------|--------|----------|----------|
| USAGE_REPORT | - | 会话FUP, 业务FUP | 流量阈值耗尽时上报 |
| QOS_CHANGE | - | QoS保证 | 业务QoS变更时触发 |
| APPLICATION_START | - | ADC | 应用开始时触发 |
| APPLICATION_STOP | - | ADC | 应用结束时触发 |
| APP_STA (N7) | - | ADC (5G) | 5G应用开始 |
| APP_STO (N7) | - | ADC (5G) | 5G应用结束 |
| UE_LOCAL_IP_ADDRESS_CHANGE | 43 | 接入点策略 | WiFi用户Local IP + UDP Port变化 |
| CELL_CONGESTION_CHANGE | 1003 | 小区负荷 | 小区负荷等级变化 |

**PCC规则类型与特性映射**:

| 规则类型 | 来源 | 适用特性 | 说明 |
|----------|------|----------|------|
| **动态规则** | PCRF/PCF实时下发 | BWM, FUP, ADC, QoS保证 | PCRF/PCF通过Gx/N7接口动态安装规则 |
| **预定义规则** | UNC/UDG本地预配置 | BWM, QoS保证, ADC | 规则名由PCRF/PCF下发，但规则内容在本地配置 |
| **UserProfile规则** | UNC本地配置 | BWM, ADC, QoS保证 | 基于用户签约信息的本地策略 |
| **本地规则** | UDG本地配置 | PCC基本功能(无PCRF时) | 无PCRF场景下使用的静态本地规则 |

### 2.2 共享的SA业务感知基础

**核心发现**: SA-Basic（GWFD-110101）是整个带宽控制场景的数据基础。

以下特性直接依赖SA的识别能力：
- GWFD-110311 / WSFD-211005 BWM（基于SA识别执行限速）
- GWFD-110312 / WSFD-211009 业务级FUP（基于SA识别按业务累计流量）
- GWFD-020354 Shaping（基于SA识别执行整形）
- GWFD-110313 智能Shaping（基于SA识别执行组级整形）
- GWFD-020357 / WSFD-109102 ADC（SA引擎的L7应用检测）
- GWFD-020358 / WSFD-109107 QoS保证（SA识别触发专有承载）
- GWFD-020305 异常流量检测（SA辅助识别异常模式）
- GWFD-020359 IM业务管控（SA识别IM业务类型）
- GWFD-110301 码率差异化（SA识别终端OS）
- GWFD-110302 视频承载控制（SA识别视频业务）
- GWFD-110331 FPI标记（SA识别业务流）
- GWFD-111600 SA特征库管控（维护SA数据本身）

**SA数据层次**:
```
SA特征库（GWFD-111600 管控版本）
    │
    ▼
SA-Basic 引擎（GWFD-110101）
    ├── L3/L4 解析（IP/端口/协议）
    ├── 协议识别（知名端口 + 签名匹配）
    └── L7 解析（URL / Method / Response Code）
    │
    ▼
业务标识输出
    ├── SVC（业务大类）: P2P, VoIP, Video, IM, Game...
    └── APP（具体应用）: BitTorrent, QQ, YouTube...
    │
    ▼
供 BWM / FUP / Shaping / ADC / QoS保证 等特性使用
```

### 2.3 共享的License控制机制

**核心发现**: 所有24个特性都有独立的License控制项，且使用统一的 `SET LICENSESWITCH` 命令开启。

| 产品 | License命令 | 特性License数量 |
|------|-------------|----------------|
| UDG | SET LICENSESWITCH | 16个独立License项 |
| UNC | SET LICENSESWITCH | 8个独立License项 |

**License依赖链**:
```
基础License（必须先开启）
├── UDG: 82209825 LKV3G5PCCB01 (PCC基本功能)
├── UDG: 82209749 LKV3G5SABS01 (SA-Basic)
├── UNC: 82207979 LKV3W9SPCC11 (PCC基本功能 SMF/PGW-C)
└── UNC: 82209964 LKV2PCCBF01 (PCC基本功能 AMF)
        │
        ▼
功能License（在基础License之上叠加）
├── UDG: 82209832 LKV3G5TCSA01 (BWM)
├── UDG: 82200AFN LKV3G5SBTS01 (Shaping)
├── UDG: 82200FNS LKV3G5FSHP01 (智能Shaping)
├── UDG: 82200AFM LKV3G5PCBT01 (会话级FUP)
├── UDG: 82209776 LKV3G5FPBS01 (业务级FUP)
├── UDG: 82200AFP LKV3G5STQE01 (QoS保证)
├── UDG: 82200AFK LKV3G5ADCF01 (ADC)
├── UDG: 82200BAJ LKV3G5ADTD01 (异常检测)
├── UDG: 82200BLD LKV3G5ITSR01 (IM管控)
├── UDG: 82209784 LKV3G5RDSC01 (码率差异化)
├── UDG: 82200EBQ LKV3G5SCUD01 (上下行解耦)
├── UDG: 82200DHE LKV3G5WOFR01 (FPI标记)
├── UDG: 82200DHW LKV3G5WOCR01 (小区负荷)
├── UDG: 81203996 LKV3G5SSDUC1 (SA特征库管控)
├── UNC: 82200CQU LKV3TCBSA01 (BWM)
├── UNC: 82207980 LKV3W9PCBT12 (会话级FUP)
├── UNC: 82200BNU LKV2FUPSAT01 (业务级FUP)
├── UNC: 82208819 LKV3W9STQE11 (QoS保证)
├── UNC: 82200BNK LKV2BADCF01 (ADC)
├── UNC: 82209475 LKV3WPWULI11 (接入点策略)
└── UNC: 82209457 LKV3W9WOCR11 (小区负荷)
```

### 2.4 共享的接口体系

| 接口 | 协议 | 连接网元 | 涉及特性数 | 核心功能 |
|------|------|----------|------------|----------|
| **Gx** | Diameter (3GPP 29.212) | PCRF ↔ PGW-C/GGSN | 16+ (所有UNC特性) | 2/3/4G QoS策略下发，Event Triggers |
| **N7** | HTTP/2 JSON (3GPP 29.512) | PCF ↔ SMF | 16+ (所有UNC特性) | 5G SM策略下发，PCR Triggers |
| **N4** | PFCP (3GPP 29.244) | SMF/PGW-C ↔ UPF/PGW-U | 24 (所有特性) | 控制面→用户面规则传递 |
| **GTP-U扩展头** | 3GPP 29.281 | RAN ↔ UPF/PGW-U | 2 (GWFD-110331/110332) | FPI标记 / 小区负荷 |

### 2.5 共享的配置对象绑定链

**核心发现**: 几乎所有需要按APN/DNN生效的策略都使用相同的绑定链。

**标准绑定链（UDG侧和UNC侧均适用）**:
```
ADD RULE (定义规则)
    │
    ▼
ADD USERPROFILE (用户模板, UPTYPE=PCC)
    │
    ├── ADD RULEBINDING (绑定Rule到UserProfile)
    │
    ▼
ADD USRPROFGROUP (用户模板组)
    │
    ├── ADD UPBINDUPG (绑定UserProfile到Group)
    │
    ▼
ADD APNUSRPROFG (绑定Group到APN/DNN)
```

使用此绑定链的特性列表:
- GWFD-110101 SA-Basic
- GWFD-020351 PCC基本功能（UDG侧）
- WSFD-109101 PCC基本功能（UNC侧）
- GWFD-110311 / WSFD-211005 BWM
- GWFD-020354 Shaping
- GWFD-110312 / WSFD-211009 业务级FUP
- GWFD-020353 / WSFD-109104 会话级FUP
- GWFD-020358 / WSFD-109107 QoS保证
- GWFD-020357 / WSFD-109102 ADC
- GWFD-110301 码率差异化

### 2.6 共享的N4规则体系

| N4规则类型 | 全称 | 功能 | 使用特性 |
|------------|------|------|----------|
| **PDR** | Packet Detection Rule | 包检测规则，定义业务流匹配 | 所有需要业务流识别的特性 |
| **FAR** | Forwarding Action Rule | 转发规则，定义报文处理 | 门控、重定向场景 |
| **QER** | QoS Enforcement Rule | QoS执行规则，限速/整形 | BWM, Shaping, GBR保证 |
| **URR** | Usage Reporting Rule | 使用量上报规则，流量监控 | FUP, QoS保证, ADC |
| **BAR** | Buffering Action Rule | 缓冲规则 | Shaping场景 |

---

## 3. 配置差异分析

### 3.1 UDG vs UNC 配置焦点差异

| 维度 | UDG（用户面） | UNC（控制面） |
|------|---------------|---------------|
| **配置重点** | 执行参数（CIR/PIR/CBS/PBS, Shaping/Policing模式, 队列深度） | 策略逻辑（规则名, 策略类型, 优先级, 绑定关系） |
| **QoS参数** | 执行MBR限速、GBR保障、Gate门控 | 接收PCRF/PCF的QCI/5QI/MBR/GBR/ARP并下发 |
| **BWM配置** | ADD BWMSERVICE/BWMCONTROLLER/BWMUSERGROUP/BWMRULE（三级控制体系） | ADD RULE(POLICYTYPE=BWM) → USERPROFILE绑定 |
| **FUP配置** | ADD URR（执行流量计数） | ADD URR + URRGROUP + PCCPOLICYGRP（含Monitoring-Key） |
| **规则执行** | DPI引擎 + 令牌桶 + GTS队列 | 不执行实际控制，仅N4下发 |
| **SA特征库** | LOD SIGNATUREDB / LOD PARSERDB（加载特征库） | 不使用特征库 |

### 3.2 BWM三级控制体系（仅UDG侧）

GWFD-110311 定义了UDG侧独有的三级BWM控制体系，UNC侧无对应：

| 层级 | 配置命令 | 控制对象 | 典型场景 |
|------|----------|----------|----------|
| **用户级** | ADD BWMUSERGROUP + ADD BWMRULE | 单个用户的特定业务 | 用户P2P限速 |
| **用户组级** | ADD BWMUSERGROUP + ADD BWMRULE | 一组用户的总带宽 | APN级带宽池 |
| **全局级** | ADD BWMRULEGLOBAL | 整机级业务带宽 | 全局P2P总量控制 |

**关键参数对比**:

| 参数 | BWM(CAR/Policing) | Shaping | 智能Shaping |
|------|--------------------|---------|------------- |
| CTRLTYPE | CAR | SHAPING（固定） | SHAPING（固定） |
| CIR | 承诺信息速率 | - | - |
| PIR | 峰值信息速率 | - | - |
| RATE | - | 限速速率 | 限速速率 |
| QUEDEPTH | - | 队列深度 | 队列深度 |
| WORKMODE | - | - | AUTO/MANUAL |
| BWMRULETYPE | SUBSCRIBER_SPECIFIC / GROUP_SPECIFIC / GLOBAL | SUBSCRIBER_SPECIFIC（固定） | GROUP_SPECIFIC |

### 3.3 Gx vs N7 接口配置差异

| 配置维度 | Gx接口（2/3/4G） | N7接口（5G） |
|----------|-------------------|--------------|
| **策略请求** | CCR-Initial / CCR-Update | Npcf_SMPolicyControl_Create/Update Request |
| **策略响应** | CCA-Initial / CCA-Update | Npcf_SMPolicyControl_Create/Update Response |
| **PCRF推送** | RAR (Re-Auth-Request) | Npcf_SMPolicyControl_UpdateNotify Request |
| **QoS参数** | QCI, MBR-UL/DL (AVP) | 5QI, Session-AMBR (JSON) |
| **流量监控** | Usage-Monitoring-Information AVP | umDecs JSON (volumeThreshold) |
| **流量上报** | CCR-U (Used-Service-Unit) | accuUsageReports (volUsage) |
| **带宽控制** | QoS-Information AVP + Default-EPS-Bearer-QoS | authSessAmbr + QoSData |
| **ADC触发器** | APPLICATION_START / APPLICATION_STOP | APP_STA / APP_STO |
| **FUP阈值类型** | Granted-Service-Unit | volumeThreshold / volumeThresholdUplink / volumeThresholdDownlink |
| **UNC侧FUP配置** | 需要SET PCCFUNC + MOD PCRF(UMCH) + MOD PCCPOLICYGRP(FUPSESSIONEXC) | 仅需License（PCF侧配置） |
| **PCRF冗余** | 主备/轮询/百分比 + Failover | GROUPID/PRIORITY模式 |
| **UMCH拥塞处理** | 支持（Monitoring-Time AVP） | 不支持（无UMCH机制） |

### 3.4 FUP两种粒度对比

| 维度 | 会话级FUP | 业务级FUP |
|------|-----------|-----------|
| **UDG特性** | GWFD-020353 | GWFD-110312 |
| **UNC特性** | WSFD-109104 | WSFD-211009 |
| **UDG License** | 82200AFM LKV3G5PCBT01 | 82209776 LKV3G5FPBS01 |
| **UNC License** | 82207980 LKV3W9PCBT12 | 82200BNU LKV2FUPSAT01 |
| **累计粒度** | per Session（整会话所有流量） | per SVC / per APP（按业务独立累计） |
| **Gx UM Level** | SESSION_LEVEL(0) | PCC_RULE_LEVEL(1) |
| **N7 URR绑定** | URR关联到所有Create PDRs | URR只绑定指定业务流的PDRs |
| **Monitoring-Key** | 与规则配置无关 | 标识一种业务（不同业务不同Key） |
| **SA依赖** | 不依赖SA（不需要业务识别） | 依赖SA + BWM |
| **典型场景** | 用户月总流量100GB后降速 | P2P周限50MB，视频月限100GB |

### 3.5 GBR保证 vs BWM限速

| 维度 | GBR保证（GWFD-020358 / WSFD-109107） | BWM限速（GWFD-110311 / WSFD-211005） |
|------|---------------------------------------|---------------------------------------|
| **控制方向** | 带宽下限保证（保证不低于GBR） | 带宽上限控制（限制不超过CIR/PIR） |
| **资源类型** | GBR（专用资源） | Non-GBR（共享资源池） |
| **载体** | 专有承载 / 专有QoS Flow | 缺省承载上的QER |
| **QoS参数** | GBR-UL/DL, MBR-UL/DL, QCI/5QI, ARP | CIR, PIR, CBS, PBS |
| **最大数量** | 每用户10个专有承载 / 63个QoS Flow | 无固定上限（受License限制） |
| **触发方式** | 业务识别触发（UPF上报QoS事件） | 规则匹配触发（SA识别业务后匹配BWM规则） |
| **QoSProp配置** | QOSTYPE=QOS_FLOW_PARA(5G) / QOS_BEARER_PARA(2/3/4G) | 不使用QOSPROP |
| **URR用途** | USAGERPTMODE=QOS（QoS事件上报） | USAGERPTMODE=ONLINE/MONITORINGKEY（流量上报） |

---

## 4. 依赖关系分析

### 4.1 特性依赖图

```
                          ┌─────────────────────┐
                          │ GWFD-111600 SA特征库 │
                          │ 更新管控（数据维护）  │
                          └──────────┬──────────┘
                                     │ 维护特征库
                                     ▼
                    ┌────────────────────────────────┐
                    │ GWFD-110101 SA-Basic           │
                    │ （业务感知基础，所有SA特性依赖） │
                    └───────────────┬────────────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
              ▼                     ▼                     ▼
    ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
    │ GWFD-020351     │  │ GWFD-110311     │  │ GWFD-020357     │
    │ PCC基本功能     │  │ BWM (核心)      │  │ ADC             │
    │ (UDG基础)       │  │                 │  │                 │
    └────────┬────────┘  └────────┬────────┘  └────────┬────────┘
             │                     │                     │
    ┌────────┼────────────┐       │                     │
    │        │            │       │                     │
    ▼        ▼            ▼       ▼                     ▼
┌────────┐┌────────┐┌────────┐┌──────────┐    ┌──────────────┐
│GWFD    ││GWFD    ││GWFD    ││GWFD      │    │GWFD-020358   │
│-020353 ││-020354 ││-020358 ││-110312   │    │(间接: SA+PCC)│
│会话FUP ││Shaping ││QoS保证 ││业务FUP   │    └──────────────┘
└────────┘└────────┘└────────┘└──────────┘
                 │
                 ▼
          ┌────────────────┐
          │ GWFD-110313    │
          │ 智能Shaping    │
          │ (依赖BWM+Shape)│
          └────────────────┘
```

### 4.2 核心特性辐射分析

**SA-Basic (GWFD-110101)** 的辐射范围最大，以下12个特性直接依赖它：

| 依赖特性 | 依赖方式 | SA提供的能力 |
|----------|----------|-------------|
| GWFD-110311 BWM | 直接依赖 | 业务识别（SVC/APP）→ BWM规则匹配 |
| GWFD-110312 业务FUP | 直接依赖 | 业务识别 → 按业务累计流量 |
| GWFD-020354 Shaping | 直接依赖 | 业务识别 → 按业务整形 |
| GWFD-110313 智能Shaping | 间接依赖（通过BWM+Shaping） | 业务识别 → 按业务组级整形 |
| GWFD-020357 ADC | 直接依赖 | L7 DPI引擎（ADC使用SA引擎） |
| GWFD-020358 QoS保证 | 直接依赖 | 业务识别 → 触发专有承载 |
| GWFD-020305 异常检测 | 间接依赖 | SA辅助识别异常流量模式 |
| GWFD-020359 IM管控 | 直接依赖 | SA识别IM业务类型（QQ/MSN/Fetion） |
| GWFD-110301 码率差异化 | 直接依赖 | SA识别终端OS类型 |
| GWFD-110302 视频承载 | 直接依赖 | SA识别视频业务 |
| GWFD-110331 FPI标记 | 直接依赖 | SA识别业务流 → FPI/DSCP标记 |
| GWFD-110332 小区负荷 | 间接依赖 | 不直接依赖SA，但需BWM配合执行 |

**PCC基本功能 (GWFD-020351 / WSFD-109101)** 的辐射范围：

| UDG侧依赖特性 | UNC侧依赖特性 | PCC提供的能力 |
|---------------|---------------|-------------|
| GWFD-110311 BWM | WSFD-211005 BWM | PCC规则体系（RULE/USERPROFILE/PCCPOLICYGRP） |
| GWFD-110312 业务FUP | WSFD-211009 业务FUP | URR使用量上报机制 |
| GWFD-020353 会话FUP | WSFD-109104 会话FUP | URR + Event Triggers |
| GWFD-020358 QoS保证 | WSFD-109107 QoS保证 | 专有承载/QoS Flow信令 |
| GWFD-020357 ADC | WSFD-109102 ADC | PCC规则中Application ID传递 |
| GWFD-020305 异常检测 | - | 内容计费基础功能 |
| GWFD-020359 IM管控 | - | DSCP标记机制 |
| GWFD-110301 码率差异化 | - | BWM基础（间接依赖PCC） |
| GWFD-110302 视频承载 | - | QoS属性配置 |
| GWFD-110331 FPI标记 | - | PCC规则匹配 |
| - | WSFD-109108 接入点策略 | Gx接口Event-Trigger上报 |
| - | WSFD-211101 小区负荷 | Gx接口CELL-CONGESTION-CHANGE上报 |

### 4.3 UDG-UNC协作链路分析

**链路1: BWM带宽控制（最核心）**
```
PCRF/PCF
  │ (Gx/N7) 下发预定义BWM规则名
  ▼
UNC (WSFD-211005)
  │ ADD RULE(POLICYTYPE=BWM) → USERPROFILE绑定
  │ (N4) 下发BWM规则
  ▼
UDG (GWFD-110311)
  │ SA识别业务 → 匹配BWM规则 → 执行CAR/Shaping
  │ ADD BWMSERVICE/BWMCONTROLLER/BWMUSERGROUP/BWMRULE
  ▼
带宽控制效果
```

**链路2: FUP降速**
```
PCRF/PCF
  │ (Gx) Usage-Monitoring-Information (阈值)
  │ (N7) umDecs.volumeThreshold
  ▼
UNC (WSFD-109104 / WSFD-211009)
  │ ADD URR + URRGROUP + PCCPOLICYGRP
  │ (N4) Create URR (流量阈值)
  ▼
UDG (GWFD-020353 / GWFD-110312)
  │ 流量计数 → 达阈值 → PFCP Session Report
  ▼
UNC → PCRF/PCF (accuUsageReports)
  │
  ▼ PCRF/PCF决策 → 新QoS (authSessAmbr降速)
  │
UNC → UDG (N4 Update URR/QER)
  │
  ▼
UDG 执行新QoS（MBR降低 → 实际限速）
```

**链路3: GBR保证**
```
UDG (GWFD-020358)
  │ SA识别高价值业务 → 匹配预定义规则
  │ PFCP Session Report (URR ID + Rule Information)
  ▼
UNC (WSFD-109107)
  │ 接收QoS事件 → 基于QoS策略
  │ 发起专有承载(2/3/4G) / 专有QoS Flow(5G)建立
  │ ADD QOSPROP(GBR/MBR/5QI/QCI/ARP)
  │ AMF/MME → RAN → UE (N1N2/Create Bearer)
  ▼
专有承载/QoS Flow建立 → GBR带宽保障
```

### 4.4 典型场景组合

| 场景 | 涉及特性组合 | 数据流 |
|------|-------------|--------|
| **P2P限速** | SA-Basic + BWM + PCC | SA识别P2P → BWM CAR限速 |
| **视频带宽保障** | SA-Basic + QoS保证 + PCC | SA识别视频 → 专有承载(GBR) |
| **月流量超限降速** | 会话级FUP + PCC | URR累计 → PCRF降MBR → QER限速 |
| **P2P月限独立累计** | SA-Basic + 业务级FUP + PCC | SA识别P2P → per SVC URR累计 → PCRF降速 |
| **组级智能整形** | SA-Basic + BWM + Shaping + 智能Shaping | SA识别 → BWM匹配 → 组级Shaping自动调优 |
| **小区拥塞限速** | 小区负荷上报 + BWM + PCC | RAN负荷 → UDG上报 → PCRF策略 → BWM限低优用户 |
| **异常终端阻断** | SA-Basic + 异常检测 | SA辅助 → 检测异常下行 → 阻断/告警 |
| **WiFi位置差异化** | 接入点策略 + PCC + BWM | 位置变化 → PCRF策略切换 → BWM差异化限速 |

---

## 5. 关键发现

### 5.1 发现一：PCC-RULE-POLICYTYPE 是统一策略标识

**核心发现**: 在UNC侧，`ADD RULE` 命令的 `POLICYTYPE` 参数是区分不同带宽控制策略类型的统一标识。

| POLICYTYPE取值 | 标识的策略类型 | 涉及特性 |
|----------------|---------------|----------|
| **BWM** | 带宽管理策略 | WSFD-211005, GWFD-110311 |
| **PCC** | 标准PCC策略（含FUP） | WSFD-109104, WSFD-211009, GWFD-020353, GWFD-110312 |
| **QOS** | QoS属性直接绑定 | WSFD-109107, GWFD-020358 |
| **ADC** | 应用检测策略 | WSFD-109102, GWFD-020357 |
| **CHARGING** | 计费策略 | （计费场景特性） |

**关键约束**: PCC类型的RULENAME值与QOS类型的RULENAME值不能相同。同名规则可以存在不同策略类型（如一个BWM、一个CHARGING）。

### 5.2 发现二：URR的多种用途模式

**核心发现**: URR（Usage Reporting Rule）在不同特性中有不同的配置模式，是连接控制面和用户面的核心数据结构。

| 特性 | USAGERPTMODE | URR关联对象 | 上报触发条件 |
|------|-------------|-------------|-------------|
| 会话级FUP | ONLINE / MONITORINGKEY | 所有Create PDRs | VOLTH（流量阈值耗尽） |
| 业务级FUP | MONITORINGKEY | 指定业务流的PDRs | VOLTH |
| QoS保证 | QOS | PDR + Rule Information | 业务识别触发/业务流老化 |
| ADC | - | PDR + Application ID | APPLICATION_START/STOP |
| 异常检测 | - | Content Charging PDR | 阈值计数触发 |

### 5.3 发现三：三层QoS参数传递链

**核心发现**: QoS参数从PCRF/PCF到最终用户面执行，经历三层传递。

```
第1层: PCRF/PCF → UNC (Gx/N7)
  PCRF: QoS-Information AVP (QCI/5QI, MBR-UL/DL, GBR-UL/DL, ARP)
  PCF:  QoSData JSON (5QI, maxbrUl/Dl, gbrUl/Dl, arp)
        │
第2层: UNC → UDG (N4/PFCP)
  SMF: Create QER (QFI, QoS Flow Identifier)
       Create URR (Volume Threshold)
       Update QER (Gate Status, MBR)
        │
第3层: UDG 用户面执行
  QER → 令牌桶限速 (CIR/PIR/CBS/PBS)
  QER → Gate门控 (Open/Closed)
  QER → GBR保障 (专用资源调度)
```

### 5.4 发现四：双产品License编号体系差异

**核心发现**: UDG和UNC的License编号体系完全独立，同一功能在两侧需要分别获取License。

| 功能 | UDG License | UNC License | 差异说明 |
|------|-------------|-------------|----------|
| PCC基本功能 | 82209825 LKV3G5PCCB01 | 82207979 LKV3W9SPCC11 | 编号完全不同 |
| BWM | 82209832 LKV3G5TCSA01 | 82200CQU LKV3TCBSA01 | 编号完全不同 |
| 会话级FUP | 82200AFM LKV3G5PCBT01 | 82207980 LKV3W9PCBT12 | 编号接近但不同后缀 |
| 业务级FUP | 82209776 LKV3G5FPBS01 | 82200BNU LKV2FUPSAT01 | 编号完全不同 |
| QoS保证 | 82200AFP LKV3G5STQE01 | 82208819 LKV3W9STQE11 | 后缀01 vs 11 |
| ADC | 82200AFK LKV3G5ADCF01 | 82200BNK LKV2BADCF01 | 前缀3G5 vs 2B |
| 小区负荷 | 82200DHW LKV3G5WOCR01 | 82209457 LKV3W9WOCR11 | 前缀3G5 vs 3W9 |

**规律**: UDG License前缀多为 `LKV3G5`，UNC License前缀多为 `LKV3W9` 或 `LKV2`。末尾 `01` 表示首发版本，`11` 表示控制面版本。

### 5.5 发现五：SET REFRESHSRV 是隐藏的关键配置点

**核心发现**: 在UDG侧，`SET REFRESHSRV` 命令用于刷新策略生效，是多个特性的共同配置步骤。

涉及SET REFRESHSRV的特性:
- GWFD-020351 PCC基本功能（策略变更后刷新）
- GWFD-110101 SA-Basic（SA配置变更后刷新）
- GWFD-110311 BWM（BWM规则变更后刷新）
- GWFD-020354 Shaping（整形规则变更后刷新）

**时序约束**: 配置变更后必须执行 SET REFRESHSRV 才能生效，且执行后约60秒（PROTBINDFLOWF定时器）策略才完全下发。

### 5.6 发现六：POLICYTYPE=BWM 仅在UNC侧配置

**核心发现**: `POLICYTYPE=BWM` 是UNC侧（WSFD-211005）独有的策略类型标识。UDG侧的GWFD-110311使用完全不同的BWM配置体系（BWMSERVICE/BWMCONTROLLER/BWMUSERGROUP/BWMRULE），不使用POLICYTYPE=BWM。

这意味着：
- UNC侧通过PCC规则体系（ADD RULE POLICYTYPE=BWM）定义"做什么业务做什么控制"
- UDG侧通过BWM专有命令体系（ADD BWMRULE等）定义"怎么执行控制（CIR/PIR/模式）"
- 两侧通过RULENAME一致性建立关联

### 5.7 发现七：预定义规则名全网一致性要求

**核心发现**: 多个特性都要求规则名在多个网元间保持一致，这是配置成功的前提。

| 特性 | 一致性要求 | 涉及网元 |
|------|-----------|----------|
| BWM | RULENAME一致 | UNC + UDG + PCRF/PCF |
| ADC | FLOWFILTERNAME/appid一致 | UNC + UDG + PCRF/PCF |
| QoS保证 | 预定义规则名一致 | UNC + UDG + PCRF/PCF |
| 业务级FUP (L7) | 预定义规则名 + URR ID + UMID一致 | UNC + UDG + PCRF/PCF |
| 小区负荷 | 预定义规则名一致 | UNC + UDG + PCRF/PCF |

**规律**: 凡涉及动态PCC（PCRF/PCF下发预定义规则名）的特性，都需要多网元规则名一致性。这是跨产品配置最易出错的地方。

---

## 附录A: 24特性索引表

| 序号 | 特性ID | 特性名称 | 产品 | 网元 | 首发版本 | License控制项 | 核心能力 |
|------|--------|----------|------|------|----------|---------------|----------|
| 1 | GWFD-110101 | SA-Basic | UDG | SGW-U/PGW-U/UPF | 20.0.0 | 82209749 LKV3G5SABS01 | L3/L4/L7业务识别基础 |
| 2 | GWFD-020351 | PCC基本功能 | UDG | SGW-U/PGW-U/UPF | 20.0.0 | 82209825 LKV3G5PCCB01 | 用户面QoS策略执行 |
| 3 | GWFD-110311 | 基于业务感知的带宽控制 | UDG | SGW-U/PGW-U/UPF | 20.9.0 | 82209832 LKV3G5TCSA01 | 三级BWM（用户/组/全局） |
| 4 | GWFD-110312 | 基于业务累计流量的策略控制 | UDG | SGW-U/PGW-U/UPF | 20.5.0 | 82209776 LKV3G5FPBS01 | 业务级FUP |
| 5 | GWFD-110313 | 智能Shaping组级带宽控制 | UDG | SGW-U/PGW-U/UPF | 20.7.0 | 82200FNS LKV3G5FSHP01 | 组级智能整形自动调优 |
| 6 | GWFD-020353 | 基于累计流量的策略控制 | UDG | SGW-U/PGW-U/UPF | 20.2.0 | 82200AFM LKV3G5PCBT01 | 会话级FUP |
| 7 | GWFD-020354 | 基于业务的Shaping | UDG | SGW-U/PGW-U/UPF | 20.1.0 | 82200AFN LKV3G5SBTS01 | 用户级令牌桶整形 |
| 8 | GWFD-020305 | 终端异常下行流量检测 | UDG | SGW-U/PGW-U/UPF | 20.5.0 | 82200BAJ LKV3G5ADTD01 | 异常流量检测阻断 |
| 9 | GWFD-020357 | 增强的ADC基本功能 | UDG | SGW-U/PGW-U/UPF | 20.1.0 | 82200AFK LKV3G5ADCF01 | L7应用检测上报 |
| 10 | GWFD-020358 | 业务触发的QoS保证 | UDG | SGW-U/PGW-U/UPF | 20.2.0 | 82200AFP LKV3G5STQE01 | 专有承载/QoS Flow GBR保证 |
| 11 | GWFD-020359 | IM类业务无线资源管控 | UDG | SGW-U/PGW-U/UPF | 20.7.0 | 82200BLD LKV3G5ITSR01 | IM业务DSCP标记 |
| 12 | GWFD-110301 | 基于终端系统的码率差异化控制 | UDG | SGW-U/PGW-U/UPF | 20.9.0 | 82209784 LKV3G5RDSC01 | 终端OS差异化码率 |
| 13 | GWFD-110302 | 基于上下行解耦的视频承载信令控制 | UDG | SGW-U/PGW-U/UPF | 20.9.0 | 82200EBQ LKV3G5SCUD01 | 视频上下行解耦 |
| 14 | GWFD-110331 | 基于业务流标识的无线资源优化 | UDG | SGW-U/PGW-U/UPF | 20.7.0 | 82200DHE LKV3G5WOFR01 | FPI/DSCP无线调度标记 |
| 15 | GWFD-110332 | 基于小区负荷上报的无线资源优化 | UDG | SGW-U/PGW-U/UPF | 20.8.2 | 82200DHW LKV3G5WOCR01 | 小区负荷感知上报 |
| 16 | GWFD-111600 | SA特征库更新管控 | UDG | SGW-U/PGW-U/UPF | 20.12.2 | 81203996 LKV3G5SSDUC1 | SA特征库版本License管理 |
| 17 | WSFD-109101 | PCC基本功能 | UNC | SMF/PGW-C/AMF/GGSN | 20.0.0 | 82207979 LKV3W9SPCC11 | 控制面QoS策略接收管理 |
| 18 | WSFD-109102 | ADC基本功能 | UNC | GGSN-C/PGW-C/SMF | 20.5.0 | 82200BNK LKV2BADCF01 | 控制面应用检测中继 |
| 19 | WSFD-109104 | 基于累计流量的策略控制 | UNC | GGSN-C/PGW-C/SMF | 20.3.0 | 82207980 LKV3W9PCBT12 | 控制面会话级FUP |
| 20 | WSFD-109107 | 业务触发的QoS保证 | UNC | GGSN-C/PGW-C/SMF | 20.5.0 | 82208819 LKV3W9STQE11 | 控制面专有承载信令 |
| 21 | WSFD-109108 | 基于接入点策略控制 | UNC | PGW-C | 20.5.0 | 82209475 LKV3WPWULI11 | WiFi位置变化感知 |
| 22 | WSFD-211005 | 基于业务感知的带宽控制 | UNC | GGSN/PGW-C/SMF | 20.5.0 | 82200CQU LKV3TCBSA01 | 控制面BWM规则管理 |
| 23 | WSFD-211009 | 基于业务累计流量的策略控制 | UNC | GGSN/PGW-C/SMF | 20.3.0 | 82200BNU LKV2FUPSAT01 | 控制面业务级FUP |
| 24 | WSFD-211101 | 基于小区负荷上报的无线资源优化 | UNC | GGSN-C/PGW-C | 20.7.0 | 82209457 LKV3W9WOCR11 | 控制面负荷信息转发 |

---

## 附录B: MML命令交叉参考

### B.1 UDG侧核心命令

| 命令 | 涉及特性 | 用途 |
|------|----------|------|
| SET LICENSESWITCH | 全部16个UDG特性 | License开关 |
| SET BANDWIDTHMNG | GWFD-110311 | BWM全局使能 |
| ADD BWMSERVICE | GWFD-110311 | BWM服务实例 |
| ADD BWMCONTROLLER | GWFD-110311 | BWM控制器 |
| ADD BWMUSERGROUP | GWFD-110311 | BWM用户组 |
| ADD BWMRULE | GWFD-110311 | BWM规则（CAR/Shaping） |
| ADD BWMRULEGLOBAL | GWFD-110311 | BWM全局规则 |
| ADD BCSRVLEVELPLY | GWFD-110311 | 业务服务等级策略 |
| ADD CATEGORYPROP | GWFD-110311, GWFD-110101 | 业务分类属性 |
| ADD APNBINDBWMUSRG | GWFD-110311 | APN绑定BWM用户组 |
| ADD SNSSAI | GWFD-110311 | 网络切片绑定 |
| ADD RULE | GWFD-110101, GWFD-020351 | PCC规则定义 |
| ADD FLOWFILTER | GWFD-110101, GWFD-020351 | 流过滤器 |
| ADD FILTER | GWFD-110101, GWFD-020351 | L3/L4过滤器 |
| ADD L7FILTER | GWFD-110101 | L7过滤器 |
| ADD FLTBINDFLOWF | GWFD-020351 | 过滤器绑定 |
| ADD USERPROFILE | GWFD-110101, GWFD-020351 | 用户模板 |
| ADD RULEBINDING | GWFD-110101, GWFD-020351 | 规则绑定 |
| ADD PCCPOLICYGRP | GWFD-020351 | PCC策略组 |
| ADD QOSPROP | GWFD-020358, GWFD-110302 | QoS属性 |
| ADD URR | GWFD-020353, GWFD-110312 | 使用量上报规则 |
| ADD URRGROUP | GWFD-020353, GWFD-110312 | URR组 |
| ADD ADCPARA | GWFD-020357 | ADC参数 |
| SET SRVCOMMONPARA | GWFD-110101 | SA公共参数 |
| SET CUINCONSPOLICY | GWFD-110101 | 收敛策略 |
| SET REFRESHSRV | GWFD-020351, GWFD-110101, GWFD-110311 | 策略刷新 |
| LOD SIGNATUREDB | GWFD-110101, GWFD-111600 | 加载SA特征库 |
| LOD PARSERDB | GWFD-110101 | 加载解析库 |
| SET APNOSLELBWMSW | GWFD-110301 | 终端OS BWM开关 |

### B.2 UNC侧核心命令

| 命令 | 涉及特性 | 用途 |
|------|----------|------|
| SET LICENSESWITCH | 全部8个UNC特性 | License开关 |
| SET PCCFUNC | WSFD-109101, WSFD-109104, WSFD-211009 | PCC功能设置 |
| SET APNPCCFUNC | WSFD-109101 | APN级PCC开关 |
| ADD PCRF | WSFD-109101 | PCRF定义 |
| ADD PCRFGROUP | WSFD-109101 | PCRF组 |
| ADD PCRFBINDGRP | WSFD-109101 | PCRF组绑定 |
| SET DFTGLBPCRFGRP | WSFD-109101 | 缺省PCRF组 |
| SET PCCFAILACTION | WSFD-109101 | PCC故障处理 |
| SET PCCTIMER | WSFD-109101 | PCC定时器 |
| ADD PCCTEMPLATE | WSFD-109101 | PCC模板 |
| ADD RULE | WSFD-211005, WSFD-109102, WSFD-109107, WSFD-211009 | 规则定义 |
| ADD USERPROFILE | WSFD-211005, WSFD-109102, WSFD-109107, WSFD-211009 | 用户模板 |
| ADD RULEBINDING | WSFD-211005, WSFD-109102, WSFD-109107, WSFD-211009 | 规则绑定 |
| ADD USRPROFGROUP | WSFD-211005, WSFD-109107, WSFD-211009 | 用户模板组 |
| ADD UPBINDUPG | WSFD-211005, WSFD-109107, WSFD-211009 | 模板绑定 |
| ADD APNUSRPROFG | WSFD-211005, WSFD-109107, WSFD-211009 | APN绑定 |
| ADD PCCPOLICYGRP | WSFD-109104, WSFD-109107, WSFD-211009 | PCC策略组 |
| ADD URR | WSFD-109107, WSFD-211009 | URR规则 |
| ADD URRGROUP | WSFD-211009 | URR组 |
| ADD QOSPROP | WSFD-109107 | QoS属性 |
| ADD FLOWFILTER | WSFD-109102 | 流过滤器 |
| ADD ADCPARA | WSFD-109102 | ADC参数 |
| SET APNIDLETIME | WSFD-109107 | 专有QoS Flow空闲定时器 |
| ADD APNDEACTQFPLCY | WSFD-109107 | 去活QoS Flow策略 |
| SET APNREPORTATTR | WSFD-211101 | APN拥塞上报属性 |
| SET POLICYMODE | WSFD-109101 | 接口模式选择 |
| SET N7RCVATTRCTRL | WSFD-109101 | N7接收属性控制 |
| SET N7SNDATTRCTRL | WSFD-109101 | N7发送属性控制 |
| SET FHBYPASS | WSFD-109101 | 紧急旁路 |

---

## 附录C: 配置对象复用矩阵

以下矩阵展示了同一配置对象在不同特性中的使用情况：

| 配置对象 | GWFD-110101 | GWFD-020351 | GWFD-110311 | GWFD-020353 | GWFD-110312 | GWFD-020354 | GWFD-110313 | GWFD-020358 | GWFD-020357 | WSFD-109101 | WSFD-211005 | WSFD-109104 | WSFD-211009 | WSFD-109107 | WSFD-109102 |
|---------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
| RULE | Y | Y | - | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| USERPROFILE | Y | Y | - | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| RULEBINDING | Y | Y | - | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| USRPROFGROUP | Y | Y | - | - | - | - | - | Y | Y | Y | Y | Y | Y | Y | Y |
| UPBINDUPG | Y | Y | - | - | - | - | - | Y | Y | Y | Y | Y | Y | Y | Y |
| APNUSRPROFG | Y | Y | - | - | - | - | - | Y | Y | Y | Y | Y | Y | Y | Y |
| PCCPOLICYGRP | - | Y | - | Y | Y | Y | Y | Y | Y | Y | - | Y | Y | Y | - |
| FLOWFILTER | Y | Y | - | - | - | - | - | - | Y | - | - | - | - | - | Y |
| FILTER | Y | Y | - | - | - | - | - | - | - | - | - | - | - | - | - |
| L7FILTER | Y | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| URR | - | - | - | Y | Y | - | - | Y | - | - | - | Y | Y | Y | - |
| URRGROUP | - | - | - | Y | Y | - | - | - | - | - | - | - | Y | - | - |
| QOSPROP | - | - | - | - | - | - | - | Y | - | - | - | - | - | Y | - |
| BWMSERVICE | - | - | Y | - | - | - | - | - | - | - | - | - | - | - | - |
| BWMCONTROLLER | - | - | Y | - | - | - | - | - | - | - | - | - | - | - | - |
| BWMUSERGROUP | - | - | Y | - | - | - | Y | - | - | - | - | - | - | - | - |
| BWMRULE | - | - | Y | - | - | Y | Y | - | - | - | - | - | - | - | - |
| CATEGORYPROP | Y | - | Y | - | - | - | - | - | - | - | - | - | - | - | - |
| ADCPARA | - | - | - | - | - | - | - | - | Y | - | - | - | - | - | Y |

**图例**: Y = 使用此配置对象; - = 不使用

**关键观察**:
1. `RULE + USERPROFILE + RULEBINDING` 是跨产品、跨特性的通用配置三元组
2. `USRPROFGROUP + UPBINDUPG + APNUSRPROFG` 是APN级策略生效的标准绑定链
3. `BWMSERVICE + BWMCONTROLLER + BWMUSERGROUP + BWMRULE` 是UDG侧BWM独有体系
4. `URR + URRGROUP` 主要用于FUP和QoS保证场景
5. `FLOWFILTER` 同时被SA-Basic、PCC和ADC使用

---

## 附录D: 典型端到端配置流程

### D.1 BWM带宽控制完整配置链路（UDG + UNC双产品）

以下为BWM场景的端到端配置步骤，展示了UDG侧和UNC侧的完整协作流程：

**第1步: 基础环境准备（UDG侧）**
```
// 开启License
SET LICENSESWITCH:LICITEM="LKV3G5SABS01",SWITCH=ENABLE;   // SA-Basic
SET LICENSESWITCH:LICITEM="LKV3G5PCCB01",SWITCH=ENABLE;   // PCC基本功能
SET LICENSESWITCH:LICITEM="LKV3G5TCSA01",SWITCH=ENABLE;   // BWM

// 加载SA特征库
LOD SIGNATUREDB:SAFILE="signature_db.dat";
LOD PARSERDB:PRFILE="parser_db.dat";

// 全局使能BWM
SET BANDWIDTHMNG:SWITCH=ENABLE;
```

**第2步: BWM三级控制配置（UDG侧）**
```
// 用户级CAR限速
ADD BWMSERVICE:NAME="p2p_svc",BWMSERVICETYPE=NONTOS,
  PROTOCOLNAME="bittorrent";
ADD BWMCONTROLLER:BWMCNAME="p2p_car",CTRLTYPE=CAR,
  CIR=2048,CBS=256000,PIR=4096,PBS=512000;
ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,
  USERGROUPNAME="gold_users",USERGROUPPRI=1,
  USERLEVSRVTYPE=NONTOS;
ADD BWMRULE:BWMRULETYPE=SUBSCRIBER_SPECIFIC,
  BWMSERVICENAME="p2p_svc",
  UPBWMCTRLNAME1="p2p_car",DNBWMCTRLNAME1="p2p_car",
  BWMRULEPRI=1;
ADD APNBINDBWMUSRG:APNNAME="internet",
  BWMUSERGROUPNAME="gold_users";

// 策略刷新（约60秒生效）
SET REFRESHSRV;
```

**第3步: UNC侧策略规则配置**
```
// 开启License
SET LICENSESWITCH:LICITEM="LKV3TCBSA01",SWITCH=ENABLE;  // BWM(UNC)

// 定义BWM策略规则（POLICYTYPE=BWM是关键标识）
ADD RULE:RULENAME="bwm_rule_p2p",POLICYTYPE=BWM,...;
ADD USERPROFILE:UPNAME="bwm_profile",UPTYPE=PCC,...;
ADD RULEBINDING:UPNAME="bwm_profile",
  RULENAME="bwm_rule_p2p",...;
ADD USRPROFGROUP:UPGNAME="bwm_upg",...;
ADD UPBINDUPG:UPGNAME="bwm_upg",UPNAME="bwm_profile";
ADD APNUSRPROFG:APNNAME="internet",UPGNAME="bwm_upg";
```

**第4步: PCRF/PCF侧规则下发**
- PCRF/PCF通过Gx/N7下发预定义规则名 `bwm_rule_p2p`
- UNC匹配本地RULE配置 → N4下发 → UDG执行

**关键约束**: RULENAME `bwm_rule_p2p` 必须在 PCRF/PCF、UNC、UDG 三处保持一致。

### D.2 会话级FUP完整配置链路

**UDG侧**:
```
ADD URR:URRID=1,USAGERPTMODE=ONLINE,
  MEASUREMENTMETHOD=VOLUME,...;
ADD URRGROUP:URRGROUPNAME="session_fUP_group",
  UPURRNAME1="1",...;
```

**UNC侧（Gx场景需额外配置）**:
```
SET PCCFUNC:MKPARSEFORMAT=ENABLE;          // 解析格式
MOD PCRF:PCRFID=1,FEATURELIST=UMCH;        // UMCH特性
MOD PCCPOLICYGRP:PCCPOLICYGRPNAME="fup_pg",
  FUPSESSIONEXC=ENABLE;                    // 会话级FUP排除
```

**UNC侧（N7场景无需额外配置）**: N7路径的FUP仅需License，阈值由PCF侧umDecs配置。

### D.3 QoS保证（GBR）完整配置链路

**UDG侧**:
```
ADD URR:URRID=100,USAGERPTMODE=QOS,...;    // QoS事件上报模式
// SA识别业务后通过URR上报触发UNC侧专载建立
```

**UNC侧**:
```
// 5G QoS Flow参数
ADD QOSPROP:QOSPROPNAME="video_gbr",
  QOSTYPE=QOS_FLOW_PARA,                   // 5G用QOS_FLOW_PARA
  FQI=5,                                   // QoS Flow Identifier
  MBRUL=10000,MBRDL=10000,                 // 最大比特率
  GBRUL=5000,GBRDL=5000,                   // 保证比特率
  ARP=5;

// 2/3/4G承载参数
ADD QOSPROP:QOSPROPNAME="video_gbr_4g",
  QOSTYPE=QOS_BEARER_PARA,                 // 2/3/4G用QOS_BEARER_PARA
  QCIVALUE=5,                              // QCI值
  MBRUL=10000,MBRDL=10000,
  GBRUL=5000,GBRDL=5000,
  ARP=5;

// 空闲定时器与去活策略
SET APNIDLETIME:APNNAME="video_apn",
  DEDQFIDLETIMER=300;                      // 专有QoS Flow空闲5分钟释放
ADD APNDEACTQFPLCY:APNNAME="video_apn",
  DEACTPOLICY=DELAY_RELEASE;               // 延迟释放策略
```

### D.4 组级智能Shaping配置链路

**依赖链**: SA-Basic → BWM → Shaping → 智能Shaping

```
ADD BWMCONTROLLER:BWMCNAME="group_shaping",
  CTRLTYPE=SHAPING,                        // 固定为SHAPING
  RATE=10000,                              // 整形速率 10Mbps
  QUEDEPTH=256,                            // 队列深度
  SRVLEVELSPEC=10,                         // 业务等级规格
  USERFAIREN=ENABLE,                       // 用户公平使能
  WORKMODE=AUTO,                           // 自动模式
  MAXPKTLOSTRATE=10000,                    // 最大丢包率（万分之一）
  PKTLOSTRATEDTL=50,                       // 丢包率差值
  ASSUREMODE=EXPFIRST;                     // 保障模式

// 为每个ServiceLevel配置策略
ADD BCSRVLEVELPLY:BWMCNAME="group_shaping",
  SERVICELEVEL=1,SHAPRATE=100;             // 高优先级 100%
ADD BCSRVLEVELPLY:BWMCNAME="group_shaping",
  SERVICELEVEL=2,SHAPRATE=60;              // 中优先级 60%
ADD BCSRVLEVELPLY:BWMCNAME="group_shaping",
  SERVICELEVEL=3,SHAPRATE=30;              // 低优先级 30%

ADD BWMRULE:BWMRULETYPE=GROUP_SPECIFIC,
  BWMSERVICENAME="video_svc",
  UPBWMCTRLNAME1="group_shaping",
  DNBWMCTRLNAME1="group_shaping",
  BWMRULEPRI=2;
```

---

## 附录E: 版本演进与首发版本分布

### E.1 版本分布统计

| 首发版本 | UDG特性数 | UNC特性数 | 合计 | 阶段说明 |
|----------|----------|----------|------|----------|
| 20.0.0 / 20.1.0 | 4 | 1 | 5 | 基础平台+核心控制首发 |
| 20.2.0 ~ 20.3.0 | 3 | 0 | 3 | 核心扩展（异常检测、Shaping、ADC） |
| 20.5.0 | 1 | 5 | 6 | UNC侧大规模上线，CU分离成型 |
| 20.7.0 | 2 | 2 | 4 | 智能Shaping + 小区负荷 |
| 20.8.2 ~ 20.9.0 | 3 | 0 | 3 | 视频优化、码率差异化、BWM增强 |
| 20.12.2 | 1 | 0 | 1 | SA特征库管控 |
| 23.1.1 | 1 | 0 | 1 | 智能Shaping v01补充 |
| **合计** | **16** | **8** | **24** | |

### E.2 UNC侧上线节奏分析

UNC侧特性集中在20.5.0发布（5个），包括ADC、会话FUP、QoS保证、接入点策略、BWM。这说明：
- 20.5.0是CU分离架构的关键里程碑版本
- BWM、FUP、QoS保证、ADC四条核心链路在20.5.0同步上线
- 接入点策略（WiFi位置感知）作为补充特性也在同期发布

### E.3 版本依赖矩阵

| 特性 | 依赖特性的最低版本要求 | 版本依赖说明 |
|------|---------------------|-------------|
| GWFD-110311 BWM v02 | SA-Basic 20.0.0+, PCC 20.0.0+ | BWM v02需SA和PCC基础 |
| GWFD-110312 业务FUP | SA-Basic 20.0.0+, BWM 20.0.0+ | 业务FUP依赖SA识别+BWM规则匹配 |
| GWFD-110313 智能Shaping | BWM 20.9.0+, Shaping 20.1.0+ | 智能Shaping依赖BWM+Shaping双基础 |
| GWFD-020358 QoS保证 | SA-Basic 20.0.0+, PCC 20.0.0+ | QoS保证依赖SA识别触发 |
| GWFD-110302 视频解耦 | QoS保证 20.2.0+, UNC 20.2.0+ | 视频解耦是QoS保证的增强版 |
| GWFD-110332 小区负荷 | PCC 20.0.0+, UNC 20.7.0+ | 小区负荷需UNC侧转发支持 |
| WSFD-109104 会话FUP | PCC(UNC) 20.0.0+ | UNC PCC是会话FUP的前置 |
| WSFD-211009 业务FUP | PCC(UNC) 20.0.0+, BWM(UNC) 20.5.0+ | 业务FUP(UNC)依赖BWM(UNC) |
| WSFD-109107 QoS保证 | PCC(UNC) 20.0.0+ | UNC PCC是QoS保证的前置 |

---

## 附录F: 令牌桶与三色标记体系深度分析

### F.1 令牌桶算法在带宽控制中的应用

带宽控制场景中，令牌桶（Token Bucket）是所有限速和整形功能的底层算法。不同特性使用令牌桶的方式有显著差异：

| 特性 | 令牌桶用途 | 参数 | 超额处理 |
|------|-----------|------|----------|
| BWM CAR (GWFD-110311) | 流量监管 | CIR/CBS/PIR/PBS | 直接丢弃或重标记 |
| Shaping (GWFD-020354) | 流量整形 | RATE/QUEDEPTH | 缓存到GTS队列 |
| 智能Shaping (GWFD-110313) | 智能整形 | RATE/QUEDEPTH/SRVLEVELSPEC | 按优先级缓存+公平丢包 |
| PCC QER执行 | QoS执行 | MBR-UL/DL (映射为CIR/PIR) | 由Gate状态决定（丢弃/放行） |
| GBR保证 | 资源预留 | GBR-UL/DL | 专用资源调度 |

### F.2 三色标记（GREEN/YELLOW/RED）

BWM的CAR模式使用RFC 2697/RFC 2698定义的三色标记体系：

| 颜色 | 条件 | 处理策略 | 可配置动作 |
|------|------|----------|-----------|
| **GREEN** | 报文消耗令牌后未超CIR | 正常转发 | PASS / REMARK / DISCARD |
| **YELLOW** | 报文超CIR但未超PIR | 有限转发 | PASS / REMARK / DISCARD |
| **RED** | 报文超PIR | 超额丢弃 | PASS / REMARK / DISCARD |

**BWM Controller三色处理配置**:
```
ADD BWMCONTROLLER:BWMCNAME="example",
  CTRLTYPE=CAR,
  CIR=2048,CBS=256000,         // GREEN阈值
  PIR=4096,PBS=512000,         // YELLOW阈值
  GREENACT=PASS,               // GREEN报文动作
  YELLOWACT=REMARK,            // YELLOW报文重标记
  REDACT=DISCARD,              // RED报文丢弃
  COLORISAWARE=ENABLE,         // 颜色感知（优先保证GREEN）
  PRIORITYISAWARE=ENABLE;      // 优先级感知
```

### F.3 Shaping与CAR的关键差异

| 维度 | CAR（Policing） | Shaping |
|------|----------------|---------|
| **超额报文** | 直接丢弃或重标记 | 缓存到GTS队列延迟转发 |
| **延迟影响** | 不增加延迟 | 增加延迟和抖动 |
| **队列** | 无队列 | GTS队列（QUEDEPTH配置深度） |
| **TCP友好性** | 差（突发丢弃导致TCP窗口缩小） | 好（平滑输出减少TCP重传） |
| **适用业务** | P2P等低价值业务 | 视频等对抖动敏感的业务 |
| **层级支持** | 用户级/组级/全局级 | **仅用户级** |
| **CTRLTYPE** | CAR | SHAPING（固定） |

### F.4 智能Shaping的自动调度算法

智能Shaping（GWFD-110313）在普通Shaping基础上增加了自动调度能力：

**MANUAL模式**: 与普通Shaping相同，各ServiceLevel按配置的SHAPRATE比例分配带宽。

**AUTO模式**: 根据丢包率差值自动调整带宽分配：
1. 监控各ServiceLevel队列的丢包率
2. 计算丢包率差值与目标值(PKTLOSTRATEDTL)的偏差
3. 动态调整各ServiceLevel的保障带宽
4. 确保高优先级业务的丢包率显著低于低优先级

**ASSUREMODE取值**:
- `EXPFIRST`: 体验优先，优先保障高优先级业务的丢包率达标
- `RATEFIRST`: 速率优先，优先保障总吞吐量

---

## 附录G: 无线资源优化类特性对比矩阵

带宽控制场景中有5个无线资源优化类特性，它们的共同特点是"不在UPF执行限速，而是通过标记或上报影响无线侧行为"：

| 特性 | 标记/上报内容 | 影响目标 | 机制 | 适用场景 |
|------|-------------|----------|------|----------|
| **GWFD-020359 IM管控** | DSCP值 (12=QQ, 14=MSN, 18=Fetion) | BSC/RNC无线调度 | SA识别IM业务 → 映射DSCP → 无线侧调整调度 | 2/3G IM业务保活心跳优化 |
| **GWFD-110301 码率差异化** | OSTYPE (Android/iOS/Windows) | BWM策略差异化 | SA识别终端OS → 匹配不同BWM规则 | 视频OTT不同编码格式适配 |
| **GWFD-110302 视频解耦** | DECOUPLINGSW=ENABLE | 专有承载方向性 | 只为下行建专载，上行走缺省 | 直播/点播下行高带宽场景 |
| **GWFD-110331 FPI标记** | FPI值 (0~255) / DSCP / GTP-U扩展头 | RAN调度队列 | SA识别 → 匹配FPI规则 → 标记报文 → 基站按队列调度 | 全业务类型无线调度优化 |
| **GWFD-110332 小区负荷** | Cell Load Level (0~3) | PCRF策略决策 | RAN上报负荷 → UDG转发 → UNC上报PCRF → 策略调整 | 小区拥塞时动态限速 |

**共性分析**:
1. 全部依赖SA-Basic（GWFD-110101）的业务识别能力
2. 全部不直接执行用户面限速/整形动作
3. GWFD-020359和GWFD-110331通过修改DSCP字段影响无线侧
4. GWFD-110332通过GTP-U扩展头上报小区负荷
5. GWFD-110301通过BWM框架增加OSTYPE维度实现差异化
6. GWFD-110302是唯一涉及专有承载方向性控制的特性

**FPI值与队列映射**（GWFD-110331专有）:

| FPI值范围 | 映射队列 | 默认调度权重 | 业务建议 |
|-----------|---------|-------------|----------|
| 0~7, 55~255 | 队列0 | 10 | 缺省/低优先级业务 |
| 8~15 | 队列1 | **1**（极低） | 需特别注意：权重仅为其他队列的1/10 |
| 16~23 | 队列2 | 10 | - |
| 24~31 | 队列3 | 10 | - |
| 32~39 | 队列4 | 10 | - |
| 40~47 | 队列5 | 10 | - |
| 48~55 | 队列6 | 10 | 高优先级业务 |

> **规划风险**: FPI值8~15映射的队列1调度权重仅为1，在空口资源紧张时几乎得不到调度机会。配置时需特别注意避免将高价值业务映射到此范围。

**小区负荷等级与策略响应**（GWFD-110332专有）:

| 负荷等级 | 数值 | 含义 | 典型PCRF策略响应 |
|----------|------|------|-----------------|
| Invalid | 0 | 无效 | 不触发策略 |
| Normal | 1 | 正常 | 放宽限速，恢复全速 |
| Congestion | 2 | 拥塞 | 对低优先级用户限速，保障高价值用户 |
| Overload | 3 | 过载 | 最严格限速，仅保障最高优先级业务 |

---

## 附录H: 特性间隐藏关系总结

以下关系并非特性文档中显式声明的"依赖"或"交互"，而是通过配置对象复用、接口共享和数据流分析推断出的隐藏关系：

### H.1 通过配置对象推断的关系

| 配置对象 | 被哪些特性共用 | 推断的隐藏关系 |
|----------|-------------|--------------|
| RULE (ADD RULE) | 14+个特性 | 所有使用RULE的特性在配置时RULENAME不能冲突（同一产品内） |
| URR (ADD URR) | 会话FUP + 业务FUP + QoS保证 | 同一会话内URR ID不能重复分配 |
| QOSPROP | QoS保证 + 视频解耦 | 视频解耦复用QoS保证的QOSPROP对象，增加DECOUPLINGSW参数 |
| BWMRULE | BWM + Shaping + 智能Shaping | 三者共享BWMRULE结构，通过CTRLTYPE区分 |
| BWMUSERGROUP | BWM + 智能Shaping | 智能Shaping的组级规则复用BWM的USERGROUP对象 |

### H.2 通过接口推断的关系

| 接口 | 共用特性 | 推断的隐藏关系 |
|------|---------|--------------|
| Gx (Diameter) | 所有UNC特性 | Gx连接故障（PCRF不可达）同时影响所有Gx特性 |
| N7 (HTTP/2) | 所有UNC 5G特性 | N7连接故障同时影响所有N7特性 |
| N4 (PFCP) | 所有UDG+UNC特性 | N4连接故障导致所有控制面→用户面规则传递中断 |

### H.3 通过SA数据流推断的关系

| SA输出 | 使用方 | 推断的隐藏关系 |
|--------|--------|--------------|
| SVC (业务大类) | BWM, FUP, Shaping, ADC, FPI标记, IM管控 | SA特征库版本升级可能同时影响所有依赖SVC的特性 |
| APP (具体应用) | ADC, 业务FUP, 码率差异化 | 新APP的识别依赖特征库更新 |
| OSTYPE (终端系统) | 码率差异化 | 终端系统识别准确率影响码率策略效果 |
| URL | L7过滤, ADC | URL解析依赖SA的L7解析引擎 |

### H.4 配置冲突风险矩阵

| 冲突场景 | 涉及特性 | 冲突原因 | 解决方案 |
|----------|---------|----------|----------|
| 同一RULENAME用于不同POLICYTYPE | BWM vs PCC vs QOS vs ADC | PCC类型的RULENAME不能与QOS类型的RULENAME同名 | 规划命名规范，加前缀区分 |
| 会话FUP与业务FUP的URR ID冲突 | 会话FUP vs 业务FUP | 同一会话内URR ID必须唯一 | 分配不同的URR ID段（如会话FUP用1-99，业务FUP用100+） |
| BWM CAR与Shaping同时配置 | BWM vs Shaping | 同一业务流不能同时做CAR和Shaping | 按业务类型区分：低价值用CAR，高价值用Shaping |
| 异常检测阻塞影响正常业务 | 异常检测 vs QoS保证 | 异常检测可能误阻QoS保证触发的专载业务流 | VoLTE等特殊APN不应开启简单异常检测方案 |
| 小区负荷触发策略覆盖BWM静态策略 | 小区负荷 vs BWM | PCRF下发的动态策略可能覆盖本地BWM规则 | 规划策略优先级，明确动态/静态策略边界 |

---

> **文档生成说明**: 本文档基于24个带宽控制场景特性知识文档横向分析产出。所有特性ID、License编号、命令名、配置对象名均严格引用自各特性的知识文档。跨特性关系分析基于配置对象复用、接口共享和依赖链路推断。文档不包含任何未经源文档支持的臆测内容。
