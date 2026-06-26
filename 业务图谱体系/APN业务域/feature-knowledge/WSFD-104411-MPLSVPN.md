# WSFD-104411 MPLS VPN 知识文档

> 聚焦 APN 业务域接入方式场景的 MPLS VPN（Multiprotocol Label Switching VPN）隧道特性
> UNC（C 面 / SMF 侧）独立产品文档；与 GWFD-020411（UDG 侧 MPLS VPN）构成同域 C-U 协同对
> 与 GRE（IPFD-015002）、IPSec（IPFD-015004/016000）、L2TP（GWFD-020412/WSFD-104410）共同构成 APN 域的隧道方案矩阵
> 适用 NF：SGW-C/PGW-C/SMF（UNC）
> 核心特点：**L3VPN**（三层 VPN）、**标签交换**（非 IP 封装/非加密）、基于 **BGP+MPLS** 实现、运营商级多租户隔离

---

## 0. 元数据（三层图谱 Schema 字段）

| 字段 | 取值 |
|------|------|
| feature_id | WSFD-104411 |
| feature_name | MPLS VPN |
| feature_group | 接入方式 |
| parent_feature_id | （配置树父节点为"组网功能"特性组；无显式父特性 ID） |
| applicable_nf_map | `{"UNC": ["SGW-C", "PGW-C", "SMF"]}` |
| variant_dimensions | ["组网模型(Intranet/Extranet/Hub&Spoke/跨域VPN/Multi-VPN-Instance CE/VPN与Internet互联)", "地址族(IPv4 VPN / IPv6 VPN(6VPE) / 双栈)", "CE-PE路由协议(静态/OSPF/BGP)", "分标签方式(每路由每标签/每实例每标签/每下一跳每标签)", "跨域方式(OptionA-VRF-to-VRF/OptionB-MP-EBGP标签VPN-IPv4)", "可靠性(VPN FRR / VPN GR(仅Helper) / VPN NSR)", "骨干网隧道(LSP/TE)", "IPv6 VPN承载(6VPE-IPv4骨干网承载IPv6 VPN)"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-01, EV-FK-02, EV-FK-03, EV-FK-04, EV-FK-05, EV-FK-06, EV-FK-07, EV-FK-08, EV-FK-09] |
| license_required | **需 License**：`81203325 LKV2MPVPN01 MPLS VPN`（产品文档明确"只有获得了 License 许可后才能获得该特性的服务"） |

---

## 1. 概述

### 1.1 特性定义（是什么）

MPLS VPN 是一种 **L3VPN（Layer 3 Virtual Private Network）**。MPLS VPN 使用 **BGP（Border Gateway Protocol）** 在服务提供商骨干网上发布 VPN 路由，使用 **MPLS（Multiprotocol Label Switch）** 在服务提供商骨干网上转发 VPN 报文。骨干网是 IP 网络，通过 IP 网络中增加面向连接的控制平面，将 IP 路由技术的灵活性与 ATM 标签交换技术的简捷性无缝集成。

本特性是 **UNC（SGW-C/PGW-C/SMF）侧的三层标签交换 VPN 特性**：UNC 作为 PE（Provider Edge）或 CE（Customer Edge）/P（Provider）角色运行 BGP+MPLS 协议，通过 VPN-IPv4 地址族、RD（Route Distinguisher）、VPN Target 等 BGP 扩展属性实现多 VPN 私网隔离与跨公网互通。与 GRE/IPSec 的"IP 隧道封装"和 L2TP 的"二层 PPP 封装"不同，**MPLS VPN 通过标签交换实现报文穿越骨干网，对 VPN 的所有处理都发生在 PE 上**。

> 来源：`WSFD-104411 MPLS VPN_45033524.md`（"定义"+"实现原理"章节）[EV-FK-01]

### 1.2 适用 NF（UNC 网元）

| 涉及 NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| SGW-C / PGW-C / SMF | 控制面（UNC） | **UNC 20.2.0 及后续版本** | UNC 作为 PE/P/CE 角色运行 MPLS VPN：通过 BGP 发布 VPN-IPv4/VPN-IPv6 路由，通过 MPLS LSP 转发 VPN 报文，实现跨公网的多 VPN 隔离与互通 |

> 来源：`WSFD-104411 MPLS VPN_45033524.md`（"可获得性/版本支持"章节，UNC 20.2.0+）[EV-FK-01]

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|---------|---------|---------|
| 01 | **UNC 20.2.0** | 首次发布 |

> 来源：`WSFD-104411 MPLS VPN_45033524.md`（"发布历史"章节）[EV-FK-01]

### 1.4 License

**本特性需 License 许可**。产品文档明确声明"只有获得了 License 许许后才能获得该特性的服务"。

| License 编号 | License 名称 |
|------------|------------|
| **81203325** | **LKV2MPVPN01 MPLS VPN** |

> 来源：`WSFD-104411 MPLS VPN_45033524.md`（"可获得性/License 支持"章节）[EV-FK-01]

### 1.5 前置条件与依赖

| 前置条件 | 说明 |
|---------|------|
| License 加载 | 必须加载 License 控制项 `81203325 LKV2MPVPN01 MPLS VPN` |
| 骨干网 IP 路由可达 | PE 与 P 设备之间、PE 与对端 PE 之间的公网（IPv4）路由必须通过 IGP 或静态路由可达 |
| BGP 邻居建立 | PE 间必须建立 MP-BGP（VPNv4/VPNv6）邻居关系；PE 与 CE 间需通过静态/OSPF/BGP 交换 IPv4 路由 |
| MPLS 使能 | 骨干网 PE 与 P 设备的接口需使能 MPLS，建立 LSP 隧道（或 TE 隧道） |
| VPN 实例配置 | PE 上为每个 VPN 配置 VPN 实例（VRF），绑定 RD 与 VPN Target，并关联到 PE-CE 接口 |
| 硬件双主控（可选） | 若需 VPN NSR，设备必须具备双主控结构（主备控制平面运行在不同 OMU 上） |

> 来源：`WSFD-104411 MPLS VPN_45033524.md`（"实现原理"章节 BGP/MPLS 依赖）、`VPN NSR_92072393.md`（双主控硬件要求）[EV-FK-01, EV-FK-08]

### 1.6 与其他特性的交互

产品文档明确声明"**本特性不涉及与其他特性的交互**"。基于接入方式场景的同域横向关系（非产品文档声明，属 Stage 3 推断）：

| 交互类型 | 相关特性 | 交互说明 |
|---------|---------|---------|
| （同域并列） | GWFD-020411 MPLS VPN（UDG） | **★C-U 协同**：UDG 与 UNC 两侧均独立存在 MPLS VPN 特性文档，文档结构完全对称（9 篇文档一一对应），属双产品同构部署模式（与 GRE 类似，非 C-U 分工型） |
| （同域并列） | IPFD-015002 GRE | 隧道方案矩阵并列：GRE 为三层 IP 封装隧道（轻量不加密），MPLS VPN 为三层标签交换 VPN（多租户隔离）；两者均为 L3 隧道但机制不同 |
| （同域并列） | IPFD-015004/016000 IPSec | 隧道方案矩阵并列：IPSec 为三层加密隧道，MPLS VPN 不加密仅标签隔离 |
| （同域并列） | GWFD-020412/WSFD-104410 L2TP | 隧道方案矩阵并列：L2TP 为二层 PPP 隧道（远程地址分配），MPLS VPN 为三层标签隧道（PE 路由转发） |

> 来源：`WSFD-104411 MPLS VPN_45033524.md`（"与其他特性的交互"章节明确声明"不涉及"）[EV-FK-01]

### 1.7 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | **无**（产品文档明确声明） |
| 用户 | - 实现客户不同地理区域的网络互通<br>- 保障客户私有网络数据在公网传输过程中的**安全性**（通过 VPN 实例隔离 + 标签交换，私网数据不直接暴露在公网） |

> 来源：`WSFD-104411 MPLS VPN_45033524.md`（"受益"章节）[EV-FK-01]

### 1.8 应用场景

UNC 支持的 MPLS VPN 典型组网：

- **Intranet**：VPN 中所有用户形成闭合用户群，相互之间能流量转发，不能与本 VPN 以外用户通信（如 VPN1 的 Site1 只能与 Site4 通信）
- **Extranet**：一个 VPN 用户可以访问其他 VPN 中的站点（如 Site1、Site2 都能访问 Site3，但 Site1 与 Site2 不能互通）
- **Hub&Spoke**：VPN 中设置中心访问控制设备（Hub），其他用户（Spoke）的互访都经 Hub，使 Spoke 间通信流经 Hub 站点（中心化访问控制）
- **跨域 VPN**：VPN 骨干网跨越多个 AS（自治系统），支持 **OptionA（VRF-to-VRF）** 和 **OptionB（MP-EBGP 标签 VPN-IPv4）** 两种方式
- **Multi-VPN-Instance CE（MCE）**：通过多实例在 CE 设备上提供逻辑独立的路由实例和地址空间，多个用户共享一台 CE，以较低成本解决 VPN 业务隔离
- **VPN 与 Internet 互联**：UNC 支持 VPN 与 Internet 互联，使 VPN 除内部通信外还可访问 Internet

为提高 VPN 网络可靠性，典型组网模型：
- 骨干层：全连接、多级备份的 MPLS 网络，PE 较多时采用 BGP 路由反射器（RR）反射 VPNv4 路由
- 汇聚层：网状或环状网
- 接入层：CE 双（多）归属

> 来源：`WSFD-104411 MPLS VPN_45033524.md`（"应用场景"章节）、`Hub&Spoke_45192696.md`、`跨域VPN_45033528.md`、`Multi-VPN-Instance CE_92072389.md`[EV-FK-01, EV-FK-04, EV-FK-06, EV-FK-07]

### 1.9 对系统的影响

本特性产品文档未明确独立"对系统的影响"章节。MPLS VPN 作为 PE 运行 BGP+MPLS 协议，对 PE 性能要求较高（"对 VPN 的所有处理都发生在 PE 上，对 PE 性能要求较高"）。可靠性相关副作用见 §1.10。

> 来源：`WSFD-104411 MPLS VPN_45033524.md`（"定义"章节 PE 性能要求）[EV-FK-01]

### 1.10 应用限制

**本特性无应用限制**（产品文档明确声明）。但可靠性技术存在支持范围限制：

