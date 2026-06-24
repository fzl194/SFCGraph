# IPFD-016000 IPSec功能 知识文档

> 聚焦 APN 业务域接入方式场景的 IPSec（Internet Protocol Security）隧道特性（UNC/SMF 侧）
> 与 IPFD-015004（UDG/UPF 侧 IPSec）构成 C-U 对称同构部署（两侧文档源同构、命令同构）
> 与 GRE（IPFD-015002）、L2TP（GWFD-020412 / WSFD-104410）、MPLS VPN（GWFD-020411 / WSFD-104411）共同构成 APN 域的隧道方案矩阵
> 适用 NF：SGW-C / PGW-C / SMF（UNC）
> C-U 对称：两侧配置对象与命令基本对称（VNRS 微服务 + IPsec 微服务双配），非 C-U 分工型

---

## 0. 元数据（三层图谱 Schema 字段）

| 字段 | 取值 |
|------|------|
| feature_id | IPFD-016000 |
| feature_name | IPSec功能 |
| feature_group | 接入方式 |
| parent_feature_id | IPFD-015000（VPN 功能，配置树父节点；两侧共用，本侧 24 篇文档未直接提及） |
| applicable_nf_map | `{"UNC": ["SGW-C", "PGW-C", "SMF"]}` |
| variant_dimensions | ["地址族(IPv4 / IPv6 / 双栈)", "安全协议(AH / ESP / AH+ESP)", "封装模式(Tunnel)", "SA创建方式(IKE自动协商 / 手工)", "IKE版本(IKEv1主模式/野蛮模式 / IKEv2)", "密码体系(标准IPSec / 国密SM2-SM3-SM4)", "NAT穿越(NATTRAVERSAL=TRUE/FALSE)", "可靠性(DPD periodic/on-demand + 主备隧道热备/冷备)", "IKE对等体绑定数量(单Peer / 多Sequence多Peer)", "GRE over IPSec(组播广播加密)", "认证方法(预共享密钥PSK / 证书RSA)", "本端IKE协商源(隧道接口 / 指定LoopBack接口)", "VPN实例绑定(公网 / VPN实例)"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-01, EV-FK-02, EV-FK-03, EV-FK-04, EV-FK-05, EV-FK-06, EV-FK-07, EV-FK-08, EV-FK-09, EV-FK-10, EV-FK-11, EV-FK-12] |
| license_required | **无需 License**（产品文档明确"本特性无需获得 License 许可即可获得该特性的服务"） |

---

## 1. 概述

### 1.1 特性定义（是什么）

IPsec（Internet Protocol Security）是由 IETF 制定的一套开放的 IP 层安全框架协议，包含一系列为 IP 网络提供完整安全性的协议和服务。IPsec 使能通信双方在 IP 层执行数据加密、数据完整性保护，保证端对端通信数据的私密性、完整性、真实性和防重放攻击。

IPsec 协议族包括两类安全协议（AH、ESP）与一类密钥交换协议（IKE）：
- **AH（Authentication Header，IP 认证头协议，IP 协议号 51）**：提供数据源认证、数据完整性校验、防重放攻击，**不加密**（不能防窃听），适合传输非机密数据。
- **ESP（Encapsulating Security Payload，IP 封装安全载荷协议，IP 协议号 50）**：提供数据源认证、数据完整性校验、防重放攻击，**并支持数据加密**。
- **IKE（Internet Key Exchange，密钥交换协议）**：动态创建 SA，为 IPsec 提供自动协商交换密钥、建立和维护 SA 的服务，简化 IPsec 的使用和管理。

> 来源：`IPFD-016000 IPSec功能特性概述_61317289.md`（"定义/实现原理"章节）、`AH和ESP_62244157.md`、`IKE_62256396.md` [EV-FK-01, EV-FK-02, EV-FK-03]

### 1.2 适用 NF（UNC 网元）

| 涉及 NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| SGW-C / PGW-C / SMF | 控制面（UNC） | UNC 20.5.0 及后续版本（IPv6 IPsec / NAT 穿越 / 主备隧道为 20.8.0） | 控制面网元间建立 IPSec 加密隧道，保护网管/信令/网间数据传输的私密性与完整性 |

> ★关键：本特性（IPFD-016000）为 UNC 侧实现。与 IPFD-015004（UDG 侧 IPSec）文档源同构——两特性概述文件 ID 均为 `61317289`，术语文件 ID 均为 `88277392`，AH/ESP、IKE、SA、NAT 穿越、可靠性、封装模式等原理文件 ID 完全一致；仅激活/调测文件 ID 因命令路径前缀（VNRS 微服务 vs UDG 命令行）不同。
>
> 来源：`IPFD-016000 IPSec功能特性概述_61317289.md`（"可获得性/版本支持"章节）；`apn-feature-doc-list.md` Batch-30/31 对照 [EV-FK-01]

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|---------|---------|---------|
| 01 | UNC 20.5.0 | 首次发布 |
| 02 | UNC 20.8.0 | 支持 IPv6 IPsec、IPsec NAT 穿越以及 IPsec 主备隧道功能 |

> 来源：`IPFD-016000 IPSec功能特性概述_61317289.md`（"发布历史"章节）[EV-FK-01]

### 1.4 License

**本特性无需 License 许可**。产品文档明确声明"本特性无需获得 License 许可即可获得该特性的服务"。

> 来源：`IPFD-016000 IPSec功能特性概述_61317289.md`（"可获得性/License 支持"章节）[EV-FK-01]

### 1.5 前置条件与依赖

| 前置条件 | 说明 |
|---------|------|
| IPSec 服务已安装 | IPSec 功能由 IPSec 服务承载，需在软件安装章节完成"安装可选服务 > 安装 IPSec 服务" |
| 操作人员已登录网管 | NMS 操作入口 |
| 接口 IP 地址已配置 | 物理出接口与隧道接口 IP |
| 隧道两端路由可达 | 通过 PING 验证（`PING`） |
| VNRS 微服务 + IPsec 微服务双配 | ★核心约束：隧道接口、接口 IP、隧道类型、VPN、指定本端接口需在两个微服务一对一配置，否则业务不通 |
| ACL（高级 ACL，定义保护数据流） | 通过 `ADD ACLGROUPIPSEC` + `ADD ACLRULEADV4IPSEC` 定义；**ACL 只支持源/目的 IP，不支持端口** |
| 预共享密钥（PSK）或证书 | PSK 方式下两端必须相同；证书方式需先 `上传IPsec证书` |

> 来源：`激活IPsec功能（普通IPv4 IPsec隧道）_61317238.md`（"必备事项/前提条件" + "操作流程"微服务说明）、`激活IPsec功能（GRE over IPsec）_78985535.md` [EV-FK-07, EV-FK-09]

### 1.6 与其他特性的交互

| 交互类型 | 相关特性 | 交互说明 |
|---------|---------|---------|
| **组合（GRE over IPSec）** | IPFD-015002 GRE / IPFD-015004 IPSec（UDG） | IPsec 只支持 IP 报文，不支持组播/广播；组播广播经 GRE 封装为 GRE 报文后引入 IPsec 隧道加解密 |
| **源地址互斥** | IPFD-015002 GRE | **GRE 隧道源地址不能与 IPSec 隧道源地址相同**（GRE 侧应用限制） |
| **协同（OSPF over IPSec）** | IPFD-014001 OSPF | 通过 IPsec 隧道保护 OSPF 协议报文（本特性文档提供"OSPF over IPsec"激活场景） |
| **国密变体** | 国密 SM2/SM3/SM4 | 本特性提供 5 个"激活国密 IPsec 支持 IKEv1 功能"场景（国密证书 + 国密算法） |

> 来源：`IPFD-016000 IPSec功能特性概述_61317289.md`（"与其他特性的交互"章节——"本特性不涉及与其他特性的交互"，但激活文档存在 GRE over IPSec / OSPF over IPSec 场景，以激活文档为准）、`激活IPsec功能（GRE over IPsec）_78985535.md`、`激活IPsec功能（OSPF over IPsec）_90949389.md` [EV-FK-01, EV-FK-09, EV-FK-11]

### 1.7 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | IPSec 保护用户数据的私密性、完整性和真实性，同时防御重放攻击、中间人攻击等，提升业务安全性 |
| 终端用户 | 用户不感知该特性 |

> 来源：`IPFD-016000 IPSec功能特性概述_61317289.md`（"客户价值"章节）[EV-FK-01]

### 1.8 应用场景

- **公网安全传输**：协议报文在公网传输面临被篡改、窃取、重放的风险，IPSec 提供端到端私密性、完整性、真实性、防重放
- **网关对网关（Site-to-Site）**：网络 A 与网络 B 通过 Device A、Device B 之间的 IPSec 隧道安全互访（IPv4 / IPv6 / 双栈）
- **GRE over IPSec**：IPSec 不支持组播/广播的场景下，先 GRE 封装再 IPSec 加密
- **OSPF over IPSec**：通过 IPSec 保护 OSPF 动态路由协议报文
- **主备隧道高可靠**：本端与两个或以上对端建立 IPSec 隧道，主用故障切换备用（热备 / 冷备）
- **多 Sequence 一隧多 Peer**：单隧道接口对接多个 IKE Peer，节省隧道接口和 IP 地址
- **指定本端接口**：以 LoopBack 口作为 IKE 协商源，支持多隧道共用同一 LoopBack
- **NAT 穿越场景**：两端之间存在 NAT 设备时，UDP 封装 + NAT 保活
- **国密合规场景**：使用国密 SM2/SM3/SM4 算法与国密证书，满足合规要求

> 来源：各激活文档"操作场景"章节（IPv4、IPv6、GRE over IPSec、OSPF over IPSec、主备隧道、多 Sequence、指定本端接口、国密 IKEv1）[EV-FK-07..12]

### 1.9 对系统的影响

该特性对用户报文会进行封装处理，**对性能有一定影响**（加解密运算开销），详细性能影响需联系华为技术支持获取。激活文档另声明"本特性对系统无影响"（指激活操作本身）。

> 来源：`IPFD-016000 IPSec功能特性概述_61317289.md`（"对系统的影响"章节）、各激活文档"对系统的影响" [EV-FK-01, EV-FK-07]

