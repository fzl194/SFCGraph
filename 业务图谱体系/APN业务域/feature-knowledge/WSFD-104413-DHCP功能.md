# WSFD-104413 DHCP功能 知识文档

> 聚焦 APN 业务域地址分配场景的 UNC（GGSN/SGW-C/PGW-C/SMF）控制面 DHCPv4 地址分配特性
> 本特性是 WSFD-010502（地址分配方式）中 DHCP 分配方式的具体实现：UNC 作 DHCP Client 代理用户向外置 DHCP Server 申请 IPv4 地址
> 与 WSFD-104005（DHCPv6 地址分配）共同构成 UNC 外置 DHCP 域地址分配能力

---

## 0. 元数据（三层图谱Schema字段）

| 字段 | 取值 |
|------|------|
| feature_id | WSFD-104413 |
| feature_name | DHCP功能 |
| feature_group | 地址分配 |
| parent_feature_id | WSFD-010502（地址分配方式，DHCP 分配子方式的具体实现特性，文档语义推断） |
| applicable_nf_map | `{"UNC": ["GGSN", "SGW-C", "PGW-C", "SMF"]}` |
| variant_dimensions | ["地址类型(IPv4)", "UNC代理角色(DHCP Client代理用户申请)", "可选附带下发信息(DNS地址/P-CSCF地址)", "申请消息参数(Parameter Request List: Domain Name Server Option/SIP Server DHCP Option)", "代理IP网段→DHCP Server地址池映射(同网段分配)", "地址归属(公网或私网IPv4)"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-01, EV-FK-02] |
| license_required | 82209430 LKV3W9DHCP12 DHCP功能 |

---

## 1. 概述

### 1.1 特性定义（是什么）

UNC 在 PDU 会话建立阶段，通过 **DHCP Client 功能**从外置的 DHCP 服务器的地址池中获取 IPv4 地址和相关配置信息，然后将获取到的用户 IPv4 地址、DNS 地址和 P-CSCF 地址等信息分配给用户，以满足 IPv4 用户的接入需求。

本特性是 **WSFD-010502 地址分配方式中 DHCP 分配方式的具体实现特性**：UNC 作为 DHCP Client，代理用户向 DHCP Server 申请 IPv4 地址。UNC 收到用户激活请求后，携带代理 IP 向 DHCP Server 申请 IP 地址，DHCP Server 从与该代理 IP 相同网段的地址池中为用户分配一个 IPv4 地址（可以是公网或私网地址）。

> 来源：`output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-104413 DHCP功能/特性概述_60866061.md`（"定义"、"原理概述"章节）

### 1.2 适用NF（UDG/UNC网元）

| 涉及NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| GGSN / SGW-C / PGW-C / SMF | 控制面（UNC） | UNC 20.8.0及后续版本 | 与外置 DHCP Server 交互，获取用户的 IPv4 地址、DNS 地址和 P-CSCF 地址的相关配置信息 |
| DHCP Server | 外部服务器 | 无特殊要求 | 通过 DHCPv4 信令交互为用户分配 IP 地址、DNS 地址和 P-CSCF 地址等相关信息 |

> 来源：`特性概述_60866061.md`（"可获得性/涉及NF"章节）

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|---------|---------|---------|
| 01 | 20.8.0 | 首次发布，支持 DHCP 地址分配 |

> 来源：`特性概述_60866061.md`（"发布历史"章节）

### 1.4 License

本特性必须获得 License 许可后才能使用，对应的 License 控制项为：

| License编号 | License名称 |
|------------|------------|
| 82209430 | LKV3W9DHCP12 DHCP功能 |

> 来源：`特性概述_60866061.md`（"可获得性/License支持"章节）

### 1.5 前置条件与依赖

| 前置条件 | 说明 |
|---------|------|
| License 加载 | 必须加载 License 控制项 82209430 LKV3W9DHCP12 DHCP功能 |
| 外置 DHCP Server 就绪 | 需要部署外置 DHCP Server，并配置好与 UNC 代理 IP 相同网段的地址池 |
| UNC 代理 IP 配置 | 必须通过 ADD AGENTIP 配置远端地址池代理 IP 信息（UNC 携带代理 IP 向 DHCP Server 申请地址） |
| DHCP Server 组与服务器配置 | 必须通过 ADD DHCPSERVERGRP + ADD DHCPSERVER 配置 DHCP 服务器组和服务器实例 |
| DHCP Server 与地址池组绑定 | 必须通过 ADD DHCPBINDPOOLGRP 建立 DHCP 服务器组与 UNC 地址池组的绑定关系 |
| APN 地址分配属性 | 必须通过 SET APNADDRESSATTR 将 APN 的地址分配方式设置为 DHCP 方式 |
| 全局地址分配规则 | 通过 SET IPALLOCRULE 配置全局地址分配规则 |

> 来源：`WSFD-104413 DHCP功能参考信息_61065989.md`（"命令"章节）、`特性概述_60866061.md`（"原理概述"章节）

### 1.6 与其他特性的交互

**本特性产品文档明确声明"不涉及与其他特性的交互"**（产品文档原文），但根据功能语义与同域特性存在以下关系：

| 交互类型 | 相关特性 | 交互说明 |
|---------|---------|---------|
| 父子关系（语义推断） | WSFD-010502 地址分配方式（UNC） | 本特性是 WSFD-010502 中 DHCP 分配方式的具体实现特性（WSFD-010502 §3.5 明确描述 DHCP 代理申请方式原理，指向本特性） |
| IPv6 对端特性 | WSFD-104005 DHCPv6地址分配（UNC） | 本特性负责 DHCPv4（RFC 2131），WSFD-104005 负责 DHCPv6（IPv6 侧 DHCP 申请）；两者共同构成 UNC 外置 DHCP 地址分配能力 |
| 用户面协同 | GWFD-010105 / GWFD-010104（UDG） | UNC 通过 DHCP 获取的 IPv4 地址需下发给 UDG 用户面执行；UDG 地址池需与 UNC DHCP 池网段一致 |

> 来源：`特性概述_60866061.md`（"与其他特性的交互"章节）、WSFD-010502 地址分配方式特性概述（§3.5 DHCP 代理申请方式引用）