- **VPN GR**：目前 UNC **仅支持 GR Helper**（不支持作为 GR Restarter）
- **VPN NSR**：支持 NSR 的设备必须在硬件上具备双主控结构（主备控制平面运行在不同 OMU 上）
- **IPv6 VPN**：当前**仅支持 6VPE 方案**（IPv4 骨干网承载 IPv6 VPN），不支持 IPv6 骨干网方案
- **分标签方式切换**：每路由每标签与按下一跳分标签两种方式切换过程中，会由于本地和 ASBR 更新标签转发表造成**业务短暂丢包**

> 来源：`WSFD-104411 MPLS VPN_45033524.md`（"应用限制"章节）、`VPN GR_45192700.md`（仅 Helper）、`VPN NSR_92072393.md`（双主控要求）、`BGP_MPLS IPv6 VPN_45033532.md`（仅 6VPE）、`MPLS VPN的分标签方式_92192637.md`（切换丢包）[EV-FK-01, EV-FK-05, EV-FK-08, EV-FK-03, EV-FK-02]

### 1.11 特性规格

**本特性不涉及特性规格**（产品文档明确声明）。具体规格（如 VPN 实例数、路由数上限）需参考 UNC 产品规格手册。

> 来源：`WSFD-104411 MPLS VPN_45033524.md`（"特性规格"章节）[EV-FK-01]

### 1.12 计费与话单

产品文档未明确独立"计费与话单"章节。MPLS VPN 作为组网特性，本身不直接产生计费与话单（与 GRE/IPSec 一致）。

> 来源：`WSFD-104411 MPLS VPN_45033524.md`（未提及计费话单）[EV-FK-01]

### 1.13 遵循标准

本特性遵循大量 BGP/MPLS 相关 RFC（节选关键的，完整列表见产品文档表3）：

| 标准类别 | 标准名称 | 说明 |
|---------|---------|------|
| RFC | **RFC 4364**（MPLS VPNs，原 RFC 2547） | MPLS L3VPN 基础标准，定义 VPN 实例（per-site forwarding table） |
| RFC | **RFC 4360** BGP Extended Communities Attribute | VPN Target（Route Target）扩展团体属性 |
| RFC | **RFC 4760** Multiprotocol Extensions for BGP-4 | **MP-BGP** 多协议扩展，支持 VPN-IPv4/IPv6 地址族 |
| RFC | **RFC 3107** Support BGP carry Label for MPLS | BGP 携带 MPLS 标签 |
| RFC | **RFC 4724** Graceful Restart Mechanism for BGP | BGP GR（VPN GR 基础） |
| RFC | **RFC 4781** Graceful Restart Mechanism for BGP with MPLS | BGP+MPLS GR |
| RFC | **RFC 4798** Connecting IPv6 Islands over IPv4 MPLS using 6PE | **6VPE** IPv6 over IPv4 MPLS |
| RFC | **RFC 4271** A Border Gateway Protocol 4 (BGP-4) | BGP-4 基础协议 |
| RFC | RFC 4577 / RFC 2547 | OSPF VPN 扩展（PE-CE OSPF） |

> 来源：`WSFD-104411 MPLS VPN_45033524.md`（"遵循标准"章节，完整列表含 50+ RFC/draft）[EV-FK-01]

---

## 2. 核心概念

### 2.1 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| MPLS VPN | Multiprotocol Label Switching VPN | 基于 MPLS 的 L3VPN，使用 BGP 发布 VPN 路由，MPLS 转发 VPN 报文 |
| L3VPN | Layer 3 Virtual Private Network | 三层 VPN（网络层），MPLS VPN 属于 L3VPN |
| CE | Customer Edge | 用户网络边缘设备，有接口直接与 SP 网络相连；可以是路由器、交换机或主机；**感知不到 VPN 的存在，不需要支持 MPLS** |
| PE | Provider Edge | 服务提供商网络边缘设备，与 CE 直接相连；**对 VPN 的所有处理都发生在 PE 上**，对性能要求较高 |
| P | Provider | 服务提供商骨干设备，不与 CE 直接相连；只需具备基本 MPLS 转发能力，**不维护 VPN 信息** |
| Site | 站点 | 相互之间具备 IP 连通性的一组 IP 系统，且不需通过 SP 网络实现连通；按拓扑划分（非地理位置）；一个 site 可属于多个 VPN |
| VPN 实例 / VRF | VPN-instance / VPN Routing and Forwarding table | PE 上为每个 VPN 维护的独立路由转发表，与公网路由转发表相互独立；防止地址重叠路由相互覆盖 |
| _public_ | 公网实例 | 代表公网实例，维护公网路由 |
| __mpp_vpn_inner__ | 内联管理接口 VPN 实例 | VNF 内部各 VNFC 的内联管理接口通信 |
| __mpp_vpn_inner_server__ | 内联服务接口 VPN 实例 | VNF 内部各 VNFC 的内联服务网口通信 |
| RD | Route Distinguisher（路由标识符） | 8 字节，用于区分使用相同地址空间的 IPv4 前缀；必须保证全局唯一；加在 IPv4 前形成 VPN-IPv4 地址 |
| VPN-IPv4 地址 | - | 12 字节 = 8 字节 RD + 4 字节 IPv4 前缀；使 BGP 能区分不同 VPN 的相同 IP 前缀 |
| VPN Target / RT | Route Target（路由目标） | 32 位 BGP 扩展团体属性，控制 VPN 路由信息在 site 间的发布和接收；分 Export Target（ERT）和 Import Target（IRT） |
| ERT | Export Target | 本地 PE 从直连 site 学到 IPv4 路由后设置，随 BGP 发布 |
| IRT | Import Target | PE 收到其他 PE 发布的 VPN-IPv4 路由时，检查其 ERT，匹配本 VPN 实例的 IRT 则加入路由表 |
| MP-BGP | Multiprotocol Extensions for BGP-4 | BGP-4 多协议扩展（RFC 4760），支持 VPN-IPv4/VPN-IPv6 等地址族 |
| I-L | Inner Label（内层标签） | 私网标签，表示报文出接口或属于哪个 VPN |
| O-L | Outer Label（外层标签） | 公网标签，指示如何到达 BGP 下一跳；骨干网 P 设备做外层标签交换 |
| LSP | Label Switched Path | 标签交换路径，MPLS 隧道 |
| 倒数第二跳弹出 | Penultimate Hop Popping (PHP) | 外层标签在到达 Egress PE 前一跳弹出，Egress PE 只收带内层标签的报文 |
| MCE | Multi-VPN-Instance CE | 多实例 CE，在 CE 上提供逻辑独立的路由实例，多用户共享一台 CE |
| VPN FRR | VPN Fast Reroute | PE 间转发不通时，VPN 流量快速切换到另一条 PE-PE 链路 |
| VPN GR | VPN Graceful Restart | 主备倒换时 VPN 流量不中断；UNC 仅支持 GR Helper |
| VPN NSR | VPN Non-Stop Routing | 控制平面故障时转发与控制平面均不中断；无需邻居支持 |
| 6VPE | IPv6 VPN over IPv4 backbone | IPv4 骨干网承载 IPv6 VPN 的方案（当前 UNC 唯一支持的 IPv6 VPN 方案） |

> 来源：`WSFD-104411 MPLS VPN_45033524.md`、`基本概念_92192633.md`、`VPN GR_45192700.md`、`VPN NSR_92072393.md`、`BGP_MPLS IPv6 VPN_45033532.md`[EV-FK-01, EV-FK-02, EV-FK-05, EV-FK-08, EV-FK-03]

### 2.2 对象模型

WSFD-104411 在 UNC 侧的核心对象模型基于 **CE-PE-P 三角色 + VPN 实例（VRF）+ BGP/MPLS 协议**：

```
┌──────────────────────────────────────────────────────────────────────────┐
│ UNC（SMF/SGW-C/PGW-C）侧 MPLS VPN 对象模型（PE 角色视角）                    │
│                                                                          │
│   ┌──────────┐         ┌──────────────────────┐         ┌──────────┐    │
│   │  CE 设备  │ ──IPv4──│   PE (UNC)           │ ──BGP───│   对端 PE │    │
│   │ (用户侧) │  路由   │                      │  VPNv4  │  (UNC)   │    │
│   └──────────┘         │  ┌────────────────┐  │         └──────────┘    │
│                        │  │ 公网实例        │  │                          │
│                        │  │ _public_       │  │      ┌──────────┐        │
│                        │  └────────────────┘  │ ─────│ P 设备   │─────   │
│                        │  ┌────────────────┐  │ MPLS │ (骨干网) │        │
│                        │  │ VPN 实例 (VRF) │  │ LSP  └──────────┘        │
│                        │  │  - VPN1        │  │                          │
│                        │  │    RD=...      │  │                          │
│                        │  │    ERT/IRT=... │  │                          │
│                        │  │  - VPN2        │  │                          │
│                        │  │    RD=...      │  │                          │
│                        │  │    ERT/IRT=... │  │                          │
│                        │  └───────┬────────┘  │                          │
│                        │          │ 绑定       │                          │
│                        │  ┌───────┴────────┐  │                          │
│                        │  │ PE-CE 接口     │  │                          │
│                        │  │ (物理/子接口)  │  │                          │
│                        │  └────────────────┘  │                          │
│                        └──────────────────────┘                          │
└──────────────────────────────────────────────────────────────────────────┘

协议栈与报文结构：
  入向（CE→PE）：IPv4 报文
  PE 入口封装：[外层MPLS标签(O-L)][内层MPLS标签(I-L)][IPv4 报文]
  骨干网 P 设备：交换外层标签
  PE 出口解封装：剥离两层标签 → 纯 IPv4 报文 → CE

关键配置对象（基于 BGP/MPLS 协议族）：
  - VPN 实例 (VRF)：RD + VPN Target + 接口绑定
  - MP-BGP：VPNv4/VPNv6 地址族 + 邻居
  - MPLS：接口使能 + LSP/TE 隧道
  - PE-CE 路由：静态/OSPF/BGP
  - 可靠性：VPN FRR / GR(Helper) / NSR
```

核心对象说明：

| 对象 | 角色 | UNC 侧实现 |
|------|------|-----------|
| **VPN 实例（VRF）** | **★本特性核心对象**。PE 上为每个 VPN 维护独立路由转发表，通过 RD 实现地址空间独立，通过 VPN Target 控制 VPN 路由发布 | 手工配置，与 PE-CE 接口绑定 |
| **RD（Route Distinguisher）** | 8 字节路由标识符，区分相同地址空间的 IPv4 前缀，全局唯一 | 每个 VPN 实例配置一个 RD |
| **VPN Target（RT）** | 32 位 BGP 扩展团体属性，控制 VPN 路由在 site 间的发布和接收 | 每个 VPN 实例配置 ERT + IRT（均可多个） |
| **MP-BGP（VPNv4/VPNv6）** | PE 间交换 VPN-IPv4/VPN-IPv6 路由，携带 RD + 标签 + VPN Target | PE 间建立 MP-IBGP/MP-EBGP 邻居 |
| **MPLS LSP** | 公网隧道，承载带两层标签的 VPN 报文穿越骨干网 | 骨干网接口使能 MPLS |
| **PE-CE 路由协议** | CE 与 PE 间交换 IPv4 路由（静态/OSPF/BGP） | PE-CE 接口配置 |
| **分标签策略** | 控制私网标签分配方式（每路由/每实例/每下一跳），节省标签资源 | VPN 实例地址族或 ASBR 配置 |

