# IPFD-015002 GRE 知识文档

> 聚焦 APN 业务域接入方式场景的 GRE（Generic Routing Encapsulation）隧道特性
> 跨 UDG（U 面）与 UNC（C 面）双产品对称部署，接入方式类核心隧道技术之一
> 与 IPSec（IPFD-015004 / IPFD-016000）、L2TP（GWFD-020412 / WSFD-104410）共同构成 APN 域的隧道方案矩阵
> 适用 NF：SGW-U/PGW-U/UPF（UDG）、SGW-C/PGW-C/SMF（UNC）
> C-U 对称：两侧配置对象与命令基本对称（ADD GRETUNNEL），非 C-U 分工型

---

## 0. 元数据（三层图谱 Schema 字段）

| 字段 | 取值 |
|------|------|
| feature_id | IPFD-015002 |
| feature_name | GRE |
| feature_group | 接入方式 |
| parent_feature_id | IPFD-015000（VPN 功能，配置树父节点） |
| applicable_nf_map | `{"UDG": ["SGW-U", "PGW-U", "UPF"], "UNC": ["SGW-C", "PGW-C", "SMF"]}` |
| variant_dimensions | ["隧道源类型(SRCIP/SRCIFNAME)", "地址族(IPv4 / IPv6 / 双栈)", "端到端校验(CHECKSUMEN=TRUE/FALSE)", "识别关键字(GREKEYEN + GREKEY)", "Keepalive检测(KEEPALVEN + 周期 + 重试次数)", "多租户共享(同源同宿多隧道 + GRE Key 区分)", "嵌套层数(单层 / 两层嵌套)", "VPN实例绑定(公网 / VPN实例)"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-01, EV-FK-02, EV-FK-03, EV-FK-04, EV-FK-05, EV-FK-06, EV-FK-07, EV-FK-08] |
| license_required | **无需 License**（UDG/UNC 两侧均无 License 要求，产品文档明确"本特性无需获得 License 许可"） |

---

## 1. 概述

### 1.1 特性定义（是什么）

GRE（Generic Routing Encapsulation，通用路由封装协议）可以对某些网络层协议的数据报文进行封装，使这些被封装的数据报文能够在 IPv4 网络中传输。GRE 提供了将一种协议的报文封装在另一种协议报文中的机制，使报文能够在异种网络中传输，而异种报文传输的通道称为 Tunnel。GRE 可以作为 VPN 的第三层隧道协议，为 VPN 数据提供透明传输通道。

本特性是**跨 UDG/UNC 双产品的轻量级三层隧道封装特性**：在 UDG（SGW-U/PGW-U/UPF）与 UNC（SGW-C/PGW-C/SMF）两侧均基于 Tunnel 接口与 GRE 隧道对象（GRETUNNEL）实现，通过公网 IP 转发封装后的报文。**GRE 只做封装，不加密、不鉴权**，通过 Keepalive 检测链路状态，通过 GRE Key 标识隧道（可扩展多租户共享）。

> 来源：`IPFD-015002 GRE特性概述_61317365.md`（"定义"章节）[EV-FK-01]

### 1.2 适用 NF（UDG/UNC 网元）

| 涉及 NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| SGW-U / PGW-U / UPF | 用户面（UDG） | UDG 20.0.0 及后续版本 | 用户面建立 GRE 隧道，封装/解封装用户面报文，穿越公网或非骨干网 |
| SGW-C / PGW-C / SMF | 控制面（UNC） | UNC 20.0.0 及后续版本 | 控制面建立 GRE 隧道，用于 C 面网管/信令通道穿越异种网络（如带内组网到 AAA Server） |

> 来源：`IPFD-015002 GRE特性概述_61317365.md`（"可获得性/版本支持"章节，UNC 20.0.0+）；UDG 侧 `调测GRE_06422611.md` 调测窗口为"MML 命令行-UDG"，命令路径同构 [EV-FK-01, EV-FK-08]

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|---------|---------|---------|
| 01 | 20.0.0 | 首次发布 |

> 来源：`IPFD-015002 GRE特性概述_61317365.md`（"发布历史"章节）[EV-FK-01]

### 1.4 License

**本特性无需 License 许可**。产品文档明确声明"本特性无需获得 License 许可即可获得该特性的服务"。UDG 与 UNC 两侧均无 License 控制项。

> 来源：`IPFD-015002 GRE特性概述_61317365.md`（"可获得性/License 支持"章节）[EV-FK-01]

### 1.5 前置条件与依赖

| 前置条件 | 说明 |
|---------|------|
| 隧道源端口和目的端口已路由可达 | 激活硬约束，需通过 PING 验证 |
| 待创建的 GRE 隧道不存在 | 同名隧道不能重复创建 |
| VPN 实例（可选） | 若采用 VPN 组网方式，需先创建 VPN 实例（`ADD VPNINST`） |
| LoopBack 接口（推荐源） | 推荐以 LoopBack 接口作为 GRE 隧道源，保证源 IP 稳定 |
| 静态路由 | Tunnel 接口需配置静态路由（`ADD SRROUTE`），引导流量进入隧道 |
| OSPF 路由（可选协同） | 源端与目的端都必须存在经过 Tunnel 转发的路由，可通过 OSPF 获得 |

> 来源：`激活支持GRE_06422610.md`（"必备事项/前提条件"）、`IPFD-015002 GRE特性概述_61317365.md`（"与其他特性的交互"章节 OSPPF）[EV-FK-03, EV-FK-01]

### 1.6 与其他特性的交互

| 交互类型 | 相关特性 | 交互说明 |
|---------|---------|---------|
| **协同** | IPFD-014001 支持 OSPF | 源端和目的端都必须存在经过 Tunnel 转发的路由；通过 OSPF 获得 Tunnel 接口路由 |
| **互斥（源地址约束）** | IPFD-015004/IPFD-016000 IPSec | **GRE 隧道的源地址不能和 IPSec 隧道的源地址相同**（应用限制硬约束） |
| **组合** | IPFD-015004/IPFD-016000 IPSec（GRE over IPSec） | IPSec 激活文档存在"GRE over IPSec"场景，即先建 GRE 隧道再叠加 IPSec 加密，弥补 GRE 不加密的缺陷 |
| **协同（Radius 组网）** | WSFD-011306 Radius 功能 | UNC 侧 Radius 激活文档中"带内/带外组网 GRE VPN"场景使用 GRE 隧道穿越到 AAA Server |

> 来源：`IPFD-015002 GRE特性概述_61317365.md`（"与其他特性的交互" + "应用限制"章节）[EV-FK-01]

### 1.7 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | GRE 对设备的性能的要求较低，可以在设备间建立隧道；多租户共享场景下节约公网 IP，提高接入设备利用率 |
| 终端用户 | 用户不感知该特性 |

> 来源：`IPFD-015002 GRE特性概述_61317365.md`、`多租户共享GRE隧道_61317217.md`（"客户价值"章节）[EV-FK-01, EV-FK-06]

### 1.8 应用场景

- **异种网络互通**：骨干网与非骨干网使用不同协议（如 IPv4 与 IPX），通过 GRE 隧道封装实现互通
- **扩大跳数受限网络的工作范围**：IP 跳数受限（如 255）时，GRE 隧道可跨越部分步跳
- **连接不连续子网组建 VPN**：使用 GRE 隧道将不连续子网连接，实现跨越广域网的 VPN
- **多租户共享 GRE 隧道**：同源同宿（源地址和目的地址相同）的多条 GRE 隧道，以 GRE Key 区分不同租户/VPN 流量，节约公网 IP
- **Radius 带内/带外组网**：UNC 到 AAA Server 之间通过 GRE VPN 穿越网络

