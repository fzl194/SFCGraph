# WSFD-104410 L2TP VPN 知识文档

> 聚焦 APN 业务域地址分配场景的 UNC（GGSN/PGW-C/SMF）控制面 L2TP VPN 特性
> 与 UDG 侧 GWFD-020412（用户面 L2TP 隧道执行）构成 C-U 协同分工
> 适用 NF：GGSN（2/3G）、PGW-C（4G）、SMF（5G）

---

## 0. 元数据（三层图谱Schema字段）

| 字段 | 取值 |
|------|------|
| feature_id | WSFD-104410 |
| feature_name | L2TP VPN |
| feature_group | 地址分配 |
| parent_feature_id | WSFD-010504（控制面地址分配方式，配置树父节点，推断） |
| applicable_nf_map | `{"UNC": ["GGSN", "PGW-C", "SMF"]}` |
| variant_dimensions | ["激活方式(本地配置使能APN L2TP开关 / AAA Server下发LNS参数)", "接入代际(2G&3G / 4G / 5G)", "LNS参数下发通道(Sx/N4接口PFCP私有信元)", "N4加密(SET L2TPKEY 加密/明文)", "用户IP类型(IPv4 / IPv6，v02起支持)"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-01, EV-FK-02, EV-FK-03, EV-FK-04, EV-FK-05] |
| license_required | 无（本特性无需License） |

---

## 1. 概述

### 1.1 特性定义（是什么）

利用 L2TP（Layer 2 Tunneling Protocol，二层隧道协议）与企业网的边缘设备 LNS（L2TP Network Server）之间建立 L2TP VPN，用户可以从固网、移动网等公共网络接入到企业的虚拟专用网。

本特性是**控制面（C 面）L2TP 触发与 LNS 参数下发特性的总集**：UNC 通过 AAA 鉴权接收 AAA Server 在 Access-Accept 消息中下发的 LNS 参数，或由本地 APN 配置使能 L2TP 功能，随后 GGSN/PGW-C/SMF 通过 **Sx/N4 接口将 LNS 参数下发到 PGW-U/UPF**；PGW-U/UPF 作为 LAC（L2TP Access Concentrator）与 LNS 之间建立 L2TP 隧道和会话。与 UDG 侧 GWFD-020412（L2TP VPN 用户面执行）形成 C-U 协同分工：C 面"决策+下发参数"，U 面"封装隧道+PPP 协商"。

> 来源：`output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104410 L2TP VPN/特性概述_46559213.md`（"定义"章节）[EV-FK-01]

### 1.2 适用NF（UDG/UNC网元）

| 涉及NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| GGSN | 控制面（UNC，2/3G） | UNC 20.3.2 及后续版本 | 通过 AAA Server 对 L2TP 用户进行鉴权，将 AAA Server 返回的 LNS 参数下发到 PGW-U/UPF |
| PGW-C | 控制面（UNC，4G） | UNC 20.3.2 及后续版本 | 同上（4G 承载通过 Sx 接口下发） |
| SMF | 控制面（UNC，5G） | UNC 20.3.2 及后续版本 | 同上（5G PDU 会话通过 N4 接口下发；R17 协议 SMF 关注 L2TP 相关 N4 接口信元变更） |
| PGW-U / UPF | 用户面（UDG） | UDG 20.3.2 及后续版本 | **非本特性主体 NF**，但作为 LAC 与 LNS 之间构建 L2TP 隧道并封装/解封装 L2TP 报文（详见 GWFD-020412） |
| LNS | 企业网边缘设备 | 无特殊需求 | LNS 封装/解封装 L2TP 报文 |

> 来源：`特性概述_46559213.md`（"可获得性/涉及NF"章节）[EV-FK-01]

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|---------|---------|---------|
| 04 | 20.11.2 | SMF 支持 L2TP 隧道信息数量为 20 个 |
| 03 | 20.9.0 | SMF 支持 L2TP 遵循 R17 标准 |
| 02 | 20.6.0 | L2TP VPN 支持 IPv6 用户接入 |
| 01 | 20.3.2 | 首次发布 |

> 来源：`特性概述_46559213.md`（"发布历史"章节）[EV-FK-01]

### 1.4 License

**本特性无需获得 License 许可即可获得该特性的服务**（与 UDG 侧 GWFD-020412 形成 C-U License 不对称：UDG 侧必须加载 License 控制项 `82200BVC LKV3G5L2TP01 L2TP VPN`）。

> 来源：`特性概述_46559213.md`（"可获得性/License 支持"章节）[EV-FK-01]
> UDG 侧 License 对比来源：`GWFD-020412 L2TP VPN特性概述_40342127.md`（UDG 文档）

### 1.5 前置条件与依赖

| 前置条件 | 说明 |
|---------|------|
| 企业网侧部署 LNS | **应用限制硬约束**：企业网侧必须部署 LNS 设备（否则 L2TP 隧道无法终结） |
| 已配置 APN | `SET APNL2TPCTRL` 命令的 APN 参数必须已通过 `ADD APN` 命令配置完成 |
| AAA Server 就绪（可选） | AAA 下发方式：AAA Server 在 Access-Accept 中携带 LNS 参数（本地配置方式可不依赖 AAA） |
| UDG 侧 L2TP License 已加载 | 对端 PGW-U/UPF 必须加载 `82200BVC LKV3G5L2TP01 L2TP VPN` License |
| C-U 版本对齐 | UNC 与 UDG 均需 20.3.2 及后续版本 |

> 来源：`特性概述_46559213.md`（"应用限制"章节）、`激活L2TP VPN_46559215.md`（"必备事项/数据"章节）[EV-FK-01, EV-FK-03]

