# 访问限制场景 — 跨主题综合分析

> 本文档基于 8 个主题知识批次（Batch-01 ~ Batch-08）共约 117 份源文档（UDG 特性指南 + UNC 特性指南 + 一望5G 业务专题）的横向综合分析，覆盖 UDG（用户面）与 UNC（控制面）两大产品线。
> 分析目标是提炼跨主题共性机制、揭示隐藏依赖关系（尤其是双轨动作机制）、建立访问限制的全景知识地图。
> 本文档是三层图谱第 1 层（业务层：方案闭包 CS / 决策点 DP / 共性机制 SemanticObject）的**主数据源**。

---

## 1. 概述

### 1.1 场景定位

访问限制（Access Control）是业务感知（SA）的第 3 个子场景（套餐 3），与计费场景（套餐 1）、带宽控制场景（套餐 2）共享 SA 基础设施（规则匹配引擎、业务识别框架、PCC 策略体系）。本场景的核心目标是：**对用户访问网络/业务/内容的请求，根据用户身份、位置、套餐配额、应用类型、URL 分类、接入网元等维度，进行阻塞（DISCARD）、头增强（HEADEN）、重定向（REDIRECT）以及 URL 过滤（BLOCK/PERMIT/REDIRECT）的差异化控制**。

访问限制的本质是 SA 的"安全防护"领域实现（Batch-01 KP-02）：业务感知提供过滤、管理 UPF 承载的数据面流量的能力，一定程度上避免用户遭受来自不安全数据中心或不法分子的恶意攻击行为，保护用户正常业务和计费。

### 1.2 文档范围

| 维度 | 覆盖内容 |
|------|----------|
| 产品 | UDG（用户面，Batch-01/02/04/05/06/07/08）、UNC（控制面，Batch-03/07） |
| 主题 | SA 基础、PCC 基本功能、SM 策略下发、ADC、头增强族、重定向族、URL 过滤与接入控制、防欺诈 |
| 源文档数 | 约 117 份原始产品文档（8 批次） |
| 批次数 | 8 个主题知识批次 |
| 核心特性 | 11 个特性（UDG 10 + UNC 1），其中 GWFD 系列 9 个、WSFD 系列 2 个 |

### 1.3 三大动作类别

访问限制场景所有动作可归纳为三大类（Batch-01 KP-05、Batch-02 KP-05）：

| 动作类别 | 含义 | 实现载体 | 典型特性 |
|----------|------|----------|----------|
| **DISCARD（阻塞）** | 丢弃用户报文，禁止访问 | PCC 兜底阻塞、ADC 兜底阻塞、URL 过滤 BLOCK、Portal 全 DOWN 时 BLOCK | ADC、URL 过滤 |
| **HEADEN（头增强）** | 在请求报文头插入运营商规划字段 | HEADEN 对象（ADD HEADEN） | HTTP/HTTPS/RTSP 头增强、HTTP 头防欺诈 |
| **REDIRECT（重定向）** | 将用户访问引导到指定服务器/页面 | FAR 改写、IP NAT、DNS 重写、HTTP 响应改写 | HTTP 智能重定向、DNS 纠错、用户 Portal、WebProxy |
| **PERMIT（放行）** | 显式允许通过（URL 过滤独有） | CFTEMPLATE.ACTION=PERMIT | URL 过滤 |

### 1.4 分析方法论

本文档采用**横向综合分析**方法，不同于按批次顺序的文档摘要。核心分析视角包括：
- **跨产品视角**：同一概念在 UDG（用户面执行体）与 UNC（控制面决策体）中的不同角色
- **跨主题视角**：SA、PCC、ADC、头增强、重定向、URL 过滤、防欺诈之间的交叉点与协同机制
- **双轨视角**：PCC 体系（轨道 A）与 URL 过滤体系（轨道 B）的对比与协同（本场景最关键的架构事实）
- **配置实证视角**：从 MML 命令、参数体系、信令流程提取可验证的技术事实
- **方案闭包视角**：按"动作机制/触发维度"归纳访问限制的完整业务方案

---

## 2. 主题分类与知识地图

### 2.1 五大主题集群

8 个批次可归纳为五大主题集群，每个集群在访问限制场景中承担不同职责：

| 主题集群 | 批次范围 | 核心职责 | 与访问限制的关系 |
|----------|----------|----------|------------------|
| SA/PCC 基础设施 | Batch-01（SA）、Batch-02（PCC UDG）、Batch-03（PCC UNC） | 提供规则匹配引擎、策略下发链路、规则类型体系 | **基础层**：所有访问限制特性的统一执行框架 |
| 应用检测层 | Batch-04（ADC） | L7 应用识别与上报，提供应用感知能力 | **眼睛**：所有 L7 动作的前置依赖 |
| 信息插入层 | Batch-05（头增强）、Batch-08（防欺诈） | 报文头字段插入与安全增强 | **带内信息传递**：支持业务认证与防欺诈 |
| 重定向族 | Batch-06（HTTP/DNS/Portal/WebProxy） | 多层级 REDIRECT 实现 | **引导层**：把用户引导到指定服务器/页面 |
| URL 过滤与接入控制 | Batch-07（URL 过滤 + UNC 接入控制 + 位置触发） | 基于 URL 分类的独立动作体系 + UNC 侧粗粒度接入控制 | **第二轨道 + 粗粒度前置**：外部数据库驱动 + 注册阶段控制 |

### 2.2 知识维度矩阵

从知识类型维度划分：

| 知识类型 | 代表批次 | 典型内容 |
|----------|----------|----------|
| 概念定义 | Batch-01、Batch-02 | SA 定义、5 种策略类型、3 种规则类型、3 种动作类型 |
| 原理机制 | Batch-01、Batch-02、Batch-03 | SA 七步流程、PCC N7→N4 下发链路、三类规则生命周期 |
| 配置规则 | Batch-02、Batch-04、Batch-05、Batch-06、Batch-07、Batch-08 | 7 步 MML 配置、HEADEN 共用命令、IP Farm 机制、双轨动作机制 |
| 流程信令 | Batch-01、Batch-02、Batch-03 | SA 七步、N7/N4 信令、PCR Trigger（5 AMF + 24 SMF） |
| 约束条件 | Batch-01、Batch-02、Batch-03、Batch-04 | 动态规则无 L7 能力、三网元一致性、License 门控、HTTPS 加密限制 |
| 调测方法 | Batch-02、Batch-03 | N4 PFCP Session Establishment 验证、DSP/LST 命令集 |
| 方案案例 | Batch-01、Batch-03、Batch-07 | 七业务套餐示例、重定向两大场景、URL 过滤 ICAP 交互 |

### 2.3 UDG vs UNC 视角分工

| 对比维度 | UDG（Batch-01/02/04/05/06/07/08） | UNC（Batch-03/07） |
|----------|-------------------------------------|---------------------|
| 网元角色 | UPF/PGW-U（执行体） | SMF/PGW-C/AMF（控制体）+ PCF（决策体） |
| 核心关注 | 报文解析、规则匹配、动作执行 | 策略决策、信令映射、位置触发 |
| 配置入口 | ADD RULE/FLOWFILTER/HEADEN/SMARTHTTPREDIR/CFTEMPLATE | ADD PCCPOLICYGRP/RULE/USERPROFILE/USRLOCATION |
| 动作视角 | 执行 DISCARD/HEADEN/REDIRECT/BLOCK/PERMIT | 决策重定向/URL 过滤/接入控制策略 |
| 接入控制 | 业务流阶段细粒度控制 | 注册/会话阶段粗粒度控制（SAR/ODB/区域） |
| URL 过滤 | 与 ICAP Server 协同执行 BLOCK/PERMIT/REDIRECT | 不直接处理 URL，但下发策略 |

### 2.4 主题知识地图（全景）

```
                         ┌─────────────────────────────────────┐
                         │  业务感知 SA 基础（Batch-01）        │
                         │  - 七步流程通用引擎                  │
                         │  - 5 种策略类型（PCC/BWM/HEADEN/      │
                         │    WEBPROXY/SMARTREDIRECT）          │
                         │  - 3 种规则类型（动态/预定义/本地）   │
                         │  - 规则匹配三原则                    │
                         └─────────────┬───────────────────────┘
                                       │ 提供执行框架
                                       ▼
        ┌──────────────────────────────────────────────────────────┐
        │  PCC 基本功能（Batch-02 UDG + Batch-03 UNC）              │
        │  - DISCARD/REDIRECT 动作载体（PCC 双动作）                │
        │  - N7→N4 下发链路                                        │
        │  - 三类规则 + 12/29 类 Event Trigger                      │
        │  - SM 策略三内容：QoS + 计费 + 短信或重定向               │
        │  - UPCF 动作组：带宽控制 + 计费控制 + 消息通知 + 重定向   │
        └─────────────┬────────────────────────────────────┬───────┘
                      │                                    │
                      ▼                                    ▼
   ┌──────────────────────────────┐   ┌─────────────────────────────────┐
   │  轨道 A：PCC 体系             │   │  轨道 B：URL 过滤体系（独立）   │
   │  RULE.POLICYTYPE 驱动         │   │  CFTEMPLATE/CONTCATEGBIND.ACTION│
   ├──────────────────────────────┤   ├─────────────────────────────────┤
   │ ADC（Batch-04）应用检测       │   │ URL 过滤（Batch-07）            │
   │ 头增强族（Batch-05）          │   │  - ICAP Server 协同             │
   │ 防欺诈（Batch-08）            │   │  - 显式 BLOCK/PERMIT/REDIRECT   │
   │ 重定向族（Batch-06）          │   │  - 独立配置体系                 │
   │  - HTTP 智能重定向            │   └─────────────────────────────────┘
   │  - DNS 纠错                   │
   │  - 用户 Portal                │   ┌─────────────────────────────────┐
   │  - WebProxy                   │   │  UNC 接入控制（Batch-07）       │
   └──────────────────────────────┘   │  - 移动接入控制（SAR/ODB/区域） │
                                      │  - 会话接入控制（服务区域限制） │
                                      │  - 位置触发（WSFD-211001）      │
                                      └─────────────────────────────────┘
```

---

## 3. 共性机制分析

### 3.1 SA 七步流程 — 贯穿全场景的通用引擎

SA（业务感知）七步流程是所有访问限制子特性的通用处理引擎（Batch-01 KP-03）：

```
规则下发 → 数据到达 → 业务解析 → 规则匹配 → 策略执行 → 转发处理 → 上报统计
 (PCF→SMF→UPF)  (UE→UPF)   (UPF解析)   (UPF匹配)   (UPF执行)   (UPF→DN)  (UPF→SMF→PCF)
```

**各步骤在访问限制中的语义**：

| Step | 动作 | 访问限制语义 |
|------|------|--------------|
| Step1 规则下发 | PCF 下发规则经 SMF 翻译后到 UPF，存于 UPF 规则库 | **规则是动作的载体**，DISCARD/REDIRECT/BLOCK 绑在规则上 |
| Step2 数据到达 | 用户数据报文经基站到达 UPF | 被检测对象 |
| Step3 解析识别 | UPF 解析报文特征（三四层/协议/七层） | 提取 URL/IP/协议/应用用于匹配 |
| Step4 规则匹配 | 报文特征与规则库匹配（过滤条件+策略+优先级） | 命中阻塞/重定向/头增强/URL 过滤规则 |
| Step5 策略执行 | 成功匹配的报文执行策略：计费、阻塞/重定向、带宽控制、头增强 | **动作执行点** |
| Step6 转发处理 | 用户数据从 UPF 转发到网络/业务服务器 | 重定向时改写目的地址 |
| Step7 上报统计 | UPF 定期向 SMF 上报使用情况 | 触发后续策略变更（如配额耗尽重定向） |

**跨批次一致性验证**：
- Batch-01（UDG 视角）：强调 SA 是"业务识别入口"，解析三层体系（三四层→协议→七层）
- Batch-02（UDG PCC 视角）：强调 Step5 中"重定向、头增强和 URL 过滤"是 PCC 动作官方枚举
- Batch-03（UNC 视角）：强调 Step1 的 PCF→SMF→UPF 控制链路、Step7 的 PCR Trigger 上报

**关键洞察**：访问限制场景的动作在第 5 步"策略执行"中以**类型独立原则**叠加运行（Batch-01 KP-09）。同一条 HTTP 报文可能同时命中 PCC 阻塞规则 + BWM 限速规则 + HEADEN 头增强规则，三类型各至多一条生效，叠加执行。

### 3.2 PCC 规则三类体系 — 跨产品统一框架

三类 PCC 规则（动态、预定义、本地）在 UDG 和 UNC 中均有覆盖（Batch-02 KP-04、Batch-03 KP-08）：

| 规则类型 | 规划位置 | 启用机制 | 访问限制场景 |
|----------|----------|----------|--------------|
| **动态规则** | PCF（不在 UPF/SMF） | 用户接入/会话中，PCF 判断条件满足时通过 N7 下发，**下发即启用** | 按用户条件触发的阻塞/重定向（如配额耗尽重定向） |
| **预定义规则** | UPF + SMF（+ PCF） | 已部署未启用；PCF 通过 `Npcf_SMPolicyControl_Create/UpdateNotify` 通知启用 | **URL 过滤、重定向族的主流方案**（批量预部署） |
| **本地规则** | UPF + SMF | **SMF 找不到 PCF 时**直接下发 | PCF 故障时的应急访问控制（容灾兜底） |

**SMF 处理同优先级规则的固定优先级**（Batch-02 KP-04、Batch-03 KP-08）：
```
动态规则 > 预定义规则 > 本地规则
```

**★ 动态规则的七层限制 ★**（Batch-01 KP-06、Batch-02 KP-13、Batch-03 KP-09 — 重大架构约束）：

> 由于 **PCF 不具备通过七层协议识别业务的能力**（如 HTTP 协议特征+URL `http://www.example.com`），而 UPF 具备该能力。因此，对于需要对特定业务类型（七层协议识别）进行访问限制，**必须通过 UPF 上的静态规则（预定义/本地）来实现**。

这意味着：
- **基于 URL 的访问限制（URL 过滤族）必须用预定义规则或本地规则**
- 动态规则只能做三四层（IP/端口）和协议级控制
- **图谱落位**：URL 过滤类特性（GWFD-110471）的规则类型应标注为"预定义规则"，feature→rule_type 关系需标注此约束

**三网元一致性约束**（Batch-02 KP-14、Batch-03 KP-10）：预定义规则要求 SMF、UPF、PCF 三个网元上的规则定义完全一致，包括：
- 规则名称（同一预定义规则三网元名称必须一致）
- URR ID（SMF/UPF 一致）
- 流量过滤器
- 动作定义

任何不一致都会导致规则激活失败。

### 3.3 规则匹配三原则 — 访问限制命中逻辑