> 来源：`IPFD-015002 GRE特性概述_61317365.md`（"应用场景"章节）、`多租户共享GRE隧道_61317217.md` [EV-FK-01, EV-FK-06]

### 1.9 对系统的影响

**本特性对系统无影响**。产品文档明确声明"本特性对系统无影响"，GRE 是轻量封装，不涉及加密运算，性能开销极低。激活操作本身对系统正常运行也无影响（去激活时若 GRE 隧道上仍有报文，将导致业务中断）。

> 来源：`IPFD-015002 GRE特性概述_61317365.md`（"对系统的影响"章节）、`激活支持GRE_06422610.md`（"对系统的影响"）、`去激活支持GRE_06422612.md`（"对系统的影响"）[EV-FK-01, EV-FK-03, EV-FK-04]

### 1.10 应用限制

- **嵌套层数限制（★关键）**：GRE 隧道可以嵌套其他 GRE 隧道，**最多支持两层嵌套**；超过两层嵌套的 GRE 隧道状态会变为 Down（如三层嵌套时，第三层 GRE 隧道状态 Down）。**禁止大于两层的 GRE 隧道嵌套**
- **源地址互斥（★关键）**：GRE 隧道的源地址不能和 IPSec 隧道的源地址相同
- 多租户共享 GRE 隧道子特性无应用限制

> 来源：`IPFD-015002 GRE特性概述_61317365.md`（"应用限制"章节）、`多租户共享GRE隧道_61317217.md`（"应用限制"章节）[EV-FK-01, EV-FK-06]

### 1.11 特性规格

| 规格名称 | 规格指标 |
|---------|---------|
| 整个系统最大支持配置 GRE Tunnel 接口数量 | **4k（4096 个）** |

> 来源：`IPFD-015002 GRE特性概述_61317365.md`（"特性规格"章节）[EV-FK-01]

### 1.12 计费与话单

**本特性不涉及计费与话单**。

> 来源：`IPFD-015002 GRE特性概述_61317365.md`（"计费与话单"章节）[EV-FK-01]

### 1.13 遵循标准

| 标准类别 | 标准名称 |
|---------|---------|
| RFC | RFC 1701 Generic Routing Encapsulation（GRE） |
| RFC | RFC 1702 Routing Encapsulation over IPv4 networks |
| RFC | RFC 2784 Generic Routing Encapsulation (GRE) |

> 来源：`IPFD-015002 GRE特性概述_61317365.md`（"遵循标准"章节）[EV-FK-01]

---

## 2. 核心概念

### 2.1 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| GRE | Generic Routing Encapsulation，通用路由封装 | 通用路由封装协议，对某些网络层协议报文进行封装，使其能在另一网络层协议（如 IP）中传输；可作为 VPN 第三层隧道协议 |
| Tunnel | 隧道 | 异种报文传输的通道；GRE 隧道由源地址、目的地址、Tunnel 接口构成 |
| 净荷（Payload） | - | 系统收到需要封装和传输的数据报 |
| 乘客协议（Passenger Protocol） | - | 封装前的报文协议 |
| 封装协议（Encapsulation Protocol） | - | GRE 协议，也称运载协议（Carrier Protocol） |
| 传输协议（Transport Protocol） | - | 负责对封装后报文转发的协议（如 IP） |
| GRETUNNEL | GRE 隧道对象 | **本特性核心配置对象**，通过 `ADD GRETUNNEL` 创建，绑定 Tunnel 接口名、隧道类型、源/目的地址 |
| Tunnel 接口 | 虚拟隧道接口 | GRE 隧道的虚拟接口，需配置 IP 地址（`ADD IFIPV4ADDRESS`），作为隧道两端的路由下一跳 |
| LoopBack 接口 | 环回接口 | 推荐作为 GRE 隧道源接口，提供稳定源 IP |
| GRE Key | 关键字字段 | GRE 报文头中的 Key 字段，隧道接收端用于验证；多租户共享场景下作为租户区分标签 |
| Checksum | 校验和字段 | GRE 报文头中的校验和，对 GRE 头及负载校验（可选，CHECKSUMEN 控制） |
| Keepalive | 链路状态检测 | GRE 不具备检测链路状态能力，Keepalive 检测功能周期发送探测报文，防止数据黑洞 |
| Recursion | 嵌套层数字段 | GRE 报文头字段，表示报文被封装层数；完成一次封装加 1，大于 3 丢弃（实际限制两层嵌套） |
| Protocol Type | 乘客协议类型 | GRE 报文头字段，标识乘客协议 |
| 协议号 47 | GRE 协议号 | 外层 IP 头协议字段值 47（参见 RFC 1701/RFC 2784），Egress PE 据此交给 GRE 模块处理 |

> 来源：`GRE报文格式_61317188.md`、`Keepalive检测_61317267.md`、`多租户共享GRE隧道_61317217.md`、`IPFD-015002 GRE特性概述_61317365.md`（"原理概述"章节协议号 47）[EV-FK-02, EV-FK-05, EV-FK-06, EV-FK-01]

### 2.2 对象模型

IPFD-015002 在 UDG 与 UNC 两侧的对象模型**高度对称**（非 C-U 分工型，而是双产品同构部署），核心对象为 GRETUNNEL + Tunnel 接口 + LoopBack 接口，辅以静态路由：

```
┌──────────────────────────────────────────────────────────────────────┐
│ UDG（U 面）/ UNC（C 面）共用配置对象（两侧同构）                       │
│                                                                      │
│   ┌──────────────┐                                                   │
│   │ LoopBack 接口│ ← ADD INTERFACE + ADD IFIPV4ADDRESS               │
│   │ (推荐隧道源)  │   提供稳定源 IP（如 10.3.3.11/32）                │
│   └──────┬───────┘                                                   │
│          │                                                           │
│          │ SRCIFNAME 引用                                            │
│          ▼                                                           │
│   ┌──────────────────────────────────────────────┐                   │
│   │  GRETUNNEL  ★本特性核心对象                   │ ← ADD GRETUNNEL   │
│   │  TNLNAME="Tunnel1"                           │   MOD GRETUNNEL   │
│   │  TNLTYPE=gre                                 │   RMV GRETUNNEL   │
│   │  SRCTYPE=if_name                             │                   │
│   │  SRCIFNAME="LoopBack1"                       │                   │
│   │  DSTIPADDR="10.4.4.11"                       │                   │
│   │  ┌────────────────────────────────────────┐  │                   │
│   │  │ 可选特性（MOD GRETUNNEL 配置）：        │  │                   │
│   │  │  CHECKSUMEN=TRUE  (端到端校验)         │  │                   │
│   │  │  GREKEYEN=TRUE + GREKEY="123" (识别字) │  │                   │
│   │  │  KEEPALVEN=TRUE                         │  │                   │
│   │  │  + KEEPALVPERIOD=5 + KEEPALVRETRYCNT=3 │  │                   │
│   │  └────────────────────────────────────────┘  │                   │
│   └──────┬───────────────────────────────────────┘                   │
│          │                                                           │
│          │ Tunnel 接口需配置 IP                                      │
│          ▼                                                           │
│   ┌──────────────┐                                                   │
│   │ Tunnel 接口  │ ← ADD IFIPV4ADDRESS: IFNAME="Tunnel1"             │
│   │ IP(如        │   隧道两端点路由下一跳（如 10.10.1.201/24）       │
│   │ 10.10.1.201)│                                                   │
│   └──────┬───────┘                                                   │
│          │                                                           │
│          │ 引导流量进入隧道                                           │
│          ▼                                                           │
│   ┌──────────────┐                                                   │
│   │ 静态路由     │ ← ADD SRROUTE: IFNAME="Tunnel1", PREFIX=对端网段  │
│   └──────────────┘                                                   │
│                                                                      │
│   可选基础设施：                                                      │
│   ┌──────────────┐  ┌──────────────┐                                │
│   │ VPN 实例     │  │ OSPF 路由    │                                │
│   │ (VPN 组网)   │  │ (动态获取    │                                │
│   │              │  │  Tunnel 路由)│                                │
│   └──────────────┘  └──────────────┘                                │
└──────────────────────────────────────────────────────────────────────┘
```

