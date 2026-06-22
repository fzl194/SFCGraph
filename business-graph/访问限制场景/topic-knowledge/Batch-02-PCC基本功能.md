# Batch-02: PCC基本功能（UDG侧）——访问限制动作载体
> 批次 02 | 主题 PCC架构/三类规则/Event Trigger/静态规则机制 | 来源 UDG特性指南 GWFD-020351(9) + 一望5G PCC静态规则(4) | 文件数 13 | 核心度 ★★★★★

## 1. 概述（本批次文档覆盖的板块）

本批次是PCC基本功能的完整UDG侧视图，**PCC是访问限制DISCARD/REDIRECT两种动作的统一载体**：

| 板块 | 来源文件 | 核心内容 |
|------|----------|----------|
| PCC架构与定义 | `GWFD-020351 PCC基本功能特性概述_47011385.md` | PCC=策略+计费控制；N7/N4下发链路；5G网元分工 |
| PCC核心概念 | `实现原理/相关概念_72244993.md` | **AM/UE/SM三类策略**；**动态/预定义/本地规则**；规则即PDR；动作PA（FAR/URR/QER） |
| 业务流程 | `实现原理/业务流程_47013470.md` | PDU会话建立/修改/释放；N7/N4信令 |
| Event Trigger | `实现原理/Event Trigger_47013472.md` | **12类触发器**（决定PCF决策时机） |
| 2/3/4/5G差异 | `实现原理/2_3_4_5G PCC功能差异_47013471.md` | 5G新增AM/UE策略；Gx→N7/N15/N4；预定义规则组统一 |
| 动态PCC配置 | `激活PCC基本功能/配置动态PCC功能_74096530.md` | **7步MML配置**（License→PCCPOLICYGRP→FLOWFILTER→RULE→USERPROFILE→REFRESHSRV） |
| 本地PCC配置 | `激活PCC基本功能/配置本地PCC功能_74096529.md.md` | 无PCF时SMF下发UserProfile |
| 调测方法 | `调测PCC基本功能_42369277.md` | N4 PFCP Session Establishment验证 |
| 命令参考 | `GWFD-020351 PCC基本功能参考信息_79592737.md` | 7条核心MML命令清单 |
| 静态规则What | `何为PCC静态规则——What？_86169704.md` | **预定义+本地=静态规则**；UPF支持三四层+七层特征 |
| 静态规则Why | `使用PCC静态规则——Why？_32946325.md` | **动态规则不支持七层特征**→必须用静态规则 |
| 静态规则How | `PCC静态规则原理——How？_86009740.md` | **6条预定义规则**完整规划/安装/应用流程示例 |
| 结语 | `结语_33031965.md` | 精细化管理三赢 |

**对访问限制场景的核心价值**：PCC规则上的"动作"明确枚举了"**重定向、URL过滤**"（见相关概念§动作），是DISCARD/REDIRECT的官方载体定义。

## 2. 核心知识点

### KP-01: PCC定义与5G架构 — ★★★★★

> SourcePath: `特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/GWFD-020351 PCC基本功能特性概述_47011385.md`

**PCC（Policy and Charging Control）** = 策略和计费控制。在业务流程中实现UE策略、移动性策略、会话策略和计费控制，通过区分业务并进行实时QoS控制。

**5G PCC架构组件**：
| 组件 | 网元 | 角色 |
|------|------|------|
| 策略控制功能 | PCRF/PCF | 策略决策 |
| 策略控制执行 | PGW-C/SMF + PGW-U/UPF | 策略执行 |
| 接入和移动策略执行 | AMF | AM策略执行 |
| 业务策略提供 | AF | 应用级会话信息 |

**适用NF**：PGW-U、UPF（本特性）、PGW-C/SMF、PCRF/PCF、SPR/UDR、AF

**License**：`82209825 LKV3G5PCCB01 PCC 基本功能`

**遵循标准（3GPP）**：
- 23501 v15.2.0（5G系统架构）
- 23502 v15.2.0（5G系统流程）
- **23503 v15.2.0（5G PCC框架）**
- 29507 v15.2.0（接入和移动策略控制）
- **29512 v15.2.0（会话管理策略控制）** ← SM策略核心标准
- 29513 v15.2.0（PCC信令流与QoS参数映射）

### KP-02: PCC下发链路 N7→N4 — ★★★★★（访问限制动作下发主链路）