Batch-01 KP-09 定义了规则匹配的三大原则，这些原则在所有访问限制子场景中通用：

1. **优先级原则**：所有报文按规则优先级逐条匹配，值越小优先级越高
2. **全条件原则**：报文必须符合一条规则**所有过滤条件**才算成功匹配
3. **类型独立原则**：**不同类型的规则同时匹配，每种类型至多一条生效**（PCC/BWM/HEADEN 互不干扰）

**两维度匹配模型**：
- 维度一：不同类型规则之间匹配**独立进行**（PCC/BWM/HEADEN 互不干扰）
- 维度二：同类型规则之间按优先级先后匹配，直到有一条匹配成功或全部失败

**访问限制典型匹配结果**（Batch-01 KP-10 示例）：一条 HTTP 访问 10.11.12.13 的报文可能同时命中：
- PCC 规则 3（阻塞，最高优先级）→ DISCARD
- BWM 规则 6（限速）
- HEADEN 规则 7（插 MSISDN+防欺诈）

三类型各至多一条，叠加执行。

**关键约束：一条规则只能绑定一条策略**（Batch-01 发现-6）：规则与策略是 1:1 关系，策略与动作类型是 1:1 关系。若要同一流量同时执行阻塞和重定向，**不能用一条规则**，必须通过两条不同优先级的规则分别承载。**图谱落位**：Rule→Policy 是单向 1:1 边，非多对多。

### 3.4 PCC 动作官方枚举 — 第 4 层动作对象权威来源

Batch-02 KP-05 给出了 PCC 动作的官方枚举（来自 `相关概念_72244993.md` §动作）：

> 动作（PA, Packet Action）包括 FAR（Forwarding Action Rule）、URR（Usage Reporting Rule）、QER（QoS Enforcement Rule）等。
> **动作包括 QoS 控制、计费、带宽管理、重定向、头增强和 URL 过滤**，触发专有 QoS flow 的建立、修改、删除等。

**访问限制动作清单**（从 PCC 动作枚举提取）：

| 动作 | 访问限制类别 | 实现机制 | 典型特性 |
|------|--------------|----------|----------|
| **重定向** | REDIRECT | FAR 动作改写目的地址 | HTTP 智能重定向、DNS 纠错、用户 Portal、WebProxy |
| **URL 过滤** | DISCARD/REDIRECT/PERMIT | 规则匹配 URL 后执行 | URL 过滤（BLOCK/PERMIT/REDIRECT） |
| **头增强** | HEADEN | FAR 插入字段 | HTTP/HTTPS/RTSP 头增强 |
| QoS 控制 | 限速（带宽域） | QER | 带宽控制（非访问限制） |
| 计费 | 计费域 | URR | 计费场景 |
| 带宽管理 | 限速（带宽域） | QER/带宽分类 | 带宽控制 |

**Batch-03 KP-07 进一步给出 UPCF 动作组官方枚举**（PCF 策略层）：
> 动作是规则中配置的操作，包括带宽控制、计费控制、**消息通知**和**重定向**等。特别是"重定向：套餐耗尽后，禁止上网，重定向到运营商充值首页"。

**关键发现**：**重定向和 URL 过滤被官方明确列为 PCC 动作**，证明 PCC 是访问限制两种核心动作（DISCARD/REDIRECT）的统一载体；同时头增强也是 PCC 动作之一。这 6 类动作是访问限制场景第 4 层（命令/配置对象层）动作对象的**权威分类基础**。

### 3.5 5 种策略类型 — 访问限制动作清单（SA 层定义）

Batch-01 KP-05 定义了 SA 的 5 种策略类型，这是访问限制动作的完整清单（SA 层定义）：

| 策略类型 | 含义 | 访问限制动作 | 核心度 | RULE POLICYTYPE |
|----------|------|--------------|--------|-----------------|
| **PCC** | 计费与策略控制；可配置 PCC 策略实现**计费**和**禁止访问/重定向** | DISCARD（阻塞）、REDIRECT（重定向） | ★★★★★ | PCC |
| **BWM** | 带宽管理；分类结果用于带宽策略匹配 | 限速（非访问限制，属带宽域） | ★★ | BWM |
| **HEADEN** | 头增强；向 HTTP/RTSP 请求报文头域**插入字段** | 头增强（HTTP 头增强防欺诈） | ★★★★ | HEADEN |
| **WEBPROXY** | Web Proxy；配置 IPFarm 对象名，设置 WebProxy 选择的服务器**地址池** | Web 代理访问控制 | ★★★★ | WEBPROXY |
| **SMARTREDIRECT** | 智能重定向；配置 CaptivePortal 的 IPFarm 名、HTTP 智能重定向名、**DNS 重写动作**名 | 重定向族（Portal/HTTP/DNS 三类） | ★★★★★ | SMARTREDIRECT |

**规则命名规则**：按绑定策略分类→PCC 规则、BWM 规则、HEADEN 规则等。这种"用策略类型对规则分类"是访问限制特性的组织主线。

**关键观察**：
- PCC 是 DISCARD/REDIRECT 双动作的统一载体（Batch-01 KP-10 业务 3 阻塞 + 业务 5 重定向都属于 PCC）
- SMARTREDIRECT 是 Portal/HTTP 智能重定向/DNS 重写三类重定向的策略类型（Batch-06 KP-3 进一步验证：HTTP 重定向与 DNS 纠错共用 POLICYTYPE=SMARTREDIRECT）
- HEADEN 是头增强族的统一策略类型（Batch-05 KP-1）
- WEBPROXY 是 WebProxy 的独立策略类型
- BWM 属于带宽控制域（套餐 2），非访问限制

### 3.6 N7→N4 下发链路 — 动作下发主链路

Batch-02 KP-02 定义了 PCC 下发链路：

> PCRF/PCF 通过 N7 接口将 QoS 及计费策略下发给 PGW-C/SMF，PGW-C/SMF 通过 N4 接口再下发给 PGW-U/UPF，PGW-U/UPF 基于用户和业务类型进行**限速和门控**。

**关键节点职责**（Batch-02 KP-02、Batch-03 KP-01）：

| 网元 | 职责 | 访问限制相关性 |
|------|------|----------------|
| PCF | 策略决策，下发动态规则/预定义规则/Triggers | 重定向/URL 过滤策略决策（最高决策权） |
| AMF | 从 PCF 接收 UE/AM 策略→传递 UE/(R)AN；无 PCF 时本地配置 AM 策略 | **SAR 服务区限制=接入控制** |
| SMF | 将 PCF 策略转换为 N4 PDR/FAR/QER/URR 下发给 UPF；将 SDF 与 QoS 流绑定 | **重定向策略翻译为 PDR 给 UPF** |
| UPF | 执行数据包检测；**执行门控、重定向等用户面策略执行** | **★重定向/URL 过滤/阻塞执行点** |

**PCF 决策垄断**（Batch-03 KP-06）：策略生成**完全由 PCF 决策，不存在与 UDM、SMF 协商的过程**。PCF 能根据用户位置、等级、时间段、配额状态、节假日等灵活定制。这意味着访问限制的策略逻辑（如"套餐耗尽→重定向"）必须在 PCF 侧完整定义。

**信令消息**（Batch-01 KP-07）：

| 场景 | 信令消息 | 方向 |
|------|----------|------|
| 用户接入时下发预定义/动态规则 | `Npcf_SMPolicyControl_Create Request` | PCF→SMF→UPF |
| 会话过程中下发/更新/删除规则 | `Npcf_SMPolicyControl_UpdateNotify Request` | PCF→SMF→UPF |
| SMF 发起的策略变更请求 | `Npcf_SMPolicyControl_Update Request` | SMF→PCF |
| 无 PCF 时下发本地规则 | SMF 内部决策→N4 | SMF→UPF |

### 3.7 REFRESHSRV 时序约束 — 配置生效的最后一步

所有 UDG 侧访问限制配置必须以 `SET REFRESHSRV` 作为最后一步（Batch-02 KP-09 步骤 8）：

```
SET REFRESHSRV:REFRESHTYPE=ALL;
```

**关键约束**：
- 60 秒延迟生效
- 必须在 Filter/FlowFilter/RULE 等变更后执行
- 不执行则配置不生效

**图谱落位**：所有 UDG 侧配置任务（Task）都应以 REFRESHSRV 作为收尾步骤，建模为 Task 模板的强制步骤。

### 3.8 Event Trigger 与 PCR Trigger — 访问限制触发条件清单

Batch-02 KP-06 定义了 12 类 UDG 侧 Event Trigger；Batch-03 KP-04 定义了 UNC 侧 PCR Trigger（5 AMF + 24 SMF）。访问限制相关的主要触发器：

**UDG 侧 Event Trigger**（Batch-02 KP-06）：
| Event Trigger | 含义 | 访问限制典型场景 |
|---------------|------|------------------|
| **VOLQU** | 流量配额耗尽 | 套餐耗尽→触发重定向到充值页 |
| **TIMQU** | 时长配额耗尽 | 同上 |
| **VOLTH** | 流量阈值 | 流量超限→触发限速/阻塞 |
| START/STOPT | 业务开始/结束 | ADC 上报 |

**UNC 侧 PCR Trigger**（Batch-03 KP-04，访问限制相关）：
| 事件 | 描述 | 访问限制相关性 |
|------|------|----------------|
| **US_RE** | 资源/监控关键资源达门限 | **★配额耗尽触发重定向** |
| **NO_CREDIT** | 信用失效（配额申请失败） | **★配额耗尽触发重定向** |
| **PRA_CH** | UE 所处位置 PRA 变化 | **★基于区域的重定向** |
| **SAREA_CH** | 服务区域（跟踪区）变化 | 位置类策略 |
| **SCELL_CH** | 服务小区变化 | 小区级策略 |
| **USER_LOCATION_CH** | SAREA/SCELL/二者组合 | 综合位置策略 |
| **LOC_CH** | UE 跟踪区 TA 改变 | 位置类接入控制 |
| **SERV_AREA_CH** | 签约 SAR 改变 | **★服务区限制变更** |
| **PLMN_CH** | PLMN 变更 | 漫游重定向 |
| **UE_IP_CH** | UE IP 分配/释放 | IP 类访问限制 |
| **UE_MAC_CH** | UE MAC 地址变化 | MAC 类访问限制 |
| APP_STA / APP_STO | 应用程序流量开始/结束 | 应用类访问限制（ADC） |

**关键发现**：**US_RE、NO_CREDIT、PRA_CH、SAREA_CH、USER_LOCATION_CH** 这几类触发器是访问限制（特别是重定向）的主要触发条件。

### 3.9 共性 SemanticObject 候选归纳

基于共性机制分析，访问限制场景的第 1 层 SemanticObject（语义对象）候选清单：

| SemanticObject ID | 中文名 | 语义范畴 | 核心属性 | 来源 |
|-------------------|--------|----------|----------|------|
| **SA-SAFlow** | SA 业务感知流程 | 流程语义 | 七步：下发→到达→解析→匹配→执行→转发→上报 | Batch-01 |
| **SA-ActionType** | 动作类型语义 | 动作语义 | DISCARD / HEADEN / REDIRECT / PERMIT / BLOCK | Batch-01/02 |
| **BA-PolicyType** | 策略类型语义 | 策略语义 | PCC / BWM / HEADEN / WEBPROXY / SMARTREDIRECT | Batch-01 |
| **BA-RuleType** | 规则类型语义 | 规则语义 | 动态 / 预定义 / 本地 | Batch-02/03 |
| **BA.FilterCondition** | 过滤条件 | 匹配语义 | 三四层过滤 / 7 层过滤 / 协议过滤 / 流过滤器 | Batch-01 KP-04 |
| **BA.Action-PCC** | PCC 动作 | 动作语义 | 重定向、URL 过滤、头增强、QoS、计费、带宽管理 | Batch-02 KP-05 |
| **BA.Action-HEADEN** | 头增强动作 | 动作语义 | 字段前缀+字段值+加密算法+编码方式 | Batch-05 |
| **BA.Action-REDIRECT** | 重定向动作 | 动作语义 | 重定向目标（URL/Portal/Proxy）+改写层级（DNS/L3/L7） | Batch-06 |
| **BA.Action-URLFilter** | URL 过滤动作 | 动作语义 | BLOCK/PERMIT/REDIRECT + ICAP 分类匹配 | Batch-07 |
| **BA.RedirectTarget** | 重定向目标 | 目标语义 | 服务器集群（IPFarm）/指定 URL/DNS 重写目标 | Batch-06 |
| **BA.Location** | 位置条件 | 条件语义 | CGI/ECGI/NCGI + PLMN/TAI + 漫游区 | Batch-07（WSFD-211001） |
| **BA.QuotaCondition** | 配额条件 | 条件语义 | VOLQU/TIMQU/NO_CREDIT + 套餐余量 | Batch-03 |
| **BA.PCFDecision** | PCF 决策 | 决策语义 | 垄断决策+无协商+位置/等级/时间/配额多维 | Batch-03 KP-06 |
| **BA.PolicyTrack** | 动作轨道 | 架构语义 | Track-A（PCC 体系）/ Track-B（URL 过滤体系） | Batch-07 发现-1 |
| **BA.LicenseGate** | License 门控 | 约束语义 | 各特性独立 License + 强依赖关系 | 全批次 |
| **BA.ConfigObject-Chain** | 配置对象链 | 配置语义 | FILTER→FLOWFILTER→RULE→USERPROFILE 四层模型 | Batch-02 KP-09 |

---

## 4. 配置差异对比

### 4.1 双轨动作机制对比 — 访问限制场景最关键的架构事实

Batch-07 发现-1 揭示了访问限制场景的**核心架构事实**：访问限制动作存在**两条完全独立的轨道路径**。

#### 轨道 A：PCC 体系（RULE.POLICYTYPE 驱动）

