# GWFD-020411 MPLS VPN 知识文档

> 聚焦 APN 业务域接入方式场景的 MPLS VPN（BGP/MPLS IP VPN）隧道特性
> UDG（U 面）侧，三层标签交换 VPN；与 GRE（IPFD-015002）、IPSec（IPFD-015004）、L2TP（GWFD-020412）共同构成 APN 域的隧道方案矩阵
> 适用 NF：SGW-U/PGW-U/UPF（UDG）；UNC 侧对应 WSFD-104411（SMF），两侧特性名称对称但分产品部署
> C-U 对称：UDG 与 UNC 两产品均存在同名"MPLS VPN"特性（基本概念、分标签、Hub&Spoke、跨域、IPv6 VPN、MCE、GR、NSR 子文档一一对应），属双产品同构部署

---

## 0. 元数据（三层图谱 Schema 字段）

| 字段 | 取值 |
|------|------|
| feature_id | GWFD-020411 |
| feature_name | MPLS VPN |
| feature_group | 接入方式 |
| parent_feature_id | （无显式父节点；与 IPFD-015000 VPN 功能同属接入方式类，配置树并列） |
| applicable_nf_map | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| variant_dimensions | ["组网模型(Intranet/Extranet/Hub&Spoke/跨域/VPN与Internet互联)", "分标签方式(每路由每标签/每实例每标签/每下一跳每标签)", "跨域方式(OptionA-VRF-to-VRF / OptionB-MP-EBGP标签VPN-IPv4)", "地址族(IPv4 VPN / IPv6 VPN-6VPE)", "IPv6承载方案(6VPE: IPv4骨干网承载IPv6 VPN业务)", "MCE多实例CE(共享CE/业务隔离)", "可靠性(VPN FRR / VPN GR-Helper / VPN NSR)", "PE-CE路由协议(静态/OSPF/BGP)", "路由标识(RD 12字节VPN-IPv4)/VPN Target(ERT/IRT扩展团体属性)"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-01, EV-FK-02, EV-FK-03, EV-FK-04, EV-FK-05, EV-FK-06, EV-FK-07, EV-FK-08, EV-FK-09] |
| license_required | **需 License**（产品文档明确"本特性是可选特性，只有获得了 License 许可后才能获得该特性的服务"；具体 License 控制项编号文档未列出，Stage 3 从 license 数据表补全） |

---

## 1. 概述

### 1.1 特性定义（是什么）

MPLS VPN 是一种 **L3VPN（Layer 3 Virtual Private Network）**，基于 **BGP/MPLS** 技术在 IP 骨干网上为用户提供三层虚拟专用网络服务。其基本模型由三部分组成：

- **CE（Customer Edge）**：用户网络边缘设备，有接口直接与服务提供商 SP 网络相连。CE 可以是路由器或交换机，也可以是一台主机。通常情况下，CE"感知"不到 VPN 的存在，也不需要支持 MPLS。
- **PE（Provider Edge）**：服务提供商网络的边缘设备，与 CE 直接相连。**在 MPLS 网络中，对 VPN 的所有处理都发生在 PE 上**，对 PE 性能要求较高。
- **P（Provider）**：服务提供商网络中的骨干设备，不与 CE 直接相连。P 设备只需要具备基本 MPLS 转发能力，**不维护 VPN 信息**。

PE 和 P 设备仅由 SP 管理；CE 设备仅由用户管理（除非用户把管理权委托给 SP）。一台 PE 设备可以接入多台 CE 设备；一台 CE 设备也可以连接属于相同或不同 SP 的多台 PE 设备。

基本 MPLS VPN 具有如下特点：
- 通过**扩展的 BGP 协议（MP-BGP）**传输路由报文
- 使用 **MPLS LSP** 为公网隧道对私网数据报文进行封装传输
- PE、P、CE 设备不兼容其它功能（没有一台设备既是 PE 又是 CE）

本特性是 **UDG（SGW-U/PGW-U/UPF）侧的三层标签交换 VPN 特性**，使 UDG 承担 PE 角色，通过 MP-BGP 发布 VPN-IPv4/VPN-IPv6 路由，通过 MPLS 标签交换转发 VPN 报文，实现用户不同地理区域的网络互通与私有网络数据在公网传输的安全性。

> 来源：`GWFD-020411 MPLS VPN_45030708.md`（"定义"章节，基本模型 CE/PE/P 三部分）[EV-FK-01]

### 1.2 适用 NF（UDG/UNC 网元）

| 涉及 NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| SGW-U / PGW-U / UPF | 用户面（UDG，作 PE） | **UDG 20.2.0 及后续版本** | UDG 作 PE 设备，承载 VPN 的所有处理：维护 VPN 实例（VRF）、MP-BGP 发布 VPN-IPv4 路由、MPLS 标签封装/解封装、VPN 报文转发 |
| SGW-C / PGW-C / SMF | 控制面（UNC，对应 WSFD-104411） | UNC 20.2.0 及后续版本（推定） | UNC 侧存在同名的 WSFD-104411 MPLS VPN 特性（子文档结构对称：基本概念/分标签/Hub&Spoke/跨域/IPv6 VPN/MCE/GR/NSR），C 面网元作 PE 承载控制面 VPN 通道 |

> 来源：`GWFD-020411 MPLS VPN_45030708.md`（"可获得性/版本支持"章节，UDG 20.2.0+，License 可选特性）；UNC 侧 WSFD-104411 文档清单见 `apn-feature-doc-list.md` Batch-33（9 文件对称分布）[EV-FK-01]

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|---------|---------|---------|
| 01 | **20.2.0** | 首次发布 |

> 来源：`GWFD-020411 MPLS VPN_45030708.md`（"发布历史"章节）[EV-FK-01]
> 说明：MPLS VPN 首次发布版本为 20.2.0，晚于 GRE（20.0.0）/ SA-Basic（20.0.0）等基础特性

### 1.4 License

**本特性需 License 许可**。产品文档明确声明"本特性是可选特性，只有获得了 License 许可后才能获得该特性的服务"。

> 来源：`GWFD-020411 MPLS VPN_45030708.md`（"可获得性/License 支持"章节）[EV-FK-01]
> 说明：具体 License 控制项编号在 9 篇文档中未列出，Stage 3 从 license 数据表补全（对比：GRE 无 License、L2TP 必须 License 82200BVC、SA-Basic License 82209749）

### 1.5 前置条件与依赖

| 前置条件 | 说明 |
|---------|------|
| License 加载 | 必须加载 MPLS VPN License 控制项（编号待补） |
| PE-CE 物理连接 | CE 与 PE 之间已建立物理/逻辑连接，接口可通信 |
| 骨干网 IGP 畅通 | PE-P-PE 之间的 IP 骨干网已通过 IGP（OSPF/IS-IS）建立路由可达性 |
| MPLS 基础使能 | 骨干网各节点已使能 MPLS，且 PE 间 LSP（Label Switched Path）已建立 |
| MP-BGP 邻居 | PE 间已建立 MP-BGP（MP-IBGP/MP-EBGP）对等体关系，用于交换 VPN-IPv4 路由 |
| PE-CE 路由协议 | PE 与 CE 之间已配置静态路由/OSPF/BGP 之一，用于交换 IPv4 或 IPv6 路由 |
| RD/VPN Target 规划 | 已为每个 VPN 实例规划唯一的 RD 和匹配的 Import/Export VPN Target |
| 标签资源规划 | 单 PE MPLS 标签规格 299008，建议 VPN 配置为每实例每标签、BGP 配置为每下一跳每标签以节约标签 |

> 来源：综合 `基本概念_92189817.md`（VPN 实例/RD/VPN Target）、`GWFD-020411 MPLS VPN_45030708.md`（特性规格/标签规格说明）、`MPLS VPN的分标签方式_92189833.md`（分标签建议）[EV-FK-02, EV-FK-01, EV-FK-04]

### 1.6 与其他特性的交互

**产品文档明确声明：本特性不涉及与其他特性的交互。**

> 来源：`GWFD-020411 MPLS VPN_45030708.md`（"与其他特性的交互"章节）[EV-FK-01]

> 说明：此声明指 MPLS VPN 作为独立特性不强制与其他特性联动配置，但实际部署中与 IGP（OSPF/IS-IS）、MPLS 基础（LDP/RSVP-TE）、BGP 基础特性存在隐性依赖（路由可达 + LSP 建立 + MP-BGP 邻居是 MPLS VPN 工作的前提）。

### 1.7 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | 无（产品文档明确写"运营商受益：无"） |
| 用户 | - 实现客户不同地理区域的网络互通<br>- 保障客户私有网络数据在公网传输过程中的安全性 |

> 来源：`GWFD-020411 MPLS VPN_45030708.md`（"受益"章节）[EV-FK-01]

### 1.8 应用场景

UDG 支持的 MPLS VPN 典型组网有以下几种：

- **Intranet**：VPN 中的所有用户形成闭合用户群，相互之间能够进行流量转发，VPN 中的用户不能与任何本 VPN 以外的用户通信（如 VPN1 的 Site1 只能与 Site4 通信，不能与 Site2、Site3 互通）
- **Extranet**：一个 VPN 用户可以访问其他 VPN 中的站点（如 Site1、Site2 都能访问 Site3，Site3 可访问 Site1 和 Site2，而 Site1 与 Site2 不能互通）
- **Hub&Spoke**：通过在 VPN 中设置中心访问控制设备，其它用户的互访都流经 Hub 站点，Spoke 站点之间不直接通信
- **跨域 VPN**：VPN 骨干网跨越多个 AS（自治系统）时部署，有 OptionA（VRF-to-VRF）和 OptionB（MP-EBGP 标签 VPN-IPv4）两种方式
- **Multi-VPN-Instance CE（MCE）**：在 CE 设备上提供逻辑独立的路由实例和地址空间，使多个用户共享一个 CE，以较低成本解决局域网的安全隔离
- **VPN 与 Internet 互联**：使 VPN 除了内部通信外，还可以访问 Internet

可靠性组网模型：
- 骨干层采用全连接、多级备份的 MPLS 网络；PE 较多时采用 BGP 路由反射器（RR）反射 VPNv4 路由
- 汇聚层网状或环状组网
- 接入层 CE 双（多）归属

UDG 支持的可靠性技术：
- **VPN FRR**：PE 之间转发不通时，VPN 流量切换到另一条 PE-PE 链路，实现端到端快速收敛
- **VPN GR**：承载 VPN 流量的 UDG（PE/P/CE）发生主备倒换时 VPN 流量不中断，**UDG 仅支持 GR Helper**
- **VPN NSR**：主备倒换后转发平面不中断且 VPN 路由发布不中断，邻居完全不感知

> 来源：`GWFD-020411 MPLS VPN_45030708.md`（"应用场景/可靠性技术"章节）[EV-FK-01]