核心对象说明：

| 对象 | 命令 | 作用 | UDG/UNC |
|------|------|------|---------|
| **GRETUNNEL** | `ADD/MOD/RMV/LST GRETUNNEL` | **★本特性核心对象**。GRE 隧道容器，定义 Tunnel 名称、类型、源/目的地址、可选的 Checksum/Key/Keepalive | 两侧同构 |
| **Tunnel 接口** | `ADD IFIPV4ADDRESS`（在 GRETUNNEL 创建后） | 隧道虚拟接口 IP，作为隧道两端路由下一跳 | 两侧同构 |
| **LoopBack 接口** | `ADD INTERFACE` + `ADD IFIPV4ADDRESS` | 推荐作为 GRE 隧道源，提供稳定源 IP | 两侧同构 |
| **静态路由** | `ADD SRROUTE` | 引导流量进入 Tunnel 接口 | 两侧同构 |
| **VPN 实例** | `ADD VPNINST` | VPN 组网方式下绑定（可选） | 两侧同构 |
| **OSPF 路由** | （IPFD-014001） | 动态获取 Tunnel 接口路由（协同） | 两侧同构 |

> 来源：`激活支持GRE_06422610.md`（"必备事项/数据"表 + "操作步骤"6 步 + 任务示例脚本）、`多租户共享GRE隧道_61317217.md`（多租户场景下 GRE Key 区分租户）[EV-FK-03, EV-FK-06]

### 2.3 在接入方式场景的角色

IPFD-015002 在 APN 接入方式场景中扮演**"轻量级三层隧道封装"**的角色，与 IPSec（加密隧道）、L2TP（二层 PPP 隧道）、MPLS VPN（标签隧道）共同构成隧道方案矩阵：

1. **轻量封装**：GRE 只对报文加 GRE 头 + 外层 IP 头，**不加密、不鉴权**，性能开销远低于 IPSec
2. **三层隧道**：作为 VPN 第三层隧道协议，为 VPN 数据提供透明传输通道（区别于 L2TP 的二层 PPP 隧道）
3. **异种网络互通**：通过协议封装解决骨干网（如 IPv4）与非骨干网（如 IPX）协议不一致问题
4. **VPN 组建**：将不连续子网连接，跨越广域网组建 VPN
5. **多隧道组合**：可与 IPSec 组合形成"GRE over IPSec"（先 GRE 封装再 IPSec 加密），弥补 GRE 不加密的缺陷
6. **多租户共享**：同源同宿多隧道以 GRE Key 区分租户，节约公网 IP

> 来源：`IPFD-015002 GRE特性概述_61317365.md`（"定义/应用场景/原理概述"章节）[EV-FK-01]

---

## 3. 原理与流程

### 3.1 实现原理（封装 + 解封装）

报文在 GRE 隧道中传输包括封装和解封装两个过程。私网报文从 Ingress PE 向 Egress PE 传输时，封装在 Ingress PE 完成，解封装在 Egress PE 进行。

```
┌─────────────────────────────────────────────────────────────────┐
│ 封装过程（Ingress PE / UDG 或 UNC 本端）                          │
│                                                                 │
│   1. 从连接私网的接口收到私网报文                                 │
│   2. 私网协议模块查路由表，出接口为 GRE Tunnel 接口               │
│   3. 交给隧道模块：                                              │
│      3a. 根据乘客协议类型 + 配置的 Key/Checksum，添加 GRE 头      │
│      3b. 加外层 IP 头：源地址=隧道源地址，目的地址=隧道目的地址   │
│      3c. 交 IP 模块，按外层 IP 目的地址查公网路由表转发           │
│                                                                 │
│   封装后报文格式（从外到内）：                                    │
│   ┌─────────┬───────────┬───────────────┬──────────────┐        │
│   │ 外层IP头│  GRE 头    │ 乘客协议头     │  Payload     │        │
│   │ 协议=47 │(Key/Checksum│(如 IP/IPX)    │              │        │
│   │         │ 可选)      │               │              │        │
│   └─────────┴───────────┴───────────────┴──────────────┘        │
└─────────────────────────────────────────────────────────────────┘
                              ↓ 公网传输
┌─────────────────────────────────────────────────────────────────┐
│ 解封装过程（Egress PE / UDG 或 UNC 对端）                         │
│                                                                 │
│   1. 从公网接口收到报文，分析 IP 头：目的地址=本设备              │
│   2. 协议字段值=47（GRE，参见 RFC 1701/RFC 2784）→ 交 GRE 模块   │
│   3. GRE 模块去 IP 头和 GRE 头                                   │
│   4. 按 GRE 头 Protocol Type 字段识别乘客协议                    │
│   5. 交乘客协议模块，像普通报文一样转发                          │
└─────────────────────────────────────────────────────────────────┘
```

> 来源：`IPFD-015002 GRE特性概述_61317365.md`（"原理概述"章节，图3 私有网络通过 GRE 隧道互连）、`GRE报文格式_61317188.md`（封装格式与字段）[EV-FK-01, EV-FK-02]

### 3.2 GRE 报文头格式

GRE 报文头包含以下关键字段：

| 字段 | 说明 |
|------|------|
| C（Checksum 位） | 置 1 表示 GRE 头插入 Checksum 字段；0 表示不含 |
| K（Key 位） | 置 1 表示 GRE 头插入 Key 字段；0 表示不含 |
| Recursion（嵌套层数） | 表示 GRE 报文被封装层数，每封装一次加 1；大于 3 丢弃（防无限封装）。UNC 实现仅在加封装时用作标记嵌套层数，解封装时不感知 |
| Flags | 预留字段，当前必须设为 0 |
| Version | 版本字段，必须置 0（Version=1 用于 RFC2637 PPTP） |
| Protocol Type | 乘客协议类型 |
| Checksum | GRE 头及负载的校验和（C=1 时存在） |
| Key | 关键字字段，隧道接收端验证报文（K=1 时存在；多租户场景作为租户区分标签） |

> 说明：UNC 实现的 GRE 头不包含源路由字段，故 Bit 1、Bit 3、Bit 4 都置为 0。

> 来源：`GRE报文格式_61317188.md`（图3 GRE 报文头格式 + 字段解释）[EV-FK-02]

### 3.3 Keepalive 检测机制

**产生原因**：GRE 协议本身不具备检测链路状态的功能。若远端不可达，隧道不会及时关闭，源端持续向对端转发数据而对端丢弃所有报文，形成"数据黑洞"。

**实现过程**：

```
┌─────────────────────────────────────────────────────────────────┐
│ Keepalive 检测（源端使能 KEEPALVEN=TRUE 后）                      │
│                                                                 │
│   1. 创建定时器，周期发送 Keepalive 探测报文（默认周期 5 秒）     │
│      同时进行不可达计数，每发一个探测报文计数加 1                 │
│                                                                 │
│   2. 对端收到探测报文 → 回应报文                                 │
│      （对端无论是否配置 Keepalive 都会回应）                     │
│                                                                 │
│   3. 源端判断：                                                  │
│      - 计数未达阈值就收到回应 → 对端可达，计数清零               │
│      - 计数达重试次数（默认 3 次）仍未收到回应 → 对端不可达      │
│        → 关闭隧道连接                                            │
└─────────────────────────────────────────────────────────────────┘
```