> SourcePath: 同上 §原理概述

**PCRF/PCF 通过 N7 接口将 QoS 及计费策略下发给 PGW-C/SMF，PGW-C/SMF 通过 N4 接口再下发给 PGW-U/UPF，PGW-U/UPF 基于用户和业务类型进行**限速和门控**。**

**关键节点职责**：
| 网元 | 职责 |
|------|------|
| PCF | 策略决策，下发动态规则/预定义规则/Triggers |
| SMF | 将PCF策略转换为N4 PDR/FAR/QER/URR下发给UPF；将SDF与QoS流绑定 |
| UPF | **执行业务数据流检测**、统计流量、**执行QoS控制/带宽管理/重定向** |

**图谱落位**：这是访问限制动作从决策到执行的标准链路。PCF决策→SMF翻译→UPF执行。

### KP-03: 三类策略（AM/UE/SM） — ★★★★

> SourcePath: `实现原理/相关概念_72244993.md` §策略

| 策略类型 | 内容项 | 作用 | 访问限制相关性 |
|----------|--------|------|----------------|
| **AM策略**（接入和移动性） | SAR（服务区限制：TAI允许/禁止列表、最大TAI数）；RFSP索引 | 决策接入区域、无线资源管理 | **SAR=接入控制类访问限制** |
| **UE策略**（选网和路由） | ANDSP（WLAN选网）；URSP（切片/SSC/DNN/PDU类型选择） | 辅助UE选网/PDU会话 | 间接（路由限制） |
| **SM策略**（会话管理） | **会话规则**（Session-AMBR/默认QoS/用量监控）+ **PCC规则**（5QI/ARP/SDF模板/计费/策略控制/流量转向） | PDU会话粒度+SDF粒度策略控制 | **★核心★**：访问限制DISCARD/REDIRECT主要通过SM策略的PCC规则实现 |

**SM策略适用范围**：2/3/4/5G用户通用；AM/UE策略仅适用5G。

**策略=触发器+规则**（强约束）。

### KP-04: 三类规则及SMF优先级 — ★★★★★（访问限制规则载体）

> SourcePath: `实现原理/相关概念_72244993.md` §规则

规则=PDR（Packet Detection Rule）=条件（PDI）+动作（PA）。

**规则定义对比表**：

| 规则类别 | PCF | SMF | UPF |
|----------|-----|-----|-----|
| **动态规则** | 定义规则名+内容，下发完整规则给SMF | 透传规则内容给UPF | 按接收规则处理 |
| **预定义规则**（单条） | 定义与SMF一致的规则名，只下发名称 | 定义规则名，透传名称给UPF | **定义具体规则内容**，按名称匹配本地规则 |
| **预定义规则组**（UserProfile） | 定义与SMF UserProfile同名的名称 | 定义UserProfile名+多条规则绑定 | **定义规则内容**，按UserProfile匹配本地规则，按UserProfile内优先级处理 |
| **本地规则** | 与PCF无关 | 定义UserProfile名，下发名称给UPF | **定义规则内容**，按UserProfile匹配 |

**SMF规则优先级（同优先级时）**：**动态规则 > 预定义规则 > 本地规则**

**规则优先级值**：值越小，优先级越高。

**关键观察**：UPF在预定义规则/预定义规则组/本地规则三类中都**负责定义具体规则内容**——UPF是访问限制动作配置的真正落地点。

### KP-05: 规则动作（PA）枚举 — ★★★★★（访问限制动作清单权威定义）

> SourcePath: `实现原理/相关概念_72244993.md` §动作

**动作（PA, Packet Action）包括 FAR（Forwarding Action Rule）、URR（Usage Reporting Rule）、QER（QoS Enforcement Rule）等。**

**动作明确枚举**：
> 动作包括 **QoS控制、计费、带宽管理、重定向、头增强和URL过滤**，触发专有QoS flow（对应4G的专有承载）的建立、修改、删除等。

**访问限制动作清单**（从PCC动作枚举提取）：
| 动作 | 访问限制类别 | 实现机制 |
|------|--------------|----------|
| **重定向** | REDIRECT | FAR动作改写目的地址 |
| **URL过滤** | DISCARD/REDIRECT | 规则匹配URL后执行阻塞或重定向 |
| **QoS控制** | 限速（带宽域） | QER |
| **计费** | 计费域 | URR |
| **带宽管理** | 限速（带宽域） | QER/带宽分类 |
| **头增强** | 头增强域 | FAR插入字段 |