### 1.9 对系统的影响

**本特性无应用限制**。产品文档明确声明"本特性无应用限制"。

> 来源：`GWFD-020411 MPLS VPN_45030708.md`（"应用限制"章节）[EV-FK-01]

> 说明：无应用限制指无硬性互斥约束，但 MPLS VPN 对 PE 设备性能要求较高（所有 VPN 处理发生在 PE 上），且标签资源有限（规格 299008），大规模部署需规划分标签方式。

### 1.10 特性规格

| 规格名称 | 规格指标 |
|---------|---------|
| MPLS 标签规格 | **299008** |

> **重要说明（标签节约约束）**：为了减少标签资源消耗，**必须**将本端 VPN 的标签方式配置为 **perInstance（每实例每标签）**，本端 BGP 的标签方式配置为 **perNexthop（每下一跳每标签）**。此配置仅能解决本端路由发布时的生成标签方式，无法解决对端发布路由的标签方式，**需要对端设备同步修改**（修改为每实例每标签或每下一跳每标签），防止对端发布路由消耗大量本端标签资源。

> 来源：`GWFD-020411 MPLS VPN_45030708.md`（"特性规格"章节 + 标签节约说明）[EV-FK-01]

### 1.11 计费与话单

产品文档 9 篇中未明确提及"计费与话单"章节。MPLS VPN 作为网络层隧道转发特性，**不直接涉及用户业务计费与话单生成**（区别于 PCC/URR 计费体系）。

> 来源：9 篇文档均无计费与话单章节 [EV-FK-01..09]

### 1.12 遵循标准

MPLS VPN 遵循大量 RFC 标准（60+），核心标准分类：

| 标准类别 | 关键 RFC |
|---------|---------|
| **BGP-4 基础** | RFC 4271（BGP-4）、RFC 1771（BGP-4 旧版）、RFC 1654/1655/1656 |
| **MP-BGP 多协议扩展** | RFC 4760、RFC 2858、RFC 2283（VPN-IPv4 地址族承载基础） |
| **MPLS 标签承载** | RFC 3107（BGP carry Label for MPLS） |
| **VPN-IPv4/VPN Target** | RFC 4360（BGP Extended Communities，即 VPN Target）、RFC 1997（Communities） |
| **BGP 路由反射** | RFC 4456、RFC 2796、RFC 1966（PE 较多时 RR 组网） |
| **4 字节 AS** | RFC 4893、RFC 5396（Textual Representation of AS Numbers） |
| **IPv6 VPN（6VPE）** | RFC 4798（6PE: Connecting IPv6 Islands over IPv4 MPLS） |
| **BGP GR（可靠性）** | RFC 4724（Graceful Restart for BGP）、RFC 4781（GR for BGP with MPLS） |
| **TCP MD5 安全** | RFC 2385（TCP MD5）、RFC 3562（Key Management for TCP MD5） |
| **CIDR** | RFC 4632、RFC 1519 |

> 来源：`GWFD-020411 MPLS VPN_45030708.md`（"遵循标准"章节，完整 60+ RFC 列表）[EV-FK-01]

---

## 2. 核心概念

### 2.1 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| MPLS | Multiprotocol Label Switch，多协议标签交换 | 无连接 IP 网络中增加面向连接的控制平面，集成 IP 路由灵活性与 ATM 标签交换简捷性 |
| L3VPN | Layer 3 Virtual Private Network | 三层虚拟专用网，MPLS VPN 属于 L3VPN |
| LSP | Label Switched Path，标签交换路径 | MPLS 隧道，公网标签转发通道 |
| CE | Customer Edge，用户网络边缘设备 | 直接与 SP 网络相连的用户设备，不感知 VPN，不需支持 MPLS |
| PE | Provider Edge，服务商边缘设备 | 与 CE 直接相连，**所有 VPN 处理发生在 PE 上**；UDG 作 PE |
| P | Provider，服务商骨干设备 | 不与 CE 相连，仅基本 MPLS 转发，不维护 VPN 信息 |
| Site | 站点 | 相互之间具备 IP 连通性的一组 IP 系统，且其连通性不需通过 SP 网络实现 |
| VPN 实例 / VRF | VPN Routing and Forwarding table，VPN 路由转发表 | PE 上每个 VPN 对应一张独立的路由转发表，与公网路由表及其它 VPN 实例相互隔离 |
| 公网实例 _public_ | - | 维护公网路由的默认实例 |
| RD | Route Distinguisher，路由标识符 | 8 字节，与 4 字节 IPv4 前缀组合成 12 字节 VPN-IPv4 地址，使不同 VPN 的重叠地址空间在全局唯一 |
| VPN-IPv4 地址 | - | 12 字节 = 8 字节 RD + 4 字节 IPv4 前缀，MP-BGP 承载的私网路由地址族 |
| VPN Target / RT | Route Target，路由目标属性 | 32 位 BGP 扩展团体属性，控制 VPN 路由发布与接收；分 ERT（Export）和 IRT（Import） |
| ERT | Export Target | 本地 PE 从直连 site 学到 IPv4 路由转 VPN-IPv4 时设置的 Target，随 BGP 发布 |
| IRT | Import Target | PE 收到对端 VPN-IPv4 路由时检查其 ERT，匹配本端 VPN 实例 IRT 才注入该实例路由表 |
| MP-BGP | Multiprotocol Extensions for BGP-4 | BGP-4 多协议扩展，支持 VPN-IPv4/IPv6 等多地址族 |
| 内层标签 I-L | Inner Label | VPN 报文在公网传输的内层 MPLS 标签，表示报文出接口或所属 VPN |
| 外层标签 O-L | Outer Label | 公网 MPLS 标签，指示如何到达 BGP 下一跳，P 设备逐跳交换 |
| 倒数第二跳弹出 | PHP | 最后的外层标签在到达 Egress PE 前一跳弹出，Egress PE 仅收到内层标签报文 |
| MCE | Multi-VPN-Instance CE，多实例 CE | CE 设备上提供多个逻辑独立的路由实例，多个用户共享一台 CE，业务隔离 |
| VPN FRR | VPN Fast Reroute | PE 间转发不通时 VPN 流量快速切换到另一条 PE-PE 链路 |
| VPN GR | VPN Graceful Restart | 主备倒换时 VPN 流量不中断；**UDG 仅支持 GR Helper** |
| VPN NSR | VPN Non-Stop Routing | 控制平面故障时转发+控制平面均不中断，邻居不感知，需双主控硬件 |
| ASBR | AS Boundary Router，自治系统边界路由器 | 跨域 VPN 中连接不同 AS 的设备 |
| RR | Route Reflector，路由反射器 | 减少 MP-IBGP 全连接数，反射 VPNv4 路由 |
| 6VPE | IPv6 VPN over IPv4 backbone | 用 IPv4 骨干网承载 IPv6 VPN 业务（当前仅支持 6VPE 方案） |

> 来源：`基本概念_92189817.md`（site/VRF/RD/VPN-IPv4/VPN Target/MP-BGP/路由发布/报文转发）、`MPLS VPN的分标签方式_92189833.md`（分标签方式）、`Hub&Spoke_92069589.md`（Hub/Spoke）、`跨域VPN_45030728.md`（ASBR/OptionA/B）、`Multi-VPN-Instance CE_45189888.md`（MCE）、`VPN GR_92069593.md`（GR Restarter/Helper/Session/Time）、`VPN NSR_45189892.md`（NSR/NSF/HA）、`BGP_MPLS IPv6 VPN_45030732.md`（6VPE）[EV-FK-02..09]

### 2.2 对象模型

MPLS VPN 的配置架构基于"VPN 实例 + 标签 + 路由属性"的三层抽象，核心对象如下：

```
┌──────────────────────────────────────────────────────────────────────┐
│ UDG（PE）侧 MPLS VPN 配置对象体系                                       │
│                                                                      │
│   ┌──────────────┐                                                   │
│   │ 接口（PE-CE）│ ← 绑定到 VPN 实例                                  │
│   └──────┬───────┘                                                   │
│          │ 关联                                                      │
│          ▼                                                           │
│   ┌──────────────────────────────────────────────┐                   │
│   │ VPN 实例（VRF）★MPLS VPN 核心对象              │                   │
│   │  - VPN-Instance Name (如 vpn1)                │                   │
│   │  - RD（8字节，全局唯一）                       │                   │
│   │  - VPN Target ERT / IRT（32位扩展团体属性）    │                   │
│   │  - 地址族：IPv4 / IPv6（6VPE）                 │                   │
│   │  - 分标签方式：每实例每标签（perInstance）     │                   │
│   └──────┬───────────────────────────────────────┘                   │
│          │                                                           │
│          ├─→ 存入 VPN 路由表（与公网路由表隔离）                       │
│          │                                                           │
│          │ MP-BGP 发布                                               │
│          ▼                                                           │
│   ┌──────────────────────────────────────────────┐                   │
│   │ VPN-IPv4 路由（12字节 = RD + IPv4前缀）        │                   │
│   │   携带：ERT + 内层标签（I-L）                  │                   │
│   └──────┬───────────────────────────────────────┘                   │
│          │ MP-BGP Update（PE↔PE，通过 RR 或直连）                     │
│          ▼                                                           │
│   ┌──────────────────────────────────────────────┐                   │
│   │ 对端 PE 接收：检查 ERT 匹配本地 IRT           │                   │
│   │   匹配 → 注入对应 VPN 实例路由表              │                   │
│   │   保留：MPLS 标签值 + 迭代成功的 Tunnel ID    │                   │
│   └──────────────────────────────────────────────┘                   │
│                                                                      │
│   报文转发栈（两层标签）：                                             │
│   ┌─────────┬───────────┬──────────────────┬──────────────┐         │
│   │外层O-L  │ 内层 I-L  │  IP 头（私网）    │  Payload     │         │
│   │(到BGP   │(出接口/  │                  │              │         │
│   │ 下一跳) │ 所属VPN) │                  │              │         │
│   └─────────┴───────────┴──────────────────┴──────────────┘         │
│                                                                      │
│   可选子特性：                                                        │
│   ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐       │
│   │Hub&Spoke   │ │ 跨域VPN    │ │ MCE        │ │ IPv6 VPN   │       │
│   │(Hub/Spoke  │ │(OptionA/B) │ │(多实例CE)  │ │(6VPE)      │       │
│   │ 双RT控制)  │ │ ASBR       │ │            │ │            │       │
│   └────────────┘ └────────────┘ └────────────┘ └────────────┘       │
│                                                                      │
│   可靠性：                                                            │
│   ┌────────────┐ ┌────────────┐ ┌────────────┐                      │
│   │VPN FRR     │ │VPN GR      │ │VPN NSR     │                      │
│   │(PE间切换)  │ │(Helper only)│ │(双主控)    │                      │
│   └────────────┘ └────────────┘ └────────────┘                      │
└──────────────────────────────────────────────────────────────────────┘
```