### 1.7 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | 通过外置 DHCP 服务器分配 IPv4 地址，实现用户 IPv4 地址、DNS 地址、P-CSCF 地址的动态管理。增强了接入业务中地址分配部署选择的多样性，运营商可以根据自身业务场景，灵活选择相关的业务方案，节省地址资源，降低运营成本 |
| 用户 | 用户不感知 |

> 来源：`特性概述_60866061.md`（"客户价值"章节）

### 1.8 应用场景

DHCP 地址分配适用于：
- 运营商管理大量地址池的场景
- 企业网自己管理地址池的场景

> 来源：`特性概述_60866061.md`（"应用场景"章节）

### 1.9 对系统的影响

**本特性对系统无影响**（文档明确声明）。

### 1.10 应用限制

- UNC 分配给用户的 P-CSCF 地址**最大支持 2 个**，包括 UNC 本地分配或外置 DHCP 服务器分配的 P-CSCF 地址
- **仅支持在 DHCP 过程中获取 P-CSCF 服务器地址**，不支持获取 P-CSCF 服务器域名

> 来源：`特性概述_60866061.md`（"应用限制"章节）

### 1.11 特性规格

**本特性无特殊规格**（文档明确声明）。

### 1.12 计费与话单

**本特性不涉及计费与话单**（文档明确声明）。

### 1.13 遵循标准

| 标准类别 | 标准编号 | 标准名称 |
|---------|---------|---------|
| 3GPP | 23.060 | General Packet Radio Service (GPRS) Service Description; Stage 2 |
| 3GPP | 29.060 | GPRS; GTP across the Gn and Gp interface |
| IETF | RFC 2131 | Dynamic Host Configuration Protocol |
| IETF | RFC 3361 | DHCP-for-IPv4 Option for Session Initiation Protocol (SIP) Servers |

> 来源：`特性概述_60866061.md`（"遵循标准"章节）

---

## 2. 核心概念

### 2.1 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| DHCP | Dynamic Host Configuration Protocol | 动态主机配置协议，本特性遵循 RFC 2131（DHCPv4） |
| DHCP Client | DHCP 客户端 | UNC 在本特性中扮演的角色，代理用户向 DHCP Server 申请 IP 地址 |
| DHCP Server | DHCP 服务器 | 外置的 DHCPv4 服务器，配置地址池为用户分配 IPv4/DNS/P-CSCF 地址 |
| 代理 IP（Agent IP） | UNC 远端地址池代理 IP | UNC 申请 IP 地址时携带的代理 IP，DHCP Server 据此从相同网段地址池分配 |
| DHCP Discover | DHCP 发现消息 | UNC 向 DHCP Server 发送的地址申请消息（第一步） |
| DHCP Offer | DHCP 提供消息 | DHCP Server 响应 Discover 返回的地址分配候选消息 |
| DHCP Request | DHCP 请求消息 | UNC 向 DHCP Server 确认选择的消息 |
| DHCP Ack / Nak | DHCP 确认/拒绝消息 | DHCP Server 最终确认或拒绝分配的消息 |
| Parameter Request List | DHCP 参数请求列表 | DHCP Discover 消息中携带的可选参数请求（如 DNS、P-CSCF 选项） |
| Domain Name Server Option | DNS 地址选项 | DHCP Option，用于下发 DNS 地址 |
| SIP Server DHCP Option | SIP Server DHCP 选项 | DHCP Option（RFC 3361），用于下发 P-CSCF 地址 |
| DHCP Server Group | DHCP 服务器组 | UNC 上将多台 DHCP Server 组织为逻辑组，支持主备 |
| DHCPSERVERGRP | DHCP 服务器组对象 | UNC MML 配置对象 |
| DHCPBINDPOOLGRP | DHCP 服务器组与地址池组绑定 | UNC MML 配置对象，建立 DHCP 服务器组与 UNC 地址池组映射 |
| AGENTIP | 远端地址池代理 IP | UNC MML 配置对象，携带申请地址时的代理 IP |

### 2.2 对象模型

WSFD-104413 DHCP功能的配置架构围绕"UNC 作 DHCP Client 代理 + 外置 DHCP Server 地址池"展开，核心对象关系如下：

```
┌──────────────────────────────────────────────────────────────────┐
│ UNC（GGSN/SGW-C/PGW-C/SMF）控制面 - DHCP Client 代理侧            │
│                                                                  │
│   ┌──────────────┐                                               │
│   │ AGENTIP      │  UNC 远端地址池代理 IP                        │
│   │ (代理IP)     │  → 决定向 DHCP Server 申请时携带的网段标识      │
│   └──────┬───────┘                                               │
│          │                                                       │
│   ┌──────┴───────┐    ┌──────────────┐    ┌──────────────────┐  │
│   │ ADDRPOOL     │ →  │ ADDRPOOLGRP  │ ←→ │ DHCPBINDPOOLGRP  │  │
│   │ (UNC地址池)  │    │ (UNC地址池组) │    │ (DHCP组↔池组绑定) │  │
│   └──────────────┘    └──────────────┘    └────────┬─────────┘  │
│                                                    │            │
│                                              ┌─────┴──────┐     │
│                                              │DHCPSERVERGRP│    │
│                                              │(DHCP服务器组)│   │
│                                              └─────┬──────┘     │
│                                                    │            │
│                                              ┌─────┴──────┐     │
│                                              │ DHCPSERVER │     │
│                                              │ (DHCP服务器)│     │
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
│   │   → 控制 Discover 携带 DNS/P-CSCF 请求     │                   │
│   └──────────────────────────────────────────┘                   │
└────────────────────────────┬─────────────────────────────────────┘
                             │ DHCPv4 信令（RFC 2131）
                             │ Discover / Request / Release
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│ 外置 DHCP Server                                                 │
│                                                                  │
│   - 按代理 IP 网段划分地址池                                      │
│   - DHCP Offer 中携带 Domain Name Server Option（DNS）            │
│   - DHCP Offer 中携带 SIP Server DHCP Option（P-CSCF）            │
│   - 返回公网或私网 IPv4 地址                                      │
└──────────────────────────────────────────────────────────────────┘
```