**关键发现**：**重定向和URL过滤被官方明确列为PCC动作**——证明PCC是访问限制两种核心动作的统一载体。

### KP-06: 12类Event Trigger（规则下发触发器） — ★★★★

> SourcePath: `实现原理/Event Trigger_47013472.md`

**触发器定义PCF决策时机，UPF通过URR上报触发**：

| Event Trigger | 含义 | 关联IE |
|---------------|------|--------|
| **PERIO** | 周期性上报 | Measurement Period |
| **VOLTH** | 流量阈值 | Volume Threshold |
| **TIMTH** | 时长阈值 | Time Threshold |
| **QUHTI** | 配额保持时间 | Quota Holding Time |
| **START** | 业务开始 | NA |
| **STOPT** | 业务结束 | NA |
| **DROTH** | 下行丢包阈值 | Dropped DL Traffic Threshold |
| **LIUSA** | 关联URR上报 | Linked URR ID |
| **VOLQU** | 流量配额耗尽 | Volume Quota |
| **TIMQU** | 时长配额耗尽 | Time Quota |
| **ENVCL** | 信封关闭 | NA |
| **MACAR** | MAC地址上报 | NA |
| **EVETH** | 事件阈值 | Event Information |

**访问限制典型触发场景**：
- **VOLQU/TIMQU**：套餐耗尽→触发重定向到充值页（业务5）
- **VOLTH**：流量超限→触发限速（业务6）
- **START/STOPT**：业务开始/结束上报

### KP-07: 2/3/4G vs 5G PCC差异 — ★★★★

> SourcePath: `实现原理/2_3_4_5G PCC功能差异_47013471.md`

| 差异点 | 2/3/4G | 5G |
|--------|--------|-----|
| 关键网元 | AF, SPR, PCRF, PGW(PCEF) | AF, UDR, PCF, AMF, PGW-C/SMF, UPF |
| **接口** | Gx | **N7, N15, N4** |
| 协议 | Diameter Gx | PFCP（N4）+HTTPS（N7/N15） |
| **策略** | 会话管理策略 | **SM策略+AM策略+UE策略**（新增AM/UE） |
| 漫游 | 归属网络生成 | 归属/访问网络均可生成 |
| 主要流程 | IP-CAN会话+专有承载 | **PCF发现选择+AM策略关联+SM策略关联+PFD管理** |
| 规则来源 | PCRF/AAA/本地 | PCF/本地 |
| **规则分类** | 动态/预定义/预定义规则组(本地userprofile) | **动态/预定义（统一4G的预定义规则和预定义规则组）** |

**关键演进**：5G将4G的"预定义规则"和"预定义规则组（本地userprofile）"统一为"预定义规则"——简化配置。

### KP-08: PDU会话三流程 — ★★★★

> SourcePath: `实现原理/业务流程_47013470.md`

| 流程 | 触发 | 关键动作 |
|------|------|----------|
| **PDU会话建立** | 用户注册 | SMF将SDF映射QoS流，N4下发QoS计费策略给UPF建会话；UPF做QFI传输层标记、Session-AMBR控制、流量统计 |
| **PDU会话修改** | 触发器条件（签约/位置变更） | PCF或SMF发起 `Npcf_SMPolicyControl_Update`/`UpdateNotify`；SMF通过N4传更新QoS给UPF |
| **PDU会话释放** | 签约删除/去注册/触发器 | UPF丢弃PDU会话相关数据包，释放N4会话隧道资源和上下文 |

**关键约束**：一条消息中存在对同一预定义rule的安装和删除操作时，**UPF对该rule执行安装操作**。

### KP-09: 动态PCC功能7步配置（MML原样保留） — ★★★★★

> SourcePath: `激活PCC基本功能/配置动态PCC功能_74096530.md`

**配置步骤**（动态PCC + 预定义规则通用）：

1. **打开License开关**
```
SET LICENSESWITCH:LICITEM="LKV3G5PCCB01",SWITCH=ENABLE;
```

2. **配置三四层过滤条件**
```
ADD FILTER: FILTERNAME="filter_test", L34PROTTYPE=STRING, L34PROTOCOL=ANY;
```

3. **配置流过滤器**
```
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_test";
```

4. **绑定过滤器到流过滤器**
```
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",FILTERNAME="filter_test";
```