> 来源：`基本概念_92192633.md`（VPN 实例/RD/VPN Target/MP-BGP 完整定义）、`MPLS VPN的分标签方式_92192637.md`[EV-FK-02, EV-FK-09]

### 2.3 在接入方式场景的角色

WSFD-104411 在 APN 接入方式场景中扮演 **"运营商级三层标签交换 VPN"** 的角色，与 GRE（轻量 IP 隧道）、IPSec（加密隧道）、L2TP（二层 PPP 隧道）形成差异化定位：

1. **L3VPN 三层 VPN**：基于网络层（IP）路由 + MPLS 标签转发，PE 维护 VPN 路由表并做三层转发（区别于 L2TP 的二层 PPP 封装）
2. **多租户隔离**：通过 VPN 实例（VRF）+ RD 实现地址空间独立，不同 VPN 可使用重叠地址空间（如多个 VPN 都用 10.110.10.0/24）
3. **标签交换（非封装/非加密）**：报文通过两层 MPLS 标签穿越骨干网，P 设备仅做外层标签交换；**不加密、不鉴权**（区别于 IPSec）
4. **BGP 路由控制**：通过 MP-BGP + VPN Target 灵活控制 VPN 路由发布，支持 Intranet/Extranet/Hub&Spoke 等多种拓扑
5. **跨域能力**：支持跨 AS（OptionA/OptionB），适合运营商级或大企业组网
6. **高可靠性**：VPN FRR + GR（Helper）+ NSR，满足电信级可靠性要求

> 来源：`WSFD-104411 MPLS VPN_45033524.md`（"定义/实现原理/应用场景"章节）[EV-FK-01]

---

## 3. 原理与流程

### 3.1 实现原理（BGP 发布路由 + MPLS 转发报文）

MPLS VPN 的核心原理是"**用 BGP 在骨干网上发布 VPN 路由，用 MPLS 在骨干网上转发 VPN 报文**"。骨干网是 IP 网络。

```
┌─────────────────────────────────────────────────────────────────────────┐
│ MPLS VPN 核心原理                                                        │
│                                                                         │
│   路由平面（BGP）：                                                      │
│     - PE 从 CE 学标准 IPv4 路由                                         │
│     - PE 加 RD 形成 VPN-IPv4 路由（12 字节 = 8B RD + 4B IPv4）           │
│     - PE 通过 MP-BGP 发布 VPN-IPv4 路由（携带 VPN Target + MPLS 标签）   │
│     - 对端 PE 按 VPN Target 匹配，加入对应 VPN 实例路由表                │
│                                                                         │
│   转发平面（MPLS）：                                                     │
│     - CE→Ingress PE：纯 IPv4 报文                                       │
│     - Ingress PE：打内层标签(I-L, 标识VPN/出接口) + 外层标签(O-L, 到BGP下跳)│
│     - 骨干网 P 设备：外层标签交换                                        │
│     - (可选) 倒数第二跳弹出外层标签                                       │
│     - Egress PE：剥离剩余标签 → 纯 IPv4 报文 → CE                        │
└─────────────────────────────────────────────────────────────────────────┘
```

**为什么用 BGP？**
- BGP 着眼于控制路由传播和选择最佳路由（而非发现计算路由），适合构建 VPN
- BGP 使用 TCP（端口 179），可靠性高，适合跨设备 PE 间交换 VPN 路由
- BGP 可承载附加路由属性（扩展团体属性），便于传播 VPN 路由
- BGP 增量更新，适合在公共网络传播大量 VPN 路由
- BGP 是 EGP，易于实现跨运营商 VPN

**为什么用 MPLS？**
- MPLS 无缝集成 IP 路由灵活性与 ATM 标签交换简捷性
- MPLS 在无连接 IP 网络中增加面向连接的控制平面
- MPLS 流量工程成为管理网络流量、减少拥塞、保证 QoS 的重要工具

> 来源：`WSFD-104411 MPLS VPN_45033524.md`（"实现原理"章节）[EV-FK-01]

### 3.2 VPN 实例与地址空间重叠解决

**问题**：不同 VPN 独立管理地址空间，可能重叠（如 VPN1 和 VPN2 都用 10.110.10.0/24）。若 PE 只维护一张路由转发表，地址重叠路由会相互覆盖导致路由丢失。

**解决**：VPN 实例（VRF）+ RD + VPN Target

- **VPN 实例（VRF）**：PE 上维护多个路由转发表（1 个公网 + N 个 VPN），各 VPN 实例维护各自 VPN 路由，公网实例维护公网路由，相互独立
- **RD（8 字节）**：使 BGP 能区分不同 VPN 的相同 IPv4 前缀。PE 从 CE 收 IPv4 路由后，加 RD 转换为全局唯一的 VPN-IPv4 路由
- **VPN Target（32 位）**：控制 VPN 路由在 site 间的发布和接收
  - ERT：本地 PE 为直连 site 路由设置，随 BGP 发布
  - IRT：PE 收到 VPN-IPv4 路由时，检查其 ERT 与本地 VPN 实例 IRT，匹配则加入该 VPN 路由表

**为什么用 VPN Target 而不直接用 RD 作为扩展团体属性？**
- 一条 VPN-IPv4 路由只能有一个 RD，但可关联多个 VPN Target（灵活）
- VPN Target 用于控制同 PE 上不同 VPN 间的路由发布（同 PE 不同 VPN 有不同 RD，BGP 扩展团体属性数量有限，直接用 RD 影响扩展性）

> 来源：`基本概念_92192633.md`（"地址空间重叠/VPN实例/RD和VPN-IPv4地址/VPN Target"章节）[EV-FK-02]

### 3.3 MPLS VPN 路由发布过程（三段式）

VPN 路由发布涉及 CE 和 PE，P 设备只维护骨干网路由，不需了解 VPN 路由。路由发布分三段：

```
┌─────────────────────────────────────────────────────────────────────────┐
│ MPLS VPN 路由发布三段式                                                  │
│                                                                         │
│   段1：本地 CE → 入口 PE                                                 │
│     - CE 与直连 PE 建立邻居/对等体（静态/OSPF/BGP）                      │
│     - CE 发布标准 IPv4 路由给 PE                                         │
│     - PE 区分路由应注入哪个 VPN 实例（手工配置，静态/路由协议自身不具备） │
│                                                                         │
│   段2：入口 PE → 出口 PE（MP-BGP）                                       │
│     - 入口 PE 为 IPv4 路由增加 RD → VPN-IPv4 路由                        │
│     - 通过 MP-BGP 发布 VPN-IPv4 路由（携带 VPN Target + MPLS 标签）      │
│     - 经 BGP 路由策略（VRF 出口策略 + peer 出口策略）过滤                │
│     - 出口 PE 检查下一跳可达性 + peer 入口策略 + 私网路由交叉（VRF 入口  │
│       策略）+ 隧道迭代 + 路由优选                                         │
│     - 按 VPN Target 加入对应 VPN 实例路由表                              │
│     - 保留：MP-BGP Update 携带的 MPLS 标签值 + 隧道迭代成功的 Tunnel ID │
│                                                                         │
│   段3：出口 PE → 远端 CE                                                 │
│     - 远端 CE 通过静态/OSPF/BGP 从出口 PE 学习 VPN 路由                  │
│     - 出口 PE 发布给远端 CE 的是普通 IPv4 路由                           │
│                                                                         │
│   本地路由交叉：PE 对来自本地 CE 的不同 VPN 路由，下一跳可达或可迭代时， │
│   与本地其他 VPN 实例的 IRT 匹配（经 VRF 入口策略过滤 + 修改属性）       │
└─────────────────────────────────────────────────────────────────────────┘
```

> 来源：`基本概念_92192633.md`（"MPLS VPN路由发布过程"章节）[EV-FK-02]

### 3.4 MPLS VPN 报文转发过程（两层标签）

以 CE1 发报文给 CE2 为例（I-L = 内层标签，O-L = 外层标签）：

```
┌─────────────────────────────────────────────────────────────────────────┐
│ MPLS VPN 报文转发流程                                                    │
│                                                                         │
│   1. CE1 → Ingress PE：发送 VPN 报文（纯 IPv4）                         │
│                                                                         │
│   2. Ingress PE 处理：                                                   │
│      - 从绑定 VPN 实例的接口接收报文                                     │
│      - 按 RD 查对应 VPN 转发表                                           │
│      - 匹配目的 IPv4 前缀，查找 Tunnel-ID                                │
│      - 打内层标签 I-L（标识 VPN/出接口）                                 │
│      - 按 Tunnel-ID 找到隧道（如 LSP），打外层标签 O-L1                  │
│      - 报文携带两层标签穿越骨干网                                        │
│                                                                         │
│   3. 骨干网 P 设备：对报文做外层标签交换（O-L1 → O-L2）                  │
│      （若应用倒数第二跳弹出，O-L2 在到达 Egress PE 前一跳弹出）          │
│                                                                         │
│   4. Egress PE 收报文：                                                  │
│      - 交 MPLS 协议处理                                                  │
│      - 去掉外层标签（若未 PHP）                                          │
│      - 剥离内层标签（栈底）                                              │
│      - 从对应出接口发送给 CE2（纯 IPv4 报文）                            │
│                                                                         │
│   报文格式演进：                                                         │
│     CE1→PE:  [IPv4 报文]                                                 │
│     PE→P:    [O-L1][I-L][IPv4 报文]                                      │
│     P→P:     [O-Lx][I-L][IPv4 报文]  (外层标签交换)                      │
│     P→PE(无PHP): [O-L2][I-L][IPv4 报文]                                  │
│     P→PE(PHP):  [I-L][IPv4 报文]      (倒数第二跳弹出外层)               │
│     PE→CE2:  [IPv4 报文]                                                  │
└─────────────────────────────────────────────────────────────────────────┘
```

**外层标签 vs 内层标签**：
- **外层标签（O-L）**：指示如何到达 BGP 下一跳（公网标签）
- **内层标签（I-L）**：表示报文的出接口或属于哪个 VPN（私网标签）