### 2.3 在地址分配场景的角色

WSFD-104413 是 WSFD-010502（地址分配方式）四种分配方式中 **DHCP 分配方式的具体实现**：

```
WSFD-010502 地址分配方式（4种决策方式）
    ├── ① UDM 静态分配      → WSFD-010400 用户数据管理支撑
    ├── ② Radius 分配        → WSFD-011306 Radius功能支撑
    ├── ③ SMF 本地池分配     → 本地 ADDRPOOL 体系（POOLTYPE=LOCAL）
    └── ④ DHCP 代理申请 ★    → 本特性 WSFD-104413（IPv4）
                              + WSFD-104005 DHCPv6地址分配（IPv6）
```

DHCP 分配方式的完整链路：

```
1. UE 发起 PDU 会话建立请求（PDU Session Establishment Request）
        ↓
2. UNC（SMF/PGW-C/GGSN）决策地址分配方式 = DHCP
   （由 APN 的 APNADDRESSATTR 配置决定）
        ↓
3. UNC 作 DHCP Client，携带代理 IP（AGENTIP）向 DHCP Server 发送
   DHCP Discover（可选通过 SET DHCPPARAREQ 请求 DNS/P-CSCF 选项）
        ↓
4. DHCP Server 从与代理 IP 相同网段的地址池中分配 IPv4 地址
   DHCP Offer 携带：IPv4 地址 + DNS（可选）+ P-CSCF（可选）
        ↓
5. UNC 发送 DHCP Request 确认 → DHCP Server 回 DHCP Ack
        ↓
6. UNC 将获得的 IPv4 地址、DNS、P-CSCF 通过
   PDU Session Establishment Response 发送给 UE
        ↓
7. 会话释放时 UNC 发送 DHCP Release 释放地址
```

---

## 3. 原理与流程

### 3.1 实现原理

#### 3.1.1 DHCP 代理申请核心机制

DHCP 分配地址的方式是指移动用户所分配的 IP 地址是在 PDU 会话建立阶段从 DHCP 服务器上配置的地址池中获取的动态 IP 地址。**UNC 作为 DHCP Client，代理用户向 DHCP Server 申请 IP 地址**。

UNC 收到用户的激活请求，携带**代理 IP** 向 DHCP Server 申请 IP 地址，DHCP Server 从**与该代理 IP 相同网段的地址池**中为用户分配一个 IP 地址，这个地址可以是公网或私网 IPv4 地址。

> 来源：`特性概述_60866061.md`（"原理概述"章节）

#### 3.1.2 可选地址申请（DNS / P-CSCF）

UNC 向 DHCP Server 发送 DHCP Discover 消息时，如果需要获取用户的 DNS 地址或 P-CSCF 地址，可通过 **SET DHCPPARAREQ** 命令进行设置；设置后 DHCP Discover 消息的 **Parameter Request List** 中将携带：
- **Domain Name Server Option**（DNS 地址选项）
- **SIP Server DHCP Option**（P-CSCF 地址选项，遵循 RFC 3361）

进行地址申请。

如果 DHCP 服务器支持给该用户分配 DNS 或 P-CSCF 地址，则在 DHCP Offer 消息中携带上述 Option，返回分配的具体地址信息。

> 来源：`特性概述_60866061.md`（"原理概述"章节）

### 3.2 业务流程（DHCPv4 地址分配端到端）

```
┌──────────────────────────────────────────────────────────────────┐
│ 阶段1：UE 触发                                                    │
│   UE → AMF/MME → SMF/PGW-C/GGSN：PDU Session Establishment       │
│   请求消息指示需要为用户分配 IPv4 地址                             │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│ 阶段2：UNC 决策与代理准备                                         │
│   UNC 查询 APN 的 APNADDRESSATTR → 地址分配方式 = DHCP            │
│   UNC 确定代理 IP（AGENTIP）→ 决定 DHCP Server 使用的网段          │
│   查询 DHCPBINDPOOLGRP → 定位 DHCPSERVERGRP → 选定 DHCPSERVER     │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│ 阶段3：DHCP Discover（UNC → DHCP Server）                         │
│   UNC 作为 DHCP Client 发送 DHCP Discover：                       │
│     - 携带代理 IP（标识网段）                                      │
│     - Parameter Request List 含 DNS Option / SIP Server Option    │
│       （由 SET DHCPPARAREQ 控制是否请求）                          │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│ 阶段4：DHCP Offer（DHCP Server → UNC）                            │
│   DHCP Server 从与代理 IP 相同网段的地址池中分配 IPv4：            │
│     - 公网或私网 IPv4 地址                                         │
│     - Domain Name Server Option（DNS 地址，如服务器支持）          │
│     - SIP Server DHCP Option（P-CSCF 地址，如服务器支持）          │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│ 阶段5：DHCP Request / Ack                                         │
│   UNC 发送 DHCP Request 确认选择 → DHCP Server 回 DHCP Ack        │
│   地址正式分配给用户                                              │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│ 阶段6：下发地址给 UE                                              │
│   UNC 将 IPv4 地址、DNS、P-CSCF 通过                              │
│   PDU Session Establishment Response 发送给 UE                    │
└──────────────────────────────────────────────────────────────────┘

（会话释放阶段）
UE 释放 → UNC 发送 DHCP Release → DHCP Server 回收地址
```

### 3.3 协议交互

| 接口/协议 | 交互网元 | 消息类型 | 说明 |
|----------|---------|---------|------|
| DHCPv4（UDP 67/68，RFC 2131） | UNC ↔ DHCP Server | Discover / Offer / Request / Ack / Nak / Decline / Release | UNC 作 DHCP Client 与外置 DHCP Server 的标准 DHCPv4 信令交互 |
| N11（5G）/ S11（4G）/ Gn（2/3G） | AMF/MME/SGSN ↔ SMF/PGW-C/GGSN | PDU Session Establishment / Create Session / Create PDP Context | 控制面接收 UE 激活请求 |
| DHCP Option 6 | DHCP Server → UNC | Domain Name Server Option | DHCP Offer 中携带 DNS 地址 |
| DHCP Option 120（RFC 3361） | DHCP Server → UNC | SIP Server DHCP Option | DHCP Offer 中携带 P-CSCF 地址 |

