# GWFD-020412 L2TP VPN 知识文档

> 聚焦 APN 业务域地址分配场景的 UDG（PGW-U/UPF）用户面 L2TP VPN 特性
> 与 UNC 侧 WSFD-104410（控制面 L2TP 决策与 LNS 参数下发）构成 C-U 协同分工
> 适用 NF：PGW-U（4G）、UPF（5G）
> C-U 对称对端：WSFD-104410（UNC/SMF）

---

## 0. 元数据（三层图谱Schema字段）

| 字段 | 取值 |
|------|------|
| feature_id | GWFD-020412 |
| feature_name | L2TP VPN |
| feature_group | 地址分配 |
| parent_feature_id | GWFD-010104（地址分配方式，配置树父节点，推断） |
| applicable_nf_map | `{"UDG": ["PGW-U", "UPF"]}` |
| variant_dimensions | ["LNS参数来源(本地配置L2TP Group / AAA Server Access-Accept下发)", "LNS工作模式(REDUNDANCY主备 / LOAD_SHARING负荷分担 / RADIUS Tunnel-Preference)", "接入代际(4G / 5G)", "用户IP类型(IPv4 / IPv6 / IPv4v6双栈)", "内层PPP鉴权(PAP / CHAP / 不鉴权)", "N4接口L2TP私有信元加密(明文 / SET L2TPN4KEY加密)"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-01, EV-FK-02, EV-FK-03, EV-FK-04, EV-FK-05, EV-FK-06, EV-FK-07, EV-FK-08, EV-FK-09, EV-FK-10, EV-FK-11, EV-FK-12, EV-FK-13, EV-FK-14, EV-FK-15] |
| license_required | 必须 License `82200BVC LKV3G5L2TP01 L2TP VPN` |

---

## 1. 概述

### 1.1 特性定义（是什么）

利用 L2TP（Layer 2 Tunneling Protocol，二层隧道协议）在 UDG 与企业网的边缘设备 LNS（L2TP Network Server）之间建立 L2TP VPN，用户可以从固网、移动网等公共网络远程接入到企业的虚拟专用网。

本特性是**用户面（U 面）L2TP 隧道执行与 PPP 再生特性的总集**：UDG（PGW-U/UPF）作为 LAC（L2TP Access Concentrator），解 GTP 封装后获得原始 IP 报文，为 IP 报文添加 PPP 封装，通过与企业网之间建立的二层 L2TP 隧道将 PPP 报文发送到企业网 LNS；LNS 完成 L2TP 解封装并通过内层 PPP 三阶段协商（LCP → PAP/CHAP 鉴权 → IPCP/IPv6CP）为 UE 分配企业内网 IP 地址。与 UNC 侧 WSFD-104410（控制面 LNS 参数决策与下发）形成 C-U 协同分工：C 面"决策+下发 LNS 参数"，U 面"LAC 封装隧道+PPP 协商透传"。

> 来源：`output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/GWFD-020412 L2TP VPN特性概述_40342127.md`（"定义/原理概述"章节）[EV-FK-01]

### 1.2 适用NF（UDG/UNC网元）

| 涉及NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| PGW-U / UPF | 用户面（UDG） | UDG 20.3.2 及后续版本 | UDG 作为 LAC 与 LNS 之间构建 L2TP 隧道，并封装/解封装 L2TP 报文；完成 PPP 协商透传 |
| PGW-C / SMF（可选） | 控制面（UNC） | UNC 20.3.2 及后续版本 | **非本特性主体 NF**，但可以通过 AAA Server 对 L2TP 用户鉴权并将 AAA Server 返回的 LNS 信息下发到 PGW-U/UPF（详见 WSFD-104410） |
| LNS | 企业网边缘设备 | 无特殊要求 | LNS 封装/解封装 L2TP 报文，作为 L2TP 隧道服务器端 |

> 来源：`GWFD-020412 L2TP VPN特性概述_40342127.md`（"可获得性/涉及NF"章节）[EV-FK-01]

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|---------|---------|---------|
| 03 | 20.12.0 | 第三次发布，UDG 和 LNS 之间的 L2TP 隧道支持 IPv6 地址 |
| 02 | 20.6.0 | 第二次发布，L2TP 支持 IPv6 用户接入 |
| 01 | 20.3.2 | 首次发布 |

> 来源：`GWFD-020412 L2TP VPN特性概述_40342127.md`（"发布历史"章节）[EV-FK-01]

### 1.4 License

本特性必须获得 License 许可后才能使用，对应的 License 控制项为：

| License编号 | License名称 |
|------------|------------|
| 82200BVC | LKV3G5L2TP01 L2TP VPN |

激活时需通过 `SET LICENSESWITCH: LICITEM="LKV3G5L2TP01", SWITCH=ENABLE` 打开 License 配置开关。

> 来源：`GWFD-020412 L2TP VPN特性概述_40342127.md`（"可获得性/License支持"章节）、`本地配置方式激活L2TP VPN_40342129.md`（步骤1）[EV-FK-01, EV-FK-03]

### 1.5 前置条件与依赖

| 前置条件 | 说明 |
|---------|------|
| 企业网侧部署 LNS | **应用限制硬约束**：企业网侧必须部署 LNS 设备（否则 L2TP 隧道无法终结） |
| 已加载 License | 必须加载 License 控制项 `82200BVC LKV3G5L2TP01 L2TP VPN` 并通过 `SET LICENSESWITCH` 打开开关 |
| 已配置 APN | `SET APNL2TPATTR` 命令的 APN 参数必须已通过 `ADD APN` 命令配置完成 |
| UDG 与 LNS 物理链路连通 | 调测前置条件，需通过 PING 命令验证 |
| LNS 侧已配置 L2TP 隧道及回程路由 | 调测前置条件 |
| C-U 版本对齐 | UNC 与 UDG 均需 20.3.2 及后续版本 |

> 来源：`GWFD-020412 L2TP VPN特性概述_40342127.md`（"应用限制"章节）、`本地配置方式激活L2TP VPN_40342129.md`（"必备事项/前提条件"）、`调测基于本地配置方式激活的L2TP VPN_40342150.md`（"必备事项/前提条件"）[EV-FK-01, EV-FK-03, EV-FK-08]

### 1.6 与其他特性的交互

| 交互类型 | 相关特性 | 控制项名称 | 交互说明 |
|---------|---------|-----------|---------|
| **互斥** | GWFD-010108 用户面地址自动检测 | 无 | L2TP VPN 不支持与用户面地址自动检测功能同时应用 |
| **互斥** | GWFD-020482 入不转板功能 | 无 | APN 下开启 L2TP VPN 特性，则不支持入不转板功能 |

> 来源：`GWFD-020412 L2TP VPN特性概述_40342127.md`（"与其他特性的交互"章节）[EV-FK-01]

### 1.7 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | 通过公网将远程企业用户接入到企业网，不需要建设专有网络，降低了运营商的建网成本 |
| 用户 | 企业用户可以通过公网接入企业网，节约了企业的网络使用费用 |

> 来源：`GWFD-020412 L2TP VPN特性概述_40342127.md`（"客户价值"章节）[EV-FK-01]

### 1.8 应用场景

企业驻外机构和出差人员可远程经由公共网络，通过虚拟隧道实现和企业总部之间的网络连接，从而为企业、小型 ISP（Internet Service Provider）、移动办公人员等提供接入服务。

> 来源：`GWFD-020412 L2TP VPN特性概述_40342127.md`（"应用场景"章节）[EV-FK-01]

### 1.9 对系统的影响

- 该特性增加了和 LNS 的交互及处理，**用户激活时延有所增加，用户激活速率有所降低**
- 该特性对用户面报文增加了 L2TP 封装，**对性能有一定影响**，详细性能影响需联系华为技术支持获取

> 来源：`GWFD-020412 L2TP VPN特性概述_40342127.md`（"对系统的影响"章节）[EV-FK-01]

### 1.10 应用限制

- **企业网侧必须部署 LNS 设备**
- **不支持 PPP 用户接入**
- L2TP 用户接入时，**不支持 DHCP 延迟分配 IPv4 地址**
- L2TP 用户接入时，**不支持 IPv6 Prefix Delegation 地址分配方式**
- **不支持 UDG 与 LNS 协商 PFC 和 ACFC 字段压缩流程**
- **该功能不支持 NAT 地址转换**
- NP 加速场景下，**L2TP VPN 特性不支持 IPv6**
- L2TP 场景下需要**关闭快速流表功能**（设置 Byte671 的 bit7 为 1），否则可能在快速流表场景下导致报文被丢弃

> 来源：`GWFD-020412 L2TP VPN特性概述_40342127.md`（"应用限制"章节）、`本地配置方式激活L2TP VPN_40342129.md`（步骤6）[EV-FK-01, EV-FK-03]

### 1.11 特性规格

| 规格名称 | 规格指标 |
|---------|---------|
| 本地 L2TP Group 规格 | 1500 |
| AAA 下发方式下的 L2TP Group 规格 | 1500 |

> 来源：`GWFD-020412 L2TP VPN特性概述_40342127.md`（"特性规格"章节）[EV-FK-01]

### 1.12 计费与话单

**本特性不涉及计费与话单**。

> 来源：`GWFD-020412 L2TP VPN特性概述_40342127.md`（"计费与话单"章节）[EV-FK-01]

### 1.13 遵循标准

| 标准类别 | 标准名称 |
|---------|---------|
| 3GPP | 3GPP TS 23.214 Architecture enhancements for control and user plane separation of EPC nodes |
| 3GPP | 3GPP TS 29.244 Interface between the Control Plane and the User Plane of EPC Nodes |
| RFC | RFC 2661 Layer Two Tunneling Protocol |
| RFC | RFC 2868 RADIUS Attributes for Tunnel Protocol Support |
| RFC | RFC 5072 IP Version 6 over PPP |
| RFC | RFC 5571 Softwire Hub and Spoke Deployment Framework with Layer Two Tunneling Protocol Version 2 (L2TPv2) |
| RFC | RFC 8064 Recommendation on Stable IPv6 Interface Identifiers |

> 来源：`GWFD-020412 L2TP VPN特性概述_40342127.md`（"遵循标准"章节）[EV-FK-01]
> 注：UDG 侧引用 7 条标准（含 L2TP 协议族 RFC 2661/5571、RADIUS 隧道属性 RFC 2868、PPP IPv6 RFC 5072、稳定 IID RFC 8064），UNC 侧 WSFD-104410 仅引用 CUPS 标准 23.214/29.244；C-U 标准互补。

---

## 2. 核心概念

### 2.1 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| L2TP | Layer 2 Tunneling Protocol，二层隧道协议 | 由 IETF 起草，结合 PPTP 和 L2F 优点，为众多公司接受并已成为标准 RFC；既可用于拨号 VPN，也可用于专线 VPN |
| VPDN | Virtual Private Dial-up Network，虚拟私有拨号网 | 利用公共网络的拨号功能接入，实现 VPN |
| LNS | L2TP Network Server，L2TP 网络服务器 | PPP 端系统上用于处理 L2TP 协议的服务器端设备，通常是企业网的边缘设备；通过 LNS 验证用户可登录私网 |
| LAC | L2TP Access Concentrator，L2TP 访问集中器 | 附属在交换网络上的具有 PPP 端系统和 L2TP 协议处理能力的设备；UDG 作为 LAC，为 UE 提供接入服务 |
| PPP | Point-to-Point Protocol，点对点协议 | TCP/IP 协议栈数据链路层协议，在点对点链路上传输网络层协议报文；包括 LCP、验证协议族（CHAP/PAP）、网络控制协议族（NCP，如 IPCP/IPv6CP） |
| LCP | Link Control Protocol，链路控制协议 | PPP 协议族，用于建立、拆除和监控 PPP 数据链路；协商 MRU、鉴权类型等 |
| IPCP | IP Control Protocol | PPP 网络控制协议，用于 IPv4 地址协商；L2TP 用户 IPv4 地址由 LNS 在 IPCP 阶段分配 |
| IPv6CP | IPv6 Control Protocol | PPP 网络控制协议，用于 IPv6 接口 ID 协商；IPv6 地址 = 网络前缀（LNS 通过 RA 下发）+ 接口 ID |
| PAP | Password Authentication Protocol | 两次握手鉴权协议，明文传输用户名和口令，安全性较低 |
| CHAP | Challenge-Handshake Authentication Protocol | 三次握手鉴权协议，只传输用户名不传口令，安全性较高 |
| 隧道（Tunnel） | L2TP Tunnel | 由一个控制连接和一个或多个会话连接组成；同一对 LAC 和 LNS 之间可建立多个 L2TP 隧道 |
| 会话（Session） | L2TP Session | 复用在控制连接之上，每个会话对应 LAC 和 LNS 之间的一个 PPP 数据流 |
| APNL2TPATTR | APN L2TP 属性 | **本特性核心配置对象**，按 APN 粒度配置 L2TP 使能、IPv6 支持、L2TP 组绑定、ICRQ/ICCN 信元、IPCP 协商等 |
| L2TPGROUP | L2TP 组 | 本地配置方式下的 LNS 容器；绑定域名、LNS 服务器、VPN 实例、HELLO 参数等；在 LAC 和 LNS 上独立编号 |
| L2TPKEY / L2TPN4KEY | N4 接口 L2TP 加密密钥 | 控制 N4 接口 L2TP 私有信元的加密；UNC 侧 `SET L2TPKEY`，UDG 侧 `SET L2TPN4KEY`，两端需配置相同密钥 |