```
用户业务流
    ↓
FILTER + FLOWFILTER + FLTBINDFLOWF（L3/L4 匹配）
[+ L7FILTER + PROTBINDFLOWF（L7 匹配）]
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

**轨道 A 特点**：
- 以 `RULE.POLICYTYPE` 为核心区分
- 动作类型由 POLICYTYPE 隐式决定（ADC 兜底阻塞、HEADEN 插入、SMARTREDIRECT 改写）
- 配置链路长（FILTER → FLOWFILTER → RULE → POLICYNAME 指向的具体对象）
- 走 PCC 体系时需要 PCRF/PCF 下发规则或本地预定义
- **走轨道 A 的特性**：GWFD-020357 ADC、GWFD-110261/262/263 头增强、GWFD-110401 头防欺诈、GWFD-110284 HTTP 智能重定向、GWFD-110283 DNS 纠错、GWFD-110281 用户 Portal、GWFD-110282 WebProxy

#### 轨道 B：URL 过滤体系（CFTEMPLATE/CONTCATEGBIND.ACTION 驱动）

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

**轨道 B 特点**：
- 以 `CFTEMPLATE.ACTION` 和 `CONTCATEGBIND.ACTION` 为核心（**显式指定 BLOCK/PERMIT/REDIRECT**）
- 动作类型直接在配置参数中声明，不通过 POLICYTYPE 间接表达
- 依赖外部 ICAP Server（引入 ICAP Server/Group/VPN 配置体系）
- 触发维度单一（仅基于 URL 分类），不涉及复杂的多条件组合
- **走轨道 B 的特性**：GWFD-110471 URL 过滤基本功能

#### 双轨对比矩阵

| 维度 | 轨道 A（PCC 体系） | 轨道 B（URL 过滤体系） |
|------|-------------------|----------------------|
| **核心 ConfigObject** | RULE（POLICYTYPE 差异化） | CFTEMPLATE + CONTCATEGBIND |
| **动作指定方式** | 隐式（POLICYTYPE 决定） | 显式（ACTION=BLOCK/PERMIT/REDIRECT） |
| **匹配维度** | 多维度（L3/L4/L7/错误码/URL/UserAgent...） | 单维度（URL 分类） |
| **外部依赖** | 可选 PCRF/PCF | **必需 ICAP Server** |
| **动作类型** | 隐式阻塞、头增强、重定向改写 | 直接 BLOCK/PERMIT/REDIRECT |
| **典型 MML 命令** | ADD RULE, ADD PCCPOLICYGRP, ADD HEADEN, ADD SMARTHTTPREDIR | ADD CFTEMPLATE, ADD CONTCATEGBIND, ADD ICAPSERVER |
| **独立配置体系** | 共用 FILTER/FLOWFILTER/USERPROFILE | 独有 APNCFFUNC/CFPROFILE/CFTEMPLATE/CONTCATEGROUP/ICAP* |
| **License 共用** | 各特性独立 License | URL 过滤独立 License（82200FCP UFBF01） |
| **PERMIT 支持** | 不支持（不做动作或做阻塞/重定向） | **★唯一显式支持 PERMIT★** |

#### 双轨协同（重要）

**两条轨道可以并存于同一用户**：
- 轨道 A 处理 ADC/头增强/重定向类需求（基于应用、URL、用户属性）
- 轨道 B 处理 URL 分类过滤（基于外部 URL 分类数据库）
- 用户业务流可能先后被两条轨道检查，最终动作取决于配置优先级和规则匹配顺序

**对图谱建模的关键启示**：
1. RULE 对象需要**两个 variant_dimension**：`policy_track`（A/B）和 `policy_type`（POLICYTYPE/ACTION）
2. 轨道 B 的 CFTEMPLATE/CONTCATEGBIND 是**独立于 RULE 体系**的配置对象，需要单独建模
3. ICAP Server 互通配置是 URL 过滤**独有的资源类对象**，类似 Portal/WebProxy 的 IPFarm

### 4.2 头增强族配置差异（HTTP/HTTPS/RTSP）

Batch-05 KP-4 归纳了头增强族内三个协议的差异：

| 差异点 | HTTP 头增强 | HTTPS 头增强 | RTSP 头增强 |
|--------|-------------|-------------|-------------|
| **触发条件** | 特定 IP / 特定 URL / HTTP 协议 | 特定 IP / 特定 **SNI** / HTTPS 协议 | 特定 IP / 特定 URL / RTSP 协议 |
| **支持协议** | HTTP1.x（不支持 HTTP2.0） | TLS 1.0/1.1/**1.2/1.3** | RTSP（不支持 RTSP over HTTP） |
| **字段插入位置** | HTTP 扩展字段 | **SSL 报文头 Extension 字段，TLV 格式组织** | RTSP 扩展字段 |
| **依赖 SA 特性** | SA-Basic + SA-Web Browsing + SA-Mobile（MMS 场景） | SA-Basic + SA-Web Browsing + SA-Mobile + **HTTP2.0 Host 识别** | SA-Basic + **SA-Streaming** |
| **加密算法** | MD5/RC4/AES-128/256/RSA-1024/2048/SHA-256 | MD5/RC4/AES-128/256/SHA-256（**无 RSA**） | 同 HTTP |
| **编码能力** | base64 + ASCII | base64 + ASCII + **十六进制** | base64 + ASCII |
| **头防欺诈支持** | **支持** | **支持** | **不支持**（族内唯一例外） |
| **License** | 82209777 HTHE01 | 82209779 HTSE01 | 82209778 RTHE01 |
| **多参数拼接** | 支持（v02 起） | 不支持 | 支持（v02 起） |

**最关键差异**：
1. **HTTPS 头增强的 TLV 格式**：字段必须按 TLS 协议 TLV 格式组织插入到 SSL Extension 内（RFC 5246），技术复杂度最高
2. **HTTPS 头增强的 SNI 触发**：因 HTTPS 报文加密，只能基于 SNI（Server Name Indication）触发
3. **头防欺诈仅支持 HTTP/HTTPS**：RTSP 协议不支持头防欺诈（Batch-08 发现-4 安全盲区）

**族内共用配置载体**（Batch-05 发现-1）：所有协议共用 `ADD HEADEN` 命令和 `HEADEN` 对象，差异仅在"**解析 SA 特性依赖**"和"**字段插入位置**"两个维度。`HEADEN` 对象的 `variant_dimensions` 应包含 `protocol_type`（HTTP/HTTPS/RTSP/NSH）。

### 4.3 重定向族四种层级实现对比

Batch-06 KP-1、发现-1 归纳了重定向族的四种层级实现：

| 维度 | HTTP 智能重定向 | DNS 纠错 | 用户 Portal | WebProxy |
|------|---------------|---------|-----------|----------|
| **协议层** | L7 HTTP 响应 | DNS 解析层 | L7 HTTP 请求 | L3 IP NAT |
| **改写对象** | HTTP 响应报文 | DNS 响应报文 | HTTP 响应（301/302/303） | IP 报文目的 IP |
| **触发时机** | HTTP 错误码 / 多条件匹配 | DNS 查询失败 | 用户 HTTP 请求（captive 周期） | TCP SYN 匹配规则 |
| **用户感知** | 跳转到新页面 | 跳转到新页面 | 跳转到 Portal | **透明（用户无感知）** |
| **目标服务器** | 第三方服务器 | 第三方 Platform | Portal Server（业务订购/管理） | Proxy Server（加速/病毒防护） |
| **典型用途** | URL 纠错、内容过滤 | 错误域名引导 | 业务订购、广告推送 | 网络加速、内容过滤 |
| **POLICYTYPE** | SMARTREDIRECT | SMARTREDIRECT | PCC（USERPROFILE captive） | WEBPROXY |
| **IP Farm** | 不用 | 不用 | 用 | 用 |
| **EXTENDEDFILTER** | 用（多维度） | 用（URL） | 不用 | 不用 |
| **依赖 SA** | SA-Basic + SA-Web Browsing | SA-Basic + SA-Network Administration | SA-Basic + SA-Web Browsing + SA-Mobile | SA-Basic |
| **协议限制** | HTTP1.x（不支持 HTTPS/HTTP2.0） | UDP DNS（不支持 TCP DNS） | HTTP1.x/WAP（不支持 HTTPS） | TCP（无协议限制，纯 IP 层） |

**介入时机对比**：DNS 纠错（最早）→ WebProxy（建立 TCP 时）→ HTTP 智能重定向（HTTP 响应时）→ 用户 Portal（定时主动触发）

**关键启示**：**仅 WebProxy 能处理加密协议**（因其在 L3 工作，不解析 L7 内容）。其他三个重定向特性均依赖 L7 解析，受加密协议限制。这是访问限制场景设计时选择重定向方式的关键考量。

### 4.4 动态 PCC vs 本地 PCC（DNN 粒度混合）

Batch-03 KP-02 揭示了 UNC 侧的动态/本地 PCC 混合部署能力：

**动态 PCC**：SMF 通过 PCF 获取 SM 策略。PCF 向 AMF/SMF 下发 UE/AM/SM 策略+PCR Trigger。

**本地 PCC**：SMF 直接使用本地配置策略，不与 PCF 交互。以 **DNN 粒度** 配置。

**★ 混合部署能力 ★**：可在**一个 UNC 上实现基于 DNN 混合使用动态 PCC 和本地 PCC**。例如配置 DNN1 用本地 PCC、DNN2 用动态 PCC。

**PCF 主备容灾**（Batch-03 KP-02、发现-7）：支持 failover 一次；超时根据 `SET PCCFAILACTION` 决定回落本地 PCC 或会话失败。这意味着访问限制策略在 PCF 故障时有**本地 PCC 兜底机制**保证连续性。

### 4.5 UDG 侧 vs UNC 侧 PCC 配置差异

| 对比维度 | UDG（Batch-02） | UNC（Batch-03） |
|----------|-----------------|-----------------|
| 规则定义角色 | **定义具体规则内容**（预定义/本地） | 定义规则名，透传给 UPF |
| UserProfile 一致性 | 与 SMF 上 UserProfile 名一致 | 与 UPF 上 UserProfile 名一致 |
| 核心命令 | ADD FILTER/FLOWFILTER/RULE/USERPROFILE | SET PCCFUNC, ADD PCCTEMPLATE, ADD RULE/USERPROFILE |
| 动态/本地 PCC 切换 | 不涉及（被动接收） | SET PCCFUNC + SET APNPCCFUNC（DNN 粒度） |
| 规则下发范围 | 不涉及 | ADD RULE 的 RULERANGE：**ALL（主+辅锚点）/CENTRAL（仅主锚点）/LOCAL（仅辅锚点）** |
| PCF 故障处理 | 不涉及 | SET PCCFAILACTION（回落本地 PCC 或会话失败） |

**SMF 支持主辅锚点 UPF 差异化规则下发**（Batch-03 发现-8）：SMF 支持将规则下发给：主+辅锚点 UPF / 仅主锚点 / 仅辅锚点 / 指定辅锚点（DNAI 粒度）。访问限制规则可按 UPF 角色差异化部署——这意味着不同 UPF 可执行不同访问限制策略。

### 4.6 URL 过滤协议解析能力差异

Batch-07 发现-3 归纳了 URL 过滤对不同协议的 URL 提取能力：

| 协议 | URL 解析能力 | 依赖 SA |
|------|-------------|---------|
| HTTP/WAP1.X/WAP2.0 | **完整 URL**（仅上行 Get/Post） | SA-Basic + SA-Web Browsing + SA-Mobile |
| HTTPS | **仅 SNI 或证书**（不能解析完整 URL） | SA-Basic + SA-Web Browsing + HTTP2.0 Host 识别 |
| 非加密 QUIC | SNI 或证书 | 同 HTTPS |

**关键限制**：HTTPS 场景下，URL 过滤**不能基于完整 URL**，只能基于 SNI——这是 HTTPS 加密带来的固有限制。

### 4.7 UDG 侧配置对象四元组 vs UNC 侧三级绑定

**UDG 侧配置对象四元组**（Batch-02 发现-6）：访问限制完整配置需 4 类对象协作：
- **FLOWFILTER**（+FILTER/L7FILTER）：定义"匹配什么流量"
- **RULE**（POLICYTYPE=PCC/HEADEN/SMARTREDIRECT/WEBPROXY）：定义"匹配后做什么"
- **USERPROFILE**：定义"对哪个用户生效"，通过 RULEBINDING 绑定 RULE
- **PCCPOLICYGRP**：定义"具体策略参数"，关联 URRGROUP

配置对象关系链：`FILTER → FLOWFILTER（via FLTBINDFLOWF）→ RULE（POLICYTYPE, POLICYNAME）→ USERPROFILE（via RULEBINDING）`

**UNC 侧三级绑定**（Batch-03 KP-15）：USRPROFGROUP → USERPROFILE → APN
- `ADD USRPROFGROUP`：用户模板组
- `ADD UPBINDUPG`：用户模板-模板组绑定
- `ADD APNUSRPROFG`：APN-用户模板组绑定（DNN 级）

---

## 5. 依赖关系与协同

### 5.1 访问限制技术栈分层依赖

```
┌───────────────────────────────────────────────────────────────┐
│  UNC 接入控制层（AMF/SMF，粗粒度）                              │
│  - 移动接入控制：SAR/区域/ODB（注册阶段）                       │
│  - 会话接入控制：服务区域限制（会话阶段）                        │
│  - 位置触发：WSFD-211001 基于 ULI 的策略决策                     │
│  Batch-07 KP-3/4                                              │
├───────────────────────────────────────────────────────────────┤
│  PCF 策略决策层（垄断决策，无协商）                              │
│  - SM 策略三内容：QoS + 计费 + 短信或重定向                     │
│  - UPCF 动作组：带宽控制 + 计费控制 + 消息通知 + 重定向          │
│  - 29 类 PCR Trigger（5 AMF + 24 SMF）                         │
│  Batch-03 KP-05/06/07                                         │
├───────────────────────────────────────────────────────────────┤
│  SMF 翻译层（N7→N4 映射）                                       │
│  - PCC 规则 → PDR/FAR/QER/URR                                  │
│  - 动态/预定义/本地规则统一处理                                  │
│  - DNN 粒度动态/本地 PCC 混合                                   │
│  Batch-03 KP-08/14                                             │
├───────────────────────────────────────────────────────────────┤
│  SA 规则匹配层（UPF，通用引擎）                                 │
│  - SA 七步流程                                                 │
│  - FlowFilter → Rule → UserProfile                             │
│  - 3 匹配原则（优先级 + 全条件 + 类型独立）                     │
│  Batch-01/02                                                   │
├───────────────────────────────────────────────────────────────┤
│  轨道 A：动作执行层（UPF，PCC 体系）                             │
│  ├─ ADC 应用检测（GWFD-020357）                                 │
│  ├─ HEADEN 头增强（GWFD-110261/262/263）                        │
│  ├─ 防欺诈（GWFD-110401，前置检测）                             │
│  └─ REDIRECT 重定向族（GWFD-110284/283/281/282）                │
│  Batch-04/05/06/08                                             │
├───────────────────────────────────────────────────────────────┤
│  轨道 B：URL 过滤层（UPF，独立体系）                             │
│  - ICAP Server 协同                                             │
│  - CFTEMPLATE/CONTCATEGBIND.ACTION                             │
│  - 显式 BLOCK/PERMIT/REDIRECT                                  │
│  Batch-07                                                      │
├───────────────────────────────────────────────────────────────┤
│  License 门控层（前置）                                         │
│  - 各特性独立 License                                          │
│  - 强依赖：防欺诈 → 头增强；ADC → SA-Basic + PCC                │
│  - WSFD-211001 → PCC + BWM（无 PCRF 场景）                     │
│  全批次                                                        │
└───────────────────────────────────────────────────────────────┘
```

### 5.2 ADC 与所有 L7 动作特性的依赖关系

ADC 是访问限制场景的"**眼睛**"——所有需要基于应用/URL 做判断的特性都依赖 ADC/SA 的解析能力（Batch-04 发现-1）：

```
ADC/SA 解析层（GWFD-020357 + SA-Web Browsing/Streaming/Mobile）
    ↓ 提供：应用标识、URL、五元组、Method、Content-Type
    ↓