> 来源：`特性概述_60866061.md`（"原理概述"、"遵循标准"章节）、`WSFD-104413 DHCP功能参考信息_61065989.md`（"测量指标"章节印证消息类型）

---

## 4. 配置规则

### 4.1 激活步骤

WSFD-104413 DHCP 功能的激活和配置流程：

```
步骤1：加载 License
  └── 确认 License 控制项 82209430 LKV3W9DHCP12 DHCP功能 已加载

步骤2：（可选）配置 VPN 实例
  └── ADD VPNINST → 如需在 VPN 场景下与 DHCP Server 交互

步骤3：配置 UNC 本地地址池与地址段（地址池组）
  ├── ADD ADDRPOOL     → 创建地址池（DHCP 远端池语义）
  ├── ADD SECTION      → 配置地址段
  └── ADD ADDRPOOLGRP  → 配置地址池组

步骤4：配置远端地址池代理 IP
  └── ADD AGENTIP      → UNC 向 DHCP Server 申请时携带的代理 IP

步骤5：配置 DHCP 服务器组与服务器
  ├── ADD DHCPSERVERGRP → 创建 DHCP 服务器组（支持主备）
  └── ADD DHCPSERVER    → 添加 DHCP 服务器实例到组

步骤6：配置 DHCP 服务器组与地址池组绑定
  └── ADD DHCPBINDPOOLGRP → 建立 DHCPSERVERGRP ↔ ADDRPOOLGRP 映射

步骤7：配置 APN 与地址分配属性
  ├── ADD APN               → 创建/确认 APN 配置
  └── SET APNADDRESSATTR    → 将 APN 的地址分配方式设为 DHCP

步骤8：（可选）配置 DHCP 请求信元参数
  └── SET DHCPPARAREQ       → 控制 Discover 是否请求 DNS / P-CSCF 选项

步骤9：配置全局地址分配规则
  └── SET IPALLOCRULE       → 设置全局地址分配规则
```

> 来源：`WSFD-104413 DHCP功能参考信息_61065989.md`（"命令"章节）

### 4.2 MML命令清单

#### 4.2.1 核心配置命令（参考信息列出的9条）

| 命令 | 用途 | 关键说明 |
|------|------|---------|
| ADD VPNINST | 增加 VPN 实例 | VPN 场景下与 DHCP Server 交互时使用 |
| **ADD ADDRPOOL** | 增加地址池 | UNC 侧地址池对象（DHCP 远端池语义） |
| **ADD AGENTIP** | 增加远端地址池代理 IP 信息 | UNC 申请地址时携带的代理 IP，决定 DHCP Server 使用的网段 |
| **ADD DHCPSERVERGRP** | 增加 DHCP 服务器组 | 组织多台 DHCP Server，支持主备 |
| **ADD DHCPSERVER** | 增加 DHCP 服务器 | 添加 DHCP Server 实例到组 |
| **ADD DHCPBINDPOOLGRP** | 增加 DHCP 服务器组与地址池组绑定关系 | 建立 DHCPSERVERGRP ↔ ADDRPOOLGRP 映射（关键绑定） |
| **ADD APN** | 增加 APN 配置 | APN 基础配置 |
| **SET APNADDRESSATTR** | 设置基于 APN 的地址分配属性 | 将 APN 地址分配方式设为 DHCP |
| **SET IPALLOCRULE** | 设置全局地址分配规则 | 全局地址分配规则控制 |

> 来源：`WSFD-104413 DHCP功能参考信息_61065989.md`（"命令"章节）

#### 4.2.2 辅助命令（特性概述引用）

| 命令 | 用途 | 来源 |
|------|------|------|
| SET DHCPPARAREQ | 设置向外部 DHCPv4 或 DHCPv6 服务器发送的消息中的请求信元中的参数信息 | `特性概述_60866061.md`（"原理概述"章节，超链接引用） |
| ADD SECTION | 配置本地地址池里的地址段 | 配套 ADD ADDRPOOL 使用（参考 WSFD-010502 同类命令） |
| ADD ADDRPOOLGRP | 配置地址池组 | 配套 ADD ADDRPOOL 使用 |
| ADD POOLBINDGRP | 绑定地址池到地址池组 | 配套 ADD ADDRPOOLGRP 使用 |

#### 4.2.3 调测查询命令

| 命令 | 用途 |
|------|------|
| LST DHCPSERVER | 查询 DHCP 服务器配置 |
| LST DHCPSERVERGRP | 查询 DHCP 服务器组配置 |
| LST DHCPBINDPOOLGRP | 查询 DHCP 服务器组与地址池组绑定关系 |
| LST AGENTIP | 查询远端地址池代理 IP 配置 |
| LST ADDRPOOL | 查询 UNC 地址池配置 |
| DSP PDUSESSION | 显示 PDU 会话（验证用户是否通过 DHCP 获得地址） |

### 4.3 参数说明

#### 4.3.1 SET DHCPPARAREQ 关键参数

| 参数 | 取值 | 说明 |
|------|------|------|
| 请求信元选项 | Domain Name Server Option | 控制 DHCP Discover 中 Parameter Request List 是否携带 DNS 地址请求 |
| 请求信元选项 | SIP Server DHCP Option（RFC 3361） | 控制 DHCP Discover 中 Parameter Request List 是否携带 P-CSCF 地址请求 |

> 说明：SET DHCPPARAREQ 同时适用于 DHCPv4 和 DHCPv6（与 WSFD-104005 共享该命令）。

#### 4.3.2 DHCP 软参（控制 DHCP 行为细节）

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

> 来源：`WSFD-104413 DHCP功能参考信息_61065989.md`（"软参"章节）

### 4.4 约束条件

