# WSFD-104005 DHCPv6地址分配 知识文档

> 聚焦 APN 业务域地址分配场景的 UNC（GGSN/SGW-C/PGW-C/SMF）控制面 DHCPv6 地址分配特性
> 本特性是 WSFD-010502（地址分配方式）中 DHCP 分配方式的具体实现（IPv6 侧）：UNC 作 DHCPv6 Client 代理用户向外置 DHCPv6 Server 申请 IPv6 地址
> 与 WSFD-104413（DHCP 功能 / DHCPv4）共同构成 UNC 外置 DHCP 域地址分配能力
> 依赖 WSFD-104001（IPv6 承载上下文）；若为 IPv4v6 双栈用户还需依赖 WSFD-104002（IPv4v6 双栈接入）

---

## 0. 元数据（三层图谱Schema字段）

| 字段 | 取值 |
|------|------|
| feature_id | WSFD-104005 |
| feature_name | DHCPv6地址分配 |
| feature_group | 地址分配 |
| parent_feature_id | WSFD-010502（地址分配方式，DHCP 分配子方式的具体实现特性，文档语义推断；同 WSFD-104413） |
| applicable_nf_map | `{"UNC": ["GGSN", "SGW-C", "PGW-C", "SMF"]}` |
| variant_dimensions | ["地址类型(IPv6)", "UNC代理角色(DHCPv6 Client代理用户申请)", "可选附带下发信息(DNS地址/P-CSCF地址)", "申请消息参数(Option Request Option: DNS Recursive Name Server Option/SIP Servers IPv6 Address List)", "代理IP网段→DHCPv6 Server地址池映射(同网段分配)", "用户类型(IPv6单栈用户/IPv4v6双栈用户)"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-01, EV-FK-02] |
| license_required | 82209423 LKV3W9V6AA11 DHCPv6地址分配 |

---

## 1. 概述

### 1.1 特性定义（是什么）

UNC 在 PDU 会话建立阶段，通过 **DHCPv6 Client 功能**从外置 DHCPv6 服务器的地址池中获取 IPv6 地址和相关配置信息，然后将获取到的用户 IPv6 地址、DNS 地址和 P-CSCF 地址等信息分配给 **IPv6 用户**或 **IPv4v6 双栈用户**，满足基于 IPv6 解决方案组网下 IPv6 用户或 IPv4v6 双栈用户的接入需求。

本特性是 **WSFD-010502 地址分配方式中 DHCP 分配方式的具体实现（IPv6 侧）**：UNC 作为 DHCPv6 Client，代理用户向 DHCPv6 Server 申请 IPv6 地址。UNC 收到用户激活请求后，携带**代理 IP** 向 DHCPv6 Server 申请 IP 地址，DHCPv6 Server 从**与该代理 IP 相同网段的地址池**中为用户分配一个 IPv6 地址。

> 来源：`output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-104005 DHCPv6地址分配/特性概述_61335231.md`（"定义"、"原理概述"章节）

### 1.2 适用NF（UDG/UNC网元）

| 涉及NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| GGSN / SGW-C / PGW-C / SMF | 控制面（UNC） | UNC 20.8.0及后续版本 | 与外置 DHCPv6 Server 交互，获取用户的 IPv6 地址、DNS 地址和 P-CSCF 地址的相关配置信息 |
| DHCP Server | 外部服务器 | 无特殊要求 | 通过 DHCPv6 信令交互为用户分配 IP 地址、DNS 地址和 P-CSCF 地址等相关信息 |

> 来源：`特性概述_61335231.md`（"可获得性/涉及NF"章节）

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|---------|---------|---------|
| 01 | 20.8.0 | 首次发布，支持 DHCPv6 地址分配 |

> 来源：`特性概述_61335231.md`（"发布历史"章节）

### 1.4 License

本特性必须获得 License 许可后才能使用，对应的 License 控制项为：

| License编号 | License名称 |
|------------|------------|
| 82209423 | LKV3W9V6AA11 DHCPv6地址分配 |

> 来源：`特性概述_61335231.md`（"可获得性/License支持"章节）

### 1.5 前置条件与依赖

| 前置条件 | 说明 |
|---------|------|
| License 加载 | 必须加载 License 控制项 82209423 LKV3W9V6AA11 DHCPv6地址分配 |
| IPv6 承载上下文特性开启（★硬依赖） | 必须开启 WSFD-104001 IPv6 承载上下文特性（License 82206568 LKV2IPV601 / 82209968 LKV2IPV6SM01）。本特性通过 DHCPv6 Client 获取 IPv6 地址，需 IPv6 承载上下文支撑 |
| IPv4v6 双栈接入特性开启（★双栈场景硬依赖） | 若为 IPv4v6 双栈用户通过 DHCP 方式分配 IPv6 地址，必须首先开启 WSFD-104002 IPv4v6 双栈接入特性（License 82206569 LKV2DUSA02 / 82209969 LKV2IPDSSM01） |
| 外置 DHCPv6 Server 就绪 | 需要部署外置 DHCPv6 Server，并配置好与 UNC 代理 IP 相同网段的 IPv6 地址池 |
| UNC 代理 IP 配置 | 必须通过 ADD AGENTIP 配置远端地址池代理 IP 信息（UNC 携带代理 IP 向 DHCPv6 Server 申请地址） |
| DHCP Server 组与服务器配置 | 必须通过 ADD DHCPSERVERGRP + ADD DHCPSERVER 配置 DHCP 服务器组和服务器实例 |
| DHCP Server 与地址池组绑定 | 必须通过 ADD DHCPBINDPOOLGRP 建立 DHCP 服务器组与 UNC 地址池组的绑定关系 |
| APN 地址分配属性 | 必须通过 SET APNADDRESSATTR 将 APN 的地址分配方式设置为 DHCP 方式 |
| 全局地址分配规则 | 通过 SET IPALLOCRULE 配置全局地址分配规则 |

> 来源：`特性概述_61335231.md`（"与其他特性的交互"、"原理概述"章节）、`WSFD-104005 DHCPv6地址分配参考信息_61255173.md`（"命令"章节）

### 1.6 与其他特性的交互

**本特性产品文档明确列出两项硬依赖**（与 WSFD-104413 "不涉及交互"的声明不同）：

| 交互类型 | 相关特性 | 控制项名称 | 交互说明 |
|---------|---------|-----------|---------|
| 依赖 | WSFD-104001 IPv6承载上下文 | 82206568 LKV2IPV601 IPv6承载上下文 / 82209968 LKV2IPV6SM01 IPv6承载上下文-USM | UNC 在 PDU 会话建立阶段通过 DHCPv6 Client 从外置 DHCPv6 Server 地址池获取 IPv6 地址和相关配置信息，因此需开启 IPv6 承载上下文特性 |
| 依赖 | WSFD-104002 IPv4v6双栈接入 | 82206569 LKV2DUSA02 IPv4v6双栈接入 / 82209969 LKV2IPDSSM01 IPv4v6双栈接入 | 如果需要为 IPv4v6 双栈接入用户通过 DHCP 方式分配 IPv6 地址，必须首先开启 IPv4v6 双栈接入特性 |

**语义推断的关联关系**（产品文档"与其他特性的交互"章节未明确列出，但功能语义存在）：

| 交互类型 | 相关特性 | 交互说明 |
|---------|---------|---------|
| 父子关系（语义推断） | WSFD-010502 地址分配方式（UNC） | 本特性是 WSFD-010502 中 DHCP 分配方式在 IPv6 侧的具体实现（与 WSFD-104413 共同构成 DHCP 子方式） |
| IPv4 对端特性 | WSFD-104413 DHCP功能（UNC） | 本特性负责 DHCPv6（RFC 3315），WSFD-104413 负责 DHCPv4（RFC 2131）；两者共同构成 UNC 外置 DHCP 域地址分配能力；共享 SET DHCPPARAREQ 命令 |
| 用户面协同 | GWFD-010105 / GWFD-010104 / GWFD-020401 / GWFD-020406（UDG） | UNC 通过 DHCPv6 获取的 IPv6 地址需下发给 UDG 用户面执行；UDG 侧 IPv6 地址池与前缀代理需与 UNC DHCPv6 池网段一致；涉及 IPv6 承载上下文（GWFD-020401）和 IPv6 PD（GWFD-020406） |