┌────────────────────────────────────────────────────────────┐
│  访问限制动作层（基于 ADC 提供的信息匹配 RULE）              │
├────────────────────────────────────────────────────────────┤
│  DISCARD 类：ADC 兜底阻塞、URL 过滤 BLOCK                   │
│  HEADEN 类：HTTP/HTTPS/RTSP 头增强、HTTP 头防欺诈            │
│  REDIRECT 类：HTTP 智能重定向、DNS 纠错、用户 Portal、WebProxy│
└────────────────────────────────────────────────────────────┘
```

**ADC 的两条触发链路**（Batch-04 发现-2）：
- **链路 A：本地 ADC 规则直接触发**（POLICYTYPE=ADC）— UDG 本地配置 RULE，匹配后直接执行；不经过 PCRF/PCF，时延低
- **链路 B：PCRF/PCF 动态决策**（POLICYTYPE=PCC + Application ID）— UDG 检测→上报 APPLICATION_START→PCRF/PCF 决策→下发新 PCC 规则；时延较高，适合动态个性化

**ADC 兜底阻塞机制**（Batch-04 KP-5）：业务流匹配不上所有规则时，**UDG 阻塞当前业务流** → 这是 ADC 提供访问限制"DISCARD"动作的底层机制。建议配置 L3/4=any、L7=any 的缺省规则避免误阻塞。

### 5.3 头增强与防欺诈的强耦合

Batch-08 发现-1 揭示了访问限制场景中**强耦合依赖关系最显著**的特性对：

| 维度 | 头防欺诈（GWFD-110401） | 头增强（GWFD-110261） |
|------|------------------------|----------------------|
| **License 依赖** | **强依赖**：启用防欺诈必须开启头增强（双开 82209786 + 82209777） | 独立 |
| **配置载体** | **共用 HEADEN 对象**：ANTIFRAUD/GRAYLIST 内嵌于 ADD HEADEN | HEADEN 对象本身 |
| **执行顺序** | **前置检测**：防欺诈检测 → 字段纠正/冗余清理 → 头增强插入 | 后置执行 |
| **触发条件** | **共用过滤链**：共用 FILTER/L7FILTER/FLOWFILTER | 同上 |
| **RULE POLICYTYPE** | **共用 HEADEN** | HEADEN |
| **协议支持** | 仅 HTTP/HTTPS（不支持 RTSP） | HTTP/HTTPS/RTSP |

**执行时序**（Batch-08 KP-1、发现-3）：
```
ADC/SA 解析（GWFD-020357）→ 识别 HTTP 报文、提取 Method/URL
    ↓
规则匹配（RULE POLICYTYPE=HEADEN）
    ↓
【头防欺诈检测 GWFD-110401】 ← 检查已有字段是否欺诈
    ├─ 不存在字段：继续头增强流程
    ├─ 字段正确：跳过头增强
    ├─ 字段错误：纠正后继续（或灰名单模式停止）
    └─ 多个字段：清理冗余后继续
    ↓
【头增强插入 GWFD-110261/262/263】 ← 插入 MSISDN/IMSI 等
    ↓
业务服务器获取增强字段
    ↓
【后续访问限制动作】
    ├─ Portal 认证（GWFD-110281）：基于 MSISDN 判断是否签约
    ├─ HTTP 智能重定向（GWFD-110284）：REDIRAPPENDINFO 携带 MSISDN
    └─ URL 过滤（GWFD-110471）：基于真实用户身份做细粒度控制
```

**关键启示**：头防欺诈保障的是**整条访问限制链路的可信基础**——若头增强字段被伪造，后续所有基于用户身份的访问控制都会失效。

### 5.4 ADC → 头增强 → 防欺诈 → 重定向/URL 过滤 的完整链路

综合 Batch-04/05/06/07/08 的依赖关系，访问限制的完整链路：

```
ADC 解析（应用识别）
    ↓ 提供 L7 信息
规则匹配（RULE）
    ↓ 根据 POLICYTYPE 分流
┌────────────────────┬────────────────────┬────────────────────┐
│ HEADEN 轨道         │ REDIRECT 轨道       │ URL 过滤轨道（B）   │
│  ↓                  │  ↓                  │  ↓                  │
│ 防欺诈检测（前置）   │ HTTP 重定向改写     │ ICAP Server 查询    │
│  ↓                  │ DNS 重写            │  ↓                  │
│ 字段纠正/清理        │ IP NAT（WebProxy）  │ 分类匹配            │
│  ↓                  │ Portal captive     │  ↓                  │
│ 头增强插入           │  ↓                  │ CFTEMPLATE.ACTION   │
│  ↓                  │ 目标服务器          │ CONTCATEGBIND.ACTION│
│ 业务服务器           │                    │  ↓                  │
│  ↓                  │                    │ BLOCK/PERMIT/REDIRECT│
│ 后续访问控制         │                    │                    │
│ （Portal 认证、     │                    │                    │
│  重定向携带 MSISDN、 │                    │                    │
│  URL 过滤）         │                    │                    │
└────────────────────┴────────────────────┴────────────────────┘
```

### 5.5 位置触发与访问限制的协同

WSFD-211001（基于初始接入位置的策略控制）是连接 UNC 侧与 UDG 侧访问限制的关键桥梁（Batch-07 KP-4、发现-2）：

**核心机制**：
- 用户激活时 SGSN/MME/AMF 上报 ULI（User Location Information）
- UNC（SMF/PGW-C）将 ULI 透传给 PCRF/PCF（动态 PCC）或本地决策（本地 PCC）
- 匹配 `USRLOCATION` + `USRLOCATIONGRP` → 触发对应的访问限制/带宽控制策略

**位置类型**：CGI（2/3G）、ECGI（4G）、NCGI（5G）

**ConfigObject**：USRLOCATION → USRLOCATIONGRP → UPBINDUPG → APNUSRPROFG

**协同关系**：
- UNC 侧（WSFD-211001）：提供"用户在哪里接入"作为策略决策输入
- PCF 侧：基于位置决策下发携带位置的 PCC 策略
- UDG 侧：执行带宽控制、重定向、阻塞

### 5.6 UNC 侧接入控制与 UDG 侧访问限制的分工

访问限制场景中，**UNC 侧和 UDG 侧承担不同角色**（Batch-07 发现-2）：

```
UNC 侧（SMF/PGW-C/AMF）：
├─ 移动接入控制：RAT/核心网/区域/ODB 限制（注册阶段，WSFD-106003/105003/106005）
├─ 会话接入控制：ODB/服务区域限制（会话阶段，WSFD-106005/105006）
├─ 位置触发：基于 ULI 的策略决策（WSFD-211001）
└─ 策略下发：通过 Gx/N7 向 PCRF/PCF，通过 N4/PFCP 向 UDG
        ↓