> 来源：`相关术语/L2TP_51067102.md`、`相关术语/LAC_51067103.md`、`相关术语/LNS_51067104.md`、`相关术语/PPP协议_51525531.md`、`GWFD-020412 L2TP VPN参考信息_40342151.md`、`本地配置方式激活L2TP VPN_40342129.md`、`AAA下发L2TP属性方式激活L2TP VPN_41487855.md` [EV-FK-09, EV-FK-10, EV-FK-11, EV-FK-12, EV-FK-02, EV-FK-03, EV-FK-04]

### 2.2 对象模型

GWFD-020412 在 UDG 侧配置对象较重，按"**LNS 参数来源**"分为两条独立配置链路（本地配置方式 / AAA 下发方式），共享 APN 粒度使能与 PPP/Giif 基础设施。核心配置对象关系如下：

```
┌──────────────────────────────────────────────────────────────────────┐
│ UDG 侧配置对象（U 面：PGW-U/UPF）                                     │
│                                                                      │
│   ┌──────────────┐                                                   │
│   │  APN         │ ← 已通过 ADD APN 配置（外部对象）                 │
│   └──────┬───────┘                                                   │
│          │ SET APNL2TPATTR                                           │
│          ▼                                                           │
│   ┌──────────────────────────────────────────────────┐               │
│   │  APNL2TPATTR  ★核心对象                          │               │
│   │  L2TPSWITCH=ENABLE                               │               │
│   │  SUPPORTIPV6=ENABLE/DISABLE                      │               │
│   │  ICRQ_CALLINGNO=MSISDN/IMSI/IMEI                 │               │
│   │  ICCN_AUTH=ENABLE/DISABLE                        │               │
│   │  IPCP_NEGO=ENABLE/DISABLE                        │               │
│   │  DOMAINNAMEACT / DOMAINNAMEPOS                   │               │
│   │  ┌─────────────────────────────────────────────┐ │               │
│   │  │ 方式A（本地配置）：                          │ │               │
│   │  │   L2TPGROUPID → 指向 L2TPGROUP               │ │               │
│   │  └─────────────────────────────────────────────┘ │               │
│   │  ┌─────────────────────────────────────────────┐ │               │
│   │  │ 方式B（AAA下发）：                           │ │               │
│   │  │   RDSLNSMODE=REDUNDANCY/TUNNEL_PREFER        │ │               │
│   │  └─────────────────────────────────────────────┘ │               │
│   └──────┬───────────────────────────────────────────┘               │
│          │                                                           │
│   ┌──────┴───────────────────────────┐                               │
│   │ ▼ 方式A：本地配置 L2TP Group      │   ▼ 方式B：AAA 下发           │
│   │                                    │                              │
│   │ ┌──────────────┐                   │ （不创建本地 L2TPGROUP，     │
│   │ │ L2TPGROUP    │ ← ADD L2TPGROUP   │  直接使用 AAA 下发 LNS 参数）│
│   │ │ DOMAINNAME   │                   │                              │
│   │ │ LOCALNAME    │                   │ ┌──────────────┐             │
│   │ │ LOCALLNSMODE │                   │ │ L2TPRDSCLIENT│ ←ADD         │
│   │ │  = REDUNDANCY│                   │ │ APN↔Giif     │  L2TPRDSCLIENT│
│   │ │  /LOAD_SHARING│                  │ │ 绑定         │             │
│   │ │ FIRSTLNSIP   │                   │ └──────────────┘             │
│   │ │ SECONDLNSIP  │                   │                              │
│   │ │ MAXSESSIONNUM│                   │                              │
│   │ │ MAXSENDWINSIZE│                  │                              │
│   │ └──────┬───────┘                   │                              │
│   │        │ ADD L2TPCLIENTIP          │                              │
│   │        ▼ (组绑定源端接口)           │                              │
│   │ ┌──────────────┐                   │                              │
│   │ │L2TPCLIENTIP  │ ← ADD L2TPCLIENTIP│                              │
│   │ │ L2TPGROUPID  │                   │                              │
│   │ │ ↔INTERFACENAME│                  │                              │
│   │ └──────────────┘                   │                              │
│   └────────────────────────────────────┘                              │
│                                                                      │
│   共享基础设施：                                                      │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐               │
│   │ GLOBALL2TP   │  │ PPPCFG       │  │ APNPPPACCESS │               │
│   │ (缺省本端名/ │  │ (MRU/HOSTNAME│  │ (APN PPP鉴权)│               │
│   │  HELLO/重发) │  │  /TIMEOUT)   │  │              │               │
│   └──────────────┘  └──────────────┘  └──────────────┘               │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐               │
│   │ VPNINST      │  │ LOGICINF     │  │ L2TPN4KEY    │               │
│   │ (VPN实例)    │  │ (Giif接口)   │  │ (N4加密,可选)│               │
│   └──────────────┘  └──────────────┘  └──────────────┘               │
└──────────────────────────────────────────────────────────────────────┘
                   │
                   │ Sx / N4 PFCP（携带 LNS 参数，来自 UNC）
                   ▼
┌──────────────────────────────────────────────────────────────────────┐
│ UNC 侧决策对象（C 面：GGSN/PGW-C/SMF，详见 WSFD-104410）              │
│   APNL2TPCTRL（C面 APN 粒度 L2TP 开关）+ PFCP 私有信元下发通道         │
└──────────────────────────────────────────────────────────────────────┘
```

核心对象说明：

| 对象 | 命令 | 作用 | 方式A/B |
|------|------|------|---------|
| **APNL2TPATTR** | `SET APNL2TPATTR` | **本特性核心对象**。按 APN 粒度使能 L2TP，配置 IPv6 支持、ICRQ/ICCN 信元、IPCP 协商、域名增删；方式A 还指定 L2TPGROUPID，方式B 指定 RDSLNSMODE | 共用 |
| **L2TPGROUP** | `ADD L2TPGROUP` | **本地配置方式核心对象**。LNS 容器，绑定域名、LNS IP、隧道密码、HELLO、发送窗口、PPP Magic-Number、VPN 实例 | 仅方式A |
| L2TPCLIENTIP | `ADD L2TPCLIENTIP` | 本地配置方式：L2TP 组绑定源端 Giif 接口 | 仅方式A |
| L2TPRDSCLIENT | `ADD L2TPRDSCLIENT` | AAA 下发方式：APN 绑定源端 Giif 接口 | 仅方式B |
| GLOBALL2TP | `SET GLOBALL2TP` | L2TP 缺省属性（本端名、HELLO 开关/间隔、重发次数、PPP Magic-Number、发送窗口、初始隧道数、会话上限） | 共用 |
| PPPCFG | `SET PPPCFG` | PPP 协商参数（本端主机名、MRU、超时） | 共用 |
| APNPPPACCESS | `SET APNPPPACCESS` | APN 的 PPP 鉴权配置 | 共用 |
| VPNINST | `ADD VPNINST` | VPN 实例 | 共用 |
| LOGICINF | `ADD LOGICINF` | Giif 逻辑接口 | 共用 |
| L2TPN4KEY | `SET L2TPN4KEY` | N4 接口 L2TP 加密密钥（可选） | 共用 |
| LICENSESWITCH | `SET LICENSESWITCH` | License 开关 | 共用 |
| SOFTPARAOFBIT | `SET SOFTPARAOFBIT` | 软参 Byte671 bit7=1 关闭快速流表 | 共用 |

> 来源：`GWFD-020412 L2TP VPN参考信息_40342151.md`（命令清单）、`本地配置方式激活L2TP VPN_40342129.md`、`AAA下发L2TP属性方式激活L2TP VPN_41487855.md` [EV-FK-02, EV-FK-03, EV-FK-04]

### 2.3 在地址分配场景的角色

GWFD-020412 在地址分配场景中扮演**"LNS 远程地址分配执行体"**的角色：

1. **LAC 角色**：UDG 解 GTP 封装获得原始 IP 报文，作为 LAC 为 IP 报文添加 PPP 封装，通过 L2TP 隧道透传到企业网 LNS
2. **PPP 再生**：4G/5G 网络中 PPP 再生（图1/图2）——UDG 在用户面重建 PPP 链路，使 UE 与 LNS 之间通过 L2TP 隧道完成 PPP 协商
3. **地址分配主体**：**L2TP 用户的 IP 地址由 LNS 分配**（L2TP 用户的地址都是由 LNS 进行分配的，即使 PGW-U/UPF 本地配置了地址池或 AAA 下发地址，最终都是将 IPCP 协商结果中的地址返回）——地址分配主体在 LNS（企业网侧），而非 UDG 本地池
4. **与本地地址分配的互斥分工**：L2TP VPN 用户的 IP 地址来自企业内网（LNS 端地址池），与 GWFD-010105/GWFD-010104 的本地分配方式（基于 APN/DNN、基于 SMF）是**互斥的并行方案**——一个用户要么走 L2TP 远程分配（经 LNS），要么走本地分配（UDG 本地池）
5. **与 GWFD-020421（基于位置的地址分配）的语义互斥**：虽然 GWFD-020412 文档**未明确声明**与 GWFD-020421 互斥，但地址分配主体不同（LNS 远程 vs UDG 位置本地池），逻辑上一个用户只能由一方分配地址，属语义级互斥（Stage 3 横向分析待验证）

> 来源：`GWFD-020412 L2TP VPN特性概述_40342127.md`（"原理概述/图1 4G网络PPP再生/图2 5G网络PPP再生"）、`L2TP激活流程_76399675.md`（"PPP协商/IPCP协商"第3条"地址都是由LNS分配"）[EV-FK-01, EV-FK-05]

---

## 3. 原理与流程

### 3.1 实现原理（U 面：LAC + PPP 再生 + 隧道封装）

UDG 解 GTP 封装后获得原始 IP 报文，然后作为 LAC（L2TP Access Concentrator）为 IP 报文添加 PPP 封装，通过与企业网之间建立的二层 L2TP 隧道，将 PPP 报文发送到企业网。

L2TP 专门针对 PPP 协议进行隧道传输和中继，是数据链路层协议。其报文分为：
- **控制消息**：用于隧道和会话连接的建立、维护以及传输控制；应用消息丢失重传和定时检测通道连通性等机制保证可靠性
- **数据消息**：用于封装 PPP 帧并在隧道上传输，采用不可靠传输

L2TP 是面向连接的，在一个 LNS 和 LAC 对之间存在两种类型的连接：
- **控制连接**：定义一个 LNS 和 LAC 对，控制隧道和会话的建立、维护和拆除
- **会话连接**：复用在控制连接之上，每个会话对应 LAC 和 LNS 之间的一个 PPP 数据流

隧道由一个控制连接和一个或多个会话连接组成；同一对 LAC 和 LNS 之间可以建立多个 L2TP 隧道。

> 来源：`GWFD-020412 L2TP VPN特性概述_40342127.md`（"原理概述"）、`相关术语/L2TP_51067102.md`（"控制消息和数据消息/控制连接和会话连接/隧道和会话"）[EV-FK-01, EV-FK-09]

### 3.2 L2TP 隧道建立端到端流程（C-U 协同 + LNS 三阶段协商）