| 约束类型 | 约束内容 |
|---------|---------|
| P-CSCF 地址数量上限 | UNC 分配给用户的 P-CSCF 地址**最大支持 2 个**（包括 UNC 本地分配或外置 DHCP 服务器分配的） |
| P-CSCF 仅支持地址 | 仅支持在 DHCP 过程中获取 P-CSCF 服务器**地址**，**不支持**获取 P-CSCF 服务器域名 |
| 地址池网段一致性 | DHCP Server 上配置的地址池网段必须与 UNC 代理 IP 网段一致（同网段分配机制） |
| License 必需 | 必须加载 License 控制项 82209430 LKV3W9DHCP12 |
| DHCP Server 必需 | 必须部署外置 DHCP Server，UNC 不能独立分配地址 |
| APN 地址分配方式 | APN 必须通过 SET APNADDRESSATTR 显式设置为 DHCP 方式才能触发本特性 |
| 仅 IPv4 | 本特性仅负责 DHCPv4 地址分配；IPv6 地址分配由 WSFD-104005 DHCPv6地址分配 负责 |

> 来源：`特性概述_60866061.md`（"应用限制"、"原理概述"章节）

---

## 5. 配置案例

### 5.1 典型场景：UNC 通过外置 DHCP Server 为用户分配 IPv4 地址

**场景描述**：运营商管理大量 IPv4 地址池，通过外置 DHCP Server 统一管理地址分配。UE 发起 PDU 会话建立时，UNC（SMF）作为 DHCP Client 代理用户向 DHCP Server 申请 IPv4 地址，并请求 DNS 和 P-CSCF 地址，然后将完整地址信息下发给 UE。

**配置步骤和 MML 命令序列**（基于参考信息命令清单 + 特性概述原理构建的最小可用配置）：

```
=== 步骤1：（可选）配置 VPN 实例（VPN 场景） ===

ADD VPNINST: VPNNAME="dhcp_vpn";
  -- 创建 VPN 实例（如 DHCP Server 部署在 VPN 内）

=== 步骤2：配置 UNC 本地地址池（DHCP 远端池语义） ===

ADD ADDRPOOL: POOLNAME="dhcp_pool_v4", IPVERSION=IPv4;
  -- 创建 UNC 地址池对象（代表 DHCP 远端池）

=== 步骤3：配置远端地址池代理 IP（关键） ===

ADD AGENTIP: POOLNAME="dhcp_pool_v4", AGENTIP="10.10.0.1";
  -- 配置代理 IP 为 10.10.0.1
  -- DHCP Server 据此从 10.10.0.0 网段的地址池中分配地址

=== 步骤4：配置 DHCP 服务器组与服务器 ===

ADD DHCPSERVERGRP: GROUPNAME="dhcp_group_1";
  -- 创建 DHCP 服务器组（支持主备）

ADD DHCPSERVER: GROUPNAME="dhcp_group_1", SERVERNAME="dhcp_server_pri", SERVERIP="10.10.0.2", VPNINSTANCE="";
  -- 添加主用 DHCP Server

ADD DHCPSERVER: GROUPNAME="dhcp_group_1", SERVERNAME="dhcp_server_sec", SERVERIP="10.10.0.3", VPNINSTANCE="";
  -- 添加备用 DHCP Server（可选，支持主备冗余）

=== 步骤5：配置 DHCP 服务器组与地址池组绑定（关键绑定） ===

ADD ADDRPOOLGRP: POOLGRPNAME="dhcp_poolgrp_1";
  -- 创建地址池组

ADD DHCPBINDPOOLGRP: POOLGRPNAME="dhcp_poolgrp_1", DHCPSERVERGRPNAME="dhcp_group_1";
  -- 建立 DHCP 服务器组与地址池组绑定关系
  -- 这是 UNC 定位 DHCP Server 的关键映射

=== 步骤6：配置 APN 地址分配属性（设为 DHCP 方式） ===

ADD APN: APN="internet.example.com";
  -- 创建/确认 APN（如已存在可跳过）

SET APNADDRESSATTR: APN="internet.example.com", IPV4ALLOCTYPE=DHCP;
  -- 将 APN 的 IPv4 地址分配方式设为 DHCP
  -- 触发本特性（WSFD-104413）

=== 步骤7：（可选）配置 DHCP 请求信元参数 ===

SET DHCPPARAREQ: ..., DOMAINNAMESERVER=ENABLE, SIPSERVER=ENABLE;
  -- 控制 DHCP Discover 携带 DNS / P-CSCF 请求选项
  -- 设置后 DHCP Discover 的 Parameter Request List 将携带
  --   Domain Name Server Option（DNS 地址）
  --   SIP Server DHCP Option（P-CSCF 地址）

=== 步骤8：配置全局地址分配规则 ===

SET IPALLOCRULE: ...;
  -- 设置全局地址分配规则（与其他地址分配方式协同）
```

**场景变体**：

| 变体 | 场景说明 | 核心差异 |
|------|---------|---------|
| 仅 IPv4 地址申请 | 不需要 DNS/P-CSCF | 不配置 SET DHCPPARAREQ，Discover 仅申请 IP |
| 申请 DNS | 需要下发 DNS | SET DHCPPARAREQ 启用 Domain Name Server Option |
| 申请 P-CSCF（IMS 语音） | IMS 语音场景 | SET DHCPPARAREQ 启用 SIP Server DHCP Option；注意 P-CSCF 上限 2 个，仅支持地址不支持域名 |
| 主备 DHCP Server | 高可用场景 | ADD DHCPSERVERGRP 中配置多台 DHCPSERVER，由 BIT218 控制续租主备选择 |
| 企业网自管地址池 | 企业接入场景 | DHCP Server 部署在企业网内，UNC 作代理向企业 DHCP 申请 |
| VPN 场景 DHCP | DHCP Server 在 VPN 内 | 配置 ADD VPNINST + DHCPSERVER 携带 VPNINSTANCE |

> 说明：本特性产品文档（仅 2 个文件）未提供完整的端到端 MML 激活脚本，上述配置序列基于参考信息命令清单（9 条 MML）和特性概述原理章节构建的最小可用配置。各命令的精确参数取值需参考对应 MML 命令的产品文档（如 ADD DHCPSERVER 的 SERVERIP、VPNINSTANCE 等），Stage 3 横向分析时如有完整脚本应补充对照。

---

## 6. 验证与调测