UDG 侧（PGW-U/UPF）：
├─ 应用检测：ADC（GWFD-020357）
├─ 头增强：HTTP/HTTPS/RTSP 头增强（GWFD-110261/262/263）
├─ 头防欺诈：GWFD-110401
├─ 重定向：HTTP 重定向/DNS 纠错/Portal/WebProxy（GWFD-110284/283/281/282）
└─ URL 过滤：GWFD-110471（与 ICAP Server 协同）
```

**关键观察**：
- UNC 侧的接入控制是**注册/会话阶段**的"是否允许接入"决策（粗粒度）
- UDG 侧的访问限制是**业务流阶段**的"允许做什么"决策（细粒度）
- 两层共同构成完整的访问限制链路：先 UNC 决定能否接入，再 UDG 决定能访问什么

### 5.7 License 依赖关系图

**强依赖关系**：
- GWFD-110401 头防欺诈 → GWFD-110261 HTTP 头增强（必须同时开启 82209786 + 82209777）
- GWFD-020357 ADC → SA-Basic（82209749）+ PCC 基本功能（82209825）
- WSFD-211001 → PCC 基本功能（WSFD-109101）+ 基于业务感知的带宽控制（WSFD-211005，无 PCRF 场景）

**各特性独立 License**：
| 特性 | License |
|------|---------|
| GWFD-020357 ADC | 82200AFK LKV3G5ADCF01 |
| GWFD-020351 PCC | 82209825 LKV3G5PCCB01 |
| GWFD-110261 HTTP 头增强 | 82209777 LKV3G5HTHE01 |
| GWFD-110262 RTSP 头增强 | 82209778 LKV3G5RTHE01 |
| GWFD-110263 HTTPS 头增强 | 82209779 LKV3G5HTSE01 |
| GWFD-110281 用户 Portal | 82209780 LKV3G5CPPT01 |
| GWFD-110282 WebProxy | 82209781 LKV3G5WEBP01 |
| GWFD-110283 DNS 纠错 | 82209782 LKV3G5DNSO01 |
| GWFD-110284 HTTP 智能重定向 | 82209783 LKV3G5SHPR01 |
| GWFD-110401 头防欺诈 | 82209786 LKV3G5HHAS01 |
| GWFD-110471 URL 过滤 | 82200FCP LKV3G5UFBF01 |
| WSFD-211001 位置策略 | 82200BNQ LKV2PCIAL01 |

---

## 6. 与访问限制核心关联（★ 第 1 层 CS/DP 直接来源）

### 6.1 五大主题集群的访问限制贡献度

| 主题集群 | 贡献度 | 核心贡献 | 关键批次 |
|----------|--------|----------|----------|
| SA/PCC 基础设施 | ★★★★★ | 规则匹配引擎、策略下发链路、动作官方枚举 | Batch-01/02/03 |
| 重定向族 | ★★★★★ | REDIRECT 动作四种实现、双轨机制厘清 | Batch-06/07 |
| URL 过滤与接入控制 | ★★★★★ | 轨道 B 独立动作体系、UNC 侧粗粒度接入 | Batch-07 |
| 应用检测层 | ★★★★☆ | L7 应用感知、所有 L7 动作的前置 | Batch-04 |
| 信息插入层 | ★★★☆☆ | 带内字段插入、防欺诈安全增强 | Batch-05/08 |

### 6.2 访问限制的五个正交维度

综合 8 个批次的分析，访问限制场景包含五个正交的控制维度：

**维度 1：动作类型（DISCARD/HEADEN/REDIRECT/PERMIT）**
- 来源：全批次
- 机制：通过 RULE.POLICYTYPE（轨道 A）或 CFTEMPLATE.ACTION（轨道 B）指定
- 典型：阻塞非法网站、重定向充值页、头增强 MSISDN

**维度 2：规则类型（动态/预定义/本地）**
- 来源：Batch-01/02/03
- 机制：PCF 决策下发 / UPF 本地预配 / SMF 兜底
- 典型：URL 过滤必须用预定义（七层限制）、配额重定向可用动态

**维度 3：动作轨道（PCC 体系/URL 过滤体系）**
- 来源：Batch-07（核心发现）
- 机制：轨道 A 走 RULE.POLICYTYPE；轨道 B 走 CFTEMPLATE.ACTION
- 典型：ADC/头增强/重定向族走轨道 A；URL 过滤走轨道 B

**维度 4：网元范围（UPF/SMF/双/AMF）**
- 来源：Batch-02/03/07
- 机制：UDG 侧执行；UNC 侧决策+接入控制；SMF 主辅锚点差异化
- 典型：业务流细粒度控制（UPF）；注册阶段接入控制（AMF）；位置触发（SMF）

**维度 5：匹配层次（L34/L7/DNS）**
- 来源：Batch-01/02/04/05/06/07
- 机制：三四层过滤、七层过滤（URL/SNI）、DNS 查询、应用识别
- 典型：IP 阻塞（L34）、URL 过滤（L7）、DNS 纠错（DNS 层）、WebProxy（L3 NAT）

### 6.3 方案闭包（CS）归纳 — ★ 第 1 层核心 ★

按**动作机制/触发维度**归纳，访问限制场景的方案闭包（CS, Closure Solution）共 **9 个**：

#### CS-AC-01 PCC 阻塞方案（DISCARD，基于 RULE.POLICYTYPE=PCC）

- **核心机制**：通过 PCC 策略类型的兜底阻塞/显式阻塞动作丢弃用户报文
- **动作类型**：DISCARD
- **动作轨道**：轨道 A（PCC 体系）
- **配置链**：FILTER → FLOWFILTER → RULE（POLICYTYPE=PCC） → PCCPOLICYGRP → USERPROFILE
- **触发方式**：PCF 动态下发 / UPF 预定义 / ADC 兜底阻塞
- **uses_feature**：GWFD-020351（PCC 基本功能）、GWFD-020357（ADC，兜底阻塞）
- **关键参数**：RULE.PRIORITY、PCCPOLICYGRP.ADCMUTEFLAG
- **决策分支**：需要 L7 识别？是→必须用预定义规则；否→可用动态规则
- **典型场景**：非法网站阻塞、不安全 IP 禁止访问、ADC 兜底阻塞
- **来源批次**：Batch-01 KP-10（业务 3 阻塞）、Batch-02 KP-05、Batch-04 KP-5

#### CS-AC-02 头增强方案（HEADEN，基于 RULE.POLICYTYPE=HEADEN）

- **核心机制**：在 HTTP/HTTPS/RTSP 请求报文头插入运营商规划字段（MSISDN/IMSI/IMEI/APN/位置等）
- **动作类型**：HEADEN
- **动作轨道**：轨道 A（PCC 体系）
- **配置链**：FILTER/L7FILTER → FLOWFILTER → HEADEN 对象 → RULE（POLICYTYPE=HEADEN） → USERPROFILE
- **触发方式**：基于 IP（三四层）/基于 URL+SNI（七层）
- **uses_feature**：GWFD-110261（HTTP 头增强）、GWFD-110262（RTSP 头增强）、GWFD-110263（HTTPS 头增强）、GWFD-110401（头防欺诈，可选前置）、GWFD-020357（ADC，L7 解析前置）
- **关键参数**：HEADEN.DATATYPE、HEADEN.PREFIXNAME、HEADEN.ENCRYALGORI、HEADEN.ANTIFRAUD、HEADEN.GRAYLIST
- **决策分支**：协议是 HTTP/HTTPS/RTSP？→ 选择对应头增强特性；需要防欺诈？→ 启用 ANTIFRAUD
- **典型场景**：业务认证、个性化服务、防欺诈校验、WAP 网关
- **来源批次**：Batch-05 全批次、Batch-08 全批次

#### CS-AC-03 HTTP 重定向方案（REDIRECT，L7 HTTP 响应改写）

- **核心机制**：基于 HTTP 错误码/URL/UserAgent/ContentType 等多条件触发，改写 HTTP 响应为 301/302/303 重定向
- **动作类型**：REDIRECT
- **动作轨道**：轨道 A（PCC 体系）
- **配置链**：EXTENDEDFILTER → ERRORCODE → SMARTHTTPREDIR → RULE（POLICYTYPE=SMARTREDIRECT） → USERPROFILE
- **触发方式**：6 种场景（URL 错误/URL 过滤/内容类型/URL 后缀/终端类型/错误码自动）
- **uses_feature**：GWFD-110284（HTTP 智能重定向）、GWFD-020357（ADC，L7 解析前置）、GWFD-110261（头增强，可选 REDIRAPPENDINFO 携带 MSISDN）
- **关键参数**：SMARTHTTPREDIR.*、REDIRAPPENDINFO.REQURLFLAG/IMSIFLAG/IMEIFLAG、ERRORCODE 范围
- **决策分支**：需要携带用户信息？→ 配置 REDIRAPPENDINFO
- **典型场景**：URL 纠错、内容过滤、错误码自动重定向
- **协议限制**：仅 HTTP1.x，不支持 HTTPS/HTTP2.0
- **来源批次**：Batch-06 KP-5

#### CS-AC-04 DNS 重定向方案（REDIRECT，DNS 解析层重写）

- **核心机制**：构造新的 DNS 响应（DNS Overwriting），IP 指向第三方 Platform，在用户建立 TCP 之前介入
- **动作类型**：REDIRECT
- **动作轨道**：轨道 A（PCC 体系）
- **配置链**：EXTENDEDFILTER（URL）→ ERRORCODE（DNS 错误码）→ DNSOVERWRITING → RULE（POLICYTYPE=SMARTREDIRECT） → USERPROFILE
- **触发方式**：DNS 查询失败（如 NXDOMAIN 错误码 = 3）
- **uses_feature**：GWFD-110283（DNS 纠错）、GWFD-020357（ADC，DNS 解析前置）
- **关键参数**：DNSOVERWRITING.*、ERRORCODE（EQUAL 3 等 DNS 错误码）
- **决策分支**：与 HTTP 重定向共用 POLICYTYPE=SMARTREDIRECT，区分点在 POLICYNAME 指向对象类型
- **典型场景**：错误域名引导、错页提示
- **协议限制**：仅 UDP DNS，不支持 TCP DNS
- **来源批次**：Batch-06 KP-3/4

#### CS-AC-05 Portal/WebProxy 重定向方案（REDIRECT，L7 HTTP/L3 IP NAT）

- **核心机制**：通过 IP Farm 服务器集群实现重定向，Portal 为周期性 captive/non-captive 交替，WebProxy 为透明 IP NAT
- **动作类型**：REDIRECT（Portal）/ REDIRECT+代理（WebProxy）
- **动作轨道**：轨道 A（PCC 体系）
- **配置链**：
  - Portal：IPFARM + IPFARMSERVER + LOGICINF → PCCPOLICYGRP（含 captive） → USERPROFILE（含 CAPMODETHRES）
  - WebProxy：IPFARM + IPFARMSERVER + LOGICINF + BLACKLISTRULE → RULE（POLICYTYPE=WEBPROXY） → USERPROFILE
- **触发方式**：
  - Portal：用户首次 HTTP 请求 + CAPMODETHRES 定时器周期触发
  - WebProxy：TCP SYN 匹配规则
- **uses_feature**：GWFD-110281（用户 Portal）、GWFD-110282（WebProxy）、GWFD-020357（ADC，Portal 依赖）
- **关键参数**：IPFARM.LBMETHOD（ROUND_ROBIN/LEAST_RECENTLY_USED/LEAST_LOAD）、IPFARM.HEALTHSUCCLIMIT/HEALTHFAILLIMIT、USERPROFILE.CAPMODETHRES、DEFAULTACT=BLOCK（Portal 全 DOWN 时）
- **决策分支**：用户需要感知重定向？→ Portal；需要透明代理？→ WebProxy；需要处理 HTTPS？→ 仅 WebProxy（L3 不依赖 L7 解析）
- **典型场景**：Portal 业务订购/广告推送；WebProxy 网络加速/病毒防护/内容过滤
- **协议限制**：Portal 仅 HTTP1.x/WAP（不支持 HTTPS）；WebProxy 无协议限制（纯 IP 层）
- **来源批次**：Batch-06 KP-2/6

#### CS-AC-06 URL 过滤方案（BLOCK/PERMIT/REDIRECT，CFTEMPLATE.ACTION 独立体系）

- **核心机制**：通过 ICAP 协议将用户访问的 URL 上送给外部 ICAP Server 分类，根据返回的分类匹配本地套餐策略执行 BLOCK/PERMIT/REDIRECT
- **动作类型**：BLOCK/PERMIT/REDIRECT（显式指定，**唯一支持 PERMIT 的方案**）
- **动作轨道**：轨道 B（URL 过滤体系，独立于 PCC 体系）
- **配置链**：VPNINST + LOGICINF + ICAPSERVER + ICAPSVRGRP（互通）→ APN + APNCFFUNC + CFPROFILE + CFTEMPLATE（含 ACTION） + APNCFTEMPLATE + CFPROFBINDCFT + CONTCATEGROUP + CONTCATEGBIND（含 ACTION）
- **触发方式**：URL 分类匹配（ICAP REQMOD 上送）
- **uses_feature**：GWFD-110471（URL 过滤基本功能）、GWFD-020357（ADC，URL 解析前置）
- **关键参数**：CFTEMPLATE.ACTION（BLOCK/PERMIT/REDIRECT）、CONTCATEGBIND.ACTION（分类级动作）、CFCACHEPARA（本地缓存加速）
- **决策分支**：需要外部 URL 分类数据库？→ 用轨道 B；HTTPS 场景？→ 仅基于 SNI（不能完整 URL）
- **典型场景**：家长控制、企业内容过滤、合规要求
- **协议限制**：HTTP 完整 URL；HTTPS 仅 SNI
- **来源批次**：Batch-07 KP-1/2

#### CS-AC-07 接入控制方案（基于位置/区域/用户类型的访问限制）

- **核心机制**：在注册/会话阶段基于 SAR/区域漫游/ODB/服务区域限制等进行粗粒度接入控制
- **动作类型**：拒绝接入（DISCARD 的粗粒度版本）
- **动作轨道**：UNC 侧独立（非 UDG 侧 PCC 体系）
- **配置链**：
  - 移动接入控制：AMF 的 SAR / 区域漫游限制 / ODB
  - 位置触发：USRLOCATION + USRLOCATIONGRP + UPBINDUPG + APNUSRPROFG
- **触发方式**：用户注册（LOC_CH/SERV_AREA_CH）、PRA 变化（PRA_CH）、PLMN 变更（PLMN_CH）
- **uses_feature**：WSFD-211001（基于初始接入位置的策略控制）、WSFD-106003（用户接入控制 AMF）、WSFD-105003（区域漫游限制 AMF）、WSFD-106005（支持 ODB AMF）、WSFD-105006（服务区域限制）
- **关键参数**：USRLOCATION（CGI/ECGI/NCGI）、SAR（TAI 允许/禁止列表）、USRLOCATIONGRP（位置组批量绑定）
- **决策分支**：限制级别？系统级/用户级/区域级；限制对象？RAT/核心网/号段/单用户/TAI
- **典型场景**：区域套餐（只能在 A 市用）、漫游限制、ODB 欠费禁用、拥塞小区流控
- **来源批次**：Batch-03 KP-04（LOC_CH/SERV_AREA_CH/PRA_CH）、Batch-07 KP-3/4

#### CS-AC-08 配额耗尽重定向方案（REDIRECT，FUP+SM 策略协同）

- **核心机制**：FUP 配额耗尽触发 US_RE/NO_CREDIT 事件，PCF 决策下发携带 RedirectInformation 的 PCC 规则，重定向到充值页
- **动作类型**：REDIRECT
- **动作轨道**：轨道 A（PCC 体系）+ PCF 决策
- **配置链**：UPCF 配额 + 触发器（US_RE/NO_CREDIT）+ 条件组 + 动作组（含重定向）→ PCF 通过 N7 下发 → SMF 映射 N4 → UPF 执行
- **触发方式**：流量配额耗尽（VOLQU）/ 时长配额耗尽（TIMQU）/ 信用失效（NO_CREDIT）
- **uses_feature**：GWFD-020351（PCC）、WSFD-109101（PCC UNC）、GWFD-110284（HTTP 智能重定向，可执行重定向）
- **关键参数**：UPCF 动作组.重定向、RedirectInformation（URL）、配额阈值（VolumeThreshold/TimeThreshold）
- **决策分支**：规则类型？动态规则（PCF 实时决策）；需重定向到充值页？→ RedirectInformation.URL
- **典型场景**：套餐耗尽重定向充值页、信用失效重定向
- **来源批次**：Batch-01 KP-10（业务 5 重定向）、Batch-03 KP-11（重定向两大场景）

#### CS-AC-09 区域引导重定向方案（REDIRECT，基于 PRA/PLMN 触发）

- **核心机制**：用户进入特定位置区域（PRA）或漫游（PLMN 变更）时，PCF 决策下发重定向策略到套餐订购/免费接入验证页面
- **动作类型**：REDIRECT
- **动作轨道**：轨道 A（PCC 体系）+ PCF 决策 + 位置触发
- **配置链**：WSFD-211001（USRLOCATION）+ UPCF 触发器（PRA_CH/PLMN_CH/SAREA_CH）+ 条件组 + 动作组（重定向）→ PCF → SMF → UPF
- **触发方式**：PRA 变化（PRA_CH）、PLMN 变更（PLMN_CH）、服务区域变化（SAREA_CH）
- **uses_feature**：WSFD-211001（基于初始接入位置的策略控制）、GWFD-110284（HTTP 智能重定向）、GWFD-110281（用户 Portal）
- **关键参数**：USRLOCATION（位置）、RedirectInformation（URL，套餐订购页/验证页）
- **决策分支**：重定向目标？套餐订购页（Portal）/ 免费接入验证页（HTTP 重定向）
- **典型场景**：出国引导签约优惠套餐、热点接入区域引导订购
- **来源批次**：Batch-03 KP-11（重定向两大场景之"进入特定位置区域"）、Batch-07 KP-4

### 6.4 决策点（DP）归纳 — ★ 第 1 层核心 ★

访问限制场景的决策点（DP, Decision Point）共 **8 个**：

#### DP-AC-01 动作类型选择决策

- **决策问题**：访问限制应执行哪种动作？
- **决策位置**：PCF 策略生成阶段 / UPF 规则匹配阶段
- **option_set**：
  - DISCARD（阻塞）：禁止访问非法内容/IP → CS-AC-01
  - HEADEN（头增强）：插入用户信息字段支持业务认证 → CS-AC-02
  - REDIRECT（重定向）：引导到指定页面/服务器 → CS-AC-03/04/05/08/09
  - PERMIT（放行）：显式允许通过（仅 URL 过滤） → CS-AC-06
- **impact**：决定配置链路、ConfigObject 选择、License 需求
- **决策依据**：业务目标（阻塞/引导/认证/放行）
- **来源批次**：Batch-01 KP-05、Batch-02 KP-05

#### DP-AC-02 规则类型选择决策

- **决策问题**：访问限制规则应使用动态、预定义还是本地？
- **决策位置**：PCF/SMF 策略规划阶段
- **option_set**：
  - 动态规则：PCF 实时生成，灵活但**无法包含 7 层过滤条件**
  - 预定义规则：UPF 本地预配，PCF 按名激活，**支持 7 层**（URL 过滤/定向业务必须用）
  - 本地规则：SMF 兜底（PCF 故障时），不可实时更新
- **impact**：决定规则的生命周期、三网元一致性要求、是否支持 L7 识别
- **决策依据**：
  - 需要 L7 应用识别？是 → 必须用预定义规则（PCF 无 L7 能力）
  - 需要实时决策？是 → 动态规则
  - PCF 故障兜底？→ 本地规则
- **优先级**（同优先级时）：动态 > 预定义 > 本地
- **来源批次**：Batch-01 KP-06、Batch-02 KP-13、Batch-03 KP-09

#### DP-AC-03 动作轨道选择决策（★ 双轨核心 ★）

- **决策问题**：访问限制动作走轨道 A（PCC 体系）还是轨道 B（URL 过滤体系）？
- **决策位置**：方案设计阶段
- **option_set**：
  - 轨道 A（PCC 体系）：RULE.POLICYTYPE 驱动，动作隐式，多维度匹配，可选 PCRF/PCF → ADC/头增强/重定向族走这条
  - 轨道 B（URL 过滤体系）：CFTEMPLATE/CONTCATEGBIND.ACTION 驱动，动作显式，单维度（URL 分类）匹配，必需 ICAP Server → URL 过滤走这条
- **impact**：决定 ConfigObject 体系、动作指定方式、外部依赖、是否支持 PERMIT
- **决策依据**：
  - 需要基于应用/用户属性/IP/错误码等多维度？→ 轨道 A
  - 需要基于 URL 分类的家长控制/企业过滤？→ 轨道 B
  - 需要外部 URL 分类数据库？→ 轨道 B
  - 需要显式 PERMIT 动作？→ 轨道 B
- **双轨协同**：两条轨道可并存于同一用户，业务流先后被检查
- **来源批次**：Batch-07 发现-1（核心发现）

#### DP-AC-04 网元范围选择决策

- **决策问题**：访问限制规则应下发到哪些网元/UPF？
- **决策位置**：SMF 策略下发阶段
- **option_set**：
  - UPF 执行（业务流阶段细粒度）：UDG 侧配置
  - SMF 决策+翻译：UNC 侧配置
  - AMF 接入控制（注册阶段粗粒度）：SAR/区域/ODB
  - 主+辅锚点 UPF（RULERANGE=ALL）
  - 仅主锚点 UPF（RULERANGE=CENTRAL）
  - 仅辅锚点 UPF（RULERANGE=LOCAL）
  - 指定辅锚点 UPF（DNAI 粒度）
- **impact**：决定规则生效范围、配置一致性要求、部署复杂度
- **决策依据**：业务粒度（粗/细）、UPF 角色、DNAI 需求
- **来源批次**：Batch-02/03、Batch-07 KP-3

#### DP-AC-05 匹配层次选择决策

- **决策问题**：访问限制应基于哪个协议层匹配？
- **决策位置**：UPF 规则配置阶段
- **option_set**：
  - L3/L4（三四层）：IP/端口/协议 → IP 阻塞、端口封锁
  - L7（七层）：URL/SNI/Method/UserAgent → URL 过滤、内容过滤
  - DNS 层：DNS 查询 → DNS 纠错
  - 应用层（ADC）：应用标识 → ADC 触发动作
- **impact**：决定 Filter 类型（FILTER/L7FILTER/EXTENDEDFILTER）、SA 依赖、协议限制
- **决策依据**：
  - 基于 IP/端口？→ L3/L4
  - 基于 URL？→ L7（需预定义规则，动态规则不支持 L7）
  - 基于域名解析失败？→ DNS 层
  - 基于应用类型？→ 应用层（ADC）
- **HTTPS 场景限制**：L7 只能基于 SNI（不能完整 URL）
- **来源批次**：Batch-01 KP-04/08、Batch-04/05/06/07

#### DP-AC-06 重定向目标选择决策

- **决策问题**：REDIRECT 动作应重定向到哪种目标？
- **决策位置**：方案设计阶段
- **option_set**：
  - 充值页面（配额耗尽）：CS-AC-08
  - 套餐订购页面（区域引导）：CS-AC-09，Portal
  - Portal 服务器（业务订购/管理）：CS-AC-05 Portal
  - Proxy 服务器（网络加速/病毒防护）：CS-AC-05 WebProxy
  - 第三方服务器（URL 纠错/内容过滤）：CS-AC-03/06
  - 第三方 Platform（错误域名引导）：CS-AC-04 DNS 纠错
- **impact**：决定重定向特性选择（HTTP 重定向/DNS/Portal/WebProxy）、IP Farm 需求、EXTENDEDFILTER 需求
- **决策依据**：业务目标（充值/订购/纠错/加速）、用户感知（透明/非透明）、协议（HTTP/HTTPS/TCP）
- **来源批次**：Batch-06 KP-1

#### DP-AC-07 协议支持决策

- **决策问题**：访问限制方案需支持哪些协议？
- **决策位置**：方案设计阶段
- **option_set**：
  - 仅 HTTP1.x：HTTP 智能重定向、用户 Portal、HTTP 头增强、头防欺诈
  - HTTP1.x + HTTPS（TLS 1.2/1.3）：HTTPS 头增强、URL 过滤（仅 SNI）
  - HTTP1.x + RTSP：RTSP 头增强
  - 任意 TCP（含 HTTPS/HTTP2.0）：**仅 WebProxy**（L3 IP NAT 不依赖 L7 解析）
  - DNS（UDP）：DNS 纠错
- **impact**：决定特性选择、SA 依赖、加密算法需求
- **决策依据**：目标业务协议、是否加密、是否需要 L7 解析
- **关键启示**：**仅 WebProxy 能处理加密协议**（因其在 L3 工作）
- **来源批次**：Batch-05 KP-4、Batch-06 发现-4

#### DP-AC-08 PCF 故障容灾决策

- **决策问题**：PCF 故障时访问限制策略如何保证连续性？
- **决策位置**：SMF 容灾配置阶段
- **option_set**：
  - 回落本地 PCC（SET PCCFAILACTION 配置）：保证业务连续性，但精细化程度低
  - 会话失败：严格模式，无兜底
  - DNN 粒度混合（动态+本地）：部分 DNN 用本地 PCC，部分用动态 PCC
- **impact**：决定访问限制策略的可靠性、容灾能力
- **决策依据**：业务连续性要求、PCF 部署情况、DNN 差异化需求
- **来源批次**：Batch-03 KP-02、发现-7

### 6.5 调测验证方法论

综合 Batch-02（UDG 调测）和 Batch-03（UNC SM 策略调测），访问限制场景的调测验证应遵循渐进式方法论：

**第一步：基础设施验证**
- 检查 License 状态：`SET LICENSESWITCH` 确认各访问限制子能力已启用
- 检查强依赖：防欺诈需同时开启头增强；ADC 需 SA-Basic + PCC
- 检查 SA 引擎状态：业务识别签名库已加载
- 检查网元连通性：PCF↔SMF（N7）、SMF↔UPF（N4）链路正常

**第二步：规则配置验证**
- UDG 侧：`LST` 系列命令查看规则安装状态（LST USERPROFILE/RULEBINDING/RULE/FLOWFILTER/FILTER/PCCPOLICYGRP/URRGROUP）
- UNC 侧：`DSP PCCSESSINFO` 查看 PCC 会话
- 检查三网元一致性：预定义规则名、URR ID 在 PCF/SMF/UPF 一致
- 检查双轨配置：轨道 A（RULE.POLICYTYPE）与轨道 B（CFTEMPLATE.ACTION）是否冲突

**第三步：业务功能验证**
- 验证 N4 接口 PFCP Session Establishment Request 存在
- 激活响应 PFCP Session Establishment Response 返回 Cause = request-accepted (1)
- 发起测试流量，确认业务识别正确（SA 七步流程前三步）
- 确认规则匹配正确（第四步）——通过调测日志验证匹配到的规则名
- 确认动作执行正确（第五步）——DISCARD 报文被丢弃/REDIRECT 跳转正确页面/HEADEN 头字段正确插入

**第四步：异常场景验证**
- PCF 故障：验证本地 PCC 兜底（SET PCCFAILACTION）
- Portal/WebProxy 全部 DOWN：验证 Portal DEFAULTACT=BLOCK / WebProxy 不做重定向
- ICAP Server 不可用：验证 URL 过滤缺省动作（CFTEMPLATE.ACTION 默认值）
- 加密协议场景：验证 HTTPS 仅 SNI、RTSP 不支持防欺诈等限制

**第五步：反向追踪**
- 从用户体验问题出发，反向追踪：访问失败 → UPF 执行日志 → N4 规则 → N7 策略 → PCF 决策 → 用户签约
- `SET REFRESHSRV` 必须在 Filter 变更后执行（60 秒延迟生效）

---

## 7. 关键发现与隐藏关系

### 7.1 发现 1：双轨动作机制是访问限制场景的核心架构事实

**现象**（Batch-07 发现-1）：访问限制动作存在两条完全独立的轨道路径——轨道 A（PCC 体系，RULE.POLICYTYPE 驱动）与轨道 B（URL 过滤体系，CFTEMPLATE/CONTCATEGBIND.ACTION 驱动）。

**深层原因**：
- 轨道 A 继承自 3GPP PCC 标准（TS 23.503），动作通过 POLICYTYPE 隐式表达，匹配维度丰富（L3/L4/L7/错误码/UserAgent）
- 轨道 B 是 UDG 特有的 URL 过滤增强，引入外部 ICAP Server，动作显式指定（BLOCK/PERMIT/REDIRECT），匹配维度单一（URL 分类）
- 两条轨道解决不同问题：轨道 A 处理"基于网络/用户/应用属性的访问控制"；轨道 B 处理"基于内容分类的访问控制"

**配置影响**：
- 同一用户可同时被两条轨道检查，业务流先后匹配
- URL 过滤虽然 RULE 用 POLICYTYPE=PCC，但其动作不走 PCCPOLICYGRP，而是走独立的 CFTEMPLATE/CONTCATEGBIND
- **图谱落位**：RULE 对象需要 `policy_track` variant_dimension；CFTEMPLATE/CONTCATEGBIND 独立建模

### 7.2 发现 2：PERMIT 动作的唯一性（URL 过滤独有）

**现象**（Batch-07 发现-5）：**URL 过滤是访问限制场景中唯一显式支持 PERMIT 动作的特性**。轨道 A 的特性（ADC/头增强/重定向）主要是"不做动作"（隐式放行）或"做阻塞/重定向"，没有显式 PERMIT。

**深层原因**：
- 轨道 A 的设计哲学是"默认放行，命中规则才动作"
- 轨道 B 的设计哲学是"基于白名单/黑名单分类，显式决策"——ICAP Server 返回分类后，必须明确决定 BLOCK/PERMIT/REDIRECT
- URL 过滤的 CFTEMPLATE.ACTION 需要"缺省动作"（如 PERMIT 作为兜底），这是分类决策的必然要求

**配置影响**：
- 家长控制、企业内容过滤等"白名单场景"必须用 URL 过滤（轨道 B）
- 黑名单场景（阻塞特定 IP/URL）可用轨道 A 或轨道 B
- **图谱落位**：动作类型对象应区分"显式 PERMIT（轨道 B 独有）"与"隐式放行（轨道 A）"

### 7.3 发现 3：动态规则的七层限制（重大架构约束）

**现象**（Batch-01 KP-06、Batch-02 KP-13、Batch-03 KP-09）：动态规则（PCF 规划）**无法包含 7 层过滤条件**，基于 URL 的访问限制只能用预定义规则或本地规则实现。

**深层原因**：
- PCF 只有 L3/L4 识别能力（IP/端口/协议），无 L7 应用层识别能力
- UPF 具备 L7 识别能力（URL/HOST/七层协议），但动态规则由 PCF 生成
- 因此涉及 L7 的访问限制（URL 过滤、定向业务阻塞）必须用 UPF 侧的静态规则（预定义/本地）

**配置影响**：
- URL 过滤（GWFD-110471）的规则类型必须为预定义规则
- 定向业务阻塞（如阻塞特定 APP）也必须用预定义规则
- 动态规则只能做 IP/端口级阻塞（如配额耗尽重定向——基于会话属性而非 L7）
- **图谱落位**：feature→rule_type 关系应标注此约束；URL 过滤类特性只能关联预定义/本地规则

### 7.4 发现 4：头防欺诈与头增强的强耦合（最显著的依赖关系）

**现象**（Batch-08 发现-1）：头防欺诈（GWFD-110401）**完全寄生**于头增强配置链路，没有独立 MML 命令。防欺诈开关 ANTIFRAUD 和灰名单 GRAYLIST 全部内嵌于 `ADD HEADEN` 命令。

**深层原因**：
- 防欺诈的本质是"头增强的前置安全检测"——检查已有字段是否被伪造
- 防欺诈不产生独立访问限制动作，它保障的是头增强插入字段的真实性
- 执行顺序：**防欺诈检测 → 字段纠正/冗余清理 → 头增强插入**（灰名单模式下跳过插入）

**配置影响**：
- 启用防欺诈必须同时开启头增强（双 License：82209786 + 82209777）
- 防欺诈应建模为**头增强对象的 variant/属性**，而非独立特性
- RTSP 头增强不支持防欺诈（族内唯一例外，Batch-08 发现-4 安全盲区）
- **图谱落位**：`110401 constrained_by 110261`；HEADEN 对象的 `variant_dimensions` 包含 `antifraud_enabled`

### 7.5 发现 5：ADC 是所有 L7 动作的共同前置（横切依赖）

**现象**（Batch-04 发现-1）：ADC（GWFD-020357）不直接产生访问限制动作，但它是访问限制场景的"**眼睛**"——所有需要基于应用/URL 做判断的特性都依赖 ADC/SA 的解析能力。

**深层原因**：
- ADC 提供 L7 应用识别（应用标识、URL、五元组、Method、Content-Type）
- 头增强、HTTP 智能重定向、DNS 纠错、用户 Portal、URL 过滤均需基于 ADC/SA 的解析能力匹配规则
- ADC 本身有两种触发链路：本地 ADC 规则直接触发（POLICYTYPE=ADC）+ PCRF/PCF 动态决策（POLICYTYPE=PCC + Application ID）

**配置影响**：
- 访问限制场景中的所有 L7 动作特性应标注"constrained_by ADC/SA 解析能力"
- ADC 的兜底阻塞机制（匹配不上所有规则时 UDG 阻塞业务流）需配置 L3/4=any、L7=any 的缺省规则避免误阻塞
- ADC 使能后会对所有业务进行 L7 解析，带来数据面性能下降、N4/N7 信令增多——需配合 ADCHYSTTIMER 控制上报频率
- **图谱落位**：ADC 应建模为一条横切依赖关系（constrained_by 边）

### 7.6 发现 6：重定向族四层级介入时序的设计逻辑

**现象**（Batch-06 KP-1）：重定向族四个特性分别在不同协议层介入，时序为：DNS 纠错（最早）→ WebProxy（建立 TCP 时）→ HTTP 智能重定向（HTTP 响应时）→ 用户 Portal（定时主动触发）。

**深层原因**：
- 介入越早，对用户感知影响越小，但能获取的信息越少
- DNS 纠错在 DNS 解析层介入，用户还未建立 TCP，但只能基于域名
- WebProxy 在 L3 IP NAT 层介入，透明无感知，但只能基于 IP（无协议限制，**唯一能处理 HTTPS/HTTP2.0**）
- HTTP 智能重定向在 L7 HTTP 响应介入，能基于 URL/UserAgent/错误码，但受 HTTP1.x 限制
- 用户 Portal 是唯一周期性触发（captive/non-captive 交替，CAPMODETHRES 定时器）

**配置影响**：
- 选择重定向方式时需考虑：介入时机、用户感知、协议支持、目标服务器类型
- 仅 WebProxy 能处理加密协议——HTTPS/HTTP2.0 场景的重定向必须用 WebProxy
- **图谱落位**：REDIRECT 动作对象的 `variant_dimensions` 包含 `redirect_layer`（DNS/L3/L7-HTTP/L7-Portal）

### 7.7 发现 7：UPCF 动作组的官方枚举厘清重定向在 PCF 策略层的定义

**现象**（Batch-03 KP-07）：UPCF 侧动作组明确包括"带宽控制、计费控制、**消息通知**和**重定向**"。特别是"重定向：套餐耗尽后，禁止上网，重定向到运营商充值首页"——这是 PCF 策略层对访问限制 REDIRECT 动作的官方定义。

**深层原因**：
- SM 策略三方面内容：QoS + 计费参数 + **短信或重定向**（Batch-03 KP-05）
- 重定向作为 SM 策略的独立内容类型，是访问限制 REDIRECT 动作的**策略层定义点**
- 重定向的两大触发场景（Batch-03 KP-11）：基于配额/资费消耗（充值页）+ 进入特定位置区域（套餐订购/验证页）

**配置影响**：
- 重定向策略在 PCF 侧完整定义（PCF 决策垄断，无协商）
- 重定向可通过 UPCF 动作组的 RedirectInformation 参数下发 URL
- 短信通知可与重定向并用（UPCF 通过 SMSC/Email/SOAP 发送通知）
- **图谱落位**：业务层（BD）的"重定向业务规则"应关联 SM 策略的"短信或重定向"内容对象

### 7.8 发现 8：规则匹配类型独立原则允许动作叠加

**现象**（Batch-01 KP-09、发现-5）：同一条报文可同时命中 PCC+BWM+HEADEN 各一条规则，三种动作叠加执行（如阻塞+限速+插头）。

**深层原因**：
- 规则匹配类型独立原则：不同类型规则之间匹配独立进行（PCC/BWM/HEADEN 互不干扰）
- 每种类型至多一条生效，但不同类型可叠加
- 这是访问限制动作能与带宽控制、计费并存的理论基础

**配置影响**：
- 业务层规则关系应体现"并行叠加"语义，而非互斥
- 一条 HTTP 访问可同时执行：DISCARD（PCC 阻塞）+ 限速（BWM）+ 头增强（HEADEN）——虽然阻塞会丢弃报文，但匹配阶段三者独立判断
- **图谱落位**：BusinessRule 关系应支持"并行"语义

### 7.9 发现 9：一条规则只能绑定一条策略的强约束

**现象**（Batch-01 发现-6）：规则与策略是 1:1 关系，策略与动作类型是 1:1 关系。

**深层原因**：
- 规则（RULE）是业务感知的最小单元，绑定过滤条件+策略+优先级
- 若要同一流量同时执行阻塞和重定向，**不能用一条规则**，必须通过两条不同优先级的规则分别承载

**配置影响**：
- 复合动作需求（如阻塞+重定向）需配置多条规则
- Rule→Policy 是单向 1:1 边，非多对多
- **图谱落位**：ConfigObject 关系边应体现此 1:1 约束

### 7.10 发现 10：PCF 决策垄断决定访问限制策略必须 PCF 侧完整定义

**现象**（Batch-03 KP-06、发现-3）：SM 策略生成"完全由 PCF 决策，不存在与 UDM、SMF 协商的过程"。

**深层原因**：
- PCF 能根据用户位置、等级、时间段、配额状态、节假日等灵活定制
- UDM 提供签约信息，但不参与策略决策
- SMF 仅执行翻译和下发，不参与决策

**配置影响**：
- 访问限制的策略逻辑（如"套餐耗尽→重定向"、"进入 PRA→重定向"）必须在 PCF 侧完整定义
- 本地 PCC（SMF 决策）的精细化程度低于 PCF 策略
- **图谱落位**：访问限制策略决策点是 PCF，非 SMF/UDM

### 7.11 发现 11：UNC 侧接入控制与 UDG 侧访问限制构成完整链路

**现象**（Batch-07 发现-2）：UNC 侧的接入控制（注册/会话阶段粗粒度）+ UDG 侧的访问限制（业务流阶段细粒度）共同构成完整链路。

**深层原因**：
- UNC 侧决策"是否允许接入"（基于 SAR/区域/ODB/号段）
- UDG 侧决策"允许做什么"（基于应用/URL/IP/用户属性）
- WSFD-211001 是连接两层的关键桥梁（在 UNC 侧用 ULI 匹配位置，下发策略到 UDG 执行）

**配置影响**：
- 完整的访问限制方案需同时考虑 UNC 侧（接入控制）和 UDG 侧（业务控制）
- 位置触发的访问限制必须用 WSFD-211001（UNC 侧）+ UDG 侧执行特性
- **图谱落位**：业务层（BD）应同时包含 UNC 侧接入控制对象和 UDG 侧访问控制对象

### 7.12 发现 12：头增强族的统一配置接口（POLICYTYPE=HEADEN）

**现象**（Batch-05 发现-2）：所有头增强族特性（HTTP/HTTPS/RTSP/NSH）通过**同一个 RULE POLICYTYPE**（HEADEN）被引用。

**深层原因**：
- 头增强族的差异化主要通过 `RULE.POLICYTYPE` 区分，这是头增强与其他动作（ADC、SMARTREDIRECT、WEBPROXY、PCC）并列的关键接口
- 族内共用 `ADD HEADEN` 命令，差异仅在"解析 SA 特性依赖"和"字段插入位置"

**配置影响**：
- HEADEN 是一个跨协议复用的 ConfigObject，其 `variant_dimensions` 应包含 `protocol_type`（HTTP/HTTPS/RTSP/NSH）
- 访问限制动作的差异化主要通过 `RULE.POLICYTYPE` 区分——这是图谱建模 RULE 对象时的核心 variant_dimension
- **图谱落位**：RULE 对象的 `policy_type` variant_dimension 是访问限制建模的关键

---

## 8. 附录

### 8.1 批次索引与主题映射

| 批次 | 主题 | 产品 | 与访问限制关联度 | 核心贡献 |
|------|------|------|------------------|----------|
| Batch-01 | SA 基础概念 | UDG | ★★★★★ | SA 七步流程、5 种策略类型、3 种规则类型、规则匹配三原则 |
| Batch-02 | PCC 基本功能（UDG） | UDG | ★★★★★ | PCC 动作官方枚举、N7→N4 链路、7 步 MML 配置、静态规则机制 |
| Batch-03 | PCC-SM 策略下发（UNC） | UNC | ★★★★★ | SM 策略三内容、UPCF 动作组、PCR Trigger、重定向两大场景 |
| Batch-04 | ADC 核心机制 | UDG | ★★★★☆ | L7 应用识别、兜底阻塞、两条触发链路、ConfigObject 复用矩阵 |
| Batch-05 | 头增强族 | UDG | ★★★★☆ | HEADEN 统一接口、族内差异、加密与编码机制、防欺诈耦合 |
| Batch-06 | 重定向族 | UDG | ★★★★★ | 四种层级实现、IP Farm 机制、EXTENDEDFILTER、协议层互斥 |
| Batch-07 | URL 过滤与接入控制 | UDG+UNC | ★★★★★ | **双轨动作机制**、UNC 接入控制、位置触发、PERMIT 唯一性 |
| Batch-08 | 防欺诈 | UDG | ★★★ | 头防欺诈机制、强耦合头增强、灰名单模式、协议覆盖盲区 |

### 8.2 双轨动作矩阵（核心架构）

| 维度 | 轨道 A（PCC 体系） | 轨道 B（URL 过滤体系） |
|------|-------------------|----------------------|
| **核心 ConfigObject** | RULE（POLICYTYPE 差异化） | CFTEMPLATE + CONTCATEGBIND |
| **动作指定方式** | 隐式（POLICYTYPE 决定） | 显式（ACTION=BLOCK/PERMIT/REDIRECT） |
| **匹配维度** | 多维度（L3/L4/L7/错误码/URL/UserAgent...） | 单维度（URL 分类） |
| **外部依赖** | 可选 PCRF/PCF | **必需 ICAP Server** |
| **动作类型** | 隐式阻塞、头增强、重定向改写 | 直接 BLOCK/PERMIT/REDIRECT |
| **PERMIT 支持** | 不支持 | **★唯一显式支持★** |
| **典型 MML 命令** | ADD RULE, ADD PCCPOLICYGRP, ADD HEADEN, ADD SMARTHTTPREDIR | ADD CFTEMPLATE, ADD CONTCATEGBIND, ADD ICAPSERVER |
| **独立配置体系** | 共用 FILTER/FLOWFILTER/USERPROFILE | 独有 APNCFFUNC/CFPROFILE/CFTEMPLATE/CONTCATEGROUP/ICAP* |
| **License 共用** | 各特性独立 License | URL 过滤独立 License（82200FCP UFBF01） |
| **走此轨道的特性** | ADC、头增强族、防欺诈、重定向族 | URL 过滤基本功能 |

### 8.3 规则类型决策树

```
需要 L7 应用/URL 识别？
├─ 是 → 必须用预定义规则（PCF 无 L7 能力）
│       ├─ URL 过滤、定向业务阻塞
│       └─ 三网元一致性要求（PCF/SMF/UPF 规则名一致）
└─ 否 → 可用动态规则或本地规则
        ├─ 需要实时决策？→ 动态规则（PCF 实时生成）
        │   └─ 配额耗尽重定向、IP 类访问限制
        └─ PCF 故障兜底/固定策略？→ 本地规则（SMF 决策）
            └─ 不可实时更新，需用户下次上线才生效