### 1.10 应用限制（★关键）

IPSec 目前**不支持**的场景：
- GREv6 over IPSecv6
- OSPFv3 over IPSecv6
- IPSecv6 地址借用
- IPV4 报文入 IPSecv6 隧道
- IPV6 报文入 IPSecv4 隧道
- **IPSec NAT 穿越**仅适用于 **ESP 隧道模式**，且**不支持 IPv6 组网**
- **指定本端接口**：被指定的接口需被 IPSec 隧道单独使用，若被其他协议使用则该协议不生效
- **ACL**：只支持源 IP 和目的 IP 配置，**不支持端口**配置生效

> 来源：`IPFD-016000 IPSec功能特性概述_61317289.md`（"应用限制"章节）、`IPsec NAT穿越_62244160.md`（"约束限制"章节）、`激活IPsec功能（指定本端接口建立IPsec隧道）_78985537.md`、`激活IPsec功能（普通IPv4 IPsec隧道）_61317238.md`（ACL 说明）[EV-FK-01, EV-FK-06, EV-FK-10, EV-FK-07]

### 1.11 特性规格

**本特性无特殊规格**（特性概述原文）。可靠性章节补充：**主备隧道热备支持一主一备，冷备最多支持一主两备**。

> 来源：`IPFD-016000 IPSec功能特性概述_61317289.md`（"特性规格"章节）、`IPsec可靠性_78460643.md`（主备隧道规格表）[EV-FK-01, EV-FK-05]

### 1.12 计费与话单

**本特性不涉及计费与话单**。

> 来源：`IPFD-016000 IPSec功能特性概述_61317289.md`（"计费与话单"章节）[EV-FK-01]

### 1.13 遵循标准

| 标准类别 | 标准名称 |
|---------|---------|
| RFC 2401 | Security Architecture for the Internet Protocol |
| RFC 2402 | IP Authentication Header（AH） |
| RFC 2406 | IP Encapsulating Security Payload（ESP） |
| RFC 2403 | The Use of HMAC-MD5-96 within ESP and AH |
| RFC 4868 | Using HMAC-SHA-256 / SHA-384 / SHA-512 with IPsec |
| RFC 4305 | Cryptographic Algorithm Implementation Requirements for ESP and AH |
| RFC 4314 | IMAP4 Access Control List (ACL) Extension |

> 来源：`IPFD-016000 IPSec功能特性概述_61317289.md`（"遵循标准"章节）[EV-FK-01]

---

## 2. 核心概念

### 2.1 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| IPSec | Internet Protocol Security | IETF 制定的 IP 层安全框架协议族，提供加密/认证/完整性/防重放 |
| AH | Authentication Header | IP 认证头协议（协议号 51），认证+完整性+防重放，**不加密** |
| ESP | Encapsulating Security Payload | IP 封装安全载荷协议（协议号 50），认证+完整性+防重放+**加密** |
| IKE | Internet Key Exchange | 密钥交换协议，动态协商 SA 与密钥；含 IKEv1 / IKEv2 |
| SA | Security Association | 安全联盟，对等体间协商的"约定"，定义安全服务策略；含 IKE SA 与 IPSec SA |
| SPI | Security Parameters Index | 安全参数索引，32 bit，唯一标识 SA，携带于 AH/ESP 报文头 |
| Proposal | 安全提议 | 定义封装模式、安全协议、认证/加密算法（含 IPSec 提议与 IKE 提议两类） |
| SP | Security Policy | 安全策略，决定对 IP 数据包提供何种保护；含 ACL、Proposal、IKE Peer、本端/对端 IP |
| SADB | Security Association Database | 安全联盟数据库，存放 SA 状态数据 |
| SPDB | Security Policy Database | 安全策略数据库，IPSec Policy 有序集合 |
| Life Time | 生存周期 | SA 有效时间；含基于时间与基于流量两种 |
| 对等体（Peer） | IKE Peer | IPSec 两个端点之一；含预共享密钥、远程地址、NAT 穿越等属性 |
| DPD | Dead Peer Detection | 失效对等体检测，防止 IKE 协议黑洞；periodic / on-demand 两种模式 |
| Tunnel 接口 | IPSec 隧道接口 | 虚拟接口，TNLTYPE=IPSEC，应用 IPSec 策略 |
| VNRS 微服务 | - | UNC 内部微服务，负责与外部网络通信、引流（明文/密文表）到 IPsec 微服务 |
| IPsec 微服务 | - | UNC 内部微服务，负责 IKE 协商与加解密 |
| 双配原则 | - | VNRS 与 IPsec 两个微服务必须一对一配置相同数据，否则业务不通 |
| 主备隧道 | Master-standby | 本端与多对端建隧道，主用故障切换备用；热备（自动协商 SA） / 冷备（备用不协商） |
| 多 Sequence | - | 单隧道接口下配置多 Sequence 对接多 IKE Peer，节省接口与 IP |
| NAT 穿越 | NAT Traversal | NAT 设备后端 IPSec，通过 UDP 封装 + 保活消息（NATKLI）穿越 |
| 国密 | - | SM2（证书）/ SM3（认证）/ SM4（加密）算法体系，合规变体 |

> 来源：`相关术语_88277392.md`、`安全联盟（SA）_62244156.md`、`AH和ESP_62244157.md`、`IKE_62256396.md`、`IPsec可靠性_78460643.md`、`IPsec NAT穿越_62244160.md`、各激活文档（微服务说明）[EV-FK-02, EV-FK-03, EV-FK-04, EV-FK-05, EV-FK-06, EV-FK-07]

### 2.2 对象模型（★重点：微服务双配）

IPFD-016000 在 UNC 侧的对象模型由 **VNRS 微服务** 与 **IPsec 微服务** 两套对象镜像构成，两套对象需**一对一配置（双配原则）**：

```
┌──────────────────────────────────────────────────────────────────────────┐
│ VNRS 微服务（负责外部通信 + 引流到 IPsec 微服务）                            │
│                                                                          │
│   VPN 实例（可选）          IPsec 隧道接口（Tunnel，TNLTYPE=IPSEC）          │
│   ADD L3VPNINST          ADD INTERFACE + ADD IPSECINTFCFG                  │
│   ADD VPNINSTAF          ADD IPBINDVPN + ADD IFIPV4ADDRESS                │
│        │                       │                                         │
│        └─────────┬─────────────┘                                         │
│                  │ 静态路由 ADD SRROUTE，出接口指向 Tunnel                  │
│                  ▼                                                       │
│   （明文引流表 / 密文引流表：将流量引到 IPsec 微服务加解密）                  │
└──────────────────────────────┬───────────────────────────────────────────┘
                               │ 双配原则（一对一）
                               ▼
┌──────────────────────────────────────────────────────────────────────────┐
│ IPsec 微服务（负责 IKE 协商 + 加解密）                                       │
│                                                                          │
│   VPN 实例                IPsec 隧道接口（镜像 VNRS）                       │
│   ADD L3VPNINSTIPSEC    ADD INTERFACEIPSEC                                │
│   ADD VPNINSTAFIPSEC    ADD IPBINDVPNIPSEC                                │
│                         ADD IFIPV4ADDRESSIPSEC                            │
│                                  │                                       │
│                                  │ 应用 IPSec 策略                        │
│                                  ▼                                       │
│   ┌────────────────────────────────────────────────────┐                  │
│   │  ACL 规则组（定义保护数据流，仅源/目的 IP）             │                  │
│   │  ADD ACLGROUPIPSEC + ADD ACLRULEADV4IPSEC          │                  │
│   └──────────────────────┬─────────────────────────────┘                  │
│                          │                                               │
│   ┌──────────────────────▼─────────────────────────────┐                  │
│   │  IPSec 安全提议（封装模式 + 安全协议 + 算法）          │                  │
│   │  ADD IPSECPROPOSALIPSEC                             │                  │
│   │    ENCAPMODE=Tunnel / IPSECPROTOCOL=Esp|Ah          │                  │
│   │    ESPAUTHALGO=Sha2_256 / ESPENCRYPTALGO=Aes_256    │                  │
│   └──────────────────────┬─────────────────────────────┘                  │
│                          │                                               │
│   ┌──────────────────────▼─────────────────────────────┐                  │
│   │  IKE 安全提议（认证方法 + 算法 + DH 组）               │                  │
│   │  ADD IKEPROPOSAL                                    │                  │
│   │    AUTHMETHOD=Pre_share / DHGROUP=Dh_group19        │                  │
│   └──────────────────────┬─────────────────────────────┘                  │
│                          │                                               │
│   ┌──────────────────────▼─────────────────────────────┐                  │
│   │  IKE 对等体（PSK + 远程地址 + NAT 穿越等）             │                  │
│   │  ADD IKEPEER                                        │                  │
│   │    PRESHAREDKEY / LOWREMOTEADDR / NATTRAVERSAL      │                  │
│   │    EXCHANGEMODE=Main / LOCALIDTYPE=Ip               │                  │
│   └──────────────────────┬─────────────────────────────┘                  │
│                          │                                               │
│   ┌──────────────────────▼─────────────────────────────┐                  │
│   │  IPSec 安全策略（聚合对象：ACL + Proposal + Peer）      │                  │
│   │  ADD IPSECPOLICY                                    │                  │
│   │    POLICYMODE=Isakmp / WORKMODE / AUTOSWITCHBACK    │                  │
│   │  ADD PROPATTACHIPSECPROPOSAL（绑定 Proposal）         │                  │
│   │  ADD ATTACHIKEPEER（绑定 IKE Peer，含优先级）          │                  │
│   └──────────────────────┬─────────────────────────────┘                  │
│                          │                                               │
│   ┌──────────────────────▼─────────────────────────────┐                  │
│   │  隧道接口绑定策略 + IKE 全局配置（DPD/NAT保活）         │                  │
│   │  ADD IPSECINTFCFGIPSEC（应用策略）                    │                  │
│   │  SET IKEGLOBALCONFIG（DPD + NATKLI）                 │                  │
│   └────────────────────────────────────────────────────┘                  │
└──────────────────────────────────────────────────────────────────────────┘
```

核心对象说明：