核心对象说明：

| 对象 | 作用 | MPLS VPN 角色 |
|------|------|--------------|
| **VPN 实例（VRF）** | 独立的私网路由转发表，与公网及其它 VPN 隔离 | **★核心对象**，每个 VPN 一张表，关联 RD/VPN Target/接口 |
| **RD** | 路由标识符，使重叠地址空间全局唯一 | 8 字节附加到 IPv4 前缀形成 VPN-IPv4 地址 |
| **VPN Target（ERT/IRT）** | 控制 VPN 路由发布与接收 | 实现 Intranet/Extranet/Hub&Spoke 等多种组网 |
| **VPN-IPv4 地址** | 12 字节 = RD + IPv4 前缀 | MP-BGP 承载的私网路由地址族 |
| **内层标签 I-L** | 标识出接口/所属 VPN | Egress PE 据此找到对应 CE 出接口 |
| **外层标签 O-L** | 公网标签，到 BGP 下一跳 | P 设备逐跳交换，PHP 时倒数第二跳弹出 |
| **MP-BGP 对等体** | PE 间交换 VPN-IPv4 路由 | 可经 RR 反射减少连接数 |
| **PE-CE 接口** | 绑定到 VPN 实例 | 实现 PE-CE 路由隔离交换 |
| **MCE** | 多实例 CE | 共享 CE，业务隔离 |
| **ASBR** | 跨域 VPN 边界 | OptionA 作对端 CE，OptionB 作 MP-EBGP 标签交换 |

> 来源：`基本概念_92189817.md`（图3 VPN 实例示意图 + RD/VPN-IPv4 + VPN Target + 路由发布 + 报文转发两层标签）、`GWFD-020411 MPLS VPN_45030708.md`（特性定义 CE/PE/P + 可靠性）[EV-FK-02, EV-FK-01]

### 2.3 在接入方式场景的角色

GWFD-020411 在 APN 接入方式场景中扮演**"三层标签交换 VPN"**的角色，与 GRE（三层 IP 封装）、IPSec（三层加密）、L2TP（二层 PPP）共同构成隧道方案矩阵：

1. **L3VPN 完整方案**：MPLS VPN 是唯一一个完整的"三层 VPN"方案——不仅封装报文，还维护 VPN 路由（VRF）、控制路由发布（VPN Target）、提供地址重叠隔离（RD）
2. **标签交换转发**：通过两层 MPLS 标签（外层公网 + 内层 VPN）转发，P 设备仅交换外层标签不感知 VPN，转发效率高
3. **公网安全传输**：私网数据通过 MPLS LSP 隧道穿越 IP 骨干网，P 设备不维护 VPN 信息，保障私有网络数据安全
4. **多组网模型**：支持 Intranet/Extranet/Hub&Spoke/跨域/MCE 等多种组网，适配企业 VPN 各种场景
5. **UDG 作 PE**：在 UDG 部署中，UDG 承担 PE 角色，对 VPN 的所有处理（VRF 维护、MP-BGP、标签处理）都在 UDG 上发生
6. **高可靠性**：VPN FRR + VPN GR（Helper）+ VPN NSR 提供端到端可靠性保障

> 来源：`GWFD-020411 MPLS VPN_45030708.md`（"定义/应用场景/实现原理"章节）[EV-FK-01]

---

## 3. 原理与流程

### 3.1 实现原理（BGP 发布路由 + MPLS 转发报文）

MPLS VPN 使用 **BGP（Border Gateway Protocol）** 在服务提供商骨干网上发布 VPN 路由，使用 **MPLS（Multiprotocol Label Switch）** 在骨干网上转发 VPN 报文。骨干网是 IP 网络。

**为什么选 BGP 发布路由**：
- BGP 着眼点不在于发现/计算路由，而在于**控制路由传播和选择最佳路由**
- VPN 利用公共网络传递 VPN 数据，公共网络通常已用 IGP 发现路由，**构建 VPN 的关键在于控制 VPN 路由的传播**
- BGP 基于 TCP（端口 179），可靠性高，适合跨 UDG 的两个 PE 间交换 VPN 路由
- BGP 可承载附加在路由后的任何信息（可选 BGP 属性），为 PE 间传播 VPN 路由提供便利
- BGP 路由更新只发送增量，减少带宽占用，适合公共网络上传播大量 VPN 路由
- BGP 是外部网关协议（EGP），实现跨运营商 VPN 更容易

**为什么选 MPLS 转发**：
- MPLS 无缝集成 IP 路由灵活性与 ATM 标签交换简捷性
- MPLS 在无连接 IP 网络中增加面向连接的控制平面，增添管理和运营手段
- MPLS 流量工程是管理网络流量、减少拥塞、保证 QoS 的重要工具

> 来源：`GWFD-020411 MPLS VPN_45030708.md`（"实现原理"章节）[EV-FK-01]

### 3.2 MPLS VPN 路由发布过程（三段式）

基本 MPLS VPN 组网中，VPN 路由信息发布涉及 CE 和 PE，**P 设备只维护骨干网路由，不需要了解任何 VPN 路由信息**；**PE 设备只维护自身接入的 VPN 路由，不维护所有 VPN 路由**。路由发布分三段：

```
┌─────────────────────────────────────────────────────────────────┐
│ 第1段：本地 CE → 入口 PE                                         │
│                                                                 │
│   1. CE 与直连 PE 建立邻居/对等体关系（静态路由/OSPF/BGP）       │
│   2. CE 把本站点 IPv4 路由发布给 PE                             │
│   3. PE 通过绑定的 VPN 实例区分路由注入哪个 VRF                  │
│      （手工配置 VPN 实例与 PE-CE 接口的绑定关系）                │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 第2段：入口 PE → 出口 PE（MP-BGP 核心）                          │
│                                                                 │
│   1. PE 从 CE 学到 VPN 路由 → 存入 VPN 实例                     │
│   2. 为标准 IPv4 路由增加 RD → 形成 VPN-IPv4 路由               │
│   3. 入口 PE 通过 MP-BGP 发布 VPN-IPv4 路由                     │
│      Update 报文携带：VPN-Target（ERT）属性 + MPLS 内层标签     │
│   4. 出口 PE 收到 VPN-IPv4 路由后：                              │
│      a. 检查下一跳可达                                          │
│      b. 通过 BGP peer 入口策略                                  │
│      c. 私网路由交叉（通过 VRF 入口策略）                        │
│      d. 隧道迭代（找 Tunnel ID）                                 │
│      e. 路由优选                                                │
│      f. 根据 ERT 与本地 IRT 匹配 → 注入对应 VPN 实例路由表      │
│   5. 出口 PE 保留：MP-BGP Update 中的 MPLS 标签值 + 迭代的 Tunnel ID │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 第3段：出口 PE → 远端 CE                                         │
│                                                                 │
│   1. 远端 CE 通过静态路由/OSPF/BGP 从出口 PE 学习 VPN 路由      │
│   2. 出口 PE 发布给远端 CE 的是普通 IPv4 路由（剥离 RD/标签）   │
│   3. 本地 CE 与远端 CE 建立可达路由                              │
└─────────────────────────────────────────────────────────────────┘
```

**本地路由交叉**：PE 对来自本地 CE 的属于不同 VPN 的路由，若下一跳直接可达或可迭代成功，也会与本地其它 VPN 实例的 IRT 匹配，该过程通过 VRF 入口策略过滤并修改属性。

> 来源：`基本概念_92189817.md`（"MPLS VPN 路由发布过程"章节，三段式完整流程）[EV-FK-02]

### 3.3 MPLS VPN 报文转发过程（两层标签）

以 CE1 发送报文给 CE2 为例（I-L = 内层标签，O-L = 外层标签）：

```
┌─────────────────────────────────────────────────────────────────┐
│ 报文转发流程（CE1 → CE2）                                        │
│                                                                 │
│ 1. CE1 向 Ingress PE 发送一个 VPN 报文（纯 IP）                  │
│                                                                 │
│ 2. Ingress PE 从绑定了 VPN 实例的接口收到报文：                  │
│    a. 根据绑定的 VPN 实例 RD 查找对应 VPN 转发表                 │
│    b. 匹配目的 IPv4 前缀，查找对应的 Tunnel-ID                   │
│    c. 报文打上对应的内层标签（I-L）                              │
│    d. 根据 Tunnel-ID 找到隧道（LSP）                             │
│    e. 打上公网外层 MPLS 标签头（O-L1）                           │
│    f. 从隧道发送出去                                             │
│                                                                 │
│ 3. 报文携带两层标签穿越骨干网：                                   │
│    ┌─────────┬───────────┬──────────────┬──────────┐            │
│    │ O-L1    │ I-L       │  IP（私网）   │ Payload  │            │
│    │(外层)   │(内层)     │              │          │            │
│    └─────────┴───────────┴──────────────┴──────────┘            │
│    骨干网每台 P 设备对该报文进行外层标签交换（O-L1→O-L2→...）    │
│                                                                 │
│ 4. Egress PE 收到携带两层标签的报文，交 MPLS 协议处理：           │
│    a. 去掉外层标签                                              │
│       ★若应用 PHP（倒数第二跳弹出），则外层标签在到达 Egress    │
│         PE 前一跳弹出，Egress PE 只收到带内层标签的报文           │
│    b. 剥离处于栈底的内层标签                                     │
│    c. 从对应出接口发送给 CE2                                     │
│       此时报文为纯 IP 报文                                       │
│                                                                 │
│ 5. CE2 按普通 IP 转发将报文传送到目的地                          │
└─────────────────────────────────────────────────────────────────┘
```

**外层标签作用**：指示如何到达 BGP 下一跳（P 设备逐跳交换）
**内层标签作用**：表示报文的出接口或者属于哪个 VPN（Egress PE 据此转发）

> 来源：`基本概念_92189817.md`（"MPLS VPN 的报文转发过程"章节 + 图5 VPN 报文转发过程）[EV-FK-02]

### 3.4 分标签方式（标签节约机制）

为节省 MPLS 标签资源（规格 299008），支持三种标签分配方式：

| 方式 | 定义 | 适用组网 | 配置位置 |
|------|------|---------|---------|
| 每路由每标签（缺省） | 每条路由分配一个 MPLS 标签 | 默认方式，但标签消耗大 | - |
| **每实例每标签（perInstance）** | 来自同一 VPN 实例的所有路由分配同一标签 | 适用于所有 MPLS VPN 组网 | 配置 VPN 实例的设备 |
| **每下一跳每标签（perNexthop）** | 下一跳和私网标签相同的所有路由分配同一标签 | 主要应用于跨域 VPN-OptionB | ASBR 设备 |