> 来源：`特性概述_61335231.md`（"与其他特性的交互"章节，文档原文）、WSFD-104413 同域特性语义对照

### 1.7 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | 通过外置 DHCPv6 服务器分配 IPv6 地址，实现用户 IPv6 地址、DNS 地址、P-CSCF 地址的动态管理。增强了接入业务中地址分配部署选择的多样性，运营商可以根据自身业务场景，灵活选择相关的业务方案，节省地址资源，降低运营成本 |
| 用户 | 用户不感知 |

> 来源：`特性概述_61335231.md`（"客户价值"章节）

### 1.8 应用场景

DHCPv6 地址分配适用于：
- 运营商管理大量 IPv6 地址池的场景
- 企业网自己管理 IPv6 地址池的场景

> 来源：`特性概述_61335231.md`（"应用场景"章节）

### 1.9 对系统的影响

**本特性对系统无影响**（文档明确声明）。

### 1.10 应用限制

- UNC 分配给用户的 P-CSCF 地址**最大支持 2 个**，包括 UNC 本地分配或外置 DHCPv6 服务器分配的 P-CSCF 地址
- **仅支持在 DHCP 过程中获取 P-CSCF 服务器地址**，不支持获取 P-CSCF 服务器域名

> 来源：`特性概述_61335231.md`（"应用限制"章节）

### 1.11 特性规格

**本特性无特殊规格**（文档明确声明）。

### 1.12 计费与话单

**本特性不涉及计费与话单**（文档明确声明）。

### 1.13 遵循标准

| 标准类别 | 标准编号 | 标准名称 |
|---------|---------|---------|
| 3GPP | 23.401 | General Packet Radio Service (GPRS) enhancements for Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access |
| 3GPP | 23.402 | Architecture enhancements for non-3GPP accesses |
| 3GPP | 29.061 | Interworking between the Public Land Mobile Network (PLMN) supporting packet based services and Packet Data Networks (PDN) |
| IETF | RFC 3315 | Dynamic Host Configuration Protocol for IPv6 (DHCPv6) |
| IETF | RFC 3646 | DNS Configuration options for Dynamic Host Configuration Protocol for IPv6 (DHCPv6) |
| IETF | RFC 3736 | Stateless Dynamic Host Configuration Protocol (DHCP) Service for IPv6 |
| IETF | RFC 3319 | Dynamic Host Configuration Protocol (DHCPv6) Options for Session Initiation Protocol (SIP) Servers |

> 来源：`特性概述_61335231.md`（"遵循标准"章节）

---

## 2. 核心概念

### 2.1 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| DHCPv6 | Dynamic Host Configuration Protocol for IPv6 | IPv6 动态主机配置协议，本特性遵循 RFC 3315 |
| DHCPv6 Client | DHCPv6 客户端 | UNC 在本特性中扮演的角色，代理用户向 DHCPv6 Server 申请 IPv6 地址 |
| DHCPv6 Server | DHCPv6 服务器 | 外置的 DHCPv6 服务器，配置 IPv6 地址池为用户分配 IPv6/DNS/P-CSCF 地址 |
| 代理 IP（Agent IP） | UNC 远端地址池代理 IP | UNC 申请 IPv6 地址时携带的代理 IP，DHCPv6 Server 据此从相同网段地址池分配 |
| DHCPv6 Solicit | DHCPv6 申请消息 | UNC 向 DHCPv6 Server 发送的地址申请消息（第一步），由 Relay-forward 承载 |
| DHCPv6 Advertise | DHCPv6 通告消息 | DHCPv6 Server 响应 Solicit 返回的地址分配候选消息 |
| DHCPv6 Request | DHCPv6 请求消息 | UNC 向 DHCPv6 Server 确认选择的消息 |
| DHCPv6 Reply | DHCPv6 应答消息 | DHCPv6 Server 最终确认分配的消息 |
| DHCPv6 Renew | DHCPv6 续租消息 | UNC 向 DHCPv6 Server 发起的地址续租消息 |
| DHCPv6 Release | DHCPv6 释放消息 | UNC 通知 DHCPv6 Server 释放地址的消息 |
| DHCPv6 Decline | DHCPv6 拒绝消息 | UNC 检测到地址冲突时发送的拒绝消息 |
| DHCPv6 Relay-forward / Relay-reply | DHCPv6 中继转发/中继应答 | DHCPv6 中继消息封装格式，UNC 通过 Relay-forward 承载 Solicit/Request，通过 Relay-reply 接收 Advertise/Reply |
| Option Request Option（ORO） | DHCPv6 选项请求选项 | DHCPv6 Solicit 消息中携带的可选参数请求列表（相当于 DHCPv4 的 Parameter Request List） |
| DNS Recursive Name Server Option | DNS 递归名字服务器选项 | DHCPv6 Option（RFC 3646），用于下发 DNS 地址 |
| SIP Servers IPv6 Address List | SIP 服务器 IPv6 地址列表 | DHCPv6 Option（RFC 3319），用于下发 P-CSCF 地址 |
| DHCP Server Group | DHCP 服务器组 | UNC 上将多台 DHCPv6 Server 组织为逻辑组，支持主备 |
| DHCPSERVERGRP | DHCP 服务器组对象 | UNC MML 配置对象（与 WSFD-104413 共享） |
| DHCPBINDPOOLGRP | DHCP 服务器组与地址池组绑定 | UNC MML 配置对象，建立 DHCP 服务器组与 UNC 地址池组映射 |
| AGENTIP | 远端地址池代理 IP | UNC MML 配置对象，携带申请地址时的代理 IP |

### 2.2 对象模型

WSFD-104005 DHCPv6 地址分配的配置架构围绕"UNC 作 DHCPv6 Client 代理 + 外置 DHCPv6 Server IPv6 地址池"展开。**MML 配置对象与 WSFD-104413（DHCPv4）完全共享**，差异仅在地址类型（IPv6）与 DHCP 协议版本（DHCPv6）：

```
┌──────────────────────────────────────────────────────────────────┐
│ UNC（GGSN/SGW-C/PGW-C/SMF）控制面 - DHCPv6 Client 代理侧          │
│                                                                  │
│   ┌──────────────┐                                               │
│   │ AGENTIP      │  UNC 远端地址池代理 IP                        │
│   │ (代理IP)     │  → 决定向 DHCPv6 Server 申请时携带的网段标识    │
│   └──────┬───────┘                                               │
│          │                                                       │
│   ┌──────┴───────┐    ┌──────────────┐    ┌──────────────────┐  │
│   │ ADDRPOOL     │ →  │ ADDRPOOLGRP  │ ←→ │ DHCPBINDPOOLGRP  │  │
│   │ (UNC地址池   │    │ (UNC地址池组) │    │ (DHCP组↔池组绑定) │  │
│   │  IPv6)       │    │              │    │                  │  │
│   └──────────────┘    └──────────────┘    └────────┬─────────┘  │
│                                                    │            │
│                                              ┌─────┴──────┐     │
│                                              │DHCPSERVERGRP│    │
│                                              │(DHCP服务器组)│   │
│                                              └─────┬──────┘     │
│                                                    │            │
│                                              ┌─────┴──────┐     │
│                                              │ DHCPSERVER │     │
│                                              │(DHCPv6服务器)│   │
│                                              └────────────┘     │
│                                                                  │
│   ┌──────────────┐    ┌──────────────────┐                       │
│   │ APN          │ →  │ APNADDRESSATTR   │  APN 地址分配属性     │
│   │ (APN配置)    │    │ (地址分配=DHCP)  │  → 将 APN 指向 DHCP   │
│   └──────────────┘    └──────────────────┘                       │
│                                                                  │
│   ┌──────────────────────────────────────────┐                   │
│   │ IPALLOCRULE（全局地址分配规则）            │                   │
│   │ DHCPPARAREQ（DHCP请求信元参数信息）        │                   │
│   │   → 控制 Solicit 携带 DNS/P-CSCF 请求      │                   │
│   └──────────────────────────────────────────┘                   │
└────────────────────────────┬─────────────────────────────────────┘
                             │ DHCPv6 信令（RFC 3315）
                             │ Relay-forward(Solicit/Request/Renew/Release/Decline)
                             │ Relay-reply(Advertise/Reply)
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│ 外置 DHCPv6 Server                                               │
│                                                                  │
│   - 按代理 IP 网段划分 IPv6 地址池                                │
│   - Advertise 中携带 DNS Recursive Name Server Option（DNS）     │
│   - Advertise 中携带 SIP Servers IPv6 Address List（P-CSCF）     │
│   - 返回 IPv6 地址                                               │
└──────────────────────────────────────────────────────────────────┘
```