### 6.1 验证方法

#### 6.1.1 查询命令

| 验证目的 | 命令 | 说明 |
|---------|------|------|
| 查询 DHCP 服务器配置 | LST DHCPSERVER | 查看 DHCP Server 实例 |
| 查询 DHCP 服务器组 | LST DHCPSERVERGRP | 查看服务器组组织 |
| 查询 DHCP 绑定关系 | LST DHCPBINDPOOLGRP | 验证 DHCPSERVERGRP ↔ ADDRPOOLGRP 映射 |
| 查询代理 IP | LST AGENTIP | 查看远端地址池代理 IP 配置 |
| 查询 UNC 地址池 | LST ADDRPOOL | 查看地址池配置 |
| 查询 PDU 会话 | DSP PDUSESSION | 验证用户是否通过 DHCP 成功获得 IPv4 地址 |
| 查询 APN 地址属性 | LST APNADDRESSATTR | 验证 APN 地址分配方式是否为 DHCP |

#### 6.1.2 信令跟踪

- 跟踪 UNC ↔ DHCP Server 的 DHCPv4 信令（Discover / Offer / Request / Ack）
- 验证 DHCP Discover 的 Parameter Request List 是否正确携带 DNS / P-CSCF 选项
- 验证 DHCP Offer 中 DHCP Server 是否返回了 DNS（Option 6）、P-CSCF（Option 120）地址
- 跟踪 N11（5G）/ S11（4G）/ Gn（2/3G）接口的 PDU Session Establishment Response 是否正确下发地址给 UE

#### 6.1.3 性能指标观测

通过性能指标观测 DHCP 地址分配的成功率和失败原因：

| 指标编号 | 指标名称 | 观测用途 |
|---------|---------|---------|
| 1929511781 | DHCP 地址请求次数 | 总请求量基线 |
| 1929511782 | DHCP 地址分配成功次数 | 成功率分子 |
| 1929511783 | DHCP 地址分配失败次数 | 失败率分子 |
| 1929511784 | 控制平面由于 DHCP 服务器无响应导致的 PDP 上下文激活失败次数 | DHCP Server 不可达导致的失败 |
| 1929511788 | 发送给 DHCP Server 的 DHCPv4 Discover 消息包数 | 阶段1流量 |
| 1929511785 | 接收的 DHCP Server 始发的 DHCPv4 Offer 消息包数 | 阶段2流量 |
| 1929511789 | 发送给 DHCP Server 的 DHCPv4 Request 消息包数 | 阶段3流量 |
| 1929511786 | 接收的 DHCP Server 始发的 DHCPv4 Ack 消息包数 | 阶段4流量（成功标志） |
| 1929511787 | 接收的 DHCP Server 始发的 DHCPv4 Nak 消息包数 | 阶段4流量（失败标志） |
| 1929511790 | 发送给 DHCP Server 的 DHCPv4 Decline 消息包数 | 地址冲突检测 |
| 1929511791 | 发送给 DHCP Server 的 DHCPv4 Release 消息包数 | 会话释放流量 |
| 1929511801 | DHCPv4 地址分配当前在线上下文数 | 在线用户数 |
| 1929511802 | DHCPv4 地址分配平均激活上下文数 | 平均在线 |
| 1929511803 | DHCPv4 地址分配同时在线的最大上下文数 | 峰值在线 |

### 6.2 告警参考

| 告警ID | 告警名称 | 触发条件 | 影响 |
|--------|---------|---------|------|
| ALM-100446 | DHCP 服务器无响应 | UNC 向 DHCP Server 发送消息无响应（链路断次数达 BYTE134 门限） | 新用户无法通过 DHCP 获得 IPv4 地址，PDU 会话建立失败 |

> 来源：`WSFD-104413 DHCP功能参考信息_61065989.md`（"告警"章节）

### 6.3 测量指标（分类）

> 来源：`WSFD-104413 DHCP功能参考信息_61065989.md`（"测量指标"章节）

#### 6.3.1 DHCP 消息处理类（9条）

| 指标编号 | 指标名称 |
|---------|---------|
| 1929511788 | 发送给 DHCP Server 的 DHCPv4 Discover 消息包数 |
| 1929511785 | 接收的 DHCP Server 始发的 DHCPv4 Offer 消息包数 |
| 1929511789 | 发送给 DHCP Server 的 DHCPv4 Request 消息包数 |
| 1929511786 | 接收的 DHCP Server 始发的 DHCPv4 Ack 消息包数 |
| 1929511787 | 接收的 DHCP Server 始发的 DHCPv4 Nak 消息包数 |
| 1929511790 | 发送给 DHCP Server 的 DHCPv4 Decline 消息包数 |
| 1929511791 | 发送给 DHCP Server 的 DHCPv4 Release 消息包数 |
| 1929511781 | DHCP 地址请求次数 |
| 1929511782 | DHCP 地址分配成功次数 |
| 1929511783 | DHCP 地址分配失败次数 |

#### 6.3.2 DHCP 会话测量类（3条）

