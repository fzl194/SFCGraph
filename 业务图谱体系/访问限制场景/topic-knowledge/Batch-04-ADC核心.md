# Batch-04: ADC 核心机制

> 批次 04 | 主题：增强的ADC检测与上报机制 | 来源：GWFD-020357 feature-knowledge + 特性原始文档 | 特性数 1 | 核心度 ★★★★★（场景基石）

---

## 1. 概述

ADC（Application Detection and Control，应用检测与控制）是访问限制场景的**应用层感知基石**。PCC基本功能只能对 L3/L4 进行动态控制，无法对 L7 业务动态控制；ADC 补齐了这一短板，使 PCRF/PCF 能感知"用户在用什么应用"，并据此下发访问限制/重定向/QoS 策略。

ADC 本身**不直接产生访问限制动作**，它是**检测与上报层**——UDG 检测应用、上报应用标识/事件给 PCRF/PCF，由 PCRF/PCF 下发携带 Application ID 的 PCC 规则触发后续动作（阻塞、重定向、头增强前置解析等）。

**关键定位**：
- 访问限制场景的"**眼睛**"：负责 L7 应用识别
- 其他访问限制特性的**共同前置**：头增强、HTTP智能重定向、用户Portal、URL过滤均需基于 ADC/SA 的应用解析能力

---

## 2. 核心知识点（KP）

### KP-1 ADC 的两种事件类型（来自 GWFD-020357 §3.2）

| 事件 | 含义 | 上报路径 | 触发后续动作 |
|------|------|----------|-------------|
| **APPLICATION_START** | 应用数据流开始 | PGW-U/UPF → PGW-C/SMF → PCRF/PCF | PCRF/PCF 下发新 PCC 策略，可能创建专有承载、触发重定向/阻塞 |
| **APPLICATION_STOP** | 应用数据流终止 | 同上 | PCRF/PCF 下发新 PCC 策略，可能去激活专有承载 |

**迟滞控制**：`ADCHYSTTIMER`（0~3600秒）控制应用级上报迟滞，避免频繁上报引起信令风暴。0 = 关闭延迟。

---

### KP-2 ADC 上报静默开关 ADCMUTEFLAG（来自 GWFD-020357 §4.3）

| 取值 | 含义 | 适用场景 |
|------|------|----------|
| DISABLE（默认） | **允许** ADC 上报到 PCRF/PCF | 需要动态 PCC 控制时 |
| ENABLE | **静默**：检测到应用不上报 | 仅本地执行规则，不打扰 PCRF/PCF |

**出现位置**：
- PCCPOLICYGRP（策略组级静默）：`ADD PCCPOLICYGRP:ADCMUTEFLAG=DISABLE,...`
- RULE（规则级静默，POLICYTYPE=ADC）：`ADD RULE:POLICYTYPE=ADC,...,ADCMUTEFLAG=DISABLE`

---

### KP-3 ADC 的两类规则配置方式（来自 GWFD-020357 §4.1）

| 方式 | POLICYTYPE | 动作策略载体 | 触发机制 | 典型场景 |
|------|-----------|-------------|----------|----------|
| 方式A：独立 ADC 规则 | `ADC` | 直接配置在 RULE 上（FLOWFILTER + ADCMUTEFLAG） | UDG 本地策略 | 不需要 PCRF/PCF 介入的本地应用检测 |
| 方式B：复用 PCC 规则 | `PCC`（携带 Application ID） | PCCPOLICYGRP + URRGROUP | PCRF/PCF 下发 TDF-Application-Identifier | 动态 PCC，PCRF/PCF 决策 |

**两方式可共存**：同一 RULE 可同时配置 `POLICYTYPE=ADC` 和 `POLICYTYPE=PCC` 两条记录，共享 FLOWFILTER。

---

### KP-4 流信息上报开关 FLOWINFORPT（来自 GWFD-020357 §4.3）

| 取值 | 含义 | 上报内容 |
|------|------|----------|
| ENABLE | 上报流信息 | 五元组等 flow 信息一并上送到 PCRF/PCF |
| DISABLE | 仅上报应用标识 | 仅 Application Identifier |

配置对象：`ADCPARA`（`ADD ADCPARA:FLOWFILTERNAME=...,FLOWINFORPT=ENABLE,ADCHYSTTIMER=0`）

---

### KP-5 ADC 规则匹配的优先级原则（来自 GWFD-020357 §3.3）

1. 预定义规则 < 动态规则 < 携带 Application ID 的动态规则（全局优先级相同时）
2. `TDF-Application-Identifier AVP`（PCRF/PCF 下发）映射到本地配置的 FlowFilter
3. **兜底阻塞**：业务流匹配不上所有规则时，**UDG 阻塞当前业务流** → 这是 ADC 提供访问限制"DISCARD"动作的底层机制
4. 建议配置 L3/4=any、L7=any 的缺省规则避免误阻塞

---

### KP-6 ADC 的应用分类（来自 GWFD-020357 §3.1）

| 应用类型 | 流特征 | 上报策略建议 |
|---------|--------|-------------|
| **可推论业务** | 流信息可识别、持续时间长（≥3分钟）、并发流少（≤16个） | 适合上报完整 flow 信息（FTP、RTSP） |
| **不可推论业务** | 五元组老化快、并发流多 | 不适合上报 flow 信息（P2P、HTTP） |
| **自营业务** | 运营商提供（VoIP、视频、文件传输） | 高价值业务，适合专有承载 QoS 保障 |

---

## 3. 关键发现（跨特性横向归纳）

### 发现-1 ADC 是访问限制场景的"应用感知层"——所有 L7 动作的共同前置