**特点**：只要隧道一端配置 Keepalive，该端就具备检测功能，**不要求对端也配置**。对端收到探测报文时，无论是否配置 Keepalive，都会回送回应报文。

> 来源：`Keepalive检测_61317267.md`（"产生原因 + 实现过程"完整说明）[EV-FK-05]

### 3.4 多租户共享 GRE 隧道机制

为节约公网 IP，在 DeviceA 和 DeviceB 上建立**同源同宿**（源地址和目的地址相同）的多条 GRE 隧道，不同隧道以 **GRE 报文头中的 GRE Key 字段**作为区分标签。

```
┌──────────────────────────────────────────────────────────┐
│ 多租户共享 GRE 隧道（同源同宿 + GRE Key 区分）             │
│                                                          │
│   租户A 流量 ──┐                                         │
│   租户B 流量 ──┼─→ DeviceA ──→ GRE 隧道1 (GRE Key=K1) ──→│
│   租户C 流量 ──┤    (公网IP相同)  GRE 隧道2 (GRE Key=K2)  │
│                │                 GRE 隧道3 (GRE Key=K3)  │
│                │                                          │
│                │    静态路由将不同租户 IP 出接口          │
│                │    分别配置到对应 GRE 隧道              │
│                                                          │
│   入隧道：不同租户流量由对应静态路由引入对应 GRE 隧道      │
│   出隧道：通过源/目的 IP + 剥离后的 GRE Key 找到对应      │
│           GRE 隧道下一跳转发                              │
└──────────────────────────────────────────────────────────┘
```

> 来源：`多租户共享GRE隧道_61317217.md`（"实现原理"章节）[EV-FK-06]

### 3.5 协议交互

| 接口 | 交互网元 | 消息类型 | 说明 |
|------|---------|---------|------|
| GRE 数据面（公网 IP） | Ingress PE ↔ Egress PE（UDG↔UDG 或 UNC↔UNC 或跨产品） | 封装后的 IP 报文（协议号 47） | 公网转发封装报文 |
| Keepalive 探测 | 源端 ↔ 对端 | Keepalive 探测报文 + 回应报文 | 链路状态检测，周期 5 秒，重试 3 次 |
| OSPF（协同） | Tunnel 接口路由交互 | OSPF Hello/LSA | 动态获取经过 Tunnel 的路由（需 IPFD-014001） |

> 来源：`Keepalive检测_61317267.md`（实现过程）、`IPFD-015002 GRE特性概述_61317365.md`（OSPF 协同）[EV-FK-05, EV-FK-01]

### 3.6 与 IPSec/L2TP 的隧道对比（★重点）

| 维度 | IPFD-015002 GRE | IPFD-015004/016000 IPSec | GWFD-020412/WSFD-104410 L2TP |
|------|----------------|--------------------------|------------------------------|
| **隧道层级** | 三层（网络层封装） | 三层（网络层加密） | 二层（数据链路层，封装 PPP） |
| **加密** | **不加密** | **加密 + 认证**（AH/ESP、IKE） | 不加密 |
| **鉴权** | 无（可选 GRE Key 标识） | 有（IKE 协商、证书） | 有（内层 PPP 的 PAP/CHAP） |
| **封装开销** | 轻量（GRE 头 + 外层 IP 头） | 重（ESP/AH 头 + 加密运算） | 中（L2TP 头 + PPP 头） |
| **对系统性能影响** | **无影响**（轻量） | 有（加密解密运算开销） | 有（激活时延增加 + L2TP 封装） |
| **License** | **无需 License** | 需 License（IPSec） | UDG 必须 License（82200BVC LKV3G5L2TP01），UNC 无 |
| **地址分配** | 不涉及（GRE 不终结用户会话） | 不涉及 | **LNS 分配企业内网 IP**（IPCP/IPv6CP 协商） |
| **核心协议** | RFC 1701/1702/2784 | RFC 系列（AH/ESP/IKE） | RFC 2661/2868/5072/5571/8064 |
| **典型用途** | 异种网络互通、VPN 组建、多租户共享 | 安全加密隧道、GRE over IPSec | 企业远程接入、LNS 远程地址分配 |
| **嵌套能力** | 最多两层 GRE 嵌套 | 可被 GRE 嵌套（GRE over IPSec） | 不涉及 |
| **C-U 分工** | **C-U 对称同构**（两侧命令一致） | C-U 分工（UDG/UNC 各自配置） | **C-U 分工**（C 决策下发 LNS 参数，U 作 LAC 封装） |
| **典型 NF 角色** | UDG/UNC 均作为 PE 设备 | UDG/UNC 均作为 IPSec 端点 | UDG 作 LAC，LNS 在企业网 |
| **互斥关系** | GRE 源地址不能与 IPSec 源地址相同 | - | 与地址自动检测、入不转板互斥 |
| **Keepalive 机制** | 有（周期 5s，重试 3 次） | 有（IKE DPD） | 有（Hello 报文 60s，重试 3 次） |

> 来源：综合本特性 8 篇文档 + GWFD-020412 L2TP 知识文档（同域样例）+ 配置树 IPSec/L2TP 特性描述 [EV-FK-01..08]

---

## 4. 配置规则

### 4.1 激活步骤

IPFD-015002 在 UDG 与 UNC 两侧的激活流程**完全对称**（非 C-U 分工），核心步骤如下：

```
步骤1：确认前置条件
  ├── 隧道源端口和目的端口已路由可达（PING 验证）
  ├── 待创建的 GRE 隧道不存在
  └── （可选）若 VPN 组网方式，已创建 VPN 实例

步骤2：配置 LoopBack 接口（推荐隧道源）
  ├── ADD INTERFACE: IFNAME="LoopBack1"
  └── ADD IFIPV4ADDRESS: IFNAME/IPADDR/SUBNETMASK/ADDRTYPE

步骤3：创建 GRE 隧道（★核心使能）
  └── ADD GRETUNNEL: TNLNAME/TNLTYPE=gre/SRCTYPE/SRCIFNAME/DSTIPADDR

步骤4：配置 Tunnel 接口 IP
  └── ADD IFIPV4ADDRESS: IFNAME="Tunnel1"/IPADDR/SUBNETMASK/ADDRTYPE
      注：建议 MOD INTERFACE 配置 MTU ≤ (出接口 MTU - GRE 头长度)
          GRE 头格式 = GRE header + 外层 IP header

步骤5：配置静态路由（引导流量进隧道）
  └── ADD SRROUTE: AFTYPE/PREFIX/MASKLENGTH/IFNAME="Tunnel1"

步骤6：（可选）使能端到端校验
  └── MOD GRETUNNEL: TNLNAME/TNLTYPE/CHECKSUMEN=TRUE

步骤7：（可选）使能识别关键字
  └── MOD GRETUNNEL: TNLNAME/TNLTYPE/GREKEYEN=TRUE/GREKEY="123"
      注：隧道两端必须配置相同 Key，或两端都不配置

步骤8：（可选）使能 Keepalive 检测
  └── MOD GRETUNNEL: TNLNAME/TNLTYPE/KEEPALVEN=TRUE/
                     KEEPALVPERIOD=5（默认）/KEEPALVRETRYCNT=3（默认）
```

> 来源：`激活支持GRE_06422610.md`（"操作步骤"8 步完整流程 + 任务示例脚本）[EV-FK-03]

### 4.2 MML 命令清单

#### 4.2.1 核心配置命令（激活文档，6 条）