| 对象 | 命令（IPsec 微服务侧） | 作用 |
|------|---------------------|------|
| **IPSec 安全策略（Policy）** | `ADD IPSECPOLICY` | ★聚合对象：引用 ACL + Proposal + IKE Peer；含 Sequence、工作模式（Master_standby）、自动切回开关 |
| **IPSec 安全提议（Proposal）** | `ADD IPSECPROPOSALIPSEC` | 定义封装模式 + 安全协议 + 算法（ESP 认证/加密算法） |
| **IKE 安全提议** | `ADD IKEPROPOSAL` | 定义认证方法 + 认证/加密/完整性算法 + DH 组 |
| **IKE 对等体（Peer）** | `ADD IKEPEER` | 对端实体：PSK、远程地址、NAT 穿越、交换模式、本地 ID 类型 |
| **策略绑定提议** | `ADD PROPATTACHIPSECPROPOSAL` | 将 Proposal 绑定到 Policy Sequence |
| **策略绑定 Peer** | `ADD ATTACHIKEPEER` | 将 IKE Peer 绑定到 Policy Sequence，含优先级（主备用） |
| **隧道接口应用策略** | `ADD IPSECINTFCFGIPSEC` | 在 Tunnel 接口（TNLTYPE=IPSEC）应用 Policy |
| **ACL 规则组/规则** | `ADD ACLGROUPIPSEC` / `ADD ACLRULEADV4IPSEC` | 定义保护数据流（仅源/目的 IP） |
| **IKE 全局配置** | `SET IKEGLOBALCONFIG` | DPD 类型/间隔/重试、NAT 保活间隔 |
| **VNRS 镜像对象** | `ADD L3VPNINST` / `ADD INTERFACE` / `ADD IPSECINTFCFG` / `ADD IFIPV4ADDRESS` / `ADD SRROUTE` | VNRS 微服务侧的 VPN、隧道接口、静态路由镜像配置 |

> 来源：`激活IPsec功能（普通IPv4 IPsec隧道）_61317238.md`（"操作流程/操作步骤"完整 9 步）、`激活IPsec功能（GRE over IPsec）_78985535.md`（VNRS+IPsec 双配说明）[EV-FK-07, EV-FK-09]

### 2.3 在接入方式场景的角色

IPFD-016000 在 APN 接入方式场景中扮演**"加密三层隧道"**的角色，与 GRE（轻量不加密）、L2TP（二层 PPP 远程接入）、MPLS VPN（标签隧道）形成互补的隧道方案矩阵：

1. **三层加密隧道**：在 IP 层为报文提供加密 + 认证 + 完整性 + 防重放（区别于 GRE 的不加密、L2TP 的二层 PPP）
2. **C 面安全通道**：UNC 作为 SMF/PGW-C/SGW-C，建立 IPSec 隧道保护网管、信令、网间数据传输
3. **组合扩展**：通过 GRE over IPSec 弥补 IPSec 不支持组播/广播的缺陷；通过 OSPF over IPSec 保护动态路由
4. **高可靠**：DPD 失效检测 + 主备隧道（热备/冷备）保障业务连续性
5. **国密合规**：SM2/SM3/SM4 国密变体满足国内合规要求

> 来源：`IPFD-016000 IPSec功能特性概述_61317289.md`（"定义/应用场景"章节）、`IPsec可靠性_78460643.md`、`激活IPsec功能（GRE over IPsec）_78985535.md` [EV-FK-01, EV-FK-05, EV-FK-09]

---

## 3. 原理与流程

### 3.1 实现原理（IKE 协商 SA + AH/ESP 保护）

IPSec 通过数据流源端、目的端事先协商好的"约定（SA）"来加密、解密数据。SA 可手工创建（永不老化）或由 IKE 自动协商（含生存周期）。流程如下：

```
┌─────────────────────────────────────────────────────────────────┐
│ 阶段1：IKE 协商（自动建立 SA）                                     │
│                                                                 │
│   发起方                          响应方                          │
│     │  ── IKEv1 主模式 6 条 / 野蛮模式 3 条 ──→                    │
│     │  ── IKEv2 初始交换 4 条（IKE SA + 一对 IPSec SA）──→         │
│     │ ←──────── 协商 IKE SA（加密/认证/DH 组）────────              │
│     │  ── IKEv1 快速模式 3 条 / IKEv2 创建子 SA ──→                 │
│     │ ←──────── 协商 IPSec SA（SPI + 密钥 + 算法）─────             │
│                                                                 │
│   协商结果：建立 1 个 IKE SA + N 个 IPSec SA（每个 IPSec SA 单向）   │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 阶段2：数据传输（AH/ESP 保护，隧道模式封装）                        │
│                                                                 │
│   原始 IP 报文                                                   │
│        │                                                        │
│        ▼  匹配 ACL（保护数据流）                                  │
│   ┌──────────────────────────────────────────┐                  │
│   │ 隧道模式封装（加新 IP 头 + AH/ESP 头）        │                  │
│   │                                          │                  │
│   │  新IP头 | AH/ESP头 | 原始IP头 | Payload    │                  │
│   │  (源=本端  (认证   (被保护)               │                  │
│   │   目的=   /加密)                          │                  │
│   │   对端)                                   │                  │
│   └──────────────────────────────────────────┘                  │
│        │                                                        │
│        ▼  公网传输（被加密/认证保护）                              │
│   对端解封装 → 校验 ICV → 解密 → 转发原始报文                       │
└─────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 阶段3：SA 维护                                                   │
│                                                                 │
│   - 生存周期到达前 IKE 协商新 SA，平滑切换                         │
│   - DPD 检测对端可达性（periodic / on-demand）                     │
│   - 主备隧道故障切换（热备立即切换 / 冷备协商后切换）                │
└─────────────────────────────────────────────────────────────────┘
```

> 来源：`IPFD-016000 IPSec功能特性概述_61317289.md`（"实现原理"章节，图1/图2/图3 IPSec 协议与工作原理）、`安全联盟（SA）_62244156.md`、`IKE_62256396.md` [EV-FK-01, EV-FK-03, EV-FK-04]

### 3.2 AH 与 ESP（★重点：差异）

| 维度 | AH（协议号 51） | ESP（协议号 50） |
|------|----------------|------------------|
| 数据源认证 | ✓ | ✓ |
| 数据完整性 | ✓ | ✓ |
| 防重放攻击 | ✓ | ✓ |
| **数据加密** | **✗（不能防窃听）** | **✓（核心能力）** |
| **认证范围** | **报头 + 有效载荷**（含外层 IP 头） | **仅有效载荷**（不含 IP 头） |
| 认证强度 | **强**（AH 强于 ESP） | 弱（IP 头不在认证范围） |
| 典型用途 | 传输非机密数据 | 机密数据加密传输 |

两者可单独使用，也可结合使用（发送方先 ESP 封装再 AH 封装；接收方先 AH 解封装再 ESP 解封装）。

**ESP 认证算法**：SHA-1 / SHA2-256/384/512 / SM3 / MD5（建议 SHA2）
**ESP 加密算法**：AES-CBC-128/192/256 / AES-GCM-128/256 / **SM4** / AES-GMAC-128 / DES
**AH 认证算法**：同 ESP 认证算法集

> 来源：`AH和ESP_62244157.md`（"AH/ESP/AH 与 ESP 的差异"完整章节 + 认证/加密算法清单）[EV-FK-02]

### 3.3 IKE 协商（★重点：IKEv1 vs IKEv2）

IKE 用于动态创建 SA，具有 DH 交换、PFS 前向安全性、身份验证、身份保护等安全机制。

**IKEv1 两阶段**：
- **第一阶段**（建立 IKE SA）：主模式（Main Mode，6 条消息，身份受 DH 保护）/ 野蛮模式（Aggressive Mode，3 条消息，身份不加密，安全性低）
- **第二阶段**（建立 IPSec SA）：快速模式（Quick Mode，3 条消息）

**IKEv2 三种交换**：
- **初始交换**：4 条消息协商 IKE SA + 一对 IPSec SA
- **创建子 SA 交换**：每对 IPSec SA 增加 1 次交换（2 条消息）
- **通知交换**：传递控制/错误信息

**IKEv1 vs IKEv2 差异（IKEv2 优势）**：
| 维度 | IKEv1 | IKEv2 |
|------|-------|-------|
| 协商效率 | 主模式 6 条 + 快速模式 3 条 | 4 条消息完成 IKE SA + 一对 IPSec SA |
| 安全性 | 存在公认密码学漏洞 | 修复漏洞，支持 IKE SA 完整性算法 |
| 认证灵活性 | - | 加入 EAP 认证，支持 re-authentication |

> ★关键：**UNC 默认使用 IKEv2**。IKEv1 存在安全风险，可通过 `MOD IKEPEER` 将 "VERSION1" 设为 "FALSE" 关闭。

> 来源：`IKE_62256396.md`（"安全机制/IKEv1/IKEv2/IKEv1 与 IKEv2 的差异"完整章节，含 UNC 默认 IKEv2 说明）[EV-FK-03]

### 3.4 报文封装模式（隧道模式）

本特性 IPSec 采用**隧道模式（Tunnel）**（激活文档 ENCAPMODE=Tunnel）：将原始 IP 数据作为负载，在原始报文外增加新的 IP 报文头，并在新 IP 头与原始 IP 头之间插入 AH 或 ESP 协议头，保护整个 IP 数据报文。

> ★约束：当同时采用 AH 和 ESP 时，两者必须采用相同的报文封装模式。

> 来源：`报文封装模式_62256279.md`（"隧道模式"章节，图1 隧道模式报文格式）[EV-FK-04]

### 3.5 SA 特征（★重点：单向 + 协议相关）

SA（安全联盟）的两个核心特征：

1. **SA 是单向的**：通信对等体间双向通讯**最少需要两个 IPSec SA**（Outbound SA 加密方向 + Inbound SA 解密方向）
2. **SA 是与协议相关的**：若同时使用 AH 和 ESP，每端需 4 个 SA（AH 入/出 + ESP 入/出）

SA 由三元组唯一标识：**SPI（安全参数索引）+ 目的 IP 地址 + 安全协议号**。

SA 创建方式：
- 手工创建：永不老化，除非手动删除
- IKE 自动协商：含基于时间/基于流量的生存周期，到期前 IKE 自动协商新 SA