**每实例每标签效果**：PE1 配置两个 VPN 实例，分别从两个 site 各收到 1 万条路由。缺省方式占用 2 万个标签；配置每实例每标签后，**仅占用 2 个标签**。

**每下一跳每标签效果**：跨域 OptionB 场景，ASBR1 向 ASBR2 发布来自 PE1 的 2 万条路由，未使能时需消耗 2 万标签；使能后对于下一跳和出标签相同的路由只分配 1 个标签，**2 万条路由仅需 2 个标签**。

> **切换约束**：每路由每标签和按下一跳分标签可灵活切换，但切换过程中本地和 ASBR 需更新标签转发表，**会造成业务短暂丢包**。
>
> **OptionB 配置约束**：跨域 VPN-OptionB 场景中，ASBR 上配置每下一跳每标签的同时，**必须在 PE 上配置每实例每标签**。

> 来源：`MPLS VPN的分标签方式_92189833.md`（产生原因/实现过程/使用价值完整说明）[EV-FK-04]

### 3.5 VPN Target 控制机制（多种组网的基础）

VPN Target（32 位 BGP 扩展团体属性）控制 VPN 路由的发布与接收：

- **ERT（Export Target）**：本地 PE 从直连 site 学到 IPv4 路由转 VPN-IPv4 时设置，随 BGP 发布
- **IRT（Import Target）**：PE 收到 VPN-IPv4 路由时检查其 ERT，匹配本端 VPN 实例 IRT 才注入

**为什么用 VPN Target 而不用 RD 作为扩展团体属性**：
- 一条 VPN-IPv4 路由只能有一个 RD，但可关联多个 VPN Target
- VPN Target 用于控制同一 PE 上不同 VPN 间的路由发布（同 PE 不同 VPN 可设匹配 VPN Target 实现互引）
- BGP 携带扩展团体属性有限，用 RD 会影响网络扩展

VPN Target 可设置多个值，实现多种组网（Intranet 同 RT 互通、Extranet 部分交叉 RT、Hub&Spoke 双 RT 控制）。

> 来源：`基本概念_92189817.md`（"VPN Target"章节）[EV-FK-02]

### 3.6 Hub&Spoke 组网原理

Hub&Spoke 通过设置两个 VPN Target（一个"Hub"、一个"Spoke"）实现 Spoke 站点间通信流经 Hub：

| 设备角色 | Export Target | Import Target |
|---------|--------------|--------------|
| Spoke-PE（连接 Spoke 站点） | "Spoke" | "Hub" |
| Hub-PE（连接 Hub 站点，需两个接口/子接口） | 接收接口：- / 发布接口："Hub" | 接收接口："Spoke" / 发布接口：- |

**路由发布路径**（Site2 → Site1 为例）：Spoke-PE2 → Hub-PE（IRT=Spoke 接收）→ Hub-CE → Hub-PE（发布 ERT=Hub）→ Spoke-PE1（IRT=Hub 接收）→ Site1

**关键约束**：任意 Spoke-PE 的 IRT 不与其它 Spoke-PE 的 ERT 相同，因此 Spoke 间不直接发布 VPN-IPv4 路由。

**EBGP AS-Loop 约束**：若 Hub-PE 与 Hub-CE 使用 EBGP，Hub-PE 发现来自 Spoke-CE 的路由已包含自己的 AS 号会丢弃，**必须在 Hub-PE 手工配置允许本地 AS 编号重复**。

> 来源：`Hub&Spoke_92069589.md`（组网应用 + 3 种 PE-CE 协议方案）[EV-FK-05]

### 3.7 跨域 VPN 原理（OptionA vs OptionB）

| 方式 | 又称 | ASBR 间机制 | 特点 |
|------|------|------------|------|
| **OptionA** | VRF-to-VRF | ASBR 间不运行 MPLS，ASBR 把对端 ASBR 看作自己的 CE，用静态路由/IGP 多实例/EBGP 交换 IPv4 路由 | **优点**：配置简单；**缺点**：可扩展性差，ASBR 需为每个 VPN 创建实例并使用不同接口，跨多 AS 时配置量大 |
| **OptionB** | EBGP redistribution of labeled VPN-IPv4 routes | ASBR 间通过 MP-EBGP 发布标签 VPN-IPv4 路由 | **优点**：不受 ASBR 互连链路数目限制；**缺点**：VPN 路由全经 ASBR 保存扩散，ASBR 负担重 |

OptionB 两种 ASBR 处理方法：
1. ASBR 对标签 VPN-IPv4 路由特殊处理，全部保存（不检查 VPN Target 过滤）—— 流量可控性好但 ASBR 负担重
2. 用 BGP 路由策略（如 RT 过滤）控制 VPN-IPv4 路由收发

> 来源：`跨域VPN_45030728.md`（OptionA/OptionB/比较完整说明）[EV-FK-06]

### 3.8 IPv6 VPN（6VPE）原理

BGP/MPLS IPv6 VPN 扩展使得 VPN 骨干网**不必升级到 IPv6** 就能给客户提供 IPv6 VPN 服务。

- **当前仅支持 6VPE 方案**（IPv6 VPN 业务由 IPv4 骨干网承载）
- PE 与 CE 间运行 IPv6 路由协议：BGP4+ / 静态 IPv6 路由 / OSPFv3
- PE 间用 IPv4 地址建立 VPNv6 邻居，传递 VPN-IPv6 路由
- VPN-IPv6 路由选择骨干网 IPv4 隧道承载 IPv6 VPN 业务
- 除 PE-CE 路由协议外，其它特性原理与 IPv4 VPN 相同

> 来源：`BGP_MPLS IPv6 VPN_45030732.md`（6VPE 方案说明）[EV-FK-07]

### 3.9 与 GRE/IPSec/L2TP 的隧道对比（★重点）

| 维度 | GWFD-020411 MPLS VPN | IPFD-015002 GRE | IPFD-015004/016000 IPSec | GWFD-020412/WSFD-104410 L2TP |
|------|---------------------|----------------|--------------------------|------------------------------|
| **隧道层级** | 三层（标签交换 VPN） | 三层（IP 封装） | 三层（IP 加密） | 二层（PPP 封装） |
| **核心机制** | **BGP 发布 VPN 路由 + MPLS 标签转发** | GRE 头 + 外层 IP 头封装 | AH/ESP 加密 + IKE 协商 | L2TP 封装 PPP 帧 |
| **VPN 路由维护** | **有（VRF + MP-BGP + RD/RT）** | 无（仅点对点隧道） | 无（仅点对点加密） | 无（仅 PPP 链路） |
| **地址重叠隔离** | **有（RD 12字节 VPN-IPv4）** | 无 | 无 | 无 |
| **路由发布控制** | **有（VPN Target ERT/IRT）** | 无 | 无 | 无 |
| **加密** | 不加密 | 不加密 | **加密 + 认证** | 不加密 |
| **鉴权** | 无（依赖 BGP/IGP 邻居） | 无（可选 GRE Key） | 有（IKE/证书） | 有（PPP 的 PAP/CHAP） |
| **封装开销** | 两层 MPLS 标签（4 字节×2） | GRE 头 + 外层 IP 头 | ESP/AH 头 + 加密运算 | L2TP 头 + PPP 头 |
| **转发效率** | **高**（P 设备仅交换外层标签，硬件转发） | 中 | 低（加密运算） | 中 |
| **对 PE 性能要求** | **高**（所有 VPN 处理在 PE） | 低 | 中 | 中 |
| **P 设备感知 VPN** | **否**（仅外层标签交换） | 不涉及（无 P 概念） | 不涉及 | 不涉及 |
| **组网灵活性** | **极高**（Intranet/Extranet/Hub&Spoke/跨域/MCE） | 低（点对点） | 中（点对点 + 主备） | 低（远程接入） |
| **跨域支持** | **原生**（OptionA/OptionB） | 需手工对接 | 需手工对接 | 不涉及 |
| **IPv6 支持** | **6VPE**（IPv4 骨干承 IPv6 VPN） | IPv6 隧道参数 | IPv6 IPSec 隧道 | L2TP IPv6 扩展 |
| **可靠性** | **VPN FRR + GR(Helper) + NSR** | Keepalive（5s/3 次） | IKE DPD | Hello 60s/3 次 |
| **License** | **需 License** | 无 | 需 License | UDG 必须（82200BVC） |
| **典型用途** | 运营商级多层 VPN、企业多 site 互通、跨域 VPN | 异种网络互通、轻量 VPN | 安全加密隧道、GRE over IPSec | 企业远程接入、LNS 地址分配 |
| **C-U 模式** | C-U 对称同构（两侧均有同名特性） | C-U 对称同构 | C-U 各自配置 | C-U 分工 |
| **典型 NF 角色** | **PE**（UDG/UNC） | PE 设备 | IPSec 端点 | UDG 作 LAC，LNS 在企业网 |
| **首次发布版本** | **20.2.0** | 20.0.0 | 20.0.0（推定） | 20.0.0（推定） |
| **标准** | RFC 4271/4760/3107/4360/4798 等 60+ | RFC 1701/1702/2784 | RFC AH/ESP/IKE 系列 | RFC 2661/2868/5072/5571/8064 |

> 来源：综合本特性 9 篇文档 + 同域 GRE 知识文档（IPFD-015002-GRE.md §3.6 隧道对比表）+ L2TP 特性描述 [EV-FK-01..09]

### 3.10 协议交互

| 接口/协议 | 交互网元 | 消息类型 | 说明 |
|----------|---------|---------|------|
| PE-CE 路由协议 | CE ↔ PE | 静态路由 / OSPF / BGP | 交换标准 IPv4（或 IPv6）路由，PE 通过 VRF 区分 |
| MP-BGP（MP-IBGP） | PE ↔ PE（同 AS） | VPN-IPv4/VPN-IPv6 Update | 携带 RD、ERT、MPLS 内层标签；可经 RR 反射 |
| MP-BGP（MP-EBGP） | ASBR ↔ ASBR（跨域 OptionB） | 标签 VPN-IPv4 Update | 跨 AS 交换标签 VPN 路由 |
| EBGP（OptionA） | ASBR ↔ ASBR（跨域 OptionA） | IPv4 路由 | ASBR 互视为 CE，普通 IPv4 交换 |
| IGP（OSPF/IS-IS） | PE ↔ P ↔ PE | 公网路由 | 骨干网路由可达，LSP 建立基础 |
| LDP / RSVP-TE | PE ↔ P ↔ PE | 标签分发 | 建立 MPLS LSP（外层标签隧道） |
| BGP GR | PE ↔ 邻居 | Open（GR capability）+ End-of-Rib | VPN GR 倒换时保持转发不中断 |

> 来源：`基本概念_92189817.md`（路由发布三段式）、`跨域VPN_45030728.md`（OptionA/B）、`VPN GR_92069593.md`（BGP GR 协商）[EV-FK-02, EV-FK-06, EV-FK-08]