5. **配置PCC策略组**（计费时需配URRGROUPNAME）
```
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pg_test",URRGROUPNAME="urrgp_test";
```

6. **配置规则**（核心：POLICYTYPE=PCC）
```
ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,
FILTERINGMODE=FLOWFILTER,
FLOWFILTERNAME="flowfilter_test",PRIORITY=65535, POLICYNAME="pg_test";
```

7. **配置UserProfile + 规则绑定**
```
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
```

8. **刷新生效**（必须最后执行）
```
SET REFRESHSRV:REFRESHTYPE=ALL;
```

**配置对象关系链**：FILTER → FLOWFILTER（via FLTBINDFLOWF）→ RULE（POLICYTYPE=PCC, POLICYNAME=PCCPOLICYGRP）→ USERPROFILE（via RULEBINDING）

**关键约束**：
- 流过滤器**必须至少绑定一个filter或一个l7filter**，否则所有报文都匹配不上
- 规则RULENAME+策略类型POLICYTYPE唯一标识一条rule
- UPF与SMF上UserProfile名称必须一致（预定义规则组/本地规则）
- UPF与SMF上规则名称必须一致（预定义规则）
- UPF与SMF上URR标识必须一致（同一rule）

### KP-10: 本地PCC功能（无PCF兜底） — ★★★★

> SourcePath: `激活PCC基本功能/配置本地PCC功能_74096529.md`

**适用场景**：网络中无PCRF/PCF，通过特定APN激活的用户需PCC功能。

**机制**：UPF/SMF上定义相同的**UserProfile名称**，UPF定义规则内容+动作；SMF下发UserProfile名称激活UPF本地静态配置的规则。

**关键限制**：**SMF不支持实时更新本地规则**——新增绑定规则不会实时生效，需用户下次上线才生效。

**MML配置与动态PCC完全相同**（步骤2-8）。

**本地规则触发场景**：
- 现网未部署PCF
- SMF未开启PCC功能开关
- SMF与PCF链路故障
- PCF签约异常
- PCF下发策略异常（且SMF配置了回滚为本地PCC用户）

### KP-11: PCC调测方法 — ★★★

> SourcePath: `调测PCC基本功能_42369277.md`

**验证方法**：在UPF上跟踪用户消息，检查：
1. **N4接口PFCP Session Establishment Request**消息存在
2. 激活响应 **PFCP Session Establishment Response** 返回码 **Cause = request-accepted (1)**

**SMF通过N4向UPF下发**：PDR/FAR/QER/URR等信息。

**LST验证命令集**：
- LST USERPROFILE / LST RULEBINDING / LST RULE
- LST FLOWFILTER / LST FLTBINDFLOWF / LST FILTER / LST PROTBINDFLOWF / LST L7FILTER
- LST PCCPOLICYGRP / LST URRGROUP / LST URR

### KP-12: PCC核心MML命令清单 — ★★★★★

> SourcePath: `GWFD-020351 PCC基本功能参考信息_79592737.md`

| 命令 | 用途 | 访问限制相关性 |
|------|------|----------------|
| **ADD PCCPOLICYGRP** | 增加PCC策略组 | ★★★★★ PCC动作载体 |
| **ADD RULE** | 增加规则（含POLICYTYPE=PCC） | ★★★★★ 规则定义 |
| **ADD FLOWFILTER** | 增加流过滤器 | ★★★★★ 过滤条件容器 |
| **ADD FILTER** | 增加过滤器（三四层） | ★★★★ IP/端口过滤 |
| **ADD USERPROFILE** | 增加用户模板 | ★★★★ 规则组容器 |
| **ADD RULEBINDING** | 增加规则与用户模板绑定 | ★★★★ 规则激活 |
| **ADD QOSPROP** | 增加QoS属性 | ★★ QoS配置 |
| **ADD FLTBINDFLOWF** | 增加流过滤器与过滤器绑定 | ★★★★ 过滤条件组装 |
| **ADD URRGROUP** | 增加URR组（计费属性） | ★★ 计费配置 |
| **SET REFRESHSRV** | 业务刷新（置生效） | ★★★★★ 配置生效必需 |
| **SET LICENSESWITCH** | License开关 | ★★★★★ 启用前置 |

**软参**：`BIT440` 控制动态业务签约场景service-property匹配失败时的报文动作。

### KP-13: 静态规则=预定义+本地（动态规则不支持七层） — ★★★★★（访问限制核心约束）