### 2.3 在地址分配场景的角色

WSFD-104005 是 WSFD-010502（地址分配方式）四种分配方式中 **DHCP 分配方式在 IPv6 侧的具体实现**，与 WSFD-104413（DHCPv4）并列：

```
WSFD-010502 地址分配方式（4种决策方式）
    ├── ① UDM 静态分配      → WSFD-010400 用户数据管理支撑
    ├── ② Radius 分配        → WSFD-011306 Radius功能支撑
    ├── ③ SMF 本地池分配     → 本地 ADDRPOOL 体系（POOLTYPE=LOCAL）
    └── ④ DHCP 代理申请 ★    → 本特性 WSFD-104005（IPv6）
                              + WSFD-104413 DHCP功能（IPv4）
                              两者共同覆盖 DHCP 子方式
```

DHCPv6 分配方式的完整链路：

```
1. UE 发起 PDU 会话建立请求（PDU Session Establishment Request）
   （IPv6 单栈用户 或 IPv4v6 双栈用户）
        ↓
2. UNC（SMF/PGW-C/GGSN）决策 IPv6 地址分配方式 = DHCP
   （由 APN 的 APNADDRESSATTR 配置决定）
   前置：WSFD-104001 IPv6承载上下文已开启
        （双栈用户还需 WSFD-104002 IPv4v6双栈接入已开启）
        ↓
3. UNC 作 DHCPv6 Client，携带代理 IP（AGENTIP）通过 DHCPv6 Relay-forward
   承载 Solicit 消息发向 DHCPv6 Server
   （可选通过 SET DHCPPARAREQ 请求 DNS/P-CSCF 选项 → ORO 携带）
        ↓
4. DHCPv6 Server 从与代理 IP 相同网段的 IPv6 地址池中分配 IPv6 地址
   DHCPv6 Advertise（Relay-reply 承载）携带：
     IPv6 地址 + DNS（可选）+ P-CSCF（可选）
        ↓
5. UNC 发送 DHCPv6 Request 确认 → DHCPv6 Server 回 DHCPv6 Reply
        ↓
6. UNC 将获得的 IPv6 地址、DNS、P-CSCF 通过
   PDU Session Establishment Response 发送给 UE
        ↓
7. 会话释放时 UNC 发送 DHCPv6 Release 释放地址
   （续租时发送 DHCPv6 Renew）
```

---

## 3. 原理与流程

### 3.1 实现原理

#### 3.1.1 DHCPv6 代理申请核心机制

DHCPv6 分配地址的方式是指移动用户所分配的 IPv6 地址是在 PDU 会话建立阶段从 DHCPv6 服务器上配置的地址池中获取的动态 IP 地址。**UNC 作为 DHCP Client，代理用户向 DHCPv6 Server 申请 IP 地址**。

UNC 收到用户的激活请求，携带**代理 IP** 向 DHCPv6 Server 申请 IP 地址，DHCPv6 Server 从**与该代理 IP 相同网段的地址池**中为用户分配一个 IPv6 地址。

> 来源：`特性概述_61335231.md`（"原理概述"章节）

#### 3.1.2 可选地址申请（DNS / P-CSCF）

UNC 向 DHCPv6 Server 发送 **DHCPv6 Relay-forward Solicit 消息**时，如果需要获取用户的 DNS 地址或 P-CSCF 地址，可通过 **SET DHCPPARAREQ** 命令进行设置；设置后 DHCPv6 Solicit 消息的 **Option Request Option（ORO）**中将携带：
- **DNS Recursive Name Server Option**（DNS 地址选项，RFC 3646）
- **SIP Servers IPv6 Address List**（P-CSCF 地址选项，RFC 3319）

进行地址申请。

如果 DHCPv6 服务器支持给该用户分配 DNS 或 P-CSCF 地址，则在 **Relay-reply Advertise 消息**中携带上述 Option，返回分配的具体地址信息。

> 来源：`特性概述_61335231.md`（"原理概述"章节）

### 3.2 业务流程（DHCPv6 地址分配端到端）

```
┌──────────────────────────────────────────────────────────────────┐
│ 阶段1：UE 触发                                                    │
│   UE → AMF/MME → SMF/PGW-C/GGSN：PDU Session Establishment       │
│   请求消息指示需要为用户分配 IPv6 地址                             │
│   （IPv6 单栈用户 或 IPv4v6 双栈用户）                             │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│ 阶段2：UNC 决策与代理准备                                         │
│   UNC 查询 APN 的 APNADDRESSATTR → IPv6 地址分配方式 = DHCP       │
│   前置依赖检查：                                                  │
│     - WSFD-104001 IPv6承载上下文已开启（硬依赖）                   │
│     - 双栈用户还需 WSFD-104002 IPv4v6双栈接入已开启                │
│   UNC 确定代理 IP（AGENTIP）→ 决定 DHCPv6 Server 使用的网段        │
│   查询 DHCPBINDPOOLGRP → 定位 DHCPSERVERGRP → 选定 DHCPSERVER     │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│ 阶段3：DHCPv6 Solicit（UNC → DHCPv6 Server，Relay-forward 承载）  │
│   UNC 作为 DHCPv6 Client 发送 DHCPv6 Solicit：                    │
│     - 由 DHCPv6 Relay-forward 消息封装承载                        │
│     - 携带代理 IP（标识网段）                                      │
│     - Option Request Option（ORO）含 DNS Recursive Name Server    │
│       Option / SIP Servers IPv6 Address List                      │
│       （由 SET DHCPPARAREQ 控制是否请求）                          │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│ 阶段4：DHCPv6 Advertise（DHCPv6 Server → UNC，Relay-reply 承载）  │
│   DHCPv6 Server 从与代理 IP 相同网段的 IPv6 地址池中分配 IPv6：    │
│     - IPv6 地址                                                   │
│     - DNS Recursive Name Server Option（DNS 地址，如服务器支持）   │
│     - SIP Servers IPv6 Address List（P-CSCF 地址，如服务器支持）   │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│ 阶段5：DHCPv6 Request / Reply                                     │
│   UNC 发送 DHCPv6 Request 确认选择 → DHCPv6 Server 回 DHCPv6 Reply│
│   地址正式分配给用户                                              │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│ 阶段6：下发地址给 UE                                              │
│   UNC 将 IPv6 地址、DNS、P-CSCF 通过                              │
│   PDU Session Establishment Response 发送给 UE                    │
└──────────────────────────────────────────────────────────────────┘

（会话生命周期）
- 地址续租：UNC → DHCPv6 Server 发送 DHCPv6 Renew
- 地址冲突检测：UNC → DHCPv6 Server 发送 DHCPv6 Decline
- 会话释放：UNC → DHCPv6 Server 发送 DHCPv6 Release → DHCPv6 Server 回收地址
```

### 3.3 协议交互

| 接口/协议 | 交互网元 | 消息类型 | 说明 |
|----------|---------|---------|------|
| DHCPv6（UDP 547，RFC 3315） | UNC ↔ DHCPv6 Server | Solicit / Advertise / Request / Reply / Renew / Release / Decline / Relay-forward / Relay-reply | UNC 作 DHCPv6 Client 与外置 DHCPv6 Server 的标准 DHCPv6 信令交互；UNC 通过 Relay-forward/Relay-reply 中继封装承载 Solicit/Request/Advertise/Reply |
| N11（5G）/ S11（4G）/ Gn（2/3G） | AMF/MME/SGSN ↔ SMF/PGW-C/GGSN | PDU Session Establishment / Create Session / Create PDP Context | 控制面接收 UE 激活请求 |
| DHCPv6 Option 23（RFC 3646） | DHCPv6 Server → UNC | DNS Recursive Name Server Option | Advertise 中携带 DNS 地址 |
| DHCPv6 Option 21（RFC 3319） | DHCPv6 Server → UNC | SIP Servers IPv6 Address List | Advertise 中携带 P-CSCF 地址 |
| DHCPv6 ORO（Option Request Option） | UNC → DHCPv6 Server | Solicit 携带的请求选项列表 | 由 SET DHCPPARAREQ 控制 |