---

## 4. 配置规则

### 4.1 激活步骤

> **重要说明**：本特性 9 篇产品文档**均为"基本概念/原理/组网应用"类说明文档，未包含"激活/配置/调测"操作文档**（与 GRE 的 8 篇含完整激活+调测文档形成对比）。MPLS VPN 配置在 UDG 上通过通用 MPLS/BGP/VPN 实例命令体系完成，以下步骤为基于原理的配置框架（具体 MML 命令需从 UDG 通用 MPLS 命令参考补全，Stage 3 横向分析时从命令字典提取）。

```
步骤1：确认前置条件
  ├── License 已加载（MPLS VPN 可选特性 License）
  ├── PE-CE 物理连接已建立
  ├── 骨干网 IGP（OSPF/IS-IS）畅通，PE-P-PE 路由可达
  └── MPLS 基础使能，PE 间 LSP 已建立（LDP/RSVP-TE）

步骤2：配置 VPN 实例（★核心使能）
  ├── 创建 VPN 实例（VRF）
  ├── 配置 RD（8 字节，全局唯一）
  ├── 配置 VPN Target（ERT 用于发布，IRT 用于接收）
  └── （可选）配置每实例每标签（perInstance）节约标签

步骤3：绑定接口到 VPN 实例
  └── 将 PE-CE 接口绑定到对应 VPN 实例

步骤4：配置 PE-CE 路由协议
  ├── （方案A）静态路由
  ├── （方案B）OSPF 多实例
  └── （方案C）BGP（PE-CE EBGP）

步骤5：配置 MP-BGP（PE 间 VPN 路由交换）
  ├── 建立 MP-IBGP/MP-EBGP 对等体
  ├── 使能 VPNv4/VPNv6 地址族
  ├── （大规模）配置 RR 反射 VPNv4 路由
  └── （节约标签）配置 BGP 每下一跳每标签（perNexthop）

步骤6：（可选）配置组网模型
  ├── Intranet：同 VPN 实例同 RT
  ├── Extranet：交叉 RT
  ├── Hub&Spoke：双 RT（Hub/Spoke）+ Hub-PE 双接口
  └── MCE：CE 侧多 VPN 实例

步骤7：（可选）配置跨域
  ├── OptionA：ASBR 互视为 CE，IPv4 交换
  └── OptionB：ASBR 间 MP-EBGP 标签 VPN-IPv4 + 每下一跳每标签

步骤8：（可选）配置 IPv6 VPN（6VPE）
  ├── PE-CE 配置 IPv6 路由协议（BGP4+/OSPFv3/静态 IPv6）
  └── MP-BGP 使能 VPNv6 地址族，IPv4 隧道承载

步骤9：（可选）配置可靠性
  ├── VPN FRR
  ├── VPN GR（Helper）
  └── VPN NSR（需双主控硬件）
```

> 来源：综合 9 篇文档的原理与组网说明推导的配置框架；`MPLS VPN的分标签方式_92189833.md`（分标签配置位置）、`跨域VPN_45030728.md`（跨域配置）、`Hub&Spoke_92069589.md`（RT 设置规则）[EV-FK-01..09]
> **文档覆盖度说明**：9 篇文档无激活/调测 MML 脚本，具体命令（如 ADD VPNINSTANCE/MOD VPNINSTANCE/ADD BGPVPNV4ROUTETARGET 等）需 Stage 3 从 UDG 命令字典补全

### 4.2 MML 命令清单

> **文档依据说明**：9 篇产品文档**未直接列出 MPLS VPN 专属 MML 命令清单**（区别于 SA-Basic 特性参考信息文档列出 17 条命令、GRE 激活文档列出 6 条核心命令）。以下命令为基于文档原理推导的通用 MPLS/VPN/BGP 命令族，具体命令名与参数需 Stage 3 从 UDG 命令字典验证。

#### 4.2.1 VPN 实例与接口相关（推导）

| 命令（推导） | 用途 | 文档依据 |
|------|------|---------|
| VPN 实例创建/修改 | 创建 VRF，配置 RD/VPN Target | 基本概念"VPN 实例"章节：PE 上每个 VPN 一张转发表 |
| 接口绑定 VPN 实例 | 将 PE-CE 接口关联到 VPN 实例 | 基本概念"将 VPN 实例和 PE 上与 CE 直接相连的接口关联（或称为绑定），这需要手工设置" |
| 每实例每标签配置 | 配置 perInstance 分标签 | 分标签方式"在 VPN 实例相应地址族下配置每实例每标签功能" |

#### 4.2.2 BGP/MP-BGP 相关（推导）

| 命令（推导） | 用途 | 文档依据 |
|------|------|---------|
| MP-BGP 对等体建立 | PE 间 VPNv4/VPNv6 邻居 | 路由发布"入口 PE 通过 MP-BGP 发布 VPN-IPv4 路由" |
| VPNv4/VPNv6 地址族使能 | 承载 VPN 路由 | 基本概念"MP-BGP 采用地址族区分不同网络层协议" |
| BGP 每下一跳每标签 | 配置 perNexthop | 分标签方式"在 ASBR 上使能按下一跳分标签" |
| RR 路由反射器配置 | 减少 MP-IBGP 连接数 | 应用场景"采用 BGP 路由反射器组网，反射 VPNv4 路由" |
| 允许 AS 编号重复（Hub&Spoke） | Hub-PE EBGP AS-Loop | Hub&Spoke"Hub-PE 上必须手工配置允许本地 AS 编号重复" |

#### 4.2.3 调测查询命令（推导）

| 命令（推导） | 用途 | 文档依据 |
|------|------|---------|
| 查询 VPN 实例 | 查看 VRF 配置 | 基本概念 VPN 实例章节 |
| 查询 VPN 路由表 | 查看 VPN 路由 | 路由发布"加入到 VPN 实例的路由表" |
| 查询 MPLS 标签 | 查看标签分配 | 分标签方式 + 特性规格 299008 |
| 查询 LSP 隧道 | 查看公网隧道 | 报文转发"根据 Tunnel-ID 找到隧道" |

> 来源：9 篇文档均无显式 MML 命令清单，命令名为推导；具体命令需 Stage 3 从 UDG 命令字典（如 `LST VPNINSTANCE`/`LST BGPVPNV4PEER` 等）补全 [EV-FK-01..09]

### 4.3 关键参数说明

#### 4.3.1 VPN 实例关键参数

| 参数 | 取值/格式 | 说明 |
|------|----------|------|
| VPN 实例名 | 字符串（如 "vpn1"） | VPN 实例标识 |
| RD | 8 字节（格式如 `100:1`、`1.2.3.4:1`） | 路由标识符，与 4 字节 IPv4 前缀组合成 12 字节 VPN-IPv4 地址；必须全局唯一 |
| ERT（Export Target） | 32 位扩展团体属性（如 `100:1`） | 本地路由发布时携带，对端 PE 据此判断接收 |
| IRT（Import Target） | 32 位扩展团体属性 | PE 接收路由时与对端 ERT 匹配，匹配才注入 VPN 实例 |
| 接口绑定 | PE-CE 接口名 | 手工将 VPN 实例与 PE-CE 接口关联 |
| 地址族 | IPv4 / IPv6 | IPv6 场景为 6VPE |
| 分标签方式 | perInstance（每实例每标签） | 节约标签资源（推荐） |

> 来源：`基本概念_92189817.md`（VPN 实例/RD/VPN-IPv4/VPN Target 章节）[EV-FK-02]

#### 4.3.2 BGP/分标签关键参数

| 参数 | 取值 | 说明 |
|------|------|------|
| 分标签方式（VPN 实例侧） | perInstance | 同一 VPN 实例所有路由共用一个标签 |
| 分标签方式（BGP 侧） | perNexthop | 下一跳和私网标签相同的路由共用一个标签 |
| AS 编号重复允许 | enable（Hub&Spoke EBGP 场景） | Hub-PE 允许本地 AS 编号重复出现 |
| GR capability | enable（GR Helper） | UDG 仅支持 GR Helper |
| NSR | enable（需双主控） | 主备实时同步私网路由/属性/标签/下一跳 |

> 来源：`MPLS VPN的分标签方式_92189833.md`、`Hub&Spoke_92069589.md`、`VPN GR_92069593.md`、`VPN NSR_45189892.md` [EV-FK-04, EV-FK-05, EV-FK-08, EV-FK-09]

### 4.4 约束条件

| 约束类型 | 约束内容 | 来源 |
|---------|---------|------|
| **标签节约约束（★关键）** | 必须配置 VPN 每实例每标签 + BGP 每下一跳每标签；本端配置无法解决对端，**需对端同步修改** | 特性规格说明章节 |
| **分标签切换丢包** | 每路由每标签与按下一跳分标签切换过程中，本地和 ASBR 更新标签转发表**会造成业务短暂丢包** | 分标签方式说明 |
| **OptionB 标签配套** | 跨域 OptionB 场景，ASBR 配置每下一跳每标签时，**必须在 PE 上配置每实例每标签** | 分标签方式说明 |
| **Hub&Spoke EBGP AS-Loop** | Hub-PE 与 Hub-CE 用 EBGP 时，**必须手工配置允许本地 AS 编号重复**，否则 Hub-PE 丢弃含自身 AS 号的路由 | Hub&Spoke 组网应用 |
| **Hub&Spoke RT 约束** | 任意 Spoke-PE 的 IRT 不与其它 Spoke-PE 的 ERT 相同（保证 Spoke 间不直通） | Hub&Spoke RT 设置规则 |
| **VPN GR 仅 Helper** | **UDG 仅支持 GR Helper**，不支持 GR Restarter | VPN GR 概述说明 |
| **VPN NSR 双主控** | 支持 NSR 的设备必须硬件具备双主控结构（主备控制平面运行在不同 OMU） | VPN NSR 相关概念 |
| **PE-CE 接口手工绑定** | VPN 实例与 PE-CE 接口的关联必须**手工设置**（路由协议自身不具备区分能力） | 基本概念 VPN 实例章节 |
| **标签规格上限** | MPLS 标签规格 299008 | 特性规格章节 |
| **无应用限制声明** | 产品文档明确"本特性无应用限制"（指无硬性互斥） | 应用限制章节 |

> 来源：综合 9 篇文档的约束说明 [EV-FK-01..09]

---

## 5. 配置案例

### 5.1 典型场景：基本 MPLS VPN（Intranet，PE-CE 用 OSPF）

**场景描述**：某企业有 Site1（总部）和 Site2（分支机构）两个地理隔离的站点，通过 SP 的 MPLS 骨干网互通。UDG1 作 PE1 连接 Site1 的 CE1，UDG2 作 PE2 连接 Site2 的 CE2。VPN1 为 Intranet 闭合用户群。P 设备在骨干网中只做外层标签交换。