| 命令 | 用途 | 本特性角色 |
|------|------|-----------|
| **ADD INTERFACE** | 增加接口 | 创建 LoopBack 接口（推荐隧道源） |
| **ADD IFIPV4ADDRESS** | 增加接口 IPv4 地址 | 配置 LoopBack 接口 IP 与 Tunnel 接口 IP |
| **ADD GRETUNNEL** | 增加 GRE 隧道 | **★本特性核心命令**。创建 GRE 隧道，绑定源/目的地址 |
| **MOD GRETUNNEL** | 修改 GRE 隧道 | 配置 Checksum/Key/Keepalive 等可选特性 |
| **ADD SRROUTE** | 增加静态路由 | 引导流量进入 Tunnel 接口 |
| **MOD INTERFACE** | 修改接口 | 配置 GRE Tunnel 的 MTU（建议 ≤ 出接口 MTU - GRE 头长度） |

> 来源：`激活支持GRE_06422610.md`（"操作步骤" + 任务示例脚本）[EV-FK-03]

#### 4.2.2 去激活命令（1 条）

| 命令 | 用途 | 说明 |
|------|------|------|
| **RMV GRETUNNEL** | 删除 GRE 隧道 | 去激活 GRE；若隧道上仍有报文，将导致业务中断 |

> 来源：`去激活支持GRE_06422612.md`（"操作步骤"）[EV-FK-04]

#### 4.2.3 调测查询命令（4 条）

| 命令 | 用途 |
|------|------|
| **DSP TUNNELINFO** | 显示隧道信息（查隧道状态 UP/DOWN） |
| **LST GRETUNNEL** | 查询 GRE 隧道配置 |
| **LST INTERFACE** | 查询接口配置 |
| **PING** | IP Ping（验证到对端网元连通性） |

> 来源：`调测GRE_06422611.md`（UDG 侧 3 步）、`调测GRE_84704881.md`（UNC 侧 3 步，命令同构）[EV-FK-07, EV-FK-08]

### 4.3 关键参数说明

#### 4.3.1 ADD GRETUNNEL 关键参数（★核心命令）

| 参数 | 取值 | 说明 |
|------|------|------|
| TNLNAME | 字符串（如 "Tunnel1"） | 隧道名称（本端规划） |
| TNLTYPE | gre | 隧道类型，GRE 隧道固定为 gre |
| SRCTYPE | if_name / IP 地址类型 | IPv4 源类型；推荐 if_name（引用 LoopBack 接口） |
| SRCTYPE6 | no_type 等 | IPv6 源类型（IPv6 场景） |
| SRCIFNAME | 接口名（如 "LoopBack1"） | 源接口名称（SRCTYPE=if_name 时指定） |
| SRCIPADDR | IPv4 地址 | 源 IPv4 地址（SRCTYPE 为 IP 地址类型时指定） |
| DSTIPADDR | IPv4 地址（如 "10.4.4.11"） | 目的 IPv4 地址（对端规划） |
| DSTIPV6ADDR | IPv6 地址（如 "2001:db8::100"） | 目的 IPv6 地址（IPv6 场景） |
| CHECKSUMEN | TRUE / FALSE | 使能端到端校验功能（对应 GRE 头 C 位） |
| GREKEYEN | TRUE / FALSE | 使能识别关键字功能（对应 GRE 头 K 位） |
| GREKEY | 字符串（如 "123"） | 识别关键字；隧道两端必须相同，或两端都不配置 |
| KEEPALVEN | TRUE / FALSE | 使能 Keepalive 功能 |
| KEEPALVPERIOD | 数字（默认 5 秒） | Keepalive 报文发送周期（秒） |
| KEEPALVRETRYCNT | 数字（默认 3 次） | 不可达计数器参数（重试次数） |

> 来源：`激活支持GRE_06422610.md`（"必备事项/数据"表 + "操作步骤" + 验证结果样例）[EV-FK-03]

#### 4.3.2 隧道接口 MTU 配置建议

为不影响 GRE 隧道收发报文性能，建议通过 `MOD INTERFACE` 配置 GRE Tunnel 的 MTU 值，该 MTU 值应**小于等于（出接口的 MTU 值 - GRE 头的长度）**。GRE 头封装格式为：**GRE header + 外层 IP header**。

> 来源：`激活支持GRE_06422610.md`（步骤2 说明）[EV-FK-03]

### 4.4 约束条件

| 约束类型 | 约束内容 | 来源 |
|---------|---------|------|
| **嵌套层数限制（★关键）** | GRE 隧道最多两层嵌套，超过两层隧道状态变 Down；禁止大于两层的 GRE 嵌套 | 特性概述"应用限制"章节 |
| **源地址互斥（★关键）** | GRE 隧道源地址不能与 IPSec 隧道源地址相同 | 特性概述"应用限制"章节 |
| **GRE Key 对称性** | 隧道两端设置 Key 时必须相同；或两端都不设置 | 激活文档步骤5 说明 |
| **路由可达性** | 隧道源端口和目的端口必须已路由可达 | 激活文档"必备事项/前提条件" |
| **隧道唯一性** | 待创建 GRE 隧道不能已存在 | 激活文档"必备事项/前提条件" |
| **Recursion 字段** | GRE 报文头 Recursion 字段大于 3 丢弃（防无限封装） | GRE 报文格式文档 |
| **去激活业务中断** | 去激活时若隧道上仍有报文，将导致业务中断 | 去激活文档"对系统的影响" |
| **规格限制** | 整个系统最大支持配置 4k 个 GRE Tunnel 接口 | 特性概述"特性规格"章节 |
| **MTU 配置建议** | GRE Tunnel MTU 应 ≤（出接口 MTU - GRE 头长度） | 激活文档步骤2 说明 |

---

## 5. 配置案例

### 5.1 典型场景：GRE 隧道建立（IPv4，端到端校验 + Key + Keepalive）

**场景描述**：本端设备（UDG 或 UNC）与对端设备之间通过公网建立 GRE 隧道。本端 LoopBack1 源 IP 为 10.3.3.11/32，对端目的 IP 为 10.4.4.11；Tunnel1 接口本端 IP 为 10.10.1.201/24，对端为 10.10.1.202/24。启用端到端校验、识别关键字（GREKEY="123"）、Keepalive（周期 5s，重试 3 次）。

**配置步骤和 MML 命令序列**（保留原始 MML）：

```
=== 本端 GRE 隧道配置 ===

// 创建 LoopBack 接口，并配置 IP 地址 10.3.3.11/32。
ADD INTERFACE:IFNAME="LoopBack1";
ADD IFIPV4ADDRESS:IFNAME="LoopBack1", IFIPADDR="10.3.3.11", SUBNETMASK="255.255.255.255", ADDRTYPE=main;

// 创建 Tunnel 接口，并配置 IP 地址 10.10.1.201/24。
ADD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, SRCTYPE=if_name, SRCIFNAME="LoopBack1", DSTIPADDR="10.4.4.11";
ADD IFIPV4ADDRESS:IFNAME="Tunnel1", IFIPADDR="10.10.1.201", SUBNETMASK="255.255.255.0", ADDRTYPE=main;

// 增加隧道间静态路由。
ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.10.1.202",MASKLENGTH=24,IFNAME="Tunnel1";

// 使能隧道端到端校验功能。
MOD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, CHECKSUMEN=TRUE;

// 使能隧道识别关键字功能。
MOD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, GREKEYEN=TRUE, GREKEY="123";

// 使能隧道 Keepalive 功能。
MOD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, KEEPALVEN=TRUE, KEEPALVPERIOD=5, KEEPALVRETRYCNT=3;

=== 对端 GRE 隧道配置 ===

// 创建 LoopBack 接口，并配置 IP 地址 10.4.4.11/32。
ADD INTERFACE:IFNAME="LoopBack1";
ADD IFIPV4ADDRESS:IFNAME="LoopBack1", IFIPADDR="10.4.4.11", SUBNETMASK="255.255.255.255", ADDRTYPE=main;

// 创建 Tunnel 接口，并配置 IP 地址 10.10.1.202/24。
ADD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, SRCTYPE=if_name, SRCIFNAME="LoopBack1", DSTIPADDR="10.3.3.11";
ADD IFIPV4ADDRESS:IFNAME="Tunnel1", IFIPADDR="10.10.1.202", SUBNETMASK="255.255.255.0", ADDRTYPE=main;

// 增加隧道间静态路由。
ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.10.1.201",MASKLENGTH=24,IFNAME="Tunnel1";

// 使能隧道端到端校验功能。
MOD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, CHECKSUMEN=TRUE;

// 使能隧道识别关键字功能。
MOD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, GREKEYEN=TRUE, GREKEY="123";

// 使能隧道 Keepalive 功能。
MOD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, KEEPALVEN=TRUE, KEEPALVPERIOD=5, KEEPALVRETRYCNT=3;
```