```
┌─────────────────────────────────────────────────────────────────┐
│ 阶段 1：UNC 接收 LNS 参数（C 面决策，见 WSFD-104410）             │
│                                                                 │
│   方式 A（AAA 下发）：AAA Server ──Access-Accept──> UNC         │
│     携带 LNS IP、Tunnel-Preference、Tunnel-Password、           │
│           Tunnel-Assignment-ID（L2TP Tunnel Info 信元）          │
│                                                                 │
│   方式 B（本地配置）：UNC 本地 SET APNL2TPCTRL L2TPSWITCH=ENABLE│
│     （此方式下 LNS 参数由 UDG 本地 L2TPGROUP 配置提供）          │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│ 阶段 2：UNC 通过 Sx/N4 接口下发 LNS 参数到 UPF（见 WSFD-104410）  │
│                                                                 │
│   UNC ──PFCP Session Establishment Request──> UPF               │
│     携带：LNS 地址 / L2TP 隧道参数 / L2TP 用户 PCO 信息          │
│     通过 PFCP 私有扩展信元（L2TP 私有扩展信元）                  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│ 阶段 3：UDG 查表判定（本特性核心）                                │
│                                                                 │
│   UDG 收到 PFCP Session Establishment Request 后查表判定：       │
│   - 方式A（AAA下发）：使用 PFCP 携带的 LNS 参数                  │
│   - 方式B（本地配置）：PGW-C/SMF 未下发 LNS 信息时，             │
│     UDG 根据本地配置的 L2TPGROUP 建立 L2TP 隧道                  │
│     （若 APN 已使能 L2TP 且用户名域名匹配 L2TPGROUP 域名）       │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│ 阶段 4：L2TP 隧道建立（SCCRQ/SCCRP/SCCCN 三次握手，U 面执行）    │
│                                                                 │
│   4a. SCCRQ：Start-Control-Connection-Request，初始化 tunnel     │
│   4b. SCCRP：Start-Control-Connection-Reply，接受连接请求        │
│   4c. SCCCN：Start-Control-Connection-Connected，完成 tunnel     │
│                                                                 │
│   重传：隧道重传定时器超时按 1s、2s、4s、8s、16s 重发，          │
│         最大发送次数默认 3 次；仍未收到 SCCCN 则发 StopCCN 拆隧道 │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│ 阶段 5：L2TP 会话建立（ICRQ/ICRP/ICCN 三次握手，U 面执行）       │
│                                                                 │
│   5a. ICRQ：Incoming-Call-Request，请求在 tunnel 中建 session    │
│       Calling-number AVP 携带 MSISDN/IMSI/IMEI                   │
│       （由 SET APNL2TPATTR ICRQ_CALLINGNO 配置）                 │
│   5b. ICRP：Incoming-Call-Reply，ICRQ 成功，LNS 标识 session     │
│   5c. ICCN：Incoming-Call-Connected，session 建立完成            │
│       （携带鉴权信元，由 SET APNL2TPATTR ICCN_AUTH 控制）        │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│ 阶段 6：内层 PPP 协商三阶段（UE ↔ LNS，经 L2TP 隧道透传）        │
│                                                                 │
│   6a. LCP（Link Control Protocol）阶段                          │
│       ← 协商 MRU、Authentication-Protocol（鉴权类型）            │
│       双向协商，支持 LCP Configure Nak/Reject/Ack                │
│                                                                 │
│   6b. 鉴权阶段（PAP / CHAP，由 LCP 协商决定）                    │
│       PAP：两次握手，明文传用户名口令                            │
│       CHAP：三次握手，只传用户名不传口令                         │
│       支持鉴权方式转换：PAP→CHAP、PAP→不鉴权、CHAP→不鉴权       │
│       （不支持反向转换）                                         │
│                                                                 │
│   6c. 网络层协议协商阶段（IPCP / IPv6CP）                        │
│       IPv4 用户：发起 IPCP 协商                                 │
│         ★ 地址分配发生在此阶段，LNS 分配 UE IP/DNS/NBNS          │
│       IPv6 用户：发起 IPv6CP 协商，获取接口 ID                   │
│         ★ IPv6 地址 = 网络前缀（LNS RA 下发）+ 接口 ID           │
│       IPv4v6 用户：同时发起 IPCP 和 IPv6CP                      │
└─────────────────────────────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│ 阶段 7：激活响应与返回                                           │
│                                                                 │
│   - UDG 给 PGW-C/SMF 回 PFCP Session Establishment Response     │
│     携带 L2TP 会话信息（私有扩展信元）                           │
│   - PGW-C/SMF 回 Create Session Response / Nsmf_PDUSession_      │
│     CreateSMContext Response，PCO 中携带 LNS 分配的              │
│     User IP Address、DNS IP、NBNS IP                            │
└─────────────────────────────────────────────────────────────────┘
```

> 来源：`L2TP查表流程_19990150.md`（"L2TP建立过程/图1"）、`L2TP激活流程_76399675.md`（"L2TP激活流程/图1 + PPP协商/图2"）[EV-FK-06, EV-FK-05]

### 3.3 与 WSFD-104410（UNC 侧）的 C-U 对称分工

```
┌──────────────────────────────────────────────────────────────────┐
│ UNC（C 面：GGSN/PGW-C/SMF） - WSFD-104410                        │
│ 角色：决策 + LNS 参数下发                                         │
│                                                                  │
│   - 接收 AAA Server Access-Accept 中的 LNS 参数                  │
│   - 或本地 APN 粒度使能 L2TP（SET APNL2TPCTRL）                  │
│   - 通过 Sx/N4 PFCP 私有信元下发 LNS 参数                       │
│   - 可选加密 L2TP 私有信元（SET L2TPKEY）                        │
│                                                                  │
│   核心配置对象：APNL2TPCTRL（C 面专用）                          │
│   特性规格：L2TP 隧道信息 20 个                                  │
│   License：无                                                    │
│   标准：3GPP 23.214 / 29.244（CUPS）                             │
└──────────────────────────┬───────────────────────────────────────┘
                           │ Sx / N4 PFCP（L2TP 私有扩展信元）
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│ UDG（U 面：PGW-U/UPF） - GWFD-020412  ★本特性                     │
│ 角色：LAC + L2TP 隧道封装 + PPP 再生与协商透传                    │
│                                                                  │
│   - 作为 LAC（L2TP Access Concentrator）                         │
│   - 解 GTP 封装获得原始 IP 报文                                  │
│   - 为 IP 报文添加 PPP 封装                                      │
│   - 与企业网 LNS 建立 L2TP 隧道，透传 PPP                        │
│   - PPP 三阶段协商（LCP→PAP/CHAP→IPCP/IPv6CP）                  │
│                                                                  │
│   核心配置对象：APNL2TPATTR（U 面专用，★非 C 面 APNL2TPCTRL）   │
│   特性规格：本地 L2TP Group 1500 / AAA 下发方式 Group 1500       │
│   License：82200BVC LKV3G5L2TP01 L2TP VPN（必须）                │
│   标准：3GPP 23.214/29.244 + RFC 2661/2868/5072/5571/8064        │
│   互斥：GWFD-010108（地址自动检测）、GWFD-020482（入不转板）     │
│        不支持 DHCP 延迟分配 IPv4；不支持 IPv6 PD；               │
│        NP 加速场景不支持 IPv6；不支持 PPP 用户接入；              │
│        不支持 PFC/ACFC 压缩；不支持 NAT；需关闭快速流表          │
└──────────────────────────────────────────────────────────────────┘
```

> 来源：综合 `WSFD-104410 特性概述_46559213.md` [EV-FK-C侧参考] 与 UDG 侧 `GWFD-020412 L2TP VPN特性概述_40342127.md` [EV-FK-01] 构建 C-U 协同分工图

### 3.4 协议交互

| 接口 | 交互网元 | 消息类型 | 说明 |
|------|---------|---------|------|
| Radius（2/3/4/5G） | AAA Server ↔ GGSN/PGW-C/SMF | Access-Request / Access-Accept | AAA 对 L2TP 用户鉴权，Access-Accept 携带 LNS Tunnel Info（LNS IP、Tunnel-Preference、Tunnel-Password、Tunnel-Assignment-ID） |
| Sx（4G）/ N4（5G） | GGSN/PGW-C/SMF ↔ PGW-U/UPF | PFCP Session Establishment Request / Response | UNC 将 LNS 参数通过 L2TP 私有扩展信元下发给 UPF；UPF 回 Response 携带 L2TP 会话信息 |
| L2TP 控制消息 | PGW-U/UPF（LAC） ↔ LNS | SCCRQ/SCCRP/SCCCN + ICRQ/ICRP/ICCN + ZLB + StopCCN + CDN | 隧道与会话建立、维护、拆除（U 面执行） |
| L2TP Hello | PGW-U/UPF（LAC） ↔ LNS | Hello + ZLB | 隧道连通性检测，默认 60 秒一次，未收到 ZLB 重发最大 3 次 |
| PPP（内层） | UE ↔ LNS（经 L2TP 隧道透传，UDG 代理） | LCP Configure Request/Ack/Nak/Reject + PAP/CHAP + IPCP/IPv6CP | 三阶段协商，地址分配在 IPCP/IPv6CP 阶段 |

> 来源：`L2TP激活流程_76399675.md`（协议交互）、`L2TP隧道维护流程_32553703.md`（Hello 维护）[EV-FK-05, EV-FK-07]

### 3.5 L2TP 去激活流程（三类发起方）

L2TP 用户去活支持三类发起方：

| 发起方 | 触发场景 | 关键消息 |
|--------|---------|---------|
| UE 或 PGW-C/SMF | PFCP Session Delete Request | UDG 发 CDN 释放会话 → 若隧道无其他会话则发 StopCCN 拆隧道 → 回 PFCP Session Delete Response |
| PGW-U/UPF | 主动去活（如 `DEA SESSION` 命令） | UDG 发 CDN → ZLB 确认 → StopCCN 拆隧道 → PFCP Session Report Request 上报 → PFCP Session Delete 删除 |
| LNS | 主动释放会话 | LNS 发 CDN → UDG 回 ZLB → StopCCN 拆隧道 → PFCP Session Report 上报 → PFCP Session Delete 删除 |

特殊场景：**LNS 发起单栈释放流程**——L2TP 用户激活后，LNS 发 IPCP Terminate-Request 或 IPv6CP Terminate-Request 请求释放 IPv4 或 IPv6 单栈地址，UDG 回 Terminate-Ack 后发起 L2TP 用户去活流程。

> 来源：`L2TP去激活流程_19990151.md`（"UE/PGW-C/SMF发起 + PGW-U/UPF发起 + LNS发起 + LNS单栈释放"四节）[EV-FK-06]

### 3.6 异常场景处理

**双栈转单栈**（双栈用户接入时，若与 LNS 协商某个单栈失败）：

| 双栈地址来源 | 协商失败处理 |
|-------------|-------------|
| 双栈地址都是外部分配 | **不允许降栈**，单栈协商失败则 L2TP 用户激活失败 |
| 双栈地址都是 LNS 分配 | **允许降栈**，单栈协商失败可降为单栈 |
| 一栈外部分配、一栈 LNS 分配 | 外部分配失败 → 激活失败；LNS 分配失败 → 允许降栈 |

**单栈限制**：双栈用户接入时，若 `SET APNL2TPATTR` 配置 `SUPPORTIPV6=DISABLE`，仅支持 IPv4 用户接入，UDG 与 LNS 之间只进行 IPv4 单栈协商。

**地址分配原则**：如果 UDG 收到 N4 PFCP Session Establishment Request，根据 L2TP 私有扩展信元或本地配置识别是 L2TP 用户，且用户激活请求消息里没有携带 UE 地址，则一般由 LNS 分配地址（L2TP 用户地址由 LNS 分配或静态签约分配）。

> 来源：`L2TP激活流程_76399675.md`（"异常场景"第1-3条 + "说明"）[EV-FK-05]

---

## 4. 配置规则

### 4.1 激活步骤

GWFD-020412 在 UDG 侧的激活流程分为两条独立路径（本地配置方式 / AAA 下发方式），共享 License、APN、Giif、PPP 等基础设施：