> **重要说明**：9 篇产品文档**未提供完整 MML 配置脚本**（区别于 GRE 激活文档含本端+对端完整 MML）。以下为基于原理的配置逻辑框架，具体 MML 命令需 Stage 3 从 UDG 命令字典补全。

**配置逻辑框架**（伪命令，待 Stage 3 补全真实 MML）：

```
=== PE1（UDG1）侧配置 ===

// 步骤1：骨干网 IGP 与 MPLS 基础（前提，非本特性专属）
//   - 配置 OSPF/IS-IS，PE-P-PE 路由可达
//   - 使能 MPLS，建立 PE1-PE2 LSP（LDP/RSVP-TE）

// 步骤2：创建 VPN 实例 vpn1，配置 RD 和 VPN Target
// [推导 MML] ADD/MOD VPNINSTANCE: NAME="vpn1", RD="100:1",
//            ERT="100:1", IRT="100:1"
//   RD=100:1 全局唯一，ERT=IRT=100:1 实现 Intranet（同 RT 才互通）

// 步骤3：将 PE1-CE1 接口绑定到 vpn1
// [推导 MML] 绑定接口到 VPN 实例 vpn1

// 步骤4：配置 PE1-CE1 路由协议（OSPF 多实例）
// [推导 MML] 配置 OSPF 进程绑定 vpn1，与 CE1 交换 IPv4 路由

// 步骤5：配置 MP-BGP，使能 VPNv4 地址族
// [推导 MML] 建立 MP-IBGP PE1-PE2 对等体
//            使能 VPNv4 地址族
//            （可选）配置 perInstance 每实例每标签节约标签

// 步骤6：（可选）配置 VPN GR Helper / NSR 可靠性
// [推导 MML] 使能 GR Helper 或 NSR（NSR 需双主控）

=== PE2（UDG2）侧配置（对称） ===

// 同 PE1，创建 VPN 实例 vpn1（RD 可同 100:1 或不同 100:2，
//   但 ERT/IRT 必须与 PE1 匹配，即 IRT=100:1 接收 PE1 的 ERT=100:1）

=== CE1/CE2 侧配置 ===

// CE1 配置 OSPF 与 PE1 交换本站点 IPv4 路由（CE 不感知 VPN）
// CE2 同理
```

**报文转发验证（CE1 → CE2）**：
1. CE1 发纯 IP 报文到 PE1
2. PE1 查 vpn1 转发表，打内层标签 I-L（标识 vpn1）+ 外层标签 O-L1（到 PE2 的 LSP）
3. P 设备逐跳交换外层标签 O-L1 → O-L2 → ...（不感知 VPN）
4. PE2 去 PHP 后的外层标签，剥离内层标签 I-L
5. PE2 从 vpn1 对应出接口发纯 IP 报文给 CE2

> 来源：综合 `基本概念_92189817.md`（路由发布三段式 + 报文转发两层标签流程）、`GWFD-020411 MPLS VPN_45030708.md`（Intranet 组网）推导 [EV-FK-02, EV-FK-01]
> **文档缺口**：无完整 MML 脚本，Stage 3 需从 UDG 命令字典补全真实命令

### 5.2 场景变体

| 变体 | 场景说明 | 核心差异 | 文档覆盖度 |
|------|---------|---------|-----------|
| Intranet | 闭合用户群互通 | 同 VPN 实例同 RT（ERT=IRT） | 基本概念 + 特性概述 |
| Extranet | VPN 间互访 | 交叉 RT（VPN1 的 ERT 匹配 VPN2 的 IRT） | 特性概述组网图 |
| Hub&Spoke | 中心控制互访 | 双 RT（Hub/Spoke）+ Hub-PE 双接口 + EBGP AS-Loop 允许 | Hub&Spoke 专属文档完整 |
| 跨域 OptionA | 跨 AS 简单互联 | ASBR 互视为 CE，IPv4 交换，每 VPN 独立接口 | 跨域 VPN 文档完整 |
| 跨域 OptionB | 跨 AS 大规模 | ASBR MP-EBGP 标签 VPN-IPv4 + 每下一跳每标签 + PE 每实例每标签 | 跨域 VPN + 分标签文档 |
| MCE | 多 VPN 共享 CE | CE 侧多 VPN 实例，接口分别绑定 | MCE 专属文档完整 |
| IPv6 VPN（6VPE） | IPv6 业务 over IPv4 骨干 | PE-CE 用 BGP4+/OSPFv3/静态 IPv6，VPNv6 over IPv4 隧道 | BGP/MPLS IPv6 VPN 文档 |
| VPN FRR | PE 间快速切换 | PE-PE 链路故障时流量切另一条 PE-PE 链路 | 特性概述提及 |
| VPN GR（Helper） | 主备倒换不中断 | UDG 仅作 Helper，保持转发状态 | VPN GR 文档完整 |
| VPN NSR | 控制平面故障不中断 | 双主控实时同步私网路由/标签/下一跳 | VPN NSR 文档完整 |
| 每实例每标签 | 节约标签 | perInstance，2 万路由占 2 标签 | 分标签文档完整 |
| 每下一跳每标签 | OptionB 节约标签 | perNexthop，ASBR 上配置 | 分标签文档完整 |

> 来源：综合 9 篇文档的场景说明 [EV-FK-01..09]

---

## 6. 验证与调测

### 6.1 验证方法

> **文档缺口说明**：9 篇产品文档**无独立调测文档**（区别于 GRE 的 `调测GRE_06422611.md`/`调测GRE_84704881.md` 两侧 3 步调测流程）。以下验证方法为基于原理推导。

#### 6.1.1 查询验证项（推导）

| 验证目的 | 查询对象 | 说明 |
|---------|---------|------|
| VPN 实例配置 | LST VPN 实例 | 查 RD/ERT/IRT/接口绑定 |
| VPN 路由表 | LST VPN 路由 | 查是否收到对端 PE 发布的 VPN-IPv4 路由 |
| MP-BGP 邻居 | LST BGP 对等体 | 查 PE-PE MP-BGP 状态 Established |
| MPLS 标签 | LST MPLS 标签 | 查内层/外层标签分配，验证 perInstance/perNexthop |
| LSP 隧道 | LSP 信息 | 查 PE-PE LSP 是否建立，Tunnel ID |
| PE-CE 路由 | LST OSPF/BGP 邻居 | 查 PE-CE 路由协议邻居状态 |

#### 6.1.2 报文转发验证

```
验证步骤（推导）：
  1. 查 PE1 VPN 实例路由表是否有 CE2 侧网段路由（经 PE2 MP-BGP 发布）
  2. 查 PE2 VPN 实例路由表是否有 CE1 侧网段路由
  3. CE1 Ping CE2 网段，验证端到端可达
  4. 抓包观察两层标签（外层 O-L 逐跳交换，内层 I-L 不变）
```

> 来源：综合 `基本概念_92189817.md`（路由发布 + 报文转发流程）推导 [EV-FK-02]
> **文档缺口**：无调测文档，具体查询命令需 Stage 3 补全

### 6.2 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| VPN 路由收不到 | ERT/IRT 不匹配 | 核对两端 VPN Target，PE1 ERT 应匹配 PE2 IRT |
| VPN 路由收不到 | MP-BGP 邻居未 Established | 查 MP-BGP 对等体状态；查 TCP 179 端口连通；查 BGP GR capability |
| 报文转发丢包 | LSP 隧道 Down | 查 PE-PE LSP；查骨干网 IGP；查 LDP/RSVP-TE 邻居 |
| 标签资源耗尽 | 使用每路由每标签 | 改配置每实例每标签（VPN）+ 每下一跳每标签（BGP），注意切换会短暂丢包 |
| OptionB 路由异常 | ASBR 与 PE 分标签不配套 | ASBR 配每下一跳每标签时，PE 必须配每实例每标签 |
| Hub&Spoke 路由丢失 | Hub-PE EBGP AS-Loop | Hub-PE 手工配置允许本地 AS 编号重复 |
| Hub&Spoke Spoke 直通 | Spoke-PE RT 配置错误 | 任意 Spoke-PE IRT 不应与其它 Spoke-PE ERT 相同 |
| 地址空间重叠路由丢失 | 未用 VPN 实例隔离 | 确认每个 VPN 独立 VRF + 唯一 RD |
| 主备倒换业务中断 | 未配 GR/NSR | 配置 VPN GR Helper（或 NSR 需双主控） |
| 6VPE IPv6 不通 | 骨干网非 IPv4 | 6VPE 需 IPv4 骨干网承载 IPv6 VPN，当前仅支持 6VPE |
| PE-CE 路由注入错误 VRF | 接口未绑定 VPN 实例 | 手工将 PE-CE 接口绑定到对应 VPN 实例 |

> 来源：综合 9 篇文档的约束与机制说明 [EV-FK-01..09]

---

## 7. 参考信息

### 7.1 接口与信元

| 接口/协议 | 涉及网元 | 关键信元 | 说明 |
|----------|---------|---------|------|
| PE-CE 路由协议 | CE ↔ PE | IPv4/IPv6 路由 | 静态路由 / OSPF（多实例）/ BGP |
| MP-BGP（VPNv4） | PE ↔ PE（同 AS） | VPN-IPv4 地址（12 字节 = RD + IPv4）、ERT、MPLS 内层标签 | PE 间 VPN 路由交换 |
| MP-BGP（VPNv6） | PE ↔ PE | VPN-IPv6 路由 | 6VPE 方案，IPv4 骨干承 IPv6 VPN |
| MP-EBGP（跨域 OptionB） | ASBR ↔ ASBR | 标签 VPN-IPv4 路由 | 跨 AS 标签 VPN 路由交换 |
| EBGP（跨域 OptionA） | ASBR ↔ ASBR | IPv4 路由 | ASBR 互视为 CE，普通 IPv4 |
| IGP（OSPF/IS-IS） | PE ↔ P ↔ PE | 公网 IPv4 路由 | 骨干网路由可达，LSP 基础 |
| LDP / RSVP-TE | PE ↔ P ↔ PE | 标签分发 | 建立 MPLS LSP（外层标签隧道） |
| BGP GR | PE ↔ 邻居 | Open（GR capability）、End-of-Rib | VPN GR 倒换保持转发 |

**VPN-IPv4 地址结构**：
```
┌────────────────────────────────────────┐
│  VPN-IPv4 地址（12 字节）              │
├────────────────┬───────────────────────┤
│  RD（8 字节）  │  IPv4 前缀（4 字节）  │
│  路由标识符    │  标准 IPv4 地址前缀   │
└────────────────┴───────────────────────┘
```