优先级（同优先级时）：动态规则 > 预定义规则 > 本地规则
```

### 8.4 动作类型决策树

```
业务目标是什么？
├─ 禁止访问（非法内容/IP）→ DISCARD（阻塞）
│   ├─ PCC 兜底阻塞（CS-AC-01）
│   ├─ ADC 兜底阻塞
│   └─ URL 过滤 BLOCK（CS-AC-06）
├─ 引导到指定页面 → REDIRECT（重定向）
│   ├─ 配额耗尽？→ 充值页（CS-AC-08）
│   ├─ 区域引导？→ 套餐订购页（CS-AC-09）
│   ├─ URL 纠错？→ HTTP 智能重定向（CS-AC-03）
│   ├─ 域名错误？→ DNS 纠错（CS-AC-04）
│   ├─ 业务订购？→ 用户 Portal（CS-AC-05）
│   ├─ 网络加速？→ WebProxy（CS-AC-05）
│   └─ URL 分类？→ URL 过滤 REDIRECT（CS-AC-06）
├─ 插入用户信息 → HEADEN（头增强）
│   ├─ 需要防欺诈？→ 启用 ANTIFRAUD（CS-AC-02）
│   └─ 协议？→ HTTP/HTTPS/RTSP 头增强（CS-AC-02）
└─ 显式放行 → PERMIT（仅 URL 过滤，CS-AC-06）
```

### 8.5 重定向方式决策树

```
需要重定向？
├─ 协议是 HTTPS/HTTP2.0？
│   └─ 是 → 仅 WebProxy（L3 IP NAT，不依赖 L7 解析）
├─ 基于错误码/URL/UserAgent 多条件？
│   └─ HTTP 智能重定向（L7 HTTP 响应）
├─ 基于域名解析失败？
│   └─ DNS 纠错（DNS 解析层，最早介入）
├─ 需要周期性触发业务订购？
│   └─ 用户 Portal（captive/non-captive 交替）
├─ 需要透明代理（用户无感知）？
│   └─ WebProxy（L3 IP NAT）
└─ 目标服务器类型？
    ├─ 第三方服务器 → HTTP 智能重定向
    ├─ 第三方 Platform → DNS 纠错
    ├─ Portal Server → 用户 Portal
    └─ Proxy Server → WebProxy