> SourcePath: `何为PCC静态规则——What？_86169704.md` + `使用PCC静态规则——Why？_32946325.md`

**静态规则定义**：预定义规则+本地规则统称静态规则。规则内容（流匹配条件+动作）**提前在UPF上配置**，非PCF动态生成。用户注册时PCF/SMF下发规则名称激活。

**策略决策者**：
- 预定义规则：**PCF**决策
- 本地规则：**SMF**决策
- UPF：负责执行

**★关键约束★：动态规则不支持七层特征**

> 由于**PCF不具备通过七层协议（例如HTTP协议特征+URL "http://www.example.com"）识别业务的能力**，而UPF具备该能力。因此，对于需要对特定业务类型（如A视频业务，七层协议识别）进行计费控制和带宽控制等，**必须通过UPF上的静态规则来实现**。

**UPF支持的流条件**：
- 三四层特征：IP、Port、三四层协议
- **七层特征：URL、HOST、七层协议**
- 组合：三四层any+特定七层 / 特定三四层+特定七层 / 特定三四层 / 三四层any+七层any

**UPF支持的流动作**：计费、带宽管理、**头增强**、QoS等；支持单动作或组合动作（如计费+FUP）。

**结论对访问限制图谱**：**基于URL的访问限制（URL过滤）必须用静态规则实现**，不能用动态规则。

### KP-14: 静态规则6规则完整示例（A视频精细化） — ★★★★

> SourcePath: `PCC静态规则原理——How？_86009740.md`

**业务套餐**（20G通用+30G A视频专项）：

| 套餐 | 业务 | 流匹配 | 策略类型 | 规则 | 优先级 |
|------|------|--------|----------|------|--------|
| 1 | A视频 | URL:www.example.com+HTTP | PCC（专项流量） | Prerule01 | 高 |
| 2 | A视频 | URL:www.example.com+HTTP | BWM（100Mbps） | Prerule02 | 高 |
| 2' | A视频 | URL:www.example.com+HTTP | BWM（25Mbps，超2000M） | Prerule03 | 高 |
| 3 | 通用 | 三四层any+七层any | PCC（通用流量） | Prerule04 | 较高 |
| 4 | 通用 | 三四层any+七层any | BWM（50Mbps） | Prerule05 | 较高 |
| 4' | 通用 | 三四层any+七层any | BWM（1Mbps，超20G） | Prerule06 | 较高 |

**PCF/SMF/UPF三网元参数规划原则**：
- 同一预定义规则：**PCF/SMF/UPF上规则名称必须一致**
- 同一预定义规则：**SMF/UPF上URR ID必须一致**

**规则安装流程**（PDU会话建立时）：
1. 用户开机发起PDU会话创建请求
2. SMF选择PCF，建立SM策略偶联，获取SM策略
3. PCF决策生成规则，下发预定义规则名称（Prerule01/02/04/05）+动态规则+Triggers
4. SMF选择UPF，发起会话建立请求（携带预定义规则名称等）
5. UPF安装预定义规则+动态规则，返回响应
6. UPF对数据报文做业务识别，匹配Filter/L7filter，按规则动作处理

**规则更新流程**（流量累计达阈值）：
- PCF更新规则（删除Prerule02，安装Prerule03）
- SMF/UPF删除旧规则，安装新规则
- 后续报文按新规则处理

## 3. 关键发现（跨文档归纳的隐性规则/约束）

### 发现-1: PCC动作官方枚举含"重定向"和"URL过滤"（第4层动作对象权威来源）
`相关概念_72244993.md` 明确："动作包括QoS控制、计费、带宽管理、**重定向、头增强和URL过滤**"。这6类动作是访问限制场景第4层（命令/配置对象层）动作对象的**权威分类基础**。

### 发现-2: 动态规则无法识别七层业务（URL过滤必须用静态规则）
PCF不具备七层识别能力，UPF具备。因此：
- **URL过滤特性→必须配置预定义规则或本地规则**
- 动态规则只能做三四层（IP/端口）和协议级控制
- **图谱落位**：URL过滤类特性（GWFD-110471）的规则类型应为"预定义规则"

### 发现-3: 三类规则的SMF优先级顺序固定（动态>预定义>本地）
SMF处理同优先级规则时，**动态规则优先于预定义规则优先于本地规则**。这意味着：
- 若动态规则和预定义规则冲突，动态规则胜出
- 本地规则是最低优先级的兜底方案
- **图谱落位**：规则冲突解决机制的优先级依据