> 来源：`特性概述_61335231.md`（"原理概述"、"遵循标准"章节）、`WSFD-104005 DHCPv6地址分配参考信息_61255173.md`（"测量指标"章节印证消息类型：Solicit/Advertise/Request/Reply/Renew/Release/Decline/Relay-forward/Relay-reply 全覆盖）

---

## 4. 配置规则

### 4.1 激活步骤

WSFD-104005 DHCPv6 地址分配的激活和配置流程：

```
步骤1：加载 License
  └── 确认 License 控制项 82209423 LKV3W9V6AA11 DHCPv6地址分配 已加载

步骤2：开启前置依赖特性（★硬依赖）
  ├── 开启 WSFD-104001 IPv6承载上下文（License 82206568 / 82209968）
  └── （双栈场景）开启 WSFD-104002 IPv4v6双栈接入（License 82206569 / 82209969）

步骤3：（可选）配置 VPN 实例
  └── ADD VPNINST → 如需在 VPN 场景下与 DHCPv6 Server 交互

步骤4：配置 UNC 本地 IPv6 地址池与地址段（地址池组）
  ├── ADD ADDRPOOL     → 创建 IPv6 地址池（DHCPv6 远端池语义）
  ├── ADD SECTION      → 配置地址段
  └── ADD ADDRPOOLGRP  → 配置地址池组

步骤5：配置远端地址池代理 IP
  └── ADD AGENTIP      → UNC 向 DHCPv6 Server 申请时携带的代理 IP

步骤6：配置 DHCP 服务器组与服务器
  ├── ADD DHCPSERVERGRP → 创建 DHCP 服务器组（支持主备）
  └── ADD DHCPSERVER    → 添加 DHCPv6 服务器实例到组

步骤7：配置 DHCP 服务器组与地址池组绑定
  └── ADD DHCPBINDPOOLGRP → 建立 DHCPSERVERGRP ↔ ADDRPOOLGRP 映射

步骤8：配置 APN 与地址分配属性
  ├── ADD APN               → 创建/确认 APN 配置
  └── SET APNADDRESSATTR    → 将 APN 的 IPv6 地址分配方式设为 DHCP

步骤9：（可选）配置 DHCP 请求信元参数
  └── SET DHCPPARAREQ       → 控制 Solicit 是否请求 DNS / P-CSCF 选项

步骤10：配置全局地址分配规则
  └── SET IPALLOCRULE       → 设置全局地址分配规则
```

> 来源：`WSFD-104005 DHCPv6地址分配参考信息_61255173.md`（"命令"章节）、`特性概述_61335231.md`（"与其他特性的交互"章节的前置依赖、"原理概述"章节）

### 4.2 MML命令清单

#### 4.2.1 核心配置命令（参考信息列出的9条，与 WSFD-104413 完全相同）

| 命令 | 用途 | 关键说明 |
|------|------|---------|
| ADD VPNINST | 增加 VPN 实例 | VPN 场景下与 DHCPv6 Server 交互时使用 |
| **ADD ADDRPOOL** | 增加地址池 | UNC 侧地址池对象（DHCPv6 远端池语义，IPv6） |
| **ADD AGENTIP** | 增加远端地址池代理 IP 信息 | UNC 申请地址时携带的代理 IP，决定 DHCPv6 Server 使用的网段 |
| **ADD DHCPSERVERGRP** | 增加 DHCP 服务器组 | 组织多台 DHCPv6 Server，支持主备 |
| **ADD DHCPSERVER** | 增加 DHCP 服务器 | 添加 DHCPv6 Server 实例到组 |
| **ADD DHCPBINDPOOLGRP** | 增加 DHCP 服务器组与地址池组绑定关系 | 建立 DHCPSERVERGRP ↔ ADDRPOOLGRP 映射（关键绑定） |
| **ADD APN** | 增加 APN 配置 | APN 基础配置 |
| **SET APNADDRESSATTR** | 设置基于 APN 的地址分配属性 | 将 APN IPv6 地址分配方式设为 DHCP |
| **SET IPALLOCRULE** | 设置全局地址分配规则 | 全局地址分配规则控制 |

> 来源：`WSFD-104005 DHCPv6地址分配参考信息_61255173.md`（"命令"章节）

#### 4.2.2 辅助命令（特性概述引用）

| 命令 | 用途 | 来源 |
|------|------|------|
| SET DHCPPARAREQ | 设置向外部 DHCPv4 或 DHCPv6 服务器发送的消息中的请求信元中的参数信息 | `特性概述_61335231.md`（"原理概述"章节，超链接引用） |
| ADD SECTION | 配置本地地址池里的地址段 | 配套 ADD ADDRPOOL 使用（参考 WSFD-010502 同类命令） |
| ADD ADDRPOOLGRP | 配置地址池组 | 配套 ADD ADDRPOOL 使用 |
| ADD POOLBINDGRP | 绑定地址池到地址池组 | 配套 ADD ADDRPOOLGRP 使用 |

> 说明：SET DHCPPARAREQ 同时适用于 DHCPv4 和 DHCPv6（与 WSFD-104413 共享该命令，命令名含"DHCPv4或者DHCPv6"）。

#### 4.2.3 调测查询命令

| 命令 | 用途 |
|------|------|
| LST DHCPSERVER | 查询 DHCP 服务器配置 |
| LST DHCPSERVERGRP | 查询 DHCP 服务器组配置 |
| LST DHCPBINDPOOLGRP | 查询 DHCP 服务器组与地址池组绑定关系 |
| LST AGENTIP | 查询远端地址池代理 IP 配置 |
| LST ADDRPOOL | 查询 UNC 地址池配置 |
| DSP PDUSESSION | 显示 PDU 会话（验证用户是否通过 DHCPv6 获得地址） |

### 4.3 参数说明

#### 4.3.1 SET DHCPPARAREQ 关键参数（DHCPv6 侧）

| 参数 | 取值 | 说明 |
|------|------|------|
| 请求信元选项 | DNS Recursive Name Server Option（RFC 3646） | 控制 DHCPv6 Solicit 中 ORO 是否携带 DNS 地址请求 |
| 请求信元选项 | SIP Servers IPv6 Address List（RFC 3319） | 控制 DHCPv6 Solicit 中 ORO 是否携带 P-CSCF 地址请求 |

> 说明：SET DHCPPARAREQ 同时适用于 DHCPv4 和 DHCPv6（与 WSFD-104413 共享该命令）。对 DHCPv4 用 Domain Name Server Option / SIP Server DHCP Option；对 DHCPv6 用 DNS Recursive Name Server Option / SIP Servers IPv6 Address List。

#### 4.3.2 DHCP 软参（控制 DHCP 行为细节，与 WSFD-104413 共享）

| 软参 | 说明 |
|------|------|
| DWORD71 | 控制 UNC 尝试向判定为 down 的 DHCP 服务器发消息的时间间隔 |
| BYTE134 | 配置上报告警的 DHCP 服务器的链路断次数门限 |
| BYTE133 | 配置 UNC 扫描 DHCP 服务器状态的时间间隔 |
| BYTE39 BIT2 | 设置 UNC 发送的 DHCP 报文中 UDP 源端口号的填充值 |
| BYTE39 BIT3 | 设置 UNC 发送的 DHCP 报文中物理地址的填充值 |
| BYTE39 BIT6 | 设置 UNC 发送的 DHCP Discover/Request 报文中是否携带 Client Identifier |
| BYTE39 BIT7 | 设置 UNC 发送的 DHCP Discover/Request 报文中是否携带 Subnet Mask |
| BYTE39 BIT8 | 设置 UNC 发送的 DHCP Discover/Request 报文中是否携带 NetBIOS over TCP/IP Name Server |
| BYTE24 | 控制每次发送 DHCP 续租消息的最大个数 |
| BYTE3 | 控制远端地址池 Agent IP 下地址的最大使用率 |
| BIT218 | DHCP 用户续租时如何选择主备 DHCP 服务器 |

> 来源：`WSFD-104005 DHCPv6地址分配参考信息_61255173.md`（"软参"章节）

### 4.4 约束条件