> 来源：`安全联盟（SA）_62244156.md`（"定义/创建方式/特征"章节，图1 SA 单向逻辑连接）[EV-FK-03]

### 3.6 IPSec NAT 穿越

当两个 IPSec 设备之间存在 NAT 设备时必须部署 NAT 穿越功能（NAT 改变源 IP/端口会影响 IPSec 报文与 IKE 协商）。

**实现原理**：对要穿越 NAT 的报文，IPSec 在新 IP 报文头后增加一个 **UDP 协议头**，用于 NAT 设备地址转换；同时对 NAT 进行探测，并增加保活消息（`NATKLI` 参数，默认 30 秒）避免 NAT 转换表超时。

**约束**：
- 仅适用于 **ESP 隧道模式**
- **不支持 IPv6 组网**

> 来源：`IPsec NAT穿越_62244160.md`（"定义/实现原理/约束限制"章节，图1 IPsec NAT 穿越报文转换）[EV-FK-06]

### 3.7 IPSec 可靠性（★重点：DPD + 主备隧道）

**IPSec DPD（失效对等体检测）**：IKE 协议本身无对等体状态检测机制，SA 生存周期到期前 SA 一直存在，对等体不可达将引发"黑洞"（数据丢弃、CPU 浪费、无法激活备用对等体）。UNC 支持 IPSec DPD，使用 IPSec 流量最小化探测报文数量。两种模式：

| 模式 | 定义 |
|------|------|
| **periodic（周期性检测）** | 检测间隔内未收到对端流量，以检测间隔为周期循环发送 DPD 检测报文 |
| **on-demand（按需检测）** | 仅当本端有加密流量要发送，且发送后 check-interval 内未收到对端流量时才发送 DPD；无加密流量时不发送 |

**IPSec 主备隧道**：本端与两个或以上对端同时建立 IPSec 隧道，主用不可用切换备用。

| 工作模式 | 定义 | 规格 |
|---------|------|------|
| **热备** | 主备隧道自动协商 SA；主用故障立即切换备用；故障恢复后若 `AUTOSWITCHBACK=Enable` 则切回主用 | **一主一备** |
| **冷备** | 主用自动协商 SA，备用默认不协商；主用故障时切换备用协商 SA | **最多一主两备**（按参数设置决定优先级） |

> 来源：`IPsec可靠性_78460643.md`（"DPD/主备隧道"完整章节，含模式定义表与规格）[EV-FK-05]

### 3.8 协议交互

| 接口 | 交互网元 | 消息类型 | 说明 |
|------|---------|---------|------|
| IKE 协商（UDP 500/4500） | IPSec 对等体（UNC↔UNC 或跨产品） | IKEv1/v2 协商报文 | 建立 IKE SA + IPSec SA |
| ESP 数据面（IP 协议号 50） | IPSec 对等体 | 加密后的 ESP 报文 | 隧道模式加密数据传输 |
| AH 数据面（IP 协议号 51） | IPSec 对等体 | 认证后的 AH 报文 | 隧道模式认证数据传输 |
| NAT 穿越（UDP 4500） | IPSec 对等体 + NAT 设备 | UDP 封装的 ESP/IKE | NAT 后端 IPSec 穿越 |
| DPD 探测 | IPSec 对等体 | DPD 检测报文 + 响应 | 对等体可达性检测 |
| VNRS↔IPsec 微服务 | UNC 内部 | 明文/密文引流 | VNRS 引流到 IPsec 微服务加解密 |

> 来源：`安全联盟（SA）_62244156.md`、`IKE_62256396.md`、`IPsec NAT穿越_62244160.md`、`激活IPsec功能（普通IPv4 IPsec隧道）_61317238.md`（VNRS+IPsec 微服务交互说明）[EV-FK-03, EV-FK-06, EV-FK-07]

### 3.9 与 GRE / L2TP / MPLS 隧道对比（★重点）

| 维度 | IPFD-016000/015004 IPSec | IPFD-015002 GRE | GWFD-020412/WSFD-104410 L2TP | GWFD-020411/WSFD-104411 MPLS VPN |
|------|--------------------------|----------------|------------------------------|----------------------------------|
| **隧道层级** | 三层（IP 加密） | 三层（IP 封装） | 二层（PPP 封装） | 二层半（MPLS 标签） |
| **加密** | **有（AH/ESP）** | 无 | 无 | 无 |
| **鉴权** | 有（IKE/PSK/证书） | 无（可选 Key） | 有（PAP/CHAP） | 无（依赖 BGP/IGP） |
| **封装开销** | 重（ESP/AH 头 + 加密运算） | 轻量（GRE 头 + 外层 IP） | 中（L2TP + PPP 头） | 轻（标签栈） |
| **对系统性能** | 有（加解密运算） | 无 | 有（封装 + 激活时延） | 低 |
| **License** | **无需** | 无需 | UDG 必须（82200BVC） | - |
| **组播/广播** | **不支持**（需 GRE over IPSec） | 支持 | 支持 | 支持 |
| **地址分配** | 不涉及 | 不涉及 | **LNS 远程分配** | 不涉及 |
| **C-U 模式** | **C-U 对称同构**（VNRS+IPsec 微服务双配） | C-U 对称同构 | C-U 分工（C 决策/U 作 LAC） | C-U 对称 |
| **典型 NF 角色** | IPSec 端点 | PE 设备 | UDG 作 LAC，LNS 在企业网 | PE 设备 |
| **核心标准** | RFC 2401/2402/2406/2403/4305/4868 | RFC 1701/1702/2784 | RFC 2661/2868 等 | RFC 4364 等 |
| **互斥关系** | 与 GRE 源地址互斥 | 与 IPSec 源地址互斥 | 与地址自动检测、入不转板互斥 | - |
| **组合关系** | GRE over IPSec / OSPF over IPSec | 可被 IPSec 嵌套 | - | - |
| **可靠性机制** | DPD + 主备隧道（热备/冷备） | Keepalive（5s/3 次） | Hello（60s/3 次） | VPN GR/NSR |

> 来源：综合本特性 12 篇文档 + IPFD-015002 GRE 知识文档（同域样例）+ 配置树 IPSec/GRE/L2TP/MPLS 特性描述 [EV-FK-01..12]

---

## 4. 配置规则

### 4.1 激活步骤（IPv4 IPSec 隧道，★核心流程）

```
步骤1：VNRS 微服务侧配置（VPN + 隧道接口 + 静态路由）
  ├── ADD L3VPNINST / ADD VPNINSTAF                    （VPN 实例）
  ├── ADD IPBINDVPN + ADD IFIPV4ADDRESS                （物理接口绑定 VPN）
  ├── ADD INTERFACE + ADD IPSECINTFCFG（TNLTYPE=IPSEC） （创建 IPSec 隧道接口）
  ├── ADD IPBINDVPN + ADD IFIPV4ADDRESS                （隧道接口绑定 VPN + IP）
  └── ADD SRROUTE                                       （静态路由出接口指向 Tunnel）

步骤2：IPsec 微服务侧配置（VPN + 隧道接口镜像）
  ├── ADD L3VPNINSTIPSEC / ADD VPNINSTAFIPSEC
  ├── ADD INTERFACEIPSEC + ADD IPBINDVPNIPSEC + ADD IFIPV4ADDRESSIPSEC
  └── ★双配原则：隧道接口名、IP、类型、VPN 必须与 VNRS 一致

步骤3：定义保护数据流（ACL，仅源/目的 IP）
  ├── ADD ACLGROUPIPSEC
  └── ADD ACLRULEADV4IPSEC

步骤4：配置 IPSec 安全提议
  └── ADD IPSECPROPOSALIPSEC（ENCAPMODE=Tunnel, IPSECPROTOCOL=Esp, 算法）

步骤5：配置 IKE 安全提议
  └── ADD IKEPROPOSAL（AUTHMETHOD=Pre_share, DHGROUP=Dh_group19, 算法）

步骤6：配置 IKE 对等体
  └── ADD IKEPEER（PRESHAREDKEY, LOWREMOTEADDR, NATTRAVERSAL=TRUE 可选）

步骤7：配置 IPSec 安全策略（聚合对象）
  ├── ADD IPSECPOLICY（POLICYMODE=Isakmp, ACLNUMBER）
  ├── ADD PROPATTACHIPSECPROPOSAL（绑定 Proposal）
  └── ADD ATTACHIKEPEER（绑定 IKE Peer + PEERPRIORITY）

步骤8：隧道接口应用策略
  └── ADD IPSECINTFCFGIPSEC（INTERFACENAME=Tunnel, TNLTYPE=IPSEC, POLICYNAME）

步骤9：（可选）配置 DPD / NAT 保活
  └── SET IKEGLOBALCONFIG（DPDTYPE, DPDINTERVAL, DPDRETRYINTRVL, NATKLI）
```

> 来源：`激活IPsec功能（普通IPv4 IPsec隧道）_61317238.md`（"操作步骤"9 步 + 完整脚本）[EV-FK-07]

### 4.2 MML 命令清单

#### 4.2.1 VNRS 微服务镜像命令（约 7 条）

| 命令 | 用途 | 本特性角色 |
|------|------|-----------|
| `ADD L3VPNINST` / `ADD VPNINSTAF` | VPN 实例 + 地址族 | VPN 组网场景下创建 VPN |
| `ADD IPBINDVPN` | 接口绑定 VPN | 物理接口 + 隧道接口绑定 VPN |
| `ADD IFIPV4ADDRESS` | 接口 IPv4 地址 | 物理接口 + 隧道接口 IP |
| `ADD INTERFACE` | 增加接口 | 创建 IPSec 隧道接口 |
| `ADD IPSECINTFCFG` | 创建 IPSec 隧道接口（TNLTYPE=IPSEC） | VNRS 侧隧道接口协议配置 |
| `ADD SRROUTE` | 静态路由 | 出接口指向 Tunnel，引导流量入隧道 |

#### 4.2.2 IPsec 微服务镜像命令（约 4 条）