ADC 提供的不是"动作"，而是"**看见**"。访问限制场景中，**所有需要基于应用/URL 做判断的特性都依赖 ADC/SA 的解析能力**：

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

**对图谱第 1 层（BusinessRule）的启示**：ADC 应建模为一条横切依赖关系——"访问限制场景中的所有 L7 动作特性 constrained_by ADC/SA 解析能力"。

---

### 发现-2 ADC 触发访问限制的两种链路

**链路 A：本地 ADC 规则直接触发**（POLICYTYPE=ADC）
- UDG 本地配置 RULE，匹配后直接执行 ADCMUTEFLAG/动作
- 不经过 PCRF/PCF，时延低，适合静态策略

**链路 B：PCRF/PCF 动态决策**（POLICYTYPE=PCC + Application ID）
- UDG 检测到应用 → 上报 APPLICATION_START → PCRF/PCF 决策 → 下发新 PCC 规则
- 触发的动作可以是阻塞、重定向、专有承载
- 时延较高（涉及 N7/N4 信令），适合动态个性化策略

**对图谱第 4 层（ConfigObject）的启示**：ADC 是少数能在**两条链路上同时出现**的特性，需要为 ADC 建立两个 ConfigObject 复用模板。

---

### 发现-3 ADC 的 ConfigObject 复用矩阵

| ConfigObject | 在 ADC 中的角色 | 复用情况 |
|--------------|----------------|---------|
| **FILTER + FLOWFILTER + FLTBINDFLOWF** | 三四层匹配条件 | **场景级共用**（所有访问限制特性都用这条链） |
| **L7FILTER + PROTBINDFLOWF** | 七层 URL 匹配 | ADC、HTTP头防欺诈、头增强共用 |
| **ADCPARA** | ADC 专属：流信息上报、迟滞定时器 | ADC 独有 |
| **URR + URRGROUP** | 使用量上报规则 | 与计费、带宽控制、URL过滤共用 |
| **PCCPOLICYGRP**（含 ADCMUTEFLAG） | PCC 策略组 + ADC 静默开关 | ADC 独有的 ADCMUTEFLAG 参数；其他特性复用 PCCPOLICYGRP 时不带此参数 |
| **RULE**（POLICYTYPE=ADC/PCC） | 规则载体 | **场景级共用**，POLICYTYPE 是关键差异化参数 |
| **USERPROFILE + RULEBINDING** | 用户模板与规则绑定 | **场景级共用** |

**核心 MML 命令复用**（与场景内其他特性共用）：
- `ADD FILTER` / `ADD FLOWFILTER` / `ADD FLTBINDFLOWF` / `SET REFRESHSRV`
- `ADD L7FILTER` / `ADD PROTBINDFLOWF`
- `ADD URR` / `ADD URRGROUP` / `ADD PCCPOLICYGRP`
- `ADD RULE` / `ADD USERPROFILE` / `ADD RULEBINDING`

**ADC 独有命令**：
- `ADD ADCPARA`（流信息上报开关、迟滞定时器）

---

### 发现-4 ADC 上报对系统与信令的影响（性能权衡）

ADC 使能后会对所有业务进行 L7 解析，带来三类影响（来自 GWFD-020357 §3.4）：
1. **数据面性能下降**：报文转发性能和吞吐量下降
2. **N4/N7 接口信令增多**：APPLICATION_START/STOP 上报
3. **GnGp/S11/S5/S8 接口 GTP 信令增多**：承载更新触发

**对业务设计的启示**：大规模部署 ADC 时应配合 `ADCHYSTTIMER` 控制上报频率，避免信令风暴；对不需要 PCRF/PCF 介入的应用使用 `ADCMUTEFLAG=ENABLE` 静默。

---

### 发现-5 ADC 映射到访问限制三种动作

| 访问限制动作 | ADC 如何贡献 | 说明 |
|-------------|-------------|------|
| **DISCARD（阻塞）** | 兜底阻塞机制：规则匹配不上时 UDG 阻塞业务流 | 最直接的访问限制动作，ADC 的隐式阻塞能力 |
| **HEADEN（头增强）** | 提供 HTTP/HTTPS/RTSP 报文解析能力，使头增强能匹配到规则 | 间接贡献：是头增强的前置依赖 |
| **REDIRECT（重定向）** | 通过 PCRF/PCF 下发的 PCC 策略触发页面重定向（如未签约业务提醒页） | 经典 ADC 重定向场景：未签约 → 重定向到订购页 |

---

## 4. 配置对象/命令复用清单

### ADC 独有配置对象
- `ADCPARA`：ADC 流信息上报开关 + 迟滞定时器

### ADC 独有 MML 命令
- `ADD ADCPARA`

### ADC 与场景内其他特性共用的配置对象（场景级通用链）
- 三四层：`FILTER` → `FLOWFILTER` → `FLTBINDFLOWF`
- 七层：`L7FILTER` → `PROTBINDFLOWF`
- 策略载体：`URR` → `URRGROUP` → `PCCPOLICYGRP`（ADC 使用 `ADCMUTEFLAG` 参数）
- 规则绑定：`RULE`（ADC 用 `POLICYTYPE=ADC` 或 `PCC`） → `USERPROFILE` → `RULEBINDING`

### License
- `82200AFK LKV3G5ADCF01 增强的ADC基本功能`
- 依赖：SA-Basic（82209749）、PCC基本功能（82209825）

---

## 5. 来源

- 主：`feature-knowledge/GWFD-020357-增强的ADC基本功能.md`
- 原始：`GWFD-020357 增强的ADC基本功能特性概述_84866818.md` 等 5 篇
- 跨特性引用：访问限制场景全部 11 个特性的 feature-knowledge 中"前置依赖"部分均提到 ADC/SA