### 1.6 与其他特性的交互

| 交互类型 | 相关特性 | 控制项名称 | 交互说明 |
|---------|---------|-----------|---------|
| 影响 | WSFD-205101 支持 Routing Behind MS（UNC） | - | L2TP VPN 通过 LNS 设备实现了 Routing Behind MS 功能，所以在**同一 APN 下，L2TP VPN 和 Routing Behind MS 无需同时部署** |

> 来源：`特性概述_46559213.md`（"与其他特性的交互"章节）[EV-FK-01]

### 1.7 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | 通过公网将远程企业用户接入到企业网，不需要建设专有网络，降低了运营商的建网成本 |
| 用户 | 企业用户可以通过公网接入企业网，节约了企业的网络使用费用 |

> 来源：`特性概述_46559213.md`（"客户价值"章节）[EV-FK-01]

### 1.8 应用场景

企业驻外机构和出差人员可远程经由公共网络，通过虚拟隧道实现和企业总部之间的网络连接，从而为企业、小型 ISP、移动办公人员等提供接入服务。

> 来源：`特性概述_46559213.md`（"应用场景"章节）[EV-FK-01]

### 1.9 对系统的影响

**本特性对系统无影响**（UNC C 面侧明确声明；UDG 侧另有性能声明）。

> 来源：`特性概述_46559213.md`（"对系统的影响"章节）[EV-FK-01]

### 1.10 应用限制

- **企业网侧必须部署 LNS 设备**（UNC 侧声明）
- 对端 UPF 需同时打开 L2TP 加密功能并配置相同密钥（若启用 `SET L2TPKEY` 加密）

> 来源：`特性概述_46559213.md`（"应用限制"章节）、`激活L2TP VPN_46559215.md`（"操作步骤/说明"）[EV-FK-01, EV-FK-03]

### 1.11 特性规格

| 规格名称 | 规格指标 |
|---------|---------|
| L2TP 隧道信息（个） | 20 |

> 来源：`特性概述_46559213.md`（"特性规格"章节）[EV-FK-01]
> 注：UNC 侧仅约束"隧道信息数量 20"，UDG 侧 GWFD-020412 另有"本地 L2TP Group 规格 1500 / AAA 下发方式下的 L2TP Group 规格 1500"。

### 1.12 计费与话单

**本特性不涉及计费与话单**。

> 来源：`特性概述_46559213.md`（"计费与话单"章节）[EV-FK-01]

### 1.13 遵循标准

| 标准类别 | 标准编号 | 标准名称 |
|---------|---------|---------|
| 3GPP | 23.214 | Architecture enhancements for control and user plane separation of EPC nodes |
| 3GPP | 29.244 | Interface between the Control Plane and the User Plane of EPC Nodes |

> 来源：`特性概述_46559213.md`（"遵循标准"章节）[EV-FK-01]
> 说明：UNC 侧两条标准均为 C-U 分离（CUPS）架构标准；UDG 侧 GWFD-020412 另引用 RFC 5571（L2TPv2 Softwire）。

---

## 2. 核心概念

### 2.1 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| L2TP | Layer 2 Tunneling Protocol，二层隧道协议 | VPDN 隧道协议的一种，在公共网络上建立安全的虚拟专网 |
| VPDN | Virtual Private Dial-up Network，虚拟私有拨号网 | 利用公共网络（ISDN/PSTN/PLMN）的拨号功能接入，实现 VPN |
| LNS | L2TP Network Server | 企业网边缘设备，L2TP 隧道的服务器端，封装/解封装 L2TP 报文 |
| LAC | L2TP Access Concentrator，L2TP 接入集中器 | L2TP 隧道的客户端，由 PGW-U/UPF（UDG）承担 |
| PPP | Point-to-Point Protocol，点对点协议 | L2TP 隧道内层承载的链路层协议；UE 与 LNS 之间通过 PPP 协商完成地址分配 |
| AAA | Authentication/Authorization/Accounting | 鉴权/授权/计费服务器，在 Access-Accept 中下发 LNS 参数 |
| Sx/N4 接口 | PFCP 接口（4G 为 Sx，5G 为 N4） | C 面与 U 面之间下发 LNS 参数的通道 |
| PFCP | Packet Forwarding Control Protocol | 5G/4G C-U 分离架构的控制面协议，承载 LNS 参数私有信元 |
| APN | Access Point Name | 接入点名称，`SET APNL2TPCTRL` 命令按 APN 粒度使能 L2TP 功能 |
| L2TPSWITCH | L2TP 功能开关 | `SET APNL2TPCTRL` 命令参数，ENABLE/DISABLE 控制 APN 下 L2TP 使能 |
| L2TPKEY | L2TP 加密密钥 | `SET L2TPKEY` 配置，控制 N4 接口 L2TP 私有信元的加密/明文 |

### 2.2 对象模型

WSFD-104410 在 UNC 侧的配置对象较轻量，核心是**按 APN 粒度的 L2TP 开关 + PFCP 私有信元下发通道 + 加密配置**，对象关系如下：