| 命令 | 用途 |
|------|------|
| `ADD L3VPNINSTIPSEC` / `ADD VPNINSTAFIPSEC` | IPsec 微服务 VPN 实例镜像 |
| `ADD INTERFACEIPSEC` | IPsec 微服务接口镜像 |
| `ADD IPBINDVPNIPSEC` | IPsec 微服务接口绑定 VPN 镜像 |
| `ADD IFIPV4ADDRESSIPSEC` | IPsec 微服务接口 IPv4 地址镜像 |

#### 4.2.3 IPSec 安全对象命令（★核心，约 8 条）

| 命令 | 用途 | 本特性角色 |
|------|------|-----------|
| **ADD ACLGROUPIPSEC** | ACL 规则组 | 定义保护数据流容器 |
| **ADD ACLRULEADV4IPSEC** | 高级 ACL 规则 | 定义源/目的 IP（不支持端口） |
| **ADD IPSECPROPOSALIPSEC** | IPSec 安全提议 | 封装模式 + 安全协议 + 算法 |
| **ADD IKEPROPOSAL** | IKE 安全提议 | 认证方法 + 算法 + DH 组 |
| **ADD IKEPEER** | IKE 对等体 | PSK + 远程地址 + NAT 穿越 + 交换模式 |
| **ADD IPSECPOLICY** | IPSec 安全策略 | ★聚合对象（ACL + Proposal + Peer） |
| **ADD PROPATTACHIPSECPROPOSAL** | 策略绑定提议 | 将 Proposal 绑定到 Policy Sequence |
| **ADD ATTACHIKEPEER** | 策略绑定 Peer | 将 IKE Peer 绑定到 Policy Sequence（含优先级） |

#### 4.2.4 应用与全局命令（约 2 条）

| 命令 | 用途 |
|------|------|
| **ADD IPSECINTFCFGIPSEC** | 隧道接口应用 IPSec 策略 |
| **SET IKEGLOBALCONFIG** | IKE 全局配置（DPD + NAT 保活） |

#### 4.2.5 证书命令（RSA / 国密，2 条）

| 命令 | 用途 |
|------|------|
| `上传IPsec证书` | 上传 RSA 证书（证书认证场景） |
| `上传国密IPsec证书` | 上传国密 SM2 证书（国密变体场景） |

#### 4.2.6 调测查询命令（约 9 条）

| 命令 | 用途 |
|------|------|
| `PING` | 验证本端↔对端物理连通 + 隧道接口连通 |
| `DSP IFSTATUS` | 查询隧道接口物理/协议状态 |
| `LST IFIPV4ADDRESS` / `LST IFIPV4ADDRESSIPSEC` | 核对 VNRS 与 IPsec 微服务双配一致性 |
| `LST IPSECINTFCFGIPSEC` | 查询隧道接口绑定的 IPSec 策略 |
| `DSP IKESA` | ★查询 IKE 安全联盟（含 SA 标识、算法、DH 组、剩余时长） |
| `DSP IKEIPSECSA` | ★查询 IKE IPSec 安全联盟 |
| `LST IKEPEER` / `LST IKEPROPOSAL` / `LST IPSECPOLICY` / `LST PROPATTACHIPSECPROPOSAL` / `LST IPSECPROPOSALIPSEC` | 查询各对象配置 |

> 来源：`激活IPsec功能（普通IPv4 IPsec隧道）_61317238.md`（操作步骤全部命令）、`调测IPsec功能_61317192.md`（调测 8 步命令）[EV-FK-07, EV-FK-08]

### 4.3 关键参数说明

#### 4.3.1 ADD IPSECPOLICY（★聚合对象）

| 参数 | 取值 | 说明 |
|------|------|------|
| POLICYNAME | 字符串（如 "map1"） | 策略名称 |
| SEQUENCENUMBER | 数字（如 10） | 序列号；多 Sequence 场景下每 Sequence 对接不同 Peer |
| POLICYMODE | Isakmp | 策略模式（IKE 自动协商） |
| TEMPLATEMODE | None | 模板模式 |
| ACLNUMBER / ACLNAME | 数字 / 字符串（如 3000） | 引用 ACL 规则组（编号或名称） |
| WORKMODE | Master_standby（主备场景） | 工作模式（普通场景省略） |
| AUTOSWITCHBACK | Enable / Disable | 自动切回开关（主备场景，故障恢复后是否切回主用） |

#### 4.3.2 ADD IPSECPROPOSALIPSEC（IPSec 提议）

| 参数 | 取值 | 说明 |
|------|------|------|
| PROPOSALNAME | 字符串（如 "tran1"） | 提议名称 |
| IPSECPROTOCOL | Esp / Ah | 安全协议（ESP 加密 / AH 仅认证） |
| ENCAPMODE | Tunnel | 封装模式（本特性固定隧道模式） |
| ESPAUTHALGO | Sha2_256 等 | ESP 认证算法 |
| ESPENCRYPTALGO | Aes_256 / SM4 等 | ESP 加密算法 |

#### 4.3.3 ADD IKEPROPOSAL（IKE 提议）

| 参数 | 取值 | 说明 |
|------|------|------|
| PROPOSALNUMBER | 1~100（如 10） | 提议号（本端配置记录，无需与对端一致） |
| AUTHMETHOD | Pre_share | 认证方法（预共享密钥；另有证书认证） |
| AUTHALGORITHM | Sha2_256 | 认证算法 |
| ENCRALGORITHM | Aes_cbc_256 | 加密算法 |
| INTEGALGORITHM | Hmac_sha2_256 | 完整性算法（IKEv2） |
| DHGROUP | Dh_group19（建议）/ 不能为 None | DH 组 |
| SADURATION | 3600（GRE over IPSec 场景） | SA 持续时长（秒） |

#### 4.3.4 ADD IKEPEER（IKE 对等体）

| 参数 | 取值 | 说明 |
|------|------|------|
| PEERNAME | 字符串（如 "b"） | 对等体名称 |
| PRESHAREDKEY | 字符串（如 "abcde"） | 预共享密钥（两端必须相同） |
| NATTRAVERSAL | TRUE / FALSE | NAT 穿越（两端间有 NAT 设备时必 TRUE） |
| EXCHANGEMODE | Main（GRE over IPSec 场景） | 交换模式（IKEv1 主模式 / 野蛮模式） |
| LOCALIDTYPE | Ip（GRE over IPSec 场景） | 本地 ID 类型 |
| LOWREMOTEADDR | IP（如 "192.168.1.2"） | 远程地址（不能为地址段） |
| INVRFNAME / OUTVRFNAME | VPN 实例名 | SA 绑定 / 远程地址 VPN |

#### 4.3.5 ADD ATTACHIKEPEER（策略绑定 Peer，主备场景）

| 参数 | 取值 | 说明 |
|------|------|------|
| IKEPEERNAME | 字符串 | 绑定的 IKE Peer |
| **PEERPRIORITY** | 1（主用）/ 2（备用） | ★优先级（主备隧道场景决定主备） |

#### 4.3.6 SET IKEGLOBALCONFIG（全局 DPD / NAT 保活）

| 参数 | 取值 | 说明 |
|------|------|------|
| DPDTYPE | Periodic / On-demand | DPD 模式 |
| DPDINTERVAL | 10（秒） | DPD 检查间隔 |
| DPDRETRYINTRVL | 3（秒） | DPD 重试间隔 |
| NATKLI | 30（秒） | NAT 保活时间间隔（NATTRAVERSAL=TRUE 时生效） |

> 来源：`激活IPsec功能（普通IPv4 IPsec隧道）_61317238.md`（"必备事项/数据"完整参数表）、`激活IPsec功能（IPv4 IPsec主备隧道）_88744738.md`（WORKMODE/AUTOSWITCHBACK/PEERPRIORITY）、`激活IPsec功能（GRE over IPsec）_78985535.md`（SADURATION/EXCHANGEMODE/LOCALIDTYPE）[EV-FK-07, EV-FK-09, EV-FK-10]

### 4.4 约束条件

| 约束类型 | 约束内容 | 来源 |
|---------|---------|------|
| **VNRS + IPsec 微服务双配（★关键）** | 隧道接口、接口 IP、隧道类型、VPN、指定本端接口必须在两微服务一对一配置，否则业务不通 | 激活文档"操作流程"说明 |
| **不支持场景** | GREv6 over IPSecv6、OSPFv3 over IPSecv6、IPSecv6 地址借用、IPV4 入 IPSecv6、IPV6 入 IPSecv4 | 特性概述"应用限制" |
| **NAT 穿越** | 仅适用 ESP 隧道模式；不支持 IPv6 组网 | NAT 穿越文档"约束限制" |
| **AH/ESP 封装模式一致** | 同时采用 AH 和 ESP 时必须采用相同封装模式 | 报文封装模式文档 |
| **ACL 仅源/目的 IP** | ACL 只支持源 IP 和目的 IP，端口配置不生效 | 激活文档 ACL 说明 |
| **DHGROUP 不能为 None** | 建议 Dh_group19，不能不配置 | 激活文档步骤5 说明 |
| **预共享密钥对称** | PSK 方式下两端必须相同，否则 SA 建立不成功 | 激活文档步骤5/6 说明 |
| **远程地址不能为地址段** | IKE Peer 远程地址必须为具体 IP | 激活文档步骤6 说明 |
| **指定本端接口独占** | 被 IPSec 指定的接口需被 IPSec 单独使用，否则其他协议不生效 | 指定本端接口激活文档 |
| **IKEv2 优先** | UNC 默认 IKEv2；对端不支持时禁用 IKEv2 用 IKEv1 | 激活文档步骤6 说明 |
| **主备隧道规格** | 热备一主一备；冷备最多一主两备 | 可靠性文档规格表 |

---

## 5. 配置案例

### 5.1 典型场景：普通 IPv4 IPSec 隧道（ESP + PSK + NAT 穿越 + DPD）

**场景描述**：网络 A（10.1.1.0/24，PCA=10.1.1.2）与网络 B（10.1.2.0/24，PCB=10.1.2.2）通过 Device A、Device B 网关对网关组网，建立 IPSec 隧道实现 PCA↔PCB 安全互访，启用 NAT 穿越与 DPD。本端 Tunnel10=192.168.1.1/32，对端 Tunnel10=192.168.1.2/32。

**配置步骤和 MML 命令序列**（保留原始 MML，本端 Device A）：