```

### 8.6 核心 MML 命令速查（按轨道分类）

#### 轨道 A — PCC 体系共用命令

| 命令 | 用途 | 关键参数 | 来源批次 |
|------|------|----------|----------|
| ADD FILTER | 三四层过滤器 | FILTERNAME, L34PROTTYPE, L34PROTOCOL | Batch-02 |
| ADD FLOWFILTER | 流过滤器 | FLOWFILTERNAME | Batch-02 |
| ADD FLTBINDFLOWF | 流过滤器-过滤器绑定 | FLOWFILTERNAME, FILTERNAME | Batch-02 |
| ADD L7FILTER | 七层过滤器 | L7FILTERNAME（URL/SNI） | Batch-04/05/07 |
| ADD PROTBINDFLOWF | 协议绑定 | PROTOCOLNAME, FLOWFILTERNAME, L7FILTERNAME | Batch-04/05 |
| ADD PCCPOLICYGRP | PCC 策略组 | PCCPOLICYGRPNM, URRGROUPNAME, ADCMUTEFLAG | Batch-02/04 |
| ADD URR / ADD URRGROUP | 使用量上报规则 | URRID, USAGERPTMODE | Batch-02 |
| ADD USERPROFILE | 用户模板 | USERPROFILENAME, CAPMODETHRES（Portal） | Batch-02/06 |
| ADD RULEBINDING | 规则-用户模板绑定 | USERPROFILENAME, RULENAME | Batch-02 |
| SET LICENSESWITCH | License 开关 | LICITEM, SWITCH | 全批次 |
| SET REFRESHSRV | 刷新生效（最后执行） | REFRESHTYPE | 全批次 |

#### 轨道 A — 头增强族命令

| 命令 | 用途 | 关键参数 | 来源批次 |
|------|------|----------|----------|
| ADD HEADEN | 头增强对象（族共用） | HEADERENNAME, DATATYPE, PREFIXNAME, ENCRYALGORI, PSWDKEY, ANTIFRAUD, GRAYLIST | Batch-05/08 |
| SET BASE64 | 编码开关 | - | Batch-05 |
| ADD RULE（POLICYTYPE=HEADEN） | 头增强规则 | RULENAME, POLICYTYPE=HEADEN, POLICYNAME=HEADEN 对象名 | Batch-05 |

#### 轨道 A — 重定向族命令

| 命令 | 用途 | 关键参数 | 来源批次 |
|------|------|----------|----------|
| ADD SMARTHTTPREDIR | HTTP 智能重定向对象 | - | Batch-06 |
| ADD REDIRAPPENDINFO | 重定向携带信息 | REQURLFLAG, IMSIFLAG, IMEIFLAG | Batch-06 |
| ADD DNSOVERWRITING | DNS 重写动作 | - | Batch-06 |
| ADD EXTENDEDFILTER | 扩展过滤器 | EXTFLTTYPE, EXTFLTNAME | Batch-06 |
| ADD ERRORCODE | 错误码 | 错误码范围 | Batch-06 |
| SET IPFARMGLOBAL | IP Farm 全局 | - | Batch-06 |
| ADD IPFARM / ADD IPFARMSERVER | IP Farm + 服务器 | IPFARMNAME, LBMETHOD, HEALTHSUCCLIMIT | Batch-06 |
| ADD LOGICINF | 逻辑接口（心跳检测） | - | Batch-06 |
| ADD BLACKLISTRULE | 黑名单规则（WebProxy） | - | Batch-06 |
| ADD RULE（POLICYTYPE=SMARTREDIRECT/WEBPROXY） | 重定向/WebProxy 规则 | POLICYNAME 指向 SMARTHTTPREDIR/DNSOVERWRITING/IPFARM | Batch-06 |

#### 轨道 A — ADC 命令

| 命令 | 用途 | 关键参数 | 来源批次 |
|------|------|----------|----------|
| ADD ADCPARA | ADC 参数（独有） | FLOWFILTERNAME, FLOWINFORPT, ADCHYSTTIMER | Batch-04 |
| ADD RULE（POLICYTYPE=ADC） | ADC 规则 | ADCMUTEFLAG | Batch-04 |

#### 轨道 B — URL 过滤命令（独立体系）

| 命令 | 用途 | 关键参数 | 来源批次 |
|------|------|----------|----------|
| SET APNCFFUNC | APN 粒度 URL 过滤开关 | APNNAME, CFSWITCHVALUE | Batch-07 |
| ADD CFPROFILE | 内容过滤策略 | CFPROFILENAME | Batch-07 |
| ADD CFTEMPLATE | 内容过滤模板（含 ACTION） | CFTEMPLATENAME, ICAPSRVGMNAME, **ACTION=BLOCK/PERMIT/REDIRECT** | Batch-07 |
| SET APNCFTEMPLATE | APN-模板绑定 | APNNAME, CFTEMPLATENAME | Batch-07 |
| ADD CFPROFBINDCFT | 策略-模板绑定 | CFTEMPLATENAME, CFPROFILENAME | Batch-07 |
| ADD CONTCATEGROUP | 内容分类组 | CATEGORYTYPE, CATEGORYID | Batch-07 |
| ADD CONTCATEGBIND | 策略-分类组绑定（含 ACTION） | CFPROFILENAME, CONTCATEGNAME, **ACTION=BLOCK/PERMIT/REDIRECT** | Batch-07 |
| SET CFCACHEPARA | 本地缓存参数 | CACHEIDLETIME, CACHESW | Batch-07 |
| ADD VPNINST / ADD LOGICINF | VPN 实例 / 逻辑接口 | - | Batch-07 |
| ADD ICAPSERVER | ICAP 服务器 | ICAPSERVERTYPE=URL_FILTERING | Batch-07 |
| ADD ICAPLOCALINFO | ICAP 本端信息 | User Agent | Batch-07 |
| ADD ICAPSVRGRP / ADD ICAPSVRBINDISG | ICAP 服务器组 + 绑定 | - | Batch-07 |

#### UNC 侧 PCC 命令

| 命令 | 用途 | 关键参数 | 来源批次 |
|------|------|----------|----------|
| SET PCCFUNC | SMF 全局 PCC 功能 | HOMEPCCSWITCH/ROAMPCCSWITCH/VISITPCCSWITCH | Batch-03 |
| ADD PCCTEMPLATE | PCC 模板 | N7FAILOVERSW（主备容灾） | Batch-03 |
| SET APNPCCFUNC | APN 粒度 PCC | APNNAME, HOMEPCCSWITCH（ENABLE/DISABLE/INHERIT） | Batch-03 |
| SET PCCFAILACTION | PCC 故障处理 | 回落本地 PCC 或会话失败 | Batch-03 |
| ADD RULE（RULERANGE） | UNC 规则（含范围） | RULERANGE=ALL/CENTRAL/LOCAL | Batch-03 |
| ADD USRPROFGROUP / ADD UPBINDUPG / ADD APNUSRPROFG | 用户模板组三级绑定 | - | Batch-03 |

#### UNC 侧接入控制/位置触发命令

| 命令 | 用途 | 关键参数 | 来源批次 |
|------|------|----------|----------|
| ADD USRLOCATION | 用户位置 | CGI/ECGI/NCGI | Batch-07 |
| ADD USRLOCATIONGRP | 位置组 | 批量绑定位置 | Batch-07 |
| ADD/MOD UPBINDUPG | 用户模板组绑定 | 含位置组 | Batch-07 |
| ADD APNUSRPROFG | APN-用户模板组绑定 | DNN 级 | Batch-07 |

### 8.7 关键参数术语表

| 术语 | 含义 | 出现批次 |
|------|------|----------|
| SA | Service Awareness，业务感知 | Batch-01 |
| PCC | Policy and Charging Control，策略和计费控制 | Batch-02/03 |
| ADC | Application Detection and Control，应用检测与控制 | Batch-04 |
| HEADEN | Header Enrichment，头增强 | Batch-05/08 |
| FAR | Forwarding Action Rule，转发动作规则 | Batch-02 |
| QER | QoS Enforcement Rule，QoS 执行规则 | Batch-02 |
| URR | Usage Reporting Rule，使用量上报规则 | Batch-02 |
| PDR | Packet Detection Rule，报文检测规则 | Batch-02/03 |
| PCR Trigger | Policy Control Request Trigger，策略控制请求触发器 | Batch-03 |
| ULI | User Location Information，用户位置信息 | Batch-07 |
| SAR | Service Area Restrictions，服务区限制 | Batch-02/03 |
| PRA | Presence Reporting Area，存在报告区域 | Batch-03 |
| ICAP | Internet Content Adaptation Protocol，互联网内容适配协议 | Batch-07 |
| IP Farm | 重定向目标服务器集群 | Batch-06 |
| TLV | Type-Length-Value，HTTPS 头增强字段格式 | Batch-05 |
| SNI | Server Name Indication，HTTPS 服务器名指示 | Batch-05/07 |
| captive/non-captive | Portal 强制portal/非强制模式 | Batch-06 |
| REDIRAPPENDINFO | 重定向携带信息（REQURLFLAG/IMSIFLAG/IMEIFLAG） | Batch-06 |
| CAPMODETHRES | captive 模式阈值（Portal 周期触发定时器） | Batch-06 |
| ADCMUTEFLAG | ADC 上报静默开关 | Batch-04 |
| ADCHYSTTIMER | ADC 迟滞定时器 | Batch-04 |
| ANTIFRAUD | 防欺诈开关（内嵌于 ADD HEADEN） | Batch-08 |
| GRAYLIST | 灰名单模式（只防欺诈不插头增强） | Batch-08 |
| CFTEMPLATE | 内容过滤模板（URL 过滤） | Batch-07 |
| CONTCATEGBIND | 内容分类组绑定（URL 过滤） | Batch-07 |
| DNAI | DN Access Identifier，DN 接入标识 | Batch-03 |
| RULERANGE | 规则范围（ALL/CENTRAL/LOCAL） | Batch-03 |

### 8.8 跨产品对应特性对

| UDG 特性 | UNC 特性 | 功能对应 | 访问限制角色 |
|---------|---------|----------|--------------|
| PCC(020351) | PCC(109101) | PCC 策略执行 | DISCARD/REDIRECT 载体 |
| SA-Basic(110101) | SA 框架 | 业务识别基础 | SA 引擎入口 |
| ADC(020357) | ADC(109102) | 应用检测控制 | L7 应用感知 |
| HTTP 头增强(110261) | - | HTTP 头增强 | 带内信息插入 |
| HTTPS 头增强(110263) | - | HTTPS 头增强 | 带内信息插入 |
| RTSP 头增强(110262) | - | RTSP 头增强 | 带内信息插入 |
| 头防欺诈(110401) | - | HTTP 头防欺诈 | 安全前置层 |
| HTTP 智能重定向(110284) | - | HTTP 智能重定向 | L7 REDIRECT |
| DNS 纠错(110283) | - | DNS 纠错 | DNS 层 REDIRECT |
| 用户 Portal(110281) | - | 用户 Portal | L7 Portal REDIRECT |
| WebProxy(110282) | - | WebProxy | L3 NAT REDIRECT |
| URL 过滤(110471) | - | URL 过滤基本功能 | 轨道 B BLOCK/PERMIT/REDIRECT |
| - | 位置策略(211001) | 基于初始接入位置的策略控制 | 位置触发层 |

### 8.9 E2E 访问限制方案场景汇总

| 场景 | 触发条件 | 规则类型 | 动作轨道 | 动作方式 | 关键批次 | 对应 CS |
|------|----------|----------|----------|----------|----------|---------|
| 非法网站阻塞 | IP/URL 匹配黑名单 | 预定义 | A | DISCARD | Batch-01/02 | CS-AC-01 |
| ADC 兜底阻塞 | 匹配不上所有规则 | 预定义/本地 | A | DISCARD | Batch-04 | CS-AC-01 |
| 配额耗尽重定向 | 流量/时长配额耗尽 | 动态 | A | REDIRECT（充值页） | Batch-03 | CS-AC-08 |
| 区域引导重定向 | PRA/PLMN 变化 | 动态 | A | REDIRECT（订购页） | Batch-03/07 | CS-AC-09 |
| URL 纠错 | URL 错误/不存在 | 预定义 | A | REDIRECT | Batch-06 | CS-AC-03 |
| DNS 错误引导 | DNS 查询失败 | 预定义 | A | REDIRECT | Batch-06 | CS-AC-04 |
| Portal 业务订购 | 用户 HTTP 请求（captive） | 预定义 | A | REDIRECT（Portal） | Batch-06 | CS-AC-05 |
| WebProxy 网络加速 | TCP SYN 匹配 | 预定义 | A | REDIRECT+代理 | Batch-06 | CS-AC-05 |
| URL 分类阻塞 | URL 匹配分类 | 预定义 | B | BLOCK | Batch-07 | CS-AC-06 |
| URL 分类放行 | URL 匹配白名单 | 预定义 | B | PERMIT | Batch-07 | CS-AC-06 |
| HTTP 头增强 | HTTP 请求匹配 | 预定义 | A | HEADEN | Batch-05 | CS-AC-02 |
| 头防欺诈 | HTTP 请求匹配（含已有字段） | 预定义 | A | HEADEN+检测 | Batch-08 | CS-AC-02 |
| 区域漫游限制 | TAI/号段/ODB | UNC 侧 | UNC | 拒绝接入 | Batch-07 | CS-AC-07 |
| 位置策略触发 | ULI 变化 | 动态 | A+UNC | 带宽/重定向 | Batch-07 | CS-AC-07 |

### 8.10 方案闭包（CS）与决策点（DP）对应矩阵

| CS \ DP | DP-01 动作类型 | DP-02 规则类型 | DP-03 动作轨道 | DP-04 网元范围 | DP-05 匹配层次 | DP-06 重定向目标 | DP-07 协议支持 | DP-08 PCF 容灾 |
|---------|---------------|---------------|---------------|---------------|---------------|----------------|---------------|---------------|
| CS-AC-01 PCC 阻塞 | DISCARD | 预定义/动态 | A | UPF | L3/L4 或 L7 | N/A | 任意 | 本地兜底 |
| CS-AC-02 头增强 | HEADEN | 预定义 | A | UPF | L3/L4 或 L7 | N/A | HTTP/HTTPS/RTSP | 本地兜底 |
| CS-AC-03 HTTP 重定向 | REDIRECT | 预定义 | A | UPF | L7（URL/UA/错误码） | 第三方服务器 | HTTP1.x | 本地兜底 |
| CS-AC-04 DNS 重定向 | REDIRECT | 预定义 | A | UPF | DNS | 第三方 Platform | UDP DNS | 本地兜底 |
| CS-AC-05 Portal/WebProxy | REDIRECT | 预定义 | A | UPF | L7/L3 | Portal/Proxy 服务器 | HTTP1.x/TCP | 本地兜底 |
| CS-AC-06 URL 过滤 | BLOCK/PERMIT/REDIRECT | 预定义 | B | UPF | L7（URL 分类） | 分类目标 | HTTP/HTTPS(SNI) | ICAP 故障降级 |
| CS-AC-07 接入控制 | 拒绝接入 | UNC 侧 | UNC | AMF/SMF | 位置/区域/用户类型 | N/A | N/A | 本地 PCC |
| CS-AC-08 配额重定向 | REDIRECT | 动态 | A+PCF | UPF+SMF | 会话属性 | 充值页 | HTTP | PCF 故障→本地 |
| CS-AC-09 区域重定向 | REDIRECT | 动态 | A+PCF+位置 | UPF+SMF | 位置 | 套餐订购页 | HTTP | PCF 故障→本地 |

---

## 总结

本跨主题综合分析基于 8 个知识批次（约 117 份源文档），系统性地揭示了访问限制场景的 **9 个方案闭包（CS）**、**8 个决策点（DP）**、**12 个关键发现**：

### 方案闭包（9 个）

1. **CS-AC-01 PCC 阻塞方案**（DISCARD，基于 RULE.POLICYTYPE=PCC）
2. **CS-AC-02 头增强方案**（HEADEN，HTTP/HTTPS/RTSP 头增强+防欺诈）
3. **CS-AC-03 HTTP 重定向方案**（REDIRECT，L7 HTTP 响应改写）
4. **CS-AC-04 DNS 重定向方案**（REDIRECT，DNS 解析层重写）
5. **CS-AC-05 Portal/WebProxy 重定向方案**（REDIRECT，L7 HTTP/L3 IP NAT）
6. **CS-AC-06 URL 过滤方案**（BLOCK/PERMIT/REDIRECT，独立体系）
7. **CS-AC-07 接入控制方案**（基于位置/区域/用户类型）
8. **CS-AC-08 配额耗尽重定向方案**（REDIRECT，FUP+SM 策略协同）
9. **CS-AC-09 区域引导重定向方案**（REDIRECT，基于 PRA/PLMN 触发）

### 决策点（8 个）

1. **DP-AC-01 动作类型选择**（DISCARD/HEADEN/REDIRECT/PERMIT）
2. **DP-AC-02 规则类型选择**（动态/预定义/本地）
3. **DP-AC-03 动作轨道选择**（★ 双轨核心：轨道 A PCC vs 轨道 B URL 过滤）
4. **DP-AC-04 网元范围选择**（UPF/SMF/AMF/主辅锚点）
5. **DP-AC-05 匹配层次选择**（L34/L7/DNS/应用层）
6. **DP-AC-06 重定向目标选择**（充值页/订购页/Portal/Proxy/第三方）
7. **DP-AC-07 协议支持选择**（HTTP/HTTPS/RTSP/TCP/DNS）
8. **DP-AC-08 PCF 故障容灾选择**（本地 PCC/会话失败/DNN 混合）

### 关键发现（12 个）

1. **双轨动作机制**是访问限制场景的核心架构事实（轨道 A PCC vs 轨道 B URL 过滤）
2. **PERMIT 动作的唯一性**（仅 URL 过滤显式支持）
3. **动态规则的七层限制**（URL 过滤必须用预定义规则）
4. **头防欺诈与头增强的强耦合**（最显著的依赖关系）
5. **ADC 是所有 L7 动作的共同前置**（横切依赖）
6. **重定向族四层级介入时序**的设计逻辑（DNS→WebProxy→HTTP→Portal）
7. **UPCF 动作组的官方枚举**厘清重定向在 PCF 策略层的定义
8. **规则匹配类型独立原则**允许动作叠加
9. **一条规则只能绑定一条策略**的强约束
10. **PCF 决策垄断**决定策略必须 PCF 侧完整定义
11. **UNC 侧接入控制与 UDG 侧访问限制**构成完整链路
12. **头增强族的统一配置接口**（POLICYTYPE=HEADEN）

### SemanticObject 候选（16 个）

SA-SAFlow、SA-ActionType、BA-PolicyType、BA-RuleType、BA.FilterCondition、BA.Action-PCC、BA.Action-HEADEN、BA.Action-REDIRECT、BA.Action-URLFilter、BA.RedirectTarget、BA.Location、BA.QuotaCondition、BA.PCFDecision、BA.PolicyTrack、BA.LicenseGate、BA.ConfigObject-Chain

访问限制场景的技术核心可概括为一句话：**以 SA 七步流程为通用引擎，以 PCC 三类规则体系为下发框架，通过双轨动作机制（轨道 A PCC 体系 + 轨道 B URL 过滤体系）和五个正交维度（动作类型/规则类型/动作轨道/网元范围/匹配层次）的组合，实现差异化的用户访问控制；方案闭包按动作机制归纳为 9 类（PCC 阻塞/头增强/HTTP 重定向/DNS 重定向/Portal-WebProxy/URL 过滤/接入控制/配额重定向/区域重定向），决策点按设计维度归纳为 8 个**。