> 来源：`基本概念_92192633.md`（"MPLS VPN的报文转发过程"章节，图5）[EV-FK-02]

### 3.5 分标签方式（节省标签资源）

缺省采用"每路由每标签"（每条路由一个 MPLS 标签）。VPN 路由多时会导致标签资源不足。支持两种替代方式：

| 方式 | 定义 | 适用组网 | 配置位置 |
|------|------|---------|---------|
| **每实例每标签** | 同一 VPN 实例的所有路由共用一个标签 | 所有 MPLS VPN 组网 | 配置 VPN 实例的设备 |
| **每下一跳每标签** | 下一跳和私网标签相同的所有路由共用一个标签 | 主要用于跨域 VPN-OptionB | ASBR 设备 |

**每实例每标签效果**：PE1 配两个 VPN 实例，各收 1 万条路由，缺省占 2 万标签；配置每实例每标签后，只占 2 个标签。

**每下一跳每标签效果**：跨域 OptionB 场景，ASBR1 向 ASBR2 发布 2 万路由，未使能需 2 万标签；使能后对下一跳和出标签相同的路由只分配 1 个标签，2 万路由仅需 2 个标签。

**约束**：
- 两种方式可灵活切换，但切换过程中本地和 ASBR 需更新标签转发表，**会造成业务短暂丢包**
- 跨域 OptionB 场景，ASBR 配每下一跳每标签的同时，**PE 上必须配每实例每标签**

> 来源：`MPLS VPN的分标签方式_92192637.md`（产生原因/实现过程/使用价值）[EV-FK-09]

### 3.6 IPv6 VPN（6VPE 方案）

BGP/MPLS IPv6 VPN 扩展使 VPN 骨干网不必升级到 IPv6，就能给客户提供 IPv6 VPN 服务。

**两种组网方案**（UNC 当前**仅支持 6VPE**）：
- **6VPE**：IPv6 VPN 业务由 IPv4 骨干网实现（UNC 支持）
- IPv6 骨干网方案：IPv6 VPN 业务由 IPv6 骨干网实现（UNC 不支持）

**6VPE 原理**：
- PE-CE 间运行 IPv6 路由协议（BGP4+ / 静态 IPv6 路由 / OSPFv3）
- PE 间使用 IPv4 地址建立 VPNv6 邻居，传递 VPN-IPv6 路由
- VPN-IPv6 路由选择骨干网中的 IPv4 隧道承载 IPv6 VPN 业务
- 除 PE-CE 路由协议不同外，其他特性原理与 IPv4 VPN 相同

> 来源：`BGP_MPLS IPv6 VPN_45033532.md`[EV-FK-03]

### 3.7 可靠性机制

#### 3.7.1 VPN FRR
PE 间转发不通时，VPN 流量快速切换到另一条 PE-PE 链路，实现 VPN 业务端到端快速收敛。

#### 3.7.2 VPN GR（仅 Helper）
- **目的**：承载 VPN 流量的 UNC（PE/P/CE）发生主备倒换时 VPN 流量不中断
- **GR Restarter**：GR 重启设备（必须具备 GR 能力）—— **UNC 不支持作为 Restarter**
- **GR Helper**：GR Restarter 的邻居（必须具备 GR 能力）—— **UNC 仅支持 Helper**
- **GR Time**：Helper 发现 Restarter Down 后，仍保留拓扑/路由信息的时间
- **实现**：PE 主备倒换时，保持 VPNv4 转发状态；GR Helper 在 GR Time 内基于 Stale 路由继续转发；倒换完成后通过 IGP/BGP 重新收敛

#### 3.7.3 VPN NSR（无需邻居支持）
- **目的**：控制平面故障（主控故障）时，控制层面连接和转发层面**均不中断**
- **与 GR 区别**：
  - GR 依赖邻居支持（Helper），NSR 是**单节点技术，无需邻居支持**
  - GR 倒换期间控制流短时间中断，无法响应拓扑变化；NSR 控制层面也不中断
  - 多点同时失效时 GR 无法从邻居获路由，NSR 仍可完成主备倒换
- **实现**：通过主备主控 VPN 数据实时同步备份（私网路由/路由属性/私网标签/下一跳）
  - 批量备份：备主控启动时同步主主控数据
  - 实时备份：业务运行中实时同步
  - 倒换处理：主主控故障，备主控接管，控制层面和转发层面均不中断
- **硬件要求**：必须具备双主控结构（主备控制平面运行在不同 OMU 上）
- **与 GR 互通**：使能 NSR 的设备仍可作为 GR Helper，与不支持 NSR 的设备互通

> 来源：`WSFD-104411 MPLS VPN_45033524.md`（可靠性技术列表）、`VPN GR_45192700.md`、`VPN NSR_92072393.md`[EV-FK-01, EV-FK-05, EV-FK-08]

### 3.8 跨域 VPN（OptionA / OptionB）

随着 MPLS VPN 广泛应用，运营商不同城域网间或协作运营商骨干网间存在跨越不同 AS 的情况。RFC 4364 提出两种跨域方案：

#### OptionA（VRF-to-VRF）
- **原理**：ASBR 间不需运行 MPLS，不需跨域特殊配置；两 ASBR 直接相连，互把对端 ASBR 看作自己的 CE；通过专用接口管理自己的 VPN 路由（静态/IGP 多实例/EBGP 发布 IPv4）
- **优点**：配置简单
- **缺点**：可扩展性差——ASBR 需管理所有 VPN 路由，为每个 VPN 创建 VPN 实例；ASBR 间是普通 IP 转发，每个跨域 VPN 需不同接口；跨多 AS 时中间域必须支持 VPN 业务
- **适用**：跨域 VPN 数量少的场景

#### OptionB（MP-EBGP 标签 VPN-IPv4）
- **原理**：两 ASBR 通过 MP-EBGP 交换从各自 AS PE 接收的标签 VPN-IPv4 路由（EBGP redistribution of labeled VPN-IPv4 routes）
- **特点**：不受 ASBR 互连链路数目限制
- **ASBR 处理**：ASBR 可配置传递路由的 VPN 实例（不绑定接口）；或对标签 VPN-IPv4 特殊处理，保存全部 VPN 路由（不做 VPN Target 过滤）
- **局限性**：VPN 路由通过 ASBR 保存和扩散，VPN 路由多时 ASBR 负担重，易成故障点；ASBR 一般不再负责公网 IP 转发

> 来源：`跨域VPN_45033528.md`（OptionA/OptionB/比较）[EV-FK-06]

### 3.9 Multi-VPN-Instance CE（MCE）

**产生原因**：传统 MPLS VPN 每个 VPN 需一台 CE，成本高；多 VPN 共用 CE 则因同路由转发表无法保证数据安全。MCE 以较低成本解决多 VPN 网络的数据安全与网络成本矛盾。

**实现**：MCE 在设备上为每个需隔离的业务部署一个 VPN 实例，不同 VPN 用户部署独立路由协议与 MCE 通信，MCE 每个接口（或子接口）及 PE 接入多实例 CE 的接口绑定相应 VPN 实例，为该 VPN 用户建立独立通道，实现业务隔离。

**价值**：把 PE 功能扩展到 CE 设备（用户侧），多用户业务隔离，避免每个 VPN 单独架设 CE，节省设备开支和维护成本。

> 来源：`Multi-VPN-Instance CE_92072389.md`[EV-FK-07]

### 3.10 Hub&Spoke 组网

**场景**：VPN 中设中心访问控制设备（Hub），其他用户（Spoke）互访都经 Hub，Spoke 间通信流经 Hub 站点（中心化访问控制）。

**角色**：
- Hub 站点接入骨干网设备：Hub-PE，Hub-CE
- Spoke 站点接入骨干网设备：Spoke-PE，Spoke-CE

**VPN Target 设置规则**：
- **Spoke-PE**：ERT = "Spoke"，IRT = "Hub"；任意 Spoke-PE 的 IRT 不与其他 Spoke-PE 的 ERT 相同
- **Hub-PE**：需两个接口/子接口——一个收 Spoke-PE 路由（IRT = "Spoke"），一个向 Spoke-PE 发路由（ERT = "Hub"）

**路由发布**（site2 → site1）：
- Hub-PE 接收所有 Spoke-PE 发布的 VPN-IPv4 路由
- Hub-PE 发布的 VPN-IPv4 路由能被所有 Spoke-PE 接收
- Hub-PE 将从 Spoke-PE 学到的路由发给 Hub-CE，将从 Hub-CE 学到的路由发给所有 Spoke-PE
- 任意两 Spoke-PE 间不直接发布 VPN-IPv4 路由

**组网方案**（3 种）：
1. Hub-CE/Hub-PE、Spoke-PE/Spoke-CE 均用 EBGP：**Hub-PE 发现路由含自己 AS 号会丢弃（AS-Loop 检查），必须手工配置允许本地 AS 编号重复**
2. Hub-CE/Hub-PE、Spoke-PE/Spoke-CE 均用 IGP：IGP 路由不携带 AS_PATH，BGP VPNv4 路由 AS_PATH 为空
3. Hub-CE/Hub-PE 用 EBGP、Spoke-PE/Spoke-CE 用 IGP：同方案1，需手工配置允许本地 AS 编号重复

> 来源：`Hub&Spoke_45192696.md`[EV-FK-04]

### 3.11 与其他隧道方案的对比（★重点）