> 来源：`激活支持GRE_06422610.md`（"任务示例/脚本"完整原文，本端+对端对称）[EV-FK-03]

### 5.2 场景变体

| 变体 | 场景说明 | 核心差异 | 文档覆盖度 |
|------|---------|---------|-----------|
| IPv4 基础 GRE 隧道 | 异种网络互通 / VPN 组建 | DSTIPADDR + LoopBack1 源 | 完整 MML 脚本（场景 5.1） |
| IPv6 GRE 隧道 | IPv6 场景 | DSTIPV6ADDR + SRCTYPE6 | 数据表参数覆盖，无独立脚本 |
| 双栈 GRE 隧道 | IPv4+IPv6 共存 | 同时配置 v4/v6 参数 | 参数说明覆盖 |
| 端到端校验 | Checksum 校验 | CHECKSUMEN=TRUE | 场景 5.1 步骤6 |
| 识别关键字 | GRE Key 验证 / 多租户区分 | GREKEYEN=TRUE + GREKEY | 场景 5.1 步骤7 |
| Keepalive 检测 | 链路状态防黑洞 | KEEPALVEN=TRUE + 周期/重试 | 场景 5.1 步骤8 |
| 多租户共享 | 同源同宿多隧道 + Key 区分 | 多条 ADD GRETUNNEL，不同 GREKEY | 多租户文档原理覆盖，无独立脚本 |
| GRE over IPSec | GRE 封装 + IPSec 加密叠加 | 先建 GRE，再叠加 IPSec（IPFD-015004/016000） | IPSec 激活文档"GRE over IPSec"场景 |
| 两层嵌套 | GRE 嵌套 GRE | 内层 GRE Tunnel 出接口为外层 GRE Tunnel | 应用限制提及（≤2 层），无独立脚本 |
| Radius 带内/带外组网 | UNC 到 AAA Server 穿越 | UNC 侧 GRE VPN 组网到 AAA | WSFD-011306 激活文档场景 |

---

## 6. 验证与调测

### 6.1 验证方法

#### 6.1.1 调测前提与目的

GRE 调测用于校验本局与对端设备的 GRE 隧道能否正常工作以及数据配置是否正确，以 GRE 隧道功能的正常运行。

> 适用：UDG（`调测GRE_06422611.md`）与 UNC（`调测GRE_84704881.md`），两侧调测流程完全同构

#### 6.1.2 调测数据准备

| 类别 | 参数 | 取值样例 | 获取方法 |
|------|------|---------|---------|
| 目的端 IP 地址 | 目的 IPv4 地址（DESTIPV4ADDRESS） | 10.4.4.11 | LST GRETUNNEL 查询 |
| 目的端 IP 地址 | 目的 IPv6 地址（DESTIPV6ADDRESS） | 2001:db8::100 | LST GRETUNNEL 查询 |

> 来源：`调测GRE_06422611.md`（UDG 侧）、`调测GRE_84704881.md`（UNC 侧）[EV-FK-07, EV-FK-08]

#### 6.1.3 调测执行步骤（UDG/UNC 通用，3 步）

```
步骤1：查看 GRE 隧道状态
  └── DSP TUNNELINFO
      ├── 预期：隧道状态 UP → 步骤2
      └── 异常：隧道状态 DOWN → 参见"GRE 隧道故障处理定位思路"

步骤2：Ping 对端网元验证连通性
  └── PING: IPVERSION=IPv4, DESTIPV4ADDRESS="10.4.4.11"
      ├── 预期：收到对端响应（0% 丢包）→ 调测结束
      └── 异常：无响应 → 参见"GRE 隧道故障处理定位思路"

步骤3：检查 GRE 隧道配置
  ├── LST INTERFACE: IFNAME="接口名"
  └── LST GRETUNNEL: TNLNAME="隧道名称"
      预期：查询结果与规划值一致
```

**LST GRETUNNEL 典型输出**：

```
             隧道名称  =  Tunnel1
             隧道类型  =  GRE隧道
           IPv4源类型  =  IP地址
           IPv6源类型  =  无类型
           源IPv4地址  =  10.3.3.11
         目的IPv4地址  =  10.4.4.11
           源IPv6地址  =  ::
         目的IPv6地址  =  ::
    使能Keepalive功能  =  TRUE
Keepalive报文发送周期  =  5
     不可达计数器参数  =  3
           源接口名称  =  NULL
          目的VPN名称  =  _public_
   使能识别关键字功能  =  去使能
           识别关键字  =  *****
   使能端到端校验功能  =  FALSE
     使能报文统计功能  =  FALSE
     使能备份隧道功能  =  FALSE
```

> 来源：`激活支持GRE_06422610.md`（"验证方法" + 输出样例）、`调测GRE_06422611.md`/`调测GRE_84704881.md`（3 步流程）[EV-FK-03, EV-FK-07, EV-FK-08]

### 6.2 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| GRE 隧道状态 DOWN | 嵌套超过两层 | 检查是否存在大于两层的 GRE 嵌套；减少嵌套层数 |
| GRE 隧道状态 DOWN | 源/目的地址路由不可达 | DSP TUNNELINFO 查状态；PING 验证源到目的连通性；检查路由 |
| GRE 隧道状态 DOWN | 源地址与 IPSec 源地址相同 | 核对 GRE 与 IPSec 源地址规划；修改使其不同 |
| 数据黑洞（隧道看似 UP 但报文丢弃） | 未启用 Keepalive，对端实际不可达 | MOD GRETUNNEL KEEPALVEN=TRUE；检查 Keepalive 计数 |
| 隧道两端 Key 不匹配 | 一端配 Key 一端不配，或 Key 值不同 | LST GRETUNNEL 核对 GREKEYEN/GREKEY；两端必须相同或都不配 |
| Ping 不通对端 | Tunnel 接口路由缺失 | LST INTERFACE + DSP ROUTE；ADD SRROUTE 补充路由 |
| MTU 导致大包丢弃 | Tunnel 接口 MTU 过大 | MOD INTERFACE 配置 MTU ≤（出接口 MTU - GRE 头长度） |
| 去激活后业务中断 | 去激活时隧道仍有报文 | 业务低峰期去激活；先切换流量再 RMV GRETUNNEL |
| 多租户流量串隧道 | GRE Key 配置错误或静态路由指向错误 Tunnel | 核对每租户 GREKEY 与 SRROUTE 出接口一致性 |

---

## 7. 参考信息

### 7.1 与其他特性的关系