| 约束类型 | 约束内容 |
|---------|---------|
| IPv6 承载上下文前置（★硬约束） | 必须开启 WSFD-104001 IPv6 承载上下文特性（文档"与其他特性的交互"明确列为依赖） |
| IPv4v6 双栈前置（★双栈场景硬约束） | 若为 IPv4v6 双栈用户，必须首先开启 WSFD-104002 IPv4v6 双栈接入特性（文档明确列为依赖） |
| P-CSCF 地址数量上限 | UNC 分配给用户的 P-CSCF 地址**最大支持 2 个**（包括 UNC 本地分配或外置 DHCPv6 服务器分配的） |
| P-CSCF 仅支持地址 | 仅支持在 DHCP 过程中获取 P-CSCF 服务器**地址**，**不支持**获取 P-CSCF 服务器域名 |
| 地址池网段一致性 | DHCPv6 Server 上配置的 IPv6 地址池网段必须与 UNC 代理 IP 网段一致（同网段分配机制） |
| License 必需 | 必须加载 License 控制项 82209423 LKV3W9V6AA11 |
| DHCPv6 Server 必需 | 必须部署外置 DHCPv6 Server，UNC 不能独立分配地址 |
| APN 地址分配方式 | APN 必须通过 SET APNADDRESSATTR 显式设置为 DHCP 方式才能触发本特性 |
| 仅 IPv6 | 本特性仅负责 DHCPv6 地址分配；IPv4 地址分配由 WSFD-104413 DHCP功能 负责 |

> 来源：`特性概述_61335231.md`（"与其他特性的交互"、"应用限制"、"原理概述"章节）

---

## 5. 配置案例

### 5.1 典型场景：UNC 通过外置 DHCPv6 Server 为 IPv6 用户分配 IPv6 地址

**场景描述**：运营商管理大量 IPv6 地址池，通过外置 DHCPv6 Server 统一管理 IPv6 地址分配。IPv6 用户（或 IPv4v6 双栈用户）发起 PDU 会话建立时，UNC（SMF）作为 DHCPv6 Client 代理用户向 DHCPv6 Server 申请 IPv6 地址，并请求 DNS 和 P-CSCF 地址，然后将完整地址信息下发给 UE。

**配置步骤和 MML 命令序列**（基于参考信息命令清单 + 特性概述原理构建的最小可用配置）：

```
=== 步骤1：加载 License 并开启前置依赖特性 ===

-- 确认 License 82209423 LKV3W9V6AA11 DHCPv6地址分配 已加载
-- 确认 WSFD-104001 IPv6承载上下文特性已开启（License 82206568 / 82209968）
-- （双栈用户）确认 WSFD-104002 IPv4v6双栈接入特性已开启（License 82206569 / 82209969）

=== 步骤2：（可选）配置 VPN 实例（VPN 场景） ===

ADD VPNINST: VPNNAME="dhcpv6_vpn";
  -- 创建 VPN 实例（如 DHCPv6 Server 部署在 VPN 内）

=== 步骤3：配置 UNC 本地 IPv6 地址池（DHCPv6 远端池语义） ===

ADD ADDRPOOL: POOLNAME="dhcp_pool_v6", IPVERSION=IPv6;
  -- 创建 UNC IPv6 地址池对象（代表 DHCPv6 远端池）

=== 步骤4：配置远端地址池代理 IP（关键） ===

ADD AGENTIP: POOLNAME="dhcp_pool_v6", AGENTIP="2001:db8:1::1";
  -- 配置代理 IP 为 2001:db8:1::1
  -- DHCPv6 Server 据此从 2001:db8:1::/64 网段的地址池中分配 IPv6 地址

=== 步骤5：配置 DHCP 服务器组与服务器 ===

ADD DHCPSERVERGRP: GROUPNAME="dhcpv6_group_1";
  -- 创建 DHCP 服务器组（支持主备）

ADD DHCPSERVER: GROUPNAME="dhcpv6_group_1", SERVERNAME="dhcpv6_server_pri", SERVERIP="2001:db8:1::2", VPNINSTANCE="";
  -- 添加主用 DHCPv6 Server

ADD DHCPSERVER: GROUPNAME="dhcpv6_group_1", SERVERNAME="dhcpv6_server_sec", SERVERIP="2001:db8:1::3", VPNINSTANCE="";
  -- 添加备用 DHCPv6 Server（可选，支持主备冗余）

=== 步骤6：配置 DHCP 服务器组与地址池组绑定（关键绑定） ===

ADD ADDRPOOLGRP: POOLGRPNAME="dhcpv6_poolgrp_1";
  -- 创建 IPv6 地址池组

ADD DHCPBINDPOOLGRP: POOLGRPNAME="dhcpv6_poolgrp_1", DHCPSERVERGRPNAME="dhcpv6_group_1";
  -- 建立 DHCP 服务器组与地址池组绑定关系
  -- 这是 UNC 定位 DHCPv6 Server 的关键映射

=== 步骤7：配置 APN 地址分配属性（设为 DHCP 方式） ===

ADD APN: APN="internet.example.com";
  -- 创建/确认 APN（如已存在可跳过）

SET APNADDRESSATTR: APN="internet.example.com", IPV6ALLOCTYPE=DHCP;
  -- 将 APN 的 IPv6 地址分配方式设为 DHCP
  -- 触发本特性（WSFD-104005）

=== 步骤8：（可选）配置 DHCP 请求信元参数 ===

SET DHCPPARAREQ: ..., DOMAINNAMESERVER=ENABLE, SIPSERVER=ENABLE;
  -- 控制 DHCPv6 Solicit 携带 DNS / P-CSCF 请求选项
  -- 设置后 DHCPv6 Solicit 的 Option Request Option（ORO）将携带
  --   DNS Recursive Name Server Option（DNS 地址，RFC 3646）
  --   SIP Servers IPv6 Address List（P-CSCF 地址，RFC 3319）

=== 步骤9：配置全局地址分配规则 ===

SET IPALLOCRULE: ...;
  -- 设置全局地址分配规则（与其他地址分配方式协同）
```

**场景变体**：

| 变体 | 场景说明 | 核心差异 |
|------|---------|---------|
| 仅 IPv6 地址申请 | 不需要 DNS/P-CSCF | 不配置 SET DHCPPARAREQ，Solicit 仅申请 IPv6 |
| 申请 DNS | 需要下发 DNS | SET DHCPPARAREQ 启用 DNS Recursive Name Server Option |
| 申请 P-CSCF（IMS 语音） | IMS 语音场景 | SET DHCPPARAREQ 启用 SIP Servers IPv6 Address List；注意 P-CSCF 上限 2 个，仅支持地址不支持域名 |
| 主备 DHCPv6 Server | 高可用场景 | ADD DHCPSERVERGRP 中配置多台 DHCPSERVER，由 BIT218 控制续租主备选择 |
| 企业网自管 IPv6 地址池 | 企业接入场景 | DHCPv6 Server 部署在企业网内，UNC 作代理向企业 DHCPv6 申请 |
| VPN 场景 DHCPv6 | DHCPv6 Server 在 VPN 内 | 配置 ADD VPNINST + DHCPSERVER 携带 VPNINSTANCE |
| IPv4v6 双栈用户 | 双栈接入场景 | 必须额外开启 WSFD-104002 IPv4v6双栈接入；IPv4 由 WSFD-104413 分配、IPv6 由本特性分配 |

> 说明：本特性产品文档（仅 2 个文件）未提供完整的端到端 MML 激活脚本，上述配置序列基于参考信息命令清单（9 条 MML，与 WSFD-104413 共享）和特性概述原理章节构建的最小可用配置。各命令的精确参数取值需参考对应 MML 命令的产品文档，Stage 3 横向分析时如有完整脚本应补充对照。

---

## 6. 验证与调测

### 6.1 验证方法

#### 6.1.1 查询命令

| 验证目的 | 命令 | 说明 |
|---------|------|------|
| 查询 DHCP 服务器配置 | LST DHCPSERVER | 查看 DHCPv6 Server 实例 |
| 查询 DHCP 服务器组 | LST DHCPSERVERGRP | 查看服务器组组织 |
| 查询 DHCP 绑定关系 | LST DHCPBINDPOOLGRP | 验证 DHCPSERVERGRP ↔ ADDRPOOLGRP 映射 |
| 查询代理 IP | LST AGENTIP | 查看远端地址池代理 IP 配置 |
| 查询 UNC 地址池 | LST ADDRPOOL | 查看地址池配置（IPv6） |
| 查询 PDU 会话 | DSP PDUSESSION | 验证用户是否通过 DHCPv6 成功获得 IPv6 地址 |
| 查询 APN 地址属性 | LST APNADDRESSATTR | 验证 APN IPv6 地址分配方式是否为 DHCP |