| 维度 | WSFD-104411 MPLS VPN (UNC) | GWFD-020411 MPLS VPN (UDG) | IPFD-015002 GRE | IPFD-015004/016000 IPSec | GWFD-020412/WSFD-104410 L2TP |
|------|----------------------------|----------------------------|-----------------|--------------------------|------------------------------|
| **隧道类型** | L3VPN（三层标签交换） | L3VPN（三层标签交换） | 三层 IP 封装隧道 | 三层 IP 加密隧道 | 二层 PPP 封装隧道 |
| **封装机制** | MPLS 双层标签（无 IP 封装） | MPLS 双层标签 | GRE 头 + 外层 IP 头 | ESP/AH 头 + 加密 | L2TP 头 + PPP 头 |
| **加密** | **不加密** | 不加密 | 不加密 | **加密 + 认证** | 不加密 |
| **鉴权** | 无（VPN Target 路由控制） | 无 | 无（可选 GRE Key） | 有（IKE/证书） | 有（PAP/CHAP） |
| **多租户隔离** | **★VPN 实例(VRF) + RD** | VPN 实例(VRF) + RD | 多租户共享（GRE Key 区分） | - | - |
| **地址空间重叠** | **★支持**（RD 区分） | 支持 | 不支持 | 不支持 | 不支持 |
| **路由协议** | **BGP (MP-BGP)** + IGP | BGP (MP-BGP) + IGP | 静态路由 / OSPF | 静态路由 / OSPF | PPP（IPCP） |
| **典型拓扑** | Intranet/Extranet/Hub&Spoke/跨域 | 同左 | 点对点 / 多租户共享 | 点对点 / 主备 | LAC-LNS 远程接入 |
| **跨域能力** | **★OptionA / OptionB** | OptionA / OptionB | 无 | 无 | 无 |
| **可靠性** | VPN FRR + GR(Helper) + NSR | VPN FRR + GR + NSR | Keepalive(5s/3次) | IKE DPD | Hello(60s/3次) |
| **License** | **需 81203325 LKV2MPVPN01** | （UDG 文档独立声明） | **无需 License** | 需 License | UDG 需 82200BVC |
| **首次发布版本** | **UNC 20.2.0** | （UDG 文档独立） | 20.0.0 | 20.0.0 | 20.0.0 |
| **标准** | RFC 4364/4360/4760/3107/4724 等 | 同左 | RFC 1701/1702/2784 | RFC AH/ESP/IKE | RFC 2661/2868 等 |
| **典型用途** | 运营商级多 VPN 隔离、跨域组网 | 同左 | 异种网络互通、轻量 VPN | 安全加密隧道 | 企业远程接入、LNS 地址分配 |
| **对 PE 性能要求** | **高**（所有 VPN 处理在 PE） | 高 | 低 | 中（加密开销） | 中（封装 + PPP 协商） |
| **C-U 协同模式** | **双产品对称同构**（9 篇文档一一对应） | 双产品对称同构 | 双产品对称同构 | 各自配置 | C-U 分工（C 决策/U 执行） |

> 来源：综合本特性 9 篇文档 + GWFD-020411（UDG 侧同构推断）+ IPFD-015002 GRE 知识文档（同域样例）+ 配置树 IPSec/L2TP 特性描述 [EV-FK-01..09]

### 3.12 与 GWFD-020411（UDG 侧 MPLS VPN）的 C-U 协同（★重点）

**关键发现：MPLS VPN 在 UNC 与 UDG 两侧为"双产品对称同构"模式，非 C-U 分工型**。

**证据**：
1. 两侧文档数量完全相同（均为 9 篇）
2. 文档结构一一对应（根概述 + 基本概念 + BGP/MPLS IPv6 VPN + Hub&Spoke + 分标签方式 + Multi-VPN-Instance CE + VPN GR + VPN NSR + 跨域 VPN）
3. MPLS VPN 是 PE 角色运行的协议特性，UDG 和 UNC 均可作为 PE 独立运行，不像 L2TP 那样有"C 决策 LNS 参数、U 作 LAC 封装"的天然分工

**C-U 协同要点**：
- **独立部署**：UDG 和 UNC 各自作为 PE 运行 BGP+MPLS，分别与各自的 CE 对接
- **文档同构**：两侧配置对象、命令、原理完全一致（与 GRE 同构模式相同）
- **差异化仅在产品维度**：UDG 文档针对用户面网元（SGW-U/PGW-U/UPF），UNC 文档针对控制面网元（SGW-C/PGW-C/SMF）；但 MPLS VPN 协议本身与网元类型无关
- **版本可能差异**：UNC 文档明确首次发布为 **UNC 20.2.0**（晚于 GRE 的 20.0.0）；UDG 侧版本需查 GWFD-020411 文档

**与 L2TP C-U 分工模式的对比**：
- L2TP：天然 C-U 分工（C 面 SMF 决策 LNS 参数并下发，U 面 UDG 作 LAC 执行封装，LNS 在企业网）
- MPLS VPN：**非 C-U 分工**（两侧对称同构，各自独立作 PE），与 GRE 的对称模式一致

> 来源：`WSFD-104411 MPLS VPN_45033524.md`（9 篇文档结构与 GWFD-020411 清单完全对应）、同域 IPFD-015002 GRE 知识文档（对称同构模式参照）[EV-FK-01..09]

### 3.13 协议交互

| 接口/协议 | 交互网元 | 消息类型 | 说明 |
|----------|---------|---------|------|
| PE-CE 路由协议 | CE ↔ PE | 静态路由 / OSPF / BGP（IPv4） | CE 发布标准 IPv4 路由给 PE；PE 发布普通 IPv4 路由给 CE |
| MP-BGP（VPNv4） | PE ↔ PE | BGP Update（携带 RD + VPN Target + MPLS 标签） | PE 间交换 VPN-IPv4 路由 |
| MP-BGP（VPNv6） | PE ↔ PE | BGP Update（VPN-IPv6） | 6VPE 场景，IPv4 骨干网承载 IPv6 VPN |
| MP-EBGP | ASBR ↔ ASBR | 标签 VPN-IPv4 路由 | 跨域 OptionB |
| MPLS LDP | PE ↔ P ↔ PE | 标签映射/请求 | 建立 LSP 隧道 |
| IGP（OSPF/IS-IS） | PE ↔ P | 公网路由 | 骨干网公网路由可达 |
| BGP GR | GR Restarter ↔ GR Helper | Open 消息（GR 能力）+ End-of-Rib | VPN GR（UNC 仅 Helper） |
| NSR 主备同步 | 主 OMU ↔ 备 OMU | 批量备份 + 实时备份 | VPN NSR 数据同步 |

> 来源：`基本概念_92192633.md`（路由发布三段式）、`跨域VPN_45033528.md`、`VPN GR_45192700.md`、`VPN NSR_92072393.md`[EV-FK-02, EV-FK-05, EV-FK-06, EV-FK-08]

---

## 4. 配置规则

### 4.1 激活步骤

> **重要说明**：WSFD-104411 的 9 篇 UNC 侧文档**均为原理/概念文档，不含 MML 命令行激活/调测文档**（无"激活XXX.md"/"调测XXX.md"文件）。这与同域 IPFD-015002 GRE（含激活/去激活/调测 MML 文档）形成鲜明对比。以下激活步骤基于产品文档中描述的协议原理与配置对象**逻辑推断**，具体 MML 命令需参考 UNC 产品的 BGP/MPLS 命令参考手册。

基于 MPLS VPN 协议原理的激活流程推断：

```
步骤1：确认前置条件
  ├── License 81203325 LKV2MPVPN01 MPLS VPN 已加载
  ├── 骨干网 IP 路由可达（IGP 或静态路由）
  └── PE-P-PE 接口使能 MPLS

步骤2：配置 MPLS 基础（骨干网）
  ├── 全局使能 MPLS
  ├── 接口使能 MPLS（PE-P、P-P）
  └── 建立 LSP 隧道（LDP 或 TE）

步骤3：配置 PE-CE 路由协议（IPv4 / IPv6）
  ├── 静态路由（CE-PE 互指）
  ├── OSPF（PE-CE）
  └── BGP（PE-CE）

步骤4：配置 VPN 实例（VRF）★核心
  ├── 创建 VPN 实例（如 VPN1）
  ├── 配置 RD（8 字节，全局唯一）
  ├── 配置 VPN Target（ERT + IRT，均可多个）
  └── 将 VPN 实例绑定到 PE-CE 接口

步骤5：配置 MP-BGP（VPNv4 / VPNv6 地址族）★核心
  ├── 建立 PE 间 MP-IBGP/MP-EBGP 邻居
  ├── 使能 VPNv4 地址族
  └── 将 VPN 实例路由引入 BGP

步骤6：（可选）配置分标签方式
  ├── 每实例每标签（VPN 实例地址族下）
  └── 每下一跳每标签（ASBR，跨域 OptionB）

步骤7：（可选）配置 IPv6 VPN（6VPE）
  ├── PE-CE 间配置 IPv6 路由协议（BGP4+/静态 IPv6/OSPFv3）
  └── PE 间建立 VPNv6 邻居（IPv4 地址）

步骤8：（可选）配置跨域 VPN
  ├── OptionA：ASBR 互看作 CE，VRF-to-VRF
  └── OptionB：ASBR 间 MP-EBGP 交换标签 VPN-IPv4

步骤9：（可选）配置可靠性
  ├── VPN FRR
  ├── VPN GR（UNC 仅 Helper）
  └── VPN NSR（需双主控硬件）

步骤10：（可选）配置高级组网
  ├── Hub&Spoke（双 VPN Target，Hub-PE 双接口）
  ├── Extranet（跨 VPN Target 匹配）
  └── MCE（CE 侧多实例）
```

> 来源：`WSFD-104411 MPLS VPN_45033524.md`（无独立激活文档）、`基本概念_92192633.md`（VPN 实例/RD/RT 配置逻辑）、`MPLS VPN的分标签方式_92192637.md`（分标签配置位置）、`跨域VPN_45033528.md`（跨域配置）、`Hub&Spoke_45192696.md`（Hub&Spoke 配置规则）[EV-FK-01, EV-FK-02, EV-FK-04, EV-FK-06, EV-FK-09]

### 4.2 MML 命令清单

> **★关键差异**：WSFD-104411（UNC）的 9 篇文档**不含 MML 命令文档**，与同域 GRE（IPFD-015002，含 ADD GRETUNNEL 等完整 MML）不同。MPLS VPN 的具体 MML 命令（如配置 VPN 实例、RD、RT、MP-BGP 邻居等）需参考 UNC 产品的 BGP/MPLS 命令参考手册。

基于协议原理推断的核心命令类别（非文档原文）：

| 命令类别 | 推断用途 | 文档依据 |
|---------|---------|---------|
| VPN 实例配置类 | 创建/删除 VPN 实例，配置 RD、VPN Target | `基本概念`文档明确"必须手工设置"VPN 实例与接口绑定 |
| 接口绑定类 | 将 VPN 实例绑定到 PE-CE 接口 | `基本概念`文档明确"VPN 实例和 PE 上与 CE 直接相连的接口关联" |
| MPLS 使能类 | 全局/接口使能 MPLS | `基本概念`报文转发过程依赖 MPLS LSP |
| MP-BGP 配置类 | VPNv4/VPNv6 地址族、邻居 | `基本概念`路由发布过程依赖 MP-BGP |
| 分标签配置类 | 每实例每标签 / 每下一跳每标签 | `分标签方式`文档明确"在 VPN 实例相应地址族下配置"、"在 ASBR 上使能" |
| PE-CE 路由配置类 | 静态/OSPF/BGP | `基本概念`明确 CE-PE 可用"静态路由、OSPF 或 BGP" |
| 可靠性配置类 | VPN FRR / GR Helper / NSR 使能 | `VPN GR`/`VPN NSR`文档 |
| 跨域配置类 | ASBR OptionA/OptionB | `跨域VPN`文档 |