```
┌────────────────────────────────────────────────────────────────┐
│ UNC 侧配置对象（C 面：GGSN/PGW-C/SMF）                          │
│                                                                │
│   ┌──────────────┐                                             │
│   │  APN         │ ← 已通过 ADD APN 配置（外部对象）           │
│   └──────┬───────┘                                             │
│          │ SET APNL2TPCTRL                                     │
│          ▼                                                     │
│   ┌──────────────────┐                                         │
│   │  APNL2TPCTRL     │ ← APN 粒度 L2TP 使能开关               │
│   │  L2TPSWITCH=     │   (ENABLE: 本 APN 用户启用 L2TP)       │
│   │   ENABLE/DISABLE │                                         │
│   └──────┬───────────┘                                         │
│          │                                                     │
│          │ (可选) SET L2TPKEY                                  │
│          ▼                                                     │
│   ┌──────────────────┐                                         │
│   │  L2TPKEY         │ ← N4 接口 L2TP 私有信元加密配置         │
│   │  ENSWITCH=       │   (DISABLE 默认明文 / ENABLE 加密)     │
│   │   ENABLE/DISABLE │                                         │
│   └──────┬───────────┘                                         │
│          │                                                     │
│          │ 配合 SET PFCPPVTEXT / ADD UPCMPT                    │
│          ▼                                                     │
│   ┌──────────────────────────────────────┐                     │
│   │  PFCP 私有信元下发通道                │                     │
│   │   SET PFCPPVTEXT: FEATURE=ENABLE     │                     │
│   │   ADD UPCMPT: L2TPTNL=INHERIT,       │                     │
│   │              L2TPPCO=INHERIT          │                     │
│   └──────────────┬───────────────────────┘                     │
└──────────────────┼─────────────────────────────────────────────┘
                   │
                   │ Sx / N4 PFCP（携带 LNS 参数）
                   ▼
┌────────────────────────────────────────────────────────────────┐
│ UDG 侧执行对象（U 面：PGW-U/UPF，详见 GWFD-020412）             │
│                                                                │
│   接收 C 面下发的 LNS 参数 → 作为 LAC 与 LNS 建立 L2TP 隧道     │
│   → 内层 PPP 协商（LCP → 鉴权 → IPCP/IPCPv6 网络层协商）        │
│   → 由 LNS 为 UE 分配企业内网 IP                                │
└────────────────────────────────────────────────────────────────┘
```

### 2.3 在地址分配场景的角色

WSFD-104410 在地址分配场景中扮演**"LNS 远程地址分配触发器"**的角色：

1. **远程接入入口**：UNC 通过 APN 粒度的 L2TP 开关，将本 APN 下的用户标识为 L2TP VPN 用户
2. **LNS 参数下发**：将 AAA Server 返回的或本地配置的 LNS 参数通过 Sx/N4 下发给 PGW-U/UPF
3. **触发 U 面 LAC 行为**：PGW-U/UPF 作为 LAC 建立 L2TP 隧道，内层 PPP 协商完成后，**由 LNS 为 UE 分配企业内网 IP**（地址分配主体在 LNS，而非 UNC/UDG 本地池）
4. **与本地地址分配的分工**：L2TP VPN 用户的 IP 地址来自企业内网（LNS 端地址池），与 WSFD-010502 的 4 种本地分配方式（UDM/Radius/SMF 本地池/DHCP）是**互斥的并行方案**——一个用户要么走 L2TP 远程分配，要么走本地分配

---

## 3. 原理与流程

### 3.1 实现原理（UNC C 面：决策+下发，U 面：隧道+PPP）

L2TP 是 VPDN 隧道协议的一种。VPDN（Virtual Private Dial-up Network，虚拟私有拨号网）是指利用公共网络（如 ISDN、PSTN、PLMN 等）的拨号功能接入公共网络，实现 VPN，从而为企业、小型 ISP、移动办公人员等提供接入服务。VPDN 采用专用的网络加密通信协议，在公共网络上为企业建立安全的虚拟专网。

UNC 支持 AAA 鉴权，**AAA Server 在 Access-Accept 消息中下发 LNS 参数时，GGSN/PGW-C/SMF 通过 Sx/N4 接口将 LNS 参数下发到 PGW-U/UPF**。PGW-U/UPF 将使用下发的 LNS 相关参数建立 L2TP 隧道和会话。

R17 协议下，SMF 重点关注 **L2TP 相关 N4 接口信元**的变更。

> 来源：`特性概述_46559213.md`（"原理概述"章节）[EV-FK-01]

### 3.2 L2TP 隧道建立端到端流程（C-U 协同 + LNS 三阶段协商）

```
┌─────────────────────────────────────────────────────────────────┐
│ 阶段 1：UNC 接收 LNS 参数（C 面决策）                             │
│                                                                 │
│   方式 A（AAA 下发）：AAA Server ──Access-Accept──> UNC         │
│     携带 LNS 地址、LNS 密钥、隧道参数等                          │
│                                                                 │
│   方式 B（本地配置）：UNC 本地 SET APNL2TPCTRL L2TPSWITCH=ENABLE│
│     （此方式下 LNS 参数可能由 UDG 本地 L2TP Group 配置提供，     │
│      见 GWFD-020412 的"本地配置方式激活"）                       │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│ 阶段 2：UNC 通过 Sx/N4 接口下发 LNS 参数到 UPF                   │
│                                                                 │
│   UNC ──PFCP Session Establishment Request──> UPF               │
│     携带：LNS 地址 / L2TP 隧道参数 / L2TP 用户 PCO 信息          │
│     通过 PFCP 私有信元传输（需 SET PFCPPVTEXT FEATURE=ENABLE，  │
│     ADD UPCMPT L2TPTNL=INHERIT / L2TPPCO=INHERIT）              │
│                                                                 │
│   可选加密：SET L2TPKEY ENSWITCH=ENABLE                         │
│     （对端 UPF 必须同时开启并配置相同密钥）                      │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│ 阶段 3：UPF 作为 LAC 与 LNS 建立 L2TP 隧道（U 面执行，见         │
│         GWFD-020412）                                            │
│                                                                 │
│   3a. L2TP 隧道建立（SCCRQ/SCCRP/SCCCN 三次握手）                │
│   3b. L2TP 会话建立（ICRQ/ICRP/ICCN 三次握手）                   │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│ 阶段 4：内层 PPP 协商三阶段（UE ↔ LNS，经 L2TP 隧道透传）        │
│                                                                 │
│   4a. LCP（Link Control Protocol）阶段                          │
│       ← 建立链路，协商 MRU、鉴权方式等                           │
│                                                                 │
│   4b. 鉴权阶段（PAP / CHAP）                                    │
│       ← LNS 对企业用户进行二次鉴权                              │
│                                                                 │
│   4c. 网络层协议协商阶段（IPCP / IPCPv6）                        │
│       ← LNS 为 UE 分配企业内网 IP（IPv4）或 IPv6 前缀            │
│       ★ 地址分配发生在此阶段，地址来源为 LNS 端地址池            │
└─────────────────────────────────────────────────────────────────┘
```