### 发现-4: UPF是访问限制动作配置的真正落地点
预定义规则/预定义规则组/本地规则三类中，**UPF都负责定义具体规则内容和动作**。PCF/SMF只下发规则名称或UserProfile名称。这意味着：
- 访问限制的MML配置（ADD RULE + ADD FLOWFILTER + ADD PCCPOLICYGRP）主要在UPF侧执行
- **图谱落位**：第4层命令对象主要挂在UPF网元下

### 发现-5: PCCPOLICYGRP是PCC动作的核心容器对象
ADD RULE 的 POLICYNAME 指向 PCCPOLICYGRP，PCCPOLICYGRP 关联 URRGROUP（计费）。访问限制动作配置链：
**RULE (POLICYTYPE=PCC) → PCCPOLICYGRP → URRGROUP（可选计费）**
PCCPOLICYGRP是访问限制动作的"策略组"容器，是第4层关键对象。

### 发现-6: 配置对象四元组（RULE+FLOWFILTER+USERPROFILE+PCCPOLICYGRP）构成完整PCC配置
访问限制完整配置需4类对象协作：
- **FLOWFILTER**（+FILTER/L7FILTER）：定义"匹配什么流量"
- **RULE**（POLICYTYPE=PCC）：定义"匹配后做什么"，关联PCCPOLICYGRP
- **USERPROFILE**：定义"对哪个用户生效"，通过RULEBINDING绑定RULE
- **PCCPOLICYGRP**：定义"具体策略参数"，关联URRGROUP

**图谱落位**：第4层ConfigObject应包含这4类对象及其关系边。

### 发现-7: 5G统一了4G的预定义规则和预定义规则组（架构简化）
5G PCC将4G的"预定义规则"和"预定义规则组（本地userprofile）"统一为"预定义规则"——UPF既可以匹配单条预定义规则，也可以匹配UserProfile（一组规则）。**图谱落位**：5G场景下规则对象模型比4G简化。

### 发现-8: AM策略的SAR（服务区限制）是接入控制类访问限制
AM策略包含SAR（Service Area Restrictions）：UE允许接入的TAI列表、不允许接入的TAI列表、最大允许接入TAI数。这是**基于位置的接入控制**，属于访问限制的"接入控制"子类。**图谱落位**：WSFD-211001（基于初始接入位置的策略控制）特性应关联AM策略/SAR对象。

### 发现-9: 规则=触发器+规则（策略组成的强约束）
原文明确："策略由触发器和规则组成"。意味着任何PCC策略下发都必须有触发器事件驱动。访问限制动作的下发也不例外——必须有Event Trigger（如VOLQU套餐耗尽）触发PCF决策。**图谱落位**：业务层策略下发决策点应关联触发器对象。

### 发现-10: 本地规则不可实时更新（容灾约束）
SMF本地规则不支持实时更新，新增绑定规则需用户下次上线才生效。这意味着本地规则作为访问限制兜底方案时，**规则变更不灵活**，适合静态访问控制策略。**图谱落位**：本地规则对象的"可变性"属性应为"静态"。

---

**涉及的配置对象（供第4层图谱引用）**：
- **PCCPOLICYGRP**（PCC策略组，动作载体容器）
- **RULE**（规则，POLICYTYPE=PCC时承载访问限制动作）
- **FLOWFILTER**（流过滤器，过滤条件容器）
- **FILTER**（三四层过滤器）
- **L7FILTER**（七层过滤器，URL过滤核心）
- **USERPROFILE**（用户模板，规则组容器）
- **RULEBINDING**（规则-用户模板绑定）
- **FLTBINDFLOWF**（流过滤器-过滤器绑定）
- **URRGROUP / URR**（计费相关）
- **QOSPROP**（QoS属性）

**涉及的MML命令（原样保留）**：
SET LICENSESWITCH, ADD FILTER, ADD FLOWFILTER, ADD FLTBINDFLOWF, ADD PCCPOLICYGRP, ADD RULE, ADD USERPROFILE, ADD RULEBINDING, SET REFRESHSRV, LST *, EXP MML

**涉及的信令接口**：N7（PCF↔SMF）、N15（AMF↔PCF）、N4（SMF↔UPF，PFCP协议）、Gx（4G遗留）