> 来源：综合 9 篇文档的协议原理描述，推断命令类别（具体 MML 语法未在文档中出现）[EV-FK-01..09]

### 4.3 关键参数说明

基于文档明确提及的配置对象，关键参数（语义级，非 MML 参数名）：

#### 4.3.1 VPN 实例参数

| 参数（语义） | 取值 | 说明 |
|-------------|------|------|
| VPN 实例名 | 字符串（如 VPN1、_public_、__mpp_vpn_inner__） | PE 上唯一标识一个 VPN 实例 |
| RD（Route Distinguisher） | 8 字节 | 区分相同地址空间 IPv4 前缀，全局唯一 |
| Export Target（ERT） | 32 位 BGP 扩展团体属性（可多个） | 本地 PE 为直连 site 路由设置，随 BGP 发布 |
| Import Target（IRT） | 32 位 BGP 扩展团体属性（可多个） | PE 收 VPN-IPv4 路由时检查其 ERT，匹配则加入本 VPN |
| 接口绑定 | PE-CE 接口（物理/子接口） | VPN 实例与 PE-CE 接口关联（手工设置） |

#### 4.3.2 分标签方式参数

| 参数（语义） | 取值 | 说明 |
|-------------|------|------|
| 标签分配方式 | 每路由每标签（缺省）/ 每实例每标签 / 每下一跳每标签 | 控制私网标签分配粒度 |
| 配置位置 | VPN 实例地址族（每实例每标签）/ ASBR（每下一跳每标签） | 按组网场景选择 |

#### 4.3.3 Hub&Spoke 参数

| 参数（语义） | 取值 | 说明 |
|-------------|------|------|
| Hub VPN Target | ERT="Hub", IRT="Spoke" | Hub-PE 配置 |
| Spoke VPN Target | ERT="Spoke", IRT="Hub" | Spoke-PE 配置 |
| AS 编号重复 | 允许（Hub-PE EBGP 场景） | Hub-PE 发现路由含自己 AS 号会丢弃，必须手工允许 |

> 来源：`基本概念_92192633.md`（RD/ERT/IRT/接口绑定）、`MPLS VPN的分标签方式_92192637.md`（标签方式）、`Hub&Spoke_45192696.md`（Hub&Spoke 规则）[EV-FK-02, EV-FK-04, EV-FK-09]

### 4.4 约束条件

| 约束类型 | 约束内容 | 来源 |
|---------|---------|------|
| **VPN GR 仅 Helper** | UNC 仅支持 GR Helper，不支持作为 GR Restarter | `VPN GR`文档明确 |
| **VPN NSR 硬件要求** | 支持 NSR 的设备必须具备双主控结构（主备控制平面运行在不同 OMU 上） | `VPN NSR`文档明确 |
| **IPv6 VPN 仅 6VPE** | 当前仅支持 6VPE（IPv4 骨干网承载 IPv6 VPN），不支持 IPv6 骨干网方案 | `BGP/MPLS IPv6 VPN`文档明确 |
| **分标签切换丢包** | 每路由每标签与按下一跳分标签切换过程中，本地和 ASBR 更新标签转发表会造成业务短暂丢包 | `分标签方式`文档明确 |
| **跨域 OptionB ASBR 负担** | VPN 路由多时 ASBR 负担重，易成故障点；ASBR 一般不再负责公网 IP 转发 | `跨域VPN`文档明确 |
| **跨域 OptionB 信任协议** | ASBR 间不对 VPN-IPv4 路由做 VPN Target 过滤，交换路由的各 AS 服务商需达成信任协议 | `跨域VPN`文档明确 |
| **Hub&Spoke EBGP AS-Loop** | Hub-PE 与 Hub-CE 用 EBGP 时，Hub-PE 发现路由含自己 AS 号会丢弃，必须手工配置允许本地 AS 编号重复 | `Hub&Spoke`文档明确 |
| **跨域 OptionB 标签配合** | ASBR 配每下一跳每标签时，PE 上必须配每实例每标签 | `分标签方式`文档明确 |
| **地址空间重叠限制** | 两 VPN 使用重叠地址空间的条件：无共同 site，或有共同 site 但不与重叠地址设备互访 | `基本概念`文档明确 |
| **VPN 实例手工绑定** | PE 从 CE 学路由时需区分注入哪个 VPN 实例，静态路由和路由协议自身不具备区分能力，必须手工配置 | `基本概念`文档明确 |
| **PE 性能要求** | 对 VPN 的所有处理都发生在 PE 上，对 PE 性能要求较高 | `概述`文档明确 |

---

## 5. 配置案例

### 5.1 典型场景：基本 MPLS VPN（Intranet，IPv4）

> **重要说明**：WSFD-104411（UNC）9 篇文档**不含 MML 配置脚本示例**（与 GRE 文档含完整 ADD GRETUNNEL 脚本不同）。以下案例基于产品文档描述的组网模型与协议原理**逻辑推断**，非文档原文 MML。

**场景描述**：企业 X 有 A 市总部（Site1）和 B 市分支机构（Site2），通过运营商 MPLS 骨干网实现 Intranet 互通。CE1-PE1-骨干网-P-PE2-CE2 拓扑，VPN1 的 Site1 与 Site2 互通，不能与其他 VPN 通信。

**配置逻辑（语义级，非 MML）**：

```
=== PE1（UNC）配置（Site1 侧）===

// 1. 配置 VPN 实例 VPN1
//    RD = 100:1（全局唯一）
//    ERT = 100:1
//    IRT = 100:1
// 2. 将 VPN1 绑定到 PE1-CE1 接口
// 3. 配置 PE1-CE1 路由协议（如 OSPF 或 BGP）
// 4. 配置 MP-BGP：
//    - 与 PE2 建立 MP-IBGP 邻居
//    - 使能 VPNv4 地址族
//    - 将 VPN1 路由引入 BGP

=== PE2（UNC）配置（Site2 侧）===

// 1. 配置 VPN 实例 VPN1
//    RD = 100:1（与 PE1 相同 RD，或不同 RD 但 IRT 匹配 PE1 ERT）
//    ERT = 100:1
//    IRT = 100:1
// 2. 将 VPN1 绑定到 PE2-CE2 接口
// 3. 配置 PE2-CE2 路由协议
// 4. 配置 MP-BGP（与 PE1 对称）

=== 骨干网 P 设备配置 ===

// 1. 接口使能 MPLS
// 2. 运行 IGP（OSPF/IS-IS）保证公网路由可达
// 3. 运行 MPLS LDP 建立 LSP

=== 报文转发（CE1 → CE2）===

// 1. CE1 发纯 IPv4 报文到 PE1
// 2. PE1 打内层标签 I-L（标识 VPN1）+ 外层标签 O-L1（到 PE2）
// 3. P 设备外层标签交换 O-L1 → O-L2
// 4. （PHP）倒数第二跳弹出外层标签
// 5. PE2 剥离内层标签，发纯 IPv4 报文给 CE2
```

> 来源：`WSFD-104411 MPLS VPN_45033524.md`（"定义/应用场景/实现原理"章节）、`基本概念_92192633.md`（图5 VPN 报文转发过程）[EV-FK-01, EV-FK-02]

### 5.2 场景变体

| 变体 | 场景说明 | 核心差异 | 文档覆盖度 |
|------|---------|---------|-----------|
| **Intranet（IPv4）** | 闭合用户群 VPN 互通 | 单 VPN 实例，ERT=IRT | 基本概念文档（场景 5.1） |
| **Extranet** | VPN 间互访（如 Site1、Site2 访问 Site3） | 多 VPN 实例，跨 VPN Target 匹配 | 概述文档应用场景 |
| **Hub&Spoke** | 中心化访问控制 | 双 VPN Target（Hub/Spoke），Hub-PE 双接口，EBGP 需允许 AS 重复 | Hub&Spoke 文档完整 |
| **跨域 OptionA** | 跨 AS，ASBR 互看作 CE | VRF-to-VRF，ASBR 间普通 IP 转发 | 跨域 VPN 文档完整 |
| **跨域 OptionB** | 跨 AS，ASBR 间 MP-EBGP | 标签 VPN-IPv4 路由交换，每下一跳每标签 | 跨域 VPN + 分标签文档 |
| **Multi-VPN-Instance CE（MCE）** | 多用户共享一台 CE | CE 侧多 VPN 实例 + 接口绑定 | MCE 文档完整 |
| **VPN 与 Internet 互联** | VPN 访问 Internet | 概述文档提及，无独立文档 | 仅概述提及 |
| **IPv6 VPN（6VPE）** | IPv4 骨干网承载 IPv6 VPN | PE-CE 用 IPv6 路由协议，PE 间 VPNv6 邻居 | 6VPE 文档完整 |
| **分标签优化（每实例）** | 节省 PE 标签资源 | VPN 实例地址族下配置每实例每标签 | 分标签文档完整 |
| **VPN FRR** | PE 间链路故障快速切换 | PE-PE 备链路 | 概述文档提及 |
| **VPN GR（Helper）** | 邻居主备倒换时流量不中断 | UNC 作 Helper，GR Time 内保留路由 | GR 文档完整 |
| **VPN NSR** | 本节点主控故障时控制+转发均不中断 | 双主控硬件，主备实时同步 | NSR 文档完整 |

---

## 6. 验证与调测

### 6.1 验证方法

> **重要说明**：WSFD-104411（UNC）9 篇文档**不含调测文档**（无"调测XXX.md"文件），与同域 GRE（含 3 步调测流程）不同。以下验证方法基于协议原理与可靠性文档**推断**。

#### 6.1.1 推断查询命令（语义级，非文档原文 MML）

| 验证目的 | 推断命令类别 | 说明 |
|---------|-------------|------|
| 查询 VPN 实例配置 | LST VPN 实例类 | 查看 RD、ERT、IRT、接口绑定 |
| 查询 BGP VPNv4 邻居 | LST BGP peer 类 | 查看 MP-IBGP/MP-EBGP 邻居状态 |
| 查询 VPN 路由 | LST VPN 路由类 | 查看 VPN 实例路由表 |
| 查询 MPLS LSP | LST LSP 类 | 查看 LSP 隧道状态 |
| 查询 MPLS 标签 | LST MPLS label 类 | 查看标签分配（每路由/每实例/每下一跳） |
| 查询 NSR 状态 | LST NSR 类 | 查看主备同步状态 |

#### 6.1.2 可靠性验证（基于文档）