| 指标编号 | 指标名称 |
|---------|---------|
| 1929511801 | DHCPv4 地址分配当前在线上下文数 |
| 1929511802 | DHCPv4 地址分配平均激活上下文数 |
| 1929511803 | DHCPv4 地址分配同时在线的最大上下文数 |

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
| 用户无法获得 IPv4 地址（PDU 会话建立失败） | DHCP Server 无响应（网络不通/服务器宕机） | 检查 ALM-100446 告警；检查 UNC 到 DHCP Server 的网络连通性；通过 LST DHCPSERVER 确认 SERVERIP 配置 |
| 用户无法获得 IPv4 地址 | DHCP Server 地址池网段与 UNC 代理 IP 不同网段 | 核对 ADD AGENTIP 的代理 IP 网段与 DHCP Server 地址池配置一致（同网段分配机制） |
| 用户无法获得 IPv4 地址 | APN 地址分配方式未设为 DHCP | LST APNADDRESSATTR 确认 IPV4ALLOCTYPE=DHCP；如未设置，SET APNADDRESSATTR 修改 |
| 用户无法获得 IPv4 地址 | DHCPBINDPOOLGRP 未正确绑定 | LST DHCPBINDPOOLGRP 确认 DHCPSERVERGRP ↔ ADDRPOOLGRP 映射存在 |
| 未获得 DNS 地址 | 未启用 DNS 请求选项 | SET DHCPPARAREQ 启用 Domain Name Server Option；确认 DHCP Server 支持 Option 6 |
| 未获得 P-CSCF 地址（IMS 语音失败） | 未启用 P-CSCF 请求选项 | SET DHCPPARAREQ 启用 SIP Server DHCP Option；确认 DHCP Server 支持 Option 120；注意仅支持地址不支持域名 |
| P-CSCF 地址超过 2 个 | 违反 P-CSCF 数量上限约束 | P-CSCF 地址最大 2 个（含本地+DHCP 分配），需精简配置 |
| DHCP 续租失败 | 主备 DHCP Server 选择异常 | 检查 BIT218 软参（DHCP 用户续租时如何选择主备 DHCP 服务器） |
| DHCP 地址分配后无法回收 | Release 消息未正确发送 | 观测指标 1929511791（Release 包数）；检查会话释放流程 |
| DHCP Server 频繁被判定为 down | 链路断次数门限过低或扫描间隔过短 | 调整 BYTE134（告警门限）、BYTE133（扫描间隔）、DWORD71（尝试间隔）软参 |
| DHCP Discover 报文被 DHCP Server 拒绝 | UDP 源端口/物理地址/Client Identifier 等 Option 不符合 Server 预期 | 调整 BYTE39 BIT2/BIT3/BIT6/BIT7/BIT8 软参控制 Discover 选项 |

---

## 7. 参考信息

### 7.1 接口与信元

| 接口/协议 | 涉及网元 | 关键信元/选项 | 说明 |
|----------|---------|--------------|------|
| DHCPv4（RFC 2131） | UNC ↔ DHCP Server | DHCP Discover / Offer / Request / Ack / Nak / Decline / Release | 标准 DHCPv4 信令交互 |
| DHCP Option 6 | DHCP Server → UNC | Domain Name Server Option | DNS 地址下发 |
| DHCP Option 120（RFC 3361） | DHCP Server → UNC | SIP Server DHCP Option | P-CSCF 地址下发 |
| DHCP Parameter Request List | UNC → DHCP Server | Discover 携带的请求选项列表 | 由 SET DHCPPARAREQ 控制 |
| N11（5G） | AMF ↔ SMF | PDU Session Establishment Request/Response | 5G 控制面接收 UE 激活、下发地址给 UE |
| S11/S4（4G） | MME ↔ SGW-C/PGW-C | Create Session Request/Response | 4G 控制面消息 |
| Gn/Gp（2/3G） | SGSN ↔ GGSN | Create PDP Context Request/Response | 2/3G 控制面消息 |

### 7.2 与其他特性的关系

| 关联特性 | 特性ID | 关系说明 |
|---------|--------|---------|
| 地址分配方式（父特性，UNC） | WSFD-010502 | 本特性是 WSFD-010502 中 DHCP 分配方式的具体实现（WSFD-010502 §3.5 描述 DHCP 代理申请方式原理，引用本特性） |
| DHCPv6 地址分配（IPv6 对端） | WSFD-104005 | 本特性负责 DHCPv4，WSFD-104005 负责 DHCPv6；两者共同构成 UNC 外置 DHCP 地址分配能力；共享 SET DHCPPARAREQ 命令 |
| 地址分配方式（UDG 侧 C-U 协同） | GWFD-010104 / GWFD-010105 | UNC 通过 DHCP 获取的 IPv4 地址需下发给 UDG 用户面执行；UDG 地址池需与 UNC DHCP 池网段一致 |
| 用户数据管理（UDM 静态分配对端） | WSFD-010400 | 同属地址分配域的另一种方式（UDM 静态），与本特性的 DHCP 动态分配并列 |
| Radius 功能（Radius 分配对端） | WSFD-011306 | 同属地址分配域的另一种方式（Radius 下发），与本特性的 DHCP 分配并列 |
| 会话管理（宿主特性） | WSFD-010501 | PDU 会话建立的宿主特性，本特性在 PDU 会话建立阶段触发 |
| 用户接入控制功能 | WSFD-106003 | APN 接入权限控制（本特性依赖 APN 正确配置） |

### 7.3 告警与软参汇总

| 类别 | 项目 | 数量/说明 |
|------|------|----------|
| 告警 | ALM-100446 DHCP服务器无响应 | 1 条 |
| 软参 | DWORD71 / BYTE134 / BYTE133 / BYTE39 BIT2 / BYTE39 BIT3 / BYTE39 BIT6 / BYTE39 BIT7 / BYTE39 BIT8 / BYTE24 / BYTE3 / BIT218 | 11 个 |
| 测量指标 | DHCP 消息处理（9）+ 会话测量（3）+ 失败流程（5）+ 指定APN（4） | 共 21 条 |