```
步骤1：确认前置条件
  ├── 已加载 License 82200BVC LKV3G5L2TP01
  ├── 已通过 SET LICENSESWITCH 打开 License 配置开关
  ├── 已通过 ADD APN 配置目标 APN（如 apn-l2tp）
  ├── 企业网侧已部署 LNS 设备（应用限制硬约束）
  └── UDG 与 LNS 物理链路连通

步骤2：（可选）配置 VPN 实例
  └── ADD VPNINST: VPNINSTANCE="vpn_l2tp"

步骤3：配置 L2TP 缺省参数
  └── SET GLOBALL2TP: LOCALNAME/HELLOINTERVALSW/HELLOINTERVAL/RETRYTIMES
      （方式B 额外配置 PPPMAGICNUMBER/MAXSENDWINSIZE/INITTUNNELNUM/MAXSESSIONNUM）

步骤4：配置 APN 的 L2TP 属性（★核心使能）
  └── SET APNL2TPATTR: APN/L2TPSWITCH=ENABLE/SUPPORTIPV6/...

步骤5：关闭快速流表功能（应用限制硬约束）
  └── SET SOFTPARAOFBIT: DT2=BYTE, BYTENUM=671, BYTEPOSITION=7, BYTEVALUE=1

步骤6：配置 Giif 接口
  └── ADD LOGICINF: NAME/IPVERSION/IPV4ADDRESS1/IPV4MASK1/VPNINSTANCE

=== 分支：方式A（本地配置）/ 方式B（AAA下发）===

【方式A：本地配置】
步骤7a：配置 L2TP 组信息（★方式A核心）
  └── ADD L2TPGROUP: GROUPID/DOMAINNAME/LOCALNAME/LOCALLNSMODE/
                     FIRSTLNSIP/SECONDLNSIP/HELLO参数/MAXSENDWINSIZE/...
步骤8a：将 L2TP 组绑定源端接口
  └── ADD L2TPCLIENTIP: L2TPGROUPID, INTERFACENAME
（注：步骤4 的 SET APNL2TPATTR 需指定 L2TPGROUPID 指向此组）

【方式B：AAA下发】
步骤7b：（无需创建本地 L2TPGROUP）
        直接使用 AAA 下发的 LNS 参数
步骤8b：将 APN 绑定源端接口
  └── ADD L2TPRDSCLIENT: APN, INTERFACENAME
（注：步骤4 的 SET APNL2TPATTR 需指定 RDSLNSMODE）

=== 共享可选配置 ===
步骤9：（可选）配置 PPP 协商参数
  └── SET PPPCFG: HOSTNAME/MRU/TIMEOUT
步骤10：（可选）配置 APN 的 PPP 鉴权
  └── SET APNPPPACCESS: APN, AUTHENTICATION=ENABLE
步骤11：（可选）配置 L2TP 业务加密（N4 接口）
  └── SET L2TPN4KEY: N4KEYVALUE, CFMN4KEYVALUE
      注：对端 SMF 需同时配置 SET L2TPKEY 并配置相同密钥
```

> 来源：`本地配置方式激活L2TP VPN_40342129.md`（操作步骤11步 + 任务示例）、`AAA下发L2TP属性方式激活L2TP VPN_41487855.md`（操作步骤10步 + 任务示例）[EV-FK-03, EV-FK-04]

### 4.2 MML命令清单

#### 4.2.1 参考信息列出的命令（8条核心）

| 命令 | 用途 | 本特性角色 |
|------|------|-----------|
| **ADD L2TPGROUP** | 创建 L2TP 组 | **方式A 核心**。LNS 容器，绑定域名/LNS IP/隧道密码/HELLO/发送窗口 |
| **SET GLOBALL2TP** | 设置 L2TP 缺省配置 | 共享。配置本端名/HELLO/重发/PPP Magic-Number/发送窗口/初始隧道数/会话上限 |
| **SET APNL2TPATTR** | 设置 APN L2TP 配置 | **★本特性核心使能命令**。APN 粒度 L2TP 开关、IPv6 支持、L2TP 组绑定、ICRQ/ICCN 信元 |
| **ADD LOGICINF** | 增加逻辑接口 | 共享。Giif 接口 |
| **ADD L2TPCLIENTIP** | 增加 L2TP 绑定的接口 | **方式A 专用**。L2TP 组绑定源端 Giif 接口 |
| **ADD L2TPRDSCLIENT** | 增加 APN 绑定的 L2TP 接口 | **方式B 专用**。APN 绑定源端 Giif 接口 |
| **SET PPPCFG** | 设置 PPP 配置 | 共享可选。PPP 协商参数（MRU/HOSTNAME/TIMEOUT） |
| **SET APNPPPACCESS** | 设置 APN PPP 配置 | 共享可选。APN PPP 鉴权 |

> 来源：`GWFD-020412 L2TP VPN参考信息_40342151.md`（"命令"章节）[EV-FK-02]

#### 4.2.2 激活文档涉及的辅助命令（6条）

| 命令 | 用途 | 来源 |
|------|------|------|
| SET LICENSESWITCH | 设置 License 项的开关 | 激活文档步骤1（打开 LKV3G5L2TP01 开关） |
| ADD VPNINST | 增加 VPN 实例 | 激活文档步骤2（VPN 组网方式） |
| ADD APN | 添加 APN 配置 | 激活文档任务示例（前置，非本特性独立命令） |
| SET SOFTPARAOFBIT | 设置软件参数表比特位的值 | 激活文档步骤6（关闭快速流表 Byte671 bit7=1） |
| SET L2TPN4KEY | 设置 L2TP N4 密码配置 | 激活文档步骤11（可选，N4 加密） |
| ADD L2TPLNSINFO | 添加 LNS 与 L2TP 组绑定关系 | 激活文档步骤3说明（L2TP 组中 6 个以上 LNS 或 LNS 为 IPv6 时使用） |

> 来源：`本地配置方式激活L2TP VPN_40342129.md`、`AAA下发L2TP属性方式激活L2TP VPN_41487855.md` [EV-FK-03, EV-FK-04]

#### 4.2.3 调测查询命令（10条）

| 命令 | 用途 |
|------|------|
| LST LICENSESWITCH | 查询 License 配置项开关 |
| DSP L2TPSESSION | 查询 L2TP 隧道下 L2TP 会话相关信息 |
| DSP L2TPTUNNEL | 查询 L2TP 隧道的相关信息 |
| PING | IP Ping（验证 UDG 到 LNS 连通性） |
| DSP ROUTE | 显示 IPv4 路由表 |
| ADD/MOD SRROUTE | 增加/修改 IPv4 静态路由 |
| LST LOGICINF | 查询逻辑接口 |
| LST INTERFACE | 查询接口 |
| LST L2TPGROUP | 查询指定 L2TP 组 |
| LST PPPCFG | 查询 PPP 配置 |
| LST APNL2TPATTR | 查询 APN L2TP 配置 |
| DEA SESSION | 去活用户会话（PGW-U/UPF 主动去活 L2TP 用户） |
| EXP MML | 导出 MML 文件（故障信息收集） |

> 来源：`调测基于本地配置方式激活的L2TP VPN_40342150.md`、`调测基于AAA下发L2TP属性方式激活的L2TP VPN_41487857.md` [EV-FK-08, EV-FK-13]

### 4.3 关键参数说明

#### 4.3.1 SET APNL2TPATTR 关键参数（★核心命令）

| 参数 | 取值 | 说明 |
|------|------|------|
| APN | 字符串（如 apn-l2tp） | APN 名称，必须已通过 ADD APN 配置 |
| L2TPSWITCH | ENABLE / DISABLE | APN 支持 L2TP 功能开关；ENABLE 表示本 APN 下用户启用 L2TP VPN |
| SUPPORTIPV6 | DISABLE（默认）/ ENABLE | L2TP 支持 IPv6 功能开关，控制是否支持 L2TP 内层 IPv6；DISABLE 时仅支持 IPv4 用户接入 |
| L2TPGROUPID | 数字（如 1） | **方式A 专用**。指定该 APN 下用户使用的本地 L2TP 组 |
| RDSLNSMODE | REDUNDANCY / TUNNEL_PREFER | **方式B 专用**。RADIUS 服务器返回多 LNS 时的工作模式：REDUNDANCY（两 LNS Tunnel-Preference 相同为主备）；TUNNEL_PREFER（Preference 不同为主备，相同为负荷分担） |
| ICRQ_CALLINGNO | MSISDN / IMSI / IMEI | ICRQ 消息中 Calling-number AVP 携带的用户标识 |
| ICCN_AUTH | ENABLE / DISABLE | ICCN 携带鉴权信元开关。不鉴权时不携带；鉴权且用户需鉴权时携带 |
| IPCP_NEGO | ENABLE / DISABLE | 发起 IPCP 协商开关，控制系统是否主动发起 IPCP 协商 |
| DOMAINNAMEACT | ADD_ENABLE_STRIP_DISABLE 等 | ICCN/CHAP/PAP 消息中用户名增加或剥离域名功能 |
| DOMAINNAMEPOS | PREFIX 等 | 域名位置（前缀/后缀） |

> 来源：`本地配置方式激活L2TP VPN_40342129.md`（"必备事项/数据"表 SET APNL2TPATTR 行）、`AAA下发L2TP属性方式激活L2TP VPN_41487855.md`（"必备事项/数据"表 SET APNL2TPATTR 行）、`L2TP激活流程_76399675.md`（"异常场景/单栈限制" SUPPORTIPV6）[EV-FK-03, EV-FK-04, EV-FK-05]

#### 4.3.2 ADD L2TPGROUP 关键参数（方式A核心）

| 参数 | 取值样例 | 说明 |
|------|---------|------|
| GROUPID | 1 | L2TP 组号（本端规划） |
| DOMAINNAME | "example.com" | 隧道的域名（方式B 本地匹配关键字） |
| LOCALNAME | "UPF" | 隧道本端的名称 |
| AUTHENTICATION | ENABLE | 隧道鉴权使能 |
| AVPHIDDEN | ENABLE | 隐藏 AVP，采用隐藏方式传输 AVP 数据 |
| HELLOINTERVALSW | ENABLE | HELLO 报文开关（检测 LAC 和 LNS 之间隧道连通性） |
| HELLOINTERVAL | 120 | HELLO 报文间隔（秒） |
| RETRYTIMES | 3 | 报文重发次数 |
| VPNINSTANCE | "vpn_l2tp" | L2TP 隧道绑定的 VPN 实例 |
| LOCALLNSMODE | REDUNDANCY / LOAD_SHARING | 多 LNS 工作模式：REDUNDANCY（主备，最多 2 个 LNS）/ LOAD_SHARING（负荷分担，可配置 6 个 LNS） |
| FIRSTLNSIP / SECONDLNSIP | "10.10.10.1" / "10.10.10.2" | 主备模式下第一/第二个 LNS IP 地址 |
| FIRSTPWD / SECONDPWD | "0123456" | 第一/第二个 LNS 隧道认证密码 |
| PPPMAGICNUMBER | ENABLE | 是否支持 PPP LCP Magic-Number 协商 |
| MAXSENDWINSIZE | 32 | LAC 侧 L2TP 隧道发送窗口上限 |
| MAXSESSIONNUM | - | 每条隧道承载的会话个数上限（超限则新建隧道） |

> 来源：`本地配置方式激活L2TP VPN_40342129.md`（"必备事项/数据"表 ADD L2TPGROUP 多行 + 操作步骤3说明）[EV-FK-03]

#### 4.3.3 SET GLOBALL2TP 关键参数

| 参数 | 取值样例 | 说明 |
|------|---------|------|
| LOCALNAME | "huawei" | 隧道本端的缺省名称（AAA 未返回 Client-Auth-ID 时使用） |
| HELLOINTERVALSW | ENABLE | HELLO 报文发送开关 |
| HELLOINTERVAL | 60 | HELLO 报文缺省间隔（秒），默认 60 秒 |
| RETRYTIMES | 3 | 报文重发次数（未收到 ZLB 响应时，最大 3 次） |
| PPPMAGICNUMBER | DISABLE | 是否支持 Magic-Number 协商（方式B 默认 DISABLE） |
| MAXSENDWINSIZE | 64 | 发送窗口上限（方式B 默认 64） |
| INITTUNNELNUM | 1 | 初始隧道个数（方式B） |
| MAXSESSIONNUM | 32767 | 每条隧道承载的会话个数上限（方式B） |

> 来源：`本地配置方式激活L2TP VPN_40342129.md`、`AAA下发L2TP属性方式激活L2TP VPN_41487855.md`（"必备事项/数据"表 SET GLOBALL2TP 多行 + 操作步骤3说明）[EV-FK-03, EV-FK-04]

#### 4.3.4 SET L2TPN4KEY 关键参数（N4 加密，可选）

| 参数 | 取值 | 说明 |
|------|------|------|
| N4KEYVALUE | 密钥字符串 | N4 密钥。若不配置，即明文携带 L2TP 私有信元，存在安全风险 |
| CFMN4KEYVALUE | 密钥字符串 | 确认 N4 密钥 |

> 安全提示：启用时对端 SMF（UNC 侧 `SET L2TPKEY`）必须同时开启并配置相同密钥，否则 L2TP 业务失败。

> 来源：`本地配置方式激活L2TP VPN_40342129.md`、`AAA下发L2TP属性方式激活L2TP VPN_41487855.md`（"必备事项/数据"表 SET L2TPN4KEY 行 + 步骤11说明）[EV-FK-03, EV-FK-04]

### 4.4 约束条件