```
=== VNRS 微服务侧配置（Device A） ===

// 创建 VPN 实例。
ADD L3VPNINST:VRFNAME="vrf1";
ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;

// 绑定 VNRS 与 VPN，配置物理接口 IP。
MOD INTERFACE:IFNAME="Ethernet66/0/5", IFADMINSTATUS=up;
MOD INTERFACE:IFNAME="Ethernet66/0/6", IFADMINSTATUS=up;
ADD IPBINDVPN:IFNAME="Ethernet66/0/5", VRFNAME="vrf1";
ADD IPBINDVPN:IFNAME="Ethernet66/0/6", VRFNAME="vrf1";
ADD IFIPV4ADDRESS:IFNAME="Ethernet66/0/5", IFIPADDR="10.1.1.1", SUBNETMASK="255.255.255.0";
ADD IFIPV4ADDRESS:IFNAME="Ethernet66/0/6", IFIPADDR="172.16.163.1", SUBNETMASK="255.255.255.0";

// 创建 VNRS 侧 IPSec 隧道接口（TNLTYPE=IPSEC），绑定 VPN 配 IP。
ADD INTERFACE:IFNAME="Tunnel10", IFADMINSTATUS=up;
ADD IPSECINTFCFG:INTERFACENAME="Tunnel10",TNLTYPE=IPSEC;
ADD IPBINDVPN:IFNAME="Tunnel10", VRFNAME="vrf1";
ADD IFIPV4ADDRESS:IFNAME="Tunnel10", IFIPADDR="192.168.1.1", SUBNETMASK="255.255.255.255";

// 静态路由：目的网络出接口指向 Tunnel10。
ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.2.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.2",IFNAME="Tunnel10";
ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.2",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.169.2",IFNAME="Invalid0";

=== IPsec 微服务侧配置（Device A，★双配） ===

ADD L3VPNINSTIPSEC:VRFNAME="vrf1";
ADD VPNINSTAFIPSEC:VRFNAME="vrf1", AFTYPE=Ipv4uni;
ADD INTERFACEIPSEC:IFNAME="Tunnel10", IFADMINSTATUS=Up;
ADD IPBINDVPNIPSEC:IFNAME="Tunnel10", VRFNAME="vrf1";
ADD IFIPV4ADDRESSIPSEC:IFNAME="Tunnel10", IFIPADDR="192.168.1.1", SUBNETMASK="255.255.255.255";

=== IPSec 安全对象配置（Device A） ===

// 高级 ACL 3000，允许 PCA 访问 PCB。
ADD ACLGROUPIPSEC:ACLNAME ="3000";
ADD ACLRULEADV4IPSEC:ACLNAME="3000",ACLRULENAME="rule_1",ACLACTION=Permit,VRFNAME="vrf1",ACLPROTOCOL=0,ACLSOURCEIP="10.1.1.2",ACLSRCWILD="0.0.0.0",ACLDESTIP="10.1.2.2",ACLDESTWILD="0.0.0.0";

// IPSec 安全提议 tran1：ESP + 隧道模式。
ADD IPSECPROPOSALIPSEC:PROPOSALNAME="tran1",ESPAUTHALGO=Sha2_256,ESPENCRYPTALGO=Aes_256,IPSECPROTOCOL=Esp,ENCAPMODE=Tunnel;

// IKE 安全提议 10：PSK + SHA2-256 + DH group19。
ADD IKEPROPOSAL:PROPOSALNUMBER=10,AUTHMETHOD=Pre_share, AUTHALGORITHM=Sha2_256,DHGROUP=Dh_group19;

// IKE 对等体 b：PSK=abcde，NAT 穿越使能，远程地址 192.168.1.2。
ADD IKEPEER:PEERNAME="b",PRESHAREDKEY="abcde",NATTRAVERSAL=TRUE,PROPOSAL=10,LOWREMOTEADDR="192.168.1.2",INVRFNAME="vrf1",OUTVRFNAME="vrf1";

// IPSec 安全策略 map1：Sequence 10，引用 ACL 3000。
ADD IPSECPOLICY:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,ACLNUMBER=3000;
ADD PROPATTACHIPSECPROPOSAL:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,IPSECPROPNAME="tran1";
ADD ATTACHIKEPEER:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,IKEPEERNAME="b",PEERPRIORITY=1;

// 在 Tunnel10 应用策略 map1。
ADD IPSECINTFCFGIPSEC:INTERFACENAME="Tunnel10",TNLTYPE=IPSEC,POLICYNAME="map1";

// DPD + NAT 保活（可选）。
SET IKEGLOBALCONFIG:DPDINTERVAL=10,DPDTYPE=Periodic,DPDRETRYINTRVL=3,NATKLI=30;

=== Device B 配置脚本（对称，源/目的 IP 互换，IKEPEER 名为 "a"） ===
//（完整对称脚本见源文档，ACL 源/目的、IKEPEER 名称、LOWREMOTEADDR 互换）
```

> 来源：`激活IPsec功能（普通IPv4 IPsec隧道）_61317238.md`（"任务示例/脚本"完整原文，Device A + Device B）[EV-FK-07]

### 5.2 场景变体（10 种，均有独立激活文档）

| 变体 | 场景说明 | 核心差异 | 文档 |
|------|---------|---------|------|
| 普通 IPv4 IPSec 隧道 | 网关对网关加密 | 基础场景（5.1） | `_61317238.md` |
| 普通 IPv6 IPSec 隧道 | IPv6 组网 | IFIPV6ADDRESS、IPv6 ACL | `_78985538.md` |
| IPv4 IPSec 主备隧道 | 高可靠 | WORKMODE=Master_standby + 多 PEERPRIORITY + AUTOSWITCHBACK | `_88744738.md` |
| IPv6 IPSec 隧道主备方式 | IPv6 + 高可靠 | IPv6 + 主备 | `_53998700.md` |
| 多 Sequence IPSec 策略 | 一隧多 Peer | 单隧道多 Sequence，对接多 IKE Peer | `_78985536.md` |
| 指定本端接口建立隧道 | LoopBack 作 IKE 源 | SRCINTERFACE 指定 LoopBack，多隧道共用 | `_78985537.md` |
| GRE over IPSec | 组播广播加密 | 先 GRE 封装（Tunnel1）再引入 IPSec（Tunnel2），ACL 匹配 GRE 源/目的 | `_78985535.md` |
| OSPF over IPSec | 保护 OSPF 路由 | IPSec 隧道承载 OSPF 协议报文 | `_90949389.md` |
| 国密 IKEv1（IPv4） | 国密合规 | 国密 SM2 证书 + SM3/SM4 算法 | `_03728909.md` |
| 国密 IKEv1（IPv6/多 Seq/GRE over） | 国密变体扩展 | 国密 + 其他变体组合 | `_53768408.md` / `_03408185.md` / `_53928160.md` / `_03567841.md` |

> 来源：各激活文档"操作场景"章节（见文档清单 Batch-31）[EV-FK-07..12]

---

## 6. 验证与调测

### 6.1 验证方法（调测 8 步）

```
步骤1：本端↔对端物理连通性
  └── PING: IPVERSION=IPv4, DESTIPV4ADDRESS="172.16.169.1"
      预期：0% 丢包；异常→Ping 不通定位思路

步骤2：本端 IPSec 隧道接口状态
  └── DSP IFSTATUS: IFNAME="Tunnel10"
      预期：物理 + 协议均 Up；异常→步骤3

步骤3：VNRS 与 IPsec 微服务双配一致性
  ├── LST IFIPV4ADDRESS: IFNAME="Tunnel10"        （VNRS 侧）
  └── LST IFIPV4ADDRESSIPSEC: IFNAME="Tunnel10"    （IPsec 侧）
      预期：两微服务接口 IP 一致；异常→按规划修改

步骤4：隧道接口绑定 IPSec 策略
  └── LST IPSECINTFCFGIPSEC: INTERFACENAME="Tunnel10"
      预期：绑定策略符合规划（Tunnel口协议类型=IPv4IP安全，策略名称=map1）

步骤5：本端↔对端隧道接口连通性
  └── PING: DESTIPV4ADDRESS="192.168.1.2"
      预期：0% 丢包；异常→步骤8

步骤6：查询 IKE SA（★关键）
  └── DSP IKESA:;
      预期：可查询到 IKE SA，SA 标识 ≠ NO STATE
      输出含：远端地址、阶段(1)、认证方法(预共享)、认证/加密/完整性算法、DH 组、剩余 SA 长度、IKE 版本

步骤7：查询 IKE IPSec SA（★关键）
  └── DSP IKEIPSECSA:;
      预期：可查询到 IKE IPSec SA，调测结束

步骤8：检查 IPSec 相关配置（异常排查）
  ├── LST IKEPEER
  ├── LST IKEPROPOSAL
  ├── LST IPSECPOLICY
  ├── LST PROPATTACHIPSECPROPOSAL
  └── LST IPSECPROPOSALIPSEC
      按网络规划核对修改
```

**DSP IKESA 典型输出**：

```
地址类型  =  IPv4地址
远端地址  =  192.168.1.2
POD名称   =  ipsecexec-pod-0172-16-1-189
连接ID    =  4
SA标识    =  RD|ST
阶段      =  1
本端地址  =  192.168.1.1
触发端Cookie  =  6b51edace1187e9
回应端Cookie  =  8bc6f6612aacc1ec
接口名称  =  Tunnel10
认证方法  =  预共享
认证算法  =  sha2-256算法
加密算法  =  256位AES算法
完整性算法=  sha2-256算法
DH组      =  DH组14
剩余SA长度=  86295
IKE版本   =  版本2
```

> 来源：`调测IPsec功能_61317192.md`（"操作步骤"8 步 + DSP IKESA 完整输出）[EV-FK-08]