| 关联特性 | 特性ID | 关系说明 |
|---------|--------|---------|
| VPN 功能（配置树父节点） | IPFD-015000 | 配置树父节点（接入方式类） |
| **支持 OSPF** | IPFD-014001（UDG/UNC 共用） | **协同**：源端和目的端必须存在经 Tunnel 转发的路由，可通过 OSPF 获得 |
| **IPSec 功能（UDG）** | IPFD-015004 | **源地址互斥 + 组合**：GRE 源地址不能与 IPSec 源地址相同；可组合为"GRE over IPSec" |
| **IPSec 功能（UNC）** | IPFD-016000 | 同上（UNC 侧 IPSec） |
| L2TP VPN（UDG） | GWFD-020412 | **隧道方案矩阵**：GRE 为三层轻量隧道，L2TP 为二层 PPP 隧道（含远程地址分配）；并列可选方案 |
| L2TP VPN（UNC） | WSFD-104410 | 同上（UNC 侧 L2TP） |
| MPLS VPN（UDG/UNC） | GWFD-020411 / WSFD-104411 | **隧道方案矩阵**：GRE 为 IP 隧道，MPLS VPN 为标签隧道；并列可选方案 |
| Radius 功能（UNC） | WSFD-011306 | **应用场景协同**：UNC 到 AAA Server 的带内/带外组网使用 GRE VPN 穿越 |
| 地址分配方式 | GWFD-010104 / WSFD-010502 | **职责分离**：GRE 不参与用户地址分配，与本地/L2TP/Radius 等地址分配方式无直接配置交互 |
| 用户面地址自动检测 | GWFD-010108 | 与 L2TP 互斥，但与 GRE 无直接互斥声明 |