| 约束类型 | 约束内容 | 来源 |
|---------|---------|------|
| 企业网 LNS 部署（应用限制） | 企业网侧必须部署 LNS 设备 | 特性概述"应用限制"章节 |
| 不支持 PPP 用户接入 | L2TP 用户接入不支持 PPP 用户接入类型 | 特性概述"应用限制"章节 |
| 不支持 DHCP 延迟分配 IPv4 | L2TP 用户接入时不支持 DHCP 延迟分配 IPv4 地址 | 特性概述"应用限制"章节 |
| 不支持 IPv6 Prefix Delegation | L2TP 用户接入时不支持 IPv6 PD 地址分配方式 | 特性概述"应用限制"章节 |
| 不支持 PFC/ACFC 压缩 | 不支持 UDG 与 LNS 协商 PFC 和 ACFC 字段压缩流程 | 特性概述"应用限制"章节 |
| 不支持 NAT | 该功能不支持 NAT 地址转换 | 特性概述"应用限制"章节 |
| NP 加速不支持 IPv6 | NP 加速场景下，L2TP VPN 特性不支持 IPv6 | 特性概述"应用限制"章节 |
| 快速流表需关闭 | L2TP 场景需关闭快速流表（Byte671 bit7=1），否则可能丢包 | 特性概述"应用限制"章节 + 激活文档步骤6 |
| APN 先决条件 | SET APNL2TPATTR 的 APN 参数必须已通过 ADD APN 配置 | 激活文档"必备事项/数据"表 |
| 加密对称性 | 启用 SET L2TPN4KEY 时，对端 SMF（SET L2TPKEY）必须同时开启并配置相同密钥 | 激活文档步骤11说明 |
| 隧道/会话规格 | 本地 L2TP Group 规格 1500；AAA 下发方式 Group 规格 1500 | 特性概述"特性规格"章节 |
| C-U License 不对称 | UDG 侧必须 License 82200BVC LKV3G5L2TP01；UNC 侧无 License | 特性概述"可获得性"章节 vs WSFD-104410 |
| C-U 版本对齐 | UNC 与 UDG 均需 20.3.2 及后续版本 | 特性概述"可获得性"章节 |
| **互斥：GWFD-010108** | L2TP VPN 不支持与用户面地址自动检测功能同时应用 | 特性概述"与其他特性的交互"章节 |
| **互斥：GWFD-020482** | APN 下开启 L2TP VPN，则不支持入不转板功能 | 特性概述"与其他特性的交互"章节 |
| 地址分配主体 | L2TP 用户地址由 LNS 分配（即使本地配置地址池或 AAA 下发地址） | 激活流程"PPP协商/IPCP"第3条 |

---

## 5. 配置案例

### 5.1 典型场景1：本地配置方式激活 L2TP VPN（主备 LNS）

**场景描述**：企业用户通过公网接入企业内网，运营商在 UDG 上为 APN `apn-l2tp` 使能 L2TP 功能，采用本地配置方式，UDG 作为 LAC 与企业网主备 LNS（10.10.10.1 / 10.10.10.2）建立 L2TP 隧道。

**配置步骤和 MML 命令序列**（保留原始 MML）：

```
// 打开本特性的 License 配置开关。
SET LICENSESWITCH:LICITEM="LKV3G5L2TP01",SWITCH=ENABLE;

// 配置 VPN 实例。
ADD VPNINST:VPNINSTANCE="vpn_l2tp";

// 配置 L2TP 组信息。配置 L2TP 组的组号、域名、本端主机名、鉴权、HELLO 报文间隔、
// magic number 协商、L2TP 隧道发送窗口大小的上限、L2TP 隧道绑定的 VPN 实例、LNS 服务器。
ADD L2TPGROUP: GROUPID=1, DOMAINNAME="example.com", LOCALNAME="UPF", AVPHIDDEN=ENABLE, HELLOINTERVALSW=ENABLE, HELLOINTERVAL=120, VPNINSTANCE="vpn_l2tp", LOCALLNSMODE=REDUNDANCY, FIRSTLNSIP="10.10.10.1", FIRSTPWD="0123456", SECONDLNSIP="10.10.10.2", SECONDPWD="0123456", CFMFIRSTPWD="0123456", CFMSECONDPWD="0123456", PPPMAGICNUMBER=ENABLE, MAXSENDWINSIZE=32;

// 配置 L2TP 的缺省参数，使能本地配置方式启用 L2TP。
SET GLOBALL2TP:LOCALNAME="huawei",HELLOINTERVALSW=ENABLE,HELLOINTERVAL=60,RETRYTIMES=3;

// 设置 APN 的 L2TP 相关信息，指定 APN 下绑定 L2TP 组。
ADD APN: APN="apn-l2tp";
SET APNL2TPATTR:APN="apn-l2tp",L2TPSWITCH=ENABLE,SUPPORTIPV6=DISABLE,L2TPGROUPID=1,ICRQ_CALLINGNO=MSISDN,ICCN_AUTH=ENABLE,IPCP_NEGO=ENABLE,DOMAINNAMEACT=ADD_ENABLE_STRIP_DISABLE,DOMAINNAMEPOS=PREFIX;

// 关闭快速流表功能。
SET SOFTPARAOFBIT: DT2=BYTE, BYTENUM=671, BYTEPOSITION=7, BYTEVALUE=1;

// 配置 Giif 接口。
ADD LOGICINF:NAME="giif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_l2tp";

// 将 L2TP 组绑定指定源端接口。
ADD L2TPCLIENTIP:L2TPGROUPID=1,INTERFACENAME="giif1/0/0";

// 系统进行 PPP 协商时所使用的参数。
SET PPPCFG:HOSTNAME="UPF",MRU=1500,TIMEOUT=3;

// 设置 APN 的 PPP 相关信息，支持 PPP 鉴权功能。
SET APNPPPACCESS: APN="apn-l2tp", AUTHENTICATION=ENABLE;

// （可选配置）设置 L2TP 业务加密。
SET L2TPN4KEY: N4KEYVALUE="*****", CFMN4KEYVALUE="*****";
```

> 来源：`本地配置方式激活L2TP VPN_40342129.md`（"任务示例/脚本"完整原文）[EV-FK-03]

### 5.2 典型场景2：AAA 下发 L2TP 属性方式激活 L2TP VPN

**场景描述**：PGW-C/SMF 支持 AAA 鉴权，AAA Server 在 Access-Accept 消息中下发 LNS 信息时，UDG 直接使用 AAA 通过 PGW-C/SMF 下发的 LNS 信息，本地不需要配置 L2TP 组。

**配置步骤和 MML 命令序列**（保留原始 MML）：

```
// 打开本特性的 License 配置开关。
SET LICENSESWITCH:LICITEM="LKV3G5L2TP01",SWITCH=ENABLE;

// 配置 VPN 实例。
ADD VPNINST:VPNINSTANCE="vpn_l2tp";

// 配置 L2TP 的缺省参数，使能本地配置方式启用 L2TP。
SET GLOBALL2TP:LOCALNAME="huawei",HELLOINTERVALSW=ENABLE,HELLOINTERVAL=60,RETRYTIMES=3,PPPMAGICNUMBER=DISABLE,MAXSENDWINSIZE=64,INITTUNNELNUM=1,MAXSESSIONNUM=32767;

// 使能 L2TP。
ADD APN: APN="apn-l2tp";
SET APNL2TPATTR:APN="apn-l2tp",L2TPSWITCH=ENABLE,SUPPORTIPV6=DISABLE,ICRQ_CALLINGNO=MSISDN,ICCN_AUTH=ENABLE,IPCP_NEGO=ENABLE,DOMAINNAMEACT=ADD_ENABLE_STRIP_DISABLE,DOMAINNAMEPOS=PREFIX;

// 关闭快速流表功能。
SET SOFTPARAOFBIT: DT2=BYTE, BYTENUM=671, BYTEPOSITION=7, BYTEVALUE=1;

// 配置 Giif 接口。
ADD LOGICINF:NAME="giif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_l2tp";

// 将指定 APN 绑定源端接口。
ADD L2TPRDSCLIENT:APN="apn-l2tp",INTERFACENAME="giif1/0/1";

// 系统进行 PPP 协商时所使用的参数。
SET PPPCFG:HOSTNAME="UPF",MRU=1500,TIMEOUT=3;

// 设置 APN 的 PPP 相关信息，支持 PPP 鉴权功能。
SET APNPPPACCESS: APN="apn-l2tp", AUTHENTICATION=ENABLE;

// （可选配置）设置 L2TP 业务加密。
SET L2TPN4KEY: N4KEYVALUE="*****", CFMN4KEYVALUE="*****";
```

> 来源：`AAA下发L2TP属性方式激活L2TP VPN_41487855.md`（"任务示例/脚本"完整原文）[EV-FK-04]

### 5.3 场景变体

| 变体 | 场景说明 | 核心差异 | 文档覆盖度 |
|------|---------|---------|-----------|
| 本地配置 - 主备 LNS | LOCALLNSMODE=REDUNDANCY，最多 2 个 LNS | FIRSTLNSIP/SECONDLNSIP | 完整 MML 脚本（场景5.1） |
| 本地配置 - 负荷分担 | LOCALLNSMODE=LOAD_SHARING，可配置 6 个 LNS | 需 ADD L2TPLNSINFO 配置多于 2 个的 LNS | 操作步骤说明提及，无独立脚本 |
| 本地配置 - LNS IPv6 | L2TP 组中对接的 LNS 自身地址是 IPv6 | 需 ADD L2TPLNSINFO 命令配置 | 操作步骤说明提及 |
| AAA 下发 - 主备 | RDSLNSMODE=REDUNDANCY，两 LNS Preference 相同 | SET APNL2TPATTR 指定 RDSLNSMODE | 完整 MML 脚本（场景5.2） |
| AAA 下发 - 基于 Preference | RDSLNSMODE=TUNNEL_PREFER | Preference 不同为主备，相同为负荷分担 | 操作步骤说明提及 |
| IPv6 用户接入 | SUPPORTIPV6=ENABLE，v02 20.6.0 起支持 | SET APNL2TPATTR SUPPORTIPV6=ENABLE | 参数说明覆盖 |
| IPv6 隧道 | v03 20.12.0 起 UDG-LNS 隧道支持 IPv6 | - | 版本信息覆盖 |
| 双栈降栈 | 双栈协商单栈失败，按地址来源决定是否降栈 | 见 §3.6 异常场景 | 流程说明覆盖 |
| N4 加密 | 增强 N4 接口 L2TP 私有信元安全 | SET L2TPN4KEY + 对端 SET L2TPKEY | 两个场景脚本均含可选步骤 |

---

## 6. 验证与调测

### 6.1 验证方法

#### 6.1.1 调测前提与目的

当运营商使用本地配置方式或 AAA 下发方式在 UDG 与对端网元之间建立 L2TP 隧道，利用公用网络以及接入网来为虚拟专用网提供接入服务时，需要通过调试手段检查 L2TP 隧道是否工作正常。

> 适用：PGW-U、UPF

#### 6.1.2 调测数据准备

| 类别 | 参数名称 | 取值样例 | 获取方法 |
|------|---------|---------|---------|
| ping 数据包 | VPN 实例名（VPNINSTANCE） | vpn_l2tp | ADD VPNINST |
| ping 数据包 | 逻辑接口 IPv4 地址（IPV4ADDRESS1） | 10.8.20.1 / 10.8.20.2 | ADD LOGICINF |
| ping 数据包 | 第一个 LNS IP 地址（FIRSTLNSIP） | 10.10.10.1 | ADD L2TPGROUP / AAA Server |
| 接口配置信息 | 逻辑接口名称（NAME） | giif1/0/0 / giif1/0/1 | ADD LOGICINF |
| L2TP 组配置 | L2TP 组号（GROUPID） | 1 | ADD L2TPGROUP |
| 测试终端 APN | APN 名称（APN） | apn-l2tp | LST APN |
| L2TP 用户信息 | MSISDN | 8613801040032 | 测试终端自带 |

工具：OM Portal 跟踪工具

> 来源：`调测基于本地配置方式激活的L2TP VPN_40342150.md`、`调测基于AAA下发L2TP属性方式激活的L2TP VPN_41487857.md`（"必备事项"）[EV-FK-08, EV-FK-13]

#### 6.1.3 调测执行步骤（本地配置方式，13步）