#### 6.1.2 信令跟踪

- 跟踪 UNC ↔ DHCPv6 Server 的 DHCPv6 信令（Solicit / Advertise / Request / Reply / Renew / Release / Decline / Relay-forward / Relay-reply）
- 验证 DHCPv6 Solicit（Relay-forward 承载）的 Option Request Option（ORO）是否正确携带 DNS / P-CSCF 选项
- 验证 DHCPv6 Advertise（Relay-reply 承载）中 DHCPv6 Server 是否返回了 DNS（Option 23）、P-CSCF（Option 21）地址
- 跟踪 N11（5G）/ S11（4G）/ Gn（2/3G）接口的 PDU Session Establishment Response 是否正确下发 IPv6 地址给 UE

#### 6.1.3 性能指标观测

通过性能指标观测 DHCPv6 地址分配的成功率和失败原因：

| 指标编号 | 指标名称 | 观测用途 |
|---------|---------|---------|
| 1929511781 | DHCP 地址请求次数 | 总请求量基线（与 DHCPv4 共享统计） |
| 1929511782 | DHCP 地址分配成功次数 | 成功率分子（与 DHCPv4 共享统计） |
| 1929511783 | DHCP 地址分配失败次数 | 失败率分子（与 DHCPv4 共享统计） |
| 1929511784 | 控制平面由于 DHCP 服务器无响应导致的 PDP 上下文激活失败次数 | DHCP Server 不可达导致的失败 |
| 1929511795 | 发送给 DHCP Server 的 DHCPv6 Solicit 消息包数 | 阶段1流量（DHCPv6 专用） |
| 1929511792 | 接收的 DHCP Server 始发的 DHCPv6 Advertise 消息包数 | 阶段2流量（DHCPv6 专用） |
| 1929511796 | 发送给 DHCP Server 的 DHCPv6 Request 消息包数 | 阶段3流量（DHCPv6 专用） |
| 1929511793 | 接收的 DHCP Server 始发的 DHCPv6 Reply 消息包数 | 阶段4流量（成功标志，DHCPv6 专用） |
| 1929511797 | 发送给 DHCP Server 的 DHCPv6 Renew 消息包数 | 续租流量（DHCPv6 专用） |
| 1929511798 | 发送给 DHCP Server 的 DHCPv6 Release 消息包数 | 会话释放流量（DHCPv6 专用） |
| 1929511799 | 发送给 DHCP Server 的 DHCPv6 Decline 消息包数 | 地址冲突检测（DHCPv6 专用） |
| 1929511800 | 发送给 DHCP Server 的 DHCPv6 Relay-forward 消息包数 | 中继封装流量（DHCPv6 专用） |
| 1929511794 | 接收的 DHCP Server 始发的 DHCPv6 Relay-reply 消息包数 | 中继封装流量（DHCPv6 专用） |

### 6.2 告警参考

| 告警ID | 告警名称 | 触发条件 | 影响 |
|--------|---------|---------|------|
| ALM-100446 | DHCP 服务器无响应 | UNC 向 DHCP Server 发送消息无响应（链路断次数达 BYTE134 门限） | 新用户无法通过 DHCPv6 获得 IPv6 地址，PDU 会话建立失败 |

> 来源：`WSFD-104005 DHCPv6地址分配参考信息_61255173.md`（"告警"章节）

### 6.3 测量指标（分类）

> 来源：`WSFD-104005 DHCPv6地址分配参考信息_61255173.md`（"测量指标"章节）

#### 6.3.1 DHCPv6 消息处理类（DHCPv6 专用，9条）

| 指标编号 | 指标名称 |
|---------|---------|
| 1929511795 | 发送给 DHCP Server 的 DHCPv6 Solicit 消息包数 |
| 1929511792 | 接收的 DHCP Server 始发的 DHCPv6 Advertise 消息包数 |
| 1929511796 | 发送给 DHCP Server 的 DHCPv6 Request 消息包数 |
| 1929511793 | 接收的 DHCP Server 始发的 DHCPv6 Reply 消息包数 |
| 1929511797 | 发送给 DHCP Server 的 DHCPv6 Renew 消息包数 |
| 1929511798 | 发送给 DHCP Server 的 DHCPv6 Release 消息包数 |
| 1929511799 | 发送给 DHCP Server 的 DHCPv6 Decline 消息包数 |
| 1929511800 | 发送给 DHCP Server 的 DHCPv6 Relay-forward 消息包数 |
| 1929511794 | 接收的 DHCP Server 始发的 DHCPv6 Relay-reply 消息包数 |

#### 6.3.2 DHCP 通用计数类（与 DHCPv4 共享，3条）

| 指标编号 | 指标名称 |
|---------|---------|
| 1929511781 | DHCP 地址请求次数 |
| 1929511782 | DHCP 地址分配成功次数 |
| 1929511783 | DHCP 地址分配失败次数 |

#### 6.3.3 失败流程类（接口级，5条）

| 指标编号 | 指标名称 |
|---------|---------|
| 1929511807 | Gn/Gp（GGSN）发送失败 Create PDP Context Response 消息数-DHCP服务器无响应（内部） |
| 1929490679 | S11/S4（SPGW-C）发送失败 Create Session Response 消息数-DHCP服务器无响应 |
| 1929458085 | S5/S8（PGW-C）发送失败 Create Session Response 消息数-DHCP服务器无响应 |
| 1929458880 | N11（SMF）发送 PDU Session Establishment Reject 消息数-DHCP服务器无响应 |
| 1929511784 | 控制平面由于 DHCP 服务器无响应导致的 PDP 上下文激活失败次数 |

#### 6.3.4 指定 APN 粒度类（4条）

| 指标编号 | 指标名称 |
|---------|---------|
| 1929492459 | 指定 APN 的 Gn/Gp（GGSN）发送失败 Create PDP Context Response 消息数-DHCP服务器无响应（内部） |
| 1929511778 | 指定 APN 的控制平面发送的用户释放 DHCP 地址请求数 |
| 1929511779 | 指定 APN 的控制平面发送的用户分配 DHCP 地址请求数 |
| 1929511780 | 指定 APN 的控制平面 DHCP 服务器地址分配成功次数 |

### 6.4 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| 用户无法获得 IPv6 地址（PDU 会话建立失败） | IPv6 承载上下文未开启（WSFD-104001 缺失） | ★本特性硬依赖：确认 WSFD-104001 IPv6 承载上下文特性已开启（License 82206568 / 82209968） |
| IPv4v6 双栈用户无法获得 IPv6 地址 | IPv4v6 双栈接入未开启（WSFD-104002 缺失） | ★双栈硬依赖：确认 WSFD-104002 IPv4v6 双栈接入特性已开启（License 82206569 / 82209969） |
| 用户无法获得 IPv6 地址 | DHCPv6 Server 无响应（网络不通/服务器宕机） | 检查 ALM-100446 告警；检查 UNC 到 DHCPv6 Server 的网络连通性；通过 LST DHCPSERVER 确认 SERVERIP 配置 |
| 用户无法获得 IPv6 地址 | DHCPv6 Server 地址池网段与 UNC 代理 IP 不同网段 | 核对 ADD AGENTIP 的代理 IP 网段与 DHCPv6 Server IPv6 地址池配置一致（同网段分配机制） |
| 用户无法获得 IPv6 地址 | APN IPv6 地址分配方式未设为 DHCP | LST APNADDRESSATTR 确认 IPV6ALLOCTYPE=DHCP；如未设置，SET APNADDRESSATTR 修改 |
| 用户无法获得 IPv6 地址 | DHCPBINDPOOLGRP 未正确绑定 | LST DHCPBINDPOOLGRP 确认 DHCPSERVERGRP ↔ ADDRPOOLGRP 映射存在 |
| 未获得 DNS 地址 | 未启用 DNS 请求选项 | SET DHCPPARAREQ 启用 DNS Recursive Name Server Option；确认 DHCPv6 Server 支持 RFC 3646 |
| 未获得 P-CSCF 地址（IMS 语音失败） | 未启用 P-CSCF 请求选项 | SET DHCPPARAREQ 启用 SIP Servers IPv6 Address List；确认 DHCPv6 Server 支持 RFC 3319；注意仅支持地址不支持域名 |
| P-CSCF 地址超过 2 个 | 违反 P-CSCF 数量上限约束 | P-CSCF 地址最大 2 个（含本地+DHCPv6 分配），需精简配置 |
| DHCPv6 续租失败 | 主备 DHCPv6 Server 选择异常 | 检查 BIT218 软参（DHCP 用户续租时如何选择主备 DHCP 服务器） |
| DHCPv6 地址分配后无法回收 | Release 消息未正确发送 | 观测指标 1929511798（Release 包数）；检查会话释放流程 |
| DHCPv6 Server 频繁被判定为 down | 链路断次数门限过低或扫描间隔过短 | 调整 BYTE134（告警门限）、BYTE133（扫描间隔）、DWORD71（尝试间隔）软参 |