### 6.2 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| Ping 对端物理 IP 不通 | 路由不可达 | 检查路由配置；PING 验证 |
| 隧道接口协议 Down | VNRS 与 IPsec 微服务双配不一致 | LST IFIPV4ADDRESS + LST IFIPV4ADDRESSIPSEC 核对一致性 |
| 隧道接口未绑定策略 | ADD IPSECINTFCFGIPSEC 缺失 | LST IPSECINTFCFGIPSEC 核对 |
| IKE SA 查询不到或 NO STATE | IKE 协商失败 | 步骤8 排查 IKEPEER/IKEPROPOSAL/IPSECPOLICY |
| IKE IPSec SA 查询不到 | IPSec 提议配置错误 | LST IPSECPROPOSALIPSEC 核对算法/协议/封装模式 |
| SA 协商失败（PSK） | 两端预共享密钥不同 | 核对两端 PRESHAREDKEY |
| SA 协商失败（IKE 版本） | 版本不匹配 | UNC 默认 IKEv2，对端不支持时禁用 IKEv2 |
| SA 协商失败（DH 组） | DHGROUP 为 None 或两端不一致 | 建议 Dh_group19，不能为 None |
| NAT 场景协商失败 | 未启用 NAT 穿越 | ADD IKEPEER NATTRAVERSAL=TRUE + SET IKEGLOBALCONFIG NATKLI=30 |
| 对等体不可达黑洞 | 未启用 DPD | SET IKEGLOBALCONFIG DPDTYPE=Periodic |
| 主备未切换 | AUTOSWITCHBACK / PEERPRIORITY 配置错误 | LST IPSECPOLICY 核对 WORKMODE/AUTOSWITCHBACK |
| 组播广播不通 | IPSec 不支持组播广播 | 改用 GRE over IPSec 场景 |
| 指定接口后其他协议失效 | 被指定接口未独占 | 确保 LoopBack 仅 IPSec 使用 |
| IPv4 入 IPSecv6 / IPv6 入 IPSecv4 | 不支持场景 | 核对地址族匹配（应用限制） |

---

## 7. 参考信息

### 7.1 与其他特性的关系

| 关联特性 | 特性ID | 关系说明 |
|---------|--------|---------|
| VPN 功能（配置树父节点） | IPFD-015000 | 配置树父节点（接入方式类） |
| **IPSec 功能（UDG 侧）** | **IPFD-015004** | **★C-U 对称同构**：两侧文档源 ID 一致（61317289/88277392 等），原理同构；仅命令路径前缀（VNRS/IPsec 微服务 vs UDG 命令行）不同 |
| **GRE（UDG+UNC）** | IPFD-015002 | **源地址互斥 + 组合**：GRE 源地址不能与 IPSec 源地址相同；可组合为 GRE over IPSec |
| L2TP VPN（UDG/UNC） | GWFD-020412 / WSFD-104410 | **隧道方案矩阵**：IPSec 为三层加密隧道，L2TP 为二层 PPP 远程接入（含 LNS 地址分配）；并列可选方案 |
| MPLS VPN（UDG/UNC） | GWFD-020411 / WSFD-104411 | **隧道方案矩阵**：IPSec 为加密隧道，MPLS VPN 为标签隧道；并列可选方案 |
| OSPF | IPFD-014001 | **协同**：OSPF over IPSec 场景，IPSec 保护 OSPF 协议报文 |
| Radius 功能 | WSFD-011306 | **应用场景**：UNC 到 AAA Server 组网可使用 GRE VPN（与 IPSec 互补的隧道方案） |
| 国密算法（SM2/SM3/SM4） | - | **变体**：本特性提供国密 IKEv1 激活场景，使用国密证书与算法 |

### 7.2 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `output/UNC 20.15.2.../IPFD-016000 IPSec功能/IPFD-016000 IPSec功能特性概述_61317289.md` | **★特性定义**（IPSec 开放 IP 层安全框架）、客户价值（私密性/完整性/真实性/防重放）、应用场景、可获得性（UNC 20.5.0+/20.8.0，**无需 License**）、对系统影响（封装性能影响）、**应用限制（5 种不支持场景）**、实现原理（IKE+AH+ESP）、计费话单（无）、特性规格（无特殊）、**遵循标准（RFC 2401/2402/2406/2403/4305/4868/4314）**、发布历史（v01 20.5.0，v02 20.8.0） |
| 2 | `相关术语_88277392.md` | 8 个核心术语定义：对等体、SA、SPI、Proposal、SP、Life Time、SADB、SPDB |
| 3 | `实现原理/AH和ESP_62244157.md` | **AH/ESP 完整说明**：AH（协议号 51，认证+完整性+防重放，不加密）、ESP（协议号 50，含加密）、报文头/尾结构、认证算法（SHA-1/SHA2/SM3/MD5）、ESP 加密算法（AES-CBC/AES-GCM/SM4/DES）、**AH 与 ESP 差异（认证范围/强度）** |
| 4 | `实现原理/IKE_62256396.md` | **IKE 完整说明**：安全机制（DH/PFS/身份验证/身份保护）、IKEv1（主模式 6 条/野蛮模式 3 条 + 快速模式 3 条）、IKEv2（初始/创建子 SA/通知交换）、**IKEv1 vs IKEv2 差异**、**UNC 默认 IKEv2 + MOD IKEPEER VERSION1=FALSE 关闭 IKEv1** |
| 5 | `实现原理/IPsec可靠性_78460643.md` | **DPD**（periodic/on-demand 两种模式，防黑洞）、**主备隧道**（热备一主一备/冷备最多一主两备 + AUTOSWITCHBACK） |
| 6 | `实现原理/IPsec NAT穿越_62244160.md` | NAT 穿越必要性（NAT 改 IP/端口影响 IPSec）、实现原理（UDP 封装 + NAT 保活 NATKLI）、**约束（仅 ESP 隧道模式，不支持 IPv6）** |
| 7 | `实现原理/安全联盟（SA）_62244156.md` | SA 定义（IKE SA/IPSec SA）、**SA 三元组（SPI+目的 IP+协议号）**、创建方式（手工/IKE）、**SA 特征（单向 + 协议相关）** |
| 8 | `实现原理/报文封装模式_62256279.md` | **隧道模式**（加新 IP 头 + AH/ESP 头，保护整个 IP 报文）、AH/ESP 封装模式一致约束 |
| 9 | `特性配置/激活IPsec功能（普通IPv4 IPsec隧道）_61317238.md` | **★激活完整 9 步流程**、VNRS+IPsec 微服务双配说明、**完整参数表（ADD IPSECPOLICY/IPSECPROPOSALIPSEC/IKEPROPOSAL/IKEPEER/ATTACHIKEPEER 等）**、ACL 仅源/目的 IP 约束、DHGROUP 不能为 None、PSK 对称性、IKEv2 默认、**完整 MML 脚本（Device A + Device B）** |
| 10 | `调测IPsec功能_61317192.md` | **调测 8 步流程**、设备接口 IP 表、**DSP IKESA 完整输出样例**（SA 标识/算法/DH 组/剩余时长/IKE 版本）、DSP IKEIPSECSA、异常排查配置查询命令清单 |
| 11 | `特性配置/激活IPsec功能（GRE over IPsec）_78985535.md` | GRE over IPSec 场景（IPSec 不支持组播广播）、先 GRE 封装（Tunnel1）再 IPSec（Tunnel2）、ACL 匹配 GRE 源/目的、SADURATION/EXCHANGEMODE/LOCALIDTYPE 参数 |
| 12 | `特性配置/激活IPsec功能（IPv4 IPsec主备隧道）_88744738.md` + `（多Sequence）_78985536.md` + `（指定本端接口）_78985537.md` | 主备隧道（WORKMODE=Master_standby + AUTOSWITCHBACK + PEERPRIORITY）、多 Sequence（单隧多 Peer）、指定本端接口（LoopBack 作 IKE 源，独占约束） |

> 注：其余 12 篇激活文档（IPv6、IPv6 主备、OSPF over IPSec、5 个国密 IKEv1 变体、上传证书 ×2）为变体场景，结构与 5.1 同构，参数差异见 §4.3 与 §5.2。

### 7.3 关键术语速查

| 术语 | 全称 | 说明 |
|------|------|------|
| IPSec | Internet Protocol Security | IP 层安全框架协议族 |
| AH | Authentication Header | IP 认证头协议（协议号 51，不加密） |
| ESP | Encapsulating Security Payload | IP 封装安全载荷（协议号 50，加密） |
| IKE | Internet Key Exchange | 密钥交换协议（IKEv1/IKEv2，UNC 默认 v2） |
| SA | Security Association | 安全联盟（IKE SA + IPSec SA） |
| SPI | Security Parameters Index | 安全参数索引（SA 三元组之一） |
| DPD | Dead Peer Detection | 失效对等体检测（periodic/on-demand） |
| VNRS 微服务 | - | UNC 内部微服务（外部通信 + 引流） |
| IPsec 微服务 | - | UNC 内部微服务（IKE 协商 + 加解密） |
| 双配原则 | - | VNRS 与 IPsec 微服务一对一配置 |
| 主备隧道 | Master-standby | 热备（一主一备）/ 冷备（一主两备） |

---

## 8. 文档一致性说明（配置树 vs 产品文档）

> 配置树仅用于定位特性 ID，以下记录以产品文档实际内容为准时发现的关键点，供 Stage 3 横向分析参考。

### 8.1 与任务要求中提及对象的核对（★重点澄清）