### 7.2 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 产品 | 主要贡献内容 |
|------|---------|------|-------------|
| 1 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015000 VPN功能/IPFD-015002 GRE/特性配置/调测GRE_06422611.md` | UDG | UDG 侧 GRE 调测流程（3 步：DSP TUNNELINFO 查状态 → PING 验证连通性 → LST INTERFACE + LST GRETUNNEL 查配置）、调测数据表（DESTIPV4ADDRESS/DESTIPV6ADDRESS）、PING 示例输出 |
| 2 | `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-015002 GRE/IPFD-015002 GRE特性概述_61317365.md` | UNC | **★特性定义**（GRE 通用路由封装，可作 VPN 第三层隧道）、客户价值（性能要求低）、应用场景（异种网络互通/扩大跳数范围/连接不连续子网组 VPN）、可获得性（UNC 20.0.0+，**无需 License**）、与其他特性交互（OSPF 协同）、对系统影响（无）、**应用限制（两层嵌套/源地址与 IPSec 互斥）**、原理概述（封装/解封装 + 协议号 47）、计费话单（无）、**特性规格（4k Tunnel）**、遵循标准（RFC 1701/1702/2784）、发布历史（v01 20.0.0） |
| 3 | `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-015002 GRE/实现原理/GRE报文格式_61317188.md` | UNC | GRE 封装格式（净荷/乘客协议/封装协议/传输协议）、GRE 报文头字段（C/K/Recursion/Flags/Version/Protocol Type/Checksum/Key）、Recursion 嵌套层数说明（UNC 仅加封装时标记，解封装不感知）、源路由字段置 0 说明 |
| 4 | `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-015002 GRE/实现原理/Keepalive检测_61317267.md` | UNC | Keepalive 检测产生原因（GRE 无链路状态检测，防止数据黑洞）、实现过程（定时器周期发送探测报文 + 不可达计数 + 重试次数默认 3）、**单端配置特性**（对端无论是否配置 Keepalive 都会回应） |
| 5 | `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-015002 GRE/实现原理/多租户共享GRE隧道_61317217.md` | UNC | 多租户共享 GRE 隧道功能（同源同宿多隧道）、客户价值（节约公网 IP）、应用场景、实现原理（**GRE Key 区分租户** + 静态路由引入对应隧道）、入隧道/出隧道转发流程 |
| 6 | `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-015002 GRE/特性配置/去激活支持GRE_06422612.md` | UNC | 去激活场景（RMV GRETUNNEL）、对系统影响（隧道有报文时去激活导致业务中断）、前提条件（隧道已建立） |
| 7 | `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-015002 GRE/特性配置/激活支持GRE_06422610.md` | UNC | **★激活完整流程**（8 步：LoopBack→GRETUNNEL→Tunnel IP→SRROUTE→Checksum→Key→Keepalive）、必备数据表（12 个参数覆盖 4 条命令）、**MTU 配置建议**（≤ 出接口 MTU - GRE 头长度）、Key 对称性约束、Keepalive 默认值（周期 5s/重试 3 次）、完整 MML 脚本（本端+对端对称）、LST GRETUNNEL 输出样例 |
| 8 | `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/IP基本功能/IPFD-015002 GRE/特性配置/调测GRE_84704881.md` | UNC | UNC 侧 GRE 调测流程（3 步，与 UDG 侧同构）、调测数据表、PING 示例输出 |

### 7.3 关键术语速查

| 术语 | 全称 | 说明 |
|------|------|------|
| GRE | Generic Routing Encapsulation | 通用路由封装协议，三层隧道封装 |
| GRETUNNEL | GRE 隧道对象 | ★本特性核心配置对象（ADD/MOD/RMV/LST GRETUNNEL） |
| Tunnel 接口 | 隧道虚拟接口 | GRE 隧道端点接口，需配 IP（ADD IFIPV4ADDRESS） |
| LoopBack 接口 | 环回接口 | 推荐作为 GRE 隧道源，提供稳定源 IP |
| GRE Key | 关键字字段 | 隧道验证 + 多租户区分标签 |
| Checksum | 校验和 | 端到端校验（CHECKSUMEN） |
| Keepalive | 链路检测 | 防数据黑洞（KEEPALVEN/PERIOD/RETRYCNT） |
| Recursion | 嵌套层数 | GRE 报文字段，>3 丢弃，实际限制两层嵌套 |
| 协议号 47 | GRE 协议号 | 外层 IP 头协议字段值 |
| SRCTYPE | 源类型 | if_name（接口名）/ IP 地址类型 |
| SRROUTE | 静态路由 | 引导流量进入 Tunnel 接口 |
| 4k 规格 | GRE Tunnel 数量上限 | 整系统最大 4096 个 GRE Tunnel 接口 |

---

## 8. 文档一致性说明（配置树 vs 产品文档）

> 配置树仅用于定位特性 ID，以下记录以产品文档实际内容为准时发现的差异与协同点，供 Stage 3 横向分析参考。

### 8.1 与任务要求中提及对象的核对（★重点澄清）

| # | 任务要求提及 | 产品文档实际 | 核对结论 |
|---|-------------|-------------|---------|
| 1 | **GRE 隧道机制（轻量封装不加密）** | **确认**：GRE 定义为"通用路由封装协议"，仅对报文加 GRE 头 + 外层 IP 头，**不加密、不鉴权**；产品文档明确"对系统无影响"，"对设备的性能的要求较低" | 已覆盖（见 §1.1、§3.1、§3.6） |
| 2 | **UDG（U 面）与 UNC（C 面）的配置分工** | **★关键发现**：GRE 两侧**非 C-U 分工型，而是双产品同构部署**。UDG 和 UNC 的 GRE 命令、对象、激活/调测步骤完全对称（均为 ADD GRETUNNEL + LoopBack + Tunnel 接口 + SRROUTE）。这与 L2TP（C 决策/U 执行）形成鲜明对比 | **澄清**：GRE 在 C/U 两侧对称同构，无分工差异；任务要求中"配置分工"表述对 GRE 不适用，需修正为"双产品对称部署" |
| 3 | **规格限制（4k 隧道/两层嵌套）** | **确认**：特性规格明确"整个系统最大支持配置 GRE Tunnel 接口数量 4k（4096）"；应用限制明确"最多支持两层嵌套，超过两层隧道状态变 Down"；Recursion 字段 >3 丢弃 | 已覆盖（见 §1.10、§1.11） |
| 4 | **与 IPSec（015004/016000）的隧道对比** | **确认**：GRE 与 IPSec 存在两层关系——(a) 源地址互斥（不能相同）；(b) 组合关系（GRE over IPSec 场景，先 GRE 封装再 IPSec 加密）。IPSec 激活文档存在"GRE over IPSec"专门场景 | 已覆盖（见 §1.6、§3.6） |
| 5 | **与 L2TP（020412/104410）的隧道对比** | **确认**：GRE 为三层轻量隧道（不加密、不分配地址、C-U 对称），L2TP 为二层 PPP 隧道（LNS 远程分配地址、C-U 分工、UDG 必须 License）。两者属并列可选的隧道方案，无直接互斥声明 | 已覆盖（见 §3.6） |
| 6 | **GRE 配置对象与命令（文档依据）** | **确认**：核心对象为 **GRETUNNEL**（ADD/MOD/RMV/LST GRETUNNEL），辅以 LoopBack 接口（ADD INTERFACE + ADD IFIPV4ADDRESS）、Tunnel 接口 IP（ADD IFIPV4ADDRESS）、静态路由（ADD SRROUTE）、去激活（RMV GRETUNNEL）。共 6 条核心配置命令 + 1 条去激活命令 + 4 条调测查询命令 | 已覆盖（见 §4.2） |

### 8.2 与配置树/文档清单的差异

| # | 维度 | 配置树/文档清单描述 | 产品文档实际内容 | 差异类型 |
|---|------|---------------------|-----------------|---------|
| 1 | 文件数与分布 | 文档清单列 8 个文件（1 UDG + 7 UNC） | 实际 UDG 仅 1 个调测文档（调测GRE_06422611.md），UNC 7 个文档（特性概述+3 实现原理+激活+去激活+调测）；**UDG/UNC 文档密度不对称**（UDG 仅调测，UNC 覆盖完整） | 补全：UDG 侧特性概述/原理/激活文档未在清单中列出，但调测文档命令路径与 UNC 同构（LST GRETUNNEL 等） |
| 2 | License 要求 | 文档清单标注"[★核心]" | 产品文档明确声明"**无需 License**"（UDG/UNC 两侧均无） | 澄清：GRE 无 License，区别于 L2TP（必须 License）和 IPSec（需 License） |
| 3 | C-U 分工 | 任务要求暗示"C-U 分工" | 实际为**双产品对称同构**，两侧命令、对象、步骤完全一致 | 澄清：GRE 非 C-U 分工型，与 L2TP 的 C-U 分工模式不同 |
| 4 | 嵌套与源地址限制 | 文档清单简述"轻量封装不加密，最多两层嵌套" | 产品文档明确两条应用限制：(a) 两层嵌套上限；(b) **GRE 源地址与 IPSec 源地址互斥**（清单未提及） | 补全：清单遗漏源地址互斥约束 |
| 5 | 多租户共享子特性 | 文档清单未提及 | UNC 侧存在独立文档"多租户共享 GRE 隧道"，以 GRE Key 区分租户 | 补全：清单遗漏多租户场景 |
| 6 | 与父节点关系 | 配置树父节点为 IPFD-015000 VPN 功能 | 本特性 8 篇文档**未直接提及** IPFD-015000 | 推断关系，Stage 3 验证 |
| 7 | Radius 组网场景 | 文档清单未提及 | WSFD-011306 Radius 功能激活文档存在"带内/带外组网 GRE VPN"场景（UNC 到 AAA Server 穿越） | 补全：跨特性应用场景 |

### 8.3 与同域隧道特性的横向对比（★Stage 3 重点）

| # | 维度 | IPFD-015002 GRE | IPFD-015004/016000 IPSec | GWFD-020412/WSFD-104410 L2TP |
|---|------|----------------|--------------------------|------------------------------|
| 1 | 隧道层级 | 三层（IP 封装） | 三层（IP 加密） | 二层（PPP 封装） |
| 2 | 加密 | 无 | 有（AH/ESP） | 无 |
| 3 | 鉴权 | 无（可选 Key） | 有（IKE/证书） | 有（PAP/CHAP） |
| 4 | 地址分配 | 不涉及 | 不涉及 | LNS 远程分配 |
| 5 | License | 无 | 有 | UDG 必须（82200BVC） |
| 6 | C-U 模式 | **对称同构** | 各自配置 | **C-U 分工** |
| 7 | 规格 | 4k Tunnel | （IPSec 激活文档覆盖） | L2TP Group 1500×2 |
| 8 | 性能影响 | 无 | 有（加密开销） | 有（封装+激活时延） |
| 9 | 互斥关系 | 与 IPSec 源地址互斥 | - | 与地址自动检测、入不转板互斥 |
| 10 | 典型 NF 角色 | PE 设备（两侧） | IPSec 端点（两侧） | UDG 作 LAC，LNS 在企业网 |
| 11 | 标准 | RFC 1701/1702/2784 | RFC AH/ESP/IKE 系列 | RFC 2661/2868/5072/5571/8064 |
| 12 | Keepalive | 5s 周期，3 次重试 | IKE DPD | Hello 60s，3 次重发 |

---

## 附录 A：source_evidence_ids 占位映射

| evidence_id | 对应来源文件 | 主要贡献章节 |
|-------------|-------------|-------------|
| EV-FK-01 | `IPFD-015002 GRE特性概述_61317365.md`（UNC） | 特性定义、客户价值、应用场景、可获得性（UNC 20.0.0+，无 License）、与其他特性交互（OSPF 协同）、对系统影响（无）、**应用限制（两层嵌套 + 源地址与 IPSec 互斥）**、原理概述（封装/解封装 + 协议号 47）、特性规格（4k Tunnel）、遵循标准（RFC 1701/1702/2784）、发布历史 |
| EV-FK-02 | `实现原理/GRE报文格式_61317188.md`（UNC） | GRE 封装格式（净荷/乘客/封装/传输协议）、GRE 报文头字段（C/K/Recursion/Flags/Version/Protocol Type/Checksum/Key）、Recursion 嵌套层数实现说明 |
| EV-FK-03 | `特性配置/激活支持GRE_06422610.md`（UNC） | ★激活完整 8 步流程、必备数据表（12 参数）、MTU 配置建议、Key 对称性约束、Keepalive 默认值、完整 MML 脚本（本端+对端）、LST GRETUNNEL 输出样例 |
| EV-FK-04 | `特性配置/去激活支持GRE_06422612.md`（UNC） | 去激活场景（RMV GRETUNNEL）、业务中断影响、前提条件 |
| EV-FK-05 | `实现原理/Keepalive检测_61317267.md`（UNC） | Keepalive 产生原因（防数据黑洞）、实现过程（定时器+计数+重试）、单端配置特性 |
| EV-FK-06 | `实现原理/多租户共享GRE隧道_61317217.md`（UNC） | 多租户共享功能（同源同宿多隧道）、GRE Key 区分租户、入/出隧道转发流程、节约公网 IP 价值 |
| EV-FK-07 | `特性配置/调测GRE_84704881.md`（UNC） | UNC 侧 GRE 调测 3 步流程、调测数据表、PING 示例输出 |
| EV-FK-08 | `特性配置/调测GRE_06422611.md`（UDG） | UDG 侧 GRE 调测 3 步流程（与 UNC 同构）、调测数据表、PING 示例输出、确认 UDG/UNC 命令对称性 |