---

## 7. 参考信息

### 7.1 接口与信元

| 接口/协议 | 涉及网元 | 关键信元/选项 | 说明 |
|----------|---------|--------------|------|
| DHCPv6（RFC 3315） | UNC ↔ DHCPv6 Server | Solicit / Advertise / Request / Reply / Renew / Release / Decline / Relay-forward / Relay-reply | 标准 DHCPv6 信令交互，UNC 通过 Relay-forward/Relay-reply 中继封装 |
| DHCPv6 ORO（Option Request Option） | UNC → DHCPv6 Server | Solicit 携带的请求选项列表 | 由 SET DHCPPARAREQ 控制 |
| DHCPv6 Option 23（RFC 3646） | DHCPv6 Server → UNC | DNS Recursive Name Server Option | Advertise 中携带 DNS 地址 |
| DHCPv6 Option 21（RFC 3319） | DHCPv6 Server → UNC | SIP Servers IPv6 Address List | Advertise 中携带 P-CSCF 地址 |
| N11（5G） | AMF ↔ SMF | PDU Session Establishment Request/Response | 5G 控制面接收 UE 激活、下发 IPv6 地址给 UE |
| S11/S4（4G） | MME ↔ SGW-C/PGW-C | Create Session Request/Response | 4G 控制面消息 |
| Gn/Gp（2/3G） | SGSN ↔ GGSN | Create PDP Context Request/Response | 2/3G 控制面消息 |

### 7.2 与其他特性的关系

| 关联特性 | 特性ID | 关系说明 |
|---------|--------|---------|
| **IPv6 承载上下文（★硬依赖，文档明确）** | WSFD-104001 | 文档"与其他特性的交互"明确列为依赖：本特性通过 DHCPv6 Client 获取 IPv6 地址，必须先开启 IPv6 承载上下文特性（License 82206568 / 82209968） |
| **IPv4v6 双栈接入（★双栈场景硬依赖，文档明确）** | WSFD-104002 | 文档"与其他特性的交互"明确列为依赖：为 IPv4v6 双栈用户分配 IPv6 地址时必须先开启 IPv4v6 双栈接入特性（License 82206569 / 82209969） |
| 地址分配方式（父特性，UNC，语义推断） | WSFD-010502 | 本特性是 WSFD-010502 中 DHCP 分配方式在 IPv6 侧的具体实现（与 WSFD-104413 共同构成 DHCP 子方式） |
| DHCP 功能（IPv4 对端） | WSFD-104413 | 本特性负责 DHCPv6（RFC 3315），WSFD-104413 负责 DHCPv4（RFC 2131）；两者共同构成 UNC 外置 DHCP 地址分配能力；**共享 SET DHCPPARAREQ 命令**、共享 9 条 MML 配置对象（ADD ADDRPOOL/AGENTIP/DHCPSERVERGRP/DHCPSERVER/DHCPBINDPOOLGRP/APN + SET APNADDRESSATTR/IPALLOCRULE）、共享 11 个软参、共享告警 ALM-100446 |
| 用户面协同（UDG 侧 IPv6） | GWFD-010105 / GWFD-010104 / GWFD-020401 / GWFD-020406 | UNC 通过 DHCPv6 获取的 IPv6 地址需下发给 UDG 用户面执行；涉及 GWFD-020401（IPv6 承载上下文，UDG 侧）、GWFD-020406（IPv6 Prefix Delegation，UDG 侧）、GWFD-010105/GWFD-010104（地址分配方式，UDG 侧） |
| 会话管理（宿主特性） | WSFD-010501 | PDU 会话建立的宿主特性，本特性在 PDU 会话建立阶段触发 |

### 7.3 告警与软参汇总

| 类别 | 项目 | 数量/说明 |
|------|------|----------|
| 告警 | ALM-100446 DHCP服务器无响应 | 1 条（与 WSFD-104413 共享） |
| 软参 | DWORD71 / BYTE134 / BYTE133 / BYTE39 BIT2 / BYTE39 BIT3 / BYTE39 BIT6 / BYTE39 BIT7 / BYTE39 BIT8 / BYTE24 / BYTE3 / BIT218 | 11 个（与 WSFD-104413 共享） |
| 测量指标 | DHCPv6 消息处理（9）+ DHCP 通用计数（3）+ 失败流程（5）+ 指定APN（4） | 共 21 条（其中 9 条 DHCPv6 消息处理为本特性独有） |