**VPN GR 验证**：
- GR Restarter 主备倒换时，GR Helper（UNC）应在 GR Time 内保留 Stale 路由继续转发
- 倒换完成后，通过 End-of-Rib 消息触发收敛

**VPN NSR 验证**：
- 主主控故障时，备主控接管，控制层面（BGP/MPLS 邻居关系）和转发层面均不中断
- 邻居控制平面不感知

> 来源：`VPN GR_45192700.md`（GR Time、Stale 标记、End-of-Rib）、`VPN NSR_92072393.md`（主备同步、邻居不感知）[EV-FK-05, EV-FK-08]

### 6.2 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| VPN 路由不通 | VPN Target 不匹配（ERT 与对端 IRT 不一致） | 检查两端 VPN 实例 ERT/IRT 配置；Extranet 需跨 VPN Target 匹配 |
| VPN 路由不通 | RD 未全局唯一（CE 双归属时路由异常） | 检查 RD 规划，确保全局唯一 |
| VPN 路由丢失 | PE 只维护一张路由表（未配 VPN 实例） | 为每个 VPN 配置独立 VPN 实例 |
| 地址空间重叠导致路由覆盖 | 未用 RD 区分 | PE 从 CE 收路由后必须加 RD 转 VPN-IPv4 |
| 报文转发失败 | MPLS LSP 未建立或 Down | 检查骨干网 MPLS 使能；检查 LDP 邻居；查询 LSP 状态 |
| 报文转发失败 | 隧道迭代失败（Tunnel ID 无效） | 检查公网路由可达性；检查 IGP |
| 跨域 OptionB 路由不通 | ASBR 未配每下一跳每标签，PE 未配每实例每标签 | 按跨域 OptionB 要求，ASBR + PE 标签方式配合配置 |
| 跨域 OptionB 路由丢失 | ASBR 对 VPN-IPv4 做 VPN Target 过滤 | ASBR 间不做 VPN Target 过滤（需信任协议） |
| Hub&Spoke 路由丢失（EBGP） | Hub-PE AS-Loop 检查丢弃路由 | Hub-PE 手工配置允许本地 AS 编号重复 |
| 分标签切换业务丢包 | 标签分配方式切换中标签转发表更新 | 在维护窗口切换；切换完成后验证 |
| 6VPE IPv6 路由不通 | 误用 IPv6 骨干网方案（UNC 不支持） | 确认使用 6VPE（IPv4 骨干网 + VPNv6 邻居） |
| GR 倒换后流量中断 | UNC 作 GR Restarter（不支持） | UNC 仅作 GR Helper，Restarter 需邻居设备 |
| NSR 倒换失败 | 单主控硬件 | NSR 需双主控结构硬件 |
| Extranet 路由不全 | 同 PE 不同 VPN 未做本地路由交叉 | 确保本地路由交叉通过 VRF 入口策略 |

---

## 7. 参考信息

### 7.1 与其他特性的关系

| 关联特性 | 特性ID | 关系说明 |
|---------|--------|---------|
| **MPLS VPN（UDG）** | **GWFD-020411** | **★C-U 协同（双产品对称同构）**：UDG 与 UNC 两侧文档结构完全对称（9 篇一一对应），均独立作 PE 运行 BGP+MPLS，非 C-U 分工型 |
| GRE | IPFD-015002 | **隧道方案矩阵并列**：GRE 为三层 IP 封装隧道（轻量不加密，点对点），MPLS VPN 为三层标签交换 VPN（多租户隔离，PE 路由转发） |
| IPSec（UDG） | IPFD-015004 | **隧道方案矩阵并列**：IPSec 为三层加密隧道，MPLS VPN 不加密仅标签隔离 |
| IPSec（UNC） | IPFD-016000 | 同上（UNC 侧 IPSec） |
| L2TP VPN（UDG） | GWFD-020412 | **隧道方案矩阵并列**：L2TP 为二层 PPP 隧道（LNS 远程地址分配，C-U 分工），MPLS VPN 为三层标签隧道（PE 路由转发，C-U 对称） |
| L2TP VPN（UNC） | WSFD-104410 | 同上（UNC 侧 L2TP） |
| Radius 功能 | WSFD-011306 | **潜在应用场景**：Radius 组网中带内/带外 GRE VPN 场景（见 IPFD-015002），MPLS VPN 理论上也可用于此类组网穿越，但本特性文档未声明 |

> 来源：`WSFD-104411 MPLS VPN_45033524.md`（明确"不涉及与其他特性的交互"）、同域 IPFD-015002 GRE 知识文档（隧道矩阵横向关系）[EV-FK-01]

### 7.2 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104411 MPLS VPN/WSFD-104411 MPLS VPN_45033524.md` | **★特性根概述**：定义（L3VPN，CE/PE/P 三角色）、受益（运营商无、用户网络互通+安全性）、可获得性（**UNC 20.2.0+，License 81203325 LKV2MPVPN01**）、应用限制（无）、与其他特性交互（无）、应用场景（Intranet/Extranet/Hub&Spoke/跨域VPN/MCE/VPN与Internet互联 + 可靠性组网模型 + VPN FRR/GR/NSR）、实现原理（BGP 发布路由 + MPLS 转发报文）、特性规格（无）、遵循标准（50+ RFC/draft）、发布历史（v01 UNC 20.2.0） |
| 2 | `output/.../WSFD-104411 MPLS VPN/基本概念_92192633.md` | **★核心概念**：site 定义、地址空间重叠、VPN 实例（VRF，_public_/__mpp_vpn_inner__/__mpp_vpn_inner_server__）、VPN/Site/VPN 实例关系、RD（8B）+ VPN-IPv4 地址（12B）、VPN Target（ERT/IRT，32 位扩展团体属性）、MP-BGP（RFC 4760）、**MPLS VPN 路由发布三段式**（CE→PE→PE→CE）、**MPLS VPN 报文转发过程**（两层标签 I-L/O-L + 倒数第二跳弹出）、本地路由交叉 |
| 3 | `output/.../WSFD-104411 MPLS VPN/BGP_MPLS IPv6 VPN_45033532.md` | **6VPE 方案**：IPv6 VPN 两种方案（6VPE-IPv4 骨干网 / IPv6 骨干网，**当前仅支持 6VPE**）、PE-CE IPv6 路由协议（BGP4+/静态 IPv6/OSPFv3）、PE 间 IPv4 地址建 VPNv6 邻居 |
| 4 | `output/.../WSFD-104411 MPLS VPN/Hub&Spoke_45192696.md` | **Hub&Spoke 组网**：Hub/Spoke 角色（Hub-PE/Hub-CE/Spoke-PE/Spoke-CE）、VPN Target 设置规则（Spoke-PE: ERT=Spoke/IRT=Hub；Hub-PE: 双接口双 Target）、路由发布途径、3 种组网方案（EBGP/IGP/混合）、**EBGP 场景 AS-Loop 检查问题 + 手工允许 AS 重复** |
| 5 | `output/.../WSFD-104411 MPLS VPN/MPLS VPN的分标签方式_92192637.md` | **分标签方式**：产生原因（每路由每标签导致标签资源不足）、三种方式（每路由每标签-缺省/每实例每标签/每下一跳每标签）、实现过程（每实例节省 PE 标签；每下一跳节省 ASBR 标签）、**切换过程业务短暂丢包**、**跨域 OptionB ASBR+PE 标签方式配合** |
| 6 | `output/.../WSFD-104411 MPLS VPN/Multi-VPN-Instance CE_92072389.md` | **MCE 技术**：产生原因（多 VPN 共用 CE 的安全与成本矛盾）、实现流程（CE 侧多 VPN 实例 + 接口绑定 + RT 匹配 PE）、实用价值（PE 功能扩展到 CE，节省设备开支） |
| 7 | `output/.../WSFD-104411 MPLS VPN/VPN GR_45192700.md` | **VPN GR**：GR 实现前提（控制转发分离多 RP 结构）、GR 相关概念（GR Restarter/GR Helper/GR Session/GR Time）、**UNC 仅支持 GR Helper**、VPN GR 概述（主备倒换流量不中断，丢包率 0%）、PE/P/CE 主备倒换处理流程（IGP/BGP/MPLS LDP GR 协商 + Stale 标记 + End-of-Rib 收敛） |
| 8 | `output/.../WSFD-104411 MPLS VPN/VPN NSR_92072393.md` | **VPN NSR**：产生原因（GR 依赖邻居、多点失效无法恢复）、相关概念（HA/NSR/NSF/主备主控）、实现过程（主备主控 VPN 数据实时同步：私网路由/属性/标签/下一跳 + 批量备份 + 实时备份 + 倒换处理）、**硬件要求（双主控结构）**、与 GR 互通（NSR 设备可作 GR Helper）、适用场景（单节点多链路接入，大容量大负载网络） |
| 9 | `output/.../WSFD-104411 MPLS VPN/跨域VPN_45033528.md` | **跨域 VPN**：OptionA（VRF-to-VRF，ASBR 互看作 CE，配置简单但扩展性差）、OptionB（MP-EBGP 标签 VPN-IPv4，不受链路数限制但 ASBR 负担重）、ASBR 特殊处理（配 VPN 实例不绑接口 / 保存全部 VPN 路由不做 VPN Target 过滤）、跨域方式比较表 |

### 7.3 关键术语速查

| 术语 | 全称 | 说明 |
|------|------|------|
| MPLS VPN | Multiprotocol Label Switching VPN | 基于 MPLS 的 L3VPN |
| L3VPN | Layer 3 VPN | 三层 VPN |
| CE | Customer Edge | 用户边缘设备 |
| PE | Provider Edge | 运营商边缘设备（VPN 处理都在 PE） |
| P | Provider | 运营商骨干设备（只 MPLS 转发） |
| VRF | VPN Routing and Forwarding | VPN 实例/路由转发表 |
| RD | Route Distinguisher | 路由标识符（8B，区分重叠地址） |
| VPN Target / RT | Route Target | 路由目标（32B，控制 VPN 路由发布） |
| ERT / IRT | Export / Import Target | 出口/入口路由目标 |
| VPN-IPv4 | - | 12B = 8B RD + 4B IPv4 |
| MP-BGP | Multiprotocol BGP | 多协议 BGP 扩展 |
| I-L / O-L | Inner / Outer Label | 内层（VPN）/外层（公网）标签 |
| LSP | Label Switched Path | 标签交换路径 |
| PHP | Penultimate Hop Popping | 倒数第二跳弹出 |
| MCE | Multi-VPN-Instance CE | 多实例 CE |
| VPN FRR | VPN Fast Reroute | VPN 快速重路由 |
| VPN GR | VPN Graceful Restart | VPN 平滑重启（UNC 仅 Helper） |
| VPN NSR | VPN Non-Stop Routing | VPN 不间断路由（需双主控） |
| 6VPE | IPv6 VPN over IPv4 | IPv4 骨干网承载 IPv6 VPN |
| OptionA / OptionB | - | 跨域 VPN 两种方式 |