> 来源：`特性概述_46559213.md`（"原理概述/图1 L2TP建立过程/图2 L2TP部署图"）[EV-FK-01]
> 说明：阶段 3-4 的 LAC 执行细节由 UDG 侧 GWFD-020412 定义；UNC 文档明确仅承担到阶段 2（参数下发）。

### 3.3 与 GWFD-020412（UDG 侧）的 C-U 对称分工

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
│   特性规格：L2TP 隧道信息 20 个                                  │
│   License：无                                                    │
│   标准：3GPP 23.214 / 29.244（CUPS）                             │
└──────────────────────────┬───────────────────────────────────────┘
                           │ Sx / N4 PFCP（私有信元）
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│ UDG（U 面：PGW-U/UPF） - GWFD-020412                              │
│ 角色：LAC + L2TP 隧道封装 + PPP 协商透传                          │
│                                                                  │
│   - 作为 LAC（L2TP Access Concentrator）                         │
│   - 解 GTP 封装后获得原始 IP 报文                                │
│   - 为 IP 报文添加 PPP 封装                                      │
│   - 与企业网 LNS 建立 L2TP 隧道，透传 PPP                        │
│                                                                  │
│   特性规格：本地 L2TP Group 1500 / AAA 下发方式 Group 1500       │
│   License：82200BVC LKV3G5L2TP01 L2TP VPN（必须）                │
│   标准：3GPP 23.214/29.244 + RFC 5571（L2TPv2）                  │
│   互斥：与 GWFD-010108（用户面地址自动检测）、GWFD-020482        │
│        （入不转板）互斥；不支持 DHCP 延迟分配 IPv4；不支持 IPv6  │
│        Prefix Delegation；NP 加速场景不支持 IPv6                 │
└──────────────────────────────────────────────────────────────────┘
```

> 来源：综合 `WSFD-104410 特性概述_46559213.md` [EV-FK-01] 与 UDG 侧 `GWFD-020412 L2TP VPN特性概述_40342127.md` 构建 C-U 协同分工图

### 3.4 协议交互

| 接口 | 交互网元 | 消息类型 | 说明 |
|------|---------|---------|------|
| Radius（2/3/4/5G） | AAA Server ↔ GGSN/PGW-C/SMF | Access-Request / Access-Accept | AAA 对 L2TP 用户鉴权，Access-Accept 携带 LNS 参数 |
| Sx（4G）/ N4（5G） | GGSN/PGW-C/SMF ↔ PGW-U/UPF | PFCP Session Establishment Request | UNC 将 LNS 参数通过 PFCP 私有信元下发给 UPF |
| L2TP | PGW-U/UPF（LAC） ↔ LNS | SCCRQ/SCCRP/SCCCN + ICRQ/ICRP/ICCN | 隧道与会话建立（U 面执行） |
| PPP（内层） | UE ↔ LNS（经 L2TP 隧道透传） | LCP / PAP/CHAP / IPCP/IPCPv6 | 三阶段协商，地址分配在 IPCP 阶段 |

---

## 4. 配置规则

### 4.1 激活步骤

WSFD-104410 在 UNC 侧的激活流程（本地配置方式）：

```
步骤1：确认前置条件
  ├── 已通过 ADD APN 配置目标 APN（如 huawei.com）
  ├── 企业网侧已部署 LNS 设备（应用限制硬约束）
  └── 对端 UPF（UDG）已加载 License 82200BVC LKV3G5L2TP01

步骤2：设置 APN L2TP 配置（核心使能）
  └── SET APNL2TPCTRL: APN=xxx, L2TPSWITCH=ENABLE

步骤3（可选）：打开 N4 接口 L2TP 加密
  └── SET L2TPKEY: ENSWITCH=ENABLE
      注：对端 UPF 需同时开启并配置相同密钥

（配合配置，非本特性独立命令但激活流程涉及）
步骤4（配合）：使能 PFCP 私有信元下发
  └── SET PFCPPVTEXT: FEATURE=ENABLE

步骤5（配合）：UP 节点协议兼容性
  └── ADD UPCMPT: L2TPTNL=INHERIT, L2TPPCO=INHERIT