```
步骤1：查询 License 开关
  └── LST LICENSESWITCH:LICITEM="LKV3G5L2TP01"
      ENABLE → 步骤3；DISABLE → SET LICENSESWITCH 打开

步骤2：在 OM Portal 创建 Gi 接口跟踪任务
  └── 输入需跟踪的 Gi 逻辑接口名称

步骤3：L2TP 用户入网，查看 Gi 接口跟踪任务
  ├── 能跟踪到 UDG 与 LNS 之间的 IPCP 报文，收到 IPCP Configure Ack → 步骤4
  └── 跟踪不到 IPCP 报文 → 步骤5

步骤4：查询 L2TP 会话
  └── DSP L2TPSESSION: INTERFACENAME="giif1/0/0",TUNNELID=1,SESSIONID=2
      会话建立成功且 MSISDN 一致 → 调测结束
      会话建立失败 → 步骤5

步骤5：查询 L2TP 隧道
  └── DSP L2TPTUNNEL: SHOWTYPE=INTERFACE,INTERFACENAME="giif1/0/0",TUNNELID=1
      隧道建立成功 → 步骤13；失败 → 步骤6

步骤6：PING 验证连通性（★关键）
  └── PING: IPVERSION=IPv4, VPNNAME=vpn_12tp, SOURCEIPV4ADDRESS=10.8.20.1, DESTIPV4ADDRESS="10.10.10.1"
      注：必须指定 SOURCEIPV4ADDRESS 为 UDG 逻辑接口 IP；VPN 实例需指定 VPNNAME
      收到响应 → 步骤10；timeout → 步骤7

步骤7：查询路由
  └── DSP ROUTE:VRFNAME="vpn_12tp",PREFIX="10.10.10.1"
      路由正确 → 步骤13；错误/缺失 → 步骤8

步骤8：重新配置路由
  └── ADD SRROUTE / MOD SRROUTE 后返回步骤6

步骤9：查询 Giif 接口与路由出接口的 VPN 实例一致性
  └── LST LOGICINF + LST INTERFACE，不同 VPN 则 MOD LOGICINF 修改

步骤10：查询 L2TP 组配置
  └── LST L2TPGROUP:GROUPID=1，与规划不一致则 ADD L2TPGROUP 更改

步骤11：查询 PPP 配置
  └── LST PPPCFG，与规划不一致则 SET PPPCFG 更改

步骤12：查询 APN L2TP 配置
  └── LST APNL2TPATTR:APN="apn-l2tp"
      未使能 L2TP 或未绑定 L2TP 组 → SET APNL2TPATTR 修正

步骤13：收集信息并寻求技术支持
  ├── OM Portal Gi 接口跟踪任务保存报文
  ├── EXP MML 导出当前配置
  ├── DSP ROUTE 保存路由信息
  ├── LST INTERFACE 保存接口信息
  ├── 收集对端设备配置及接口状态
  └── 联系华为技术支持
```

> 来源：`调测基于本地配置方式激活的L2TP VPN_40342150.md`（"操作步骤"13步完整流程）[EV-FK-08]

#### 6.1.4 调测执行步骤（AAA 下发方式，13步）

与本地配置方式主要差异：
- 步骤2：额外创建 UDG N4 接口跟踪任务，选择 PPP 和 L2TP 消息类型
- 步骤6：检查 N4 接口跟踪任务中 PGW-C/SMF 在 PFCP Session Establishment Request 下发的 L2TP 属性值与规划是否一致；不一致则请求修改 AAA 配置
- 步骤8-11：PING、路由、接口查询流程相同
- 步骤12：查询 LST APNL2TPATTR 验证 L2TP 使能（无需验证 L2TP 组绑定，因 LNS 信息由 AAA 下发）

> 来源：`调测基于AAA下发L2TP属性方式激活的L2TP VPN_41487857.md`（"操作步骤"13步完整流程）[EV-FK-13]

### 6.2 告警参考

| 告警ID | 告警名称 | 触发条件 | 影响 |
|--------|---------|---------|------|
| ALM-81053 | LNS 无响应 | 主 LNS 故障时，UDG 与主 LNS 的 L2TP 隧道断开 | UDG 与备 LNS 建立 L2TP 隧道；告警恢复后新用户业务报文优先发往主 LNS |

> 来源：`GWFD-020412 L2TP VPN参考信息_40342151.md`（"告警"章节）、`本地配置方式激活L2TP VPN_40342129.md`（步骤3说明）[EV-FK-02, EV-FK-03]

### 6.3 软参

| 软参 | 说明 |
|------|------|
| BIT571 | 当 LNS 为主备模式时，控制系统在发送 SCCRQ 消息后收到 LNS 发送的 StopCCN 消息时的处理原则 |
| BIT791 | 控制系统是否支持 L2TP 组和 L2TP 隧道下的隧道密码更新 |
| BIT1169 | 控制系统与 LNS 进行 PPP 初始协商时，系统发送的 PPP 信令消息是否携带地址域和控制域 |
| Byte671 bit7 | **★应用限制关键软参**。需设置为 1 关闭快速流表功能，否则 L2TP 场景下可能导致报文被丢弃（通过 SET SOFTPARAOFBIT 配置） |

> 来源：`GWFD-020412 L2TP VPN参考信息_40342151.md`（"软参"章节）、`GWFD-020412 L2TP VPN特性概述_40342127.md`（"应用限制"章节 Byte671）[EV-FK-02, EV-FK-01]

### 6.4 测量指标

本特性相关测量指标丰富（40+ 项），按维度分类：

| 指标类别 | 代表指标 | 说明 |
|---------|---------|------|
| L2TP 控制报文 | 1914316300 收到 L2TP 控制报文数 / 1914316302 发送 L2TP 控制报文数 / 1914316301 无效 L2TP 控制报文数 | UDG 收发 L2TP 控制报文统计 |
| L2TP 隧道建立 | 1914316303 建立隧道尝试次数 / 1914316304 建立隧道成功次数 / 1914316310 在线 L2TP 隧道数 | 隧道建立成功率与在线数 |
| L2TP 会话 | 1914316305 建立会话尝试次数 / 1914316306 建立会话成功次数 / 1914316307 在线 L2TP 会话数 / 1914316308 会话最大数量 / 1914316309 去活会话成功次数 | 会话建立成功率与在线数 |
| StopCCN/CDN 报文 | 1914316311/1914316312 发送/收到 StopCCN 报文数 / 1914316313/1914316314 发送/收到 CDN 报文数 | 隧道与会话拆除统计 |
| PPP 协商 | 1914316400/1914316401 收到/发送 PPP 协商包次数 / 1914316402 无效 PPP 协商包数 / 1914316403 IPCP 协商成功次数 / 1914316404 IPCP 协商尝试次数 | PPP 协商成功率 |
| LNS 分配地址会话 | 1914307757-1914307777 系列（LNS 分配 IPv6 / LNS 分配 IPv4+IPv6 / 外部 IPv4+LNS 分配 IPv6 的会话数） | **★地址分配主体验证**。指标明确按"LNS 分配"维度统计，证实 L2TP 用户地址由 LNS 分配 |
| 多维度（APN/CP/POD） | 1914307993-1914308012（指定 APN/DNN）、1914314013-1914314019（指定控制平面）、1914318629-1914318648（指定 POD） | 多维度会话统计 |

> 来源：`GWFD-020412 L2TP VPN参考信息_40342151.md`（"测量指标"章节 40+ 项指标完整列表）[EV-FK-02]

### 6.5 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| L2TP VPN 未生效 | APN 下 L2TPSWITCH 未使能 | LST APNL2TPATTR 查询；DISABLE 则 SET APNL2TPATTR L2TPSWITCH=ENABLE |
| L2TP 业务失败 | 启用了 L2TPN4KEY 加密但对端 SMF 未开启或密钥不一致 | 核对两端加密开关与密钥；建议两端同时 ENABLE 并配置相同密钥 |
| L2TP 隧道无法建立 | UDG 到 LNS 链路不通 | PING 指定源 IP 与 VPN 实例验证连通性；检查路由（DSP ROUTE） |
| Giif 接口与路由出接口 VPN 不一致 | 接口与路由分属不同 VPN 实例 | LST LOGICINF + LST INTERFACE 核对；MOD LOGICINF 统一 VPN 实例 |
| L2TP 组配置与规划不一致 | L2TPGROUP 参数错误 | LST L2TPGROUP 核对；ADD L2TPGROUP 更正 |
| PPP 协商参数不一致 | PPPCFG 配置错误 | LST PPPCFG 核对；SET PPPCFG 更正 |
| L2TP 用户激活失败 | License 未加载或开关未打开 | LST LICENSESWITCH；DISABLE 则 SET LICENSESWITCH 打开 |
| AAA 下发方式 LNS 参数不一致 | AAA Server 配置错误或 N4 下发错误 | 检查 N4 接口跟踪任务 PFCP Session Establishment Request 中 L2TP 属性值 |
| 主 LNS 故障 | 主 LNS 不可达 | 检查 ALM-81053 告警；UDG 自动切换备 LNS |
| 快速流表场景报文丢弃 | 未关闭快速流表 | SET SOFTPARAOFBIT Byte671 bit7=1 |
| 双栈用户激活失败 | 双栈地址都是外部分配且单栈协商失败 | 不允许降栈；检查外部分配地址协商链路 |

---

## 7. 参考信息

### 7.1 与其他特性的关系

| 关联特性 | 特性ID | 关系说明 |
|---------|--------|---------|
| 地址分配方式（配置树父节点，推断） | GWFD-010104（UDG） | 配置树父节点关系推断（Stage 3 验证） |
| 用户面地址分配（本地分配方式） | GWFD-010105（UDG） | **语义互斥**：L2TP 用户地址由 LNS 远程分配，与 GWFD-010105 的基于 APN/DNN、基于 SMF 本地分配是并行方案；一个用户要么走 L2TP，要么走本地 |
| **用户面地址自动检测（互斥）** | GWFD-010108（UDG） | **★文档明确互斥**：L2TP VPN 不支持与用户面地址自动检测功能同时应用 |
| 基于位置的地址分配（语义互斥） | GWFD-020421（UDG） | **语义级互斥**（文档未明确声明）：地址分配主体不同（LNS 远程 vs UDG 位置本地池），逻辑上一个用户只能由一方分配地址。Stage 3 横向分析待验证 |
| **入不转板功能（互斥）** | GWFD-020482（UDG） | **★文档明确互斥**：APN 下开启 L2TP VPN 特性，则不支持入不转板功能 |
| L2TP VPN（UNC 侧 C-U 协同对端） | WSFD-104410（UNC） | **C-U 协同分工**：UNC 决策+下发 LNS 参数；UDG 作为 LAC 执行隧道封装与 PPP 协商透传 |
| 控制面地址分配方式（配置树父节点，推断） | WSFD-010504（UNC） | UNC 侧配置树父节点关系推断（Stage 3 验证） |
| 地址分配方式（UNC 本地 4 种） | WSFD-010502（UNC） | **互斥关系**：L2TP 远程分配与 WSFD-010502 的 UDM/Radius/SMF 本地池/DHCP 本地分配是并行方案 |
| AAA Radius 鉴权接入 | WSFD-011305（UNC） | AAA 下发方式时 LNS 参数通过 AAA Access-Accept 下发（依赖 Radius 鉴权链路） |
| Radius 功能 | WSFD-011306（UNC） | Radius 服务器配置（AAA 下发方式时 LNS 参数在 Radius 侧配置） |
| 会话管理 | GWFD-010101（UDG） | PDU/PDP/承载会话建立的宿主特性 |
| 支持 Routing Behind MS（UNC） | WSFD-205101（UNC） | **同 APN 互斥**（UNC 侧声明）：L2TP VPN 已通过 LNS 实现 Routing Behind MS，同一 APN 下无需同时部署 |