**两层标签栈**：
```
┌─────────────┬─────────────┬──────────────┬──────────┐
│ 外层标签 O-L│ 内层标签 I-L│ IP 头（私网）│ Payload  │
│ (到 BGP     │ (出接口/    │             │          │
│  下一跳)    │  所属 VPN)  │             │          │
└─────────────┴─────────────┴──────────────┴──────────┘
```

> 来源：`基本概念_92189817.md`（图4 VPN-IPv4 地址结构 + 图5 报文转发两层标签）[EV-FK-02]

### 7.2 与其他特性的关系

| 关联特性 | 特性ID | 关系说明 |
|---------|--------|---------|
| **IPFD-015002 GRE**（UDG+UNC） | IPFD-015002 | **隧道方案矩阵**：MPLS VPN 为三层标签交换 VPN（完整 VPN 方案含路由维护），GRE 为三层 IP 封装（点对点隧道，无 VPN 路由维护）；**并列可选方案**，MPLS VPN 适合多 site 运营商级 VPN，GRE 适合简单点对点 |
| **IPFD-015004 IPSec（UDG）** | IPFD-015004 | **隧道方案矩阵**：MPLS VPN 不加密，IPSec 加密+认证；MPLS VPN 适合可信骨干网大规模 VPN，IPSec 适合安全加密场景；可理论叠加（MPLS VPN over IPSec，但本特性文档未提及此组合） |
| **IPFD-016000 IPSec（UNC）** | IPFD-016000 | 同上（UNC 侧 IPSec） |
| **GWFD-020412 L2TP VPN（UDG）** | GWFD-020412 | **隧道方案矩阵**：MPLS VPN 为三层（标签交换），L2TP 为二层（PPP 封装）；MPLS VPN 适合 site-to-site 运营商 VPN，L2TP 适合远程接入（LNS 分配企业 IP） |
| **WSFD-104410 L2TP VPN（UNC）** | WSFD-104410 | 同上（UNC 侧 L2TP） |
| **WSFD-104411 MPLS VPN（UNC）** | WSFD-104411 | **★C-U 对称同构**：UDG 与 UNC 两侧均有同名 MPLS VPN 特性，子文档结构对称（基本概念/分标签/Hub&Spoke/跨域/IPv6 VPN/MCE/GR/NSR 一一对应），双产品同构部署，非 C-U 分工型 |
| IPFD-015000 VPN 功能（配置树父类） | IPFD-015000 | 接入方式类配置树并列节点（本特性 9 篇文档未直接提及父节点关系） |
| IGP（OSPF/IS-IS） | （基础特性） | **隐性依赖**：骨干网路由可达，LSP 建立前提（MPLS VPN 文档未声明交互，但实际依赖） |
| MPLS 基础（LDP/RSVP-TE） | （基础特性） | **隐性依赖**：LSP 隧道建立（外层标签） |
| BGP 基础 | （基础特性） | **隐性依赖**：MP-BGP 邻居建立 |

### 7.3 告警参考

9 篇产品文档中**未列出 MPLS VPN 专属告警**（区别于 SA-Basic 的 ALM-81011/81030/81054）。常见 MPLS VPN 相关告警（如 LSP Down、BGP 邻居断、标签资源告警）需 Stage 3 从告警字典补全。

> 来源：9 篇文档均无告警章节 [EV-FK-01..09]

---

## 8. 知识来源

### 8.1 文档清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020411 MPLS VPN/GWFD-020411 MPLS VPN_45030708.md` | **★特性根文档**：定义（L3VPN，CE/PE/P 三部分）、受益（运营商无，用户网络互通+安全）、可获得性（UDG 20.2.0+，需 License）、应用限制（无）、与其他特性交互（无）、应用场景（Intranet/Extranet/Hub&Spoke/跨域/MCE/VPN-Internet 互联 + 可靠性 VPN FRR/GR Helper/NSR）、实现原理（BGP 发布路由 + MPLS 转发，选 BGP/MPLS 原因）、**特性规格（MPLS 标签 299008 + 必须配置 perInstance/perNexthop 节约标签）**、遵循标准（60+ RFC）、发布历史（v01 20.2.0） |
| 2 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020411 MPLS VPN/基本概念_92189817.md` | **★核心概念**：site 定义、地址空间重叠、VPN 实例（VRF，per-site forwarding table，与公网表隔离）、VPN/Site/VPN 实例关系、**RD（8 字节）+ VPN-IPv4 地址（12 字节）**、**VPN Target（ERT/IRT，32 位扩展团体属性，为什么不直接用 RD）**、MP-BGP（多协议扩展，地址族）、**MPLS VPN 路由发布三段式**（CE→PE→PE→CE）、**MPLS VPN 报文转发两层标签**（I-L/O-L，PHP 倒数第二跳弹出） |
| 3 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020411 MPLS VPN/MPLS VPN的分标签方式_92189833.md` | **分标签机制**：产生原因（缺省每路由每标签消耗大）、三种方式（每路由每标签/每实例每标签 perInstance/每下一跳每标签 perNexthop）、每实例每标签效果（2 万路由→2 标签）、每下一跳每标签效果（OptionB ASBR，2 万路由→2 标签）、**切换丢包约束**、**OptionB 配套约束**（ASBR perNexthop + PE perInstance） |
| 4 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020411 MPLS VPN/Hub&Spoke_92069589.md` | **Hub&Spoke 组网**：Hub/Spoke 站点定义、双 VPN Target（Hub/Spoke）设置规则、Spoke-PE 与 Hub-PE 的 ERT/IRT 配置、路由发布路径（Site2→Hub-PE→Hub-CE→Hub-PE→Site1）、**EBGP AS-Loop 约束**（Hub-PE 须允许本地 AS 重复）、3 种 PE-CE 协议方案（EBGP/IGP/混合） |
| 5 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020411 MPLS VPN/BGP_MPLS IPv6 VPN_45030732.md` | **IPv6 VPN（6VPE）**：两种方案（6VPE: IPv4 骨干承 IPv6 / IPv6 骨干承 IPv6，当前仅支持 6VPE）、PE-CE IPv6 路由协议（BGP4+/静态 IPv6/OSPFv3）、PE 间 IPv4 地址建 VPNv6 邻居、VPN-IPv6 路由选 IPv4 隧道承载、其它原理同 IPv4 VPN |
| 6 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020411 MPLS VPN/跨域VPN_45030728.md` | **跨域 VPN**：跨域需求背景（RFC4364）、OptionA（VRF-to-VRF，ASBR 互视为 CE，IPv4 交换，配置简单但扩展性差）、OptionB（MP-EBGP 标签 VPN-IPv4，不受链路数限制但 ASBR 负担重）、两种 ASBR 处理方法（全部保存 vs RT 过滤）、OptionA/OptionB 优缺点对比 |
| 7 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020411 MPLS VPN/Multi-VPN-Instance CE_45189888.md` | **MCE（多实例 CE）**：产生原因（多 VPN 共享 CE 的成本与安全矛盾）、实现流程（CE 上每个隔离业务一个 VPN 实例，接口+PE 接入接口分别绑定 VPN 实例，RT 一一匹配）、实用价值（PE 功能扩展到 CE，多用户业务隔离，节省设备成本） |
| 8 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020411 MPLS VPN/VPN GR_92069593.md` | **VPN GR**：GR 实现前提（控制转发分离，多 RP 结构）、相关概念（GR Restarter/Helper/Session/Time）、VPN GR 概述（主备倒换 VPN 流量不中断，丢包率 0%）、**UDG 仅支持 GR Helper**、PE/P/CE 主备倒换三阶段处理（倒换前协商/倒换时保持转发/倒换后收敛） |
| 9 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020411 MPLS VPN/VPN NSR_45189892.md` | **VPN NSR**：产生原因（GR 在邻居不支持/多点失效时缺陷，NSR 是 NSF 革新）、相关概念（HA/NSR/NSF/主备主控）、实现过程（批量备份+实时备份+倒换处理，同步私网路由/属性/标签/下一跳）、**双主控硬件约束**、相关功能（NSR 设备仍可作 GR Helper）、适用场景（单节点多链路，如 PE3）、使用价值（单节点技术无需邻居支持） |

### 8.2 关键术语速查

| 术语 | 全称 | 说明 |
|------|------|------|
| MPLS VPN | MPLS L3VPN | 三层标签交换 VPN，BGP 发布路由 + MPLS 转发 |
| VRF | VPN Routing and Forwarding | VPN 路由转发表，每个 VPN 一张，与公网隔离 |
| RD | Route Distinguisher | 8 字节路由标识符，组合 IPv4 成 VPN-IPv4 |
| VPN Target / RT | Route Target | 32 位扩展团体属性，ERT 发布/IRT 接收 |
| MP-BGP | Multiprotocol BGP | BGP 多协议扩展，承载 VPN-IPv4/IPv6 |
| LSP | Label Switched Path | 标签交换路径，公网 MPLS 隧道 |
| I-L / O-L | Inner/Outer Label | 内层标签（VPN/出接口）/ 外层标签（到下一跳） |
| PHP | Penultimate Hop Popping | 倒数第二跳弹出，外层标签提前弹出 |
| perInstance | 每实例每标签 | VPN 实例所有路由共用一标签（节约标签） |
| perNexthop | 每下一跳每标签 | 同下一跳同标签路由共用（OptionB ASBR） |
| MCE | Multi-VPN-Instance CE | 多实例 CE，共享 CE 业务隔离 |
| ASBR | AS Boundary Router | 自治系统边界路由器（跨域） |
| RR | Route Reflector | 路由反射器，减少 MP-IBGP 连接 |
| 6VPE | IPv6 VPN over IPv4 | IPv4 骨干承 IPv6 VPN（当前仅支持） |
| VPN FRR | Fast Reroute | PE 间快速切换 |
| VPN GR | Graceful Restart | 主备倒换不中断（UDG 仅 Helper） |
| VPN NSR | Non-Stop Routing | 控制平面故障不中断（需双主控） |

---

## 9. 文档一致性说明（配置树 vs 产品文档）

> 配置树仅用于定位特性 ID，以下记录以产品文档实际内容为准时发现的差异与协同点，供 Stage 3 横向分析参考。

### 9.1 与任务要求中提及对象的核对（★重点澄清）