---

## 8. 文档一致性说明（配置树 vs 产品文档）

> 配置树仅用于定位特性 ID，以下记录以产品文档实际内容为准时发现的差异与协同点，供 Stage 3 横向分析参考。

### 8.1 与任务要求中提及对象的核对（★重点澄清）

| # | 任务要求提及 | 产品文档实际 | 核对结论 |
|---|-------------|-------------|---------|
| 1 | **SMF 侧 MPLS VPN** | **确认**：WSFD-104411 适用 NF 为 SGW-C/PGW-C/SMF（UNC），首次发布 **UNC 20.2.0**。MPLS VPN 是 PE 角色运行的 L3VPN 协议特性，UNC 作为 PE 运行 BGP+MPLS | 已覆盖（见 §1.1、§1.2） |
| 2 | **与 GWFD-020411（UDG 侧 MPLS）的 C-U 协同** | **★关键发现**：两侧为**双产品对称同构**模式（9 篇文档一一对应），非 C-U 分工型。UDG 与 UNC 均独立作 PE 运行 BGP+MPLS，无 C 决策/U 执行的天然分工。这与 L2TP（C-U 分工）形成对比，与 GRE（对称同构）一致 | **澄清**：MPLS VPN 在 C/U 两侧对称同构，任务要求中"C-U 协同"应理解为"双产品对称部署"而非"C-U 分工"（见 §3.12） |
| 3 | **与其他隧道（GRE/IPSec/L2TP）对比** | **确认**：MPLS VPN 与三者形成差异化定位——L3VPN 标签交换（非 IP 封装/非加密）、支持地址空间重叠（RD）、支持跨域（OptionA/B）、高可靠性（FRR/GR/NSR）。与 GRE（轻量 IP 隧道）、IPSec（加密隧道）、L2TP（二层 PPP）构成完整隧道矩阵 | 已覆盖（见 §3.11） |
| 4 | **MPLS 配置对象（文档依据）** | **★关键差异**：WSFD-104411 的 9 篇文档**均为原理/概念文档，不含 MML 命令行激活/调测文档**（无"激活XXX.md"/"调测XXX.md"）。这与同域 GRE（IPFD-015002，含 ADD GRETUNNEL 等 6 条核心 MML + 完整脚本）形成鲜明对比。MPLS VPN 的核心配置对象（VPN 实例/RD/RT/MP-BGP/MPLS 使能/分标签）在原理文档中有明确语义定义，但**具体 MML 命令语法未在文档中出现**，需参考 UNC BGP/MPLS 命令参考手册 | **澄清**：文档只讲"是什么/为什么"，不讲"怎么配 MML"；配置对象可从原理文档语义级推断（见 §4.2） |
| 5 | **配置树补全** | **确认**：文档清单列 9 个文件（全部 UNC 侧），均为原理/概念文档。配置树将此特性归入"组网功能"特性组 | 文档结构完整但缺 MML 操作类文档 |

### 8.2 与配置树/文档清单的差异

| # | 维度 | 配置树/文档清单描述 | 产品文档实际内容 | 差异类型 |
|---|------|---------------------|-----------------|---------|
| 1 | 文档类型分布 | 文档清单列 9 个文件 | 9 个文件**全部为原理/概念文档**（根概述 + 8 篇子主题原理），**无激活/调测/去激活 MML 文档** | 补全：与同域 GRE（IPFD-015002，含激活/去激活/调测）相比，MPLS VPN 文档集偏原理，缺操作类文档 |
| 2 | License 要求 | 文档清单标注"[★核心]" | 产品文档明确声明**需 License 81203325 LKV2MPVPN01** | 澄清：MPLS VPN 需 License，区别于 GRE（无需 License） |
| 3 | C-U 协同模式 | 任务要求暗示"C-U 协同" | 实际为**双产品对称同构**（与 GWFD-020411 文档结构一一对应） | 澄清：非 C-U 分工，与 GRE 对称模式一致 |
| 4 | 首次发布版本 | 文档清单未标注版本 | **UNC 20.2.0**（晚于 GRE 的 20.0.0） | 补全：版本信息 |
| 5 | 应用限制 | 文档清单简述"MPLS VPN 隧道（SMF 侧）" | 产品文档明确声明"**本特性无应用限制**"，但可靠性技术存在支持范围限制（GR 仅 Helper、NSR 需双主控、6VPE 仅 IPv4 骨干网） | 澄清：无应用限制，但有可靠性技术支持范围 |
| 6 | 特性规格 | 文档清单未提及 | 产品文档明确声明"**本特性不涉及特性规格**" | 澄清：规格需查 UNC 产品规格手册 |
| 7 | 与其他特性交互 | 文档清单未提及 | 产品文档明确声明"**本特性不涉及与其他特性的交互**" | 澄清：产品文档维度无交互声明（Stage 3 同域横向关系属推断） |
| 8 | 计费与话单 | 文档清单未提及 | 产品文档未设独立章节（组网特性，不直接产生计费） | 澄清：与 GRE/IPSec/L2TP 一致，组网特性不产生计费 |

### 8.3 与同域隧道特性的横向对比（★Stage 3 重点）

| # | 维度 | WSFD-104411 MPLS VPN (UNC) | GWFD-020411 MPLS VPN (UDG) | IPFD-015002 GRE | IPFD-015004/016000 IPSec | GWFD-020412/WSFD-104410 L2TP |
|---|------|----------------------------|----------------------------|-----------------|--------------------------|------------------------------|
| 1 | 隧道类型 | L3VPN（标签交换） | L3VPN（标签交换） | 三层 IP 封装 | 三层 IP 加密 | 二层 PPP 封装 |
| 2 | 加密 | 无 | 无 | 无 | **有** | 无 |
| 3 | 多租户隔离 | **★VRF + RD** | VRF + RD | GRE Key | - | - |
| 4 | 地址重叠支持 | **★支持（RD）** | 支持 | 不支持 | 不支持 | 不支持 |
| 5 | 跨域能力 | **★OptionA/B** | OptionA/B | 无 | 无 | 无 |
| 6 | 可靠性 | FRR+GR+NSR | FRR+GR+NSR | Keepalive | IKE DPD | Hello |
| 7 | License | **81203325** | （UDG 独立） | 无 | 有 | UDG: 82200BVC |
| 8 | 首发版本 | **UNC 20.2.0** | （UDG 独立） | 20.0.0 | 20.0.0 | 20.0.0 |
| 9 | C-U 模式 | **对称同构** | 对称同构 | 对称同构 | 各自配置 | **C-U 分工** |
| 10 | 文档含 MML | **否（仅原理）** | 否（仅原理） | **是（6 条核心）** | 是（多场景） | 是 |
| 11 | PE 性能要求 | **高** | 高 | 低 | 中 | 中 |
| 12 | 典型用途 | 运营商级多 VPN | 同左 | 轻量 VPN | 安全加密 | 远程接入 |

---

## 附录 A：source_evidence_ids 占位映射

| evidence_id | 对应来源文件 | 主要贡献章节 |
|-------------|-------------|-------------|
| EV-FK-01 | `WSFD-104411 MPLS VPN_45033524.md`（根概述） | ★特性定义（L3VPN，CE/PE/P）、受益（运营商无/用户互通+安全）、可获得性（UNC 20.2.0+，License 81203325）、应用限制（无）、与其他特性交互（无）、应用场景（6 种组网 + 可靠性组网模型 + FRR/GR/NSR）、实现原理（BGP 发路由 + MPLS 转发）、特性规格（无）、遵循标准（50+ RFC）、发布历史（v01 UNC 20.2.0） |
| EV-FK-02 | `基本概念_92192633.md` | ★核心概念：site、地址空间重叠、VPN 实例（VRF，3 种内置实例）、VPN/Site/VPN 实例关系、RD（8B）+ VPN-IPv4（12B）、VPN Target（ERT/IRT）、MP-BGP（RFC 4760）、路由发布三段式（CE→PE→PE→CE）、报文转发过程（I-L/O-L 双层标签 + PHP）、本地路由交叉 |
| EV-FK-03 | `BGP_MPLS IPv6 VPN_45033532.md` | 6VPE 方案（IPv4 骨干网承载 IPv6 VPN，当前唯一支持）、PE-CE IPv6 路由协议（BGP4+/静态 IPv6/OSPFv3）、PE 间 IPv4 地址建 VPNv6 邻居 |
| EV-FK-04 | `Hub&Spoke_45192696.md` | Hub&Spoke 组网：角色定义、VPN Target 规则（Spoke-PE: ERT=Spoke/IRT=Hub；Hub-PE: 双 Target 双接口）、路由发布途径、3 种组网方案、EBGP AS-Loop 检查 + 手工允许 AS 重复 |
| EV-FK-05 | `VPN GR_45192700.md` | VPN GR：实现前提（控制转发分离）、概念（Restarter/Helper/Session/Time）、**UNC 仅 Helper**、PE/P/CE 主备倒换处理流程（Stale 标记 + End-of-Rib 收敛） |
| EV-FK-06 | `跨域VPN_45033528.md` | 跨域 VPN：OptionA（VRF-to-VRF，配置简单扩展性差）、OptionB（MP-EBGP 标签 VPN-IPv4，不受链路数限制 ASBR 负担重）、ASBR 特殊处理（不做 VPN Target 过滤，需信任协议）、跨域方式比较 |
| EV-FK-07 | `Multi-VPN-Instance CE_92072389.md` | MCE 技术：产生原因（多 VPN 共用 CE 安全成本矛盾）、实现流程（CE 侧多 VPN 实例 + 接口绑定 + RT 匹配）、价值（PE 功能扩展到 CE） |
| EV-FK-08 | `VPN NSR_92072393.md` | VPN NSR：产生原因（GR 依赖邻居/多点失效）、概念（HA/NSR/NSF/主备主控）、实现（主备实时同步：私网路由/属性/标签/下一跳）、**硬件要求双主控**、与 GR 互通、适用场景 |
| EV-FK-09 | `MPLS VPN的分标签方式_92192637.md` | 分标签方式：三种方式（每路由-缺省/每实例/每下一跳）、实现过程（每实例节省 PE 标签；每下一跳节省 ASBR 标签）、切换丢包、跨域 OptionB ASBR+PE 标签配合 |