### 7.2 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/GWFD-020412 L2TP VPN特性概述_40342127.md` | 适用NF（PGW-U/UPF + PGW-C/SMF可选 + LNS）、定义（UDG与LNS之间建立L2TP VPN）、客户价值、应用场景、可获得性（UDG 20.3.2+/UNC 20.3.2+、License 82200BVC LKV3G5L2TP01）、与其他特性的交互（★互斥GWFD-010108/GWFD-020482）、对系统影响（激活时延增加+封装性能影响）、应用限制（8条：LNS必须部署/不支持PPP用户/不支持DHCP延迟分配IPv4/不支持IPv6 PD/不支持PFC/ACFC/不支持NAT/NP加速不支持IPv6/需关闭快速流表Byte671 bit7=1）、原理概述（解GTP封装+LAC+PPP封装+图1 4G PPP再生+图2 5G PPP再生）、计费话单（无）、特性规格（本地L2TP Group 1500/AAA方式Group 1500）、遵循标准（3GPP 23.214/29.244 + RFC 2661/2868/5072/5571/8064）、发布历史（v01 20.3.2 / v02 20.6.0 IPv6用户 / v03 20.12.0 IPv6隧道） |
| 2 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/GWFD-020412 L2TP VPN参考信息_40342151.md` | MML命令清单（8条核心：ADD L2TPGROUP/SET GLOBALL2TP/SET APNL2TPATTR/ADD LOGICINF/ADD L2TPCLIENTIP/ADD L2TPRDSCLIENT/SET PPPCFG/SET APNPPPACCESS）、告警（ALM-81053 LNS无响应）、软参（BIT571/BIT791/BIT1169）、测量指标（40+项：L2TP控制报文/隧道建立/会话建立/StopCCN-CDN/PPP协商/LNS分配地址会话/多维度APN-CP-POD） |
| 3 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/激活L2TP VPN/本地配置方式激活L2TP VPN_40342129.md` | 本地配置方式激活场景、必备数据表（30+参数覆盖8条命令）、11步操作步骤（License开关→VPN实例→L2TP组→GLOBALL2TP→APNL2TPATTR→关闭快速流表→Giif→L2TPCLIENTIP→PPPCFG→APNPPPACCESS→L2TPN4KEY）、L2TP组主备/负荷分担说明、ALM-81053告警切换说明、ADD L2TPLNSINFO使用场景（6个以上LNS或IPv6 LNS）、L2TPN4KEY加密对称性约束、完整MML脚本（SET LICENSESWITCH/ADD VPNINST/ADD L2TPGROUP/SET GLOBALL2TP/ADD APN/SET APNL2TPATTR/SET SOFTPARAOFBIT/ADD LOGICINF/ADD L2TPCLIENTIP/SET PPPCFG/SET APNPPPACCESS/SET L2TPN4KEY） |
| 4 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/激活L2TP VPN/AAA下发L2TP属性方式激活L2TP VPN_41487855.md` | AAA下发方式激活场景（PGW-U/UPF本地不需配置L2TP组）、必备数据表（SET GLOBALL2TP扩展参数PPPMAGICNUMBER/MAXSENDWINSIZE/INITTUNNELNUM/MAXSESSIONNUM + SET APNL2TPATTR的RDSLNSMODE参数）、10步操作步骤、RDSLNSMODE三种工作模式说明（REDUNDANCY/TUNNEL_PREFER主备/负荷分担）、ADD L2TPRDSCLIENT使用（APN绑定源端接口）、完整MML脚本 |
| 5 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/实现原理/L2TP激活流程_76399675.md` | L2TP激活流程图1（端到端11步：UE激活请求→可选AAA获取LNS→PFCP下发→L2TP隧道建立SCCRQ/SCCRP/SCCCN→L2TP会话建立ICRQ/ICRP/ICCN→PPP协商LCP/PAP-CHAP/IPCP-IPv6CP→PFCP Response→PFCP Modification→Create Session Response）、隧道重传机制（1s/2s/4s/8s/16s，默认3次）、ICRQ Calling-number AVP（MSISDN/IMSI/IMEI由ICRQ_CALLINGNO配置）、★地址分配原则（L2TP用户地址由LNS分配，即使本地配置地址池或AAA下发地址）、IPv6地址=网络前缀+接口ID、异常场景（双栈转单栈规则、SUPPORTIPV6=DISABLE单栈限制）、PPP协商流程图2（LCP Configure Nak/Reject/Ack + PAP两次握手 + CHAP三次握手 + IPCP双向协商）、★鉴权方式转换（PAP→CHAP/PAP→不鉴权/CHAP→不鉴权，不支持反向） |
| 6 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/实现原理/L2TP查表流程_19990150.md` | L2TP建立过程图1、查表判定逻辑（AAA下发方式使用PFCP携带LNS参数；本地配置方式UDG根据本地L2TPGROUP建立）、方式A/B触发条件 |
| 7 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/实现原理/L2TP隧道维护流程_32553703.md` | L2TP隧道维护图1、Hello报文检测机制（UDG与LNS定时发送Hello）、Hello参数（默认60秒，ADD L2TPGROUP配置开关/间隔/最大次数）、ZLB确认机制、重发规则（2s/4s/8s/16s，最大次数后发StopCCN拆隧道） |
| 8 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/实现原理/L2TP去激活流程_19990151.md` | 4类去激活流程图1-4（UE/PGW-C-SMF发起 + PGW-U-UPF主动发起DEA SESSION + LNS发起 + LNS单栈释放）、CDN/StopCCN/ZLB消息交互、PFCP Session Delete/Report上报流程 |
| 9 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/调测L2TP VPN/调测基于本地配置方式激活的L2TP VPN_40342150.md` | 本地配置方式调测13步完整流程（LST LICENSESWITCH→OM Portal Gi跟踪→用户入网查IPCP→DSP L2TPSESSION→DSP L2TPTUNNEL→PING指定源IP和VPN→DSP ROUTE→ADD-MOD SRROUTE→LST LOGICINF+INTERFACE核对VPN→LST L2TPGROUP→LST PPPCFG→LST APNL2TPATTR→收集信息EXP MML）、调测数据表、PING必须指定SOURCEIPV4ADDRESS和VPNNAME的关键提示 |
| 10 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/调测L2TP VPN/调测基于AAA下发L2TP属性方式激活的L2TP VPN_41487857.md` | AAA下发方式调测13步流程（差异：步骤2额外创建UDG N4接口跟踪任务选PPP和L2TP消息类型；步骤6检查N4跟踪PFCP Establishment Request中L2TP属性值；步骤7请求修改AAA配置）、调测数据表 |
| 11 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/相关术语/L2TP_51067102.md` | L2TP术语定义（IETF起草，结合PPTP和L2F优点）、控制消息和数据消息（控制消息可靠传输支持重传和流量控制；数据消息不可靠不重传）、控制连接和会话连接、隧道和会话（Tunnel ID和Session ID由对端分配） |
| 12 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/相关术语/LAC_51067103.md` | LAC术语定义（附属在交换网络上的具有PPP端系统和L2TP协议处理能力的设备；UDG作为LAC为UE提供接入服务） |
| 13 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/相关术语/LNS_51067104.md` | LNS术语定义（PPP端系统上处理L2TP协议服务器端设备，通常是企业网边缘设备；UDG支持主备或负荷分担方式LNS通信） |
| 14 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN/相关术语/PPP协议_51525531.md` | PPP协议术语定义（TCP/IP数据链路层协议；包括LCP链路控制协议族、CHAP/PAP验证协议族、NCP网络控制协议族如IPCP/IPv6CP） |
| 15 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/组网功能/GWFD-020412 L2TP VPN_40342126.md` | 特性根索引文件（仅标题"GWFD-020412 L2TP VPN"，无实质内容） |

### 7.3 关键术语速查

| 术语 | 全称 | 说明 |
|------|------|------|
| L2TP | Layer Two Tunneling Protocol | 二层隧道协议，VPDN 隧道协议的一种 |
| VPDN | Virtual Private Dial-up Network | 虚拟私有拨号网 |
| LNS | L2TP Network Server | 企业网边缘设备，L2TP 隧道服务器端 |
| LAC | L2TP Access Concentrator | L2TP 接入集中器，由 PGW-U/UPF（UDG）承担 |
| PPP | Point-to-Point Protocol | L2TP 内层链路层协议 |
| LCP | Link Control Protocol | PPP 链路建立阶段协议，协商 MRU 和鉴权类型 |
| IPCP / IPv6CP | IP Control Protocol | PPP 网络层协商协议，IPv4/IPv6 地址分配发生于此 |
| PAP / CHAP | Password / Challenge-Handshake Authentication Protocol | PPP 鉴权协议（PAP 两次握手明文 / CHAP 三次握手仅传用户名） |
| PFCP | Packet Forwarding Control Protocol | 5G/4G C-U 分离控制面协议 |
| Sx / N4 | 4G / 5G C-U 接口 | LNS 参数下发通道 |
| APNL2TPATTR | APN L2TP 属性 | ★本特性 U 面核心配置对象（SET APNL2TPATTR） |
| APNL2TPCTRL | APN L2TP CTRL | C 面（WSFD-104410）核心配置对象（SET APNL2TPCTRL），U 面不使用 |
| L2TPGROUP | L2TP 组 | 本地配置方式 LNS 容器（ADD L2TPGROUP） |
| GLOBALL2TP | L2TP 缺省配置 | 本端名/HELLO/重发等缺省参数（SET GLOBALL2TP） |
| L2TPN4KEY / L2TPKEY | N4 接口 L2TP 加密密钥 | U 面 SET L2TPN4KEY / C 面 SET L2TPKEY |
| LOCALLNSMODE | 多 LNS 工作模式 | REDUNDANCY（主备）/ LOAD_SHARING（负荷分担） |
| RDSLNSMODE | RADIUS 返回多 LNS 模式 | REDUNDANCY / TUNNEL_PREFER（AAA 下发方式） |
| SUPPORTIPV6 | L2TP 支持 IPv6 开关 | SET APNL2TPATTR 参数，DISABLE 时仅支持 IPv4 |
| ICRQ_CALLINGNO | ICRQ Calling-number AVP | MSISDN / IMSI / IMEI |
| Byte671 bit7 | 快速流表软参 | 需置 1 关闭快速流表（L2TP 场景应用限制） |

---

## 8. 文档一致性说明（配置树 vs 产品文档 vs WSFD-104410）

> 配置树仅用于定位特性 ID，以下记录以产品文档实际内容为准时发现的差异与协同点，供 Stage 3 横向分析参考。

### 8.1 与任务要求中提及对象的核对（★重点澄清）

| # | 任务要求提及 | 产品文档实际 | 核对结论 |
|---|-------------|-------------|---------|
| 1 | **APNL2TPATTR 配置** | **★确认存在且是核心对象**。`SET APNL2TPATTR` 是本特性 U 面的核心使能命令，参考信息明确列出，激活文档必备数据表详细列出 10 个参数（APN/L2TPSWITCH/SUPPORTIPV6/L2TPGROUPID/RDSLNSMODE/ICRQ_CALLINGNO/ICCN_AUTH/IPCP_NEGO/DOMAINNAMEACT/DOMAINNAMEPOS） | **澄清确认**：`APNL2TPATTR` 是 U 面（GWFD-020412）真实存在的核心配置对象，与 C 面（WSFD-104410）的 `APNL2TPCTRL` 不同。C-U 两侧配置对象命名不对称：U 面 ATTR，C 面 CTRL |
| 2 | **APNADDRESSATTR 配置** | **未出现该对象**。15 篇 GWFD-020412 文档（含特性概述、参考信息、激活×2、调测×2、实现原理×4、相关术语×4、根索引）均未提及 `APNADDRESSATTR` | **澄清**：`APNADDRESSATTR` 并非 GWFD-020412 文档定义的对象，任务要求中的命名与文档不一致；与 C 侧 WSFD-104410 结论一致（C 侧也未出现）。可能为 Stage 3 横向分析时识别的聚合概念，与本特性无直接配置关系 |
| 3 | L2TP 隧道/LNS 地址分配机制 | 文档明确：UDG 作为 LAC 与 LNS 建立 L2TP 隧道（SCCRQ/SCCRP/SCCCN + ICRQ/ICRP/ICCN），内层 PPP 三阶段协商中由 LNS 分配企业内网 IP | 已覆盖（见 §3.2 阶段 4-6） |
| 4 | LCP/鉴权/网络协商三阶段 | 文档完整展开（L2TP激活流程_76399675.md 图2 PPP协商流程），包括 LCP Configure Nak/Reject/Ack、PAP/CHAP、IPCP/IPv6CP 双向协商、鉴权方式转换规则 | 已覆盖（见 §3.2 阶段 6） |
| 5 | 与 WSFD-104410 C-U 对称 | C 面决策+下发 / U 面 LAC 执行隧道封装+PPP 协商；C 面无 License，U 面必须 License；C 面 APNL2TPCTRL，U 面 APNL2TPATTR | 已覆盖（见 §3.3） |
| 6 | 与 GWFD-020421（位置区）互斥 | **文档未明确声明互斥**。GWFD-020412 特性概述"与其他特性的交互"仅列 GWFD-010108 和 GWFD-020482 两条互斥；未提及 GWFD-020421 | **语义级互斥推断**：地址分配主体不同（LNS 远程 vs UDG 位置本地池），逻辑上一个用户只能由一方分配。Stage 3 横向分析需结合 GWFD-020421 文档验证是否双向声明 |
| 7 | 与 GWFD-010108（地址检测）互斥 | **文档明确声明互斥**。特性概述"与其他特性的交互"章节明确：L2TP VPN 不支持与用户面地址自动检测功能同时应用 | 已确认（见 §1.6、§4.4、§7.1） |