```

> 来源：`激活L2TP VPN_46559215.md`（"操作步骤"章节）[EV-FK-03]

### 4.2 MML命令清单

#### 4.2.1 本特性参考信息列出的命令（1条核心）

| 命令 | 用途 | 关键参数 |
|------|------|---------|
| SET APNL2TPCTRL | 设置 APN L2TP CTRL 配置 | APN（APN名称）、L2TPSWITCH（支持L2TP功能开关 ENABLE/DISABLE） |

> 来源：`WSFD-104410 L2TP VPN参考信息_46559217.md`（"命令"章节）[EV-FK-02]

#### 4.2.2 激活文档涉及的相关命令（5条辅助）

| 命令 | 用途 | 关键参数 | 来源 |
|------|------|---------|------|
| ADD APN | 增加 APN 配置（前置，非本特性独立命令） | APN | 激活文档"必备事项/数据"表 |
| SET PFCPPVTEXT | 设置 PFCP 私有信元携带配置 | FEATURE=ENABLE | 激活文档"必备事项/数据"表 |
| ADD UPCMPT | 增加 UP 节点协议兼容性配置 | L2TPTNL=INHERIT、L2TPPCO=INHERIT | 激活文档"必备事项/数据"表 |
| SET L2TPKEY | 设置 L2TP 加密参数 | ENSWITCH=ENABLE/DISABLE、密钥 | 激活文档"必备事项/数据"表 + 操作步骤 |
| LST APNL2TPCTRL | 查询 APN L2TP CTRL 配置（调测） | APN | 调测文档"操作步骤" |

> 来源：`激活L2TP VPN_46559215.md`（"必备事项/数据"表）、`调测L2TP VPN_46559216.md`（"操作步骤"）[EV-FK-03, EV-FK-04]

### 4.3 关键参数说明

#### 4.3.1 SET APNL2TPCTRL 关键参数

| 参数 | 取值 | 说明 |
|------|------|------|
| APN | 字符串（如 huawei.com） | APN 名称，必须已通过 ADD APN 配置 |
| L2TPSWITCH | ENABLE / DISABLE | 支持 L2TP 功能开关；ENABLE 表示本 APN 下用户启用 L2TP VPN |

#### 4.3.2 SET L2TPKEY 关键参数

| 参数 | 取值 | 说明 |
|------|------|------|
| ENSWITCH | DISABLE（默认）/ ENABLE | 加密开关。DISABLE 时明文携带 L2TP 私有信元，存在安全风险，建议和对端 UPF 同时开启加密 |

> 安全提示：加密开关默认 DISABLE（明文），存在安全风险；启用时对端 UPF 必须同时开启并配置相同密钥，否则 L2TP 业务失败。

#### 4.3.3 ADD UPCMPT 关键参数

| 参数 | 取值 | 说明 |
|------|------|------|
| L2TPTNL | INHERIT | L2TP 隧道信息，继承方式下发 |
| L2TPPCO | INHERIT | L2TP 用户 PCO 信息，继承方式下发 |

#### 4.3.4 SET PFCPPVTEXT 关键参数

| 参数 | 取值 | 说明 |
|------|------|------|
| FEATURE | ENABLE | 特性名称，启用 PFCP 私有信元携带（LNS 参数下发通道） |

### 4.4 约束条件

| 约束类型 | 约束内容 | 来源 |
|---------|---------|------|
| 企业网 LNS 部署（应用限制） | 企业网侧必须部署 LNS 设备 | 特性概述"应用限制"章节 |
| APN 先决条件 | `SET APNL2TPCTRL` 的 APN 参数必须已通过 `ADD APN` 配置 | 激活文档"必备事项/数据"表 |
| 加密对称性 | 启用 `SET L2TPKEY ENSWITCH=ENABLE` 时，对端 UPF 必须同时开启并配置相同密钥，否则 L2TP 业务失败 | 激活文档"操作步骤"说明 |
| 同 APN 互斥（与 WSFD-205101） | 同一 APN 下，L2TP VPN 和 Routing Behind MS 无需同时部署（L2TP VPN 已通过 LNS 实现后者） | 特性概述"与其他特性的交互"章节 |
| 隧道信息规格 | UNC 侧 L2TP 隧道信息上限 20 个 | 特性概述"特性规格"章节 |
| C-U License 不对称 | UNC 侧无 License；UDG 侧必须加载 82200BVC LKV3G5L2TP01 | 特性概述 vs GWFD-020412 对比 |
| C-U 版本对齐 | UNC 与 UDG 均需 20.3.2 及后续版本 | 特性概述"可获得性"章节 |

---

## 5. 配置案例

### 5.1 典型场景：APN 粒度使能 L2TP VPN（本地配置方式）

**场景描述**：企业用户通过公网接入企业内网，运营商在 UNC 上为 APN `huawei.com` 使能 L2TP 功能。用户接入该 APN 时，由 AAA Server 下发 LNS 参数，UNC 通过 N4 接口将 LNS 参数下发到 UPF，UPF 作为 LAC 与企业网 LNS 建立 L2TP 隧道。

**配置步骤和 MML 命令序列**：

```
=== 步骤1：确认前置条件 ===
  -- 已通过 ADD APN 配置 APN="huawei.com"
  -- 企业网侧已部署 LNS 设备
  -- 对端 UPF 已加载 License 82200BVC LKV3G5L2TP01

=== 步骤2：设置 APN L2TP 配置（核心使能） ===

SET APNL2TPCTRL: APN="huawei.com", L2TPSWITCH=ENABLE;
  -- 为 APN huawei.com 使能 L2TP 功能
  -- 本 APN 下用户接入时触发 L2TP VPN 流程

=== 步骤3（可选）：打开 N4 接口 L2TP 加密 ===

SET L2TPKEY: ENSWITCH=ENABLE;
  -- 启用 L2TP 私有信元加密，增强 N4 接口传输安全
  -- 注意：对端 UPF 需同时打开该功能，并配置相同密钥
