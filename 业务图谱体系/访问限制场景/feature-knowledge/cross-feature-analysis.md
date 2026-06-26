# 访问限制场景 - 跨特性横向分析报告

> **分析范围**: 11个访问限制场景独有特性（10 UDG + 1 UNC） + 3个复用特性（SA-Basic / PCC基本功能 UDG / PCC基本功能 UNC / ADC UNC）共构成 14特性视角
> **分析维度**: 分类总览 / 共性分析 / 配置差异 / 依赖关系 / 关键发现 / 双轨动作机制
> **文档目的**: 通过横向对比揭示特性间隐藏关系、配置对象复用模式、双轨动作机制（轨道A PCC体系 vs 轨道B URL过滤体系），作为三层图谱第2-4层（特性/任务/命令/对象）实例化的主数据源
> **质量标杆**: 参照 `带宽控制场景/feature-knowledge/cross-feature-analysis.md`（1119行）的表格密度和附录完整性

---

## 目录

1. [特性分类总览](#1-特性分类总览)
2. [共性分析](#2-共性分析)
3. [配置差异分析](#3-配置差异分析)
4. [依赖关系分析](#4-依赖关系分析)
5. [关键发现](#5-关键发现)
6. [附录A: 14特性索引表](#附录a-14特性索引表)
7. [附录B: MML命令交叉参考](#附录b-mml命令交叉参考)
8. [附录C: 配置对象复用矩阵](#附录c-配置对象复用矩阵)
9. [附录D: 典型端到端配置流程](#附录d-典型端到端配置流程)
10. [附录E: 双轨动作机制深度对比](#附录e-双轨动作机制深度对比)
11. [附录F: POLICYTYPE取值全景表](#附录f-policytype取值全景表)
12. [附录G: SA协议解析依赖矩阵](#附录g-sa协议解析依赖矩阵)

---

## 1. 特性分类总览

### 1.1 按功能层次分类

访问限制场景的14特性（11独有 + 3复用）按功能层次可分为 7 组。**产品定义上所有有正式特性编号的都是 Feature（无 SubFeature 概念）**。

| 功能层次 | UDG侧特性 | UNC侧特性 | 核心能力 | feature_group |
|----------|-----------|-----------|----------|---------------|
| **业务感知层（复用）** | GWFD-110101 SA-Basic | - | L3/L4/L7业务识别基础，协议解析引擎 | `SA_BASE` |
| **PCC骨架层（复用）** | GWFD-020351 PCC基本功能 | WSFD-109101 PCC基本功能 | PCC规则体系（RULE/USERPROFILE/PCCPOLICYGRP）、Gx/N7/N4信令承载 | `PCC_FRAME` |
| **ADC应用检测层** | GWFD-020357 增强的ADC基本功能 | WSFD-109102 ADC基本功能（复用） | L7应用检测上报、APPLICATION_START/STOP事件、兜底阻塞 | `ADC` |
| **头增强族** | GWFD-110261 HTTP头增强、GWFD-110262 RTSP头增强、GWFD-110263 HTTPS头增强 | - | 报文头插入MSISDN/IMSI/IMEI等用户信息字段 | `HEADEN` |
| **防欺诈层** | GWFD-110401 HTTP头防欺诈 | - | 头增强前置检测，纠正/清理欺诈字段 | `ANTIFRAUD` |
| **重定向族** | GWFD-110281 用户Portal、GWFD-110282 WebProxy、GWFD-110283 DNS纠错、GWFD-110284 HTTP智能重定向 | - | 将用户业务流引导到指定服务器/页面 | `REDIRECT` |
| **URL内容过滤层** | GWFD-110471 URL过滤基本功能 | - | 基于ICAP Server的URL分类数据库，执行BLOCK/PERMIT/REDIRECT | `URL_FILTER` |
| **接入控制触发层** | - | WSFD-211001 基于初始接入位置的策略控制 | ULI位置匹配，触发带宽/访问限制策略下发 | `ACCESS_CTRL_TRIGGER` |

### 1.2 按产品归属分类

| 产品 | 独有特性数 | 复用特性数 | 特性ID列表（独有） |
|------|-----------|-----------|-------------------|
| **UDG（用户面）** | 10 | 3（SA-Basic / PCC / ADC） | GWFD-020357, GWFD-110261, GWFD-110262, GWFD-110263, GWFD-110281, GWFD-110282, GWFD-110283, GWFD-110284, GWFD-110401, GWFD-110471 |
| **UNC（控制面）** | 1 | 2（PCC / ADC） | WSFD-211001 |

> **观察**：访问限制场景是**UDG重场景**（10独有 vs UNC 1独有）。UNC侧的访问限制更多体现为"接入控制策略下发"（WSFD-211001位置触发），实际执行动作都在UDG侧。

### 1.3 按访问限制动作类型分类（三大动作 + PERMIT）

访问限制场景的核心业务语义是 **DISCARD（阻塞）/ HEADEN（头增强）/ REDIRECT（重定向）** 三大动作，加上 URL 过滤特有的 **PERMIT（放行）**。

| 动作类型 | 直接产生此动作的特性 | 间接贡献的特性 | 实现机制 |
|---------|---------------------|---------------|----------|
| **DISCARD（阻塞）** | GWFD-020357 ADC（兜底阻塞）、GWFD-110471 URL过滤（CFTEMPLATE.ACTION=BLOCK） | GWFD-110281 Portal（IPFarm全DOWN时DEFAULTACT=BLOCK）、GWFD-110282 WebProxy（服务器DOWN丢包） | 轨道A隐式阻塞（规则匹配不上丢弃）；轨道B显式BLOCK |
| **HEADEN（头增强）** | GWFD-110261/110262/110263 头增强族 | GWFD-110401 头防欺诈（保障头增强正确性）、GWFD-110284 HTTP智能重定向（REDIRAPPENDINFO携带MSISDN/IMSI） | 轨道A；POLICYTYPE=HEADEN 引用 HEADEN 对象 |
| **REDIRECT（重定向）** | GWFD-110281 Portal、GWFD-110282 WebProxy、GWFD-110283 DNS纠错、GWFD-110284 HTTP智能重定向、GWFD-110471 URL过滤（CFTEMPLATE.ACTION=REDIRECT） | - | 4种协议层实现（DNS/L3-IPNAT/L7-HTTP响应/L7-Portal） + URL过滤轨道B |
| **PERMIT（放行）** | GWFD-110471 URL过滤（CFTEMPLATE.ACTION=PERMIT） | - | **仅URL过滤显式支持PERMIT**（轨道A的特性主要是"不做动作"） |

### 1.4 按动作轨道路径分类（双轨机制——本场景核心架构）

| 轨道 | 驱动核心 | 动作指定方式 | 涉及特性 |
|------|---------|-------------|----------|
| **轨道A：PCC体系** | RULE.POLICYTYPE | 隐式（POLICYTYPE决定动作） | GWFD-020357 ADC、GWFD-110261/262/263 头增强、GWFD-110401 头防欺诈、GWFD-110281 Portal、GWFD-110282 WebProxy、GWFD-110283 DNS纠错、GWFD-110284 HTTP智能重定向 |
| **轨道B：URL过滤体系** | CFTEMPLATE.ACTION / CONTCATEGBIND.ACTION | 显式（BLOCK/PERMIT/REDIRECT） | GWFD-110471 URL过滤 |

> **详细对比见 §5.1 和 附录E**——这是本场景区别于计费/带宽场景的最关键架构事实。

### 1.5 滚动发布时间线

| 发布批次 | 首发版本 | 特性 | 分析要点 |
|---------|----------|------|----------|
| **第1批（基础平台，复用）** | UDG 20.0.0 / UNC 20.0.0 | GWFD-110101 SA-Basic、GWFD-020351 PCC、WSFD-109101 PCC | 全场景基础设施，访问限制的所有L7动作都依赖SA解析和PCC规则载体 |
| **第2批（核心访问限制首发）** | UDG 20.0.0 | GWFD-110261 HTTP头增强、GWFD-110262 RTSP头增强、GWFD-110263 HTTPS头增强、GWFD-110281 用户Portal、GWFD-110282 WebProxy、GWFD-110284 HTTP智能重定向、GWFD-110401 HTTP头防欺诈 | 访问限制的"主干特性"集中在 UDG 20.0.0 首发，说明本场景是 UDG 初始能力之一 |
| **第3批（ADC+DNS纠错）** | UDG 20.1.0 | GWFD-020357 增强的ADC基本功能 | ADC晚于头增强族1个版本，作为L7动态控制的补强 |
| **第4批（UNC侧位置触发）** | UNC 20.3.0 | WSFD-211001 基于初始接入位置 v01 | UNC侧首次引入位置触发，4G（PGW-C）先支持 |
| **第5批（DNS纠错补强）** | UDG 20.0.0 | GWFD-110283 DNS纠错 | 与重定向族同期 |
| **第6批（SMF支持）** | UNC 20.7.0 | WSFD-211001 v02 | 5G SMF 加入位置触发支持 |
| **第7批（头增强多参数）** | UDG 20.10.0 | GWFD-110261/110262 v02 | HTTP/RTSP头增强支持多参数拼接 |
| **第8批（URL过滤）** | UDG 20.10.2 | GWFD-110471 URL过滤基本功能 | **最晚发布的独有特性**，引入ICAP Server和轨道B |

**时间线规律**：
- 头增强族 + 重定向族 + 防欺诈 + Portal/WebProxy 都是 **UDG 20.0.0 首发**——本场景的核心能力在UDG初版就成型
- ADC 在 20.1.0 补强，为 L7 动态控制铺路
- UNC 侧的位置触发（WSFD-211001）在 20.3.0 加入，5G支持在20.7.0
- **URL过滤最晚（20.10.2）**，引入了独立的ICAP架构和轨道B体系，是访问限制场景的能力扩展里程碑

---

## 2. 共性分析

### 2.1 共享的SA业务感知基础（SA识别前置）

**核心发现**: 访问限制场景中**所有L7动作特性都直接依赖SA-Basic**（GWFD-110101）的协议解析能力，SA是整个场景的数据基础。

以下特性**直接依赖** SA-Basic（来自各特性 §1.5 前置条件）：

| 特性 | SA依赖说明 |
|------|-----------|
| GWFD-020357 ADC | 基于SA执行L7业务检测 |
| GWFD-110261 HTTP头增强 | 需要对HTTP报文进行解析以执行头增强 |
| GWFD-110262 RTSP头增强 | 需要对RTSP报文进行解析 |
| GWFD-110263 HTTPS头增强 | 需要对HTTPS报文进行解析 |
| GWFD-110281 用户Portal | SA的基本功能 + SA-Web Browsing + SA-Mobile |
| GWFD-110282 WebProxy | SA解析获得Web Proxy动作和重定向地址 |
| GWFD-110283 DNS纠错 | SA解析获得URL + SA-Network Administration解析DNS |
| GWFD-110284 HTTP智能重定向 | SA解析和规则匹配（SA-Web Browsing） |
| GWFD-110401 HTTP头防欺诈 | 识别和解析HTTP报文（SA-Web Browsing） |
| GWFD-110471 URL过滤 | SA解析获得URL（SA-Web Browsing + SA-Mobile + HTTP2.0 Host识别） |

**SA数据层次**（来自 Batch-01）:
```
SA特征库（由LOD SIGNATUREDB加载）
    │
    ▼
SA-Basic 引擎（GWFD-110101）
    ├── L3/L4 解析（IP/端口/协议） → FILTER 匹配
    ├── 协议识别（知名端口 + 签名匹配） → PROTBINDFLOWF 绑定
    └── L7 解析（URL / Method / Response Code / SNI） → L7FILTER / EXTENDEDFILTER 匹配
    │
    ▼
业务标识输出（SVC/APP、URL、Method、UserAgent、Content-Type）
    │
    ▼
供 ADC / 头增强族 / 重定向族 / URL过滤 / 防欺诈 等特性使用
```

### 2.2 共享的PCC规则框架（PCC骨架）

**核心发现**: 除URL过滤（轨道B）外，**所有轨道A特性都共享PCC规则体系**。PCC是访问限制动作的统一承载框架。

**PCC框架的共用配置对象**（来自各特性配置章节 + Batch-02）:

| 配置对象 | UDG命令 | UNC命令 | 跨产品一致性要求 | 访问限制场景用途 |
|---------|---------|---------|-----------------|-----------------|
| RULE（规则） | ADD RULE | ADD RULE | 动态PCC场景RULENAME全网一致 | **核心载体**，POLICYTYPE差异化 |
| USERPROFILE（用户模板） | ADD USERPROFILE | ADD USERPROFILE | 预定义规则组名称一致 | 规则绑定 + Portal captive配置 |
| RULEBINDING（规则绑定） | ADD RULEBINDING | ADD RULEBINDING | - | UserProfile ↔ Rule 绑定 |
| PCCPOLICYGRP（策略组） | ADD PCCPOLICYGRP | ADD PCCPOLICYGRP | - | PCC策略组（含ADCMUTEFLAG） |
| USRPROFGROUP（用户模板组） | ADD USRPROFGROUP | ADD USRPROFGROUP | - | UNC侧位置策略绑定 |
| UPBINDUPG（模板绑定） | ADD UPBINDUPG | ADD/MOD UPBINDUPG | - | 含LOCGROUPNAME（位置组） |
| APNUSRPROFG（APN绑定） | ADD APNUSRPROFG | ADD APNUSRPROFG | APN/DNN名称一致 | APN级策略生效 |
| FLOWFILTER（流过滤器） | ADD FLOWFILTER | ADD FLOWFILTER | ADC场景三网元一致 | L3/L4匹配入口 |
| FILTER（三四层过滤器） | ADD FILTER | - | UDG独有 | 五元组匹配 |
| L7FILTER（七层过滤器） | ADD L7FILTER | - | UDG独有 | URL/Method匹配 |
| FLTBINDFLOWF（过滤器绑定） | ADD FLTBINDFLOWF | - | UDG独有 | FILTER → FLOWFILTER |
| PROTBINDFLOWF（协议绑定） | ADD PROTBINDFLOWF | - | UDG独有 | 协议 + L7FILTER |
| EXTENDEDFILTER（扩展过滤器） | ADD EXTENDEDFILTER | - | UDG独有 | URL/UserAgent/ContentType多维匹配 |
| URR（使用量上报规则） | ADD URR | ADD URR | URRID一致 | 计费属性绑定（URL过滤/Portal/WebProxy/ADC） |
| URRGROUP | ADD URRGROUP | ADD URRGROUP | - | URR组 |
| ADCPARA | ADD ADCPARA | ADD ADCPARA | ADC参数三网元一致 | ADC独有：流信息上报 + 迟滞定时器 |

### 2.3 共享的三四层过滤链路

**核心发现**: 几乎所有L7动作特性都共用相同的三四层过滤链路作为规则匹配入口。

**标准过滤链**（来自各特性 §配置流程）:
```
ADD FILTER (定义三四层过滤条件)
    │
    ▼
ADD FLOWFILTER (定义流过滤器)
    │
    ├── ADD FLTBINDFLOWF (绑定Filter到FlowFilter)
    │
    ▼
[可选] ADD L7FILTER → ADD PROTBINDFLOWF (七层扩展)
    │
    ▼
SET REFRESHSRV:REFRESHTYPE=ALL (策略刷新生效，约60秒)
    │
    ▼
ADD RULE:FLOWFILTERNAME=... (规则引用)
```

使用此过滤链的特性：**全部11个独有特性**都使用 FILTER + FLOWFILTER + FLTBINDFLOWF 链。

### 2.4 共享的License控制机制

**核心发现**: 所有特性都有独立的License控制项，使用统一的 `SET LICENSESWITCH` 命令开启。License前缀有规律。

| 特性组 | UDG License前缀 | UNC License前缀 | 典型样例 |
|--------|----------------|----------------|---------|
| 头增强族 | `LKV3G5` + `HTHE/HTSE/RTHE` + `01` | - | 82209777 LKV3G5HTHE01（HTTP头增强） |
| 重定向族 | `LKV3G5` + `SHPR/DNSO/CPPT/WEBP` + `01` | - | 82209783 LKV3G5SHPR01（HTTP智能重定向） |
| 防欺诈 | `LKV3G5` + `HHAS` + `01` | - | 82209786 LKV3G5HHAS01 |
| ADC | `LKV3G5` + `ADCF` + `01` | `LKV2` + `ADCF` + `01` | 82200AFK LKV3G5ADCF01 |
| URL过滤 | `LKV3G5` + `UFBF` + `01` | - | 82200FCP LKV3G5UFBF01 |
| 位置触发 | - | `LKV2` + `PCIAL` + `01` | 82200BNQ LKV2PCIAL01 |

**规律**: UDG License前缀统一为 `LKV3G5`；UNC License前缀为 `LKV2`（独立特性）或 `LKV3W9`（复用PCC家族）。

### 2.5 共享的SET REFRESHSRV时序约束

**核心发现**: 多个特性都要求配置变更后执行 `SET REFRESHSRV` 才能生效，且执行后约 60 秒（PROTBINDFLOWF定时器）策略才完全下发。

涉及SET REFRESHSRV的特性：
- GWFD-020357 ADC（FILTER/L7FILTER变更后）
- GWFD-110261/262/263 头增强族（过滤条件变更后）
- GWFD-110281 用户Portal（L7FILTER变更后）
- GWFD-110282 WebProxy（FILTER变更后）
- GWFD-110283 DNS纠错（FILTER变更后）
- GWFD-110284 HTTP智能重定向（FILTER变更后）
- GWFD-110401 HTTP头防欺诈（FILTER/L7FILTER变更后）
- GWFD-110471 URL过滤（FILTER变更后）

**REFRESHTYPE 取值**:
- `ALL`: 全量刷新
- `USERPROFILE`: 用户模板级刷新（粒度较细）

### 2.6 共享的三网元一致性要求

**核心发现**: 凡涉及动态PCC（PCRF/PCF下发预定义规则）的特性，都需要多网元规则名一致性。

| 特性 | 一致性要求 | 涉及网元 |
|------|-----------|----------|
| ADC | RULENAME / appid / FlowFilterName 一致 | UDG + UNC + PCRF/PCF |
| 头增强族 | 预定义规则名一致（PCRF/PCF下发场景） | UDG + UNC + PCRF/PCF |
| 重定向族 | 预定义规则名一致 | UDG + UNC + PCRF/PCF |
| URL过滤 | URL过滤套餐名、Category ID一致 | UDG + ICAP Server + PCRF/PCF |
| 位置触发 | 位置信息（CGI/ECGI/NCGI）取值一致 | UNC + RAN + PCRF/PCF |

### 2.7 共享的接口体系

| 接口 | 协议 | 连接网元 | 涉及特性数 | 核心功能 |
|------|------|---------|-----------|---------|
| **Gx** | Diameter (3GPP 29.212) | PCRF ↔ PGW-C/GGSN | 所有UNC特性 | 2/3/4G策略下发，Event Triggers |
| **N7** | HTTP/2 JSON (3GPP 29.512) | PCF ↔ SMF | 所有UNC 5G特性 | 5G SM策略下发，PCR Triggers |
| **N4** | PFCP (3GPP 29.244) | SMF/PGW-C ↔ UPF/PGW-U | 所有特性 | 控制面→用户面规则传递 |
| **ICAP** | RFC 3507 | UDG ↔ ICAP Server | 仅 GWFD-110471 URL过滤 | URL上送 + 动作返回（轨道B独立） |
| **GTP-U** | 3GPP 29.281 | RAN ↔ UPF | 仅位置触发辅助 | 用户位置信息上报 |

### 2.8 共享的IP Farm服务器集群机制（Portal + WebProxy）

**核心发现**: GWFD-110281 用户Portal 和 GWFD-110282 WebProxy 共享 IP Farm 机制作为重定向服务器集群方案（来自 Batch-06 KP-2）。

| 维度 | 机制 |
|------|------|
| **IP Farm 定义** | 若干个重定向目标服务器的集合 |
| **负荷分担方式（LBMETHOD）** | ROUND_ROBIN（轮询）/ LEAST_RECENTLY_USED（最久未用）/ LEAST_LOAD（最小负荷，默认） |
| **心跳检测** | UDG 定时发送 ICMP 报文，UP↔DOWN 状态切换由 HEALTHSUCCLIMIT/HEALTHFAILLIMIT 控制 |
| **心跳接口** | 每个 IP Farm 绑定一个 LOGICINF，不同 IP Farm 必须用不同接口 |
| **全部 DOWN 处理** | Portal 默认 DEFAULTACT=BLOCK；WebProxy 不做重定向（业务按原路径走） |
| **告警** | ALM-81034 IPFarm无可用server / ALM-81035 IPFarm服务器无响应 |
| **规格** | 整机 64 个 IP Farm，每个 IP Farm 512 个 IP |

---

## 3. 配置差异分析

### 3.1 RULE.POLICYTYPE 取值差异（核心差异维度）

**核心发现**: `RULE.POLICYTYPE` 是访问限制场景中**区分动作类型的最关键参数**，每个POLICYTYPE对应不同的POLICYNAME指向对象。

| POLICYTYPE | 标识的动作类型 | POLICYNAME指向 | 涉及特性 | 轨道 |
|-----------|---------------|---------------|----------|------|
| **ADC** | ADC应用检测（独立规则） | 直接在RULE上（FLOWFILTER） | GWFD-020357 | A |
| **PCC** | 标准PCC规则（含ADC复用、URL过滤触发） | PCCPOLICYGRP | GWFD-020357(复用)、GWFD-110471(URL过滤触发) | A |
| **HEADEN** | 头增强（族内统一） | HEADEN 对象名 | GWFD-110261/262/263、GWFD-110401 | A |
| **SMARTREDIRECT** | HTTP智能重定向 / DNS纠错（共用！） | SMARTHTTPREDIR / DNSOVERWRITING | GWFD-110284、GWFD-110283 | A |
| **WEBPROXY** | Web Proxy（L3 IP NAT） | IPFARM 对象名 | GWFD-110282 | A |
| **（Portal）** | 用户Portal（captive配置在USERPROFILE） | PCCPOLICYGRP | GWFD-110281 | A |
| **（URL过滤）** | URL过滤（仍需PCC RULE触发，但动作不走PCC） | PCCPOLICYGRP（仅匹配触发） | GWFD-110471 | A→B混合 |

**关键约束**（来自各特性文档）：
- 同一RULENAME值在不同POLICYTYPE间**不能重复**（PCC类型与QOS类型的RULENAME不能同名）
- HTTP智能重定向和DNS纠错**共用 POLICYTYPE=SMARTREDIRECT**，区分点在 POLICYNAME 指向的对象类型（SMARTHTTPREDIR vs DNSOVERWRITING）
- URL过滤的 RULE 用 POLICYTYPE=PCC，但实际BLOCK/PERMIT/REDIRECT动作不走 PCCPOLICYGRP，而走 CFTEMPLATE/CONTCATEGBIND（轨道B）

### 3.2 重定向族四种协议层实现差异

**核心发现**: 重定向族（4特性）在4个不同协议层实现"把用户引导到指定服务器"的同一目标（来自 Batch-06 发现-1）。

| 维度 | HTTP智能重定向（110284） | DNS纠错（110283） | 用户Portal（110281） | WebProxy（110282） |
|------|------------------------|------------------|---------------------|-------------------|
| **协议层** | L7 HTTP 响应 | DNS 解析层 | L7 HTTP 请求 | L3 IP NAT |
| **改写对象** | HTTP 响应报文 | DNS 响应报文 | HTTP 响应（301/302/303） | IP 报文目的IP |
| **触发时机** | HTTP 错误码 / 多条件匹配 | DNS 查询失败 | 用户 HTTP 请求（captive周期） | TCP SYN 匹配规则 |
| **介入时机** | 较晚（HTTP响应时） | **最早**（DNS解析时，未建TCP） | 用户首次HTTP请求 | 建立TCP时 |
| **用户感知** | 跳转到新页面 | 跳转到新页面 | 跳转到 Portal | **透明（无感知）** |
| **目标服务器** | 第三方服务器 | 第三方 Platform | Portal Server | Proxy Server |
| **典型用途** | URL纠错、内容过滤 | 错误域名引导 | 业务订购、广告推送 | 网络加速、病毒防护 |
| **POLICYTYPE** | SMARTREDIRECT | SMARTREDIRECT | PCC（USERPROFILE captive） | WEBPROXY |
| **IP Farm** | 不用 | 不用 | 用 | 用 |
| **EXTENDEDFILTER** | 用（多维度） | 用（URL） | 不用 | 不用 |
| **HTTPS 支持** | **不支持** | N/A（DNS独立） | **不支持** | **支持**（IP NAT不依赖L7） |
| **HTTP2.0 支持** | **不支持** | N/A | **不支持** | **支持** |

### 3.3 头增强族三种协议差异

**核心发现**: 头增强族（3特性）共用 ADD HEADEN 命令，差异仅在"SA依赖"和"字段插入位置"两个维度（来自 Batch-05 KP-4）。

| 差异点 | HTTP 头增强（110261） | HTTPS 头增强（110263） | RTSP 头增强（110262） |
|--------|---------------------|----------------------|---------------------|
| **支持协议** | HTTP1.x（不支持HTTP2.0） | TLS 1.0/1.1/1.2/1.3 | RTSP（不支持RTSP over HTTP） |
| **字段插入位置** | HTTP 扩展字段 | **SSL 报文头 Extension 字段，TLV 格式** | RTSP 扩展字段 |
| **触发条件** | 特定IP / 特定URL / HTTP协议 | 特定IP / 特定**SNI** / HTTPS协议 | 特定IP / 特定URL / RTSP协议 |
| **业务** | Web 浏览 | Web 浏览 | 视频流媒体 |
| **业务服务器** | Web Server | Web Server | Streaming Server |
| **依赖 SA** | SA-Basic + SA-Web Browsing + SA-Mobile（MMS场景） | SA-Basic + SA-Web Browsing + SA-Mobile + **HTTP2.0 Host识别** | SA-Basic + **SA-Streaming** |
| **加密算法** | MD5/RC4/AES-128/256/RSA-1024/2048/SHA-256 | MD5/RC4/AES-128/256/SHA-256（无RSA） | 同 HTTP |
| **编码能力** | base64 + ASCII | base64 + ASCII + **十六进制** | base64 + ASCII |
| **头防欺诈支持** | **支持** | **支持** | **不支持** |
| **License** | 82209777 HTHE01 | 82209779 HTSE01 | 82209778 RTHE01 |
| **多参数拼接** | 支持（v02起） | 不支持 | 支持（v02起） |

### 3.4 URL过滤两种匹配模式

GWFD-110471 URL过滤支持两种与ICAP Server的交互模式（来自 §3.1）:

| 模式 | ICAP返回 | UDG本地动作 | 适用场景 |
|------|---------|-----------|----------|
| **分类匹配模式** | URL分类ID（Category ID） | UDG本地CONTCATEGBIND匹配套餐策略 | UDG保有套餐配置主权 |
| **直接动作模式** | 直接返回BLOCK/PERMIT/REDIRECT | UDG直接执行 | ICAP Server集中决策 |

### 3.5 URL过滤对不同协议的URL解析能力差异

| 协议 | URL解析能力 | 依赖SA |
|------|-----------|--------|
| HTTP/WAP1.X/WAP2.0 | **完整URL**（仅上行Get/Post） | SA-Basic + SA-Web Browsing + SA-Mobile |
| HTTPS | **仅SNI或证书**（不能解析完整URL） | SA-Basic + SA-Web Browsing + HTTP2.0 Host识别 |
| 非加密 QUIC | SNI或证书 | 同HTTPS |

> **关键限制**: HTTPS场景下，URL过滤**不能基于完整URL**，只能基于SNI——这是HTTPS加密带来的固有限制。

### 3.6 WSFD-211001 动态PCC vs 本地PCC

| 维度 | 动态PCC | 本地PCC |
|------|---------|---------|
| **决策方** | PCRF/PCF | GGSN-C/PGW-C/SMF 本地 |
| **接口** | Gx（4G）/ N7（5G） | PFCP |
| **适用场景** | 组网中有PCRF/PCF | 组网中无PCRF/PCF，或回滚到本地PCC |
| **UNC配置** | 仅需License（PCRF/PCF决策） | 需配置USRLOCATION + USRLOCATIONGRP + UPBINDUPG + APNUSRPROFG |
| **依赖UNC特性** | PCC基本功能（WSFD-109101） | PCC基本功能 + 基于业务感知的带宽控制（WSFD-211005） |

---

## 4. 依赖关系分析

### 4.1 特性依赖图（场景级全景）

```
                  ┌─────────────────────────────────────┐
                  │ GWFD-110101 SA-Basic（复用）          │
                  │ （业务感知基础，所有L7动作特性依赖）    │
                  └─────────────────┬───────────────────┘
                                    │ SA解析能力
                                    ▼
       ┌───────────────────────────────────────────────────────┐
       │                                                       │
       ▼                                                       ▼
┌──────────────────────┐                         ┌──────────────────────────┐
│ GWFD-020351 PCC基本   │                         │ GWFD-020357 ADC          │
│ 功能（UDG复用）       │                         │ （L7应用检测）            │
│ + WSFD-109101 PCC    │                         │ + WSFD-109102 ADC(UNC)   │
│ 基本功能（UNC复用）   │                         └──────────┬───────────────┘
└──────────┬───────────┘                                     │
           │                                                 │
           │ PCC规则体系                                       │ ADC检测+上报
           ▼                                                 ▼
    ┌──────┴────────────────────────────────────────┐  ┌─────────────────────┐
    │      │                  │                    │  │ 头增强族前置：        │
    │      ▼                  ▼                    ▼  │ ADC提供HTTP解析能力   │
    │ ┌─────────┐    ┌──────────────┐    ┌──────────────┐    └──────────┐
    │ │头增强族  │    │ 重定向族      │    │ URL过滤      │               │
    │ │110261/   │    │ 110281 Portal │    │ 110471       │               │
    │ │110262/   │    │ 110282 WebPxy │    │ (轨道B)      │               │
    │ │110263    │    │ 110283 DNS纠错│    └──────────────┘               │
    │ └────┬─────┘    │ 110284 HTTP重 │                                   │
    │      │          └──────────────┘                                   │
    │      ▼                                                             │
    │ ┌──────────────┐                                                   │
    │ │ GWFD-110401  │ ←强耦合依赖（启用防欺诈必须开启头增强）              │
    │ │ HTTP头防欺诈 │                                                   │
    │ └──────────────┘                                                   │
    │                                                                   │
    └───────────────────────────────────────────────────────────────────┘

           UNC侧（独立分支）
           ┌──────────────────────────────────────────┐
           │ WSFD-109101 PCC基本功能（UNC复用）         │
           │ + WSFD-211005 基于业务感知的带宽控制       │
           │     （无PCRF场景的本地PCC规则来源）         │
           └──────────────┬───────────────────────────┘
                          │
                          ▼
           ┌──────────────────────────────────────────┐
           │ WSFD-211001 基于初始接入位置的策略控制     │
           │ （位置触发层，本身不产生动作）              │
           │ 通过ULI匹配位置 → 触发带宽/访问限制策略下发 │
           └──────────────────────────────────────────┘
```

### 4.2 核心特性辐射分析

**SA-Basic（GWFD-110101）** 的辐射范围——**10个独有特性直接依赖它**：

| 依赖特性 | 依赖方式 | SA提供的能力 |
|---------|---------|-------------|
| GWFD-020357 ADC | 直接依赖 | L7应用检测引擎 |
| GWFD-110261 HTTP头增强 | 直接依赖 | HTTP报文解析 |
| GWFD-110262 RTSP头增强 | 直接依赖 | RTSP报文解析（+SA-Streaming） |
| GWFD-110263 HTTPS头增强 | 直接依赖 | HTTPS报文解析（+HTTP2.0 Host识别） |
| GWFD-110281 用户Portal | 直接依赖 | HTTP/WAP协议解析 |
| GWFD-110282 WebProxy | 直接依赖 | 业务流解析 |
| GWFD-110283 DNS纠错 | 直接依赖 | DNS报文解析（+SA-Network Administration） |
| GWFD-110284 HTTP智能重定向 | 直接依赖 | HTTP解析和规则匹配 |
| GWFD-110401 HTTP头防欺诈 | 直接依赖 | HTTP报文识别和解析 |
| GWFD-110471 URL过滤 | 直接依赖 | URL提取（HTTP/HTTPS SNI） |

**ADC（GWFD-020357）** 的辐射范围——ADC是L7动作特性的**共同前置**（应用感知层）：

| 依赖特性 | ADC提供的能力 | 强制度 |
|---------|-------------|--------|
| GWFD-110261/262/263 头增强族 | HTTP/HTTPS/RTSP报文解析（ADC使用SA引擎） | 间接（通过SA） |
| GWFD-110281 用户Portal | HTTP报文解析 | 间接 |
| GWFD-110284 HTTP智能重定向 | HTTP解析匹配规则 | 间接 |
| GWFD-110401 HTTP头防欺诈 | HTTP报文识别 | 间接 |
| GWFD-110471 URL过滤 | URL提取 | 间接 |

> **观察**: ADC不是显式强依赖（特性文档中头增强族只显式依赖SA-Basic），但ADC是"所有L7应用级控制"的事实前置（来自 Batch-04 发现-1）。

**头增强族（GWFD-110261）** 的辐射——**GWFD-110401 头防欺诈强耦合依赖**：

| 依赖特性 | 依赖方式 | 关系描述 |
|---------|---------|----------|
| GWFD-110401 HTTP头防欺诈 | **强耦合** | 启用防欺诈必须开启头增强（License 82209786 + 82209777 双开）；共用 HEADEN 对象（ANTIFRAUD/GRAYLIST 内嵌于 ADD HEADEN） |

### 4.3 强耦合与互斥关系

#### 4.3.1 强耦合依赖

| 关系 | 类型 | 说明 |
|------|------|------|
| GWFD-110401 → GWFD-110261 | **License强依赖** | 启用防欺诈必须开启HTTP头增强 |
| GWFD-020357 → GWFD-110101 (SA-Basic) | License依赖 | ADC基于SA执行检测 |
| GWFD-020357 → GWFD-020351 (PCC) | License依赖 | PCRF/PCF下发携带Application ID的PCC规则 |
| 头增强族 → SA-Web Browsing/Streaming/Mobile | License依赖 | 协议解析依赖 |
| GWFD-110471 → SA-Web Browsing/Mobile/HTTP2.0 Host识别 | License依赖 | URL提取依赖 |
| GWFD-110283 → GWFD-110136 (SA-Network Administration) | License依赖 | DNS报文解析依赖 |
| GWFD-110283 → GWFD-020301 (内容计费基本功能) | License依赖 | DNS纠错动作绑定在Rule |
| WSFD-211001 → WSFD-109101 (PCC UNC) | License强依赖 | PCC策略下发承载 |
| WSFD-211001 → WSFD-211005 (带宽控制 UNC，无PCRF场景) | License依赖 | 本地PCC规则来源 |

#### 4.3.2 互斥关系（加密协议限制）

| 特性 | 互斥特性 | 互斥原因 |
|------|---------|----------|
| GWFD-110261 HTTP头增强 | GWFD-110201 HTTP2.0 Host识别、GWFD-110203 HTTPS业务地址识别 | HTTP2.0/HTTPS加密报文不支持头增强 |
| GWFD-110262 RTSP头增强 | RTSP over HTTP | 不支持对RTSP over HTTP协议报文处理 |
| GWFD-110281 用户Portal | GWFD-110201 HTTP2.0 Host识别、GWFD-110203 HTTPS业务地址识别 | 加密报文不支持重定向处理 |
| GWFD-110284 HTTP智能重定向 | GWFD-110201 HTTP2.0 Host识别、GWFD-110203 HTTPS业务地址识别 | 加密报文不支持HTTP重定向 |
| GWFD-110401 HTTP头防欺诈 | RTSP协议 | 头防欺诈仅支持HTTP/HTTPS，RTSP不支持（族内唯一例外） |

### 4.4 UDG-UNC协作链路分析

#### 链路1: 位置触发的访问限制（最完整的CU协作）

```
用户激活（携带ULI）
  │
  ▼
RAN (SGSN/MME/AMF) 上报 ULI
  │
  ▼
UNC (SMF/PGW-C) [WSFD-211001]
  ├── 动态PCC: ULI透传给PCRF/PCF → PCRF决策 → CCA下发策略
  └── 本地PCC: 本地USRLOCATION匹配 → 本地决策
  │
  ▼ (N4/PFCP)
UDG (PGW-U/UPF) 安装访问限制规则
  ├── 带宽控制（WSFD-211005 BWM规则）
  ├── 阻塞（轨道A兜底阻塞）
  └── 重定向（轨道A，110281/282/283/284）
  │
  ▼
用户业务流被限制
```

#### 链路2: ADC触发的动态访问限制（PCRF决策）

```
UDG (GWFD-020357) 检测到应用数据流开始
  │ APPLICATION_START 事件
  ▼
UNC (PGW-C/SMF) 转发
  │ N7 Npcf_SMPolicyControl_Update
  ▼
PCRF/PCF 决策
  │ 下发新PCC规则（可能携带BLOCK/REDIRECT动作）
  ▼ (N4)
UDG 执行新PCC策略
  ├── 兜底阻塞（轨道A）
  ├── 重定向到订购页面
  └── 专有承载（高价值业务保障）
```

#### 链路3: URL过滤（独立ICAP链路，不经过PCRF）

```
用户访问URL
  │
  ▼
UDG (GWFD-110471) 解析提取URL
  │ ICAP REQMOD 请求
  ▼
ICAP Server 查询URL分类数据库
  │ 返回 Category ID 或 直接动作
  ▼
UDG 本地匹配 CONTCATEGBIND.ACTION
  │
  ▼
UDG 直接执行 BLOCK / PERMIT / REDIRECT
（轨道B，不经过PCRF/PCF，不经过PCCPOLICYGRP）
```

### 4.5 典型场景组合

| 场景 | 涉及特性组合 | 数据流 |
|------|------------|--------|
| **未签约业务阻塞+订购引导** | SA-Basic + ADC + HTTP智能重定向 + Portal | ADC识别应用 → PCRF下发策略 → 重定向到Portal订购页 |
| **URL黑名单阻塞** | SA-Basic + URL过滤 + ICAP Server | URL上送ICAP → 分类匹配 → CONTCATEGBIND.ACTION=BLOCK |
| **错误域名引导** | SA-Basic + SA-Network Admin + DNS纠错 | DNS查询失败 → DNSOVERWRITING重写 → 引导到搜索引擎 |
| **头增强认证** | SA-Basic + ADC + HTTP头增强 + 头防欺诈 | ADC解析HTTP → 防欺诈检测 → 头增强插入MSISDN → Web Server认证 |
| **网络加速代理** | SA-Basic + WebProxy + IPFarm | TCP SYN匹配 → 目的IP NAT到Proxy → Proxy加速 |
| **忙时拥塞小区限速** | UNC PCC + WSFD-211001 + UDG BWM | ULI匹配 → 策略下发 → BWM执行（访问限制+带宽控制协同） |
| **HTTPS业务管控（受限）** | SA-Basic + HTTPS头增强 + URL过滤（SNI） | HTTPS无法做HTTP智能重定向，但可做SNI级URL过滤 + SSL Extension头增强 |

---

## 5. 关键发现

### 5.1 ⭐ 发现一：双轨动作机制（核心架构发现）

**核心发现**: 访问限制场景中存在**两条完全独立的动作轨道路径**——这是本场景区别于计费/带宽场景的最关键架构事实。

#### 轨道A：PCC体系（RULE.POLICYTYPE 驱动）

```
用户业务流
    ↓
FILTER + FLOWFILTER + FLTBINDFLOWF（L3/L4匹配）
[+ L7FILTER + PROTBINDFLOWF（L7匹配）]
    ↓
RULE（POLICYTYPE = ADC / PCC / HEADEN / SMARTREDIRECT / WEBPROXY）
    ↓ POLICYNAME 指向
┌─────────────────────────────────────────────┐
│ ADC：直接在 RULE 上（FLOWFILTER）             │
│ PCC：PCCPOLICYGRP + URRGROUP                 │
│ HEADEN：HEADEN 对象                           │
│ SMARTREDIRECT：SMARTHTTPREDIR / DNSOVERWRITING│
│ WEBPROXY：IPFARM                              │
└─────────────────────────────────────────────┘
    ↓
UDG 执行动作（隐式 BLOCK / 头增强插入 / 重定向报文改写）
```

**轨道A特点**:
- 以 `RULE.POLICYTYPE` 为核心区分
- 动作类型由POLICYTYPE隐式决定（ADC兜底阻塞、HEADEN插入、SMARTREDIRECT改写）
- 配置链路长（FILTER → FLOWFILTER → RULE → POLICYNAME指向的具体对象）
- 走PCC体系时需要PCRF/PCF下发规则或本地预定义

**走轨道A的特性**: GWFD-020357 ADC、GWFD-110261/262/263 头增强、GWFD-110401 头防欺诈、GWFD-110284 HTTP智能重定向、GWFD-110283 DNS纠错、GWFD-110281 用户Portal、GWFD-110282 WebProxy

#### 轨道B：URL过滤体系（CFTEMPLATE/CONTCATEGBIND.ACTION 驱动）

```
用户访问 URL
    ↓
UDG 解析提取 URL（HTTP Get/Post / HTTPS SNI）
    ↓
ICAP REQMOD 上送 URL 到 ICAP Server
    ↓
ICAP Server 返回 Category ID 或直接动作
    ↓
UDG 匹配本地套餐策略：
┌─────────────────────────────────────────────┐
│ ADD CFTEMPLATE:ACTION=BLOCK/PERMIT/REDIRECT  │ ← 模板级缺省动作
│ ADD CONTCATEGBIND:ACTION=BLOCK/PERMIT/REDIRECT│ ← 分类级精确动作
└─────────────────────────────────────────────┘
    ↓
UDG 直接执行 BLOCK/PERMIT/REDIRECT
```

**轨道B特点**:
- 以 `CFTEMPLATE.ACTION` 和 `CONTCATEGBIND.ACTION` 为核心（**显式指定BLOCK/PERMIT/REDIRECT**）
- 动作类型直接在配置参数中声明，不通过POLICYTYPE间接表达
- 依赖外部ICAP Server（引入ICAP Server/Group/VPN配置体系）
- 触发维度单一（仅基于URL分类），不涉及复杂多条件组合
- **唯一显式支持PERMIT动作的轨道**

**走轨道B的特性**: GWFD-110471 URL过滤基本功能

#### 双轨对比矩阵（详见附录E）

| 维度 | 轨道A（PCC体系） | 轨道B（URL过滤体系） |
|------|-----------------|---------------------|
| **核心ConfigObject** | RULE（POLICYTYPE差异化） | CFTEMPLATE + CONTCATEGBIND |
| **动作指定方式** | 隐式（POLICYTYPE决定） | 显式（ACTION=BLOCK/PERMIT/REDIRECT） |
| **匹配维度** | 多维度（L3/L4/L7/错误码/URL/UserAgent...） | 单维度（URL分类） |
| **外部依赖** | 可选PCRF/PCF | **必需ICAP Server** |
| **典型MML命令** | ADD RULE, ADD PCCPOLICYGRP, ADD HEADEN, ADD SMARTHTTPREDIR | ADD CFTEMPLATE, ADD CONTCATEGBIND, ADD ICAPSERVER |
| **License共用** | 各特性独立License | URL过滤独立License（82200FCP UFBF01） |

#### 双轨协同

**两条轨道可以并存于同一用户**:
- 轨道A处理ADC/头增强/重定向类需求（基于应用、URL、用户属性）
- 轨道B处理URL分类过滤（基于外部URL分类数据库）
- 用户业务流可能先后被两条轨道检查，最终动作取决于配置优先级和规则匹配顺序

**对图谱建模的关键启示**:
1. RULE对象需要**两个variant_dimension**: `policy_track`（A/B）和`policy_type`（POLICYTYPE/ACTION）
2. 轨道B的CFTEMPLATE/CONTCATEGBIND是**独立于RULE体系**的配置对象，需要单独建模
3. ICAP Server互通配置是URL过滤**独有的资源类对象**，类似Portal/WebProxy的IPFarm

### 5.2 发现二：动态规则不支持七层（HTTPS/HTTP2.0 限制）

**核心发现**: 访问限制场景中**多个L7动作特性都不支持加密协议（HTTPS/HTTP2.0）**，仅WebProxy（L3层工作）和URL过滤（仅SNI）能部分处理加密协议。

| 特性 | HTTPS支持 | HTTP2.0支持 | 互斥原因 |
|------|----------|------------|----------|
| HTTP智能重定向 | 不支持 | 不支持 | 加密无法获取HTTP响应特征 |
| 用户Portal | 不支持 | 不支持 | 加密无法改写HTTP响应 |
| HTTP头增强 | 不支持（HTTP only） | 不支持 | 仅HTTP1.x |
| HTTPS头增强 | **支持**（在SSL Extension内） | 不支持 | 需TLV格式 |
| RTSP头增强 | N/A | N/A | 流媒体独立 |
| HTTP头防欺诈 | 支持（HTTPS） | 不支持 | 仅HTTP1.x |
| DNS纠错 | N/A（DNS独立） | N/A | 仅UDP DNS |
| WebProxy | **支持**（IP NAT不依赖L7） | **支持** | L3工作 |
| URL过滤 | 部分支持（仅SNI） | 部分支持 | HTTPS只能解析SNI |

**规律**: 凡是**需要在L7解析HTTP内容**的特性（重定向族的大部分、头增强中的HTTP）都不支持HTTPS/HTTP2.0；**WebProxy在L3工作**所以不受加密影响；**HTTPS头增强和URL过滤**通过特殊机制（SSL Extension / SNI）部分支持加密协议。

### 5.3 发现三：PERMIT 唯一性（仅URL过滤显式支持）

**核心发现**: 在访问限制场景的14特性中，**仅GWFD-110471 URL过滤（轨道B）显式支持PERMIT（放行）动作**；轨道A的特性主要是"不做动作"或"做阻塞/重定向"。

| 特性 | 是否显式PERMIT | 说明 |
|------|--------------|------|
| GWFD-110471 URL过滤 | **是**（CFTEMPLATE.ACTION=PERMIT） | 轨道B的独立动作参数 |
| ADC | 否 | 不匹配规则时兜底阻塞；匹配时不做动作（非显式PERMIT） |
| 头增强族 | 否 | 不匹配时不插入字段（非显式PERMIT） |
| 重定向族 | 否 | 不匹配时不重定向（非显式PERMIT） |
| 头防欺诈 | 否 | 不匹配时不检测（非显式PERMIT） |

**对业务语义的影响**:
- 轨道A的"放行"是隐式的（不匹配=放行），无法在策略中显式声明"此用户/此业务必须放行"
- 轨道B的PERMIT是显式的，可以针对特定URL分类配置"必须放行"（如白名单）
- URL过滤的 PERMIT 为访问限制场景提供了**白名单机制**（轨道A不具备）

### 5.4 发现四：RULE.POLICYTYPE 是动作类型的核心区分

**核心发现**: 在轨道A中，**RULE.POLICYTYPE 是区分不同访问限制动作类型的统一标识**，每个POLICYTYPE对应不同的POLICYNAME指向对象。

详见 §3.1 和 附录F（POLICYTYPE取值全景表）。

**关键约束**:
- HTTP智能重定向和DNS纠错共用 POLICYTYPE=SMARTREDIRECT（区分点在POLICYNAME指向对象）
- 用户Portal的captive配置不在RULE，而在USERPROFILE的CAPMODETHRES参数
- URL过滤的RULE虽然用POLICYTYPE=PCC，但动作不走PCCPOLICYGRP（轨道A→B混合）

### 5.5 发现五：头增强族共用的HEADEN对象——跨协议复用

**核心发现**: 头增强族3特性（HTTP/HTTPS/RTSP）**共用同一套配置对象和命令（ADD HEADEN）**，差异仅在"SA依赖"和"字段插入位置"两个维度（来自 Batch-05 发现-1）。

```
统一配置载体（所有协议共用）：
  ADD HEADEN（含 HEADERENNAME/DATATYPE/PREFIXNAME/ENCRYALGORI/PSWDKEY/ANTIFRAUD/GRAYLIST）
  ADD RULE:POLICYTYPE=HEADEN,POLICYNAME=<HEADEN 对象名>

差异点：
  ├─ HTTP：依赖SA-Web Browsing，插入HTTP扩展字段
  ├─ HTTPS：依赖SA-Web Browsing + HTTP2.0 Host识别，插入SSL Extension（TLV格式）
  └─ RTSP：依赖SA-Streaming，插入RTSP扩展字段
```

**对图谱第4层（ConfigObject）的启示**: HEADEN是一个跨协议复用的ConfigObject，其`variant_dimensions`应包含`protocol_type`（HTTP/HTTPS/RTSP/NSH）。

### 5.6 发现六：头防欺诈内嵌于头增强（强耦合）

**核心发现**: GWFD-110401 HTTP头防欺诈**不独立产生访问限制动作**，而是**内嵌于头增强（HEADEN）动作的前置检测层**（来自 Batch-08 发现-1）。

- `ADD HEADEN` 命令自带 `ANTIFRAUD=ENABLE/DISABLE` 和 `GRAYLIST=ENABLE/DISABLE` 参数
- 防欺诈不是独立动作，而是**内嵌于HEADEN对象的检测前置**
- 执行顺序：**防欺诈检测 → 字段纠正/冗余清理 → 头增强插入**（灰名单模式下跳过插入）
- RTSP头增强不支持防欺诈（族内唯一例外）

**License强依赖**: 启用防欺诈必须开启头增强（82209786 + 82209777 双开）。

### 5.7 发现七：重定向族共用的EXTENDEDFILTER与ERRORCODE

**核心发现**: HTTP智能重定向（GWFD-110284）和DNS纠错（GWFD-110283）共用 `EXTENDEDFILTER` 和 `ERRORCODE` 配置对象（来自 Batch-06 KP-4）。

| 特性 | EXTENDEDFILTER匹配维度 | ERRORCODE含义 |
|------|----------------------|--------------|
| HTTP智能重定向 | URL / USERAGENT / ERRORCODE / CONTENTTYPE / URLPOSTFIX | HTTP错误码（如 GT 400） |
| DNS纠错 | URL（域名）+ ERRORCODE | DNS错误码（如 EQUAL 3 NXDOMAIN） |

**关键观察**: 两者都通过 `ADD RULE:POLICYTYPE=SMARTREDIRECT`，区分点在 POLICYNAME 指向（SMARTHTTPREDIR vs DNSOVERWRITING）。

### 5.8 发现八：ADC是访问限制的"应用感知层"横切依赖

**核心发现**: ADC（GWFD-020357）提供的是"看见"而非"动作"——**所有需要基于应用/URL做判断的特性都依赖ADC/SA的解析能力**（来自 Batch-04 发现-1）。

```
ADC/SA 解析层（GWFD-020357 + SA-Web Browsing/Streaming/Mobile）
    ↓ 提供：应用标识、URL、五元组、Method、Content-Type
    ↓
┌────────────────────────────────────────────────────────────┐
│  访问限制动作层（基于 ADC 提供的信息匹配 RULE）              │
├────────────────────────────────────────────────────────────┤
│  DISCARD 类：ADC 兜底阻塞、URL 过滤 BLOCK                   │
│  HEADEN 类：HTTP/HTTPS/RTSP 头增强、HTTP 头防欺诈            │
│  REDIRECT 类：HTTP 智能重定向、DNS 纠错、用户Portal、WebProxy│
└────────────────────────────────────────────────────────────┘
```

**对图谱第1层（BusinessRule）的启示**: ADC应建模为一条横切依赖关系——"访问限制场景中的所有L7动作特性 constrained_by ADC/SA解析能力"。

---

## 附录A: 14特性索引表

| 序号 | 特性ID | 特性名称 | 产品 | 网元 | 首发版本 | License控制项 | feature_group | 核心能力 |
|------|--------|---------|------|------|---------|--------------|--------------|----------|
| 1 | GWFD-110101 | SA-Basic（复用） | UDG | PGW-U/UPF | 20.0.0 | 82209749 LKV3G5SABS01 | SA_BASE | L3/L4/L7业务识别基础 |
| 2 | GWFD-020351 | PCC基本功能（UDG复用） | UDG | PGW-U/UPF | 20.0.0 | 82209825 LKV3G5PCCB01 | PCC_FRAME | 用户面PCC规则执行 |
| 3 | WSFD-109101 | PCC基本功能（UNC复用） | UNC | SMF/PGW-C/AMF | 20.0.0 | 82207979 LKV3W9SPCC11 | PCC_FRAME | 控制面PCC策略接收 |
| 4 | GWFD-020357 | 增强的ADC基本功能 | UDG | PGW-U/UPF | 20.1.0 | 82200AFK LKV3G5ADCF01 | ADC | L7应用检测上报 |
| 5 | WSFD-109102 | ADC基本功能（UNC复用） | UNC | GGSN-C/PGW-C/SMF | 20.5.0 | 82200BNK LKV2BADCF01 | ADC | 控制面应用检测中继 |
| 6 | GWFD-110261 | HTTP头增强 | UDG | PGW-U/UPF | 20.0.0 | 82209777 LKV3G5HTHE01 | HEADEN | HTTP报文头插入用户信息 |
| 7 | GWFD-110262 | RTSP头增强 | UDG | PGW-U/UPF | 20.0.0 | 82209778 LKV3G5RTHE01 | HEADEN | RTSP报文头插入用户信息 |
| 8 | GWFD-110263 | HTTPS头增强 | UDG | PGW-U/UPF | 20.0.0 | 82209779 LKV3G5HTSE01 | HEADEN | HTTPS报文头（SSL Extension）插入 |
| 9 | GWFD-110281 | 用户Portal | UDG | PGW-U/UPF | 20.0.0 | 82209780 LKV3G5CPPT01 | REDIRECT | 重定向到Portal Server（captive/non-captive交替） |
| 10 | GWFD-110282 | Web Proxy | UDG | PGW-U/UPF | 20.0.0 | 82209781 LKV3G5WEBP01 | REDIRECT | L3 IP NAT重定向到Proxy |
| 11 | GWFD-110283 | DNS纠错 | UDG | PGW-U/UPF | 20.0.0 | 82209782 LKV3G5DNSO01 | REDIRECT | DNS Overwriting引导到Platform |
| 12 | GWFD-110284 | HTTP智能重定向 | UDG | PGW-U/UPF | 20.0.0 | 82209783 LKV3G5SHPR01 | REDIRECT | L7 HTTP响应改写（多条件触发） |
| 13 | GWFD-110401 | HTTP头防欺诈 | UDG | PGW-U/UPF | 20.0.0 | 82209786 LKV3G5HHAS01 | ANTIFRAUD | 头增强前置检测+纠正欺诈字段 |
| 14 | GWFD-110471 | URL过滤基本功能 | UDG | PGW-U/UPF | 20.10.2 | 82200FCP LKV3G5UFBF01 | URL_FILTER | 基于ICAP的URL分类过滤（轨道B） |
| 15 | WSFD-211001 | 基于初始接入位置的策略控制 | UNC | SMF/PGW-C/GGSN-C | 20.3.0 (v01) / 20.7.0 (v02 SMF) | 82200BNQ LKV2PCIAL01 | ACCESS_CTRL_TRIGGER | ULI位置匹配触发策略下发 |

> **说明**: 序号1-5为复用特性（来自带宽控制/计费场景的共用基础设施），序号6-15为访问限制场景独有特性（10 UDG + 1 UNC = 11独有）。附录B/C主要覆盖11独有特性的命令与对象。

---

## 附录B: MML命令交叉参考

> 图谱第4层（MMLCommand + invokes边）实例化的直接输入。覆盖11独有特性的所有命令 + 复用特性的关键命令。

### B.1 UDG侧核心命令（按功能分组）

#### B.1.1 License与刷新（场景级共用）

| 命令 | 涉及特性 | 用途 |
|------|---------|------|
| SET LICENSESWITCH | 全部11个独有特性 | License开关 |
| SET REFRESHSRV | GWFD-020357, 110261/262/263, 110281, 110282, 110283, 110284, 110401, 110471 | 策略刷新生效（ALL/USERPROFILE） |
| LOD SIGNATUREDB | GWFD-020357, 110281, 110283, 110401, 110471 | 加载SA特征库 |
| LOD PARSERDB | GWFD-110401 | 加载协议解析库 |

#### B.1.2 三四层过滤链（场景级共用）

| 命令 | 涉及特性 | 用途 |
|------|---------|------|
| ADD FILTER | 全部11个独有特性 | 增加三四层过滤器 |
| ADD FLOWFILTER | 全部11个独有特性 | 增加流过滤器 |
| ADD FLTBINDFLOWF | 全部11个独有特性 | 增加Filter与FlowFilter绑定 |

#### B.1.3 七层过滤链（ADC/头增强/重定向族/防欺诈/Portal共用）

| 命令 | 涉及特性 | 用途 |
|------|---------|------|
| ADD L7FILTER | GWFD-020357, 110261/262/263, 110281, 110401 | 增加七层过滤器（URL/Method） |
| ADD PROTBINDFLOWF | GWFD-020357, 110261/262/263, 110281, 110401 | 增加流过滤器协议绑定 |
| ADD EXTENDEDFILTER | GWFD-110283, 110284 | 增加扩展过滤器（URL/UserAgent/ContentType多维） |
| ADD ERRORCODE | GWFD-110283, 110284 | 增加错误码（HTTP错误码 / DNS错误码） |
| ADD WELLKNOWNPORT | GWFD-110401 | 增加知名端口（HTTP端口80/8080） |

#### B.1.4 ADC独有命令

| 命令 | 涉及特性 | 用途 |
|------|---------|------|
| ADD ADCPARA | GWFD-020357 | 增加ADC参数（FLOWINFORPT + ADCHYSTTIMER） |

#### B.1.5 头增强族独有命令

| 命令 | 涉及特性 | 用途 |
|------|---------|------|
| ADD HEADEN | GWFD-110261, 110262, 110263, 110401 | 增加头增强对象（含ANTIFRAUD/GRAYLIST） |
| SET BASE64 | GWFD-110261, 110262, 110263 | base64编码开关 |

#### B.1.6 重定向族独有命令

| 命令 | 涉及特性 | 用途 |
|------|---------|------|
| ADD SMARTHTTPREDIR | GWFD-110284 | 增加HTTP智能重定向动作策略 |
| ADD REDIRAPPENDINFO | GWFD-110284 | 增加重定向携带信息（MSISDN/IMSI/IMEI） |
| ADD DNSOVERWRITING | GWFD-110283 | 增加DNS重写动作（含Platform IP） |
| SET IPFARMGLOBAL | GWFD-110281, 110282 | 设置IPFarm全局参数（LBMETHOD/心跳阈值） |
| ADD IPFARM | GWFD-110281, 110282 | 增加IPFarm |
| ADD IPFARMSERVER | GWFD-110281, 110282 | 增加IPFarm服务器 |
| ADD LOGICINF | GWFD-110281, 110282, 110471 | 增加逻辑接口（心跳检测/ICAP互通） |
| ADD BLACKLISTRULE | GWFD-110282 | 增加黑名单规则（WebProxy独有） |

#### B.1.7 URL过滤独有命令（轨道B核心）

| 命令 | 涉及特性 | 用途 |
|------|---------|------|
| ADD VPNINST | GWFD-110471 | 增加VPN实例（ICAP互通专网） |
| ADD ICAPSERVER | GWFD-110471 | 增加ICAP服务器（URL_FILTERING类型） |
| ADD ICAPLOCALINFO | GWFD-110471 | 增加ICAP本端信息（User Agent） |
| ADD ICAPSVRGRP | GWFD-110471 | 增加ICAP服务器组 |
| ADD ICAPSVRBINDISG | GWFD-110471 | 增加ICAP服务器与组绑定 |
| ADD APN | GWFD-110281, 110282, 110471 | 增加APN配置 |
| SET APNCFFUNC | GWFD-110471 | 设置APN内容过滤开关 |
| ADD CFPROFILE | GWFD-110471 | 增加内容过滤策略 |
| ADD CFTEMPLATE | GWFD-110471 | 增加内容过滤模板（含ACTION=BLOCK/PERMIT/REDIRECT） |
| SET APNCFTEMPLATE | GWFD-110471 | 设置APN内容过滤模板绑定 |
| ADD CFPROFBINDCFT | GWFD-110471 | 增加内容过滤策略与模板绑定 |
| ADD CONTCATEGROUP | GWFD-110471 | 增加内容分类组（CATEGORYID） |
| ADD CONTCATEGBIND | GWFD-110471 | 增加策略与分类组绑定（含ACTION） |
| SET CFCACHEPARA | GWFD-110471 | 设置内容过滤缓存参数 |
| SET GLBCFFUNC | GWFD-110471 | 设置内容过滤全局开关 |
| ADD GLBCFTEMPLATE | GWFD-110471 | 增加全局内容过滤模板 |
| SET CFPROTOCOLLST | GWFD-110471 | 设置开启内容过滤的协议列表 |
| ADD CFWHITEURLLST | GWFD-110471 | 增加URL过滤白名单列表 |
| SET CFSRVMODE | GWFD-110471 | 配置URL过滤业务模式 |
| ADD CFIPWHITELIST | GWFD-110471 | 增加内容过滤IP白名单 |
| ADD CFPFSPECACTION | GWFD-110471 | 增加指定策略特殊场景动作 |

#### B.1.8 计费属性（场景级共用）

| 命令 | 涉及特性 | 用途 |
|------|---------|------|
| ADD URR | GWFD-020357, 110281, 110282, 110471 | 增加使用量上报规则 |
| ADD URRGROUP | GWFD-020357, 110281, 110282, 110471 | 增加URR组 |

#### B.1.9 PCC策略与规则（场景级共用）

| 命令 | 涉及特性 | 用途 |
|------|---------|------|
| ADD PCCPOLICYGRP | GWFD-020357, 110281, 110282, 110471 | 增加PCC策略组（含ADCMUTEFLAG） |
| ADD RULE | 全部11个独有特性 | 增加规则（POLICYTYPE差异化） |
| ADD USERPROFILE | 全部11个独有特性 | 增加用户模板（含CAPMODETHRES） |
| ADD RULEBINDING | 全部11个独有特性 | 增加UserProfile与Rule绑定 |

#### B.1.10 调测验证命令

| 命令 | 涉及特性 | 用途 |
|------|---------|------|
| LST LICENSESWITCH | 全部 | 查询License开关 |
| LST RULE | 全部 | 查询规则配置 |
| LST RULEBINDING | 全部 | 查询规则绑定 |
| LST USERPROFILE | 全部 | 查询用户模板 |
| LST FLOWFILTER / LST FLTBINDFLOWF / LST FILTER | 全部 | 查询过滤器链 |
| LST L7FILTER / LST PROTBINDFLOWF | ADC/头增强/重定向/防欺诈/Portal | 查询七层过滤 |
| LST HEADEN | 头增强族/防欺诈 | 查询头增强对象（含ANTIFRAUD） |
| LST PCCPOLICYGRP | 多特性 | 查询PCC策略组 |
| LST URRGROUP | 多特性 | 查询URR组 |
| LST IPFARM / LST IPFARMSERVER | Portal/WebProxy | 查询IPFarm及服务器状态 |
| LST LOGICINF | Portal/WebProxy/URL过滤 | 查询逻辑接口 |
| LST SMARTHTTPREDIR | HTTP智能重定向 | 查询HTTP智能重定向配置 |
| LST DNSOVERWRITING | DNS纠错 | 查询DNS重写动作 |
| LST EXTENDEDFILTER | HTTP智能重定向/DNS纠错 | 查询扩展过滤器 |
| LST CONTCATEGROUP | URL过滤 | 查询内容分类组 |
| LST ICAPSERVER / LST ICAPSVRGRP | URL过滤 | 查询ICAP服务器配置 |
| DSP ICAPSVRSTATUS | URL过滤 | 查询ICAP服务器状态 |
| DSP SESSIONINFO | 全部 | 查询用户上下文 |
| DSP RULECHECK | WebProxy | 规则IP版本一致性检查 |
| EXP MML | 全部 | 导出MML配置（故障收集） |

### B.2 UNC侧核心命令

#### B.2.1 PCC基本功能（复用，来自带宽场景）

| 命令 | 涉及特性 | 用途 |
|------|---------|------|
| SET LICENSESWITCH | 全部UNC特性 | License开关 |
| SET PCCFUNC | WSFD-109101 | PCC功能设置 |
| ADD PCRF / ADD PCRFGROUP / ADD PCRFBINDGRP | WSFD-109101 | PCRF定义与组绑定 |
| SET DFTGLBPCRFGRP | WSFD-109101 | 缺省PCRF组 |
| SET PCCFAILACTION | WSFD-109101 | PCC故障处理 |
| SET POLICYMODE | WSFD-109101 | 接口模式选择（Gx/N7） |
| SET N7RCVATTRCTRL / SET N7SNDATTRCTRL | WSFD-109101 | N7接收/发送属性控制 |
| SET FHBYPASS | WSFD-109101 | 紧急旁路 |

#### B.2.2 WSFD-211001 位置触发独有命令

| 命令 | 涉及特性 | 用途 |
|------|---------|------|
| ADD USRLOCATION | WSFD-211001 | 增加用户位置（CGI/ECGI/NCGI） |
| ADD USRLOCATIONGRP | WSFD-211001 | 增加用户位置组 |
| ADD UPBINDUPG / MOD UPBINDUPG | WSFD-211001 | 用户模板组绑定（含LOCGROUPNAME） |
| ADD APNUSRPROFG | WSFD-211001 | APN/DNN与用户模板组绑定 |
| LST USRLOCATION / LST USRLOCATIONGRP | WSFD-211001 | 查询位置与位置组 |
| LST UPBINDUPG / LST APNUSRPROFG | WSFD-211001 | 查询绑定关系 |

#### B.2.3 UNC侧通用规则命令（与UDG共用结构）

| 命令 | 涉及特性 | 用途 |
|------|---------|------|
| ADD RULE | WSFD-109101, WSFD-211001(间接) | 规则定义 |
| ADD USERPROFILE | WSFD-109101 | 用户模板 |
| ADD RULEBINDING | WSFD-109101 | 规则绑定 |
| ADD USRPROFGROUP | WSFD-211001 | 用户模板组 |
| ADD APNUSRPROFG | WSFD-211001 | APN/DNN绑定 |
| ADD APN | 多特性 | APN配置 |

### B.3 命令总数统计

| 类别 | UDG侧命令数 | UNC侧命令数 | 合计 |
|------|-----------|-----------|------|
| License与刷新 | 4 | 1 | 5 |
| 三四层过滤链 | 3 | 0 | 3 |
| 七层过滤链 | 5 | 0 | 5 |
| ADC独有 | 1 | 0 | 1 |
| 头增强族独有 | 2 | 0 | 2 |
| 重定向族独有 | 8 | 0 | 8 |
| URL过滤独有 | 21 | 0 | 21 |
| 计费属性 | 2 | 0 | 2 |
| PCC策略与规则 | 4 | 5 | 9 |
| 位置触发独有 | 0 | 4 | 4 |
| 调测验证 | 20+ | 6+ | 26+ |
| **合计（去重后）** | **约55** | **约17** | **约70** |

> URL过滤独有命令最多（21条），反映轨道B体系的独立性。

---

## 附录C: 配置对象复用矩阵

> 图谱第4层（ConfigObject + operates_on边）实例化的直接输入。

### C.1 场景级共用配置对象（跨特性复用）

| 配置对象 | 涉及特性数 | 主要用途 |
|---------|----------|---------| 
| FILTER | 11（全部独有） | 三四层匹配条件 |
| FLOWFILTER | 11（全部独有） | 流过滤器 |
| FLTBINDFLOWF | 11（全部独有） | Filter与FlowFilter绑定 |
| L7FILTER | 6（ADC/头增强族/Portal/防欺诈） | 七层URL/Method匹配 |
| PROTBINDFLOWF | 6（同L7FILTER） | 协议+L7FILTER绑定 |
| EXTENDEDFILTER | 2（HTTP重定向/DNS纠错） | 多维扩展过滤 |
| ERRORCODE | 2（HTTP重定向/DNS纠错） | 错误码范围 |
| RULE | 11（全部独有） | 规则载体（POLICYTYPE差异化） |
| USERPROFILE | 11（全部独有） | 用户模板（含CAPMODETHRES） |
| RULEBINDING | 11（全部独有） | UserProfile与Rule绑定 |
| URR | 4（ADC/Portal/WebProxy/URL过滤） | 使用量上报规则 |
| URRGROUP | 4（同URR） | URR组 |
| PCCPOLICYGRP | 4（ADC/Portal/WebProxy/URL过滤） | PCC策略组（含ADCMUTEFLAG） |
| APN | 3（Portal/WebProxy/URL过滤） | APN配置 |

### C.2 特性独有配置对象

| 配置对象 | 所属特性 | 用途 |
|---------|---------|------|
| **ADCPARA** | GWFD-020357 ADC | ADC流信息上报+迟滞定时器 |
| **HEADEN** | GWFD-110261/262/263 头增强族 + GWFD-110401 头防欺诈 | 跨协议复用，含ANTIFRAUD/GRAYLIST |
| **SMARTHTTPREDIR** | GWFD-110284 HTTP智能重定向 | HTTP重定向动作策略 |
| **REDIRAPPENDINFO** | GWFD-110284 HTTP智能重定向 | 重定向携带字段（MSISDN/IMSI/IMEI） |
| **DNSOVERWRITING** | GWFD-110283 DNS纠错 | DNS重写动作（含Platform IP） |
| **IPFARMGLOBAL** | GWFD-110281 Portal + GWFD-110282 WebProxy | IPFarm全局参数 |
| **IPFARM** | GWFD-110281 Portal + GWFD-110282 WebProxy | 重定向服务器集群 |
| **IPFARMSERVER** | GWFD-110281 Portal + GWFD-110282 WebProxy | IPFarm下的服务器IP |
| **LOGICINF** | GWFD-110281/110282 Portal/WebProxy + GWFD-110471 URL过滤 | 逻辑接口（心跳检测/ICAP互通） |
| **BLACKLISTRULE** | GWFD-110282 WebProxy | 黑名单规则 |
| **WELLKNOWNPORT** | GWFD-110401 头防欺诈 | 知名端口（HTTP端口识别） |
| **VPNINST** | GWFD-110471 URL过滤 | VPN实例（ICAP专网） |
| **ICAPSERVER** | GWFD-110471 URL过滤 | ICAP服务器（URL_FILTERING类型） |
| **ICAPLOCALINFO** | GWFD-110471 URL过滤 | ICAP本端信息 |
| **ICAPSVRGRP** | GWFD-110471 URL过滤 | ICAP服务器组 |
| **ICAPSVRBINDISG** | GWFD-110471 URL过滤 | ICAP服务器与组绑定 |
| **APNCFFUNC** | GWFD-110471 URL过滤 | APN粒度内容过滤开关 |
| **CFPROFILE** | GWFD-110471 URL过滤 | 内容过滤策略 |
| **CFTEMPLATE** | GWFD-110471 URL过滤 | 内容过滤模板（含ACTION） |
| **APNCFTEMPLATE** | GWFD-110471 URL过滤 | APN与模板绑定 |
| **CFPROFBINDCFT** | GWFD-110471 URL过滤 | 策略与模板绑定 |
| **CONTCATEGROUP** | GWFD-110471 URL过滤 | 内容分类组（CATEGORYID） |
| **CONTCATEGBIND** | GWFD-110471 URL过滤 | 策略与分类组绑定（含ACTION） |
| **CFCACHEPARA** | GWFD-110471 URL过滤 | 本地缓存参数 |
| **USRLOCATION** | WSFD-211001 位置触发 | 用户位置（CGI/ECGI/NCGI） |
| **USRLOCATIONGRP** | WSFD-211001 位置触发 | 用户位置组 |

### C.3 完整复用矩阵（11独有特性 × 主要对象）

| 配置对象 | GWFD-020357 ADC | GWFD-110261 HTTP头增强 | GWFD-110262 RTSP头增强 | GWFD-110263 HTTPS头增强 | GWFD-110281 Portal | GWFD-110282 WebProxy | GWFD-110283 DNS纠错 | GWFD-110284 HTTP重定向 | GWFD-110401 头防欺诈 | GWFD-110471 URL过滤 | WSFD-211001 位置触发 |
|---------|------|------|------|------|------|------|------|------|------|------|------|
| FILTER | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | - |
| FLOWFILTER | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | - |
| FLTBINDFLOWF | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | - |
| L7FILTER | Y | Y | Y | Y | Y | - | - | - | Y | - | - |
| PROTBINDFLOWF | Y | Y | Y | Y | Y | - | - | - | Y | - | - |
| EXTENDEDFILTER | - | - | - | - | - | - | Y | Y | - | - | - |
| ERRORCODE | - | - | - | - | - | - | Y | Y | - | - | - |
| ADCPARA | Y | - | - | - | - | - | - | - | - | - | - |
| HEADEN | - | Y | Y | Y | - | - | - | - | Y | - | - |
| SMARTHTTPREDIR | - | - | - | - | - | - | - | Y | - | - | - |
| REDIRAPPENDINFO | - | - | - | - | - | - | - | Y | - | - | - |
| DNSOVERWRITING | - | - | - | - | - | - | Y | - | - | - | - |
| IPFARMGLOBAL | - | - | - | - | Y | Y | - | - | - | - | - |
| IPFARM | - | - | - | - | Y | Y | - | - | - | - | - |
| IPFARMSERVER | - | - | - | - | Y | Y | - | - | - | - | - |
| LOGICINF | - | - | - | - | Y | Y | - | - | - | Y | - |
| BLACKLISTRULE | - | - | - | - | - | Y | - | - | - | - | - |
| WELLKNOWNPORT | - | - | - | - | - | - | - | - | Y | - | - |
| VPNINST | - | - | - | - | - | - | - | - | - | Y | - |
| ICAPSERVER | - | - | - | - | - | - | - | - | - | Y | - |
| ICAPLOCALINFO | - | - | - | - | - | - | - | - | - | Y | - |
| ICAPSVRGRP | - | - | - | - | - | - | - | - | - | Y | - |
| ICAPSVRBINDISG | - | - | - | - | - | - | - | - | - | Y | - |
| APN | - | - | - | - | Y | Y | - | - | - | Y | - |
| APNCFFUNC | - | - | - | - | - | - | - | - | - | Y | - |
| CFPROFILE | - | - | - | - | - | - | - | - | - | Y | - |
| CFTEMPLATE | - | - | - | - | - | - | - | - | - | Y | - |
| APNCFTEMPLATE | - | - | - | - | - | - | - | - | - | Y | - |
| CFPROFBINDCFT | - | - | - | - | - | - | - | - | - | Y | - |
| CONTCATEGROUP | - | - | - | - | - | - | - | - | - | Y | - |
| CONTCATEGBIND | - | - | - | - | - | - | - | - | - | Y | - |
| CFCACHEPARA | - | - | - | - | - | - | - | - | - | Y | - |
| USRLOCATION | - | - | - | - | - | - | - | - | - | - | Y |
| USRLOCATIONGRP | - | - | - | - | - | - | - | - | - | - | Y |
| URR | Y | - | - | - | Y | Y | - | - | - | Y | - |
| URRGROUP | Y | - | - | - | Y | Y | - | - | - | Y | - |
| PCCPOLICYGRP | Y | - | - | - | Y | Y | - | - | - | Y | - |
| RULE | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | - |
| USERPROFILE | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | - |
| RULEBINDING | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | - |
| UPBINDUPG | - | - | - | - | - | - | - | - | - | - | Y |
| APNUSRPROFG | - | - | - | - | - | - | - | - | - | - | Y |

**图例**: Y = 使用此配置对象; - = 不使用

**关键观察**:
1. `FILTER + FLOWFILTER + FLTBINDFLOWF + RULE + USERPROFILE + RULEBINDING` 是跨特性的通用配置六元组（10个UDG独有特性全用）
2. URL过滤（GWFD-110471）拥有最多独有对象（13个：VPNINST + ICAP系列5个 + CF系列7个），反映轨道B的独立配置体系
3. HEADEN 跨4特性复用（HTTP/HTTPS/RTSP头增强 + 头防欺诈），是协议无关的统一头增强对象
4. IPFarm系列仅Portal+WebProxy共用，是重定向服务器集群机制
5. ADC/Portal/WebProxy/URL过滤 共用 URR/URRGROUP/PCCPOLICYGRP，因为它们都涉及计费属性绑定

---

## 附录D: 典型端到端配置流程

> 图谱第3层（TaskCommandOrderEdge）实例化的直接输入。按访问限制动作类型组织。

### D.1 DISCARD（阻塞）流程：ADC兜底阻塞 + URL过滤BLOCK

#### 场景1：ADC兜底阻塞（轨道A）

**依赖**: SA-Basic + PCC基本功能 + ADC

```mml
// 1. 开启License
SET LICENSESWITCH:LICITEM="LKV3G5SABS01",SWITCH=ENABLE;   // SA-Basic
SET LICENSESWITCH:LICITEM="LKV3G5PCCB01",SWITCH=ENABLE;   // PCC
SET LICENSESWITCH:LICITEM="LKV3G5ADCF01",SWITCH=ENABLE;   // ADC

// 2. 配置三四层过滤（匹配所有流量作为兜底）
ADD FILTER:FILTERNAME="filter_default",L34PROTTYPE=STRING,L34PROTOCOL=ANY;
ADD FLOWFILTER:FLOWFILTERNAME="ff_default";
ADD FLTBINDFLOWF:FLOWFILTERNAME="ff_default",FILTERNAME="filter_default";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 3. 配置七层过滤（匹配特定应用）
ADD L7FILTER:L7FILTERNAME="l7_p2p",SUBL7FLTNAME="1",URL="*bittorrent*";
ADD PROTBINDFLOWF:FLOWFILTERNAME="ff_default",PROTOCOLNAME="http",L7FILTERNAME="l7_p2p";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 4. 配置ADC参数（可选，控制上报频率）
ADD ADCPARA:FLOWFILTERNAME="ff_default",FLOWINFORPT=ENABLE,ADCHYSTTIMER=300;

// 5. 配置ADC规则（POLICYTYPE=ADC，允许上报）
ADD RULE:RULENAME="rule_adc_p2p",POLICYTYPE=ADC,
  FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="ff_default",
  PRIORITY=15,ADCMUTEFLAG=DISABLE;

// 6. 绑定用户模板
ADD USERPROFILE:USERPROFILENAME="up_adc_block";
ADD RULEBINDING:USERPROFILENAME="up_adc_block",RULENAME="rule_adc_p2p";

// 兜底阻塞机制：业务流匹配不上所有PCC rule时，UDG阻塞业务流
```

#### 场景2：URL过滤BLOCK（轨道B）

**依赖**: SA-Basic + SA-Web Browsing + URL过滤 + ICAP Server

```mml
// 1. 开启License
SET LICENSESWITCH:LICITEM="LKV3G5UFBF01",SWITCH=ENABLE;   // URL过滤

// 2. 配置ICAP Server互通（前置）
ADD VPNINST:VPNINSTANCE="vpn-gcfif";
ADD LOGICINF:NAME="gcfif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="192.168.1.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn-gcfif";
ADD ICAPSERVER:ICAPSERVERNAME="icapserver1",ICAPSERVERTYPE=URL_FILTERING,ICAPSVRIPTYPE=IPV4,ICAPSERVERIPV4="172.16.39.136",VPNINSTANCE="vpn-gcfif";
ADD ICAPLOCALINFO:ICAPSERVERTYPE=URL_FILTERING,USERAGENT="test";
ADD ICAPSVRGRP:ICAPSVRGRPNAME="icapsvrgrp1",ICAPSERVERTYPE=URL_FILTERING;
ADD ICAPSVRBINDISG:ICAPSVRGRPNAME="icapsvrgrp1",ICAPSERVERNAME="icapserver1";

// 3. 配置APN并开启内容过滤
ADD APN:APN="apn-test";
SET APNCFFUNC:APNNAME="apn-test",CFSWITCHVALUE=ENABLE;

// 4. 配置内容过滤策略 + 模板（缺省动作=BLOCK）
ADD CFPROFILE:CFPROFILENAME="cf1";
ADD CFTEMPLATE:CFTEMPLATENAME="icaptemplate",ICAPSRVGMNAME="icapsvrgrp1",ACTION=BLOCK;  // 关键：缺省BLOCK
SET APNCFTEMPLATE:APNNAME="apn-test",CFTEMPLATENAME="icaptemplate";
ADD CFPROFBINDCFT:CFTEMPLATENAME="icaptemplate",CFPROFILENAME="cf1";

// 5. 配置内容分类组与策略绑定（分类级动作=BLOCK）
ADD CONTCATEGROUP:CONTCATEGNAME="ccgp1",CATEGORYTYPE=SPECIFIC,CATEGORYID=1;
ADD CONTCATEGBIND:CFPROFILENAME="cf1",CONTCATEGNAME="ccgp1",ACTION=BLOCK;  // 关键：分类BLOCK

// 6. 开启本地cache（减少ICAP交互）
SET CFCACHEPARA:CACHEIDLETIME=7200,CACHESW=ENABLE;

// 7. 配置三四层过滤 + 规则（POLICYTYPE=PCC，仅匹配触发）
ADD FILTER:FILTERNAME="filter_test",L34PROTTYPE=STRING,L34PROTOCOL=ANY;
SET REFRESHSRV:REFRESHTYPE=USERPROFILE;
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_test1";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test1",FILTERNAME="filter_test";

// 8. 配置计费属性与PCC策略
ADD URR:URRNAME="urr_2",URRID=2,USAGERPTMODE=OFFLINE;
ADD URRGROUP:URRGROUPNAME="urrgroup1",UPURRNAME1="urr_2",DOWNURRNAME1="urr_2";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="ppg_test",URRGROUPNAME="urrgroup1";

// 9. 配置业务规则（POLICYTYPE=PCC 触发URL过滤业务，但实际BLOCK走CFTEMPLATE/CONTCATEGBIND）
ADD RULE:RULENAME="rule_urlfilter",POLICYTYPE=PCC,
  FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilter_test1",
  PRIORITY=1,POLICYNAME="ppg_test";

// 10. 绑定用户模板
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_urlfilter";
```

### D.2 HEADEN（头增强）流程：HTTP头增强 + 防欺诈

**依赖**: SA-Basic + SA-Web Browsing + HTTP头增强 + HTTP头防欺诈

```mml
// 1. 开启License（防欺诈强依赖头增强，双开）
SET LICENSESWITCH:LICITEM="LKV3G5HTHE01",SWITCH=ENABLE;   // HTTP头增强
SET LICENSESWITCH:LICITEM="LKV3G5HHAS01",SWITCH=ENABLE;   // HTTP头防欺诈

// 2. 配置三四层过滤
ADD FILTER:FILTERNAME="filter_test_0",L34PROTTYPE=STRING,L34PROTOCOL=ANY,SVRSTARTPORT=0,SVRENDPORT=0;
ADD FILTER:FILTERNAME="filter_test_65535",L34PROTTYPE=STRING,L34PROTOCOL=ANY,SVRSTARTPORT=65535,SVRENDPORT=65535;
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_test";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",FILTERNAME="filter_test_0";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",FILTERNAME="filter_test_65535";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 3. 配置七层过滤（URL + Method=GET/POST）
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="1",URL="www.huawei.com/*",METHODTYPE=GET-1;
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="2",URL="www.huawei.com/*",METHODTYPE=POST-1;
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",PROTOCOLNAME="http",L7FILTERNAME="l7filter_test";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 4. 配置知名端口（识别HTTP协议）
ADD WELLKNOWNPORT:IDENPROTNAME="http0",PROTOCOLNAME="http",PORTOP=EQUAL,STARTPORT=0,PRIORITY=5;
LOD SIGNATUREDB:LOADMODE=LATEST;
LOD PARSERDB:LOADMODE=LATEST;

// 5. 配置头增强对象（使能防欺诈）
ADD HEADEN:HEADERENNAME="header_test",DATATYPE=IMSI1,PREFIXNAME="X-imsi",
  ENCRYALGORI=AES128,PSWDKEY="XXXXXX",PSWDKEYCONFIRM="XXXXXX",
  ANTIFRAUD=ENABLE;   // 关键：使能HTTP头防欺诈

// 6. 配置业务规则（POLICYTYPE=HEADEN）
ADD RULE:RULENAME="rule_headen",POLICYTYPE=HEADEN,
  FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilter_test",
  POLICYNAME="header_test";

// 7. 绑定用户模板
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_headen";
```

### D.3 REDIRECT（重定向）流程：4种协议层实现

#### D.3.1 HTTP智能重定向流程（L7 HTTP响应改写）

**依赖**: SA-Basic + SA-Web Browsing + HTTP智能重定向

```mml
// 1. 开启License
SET LICENSESWITCH:LICITEM="LKV3G5SHPR01",SWITCH=ENABLE;

// 2. 配置三四层过滤
ADD FILTER:FILTERNAME="f-any",L34PROTTYPE=STRING,L34PROTOCOL=ANY;
ADD FLOWFILTER:FLOWFILTERNAME="flow-filter1";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flow-filter1",FILTERNAME="f-any";
SET REFRESHSRV:REFRESHTYPE=USERPROFILE;

// 3. 配置扩展过滤器（多维度匹配）
ADD EXTENDEDFILTER:EXTFLTNAME="filter_url",URL="www.huawei.com/*";
ADD EXTENDEDFILTER:EXTFLTNAME="filter_ua",USERAGENT="Mozilla/*";

// 4. 配置错误码（HTTP错误码大于400）
ADD ERRORCODE:ERRORCODENAME="httperrorcode",ERRORCODEOP=GT,ERRORCODESTART=400;

// 5. 配置重定向携带信息
ADD REDIRAPPENDINFO:APPENDINFONAME="redir_info",REQURLFLAG=ENABLE,IMSIFLAG=ENABLE;

// 6. 配置HTTP智能重定向动作
ADD SMARTHTTPREDIR:SMTHTTPREDINAME="http-redirect_test",
  SERVERURL="www.example.com",
  EXTFLTTYPE1=AND,EXTFLTNAME1="filter_url",
  EXTFLTTYPE2=AND,EXTFLTNAME2="filter_ua",
  APPENDINFONAME="redir_info",BINDErrCODENAME="httperrorcode";

// 7. 配置业务规则（POLICYTYPE=SMARTREDIRECT）
ADD RULE:RULENAME="rule_redirect",POLICYTYPE=SMARTREDIRECT,
  FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flow-filter1",
  PRIORITY=1,POLICYNAME="http-redirect_test";
```

#### D.3.2 DNS纠错流程（DNS Overwriting）

**依赖**: SA-Basic + SA-Network Administration + 内容计费基本功能 + DNS纠错

```mml
// 1. 开启License
SET LICENSESWITCH:LICITEM="LKV3G5DNSO01",SWITCH=ENABLE;

// 2. 配置三四层过滤（匹配DNS UDP 53端口）
ADD FILTER:FILTERNAME="filter1",L34PROTTYPE=STRING,L34PROTOCOL=UDP,SVRSTARTPORT=53,SVRENDPORT=53;
ADD FLOWFILTER:FLOWFILTERNAME="flow-filter1";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flow-filter1",FILTERNAME="filter1";
SET REFRESHSRV:REFRESHTYPE=USERPROFILE;

// 3. 配置扩展过滤器（错误域名匹配）
ADD EXTENDEDFILTER:EXTFLTNAME="l7-filter1",URL="www.example.com/*";

// 4. 配置DNS错误码（NXDOMAIN = 3）
ADD ERRORCODE:ERRORCODENAME="dnserrorcode",ERRORCODEOP=EQUAL,ERRORCODESTART=3;

// 5. 配置DNS纠错动作（绑定Platform IP）
ADD DNSOVERWRITING:DNSOVERWRTNAME="dec_1",
  EXTFLTTYPE1=AND,EXTFLTNAME1="l7-filter1",
  SERVERIP1="192.168.1.1",                    // 第三方Platform IP
  BINDERRCODENAME="dnserrorcode";

// 6. 配置业务规则（POLICYTYPE=SMARTREDIRECT，与HTTP重定向共用）
ADD RULE:RULENAME="rule_dns",POLICYTYPE=SMARTREDIRECT,
  FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flow-filter1",
  PRIORITY=20,POLICYNAME="dec_1";              // 关键：POLICYNAME指向DNSOVERWRITING
```

#### D.3.3 用户Portal流程（captive/non-captive交替）

**依赖**: SA-Basic + SA-Web Browsing + SA-Mobile + 用户Portal

```mml
// 1. 开启License
SET LICENSESWITCH:LICITEM="LKV3G5CPPT01",SWITCH=ENABLE;

// 2. 配置IPFarm全局参数
SET IPFARMGLOBAL:SERVERTYPE=REDIRECT,TIMETHRESHOLD=10,
  HEALTHSUCCLIMIT=2,HEALTHFAILLIMIT=4,LBMETHOD=LEAST_LOAD;

// 3. 配置心跳检测接口
ADD LOGICINF:NAME="phif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.10.10.10",IPV4MASK1="255.255.255.255";

// 4. 配置IPFarm与Portal服务器
ADD IPFARM:HEALTHCHECKFLAG=ENABLE,IPFARMNAME="farm_portal",IPVERSION=IPV4,INTERFACENAME="phif1/0/0";
ADD IPFARMSERVER:IPFARMNAME="farm_portal",IPVERSION=IPV4,SERVERIPV4="192.168.253.251";
ADD IPFARMSERVER:IPFARMNAME="farm_portal",IPVERSION=IPV4,SERVERIPV4="192.168.253.253";

// 5. 配置过滤链 + L7FILTER
ADD FILTER:FILTERNAME="filter_http",L34PROTTYPE=STRING,L34PROTOCOL=TCP,SVRSTARTPORT=80,SVRENDPORT=80;
ADD FLOWFILTER:FLOWFILTERNAME="ff_portal";
ADD FLTBINDFLOWF:FLOWFILTERNAME="ff_portal",FILTERNAME="filter_http";
ADD L7FILTER:L7FILTERNAME="l7-portal",SUBL7FLTNAME="1",URL="*";
ADD PROTBINDFLOWF:FLOWFILTERNAME="ff_portal",PROTOCOLNAME="http",L7FILTERNAME="l7-portal";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 6. 配置PCC策略组
ADD URR:URRNAME="urr_portal",URRID=100,USAGERPTMODE=ONLINE;
ADD URRGROUP:URRGROUPNAME="cp_portal",UPURRNAME1="urr_portal",DOWNURRNAME1="urr_portal";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pg_portal",URRGROUPNAME="cp_portal";

// 7. 配置规则（POLICYTYPE=PCC，captive配置在USERPROFILE）
ADD RULE:RULENAME="rule_portal",POLICYTYPE=PCC,
  FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="ff_portal",
  PRIORITY=10,POLICYNAME="pg_portal";

// 8. 配置用户模板（含CAPMODETHRES captive定时器）
ADD USERPROFILE:USERPROFILENAME="up_portal",CAPMODETHRES=6;  // 6分钟captive周期
ADD RULEBINDING:USERPROFILENAME="up_portal",RULENAME="rule_portal";
ADD APN:APN="apn-portal";
```

#### D.3.4 WebProxy流程（L3 IP NAT）

**依赖**: SA-Basic + WebProxy

```mml
// 1. 开启License
SET LICENSESWITCH:LICITEM="LKV3G5WEBP01",SWITCH=ENABLE;

// 2. 配置IPFarm全局参数
SET IPFARMGLOBAL:SERVERTYPE=REDIRECT,TIMETHRESHOLD=10,
  HEALTHSUCCLIMIT=2,HEALTHFAILLIMIT=4,LBMETHOD=LEAST_LOAD;

// 3. 配置心跳检测接口
ADD LOGICINF:NAME="phif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.10.10.10",IPV4MASK1="255.255.255.255";

// 4. 配置IPFarm与Proxy服务器
ADD IPFARM:HEALTHCHECKFLAG=ENABLE,IPFARMNAME="farm_proxy",IPVERSION=IPV4,INTERFACENAME="phif1/0/0";
ADD IPFARMSERVER:IPFARMNAME="farm_proxy",IPVERSION=IPV4,SERVERIPV4="192.168.253.251";
ADD IPFARMSERVER:IPFARMNAME="farm_proxy",IPVERSION=IPV4,SERVERIPV4="192.168.253.253";

// 5. 配置三四层过滤（匹配特定Server IP）
ADD FILTER:FILTERNAME="filter_proxy",L34PROTTYPE=STRING,L34PROTOCOL=TCP,
  SVRIPMODE=IP,SVRIP="192.168.10.123",SVRIPMASKTYPE=IPTYPE,SVRIPMASK="0.0.0.0";
ADD FLOWFILTER:FLOWFILTERNAME="flow-l34";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flow-l34",FILTERNAME="filter_proxy";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 6. 配置计费属性 + PCC策略组
ADD URR:URRNAME="urr_proxy",URRID=1000,USAGERPTMODE=ONLINE;
ADD URRGROUP:URRGROUPNAME="cp_proxy",UPURRNAME1="urr_proxy",DOWNURRNAME1="urr_proxy";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pg_proxy",URRGROUPNAME="cp_proxy";

// 7. 配置WebProxy规则（POLICYTYPE=WEBPROXY，POLICYNAME指向IPFarm）
ADD RULE:RULENAME="rule_webproxy",POLICYTYPE=WEBPROXY,
  FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flow-l34",
  PRIORITY=10,POLICYNAME="farm_proxy";           // 关键：POLICYNAME指向IPFarm名

// 8. 配置计费规则（POLICYTYPE=PCC）
ADD RULE:RULENAME="rule_pcc",POLICYTYPE=PCC,
  FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flow-l34",
  PRIORITY=20,POLICYNAME="pg_proxy";

// 9. 配置用户模板（含CAPMODETHRES）
ADD USERPROFILE:USERPROFILENAME="up_proxy",CAPMODETHRES=6;
ADD RULEBINDING:USERPROFILENAME="up_proxy",RULENAME="rule_webproxy";
ADD RULEBINDING:USERPROFILENAME="up_proxy",RULENAME="rule_pcc";
ADD APN:APN="apn-webproxy";
```

### D.4 接入控制流程：UNC位置触发 → UDG执行

**依赖**: UNC PCC基本功能 + WSFD-211001 + UDG BWM/重定向（策略执行端）

```mml
// ============ UNC侧配置 ============

// 1. 开启License
SET LICENSESWITCH:LICITEM="LKV2PCIAL01",SWITCH=ENABLE;   // 初始接入位置

// 2. 配置用户位置信息（3个小区，覆盖2/3G、4G、5G）
ADD USRLOCATION:LOCATIONNAME="loc_test1",LOCATIONTYPE=CGI,MCC="333",MNC="111",LAC="0xFFFD",CI="0xFFFD";
ADD USRLOCATION:LOCATIONNAME="loc_test2",LOCATIONTYPE=ECGI,MCC="333",MNC="111",ECI="0xffffffd";
ADD USRLOCATION:LOCATIONNAME="loc_test3",LOCATIONTYPE=NCGI,MCC="333",MNC="111",NCI="0xffffffffd";

// 3. 配置用户位置组（批量绑定）
ADD USRLOCATIONGRP:LOCGROUPNAME="locgrp_test",LOCATIONNAME="loc_test1";
ADD USRLOCATIONGRP:LOCGROUPNAME="locgrp_test",LOCATIONNAME="loc_test2";
ADD USRLOCATIONGRP:LOCGROUPNAME="locgrp_test",LOCATIONNAME="loc_test3";

// 4. 将用户模板与位置组绑定到用户模板组
MOD UPBINDUPG:USERPROFGNAME="upg_test1",UPBINDTYPE=SPECIFIC,
  USERPROFILENAME="up_test1",LOCGROUPNAME="locgrp_test";

// 5. 将用户模板组绑定到APN/DNN
ADD APNUSRPROFG:APN="apn-test",USERPROFGNAME="upg_test1";

// ============ UDG侧执行端（动作由USERPROFILE绑定的规则定义） ============
// 注：USERPROFILE up_test1 已绑定带宽控制/重定向/阻塞规则（来自其他特性的配置）
// 用户激活时，UNC匹配ULI → 下发策略 → UDG执行对应访问限制动作
```

---

## 附录E: 双轨动作机制深度对比

> 本场景核心架构发现。访问限制动作存在两条独立的轨道路径。

### E.1 双轨核心对比表

| 维度 | 轨道A（PCC体系） | 轨道B（URL过滤体系） |
|------|-----------------|---------------------|
| **核心ConfigObject** | RULE（POLICYTYPE差异化） | CFTEMPLATE + CONTCATEGBIND |
| **动作指定方式** | 隐式（POLICYTYPE决定动作） | 显式（ACTION=BLOCK/PERMIT/REDIRECT） |
| **匹配维度** | 多维度（L3/L4/L7/错误码/URL/UserAgent...） | 单维度（URL分类） |
| **外部依赖** | 可选PCRF/PCF | **必需ICAP Server** |
| **动作类型** | 隐式阻塞、头增强插入、重定向改写 | 直接BLOCK/PERMIT/REDIRECT |
| **典型MML命令** | ADD RULE, ADD PCCPOLICYGRP, ADD HEADEN, ADD SMARTHTTPREDIR | ADD CFTEMPLATE, ADD CONTCATEGBIND, ADD ICAPSERVER |
| **独立配置体系** | 共用 FILTER/FLOWFILTER/USERPROFILE | 独有 APNCFFUNC/CFPROFILE/CFTEMPLATE/CONTCATEGROUP/ICAP系列 |
| **License共用** | 各特性独立License | URL过滤独立License（82200FCP UFBF01） |
| **走此轨道的特性** | 7个（ADC/头增强族/头防欺诈/重定向族4特性） | 1个（URL过滤） |
| **PERMIT支持** | 不显式支持 | **唯一显式支持PERMIT** |
| **PCRF/PCF交互** | 是（动态PCC场景） | 否（ICAP独立链路） |

### E.2 双轨动作类型映射表

| 动作类型 | 轨道A如何表达 | 轨道B如何表达 |
|---------|-------------|-------------|
| **DISCARD（阻塞）** | ADC兜底阻塞（规则匹配不上丢弃）；Portal IPFarm全DOWN时DEFAULTACT=BLOCK | CFTEMPLATE.ACTION=BLOCK 或 CONTCATEGBIND.ACTION=BLOCK |
| **HEADEN（头增强）** | POLICYTYPE=HEADEN，POLICYNAME指向HEADEN对象 | 不支持（轨道B不做头增强） |
| **REDIRECT（重定向）** | POLICYTYPE=SMARTREDIRECT/WEBPROXY，或USERPROFILE captive | CFTEMPLATE.ACTION=REDIRECT 或 CONTCATEGBIND.ACTION=REDIRECT |
| **PERMIT（放行）** | 不显式支持（不匹配=放行） | CFTEMPLATE.ACTION=PERMIT 或 CONTCATEGBIND.ACTION=PERMIT |

### E.3 双轨对应的ConfigObject体系

#### 轨道A的ConfigObject层次

```
FILTER → FLOWFILTER → FLTBINDFLOWF （三四层匹配）
[+ L7FILTER → PROTBINDFLOWF] （七层匹配，可选）
[+ EXTENDEDFILTER + ERRORCODE] （多维匹配，HTTP重定向/DNS纠错）
    ↓
RULE （POLICYTYPE = ADC / PCC / HEADEN / SMARTREDIRECT / WEBPROXY）
    ↓ POLICYNAME 指向具体对象
┌──────────────────────────────────────────────────┐
│ ADC：直接在 RULE 上                                │
│ PCC：PCCPOLICYGRP + URRGROUP                      │
│ HEADEN：HEADEN 对象（含ANTIFRAUD/GRAYLIST）         │
│ SMARTREDIRECT：SMARTHTTPREDIR 或 DNSOVERWRITING    │
│ WEBPROXY：IPFARM 对象                              │
└──────────────────────────────────────────────────┘
    ↓
USERPROFILE → RULEBINDING → APN （用户绑定）
```

#### 轨道B的ConfigObject层次（URL过滤独有）

```
=== ICAP Server互通层（前置）===
VPNINST → LOGICINF → ICAPSERVER → ICAPLOCALINFO
                            ↓
                  ICAPSVRGRP → ICAPSVRBINDISG
=== URL过滤业务层（独立动作体系）===
APN → APNCFFUNC （APN粒度开关）
    ↓
CFPROFILE （内容过滤策略）
    ↓
CFTEMPLATE （内容过滤模板，含ACTION=BLOCK/PERMIT/REDIRECT） ← 模板级动作
    ↓
APNCFTEMPLATE （APN与模板绑定）
    ↓
CFPROFBINDCFT （策略与模板绑定）
    ↓
CONTCATEGROUP （内容分类组，CATEGORYID）
    ↓
CONTCATEGBIND （策略与分类组绑定，含ACTION=BLOCK/PERMIT/REDIRECT） ← 分类级动作
    ↓
CFCACHEPARA （本地缓存参数）

=== 与轨道A共用的匹配触发层 ===
FILTER → FLOWFILTER → FLTBINDFLOWF （仅匹配触发，动作不走轨道B）
    ↓
RULE （POLICYTYPE=PCC，仅触发URL过滤业务）
    ↓
USERPROFILE → RULEBINDING
```

### E.4 双轨协同（同一用户可并存）

**两条轨道可以并存于同一用户**:
- 轨道A处理 ADC/头增强/重定向类需求（基于应用、URL、用户属性）
- 轨道B处理 URL分类过滤（基于外部URL分类数据库）
- 用户业务流可能先后被两条轨道检查，最终动作取决于配置优先级和规则匹配顺序

**潜在建模难点**（来自 Batch-07 §6 后续待办）:
1. **双轨优先级**: 当RULE（轨道A）和CFTEMPLATE/CONTCATEGBIND（轨道B）对同一业务流给出不同动作时，实际执行哪个？需查参考信息或现网验证
2. **ICAP故障降级**: ICAP Server不可用时，URL过滤的缺省动作（BLOCK还是PERMIT）需查ADD CFTEMPLATE的ACTION默认值
3. **双轨与PCCPOLICYGRP的交互**: URL过滤的RULE也用POLICYTYPE=PCC，但其动作不走PCCPOLICYGRP，这是潜在建模难点

### E.5 双轨对图谱建模的启示

1. **RULE对象需要两个variant_dimension**: `policy_track`（A/B）和`policy_type`（POLICYTYPE/ACTION）
2. **轨道B的CFTEMPLATE/CONTCATEGBIND是独立于RULE体系的配置对象**，需要单独建模为ConfigObject
3. **ICAP Server互通配置是URL过滤独有的资源类对象**，类似Portal/WebProxy的IPFarm，应建模为独立的ResourceObject
4. **PERMIT动作的建模**: 仅在轨道B显式存在，应在BusinessRule中标注"轨道B独有动作"

---

## 附录F: POLICYTYPE取值全景表

> RULE.POLICYTYPE 是访问限制场景区分动作类型的核心参数。本附录穷举所有取值。

| POLICYTYPE | 动作类型 | POLICYNAME指向对象 | 涉及特性 | 轨道 | 备注 |
|-----------|---------|-------------------|----------|------|------|
| **ADC** | ADC应用检测（独立规则） | 直接在RULE上（FLOWFILTER） | GWFD-020357 | A | 配合ADCMUTEFLAG控制上报 |
| **PCC** | 标准PCC规则（多用途） | PCCPOLICYGRP | GWFD-020357(ADC复用)、GWFD-110281(Portal)、GWFD-110282(WebProxy计费规则)、GWFD-110471(URL过滤触发) | A | 多特性复用 |
| **HEADEN** | 头增强（族内统一） | HEADEN 对象名 | GWFD-110261/262/263、GWFD-110401 | A | 跨4特性复用（含防欺诈） |
| **SMARTREDIRECT** | HTTP智能重定向 / DNS纠错（共用！） | SMARTHTTPREDIR / DNSOVERWRITING | GWFD-110284、GWFD-110283 | A | 两特性共用，区分在POLICYNAME指向 |
| **WEBPROXY** | Web Proxy（L3 IP NAT） | IPFARM 对象名 | GWFD-110282 | A | POLICYNAME指向IPFarm |
| **（Portal特殊）** | 用户Portal（captive） | PCCPOLICYGRP | GWFD-110281 | A | captive配置在USERPROFILE.CAPMODETHRES，RULE用POLICYTYPE=PCC |
| **BWM**（带宽场景） | 带宽管理策略 | PCCPOLICYGRP | （带宽控制场景特性） | A | 不在访问限制场景，仅作对比 |
| **QOS**（带宽场景） | QoS属性直接绑定 | QOSPROP | （带宽控制场景特性） | A | 不在访问限制场景 |
| **CHARGING**（计费场景） | 计费策略 | PCCPOLICYGRP | （计费场景特性） | A | 不在访问限制场景 |

**关键约束**:
- 同一RULENAME值在不同POLICYTYPE间**不能重复**（如PCC类型与QOS类型的RULENAME不能同名）
- 同一特性可同时配置不同POLICYTYPE的多条RULE记录（如WebProxy同时配置WEBPROXY和PCC规则）

---

## 附录G: SA协议解析依赖矩阵

> 访问限制场景的所有L7动作特性都依赖SA协议解析能力。本附录详列各特性的SA依赖。

| 特性 | SA-Basic | SA-Web Browsing | SA-Mobile | SA-Streaming | SA-Network Admin | HTTP2.0 Host识别 | 内容计费基本功能 |
|------|---------|----------------|----------|-------------|-----------------|-----------------|---------------|
| GWFD-020357 ADC | ✓ 必须 | ✓ HTTP场景 | ✓ MMS场景 | - | - | - | - |
| GWFD-110261 HTTP头增强 | ✓ 必须 | ✓ 必须 | ✓ MMS场景 | - | - | - | - |
| GWFD-110262 RTSP头增强 | ✓ 必须 | - | - | ✓ 必须 | - | - | - |
| GWFD-110263 HTTPS头增强 | ✓ 必须 | ✓ 必须 | ✓ MMS场景 | - | - | ✓ 必须 | - |
| GWFD-110281 用户Portal | ✓ 必须 | ✓ 必须 | ✓ WAP1.X | - | - | - | - |
| GWFD-110282 WebProxy | ✓ 必须 | - | - | - | - | - | - |
| GWFD-110283 DNS纠错 | ✓ 必须 | - | - | - | ✓ 必须 | - | ✓ 必须 |
| GWFD-110284 HTTP智能重定向 | ✓ 必须 | ✓ 必须 | - | - | - | - | - |
| GWFD-110401 HTTP头防欺诈 | ✓ 必须 | ✓ 必须 | - | - | - | - | - |
| GWFD-110471 URL过滤 | ✓ 必须 | ✓ HTTP/WAP2.0 | ✓ WAP1.X | - | - | ✓ HTTPS | - |

**图例**: ✓ 必须 = 此SA子特性是该访问限制特性的强制依赖

**关键观察**:
1. **SA-Basic 是所有10个UDG独有特性的共同依赖**（横切依赖）
2. **SA-Web Browsing** 是HTTP类特性的主要依赖（ADC/头增强族/Portal/重定向/防欺诈/URL过滤）
3. **SA-Network Administration** 仅DNS纠错使用（DNS报文解析）
4. **HTTP2.0 Host识别** 仅HTTPS类特性使用（HTTPS头增强/URL过滤的HTTPS场景）
5. **SA-Streaming** 仅RTSP头增强使用
6. **内容计费基本功能** 仅DNS纠错显式依赖（DNS纠错动作绑定在Rule，依赖内容计费基础功能）

---

## 附录H: 特性间隐藏关系总结

以下关系并非特性文档中显式声明的"依赖"或"交互"，而是通过配置对象复用、接口共享和数据流分析推断出的隐藏关系。

### H.1 通过配置对象推断的关系

| 配置对象 | 被哪些特性共用 | 推断的隐藏关系 |
|---------|-------------|--------------|
| RULE (ADD RULE) | 全部11个独有特性 | 所有使用RULE的特性在配置时RULENAME不能冲突（同一产品内） |
| HEADEN | HTTP/HTTPS/RTSP头增强 + 头防欺诈 | 头防欺诈完全寄生，没有独立配置命令 |
| EXTENDEDFILTER + ERRORCODE | HTTP智能重定向 + DNS纠错 | 两者共用POLICYTYPE=SMARTREDIRECT，是技术近亲 |
| IPFarm + IPFARMSERVER + LOGICINF | 用户Portal + WebProxy | 共享重定向服务器集群方案，心跳检测机制相同 |
| URR + URRGROUP + PCCPOLICYGRP | ADC + Portal + WebProxy + URL过滤 | 计费属性绑定是这4个特性的共同配置 |
| CFTEMPLATE + CONTCATEGBIND | 仅URL过滤 | 轨道B独立于RULE体系，是访问限制场景的"另起炉灶" |

### H.2 通过接口推断的关系

| 接口 | 共用特性 | 推断的隐藏关系 |
|------|---------|--------------|
| Gx (Diameter) | 所有UNC特性 | Gx连接故障（PCRF不可达）同时影响所有Gx特性 |
| N7 (HTTP/2) | 所有UNC 5G特性 | N7连接故障同时影响所有N7特性 |
| N4 (PFCP) | 所有UDG+UNC特性 | N4连接故障导致所有控制面→用户面规则传递中断 |
| ICAP (RFC 3507) | 仅URL过滤 | ICAP链路故障仅影响URL过滤（轨道B独立） |

### H.3 通过业务流推断的关系

| 业务流环节 | 使用方 | 推断的隐藏关系 |
|----------|--------|--------------|
| SA解析的URL | ADC、头增强族、HTTP智能重定向、DNS纠错、URL过滤 | SA特征库升级可能同时影响所有依赖URL的特性 |
| SA解析的Method | 头增强族（GET/POST）、HTTP智能重定向、头防欺诈 | Method识别准确率影响多种动作 |
| SA解析的SNI | HTTPS头增强、URL过滤（HTTPS场景） | HTTPS加密场景共享SNI识别能力 |
| ADC上报的应用标识 | PCRF/PCF动态策略 → 触发所有访问限制动作 | ADC是动态访问限制的"眼睛" |

### H.4 配置冲突风险矩阵

| 冲突场景 | 涉及特性 | 冲突原因 | 解决方案 |
|---------|---------|---------|---------|
| 同一RULENAME用于不同POLICYTYPE | 多特性 | 不同POLICYTYPE的RULENAME不能同名 | 规划命名规范，加前缀区分（如adc_/headen_/redirect_） |
| 头增强字段配置为HTTP标准头域名 | 头增强族 + 头防欺诈 | 标准头域名（如host）可能导致防欺诈失败 | 使用非标准前缀（如X-msisdn、X-imsi） |
| 同时配置ADC规则和URL过滤规则 | ADC + URL过滤 | 两条轨道可能对同一业务流给出不同动作 | 明确双轨优先级，规划策略边界 |
| Portal与WebProxy同时配置 | Portal + WebProxy | 都使用IPFarm，可能冲突 | 不同业务流匹配不同规则，IPFarm独立配置 |
| HTTPS场景期望HTTP重定向 | HTTP智能重定向 + 用户业务 | HTTP重定向不支持HTTPS | 改用WebProxy（L3）或URL过滤（HTTPS SNI） |
| RTSP头增强期望防欺诈 | RTSP头增强 + 头防欺诈 | 头防欺诈不支持RTSP协议 | 配合Streaming Server自身认证弥补盲区 |

### H.5 协议覆盖盲区总结

| 协议 | 不支持此协议的特性 | 启示 |
|------|-----------------|------|
| **HTTPS** | HTTP智能重定向、用户Portal、HTTP头增强 | 加密协议是L7动作的盲区，需通过HTTPS头增强/URL过滤SNI/WebProxy弥补 |
| **HTTP2.0** | 几乎所有L7动作特性（除WebProxy） | HTTP2.0加密普及后，传统L7动作方案面临挑战 |
| **RTSP over HTTP** | RTSP头增强 | 流媒体特殊场景需单独处理 |
| **TCP DNS** | DNS纠错 | 仅支持UDP DNS，TCP DNS场景无法纠错 |

---

> **文档生成说明**: 本文档基于11个访问限制场景特性知识文档 + 5个主题批次（Batch-04~08）横向分析产出。所有特性ID、License编号、命令名、配置对象名均严格引用自各特性的知识文档和主题批次。跨特性关系分析基于配置对象复用、接口共享、依赖链路推断，以及双轨动作机制的对比。文档不包含任何未经源文档支持的臆测内容。
>
> **关键源文档**:
> - 11个特性文档: `feature-knowledge/GWFD-*.md` + `WSFD-211001-*.md`
> - 5个主题批次: `topic-knowledge/Batch-04-ADC核心.md` / `Batch-05-头增强.md` / `Batch-06-重定向族.md` / `Batch-07-URL过滤与接入控制.md` / `Batch-08-防欺诈.md`
> - 质量标杆: `带宽控制场景/feature-knowledge/cross-feature-analysis.md`（1119行）
>
> **核心架构发现**: 双轨动作机制（轨道A PCC体系 vs 轨道B URL过滤体系）是访问限制场景区别于计费/带宽场景的最关键架构事实，详见 §5.1 和 附录E。