| # | 任务要求提及 | 产品文档实际 | 核对结论 |
|---|-------------|-------------|---------|
| 1 | **SMF 侧 IPSec** | **确认**：IPFD-016000 为 UNC（含 SGW-C/PGW-C/SMF）侧 IPSec 实现。UNC 20.5.0 首发，20.8.0 扩展 IPv6/NAT 穿越/主备隧道 | 已覆盖（见 §1.2、§1.3） |
| 2 | **与 IPFD-015004（UDG 侧 IPSec）的 C-U 对称关系（对称同构还是分工？）** | **★关键发现**：IPFD-016000（UNC）与 IPFD-015004（UDG）为 **C-U 对称同构**，非分工型。证据：(a) 两特性概述文件 ID 均为 `61317289`，术语文件 ID 均为 `88277392`，AH/ESP/IKE/SA/NAT 穿越/可靠性/封装模式 7 个原理文件 ID 完全一致；(b) 激活脚本结构同构（均含 ACL+Proposal+IKEPeer+Policy+隧道接口应用+DPD 全套对象）；(c) 仅命令路径前缀不同（UNC 走 VNRS+IPsec 微服务双配，UDG 走 UDG 命令行）。**这与 L2TP 的 C-U 分工（C 决策下发 LNS 参数 / U 作 LAC 封装）形成鲜明对比** | **澄清**：IPSec 在 C/U 两侧对称同构，两侧各自独立建立 IPSec 隧道（端到端加密对等体），无 C-U 分工 |
| 3 | **IKE 协商** | **确认**：IKE 含 IKEv1（主模式 6 条/野蛮模式 3 条 + 快速模式 3 条）与 IKEv2（初始 4 条/创建子 SA/通知交换）。**UNC 默认 IKEv2**，IKEv1 存在安全风险可通过 MOD IKEPEER VERSION1=FALSE 关闭。DH 交换 + PFS + 身份验证 + 身份保护四项安全机制 | 已覆盖（见 §3.3） |
| 4 | **IPSec 配置对象与命令（文档依据）** | **确认**：核心对象为 **IPSec 安全策略（ADD IPSECPOLICY，聚合 ACL+Proposal+Peer）**，辅以 IPSec 提议（ADD IPSECPROPOSALIPSEC）、IKE 提议（ADD IKEPROPOSAL）、IKE 对等体（ADD IKEPEER）、ACL（ADD ACLGROUPIPSEC/ACLRULEADV4IPSEC）、策略绑定（ADD PROPATTACHIPSECPROPOSAL/ATTACHIKEPEER）、隧道接口应用（ADD IPSECINTFCFGIPSEC）、全局配置（SET IKEGLOBALCONFIG）。★UNC 特色：VNRS+IPsec 微服务双配（镜像 VPN/接口/IP）。共 20+ 条 MML 命令 | 已覆盖（见 §4.2） |
| 5 | **与 GRE/L2TP/MPLS 隧道对比** | **确认**：IPSec 为三层加密隧道（区别于 GRE 轻量不加密、L2TP 二层 PPP 远程接入、MPLS 标签隧道）。IPSec 与 GRE 源地址互斥；可组合 GRE over IPSec（弥补 IPSec 不支持组播广播）；UNC 侧无需 License（区别于 L2TP UDG 必须 License） | 已覆盖（见 §3.9） |

### 8.2 与配置树/文档清单的差异

| # | 维度 | 配置树/文档清单描述 | 产品文档实际内容 | 差异类型 |
|---|------|---------------------|-----------------|---------|
| 1 | C-U 对称性 | 文档清单分别列 IPFD-015004（UDG，24 文件）与 IPFD-016000（UNC，24 文件） | **两特性文档源 ID 完全一致**（概述/术语/7 个原理文件），为同一份特性文档的 C/U 两侧部署 | 澄清：C-U 对称同构，非两套独立特性 |
| 2 | License 要求 | 文档清单标注"[★核心]" | 产品文档明确声明"**无需 License**"（两侧均无） | 澄清：IPSec 无 License，区别于 L2TP（UDG 必须 82200BVC） |
| 3 | 版本支持 | 文档清单未说明 | UNC **20.5.0 首发**（晚于多数 20.0.0 特性），20.8.0 扩展 IPv6/NAT 穿越/主备隧道 | 补全：版本支持信息 |
| 4 | 微服务架构 | 文档清单未提及 | UNC 侧 IPSec 通过 **VNRS 微服务 + IPsec 微服务**实现，遵循**双配原则**（UNC 特有架构，UDG 侧无此概念） | 补全：UNC 特有微服务双配架构 |
| 5 | 国密变体 | 文档清单仅列"国密 IPSec 证书"1 项 | 实际有 **5 个国密 IKEv1 激活场景**（IPv4/IPv6/多 Seq/指定接口/GRE over IPSec）+ 1 个上传国密证书 | 补全：国密变体完整覆盖 |
| 6 | 可靠性机制 | 文档清单未提及 | DPD（periodic/on-demand）+ 主备隧道（热备一主一备/冷备一主两备） | 补全：可靠性章节独立文档 |
| 7 | 与父节点关系 | 配置树父节点为 IPFD-015000 VPN 功能 | 本特性 24 篇文档**未直接提及** IPFD-015000 | 推断关系，Stage 3 验证 |

### 8.3 与同域隧道特性的横向对比（★Stage 3 重点）

| # | 维度 | IPFD-016000/015004 IPSec | IPFD-015002 GRE | GWFD-020412/WSFD-104410 L2TP | GWFD-020411/WSFD-104411 MPLS VPN |
|---|------|--------------------------|----------------|------------------------------|----------------------------------|
| 1 | 隧道层级 | 三层（IP 加密） | 三层（IP 封装） | 二层（PPP 封装） | 二层半（MPLS 标签） |
| 2 | 加密 | **有（AH/ESP）** | 无 | 无 | 无 |
| 3 | 鉴权 | 有（IKE/PSK/证书） | 无（可选 Key） | 有（PAP/CHAP） | 无 |
| 4 | 地址分配 | 不涉及 | 不涉及 | LNS 远程分配 | 不涉及 |
| 5 | License | **无** | 无 | UDG 必须（82200BVC） | - |
| 6 | C-U 模式 | **对称同构** | 对称同构 | **C-U 分工** | 对称 |
| 7 | 微服务架构 | **VNRS+IPsec 双配（UNC）** | 无 | 无 | 无 |
| 8 | 性能影响 | 有（加解密） | 无 | 有（封装+时延） | 低 |
| 9 | 组播广播 | **不支持**（需 GRE over IPSec） | 支持 | 支持 | 支持 |
| 10 | 可靠性 | DPD + 主备隧道（热备/冷备） | Keepalive（5s/3 次） | Hello（60s/3 次） | VPN GR/NSR |
| 11 | 互斥关系 | 与 GRE 源地址互斥 | 与 IPSec 源地址互斥 | 与地址自动检测/入不转板互斥 | - |
| 12 | 组合关系 | GRE over IPSec / OSPF over IPSec | 可被 IPSec 嵌套 | - | - |
| 13 | 典型 NF 角色 | IPSec 端点 | PE 设备 | UDG 作 LAC，LNS 在企业网 | PE 设备 |
| 14 | 标准 | RFC 2401/2402/2406 等 | RFC 1701/1702/2784 | RFC 2661/2868 等 | RFC 4364 等 |
| 15 | UNC 首发版本 | 20.5.0 | 20.0.0 | 20.0.0 | 20.0.0 |

---

## 附录 A：source_evidence_ids 占位映射

| evidence_id | 对应来源文件 | 主要贡献章节 |
|-------------|-------------|-------------|
| EV-FK-01 | `IPFD-016000 IPSec功能特性概述_61317289.md` | 特性定义、客户价值、应用场景、可获得性（UNC 20.5.0+/20.8.0，无 License）、对系统影响、**应用限制（5 种不支持场景）**、实现原理、计费话单（无）、特性规格（无特殊）、**遵循标准（RFC 2401/2402/2406/2403/4305/4868/4314）**、发布历史 |
| EV-FK-02 | `实现原理/AH和ESP_62244157.md` | AH（协议号 51，不加密）与 ESP（协议号 50，加密）完整说明、报文头/尾结构、认证算法（SHA/SM3/MD5）、ESP 加密算法（AES-CBC/AES-GCM/SM4/DES）、**AH 与 ESP 差异（认证范围与强度）** |
| EV-FK-03 | `实现原理/IKE_62256396.md` + `安全联盟（SA）_62244156.md` | IKE 安全机制（DH/PFS/身份验证/身份保护）、IKEv1（主/野蛮/快速模式）、IKEv2（初始/创建子 SA/通知）、**IKEv1 vs IKEv2 差异**、**UNC 默认 IKEv2 + 关闭 IKEv1 方法**；SA 定义/三元组/创建方式/**SA 单向 + 协议相关特征** |
| EV-FK-04 | `实现原理/报文封装模式_62256279.md` | 隧道模式（加新 IP 头 + AH/ESP 头）、AH/ESP 封装模式一致约束 |
| EV-FK-05 | `实现原理/IPsec可靠性_78460643.md` | DPD（periodic/on-demand 两种模式）、**主备隧道（热备一主一备/冷备最多一主两备 + AUTOSWITCHBACK）** |
| EV-FK-06 | `实现原理/IPsec NAT穿越_62244160.md` | NAT 穿越必要性、实现原理（UDP 封装 + NATKLI 保活）、**约束（仅 ESP 隧道模式，不支持 IPv6）** |
| EV-FK-07 | `特性配置/激活IPsec功能（普通IPv4 IPsec隧道）_61317238.md` | **★激活完整 9 步流程**、VNRS+IPsec 微服务双配说明、完整参数表、ACL 仅源/目的 IP、DHGROUP 不能 None、PSK 对称、IKEv2 默认、**完整 MML 脚本（Device A + Device B）** |
| EV-FK-08 | `调测IPsec功能_61317192.md` | **调测 8 步流程**、设备接口表、**DSP IKESA 完整输出样例**、DSP IKEIPSECSA、异常排查配置查询命令 |
| EV-FK-09 | `特性配置/激活IPsec功能（GRE over IPsec）_78985535.md` | GRE over IPSec 场景（IPSec 不支持组播广播的解决方案）、GRE Tunnel1 + IPSec Tunnel2 双隧道、SADURATION/EXCHANGEMODE/LOCALIDTYPE 参数 |
| EV-FK-10 | `特性配置/激活IPsec功能（IPv4 IPsec主备隧道）_88744738.md` | 主备隧道（WORKMODE=Master_standby + AUTOSWITCHBACK + 多 PEERPRIORITY 主备优先级） |
| EV-FK-11 | `特性配置/激活IPsec功能（多Sequence的IPsec策略）_78985536.md` + `（指定本端接口）_78985537.md` + `（OSPF over IPsec）_90949389.md` | 多 Sequence（单隧多 Peer 节省接口）、指定本端接口（LoopBack 作 IKE 源，独占约束）、OSPF over IPSec（保护动态路由） |
| EV-FK-12 | `特性配置/激活国密IPsec支持IKEv1功能（普通IPv4）_03728909.md` 等 5 篇国密变体 + `上传IPsec证书_83878778.md` + `上传国密IPsec证书_53966806.md` | 国密 SM2/SM3/SM4 合规变体（IPv4/IPv6/多 Seq/指定接口/GRE over IPSec 5 场景）+ RSA 证书与国密证书上传 |