```

> 来源：`激活L2TP VPN_46559215.md`（"任务示例"）[EV-FK-03]

**场景变体**：

| 变体 | 场景说明 | 核心差异 | 文档覆盖度 |
|------|---------|---------|-----------|
| 本地配置方式激活 | UNC 本地 APN 粒度使能 L2TP | SET APNL2TPCTRL L2TPSWITCH=ENABLE | 完整 MML 脚本（本场景） |
| AAA 下发方式 | LNS 参数完全由 AAA Server 在 Access-Accept 中下发 | UNC 仅负责透传，无独立激活脚本 | 仅原理描述（见 §3.2） |
| 启用 N4 加密 | 增强 N4 接口 L2TP 私有信元安全 | 额外执行 SET L2TPKEY ENSWITCH=ENABLE | 操作步骤提及，无独立示例脚本 |

---

## 6. 验证与调测

### 6.1 验证方法

#### 6.1.1 调测前提与目的

当运营商部署 L2TP VPN 特性时，需对该特性进行调测，确保本功能可以正常使用。

> 适用：GGSN、PGW-C、SMF

#### 6.1.2 调测数据准备

**该操作无需准备数据**（文档明确声明）。**该操作无需准备其他工具**。

#### 6.1.3 调测执行步骤

**步骤1**：进入 "MML 命令行-UNC" 窗口。

**步骤2**：执行 **LST APNL2TPCTRL** 命令，查询 APN 下 L2TP 配置开关是否打开。

- 如果 "L2TPSWITCH" 为 "ENABLE" → 请执行步骤3
- 如果 "L2TPSWITCH" 为 "DISABLE" → 则执行 **SET APNL2TPCTRL** 命令打开本特性对应的配置开关

**步骤3**：测试终端接入网络，使用 L2TP 方式激活。

> 来源：`调测L2TP VPN_46559216.md`（"操作步骤"）[EV-FK-04]

### 6.2 告警参考

**本特性无相关告警**（参考信息明确声明）。

> 来源：`WSFD-104410 L2TP VPN参考信息_46559217.md`（"告警"章节）[EV-FK-02]

### 6.3 测量指标

**本特性无相关测量指标**（参考信息明确声明）。

> 来源：`WSFD-104410 L2TP VPN参考信息_46559217.md`（"测量指标"章节）[EV-FK-02]

### 6.4 软参

**本特性无相关软参**（参考信息明确声明）。

> 来源：`WSFD-104410 L2TP VPN参考信息_46559217.md`（"软参"章节）[EV-FK-02]

### 6.5 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| L2TP VPN 未生效 | APN 下 L2TPSWITCH 未使能 | 执行 LST APNL2TPCTRL 查询；若 DISABLE 则 SET APNL2TPCTRL 打开 |
| L2TP 业务失败 | 启用了 L2TPKEY 加密但对端 UPF 未开启或密钥不一致 | 核对两端加密开关与密钥；建议两端同时 ENABLE 并配置相同密钥 |
| UPF 未收到 LNS 参数 | PFCP 私有信元下发通道未启用 | 检查 SET PFCPPVTEXT FEATURE=ENABLE；检查 ADD UPCMPT L2TPTNL/L2TPPCO |
| L2TP 隧道无法建立 | 企业网侧未部署 LNS 或 LNS 不可达 | 核对 LNS 部署；检查 UPF 到 LNS 的网络连通性 |
| L2TP 用户接入失败 | UDG 侧 License 未加载 | 检查 UPF 是否加载 82200BVC LKV3G5L2TP01 License |
| 同 APN 下业务冲突 | 同一 APN 同时部署了 L2TP VPN 和 WSFD-205101 Routing Behind MS | 文档明确两者无需同时部署；移除其中一个 |

---

## 7. 参考信息

### 7.1 与其他特性的关系

| 关联特性 | 特性ID | 关系说明 |
|---------|--------|---------|
| 控制面地址分配方式（配置树父节点，推断） | WSFD-010504（UNC） | 配置树父节点关系推断（Stage 3 验证） |
| 地址分配方式（本地 4 种分配方式） | WSFD-010502（UNC） | **互斥关系**：L2TP 用户的 IP 由 LNS 远程分配，与 WSFD-010502 的 UDM/Radius/SMF 本地池/DHCP 本地分配是并行方案；一个用户要么走 L2TP，要么走本地（文档依据：L2TP VPN 通过 LNS 实现地址分配，属于"远程"地址分配维度） |
| L2TP VPN（UDG 侧 C-U 协同对端） | GWFD-020412（UDG） | **C-U 协同分工**：UNC 决策+下发 LNS 参数；UDG 作为 LAC 执行隧道封装与 PPP 协商透传 |
| 支持 Routing Behind MS（UNC） | WSFD-205101（UNC） | **同 APN 互斥**：L2TP VPN 已通过 LNS 实现 Routing Behind MS，同一 APN 下无需同时部署 |
| AAA Radius 鉴权接入 | WSFD-011305（UNC） | LNS 参数通过 AAA Access-Accept 下发（依赖 Radius 鉴权链路） |
| Radius 功能 | WSFD-011306（UNC） | Radius 服务器配置（AAA 下发方式时 LNS 参数在 Radius 侧配置） |
| 会话管理 | WSFD-010501（UNC） | PDU/PDP/承载会话建立的宿主特性 |
| 用户面地址自动检测 | GWFD-010108（UDG，互斥） | UDG 侧明确：L2TP VPN 与用户面地址自动检测功能互斥（UDG 侧约束，UNC 侧未声明） |

### 7.2 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104410 L2TP VPN/特性概述_46559213.md` | 适用NF（GGSN/PGW-C/SMF + PGW-U/UPF + LNS）、定义、客户价值、应用场景、可获得性（UNC 20.3.2+/UDG 20.3.2+、无License）、与其他特性的交互（与WSFD-205101互斥）、对系统影响（无）、应用限制（企业网必须部署LNS）、原理概述（L2TP VPN原理+图1 L2TP建立过程+图2 L2TP部署图，R17 SMF关注N4信元）、计费话单（无）、特性规格（L2TP隧道信息20个）、遵循标准（3GPP 23.214/29.244）、发布历史（v01 20.3.2 / v02 20.6.0 IPv6用户 / v03 20.9.0 R17 / v04 20.11.2 20个隧道） |
| 2 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104410 L2TP VPN/WSFD-104410 L2TP VPN参考信息_46559217.md` | MML命令清单（仅1条核心：SET APNL2TPCTRL）、告警（无）、软参（无）、测量指标（无） |
| 3 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104410 L2TP VPN/激活L2TP VPN_46559215.md` | 激活操作场景、必备数据表（6个参数：APN/L2TPSWITCH/FEATURE/L2TPTNL/L2TPPCO/ENSWITCH，覆盖SET APNL2TPCTRL/SET PFCPPVTEXT/ADD UPCMPT/SET L2TPKEY命令）、2步操作步骤、L2TPKEY加密对称性约束、任务示例（SET APNL2TPCTRL APN=huawei.com L2TPSWITCH=ENABLE 完整MML脚本） |
| 4 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104410 L2TP VPN/调测L2TP VPN_46559216.md` | 3步调测流程（LST APNL2TPCTRL 查询开关 → SET APNL2TPCTRL 打开 → 测试终端L2TP激活）、无需准备数据/工具 |
| 5 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104410 L2TP VPN_46534504.md` | 特性根索引文件（仅标题，无实质内容） |