| # | 任务要求提及 | 产品文档实际 | 核对结论 |
|---|-------------|-------------|---------|
| 1 | **MPLS VPN 机制（标签交换/VRF）** | **确认**：(a) 标签交换——两层标签栈（外层 O-L 到 BGP 下一跳，P 设备逐跳交换；内层 I-L 标识 VPN/出接口），P 设备不感知 VPN，转发效率高；(b) VRF——VPN 实例（VPN Routing and Forwarding table），PE 上每个 VPN 一张独立路由转发表，与公网表及其它 VPN 隔离，通过 RD 实现 12 字节 VPN-IPv4 地址全局唯一 | 已覆盖（见 §1.1、§2.2、§3.3） |
| 2 | **与 GRE（015002）的隧道对比** | **确认**：MPLS VPN 为三层标签交换 VPN（完整 VPN 方案，含 VRF/MP-BGP/RD/RT，维护 VPN 路由），GRE 为三层 IP 封装（点对点隧道，无 VPN 路由维护，不加密不鉴权）；MPLS VPN 适合运营商级多 site VPN，GRE 适合简单点对点互联；两者并列可选，无直接互斥 | 已覆盖（见 §3.9） |
| 3 | **与 IPSec（015004）的隧道对比** | **确认**：MPLS VPN 不加密（标签转发），IPSec 加密+认证（AH/ESP/IKE）；MPLS VPN 适合可信骨干网大规模 VPN（转发效率高），IPSec 适合安全加密场景；可理论叠加但文档未提及 MPLS VPN over IPSec 组合（与 GRE over IPSec 不同） | 已覆盖（见 §3.9） |
| 4 | **与 L2TP（020412）的隧道对比** | **确认**：MPLS VPN 为三层（标签交换），L2TP 为二层（PPP 封装）；MPLS VPN 适合 site-to-site 运营商 VPN（多组网模型），L2TP 适合远程接入（LNS 分配企业内网 IP）；并列可选 | 已覆盖（见 §3.9） |
| 5 | **与 WSFD-104411（UNC 侧 MPLS）的 C-U 关系** | **★关键发现**：UDG 的 GWFD-020411 与 UNC 的 WSFD-104411 是**双产品对称同构部署**，两侧子文档结构完全对称（基本概念/分标签/Hub&Spoke/跨域/IPv6 VPN/MCE/GR/NSR 一一对应，文件命名仅文件 ID 不同），属 C-U 对称特性，非 C-U 分工型。这与 L2TP（C 决策/U 执行）形成鲜明对比，与 GRE（C-U 对称同构）一致 | 已覆盖（见 §1.2、§7.2） |
| 6 | **MPLS 配置对象与命令（文档依据）** | **★关键缺口**：9 篇产品文档**均为基本概念/原理/组网应用类说明**，**无激活/配置/调测操作文档**（区别于 GRE 含完整激活+调测 MML 脚本）。核心配置对象为 VPN 实例（VRF）+ RD + VPN Target（ERT/IRT）+ 两层标签 + MP-BGP 对等体，但具体 MML 命令（如 ADD/MOD VPNINSTANCE、配置 BGP VPNv4 对等体等）**文档未直接列出**，需 Stage 3 从 UDG 命令字典补全 | **缺口**：MML 命令需 Stage 3 补全（见 §4.2） |

### 9.2 与配置树/文档清单的差异

| # | 维度 | 配置树/文档清单描述 | 产品文档实际内容 | 差异类型 |
|---|------|---------------------|-----------------|---------|
| 1 | 文件数与分布 | 文档清单列 9 个文件（全 UDG 侧） | 实际 9 篇全为概念/原理/组网说明文档，**无激活/调测/参考信息操作文档**；文档密度偏理论 | 补全：MML 命令清单缺失，需 Stage 3 从命令字典补 |
| 2 | License 要求 | 文档清单标注"[★核心]" | 产品文档明确"**需 License**"（可选特性，编号未列出） | 澄清：MPLS VPN 需 License，区别于 GRE（无 License） |
| 3 | 首次发布版本 | 文档清单未标注版本 | **20.2.0 首次发布**，晚于 GRE（20.0.0）/ SA-Basic（20.0.0）等基础特性 | 补全：版本信息 |
| 4 | 特性规格 | 文档清单未提及规格 | **MPLS 标签规格 299008**，且**必须配置 perInstance/perNexthop**节约标签（本端+对端同步） | 补全：标签规格与节约约束 |
| 5 | 与其他特性交互 | 文档清单未提及 | 产品文档明确"**本特性不涉及与其他特性的交互**"（但隐性依赖 IGP/MPLS/BGP 基础特性） | 澄清：显式无交互，隐性依赖 |
| 6 | 应用限制 | 文档清单未提及 | 产品文档明确"**本特性无应用限制**"（指无硬性互斥） | 补全：无应用限制声明 |
| 7 | 运营商受益 | 文档清单未提及 | 产品文档明确"运营商受益：**无**"（仅用户受益：网络互通+安全） | 补全：受益说明 |
| 8 | 文档缺口 | 文档清单未提及 | 9 篇文档无 MML 命令清单、无完整配置脚本、无调测流程、无告警清单 | **重大缺口**：Stage 3 需补全命令/脚本/调测/告警 |

### 9.3 与同域隧道特性的横向对比（★Stage 3 重点）

| # | 维度 | GWFD-020411 MPLS VPN | IPFD-015002 GRE | IPFD-015004 IPSec | GWFD-020412 L2TP |
|---|------|---------------------|----------------|-------------------|------------------|
| 1 | 隧道层级 | 三层（标签交换） | 三层（IP 封装） | 三层（IP 加密） | 二层（PPP 封装） |
| 2 | VPN 路由维护 | **有（VRF+MP-BGP+RD/RT）** | 无 | 无 | 无 |
| 3 | 地址重叠隔离 | **有（RD）** | 无 | 无 | 无 |
| 4 | 加密 | 无 | 无 | 有（AH/ESP） | 无 |
| 5 | 鉴权 | 无 | 无（可选 Key） | 有（IKE） | 有（PAP/CHAP） |
| 6 | 地址分配 | 不涉及 | 不涉及 | 不涉及 | LNS 远程分配 |
| 7 | License | **需** | 无 | 需 | UDG 必须 |
| 8 | C-U 模式 | **对称同构** | 对称同构 | 各自配置 | C-U 分工 |
| 9 | 规格 | 标签 299008 | 4k Tunnel | （IPSec 覆盖） | Group 1500×2 |
| 10 | 组网模型 | **6 种**（Intranet/Extranet/Hub&Spoke/跨域/MCE/VPN-Internet） | 点对点 | 点对点+主备 | 远程接入 |
| 11 | 跨域支持 | **原生**（OptionA/B） | 手工对接 | 手工对接 | 不涉及 |
| 12 | 可靠性 | **FRR+GR+NSR** | Keepalive | IKE DPD | Hello 60s |
| 13 | IPv6 | 6VPE | IPv6 参数 | IPv6 IPSec | L2TP IPv6 |
| 14 | 首发版本 | **20.2.0** | 20.0.0 | 20.0.0 | 20.0.0 |
| 15 | 标准 | RFC 60+ | RFC 1701/1702/2784 | RFC AH/ESP/IKE | RFC 2661 等 |
| 16 | 典型 NF 角色 | **PE** | PE | IPSec 端点 | UDG 作 LAC |
| 17 | 典型用途 | 运营商级多 site VPN | 轻量互联 | 安全加密 | 远程接入 |

---

## 附录 A：source_evidence_ids 占位映射

| evidence_id | 对应来源文件 | 主要贡献章节 |
|-------------|-------------|-------------|
| EV-FK-01 | `GWFD-020411 MPLS VPN_45030708.md` | ★特性根文档：定义（CE/PE/P）、受益（运营商无/用户互通+安全）、可获得性（UDG 20.2.0+，需 License）、应用限制（无）、与其他特性交互（无）、应用场景（Intranet/Extranet/Hub&Spoke/跨域/MCE/VPN-Internet + 可靠性 FRR/GR Helper/NSR）、实现原理（BGP 发布 + MPLS 转发）、**特性规格（标签 299008 + perInstance/perNexthop 节约约束）**、遵循标准（60+ RFC）、发布历史（v01 20.2.0） |
| EV-FK-02 | `基本概念_92189817.md` | ★核心概念：site/地址空间重叠/VPN 实例（VRF）/VPN-Site-VRF 关系/**RD 8 字节 + VPN-IPv4 12 字节**/**VPN Target ERT/IRT 32 位扩展团体属性（为什么不用 RD）**/MP-BGP 地址族/**路由发布三段式**（CE→PE→PE→CE）/**报文转发两层标签**（I-L/O-L + PHP 倒数第二跳弹出） |
| EV-FK-03 | （并入 EV-FK-01，特性根文档已覆盖应用场景与可靠性） | 保留占位，避免重号 |
| EV-FK-04 | `MPLS VPN的分标签方式_92189833.md` | 分标签机制：三种方式（每路由/每实例 perInstance/每下一跳 perNexthop）、节约效果（2 万路由→2 标签）、**切换丢包约束**、**OptionB 配套约束**（ASBR perNexthop + PE perInstance） |
| EV-FK-05 | `Hub&Spoke_92069589.md` | Hub&Spoke 组网：双 VPN Target（Hub/Spoke）设置规则、Spoke-PE/Hub-PE 的 ERT/IRT、路由发布路径、**EBGP AS-Loop 约束**（Hub-PE 须允许本地 AS 重复）、3 种 PE-CE 协议方案 |
| EV-FK-06 | `跨域VPN_45030728.md` | 跨域 VPN：RFC4364 背景、OptionA（VRF-to-VRF，ASBR 互视 CE，IPv4 交换，简单但扩展性差）、OptionB（MP-EBGP 标签 VPN-IPv4，不受链路数限但 ASBR 负担重）、两种 ASBR 处理方法、OptionA/B 对比 |
| EV-FK-07 | `BGP_MPLS IPv6 VPN_45030732.md` | IPv6 VPN（6VPE）：两种方案（当前仅支持 6VPE：IPv4 骨干承 IPv6）、PE-CE IPv6 协议（BGP4+/静态/OSPFv3）、PE 间 IPv4 建 VPNv6 邻居、VPN-IPv6 选 IPv4 隧道承载 |
| EV-FK-08 | `VPN GR_92069593.md` | VPN GR：GR 前提（控制转发分离多 RP）、概念（Restarter/Helper/Session/Time）、**UDG 仅支持 GR Helper**、PE/P/CE 主备倒换三阶段（协商/保持转发/收敛）、丢包率 0% |
| EV-FK-09 | `VPN NSR_45189892.md` + `Multi-VPN-Instance CE_45189888.md` | VPN NSR：NSR vs NSF、双主控硬件约束、批量+实时备份（私网路由/属性/标签/下一跳）、NSR 设备仍可作 GR Helper、单节点多链路场景；MCE：多 VPN 共享 CE、接口+PE 接口分别绑定 VPN 实例、RT 一一匹配、PE 功能扩展到 CE 节省成本 |

> **注**：EV-FK-03 与 EV-FK-01 内容重叠（特性根文档已覆盖应用场景与可靠性），保留占位以与 source_evidence_ids 列表一致；实际证据贡献由 EV-FK-01/02/04/05/06/07/08/09 八篇文档提供（根 + 基本概念 + 6 篇子文档）。