### 7.4 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-104413 DHCP功能/特性概述_60866061.md` | 适用NF（GGSN/SGW-C/PGW-C/SMF + 外置 DHCP Server）、定义（UNC 作 DHCP Client 代理用户申请 IPv4）、客户价值（动态管理 IPv4/DNS/P-CSCF、节省地址资源）、应用场景（运营商大量地址池/企业网自管）、可获得性（UNC 20.8.0+，License 82209430 LKV3W9DHCP12）、与其他特性交互（无）、对系统影响（无）、应用限制（P-CSCF 最大 2 个、仅地址不支持域名）、原理概述（UNC 作 Client、代理 IP、Parameter Request List、Domain Name Server Option/SIP Server DHCP Option、SET DHCPPARAREQ 控制）、计费（无）、特性规格（无）、遵循标准（3GPP 23.060/29.060 + RFC 2131/3361）、发布历史（v01 20.8.0） |
| 2 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-104413 DHCP功能/WSFD-104413 DHCP功能参考信息_61065989.md` | MML命令清单（9条：ADD VPNINST / ADD ADDRPOOL / ADD AGENTIP / ADD DHCPSERVERGRP / ADD DHCPSERVER / ADD DHCPBINDPOOLGRP / ADD APN / SET APNADDRESSATTR / SET IPALLOCRULE）、告警（ALM-100446）、软参（11个：DWORD71/BYTE134/BYTE133/BYTE39 BIT2-8/BYTE24/BYTE3/BIT218）、测量指标（21条：DHCP 消息处理 9 + 会话测量 3 + 失败流程 5 + 指定APN 4） |

### 7.5 关键术语（补充）

| 术语 | 全称 | 说明 |
|------|------|------|
| DHCP Client（UNC 角色） | UNC 作为 DHCP 客户端 | UNC 代理用户向 DHCP Server 申请 IP，不是 UE 直接与 DHCP Server 交互 |
| 代理 IP（Agent IP） | UNC 远端地址池代理 IP | UNC 申请时携带的网段标识，DHCP Server 据此选择同网段地址池 |
| DHCPBINDPOOLGRP | DHCP 服务器组与地址池组绑定 | UNC 定位 DHCP Server 的关键映射对象 |
| Parameter Request List | DHCP 参数请求列表 | Discover 消息中请求 DNS/P-CSCF 等可选参数的列表 |
| Domain Name Server Option | DHCP Option 6 | DNS 地址下发选项 |
| SIP Server DHCP Option | DHCP Option 120（RFC 3361） | P-CSCF 地址下发选项 |

---

## 8. 文档一致性说明（配置树 vs 产品文档 vs 关联特性）

> 配置树仅用于定位特性 ID，以下记录以产品文档实际内容为准时发现的关系与差异，供 Stage 3 横向分析参考。

### 8.1 与配置树/文档清单的关系确认

| # | 维度 | 配置树/文档清单描述 | 产品文档实际内容 | 一致性 |
|---|------|---------------------|-----------------|---------|
| 1 | 特性定位 | "DHCPv4地址分配(SMF作DHCP Client)" | 产品文档明确"UNC 作为 DHCP Client，代理用户向 DHCP Server 申请 IP 地址" | 一致 |
| 2 | License | 文档清单标注"[★核心]" | 产品文档明确 License 82209430 LKV3W9DHCP12 必需 | 一致：★核心特性需 License |
| 3 | 文件数 | 2 篇 | 2 篇（特性概述 + 参考信息） | 一致 |

### 8.2 与 WSFD-010502（地址分配方式）的关系（文档依据）

| # | 维度 | WSFD-010502 描述 | WSFD-104413 实际内容 | 关系确认 |
|---|------|------------------|---------------------|---------|
| 1 | DHCP 分配方式定义 | WSFD-010502 §3.5："UNC 作为 DHCP Client，代理用户向 DHCP Server 申请 IP 地址" | WSFD-104413 定义："UNC 通过 DHCP Client 功能从外置 DHCP 服务器地址池获取 IPv4" | **完全一致**：WSFD-104413 是 WSFD-010502 DHCP 子方式的具体实现 |
| 2 | 适用代际 | WSFD-010502 标注 DHCP 方式"主要 5G（SMF）" | WSFD-104413 适用NF为"GGSN/SGW-C/PGW-C/SMF"，覆盖 2/3/4/5G | **扩展**：WSFD-104413 实际支持全部代际，WSFD-010502 的"主要 5G"为概括 |
| 3 | DNS/P-CSCF | WSFD-010502 未展开 DHCP 申请的可选参数 | WSFD-104413 明确可通过 SET DHCPPARAREQ 申请 DNS/P-CSCF | **细化**：WSFD-104413 提供 DHCP 申请的详细可选参数机制 |
| 4 | IPv4/v6 对端 | WSFD-010502 DHCP 方式包含 DHCPv4/DHCPv6 Server | WSFD-104413 仅 DHCPv4；DHCPv6 由 WSFD-104005 负责 | **分工**：WSFD-104413（v4）+ WSFD-104005（v6）共同覆盖 |

### 8.3 与 WSFD-104005（DHCPv6地址分配）的关系（文档依据）

| # | 维度 | WSFD-104413（DHCPv4） | WSFD-104005（DHCPv6） | 关系 |
|---|------|----------------------|----------------------|------|
| 1 | 地址类型 | IPv4 地址（公网或私网） | IPv6 地址 | 互补 |
| 2 | 遵循标准 | RFC 2131（DHCPv4）+ RFC 3361（SIP Server for IPv4） | 预期遵循 RFC 8415（DHCPv6）等 | 标准不同 |
| 3 | P-CSCF 选项 | SIP Server DHCP Option（Option 120） | 预期使用 DHCPv6 SIP Server Option | 选项编码不同 |
| 4 | 共享命令 | SET DHCPPARAREQ 同时控制 DHCPv4/DHCPv6 请求信元 | 同 | **共享 SET DHCPPARAREQ**（命令名含"DHCPv4或者DHCPv6"） |
| 5 | License | 82209430 LKV3W9DHCP12 | 预期独立 License（Stage 3 验证 WSFD-104005 文档） | 待确认 |

### 8.4 文档覆盖度与缺口

| # | 维度 | 现状 | Stage 3 待补充 |
|---|------|------|---------------|
| 1 | 完整 MML 激活脚本 | 产品文档仅 2 篇，无完整端到端激活脚本 | 如有 ADD DHCPSERVER / SET APNADDRESSATTR / SET DHCPPARAREQ / SET IPALLOCRULE 等命令的详细参数文档，应横向引用补充 |
| 2 | 与 WSFD-104005 共享命令详情 | SET DHCPPARAREQ 命令在特性概述中以超链接引用，未展开参数 | Stage 3 引用 OM 参考的 SET DHCPPARAREQ 命令文档补充参数 |
| 3 | IPv4v6 双栈场景 | 本特性仅 DHCPv4，双栈需与 WSFD-104005 组合 | Stage 3 横向分析双栈场景下的 DHCPv4 + DHCPv6 协同配置 |
| 4 | C-U 协同细节 | 本特性未明确与 UDG 侧的 C-U 协同约束 | Stage 3 横向 GWFD-010104/GWFD-010105 确认 DHCP 池网段一致性约束 |