### 7.3 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| L2TP | Layer 2 Tunneling Protocol | 二层隧道协议，VPDN 隧道协议的一种 |
| VPDN | Virtual Private Dial-up Network | 虚拟私有拨号网 |
| LNS | L2TP Network Server | 企业网边缘设备，L2TP 隧道服务器端 |
| LAC | L2TP Access Concentrator | L2TP 接入集中器，由 PGW-U/UPF 承担 |
| PPP | Point-to-Point Protocol | L2TP 内层链路层协议 |
| LCP | Link Control Protocol | PPP 链路建立阶段协议 |
| IPCP / IPCPv6 | IP Control Protocol | PPP 网络层协商协议，地址分配发生于此 |
| PFCP | Packet Forwarding Control Protocol | 5G/4G C-U 分离控制面协议 |
| Sx / N4 | 4G / 5G C-U 接口 | LNS 参数下发通道 |
| L2TPSWITCH | L2TP 功能开关 | SET APNL2TPCTRL 参数 |
| ENSWITCH | 加密开关 | SET L2TPKEY 参数 |
| L2TPTNL / L2TPPCO | L2TP 隧道信息 / 用户 PCO 信息 | ADD UPCMPT 参数，继承方式下发 |

---

## 8. 文档一致性说明（配置树 vs 产品文档 vs GWFD-020412）

> 配置树仅用于定位特性 ID，以下记录以产品文档实际内容为准时发现的差异与协同点，供 Stage 3 横向分析参考。

### 8.1 与任务要求中提及对象的核对（★重点澄清）

| # | 任务要求提及 | 产品文档实际 | 核对结论 |
|---|-------------|-------------|---------|
| 1 | APNL2TPATTR 配置 | **未出现该对象**。本特性实际的核心配置对象是 `APNL2TPCTRL`（命令 `SET APNL2TPCTRL`），按 APN 粒度使能 L2TP 开关 | **澄清**：`APNL2TPATTR` 并非 WSFD-104410 文档定义的对象，任务要求中的命名与文档不一致；以产品文档 `APNL2TPCTRL` 为准 |
| 2 | APNADDRESSATTR 配置 | **未出现该对象**。5 篇 WSFD-104410 文档均未提及 `APNADDRESSATTR` | **澄清**：`APNADDRESSATTR` 可能为其他特性的对象（或 Stage 3 横向分析时识别的聚合概念），与本特性无直接配置关系 |
| 3 | L2TP 隧道/LNS 地址分配机制 | 文档明确：UNC 通过 Sx/N4 下发 LNS 参数到 UPF，UPF 作为 LAC 建隧道，内层 PPP 协商中由 LNS 分配企业内网 IP | 已覆盖（见 §3.2 阶段 3-4） |
| 4 | LCP/鉴权/网络协商三阶段 | UNC 文档未展开（属于 PPP 协议标准流程），但明确 UPF 建立 L2TP 隧道和会话后由 LNS 完成 | 已补充（见 §3.2 阶段 4，标准 PPP 三阶段） |
| 5 | 与 GWFD-020412 C-U 对称 | UNC 决策+下发 / UDG LAC 执行隧道封装；UNC 无 License，UDG 需 License | 已覆盖（见 §3.3） |

### 8.2 与配置树/文档清单的差异

| # | 维度 | 配置树/文档清单描述 | 产品文档实际内容 | 差异类型 |
|---|------|---------------------|-----------------|---------|
| 1 | 文件数 | 文档清单列 5 个文件 | 实际 1 个根索引文件为空（仅标题），实质内容 4 篇 | 补全：根索引无内容 |
| 2 | 命令清单覆盖度 | 参考信息仅列 1 条命令（SET APNL2TPCTRL） | 激活文档额外涉及 5 条辅助命令（ADD APN/SET PFCPPVTEXT/ADD UPCMPT/SET L2TPKEY/LST APNL2TPCTRL） | 补全：参考信息命令清单不完整 |
| 3 | License要求 | 文档清单标注"[★核心]" | 产品文档明确声明"**无需License**"；但 UDG 侧 GWFD-020412 必须 License | C-U 不对称：UNC 无 License，UDG 必须 License |
| 4 | 子方式分类 | 文档清单概括："LNS分配(SMF侧,L2TP隧道PPP协商)" | UNC 侧仅"参数下发"角色；PPP 协商在 UDG（LAC）与 LNS 之间 | 角色定位偏差：清单描述偏 U 面 |
| 5 | 遵循标准 | 配置树无 | UNC 仅引用 3GPP 23.214/29.244（CUPS）；UDG 另引用 RFC 5571（L2TPv2） | C-U 互补：UNC 关注 C-U 分离标准，UDG 关注 L2TP 协议标准 |
| 6 | 与父节点关系 | 配置树父节点推断为 WSFD-010504 | 本特性 5 篇文档**未直接提及** WSFD-010504 | 推断关系，Stage 3 验证 |