### 7.4 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-104005 DHCPv6地址分配/特性概述_61335231.md` | 适用NF（GGSN/SGW-C/PGW-C/SMF + 外置 DHCPv6 Server）、定义（UNC 作 DHCPv6 Client 代理用户申请 IPv6，服务 IPv6 单栈/IPv4v6 双栈用户）、客户价值（动态管理 IPv6/DNS/P-CSCF、节省地址资源）、应用场景（运营商大量地址池/企业网自管）、可获得性（UNC 20.8.0+，License 82209423 LKV3W9V6AA11）、**与其他特性交互（★文档明确两项硬依赖：WSFD-104001 IPv6承载上下文 + WSFD-104002 IPv4v6双栈接入）**、对系统影响（无）、应用限制（P-CSCF 最大 2 个、仅地址不支持域名）、原理概述（UNC 作 Client、代理 IP、Relay-forward Solicit、Option Request Option、DNS Recursive Name Server Option/SIP Servers IPv6 Address List、SET DHCPPARAREQ 控制、Relay-reply Advertise）、计费（无）、特性规格（无）、遵循标准（3GPP 23.401/23.402/29.061 + RFC 3315/3646/3736/3319）、发布历史（v01 20.8.0） |
| 2 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-104005 DHCPv6地址分配/WSFD-104005 DHCPv6地址分配参考信息_61255173.md` | MML命令清单（9条，与 WSFD-104413 完全一致：ADD VPNINST / ADD ADDRPOOL / ADD AGENTIP / ADD DHCPSERVERGRP / ADD DHCPSERVER / ADD DHCPBINDPOOLGRP / ADD APN / SET APNADDRESSATTR / SET IPALLOCRULE）、告警（ALM-100446，与 WSFD-104413 共享）、软参（11个，与 WSFD-104413 完全相同）、测量指标（21条：**9 条 DHCPv6 消息处理本特性独有** + 3 条 DHCP 通用计数 + 5 条失败流程 + 4 条指定APN） |

### 7.5 关键术语（补充）

| 术语 | 全称 | 说明 |
|------|------|------|
| DHCPv6 Client（UNC 角色） | UNC 作为 DHCPv6 客户端 | UNC 代理用户向 DHCPv6 Server 申请 IPv6，不是 UE 直接与 DHCPv6 Server 交互 |
| 代理 IP（Agent IP） | UNC 远端地址池代理 IP | UNC 申请时携带的网段标识，DHCPv6 Server 据此选择同网段地址池 |
| DHCPv6 Relay-forward / Relay-reply | DHCPv6 中继转发/中继应答 | UNC 使用的 DHCPv6 中继封装消息格式，承载 Solicit/Request/Renew/Release/Decline（forward 方向）和 Advertise/Reply（reply 方向） |
| Option Request Option（ORO） | DHCPv6 选项请求选项 | DHCPv6 Solicit 消息中请求 DNS/P-CSCF 等可选参数的列表，相当于 DHCPv4 的 Parameter Request List |
| DNS Recursive Name Server Option | DHCPv6 Option 23（RFC 3646） | DNS 地址下发选项（对应 DHCPv4 的 Option 6） |
| SIP Servers IPv6 Address List | DHCPv6 Option 21（RFC 3319） | P-CSCF 地址下发选项（对应 DHCPv4 的 Option 120） |

---

## 8. 文档一致性说明（配置树 vs 产品文档 vs 关联特性）

> 配置树仅用于定位特性 ID，以下记录以产品文档实际内容为准时发现的关系与差异，供 Stage 3 横向分析参考。

### 8.1 与配置树/文档清单的关系确认

| # | 维度 | 配置树/文档清单描述 | 产品文档实际内容 | 一致性 |
|---|------|---------------------|-----------------|---------|
| 1 | 特性定位 | "DHCPv6地址分配" | 产品文档明确"UNC 作为 DHCPv6 Client，代理用户向 DHCPv6 Server 申请 IPv6 地址" | 一致 |
| 2 | License | 文档清单标注"[★核心]" | 产品文档明确 License 82209423 LKV3W9V6AA11 必需 | 一致：★核心特性需 License |
| 3 | 文件数 | 2 篇 | 2 篇（特性概述 + 参考信息） | 一致 |

### 8.2 与 WSFD-010502（地址分配方式）的关系（文档依据）

| # | 维度 | WSFD-010502 描述 | WSFD-104005 实际内容 | 关系确认 |
|---|------|------------------|---------------------|---------|
| 1 | DHCP 分配方式定义 | WSFD-010502 §3.5 DHCP 代理申请方式（同 WSFD-104413 推断路径） | WSFD-104005 定义："UNC 通过 DHCPv6 Client 功能从外置 DHCPv6 服务器地址池获取 IPv6" | **一致**：WSFD-104005 是 WSFD-010502 DHCP 子方式在 IPv6 侧的具体实现 |
| 2 | 适用代际 | WSFD-010502 标注 DHCP 方式"主要 5G（SMF）" | WSFD-104005 适用NF为"GGSN/SGW-C/PGW-C/SMF"，覆盖 2/3/4/5G | **扩展**：WSFD-104005 实际支持全部代际 |
| 3 | DNS/P-CSCF | WSFD-010502 未展开 DHCP 申请的可选参数 | WSFD-104005 明确可通过 SET DHCPPARAREQ 申请 DNS/P-CSCF（DHCPv6 ORO + DNS Recursive Name Server Option / SIP Servers IPv6 Address List） | **细化**：WSFD-104005 提供 DHCPv6 申请的详细可选参数机制 |
| 4 | IPv4/v6 分工 | WSFD-010502 DHCP 方式包含 DHCPv4/DHCPv6 Server | WSFD-104005 仅 DHCPv6；DHCPv4 由 WSFD-104413 负责 | **分工**：WSFD-104005（v6）+ WSFD-104413（v4）共同覆盖 |

### 8.3 与 WSFD-104413（DHCP功能 / DHCPv4）的关系（文档依据）

| # | 维度 | WSFD-104413（DHCPv4） | WSFD-104005（DHCPv6） | 关系 |
|---|------|----------------------|----------------------|------|
| 1 | 地址类型 | IPv4 地址（公网或私网） | IPv6 地址 | 互补 |
| 2 | 遵循标准 | RFC 2131（DHCPv4）+ RFC 3361（SIP Server for IPv4） | RFC 3315（DHCPv6）+ RFC 3646（DNS）+ RFC 3319（SIP Server for IPv6）+ RFC 3736（Stateless DHCPv6） | 标准不同 |
| 3 | P-CSCF 选项 | SIP Server DHCP Option（Option 120） | SIP Servers IPv6 Address List（Option 21） | 选项编码不同 |
| 4 | DNS 选项 | Domain Name Server Option（Option 6） | DNS Recursive Name Server Option（Option 23） | 选项编码不同 |
| 5 | 申请消息 | DHCP Discover（直接发送） | DHCPv6 Solicit（**Relay-forward 中继封装**） | 封装方式不同：DHCPv6 走中继封装 |
| 6 | 共享 MML 命令 | ADD ADDRPOOL/AGENTIP/DHCPSERVERGRP/DHCPSERVER/DHCPBINDPOOLGRP/APN + SET APNADDRESSATTR/IPALLOCRULE + SET DHCPPARAREQ | 同（9 条配置命令完全一致 + SET DHCPPARAREQ） | **共享 MML 配置对象** |
| 7 | 共享软参 | 11 个软参（DWORD71/BYTE134/BYTE133/BYTE39 BIT2-8/BYTE24/BYTE3/BIT218） | 完全相同 | **完全共享** |
| 8 | 共享告警 | ALM-100446 | ALM-100446 | **共享** |
| 9 | License | 82209430 LKV3W9DHCP12 | 82209423 LKV3W9V6AA11 | **独立 License**（两者需分别加载） |
| 10 | 特性交互声明 | "不涉及与其他特性的交互" | **明确列出两项硬依赖**（WSFD-104001 + WSFD-104002） | **差异**：WSFD-104005 因 IPv6 特性，额外依赖 IPv6 承载上下文与双栈接入 |
| 11 | 测量指标 | 9 条 DHCPv4 消息处理 | **9 条 DHCPv6 消息处理（独有）** + 共享 DHCP 通用计数/失败流程/指定APN | DHCPv4/v6 各有独立的消息处理指标集，通用计数共享 |

### 8.4 与 WSFD-104001 / WSFD-104002 的依赖关系（文档依据）

| # | 依赖特性 | License 控制项 | 文档原文依据 |
|---|---------|---------------|-------------|
| 1 | WSFD-104001 IPv6承载上下文 | 82206568 LKV2IPV601 / 82209968 LKV2IPV6SM01 | "UNC 在 PDU 会话建立阶段，通过 DHCPv6 Client 功能从外置的 DHCPv6 服务器的地址池中获取 IPv6 地址和相关配置信息，因此需开启 IPv6 承载上下文特性" |
| 2 | WSFD-104002 IPv4v6双栈接入 | 82206569 LKV2DUSA02 / 82209969 LKV2IPDSSM01 | "如果需要为 IPv4v6 双栈接入用户通过 DHCP 方式分配 IPv6 地址，必须首先开启 IPv4v6 双栈接入特性" |

> 关键差异：WSFD-104413（DHCPv4）声明"不涉及与其他特性的交互"；WSFD-104005（DHCPv6）**明确列出两项硬依赖**——这是 DHCPv6 与 DHCPv4 在产品文档层面最显著的差异，源于 IPv6 协议栈本身的特性依赖链。

### 8.5 文档覆盖度与缺口

| # | 维度 | 现状 | Stage 3 待补充 |
|---|------|------|---------------|
| 1 | 完整 MML 激活脚本 | 产品文档仅 2 篇，无完整端到端激活脚本 | 如有 ADD DHCPSERVER / SET APNADDRESSATTR / SET DHCPPARAREQ / SET IPALLOCRULE 等命令的详细参数文档，应横向引用补充 |
| 2 | 与 WSFD-104413 共享命令详情 | SET DHCPPARAREQ 命令在特性概述中以超链接引用，未展开参数 | Stage 3 引用 OM 参考的 SET DHCPPARAREQ 命令文档补充参数（DHCPv4 与 DHCPv6 选项的差异） |
| 3 | IPv4v6 双栈场景 | 本特性仅 DHCPv6，双栈需与 WSFD-104413 组合 | Stage 3 横向分析双栈场景下的 DHCPv4 + DHCPv6 协同配置（需结合 WSFD-104002 双栈接入） |
| 4 | C-U 协同细节 | 本特性未明确与 UDG 侧的 C-U 协同约束 | Stage 3 横向 GWFD-010104/GWFD-010105/GWFD-020401/GWFD-020406 确认 DHCPv6 池网段一致性与 IPv6 前缀代理（PD）的协同 |
| 5 | IPv6 前缀下发 | 本特性文档未明确 DHCPv6-PD（前缀代理）场景 | Stage 3 横向 GWFD-020406（IPv6 Prefix Delegation，UDG）/ WSFD-104004（IPv6 前缀代理，SMF）确认前缀下发是否经由 DHCPv6 通道 |