### 8.2 与配置树/文档清单的差异

| # | 维度 | 配置树/文档清单描述 | 产品文档实际内容 | 差异类型 |
|---|------|---------------------|-----------------|---------|
| 1 | 文件数 | 文档清单列 15 个文件 | 实际 1 个根索引文件为空（仅标题），实质内容 14 篇（特性概述+参考信息+激活×2+调测×2+实现原理×4+相关术语×4） | 补全：根索引无内容 |
| 2 | 命令清单覆盖度 | 参考信息列 8 条命令 | 激活文档额外涉及 6 条辅助命令（SET LICENSESWITCH/ADD VPNINST/ADD APN/SET SOFTPARAOFBIT/SET L2TPN4KEY/ADD L2TPLNSINFO）+ 10+ 条调测查询命令 | 补全：参考信息命令清单不完整 |
| 3 | License要求 | 文档清单标注"[★核心]" | 产品文档明确声明"**必须 License** 82200BVC LKV3G5L2TP01"；UNC 侧 WSFD-104410 无 License | C-U 不对称：UDG 必须 License，UNC 无 License |
| 4 | 子方式分类 | 文档清单概括："LNS分配(UPF侧,L2TP隧道PPP协商)" | UDG 侧实际承担 LAC + PPP 再生 + 隧道封装全流程；地址分配主体为 LNS（企业网侧），UPF 仅透传 | 描述准确：清单描述符合 U 面角色 |
| 5 | 遵循标准 | 配置树无 | UDG 引用 7 条（3GPP 23.214/29.244 + RFC 2661/2868/5072/5571/8064）；UNC 仅引用 2 条 CUPS 标准 | C-U 互补：U 面多引用 L2TP 协议族 + RADIUS 隧道属性 + PPP IPv6 + 稳定 IID |
| 6 | 与父节点关系 | 配置树父节点推断为 GWFD-010104 | 本特性 15 篇文档**未直接提及** GWFD-010104 | 推断关系，Stage 3 验证 |
| 7 | 方式A/B 分类 | 文档清单未明确 | 产品文档明确分"本地配置方式"（ADD L2TPGROUP + ADD L2TPCLIENTIP）和"AAA下发方式"（ADD L2TPRDSCLIENT，无本地组）两条独立激活路径 | 补全：清单未区分两种激活方式 |

### 8.3 与 WSFD-104410（UNC 侧）的 C-U 协同与不一致

| # | 维度 | GWFD-020412（UDG/U面） | WSFD-104410（UNC/C面） | 协同/差异 |
|---|------|------------------------|------------------------|----------|
| 1 | 角色定位 | LAC + L2TP 隧道封装 + PPP 再生与协商透传执行方 | 决策方 + LNS 参数下发方 | **C-U 协同分工**：决策+参数在 C 面，隧道执行+PPP 协商在 U 面 |
| 2 | 网元角色 | PGW-U / UPF（用户面） | GGSN / PGW-C / SMF（控制面） | C-U 分离 |
| 3 | **★核心配置对象** | **APNL2TPATTR**（`SET APNL2TPATTR`，10+ 参数） | **APNL2TPCTRL**（`SET APNL2TPCTRL`，2 参数 APN/L2TPSWITCH） | **C-U 配置对象不对称**：U 面对象参数远多于 C 面（U 面承担实际隧道执行，需配置 L2TP 组/信元/协商等细节） |
| 4 | License | 必须 License `82200BVC LKV3G5L2TP01` | **无 License** | **C-U License 不对称**（差异点） |
| 5 | 特性规格 | 本地 L2TP Group 1500 / AAA 下发方式 Group 1500 | L2TP 隧道信息 20 个 | 规格维度不同（U 面按 Group 1500，C 面按隧道信息 20） |
| 6 | 互斥特性 | GWFD-010108（地址自动检测）、GWFD-020482（入不转板）+ 多项 U 面约束（不支持 DHCP 延迟分配 IPv4 / 不支持 IPv6 PD / NP 加速不支持 IPv6 / 不支持 PPP 用户 / 不支持 PFC-ACFC / 不支持 NAT / 需关闭快速流表） | WSFD-205101（Routing Behind MS）同 APN 无需同时部署 | **互斥维度不对称**：U 面互斥约束多（涉及 U 面加速/地址检测/PPP/PD/NAT/快速流表），C 面仅声明同 APN 互斥 |
| 7 | 标准 | 3GPP 23.214/29.244 + RFC 2661/2868/5072/5571/8064（7条） | 3GPP 23.214/29.244（2条） | U 面多引用 L2TP 协议族 + PPP IPv6 + RADIUS 隧道属性 |
| 8 | 版本起点 | UDG 20.3.2 | UNC 20.3.2 | C-U 版本对齐 |
| 9 | IPv6 支持 | v02 20.6.0 支持 IPv6 用户；v03 20.12.0 隧道支持 IPv6 地址 | v02 20.6.0 支持 IPv6 用户接入 | C-U 两侧均在 v02 起支持 IPv6 用户；U 面 v03 额外支持 IPv6 隧道 |
| 10 | 对系统影响 | 用户激活时延增加 + 报文 L2TP 封装性能影响 | 无影响 | 性能影响集中在 U 面 |
| 11 | 告警/软参/指标 | 告警 ALM-81053 + 软参 BIT571/BIT791/BIT1169/Byte671bit7 + 测量指标 40+项 | **全部为"无"** | 运维观测点在 U 面侧 |
| 12 | 地址分配主体 | LAC 不分配地址（仅封装透传 PPP 协商） | UNC 不分配地址（仅下发参数） | **地址分配主体为 LNS**（企业网侧） |
| 13 | N4 加密 | SET L2TPN4KEY（U 面） | SET L2TPKEY（C 面） | C-U 加密配置点不同，需两端同时配置相同密钥 |
| 14 | AAA 下发方式 | 使用 ADD L2TPRDSCLIENT 绑定 APN 与源端接口 | 通过 SET APNL2TPCTRL L2TPSWITCH=ENABLE 使能（依赖 AAA Access-Accept） | C-U 协同：C 面使能+AAA 鉴权，U 面准备源端接口接收 N4 下发参数 |
| 15 | 本地配置方式 | 使用 ADD L2TPGROUP + ADD L2TPCLIENTIP 配置本地 LNS | 无对应本地配置（C 面仅使能开关） | U 面独立承担本地 LNS 配置（不依赖 C 面） |

---

## 附录 A：与 WSFD-104410 的 C-U 对照速查表

| 对照维度 | GWFD-020412（UDG）★本特性 | WSFD-104410（UNC） |
|---------|--------------------|--------------------|
| 网元角色 | PGW-U / UPF（用户面） | GGSN / PGW-C / SMF（控制面） |
| L2TP 角色 | LAC（L2TP Access Concentrator） | 决策+LNS 参数下发 |
| 地址分配主体 | 不分配（LAC 透传 PPP 协商） | 不分配（仅下发参数） |
| **★核心配置对象** | **APNL2TPATTR**（SET APNL2TPATTR，10+参数） | **APNL2TPCTRL**（SET APNL2TPCTRL，2参数） |
| License | 82200BVC LKV3G5L2TP01（必须） | 无 |
| 特性规格 | L2TP Group 1500（本地+AAA 各 1500） | 隧道信息 20 个 |
| 互斥特性 | GWFD-010108 / GWFD-020482 + 8项 U 面约束 | WSFD-205101 同 APN 互斥 |
| 标准 | 3GPP 23.214/29.244 + RFC 2661/2868/5072/5571/8064（7条） | 3GPP 23.214/29.244（2条） |
| 版本起点 | UDG 20.3.2 | UNC 20.3.2 |
| 核心激活命令 | SET APNL2TPATTR + ADD L2TPGROUP（方式A）/ ADD L2TPRDSCLIENT（方式B） | SET APNL2TPCTRL |
| N4 加密 | SET L2TPN4KEY（U 面，可选） | SET L2TPKEY（C 面，可选） |
| 告警/软参/指标 | 有（ALM-81053 + 3软参 + Byte671bit7 + 40+指标） | 无 |
| 对系统影响 | 有（激活时延+封装开销） | 无 |
| 决策/执行 | 执行方（无决策权，接收 C 面参数或本地配置） | 决策方（参数下发） |
| 调测复杂度 | 高（13步调测流程，涉及License/隧道/会话/路由/接口/PPP/APN 6层排查） | 低（3步调测：LST APNL2TPCTRL → SET APNL2TPCTRL → 终端测试） |

---

## 附录 B：source_evidence_ids 占位映射

| evidence_id | 对应来源文件 | 主要贡献章节 |
|-------------|-------------|-------------|
| EV-FK-01 | `GWFD-020412 L2TP VPN特性概述_40342127.md` | 适用NF、定义、客户价值、应用场景、可获得性（License必须）、与其他特性交互（互斥010108/020482）、对系统影响、应用限制（8条）、原理概述（PPP再生）、计费话单（无）、特性规格（Group 1500×2）、遵循标准（7条）、发布历史 |
| EV-FK-02 | `GWFD-020412 L2TP VPN参考信息_40342151.md` | MML命令清单（8条核心）、告警（ALM-81053）、软参（BIT571/BIT791/BIT1169）、测量指标（40+项） |
| EV-FK-03 | `本地配置方式激活L2TP VPN_40342129.md` | 本地配置方式激活场景、必备数据表（30+参数）、11步操作步骤、L2TP组主备/负荷分担说明、ALM-81053切换说明、ADD L2TPLNSINFO场景、L2TPN4KEY加密对称性、完整MML脚本 |
| EV-FK-04 | `AAA下发L2TP属性方式激活L2TP VPN_41487855.md` | AAA下发方式激活场景、必备数据表（含RDSLNSMODE）、10步操作步骤、RDSLNSMODE三种工作模式、ADD L2TPRDSCLIENT使用、完整MML脚本 |
| EV-FK-05 | `实现原理/L2TP激活流程_76399675.md` | L2TP激活流程图1（11步端到端）、隧道重传机制、ICRQ Calling-number AVP、★地址分配原则（LNS分配）、IPv6地址组成、异常场景（双栈降栈）、PPP协商流程图2（LCP/PAP-CHAP/IPCP-IPv6CP）、★鉴权方式转换规则 |
| EV-FK-06 | `实现原理/L2TP查表流程_19990150.md` + `实现原理/L2TP去激活流程_19990151.md` | 查表判定逻辑（方式A/B触发）、4类去激活流程（UE/PGW-U-UPF/LNS发起+LNS单栈释放）、CDN/StopCCN/ZLB消息交互 |
| EV-FK-07 | `实现原理/L2TP隧道维护流程_32553703.md` | Hello报文检测机制、Hello参数（60秒默认，ADD L2TPGROUP配置）、ZLB确认、重发规则（2s/4s/8s/16s，StopCCN拆隧道） |
| EV-FK-08 | `调测L2TP VPN/调测基于本地配置方式激活的L2TP VPN_40342150.md` | 本地配置方式调测13步完整流程、调测数据表、PING指定源IP和VPN关键提示、DSP L2TPSESSION/DSP L2TPTUNNEL 示例输出 |
| EV-FK-09 | `相关术语/L2TP_51067102.md` | L2TP术语定义、控制消息和数据消息、控制连接和会话连接、隧道和会话（Tunnel ID/Session ID由对端分配） |
| EV-FK-10 | `相关术语/LAC_51067103.md` | LAC术语定义（UDG作为LAC为UE提供接入服务） |
| EV-FK-11 | `相关术语/LNS_51067104.md` | LNS术语定义（企业网边缘设备，UDG支持主备或负荷分担LNS） |
| EV-FK-12 | `相关术语/PPP协议_51525531.md` | PPP协议术语定义（LCP/CHAP-PAP/NCP协议族） |
| EV-FK-13 | `调测L2TP VPN/调测基于AAA下发L2TP属性方式激活的L2TP VPN_41487857.md` | AAA下发方式调测13步流程（含N4接口跟踪任务、AAA配置核对）、调测数据表 |
| EV-FK-14 | （保留，对应可能补充的命令参考文档，如 ADD L2TPGROUP / SET APNL2TPATTR 命令详述） | 命令参数详细说明（本知识文档激活文档已覆盖关键参数） |
| EV-FK-15 | `GWFD-020412 L2TP VPN_40342126.md` | 特性根索引（仅标题，无实质内容） |