### 8.3 与 GWFD-020412（UDG 侧）的 C-U 协同与不一致

| # | 维度 | GWFD-020412（UDG/U面） | WSFD-104410（UNC/C面） | 协同/差异 |
|---|------|------------------------|------------------------|----------|
| 1 | 角色定位 | LAC + L2TP 隧道封装 + PPP 透传执行方 | 决策方 + LNS 参数下发方 | **C-U 协同分工**：决策+参数在 C 面，隧道执行在 U 面 |
| 2 | 网元角色 | PGW-U / UPF（用户面） | GGSN / PGW-C / SMF（控制面） | C-U 分离 |
| 3 | License | 必须 License `82200BVC LKV3G5L2TP01` | **无 License** | **C-U License 不对称**（差异点） |
| 4 | 特性规格 | 本地 L2TP Group 1500 / AAA 下发方式 Group 1500 | L2TP 隧道信息 20 个 | 规格维度不同（U 面按 Group，C 面按隧道信息） |
| 5 | 互斥特性 | 与 GWFD-010108（用户面地址自动检测）、GWFD-020482（入不转板）互斥；不支持 DHCP 延迟分配 IPv4；不支持 IPv6 PD；NP 加速不支持 IPv6 | 与 WSFD-205101（Routing Behind MS）同 APN 无需同时部署 | **互斥维度不对称**：U 面互斥约束多（涉及 U 面加速/地址检测/PD），C 面仅声明同 APN 互斥 |
| 6 | 标准 | 3GPP 23.214/29.244 + RFC 5571（L2TPv2） | 3GPP 23.214/29.244 | U 面多引用 L2TP 协议标准 |
| 7 | 版本起点 | UDG 20.3.2 | UNC 20.3.2 | C-U 版本对齐 |
| 8 | IPv6 支持 | v02 20.6.0 支持 IPv6 用户；v03 20.12.0 隧道支持 IPv6 地址 | v02 20.6.0 支持 IPv6 用户接入 | C-U 两侧均在 v02 起支持 IPv6 用户 |
| 9 | 对系统影响 | 用户面报文增加 L2TP 封装，对性能有一定影响 | 无影响 | 性能影响集中在 U 面 |
| 10 | 告警/软参/指标 | UDG 侧有（详见 GWFD-020412 参考信息） | **全部为"无"** | 运维观测点在 U 面侧 |
| 11 | 地址分配主体 | LAC 不分配地址（仅封装透传） | UNC 不分配地址（仅下发参数） | **地址分配主体为 LNS**（企业网侧） |

---

## 附录 A：与 GWFD-020412 的 C-U 对照速查表

| 对照维度 | GWFD-020412（UDG） | WSFD-104410（UNC） |
|---------|--------------------|--------------------|
| 网元角色 | PGW-U / UPF（用户面） | GGSN / PGW-C / SMF（控制面） |
| L2TP 角色 | LAC（L2TP Access Concentrator） | 决策+LNS 参数下发 |
| 地址分配主体 | 不分配（LAC 透传） | 不分配（仅下发参数） |
| License | 82200BVC LKV3G5L2TP01（必须） | 无 |
| 特性规格 | L2TP Group 1500（本地+AAA 各 1500） | 隧道信息 20 个 |
| 互斥特性 | GWFD-010108 / GWFD-020482 + 多项 U 面约束 | WSFD-205101 同 APN 互斥 |
| 标准 | 3GPP 23.214/29.244 + RFC 5571 | 3GPP 23.214/29.244 |
| 版本起点 | UDG 20.3.2 | UNC 20.3.2 |
| 核心 MML | （UDG 侧 L2TP Group 配置） | SET APNL2TPCTRL |
| N4 加密 | （U 面） | SET L2TPKEY（C 面，可选） |
| 告警/软参/指标 | 有 | 无 |
| 对系统影响 | 有（封装开销） | 无 |
| 决策/执行 | 执行方（无决策权） | 决策方（参数下发） |

---

## 附录 B：source_evidence_ids 占位映射

| evidence_id | 对应来源文件 | 主要贡献章节 |
|-------------|-------------|-------------|
| EV-FK-01 | `特性概述_46559213.md` | 适用NF、定义、原理、规格、标准、版本、交互、License、限制 |
| EV-FK-02 | `WSFD-104410 L2TP VPN参考信息_46559217.md` | MML命令清单（SET APNL2TPCTRL）、告警/软参/指标（均无） |
| EV-FK-03 | `激活L2TP VPN_46559215.md` | 激活步骤、必备数据表（6参数）、L2TPKEY加密约束、MML脚本 |
| EV-FK-04 | `调测L2TP VPN_46559216.md` | 3步调测流程、LST APNL2TPCTRL 查询 |
| EV-FK-05 | `WSFD-104410 L2TP VPN_46534504.md` | 特性根索引（仅标题，无实质内容） |
