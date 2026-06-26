# IPFD-015004 IPSec功能 知识文档

> 聚焦 APN 业务域接入方式场景的 IPSec（Internet Protocol Security）隧道特性
> UDG（U 面/UPF 侧）独立部署；与 IPFD-016000（UNC/SMF 侧 IPSec）构成 C-U 对称的 IPSec 方案矩阵
> 与 GRE（IPFD-015002 / 016000 GRE over IPSec）、L2TP（GWFD-020412 / WSFD-104410）共同构成 APN 域隧道方案
> 适用 NF：SGW-U/PGW-U/UPF（UDG）；UNC 侧对应 IPFD-016000 适用 SGW-C/PGW-C/SMF
> C-U 对称：两侧特性概述/AH-ESP/IKE/SA/封装模式文档完全同构（文件 hash 一致），激活脚本命令族对称

---

## 0. 元数据（三层图谱 Schema 字段）

| 字段 | 取值 |
|------|------|
| feature_id | IPFD-015004 |
| feature_name | IPSec功能 |
| feature_group | 接入方式 |
| parent_feature_id | （配置树未明确父节点；接入方式类） |
| applicable_nf_map | `{"UDG": ["SGW-U", "PGW-U", "UPF"]}` |
| variant_dimensions | ["安全协议(AH / ESP / AH+ESP)", "封装模式(Tunnel)", "IKE版本(IKEv1 / IKEv2，缺省 IKEv2)", "IKEv1阶段1模式(主模式 Main / 野蛮模式 Aggressive)", "认证方法(PSK 预共享密钥 / 证书)", "加密算法(AES-CBC-128/192/256 / AES-GCM-128/256 / SM4 / DES)", "认证算法(SHA-1 / SHA2-256/384/512 / SM3 / MD5)", "DH组(Dh_group19 等，不可为 None)", "SA创建方式(手工 / IKE自动协商)", "隧道地址族(IPv4 IPsec / IPv6 IPsec)", "组网模式(普通隧道 / GRE over IPsec / OSPF over IPsec / 主备隧道 / 多Sequence)", "可靠性(DPD periodic/on-demand + 主备 热备/冷备)", "NAT穿越(TRUE/FALSE，仅 ESP 隧道模式)", "国密支持(IKEv1国密 / 国密证书)"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-01, EV-FK-02, EV-FK-03, EV-FK-04, EV-FK-05, EV-FK-06, EV-FK-07, EV-FK-08, EV-FK-09, EV-FK-10, EV-FK-11] |
| license_required | **无需 License**（UDG/UNC 两侧产品文档均明确"本特性无需获得 License 许可"） |

---

## 1. 概述

### 1.1 特性定义（是什么）

IPsec（Internet Protocol Security）是由 IETF（Internet Engineering Task Force）制定的一个开放的 IP 层安全框架协议，包含一系列为 IP 网络提供完整安全性的协议和服务。IPsec 使能通信双方在 IP 层执行数据加密、数据完整性保护，保证端对端通信数据的私密性、完整性、真实性和防重放攻击。

本特性是 **UDG（SGW-U/PGW-U/UPF）用户面侧的 IP 层加密隧道特性**：通过两个安全协议（AH 认证头、ESP 封装安全载荷）和一个密钥交换协议（IKE）实现报文加解密、身份认证、密钥自动协商。**IPSec 同时提供加密（ESP）和认证（AH/ESP）**，弥补了 GRE（IPFD-015002）"轻量封装不加密"的缺陷，是 APN 隧道方案矩阵中安全等级最高的方案。

> 来源：`IPFD-015004 IPSec功能特性概述_61317289.md`（"定义"章节）[EV-FK-01]

### 1.2 适用 NF（UDG/UNC 网元）

| 涉及 NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| SGW-U / PGW-U / UPF | 用户面（UDG） | UDG 20.5.1 及后续版本 | 用户面建立 IPsec 隧道，加密/解密用户面报文，穿越公网时保证私密性、完整性、真实性和防重放 |
| SGW-C / PGW-C / SMF | 控制面（UNC，对应 IPFD-016000） | UNC 20.6.0 及后续版本 | 控制面对称建立 IPsec 隧道，用于 C 面网管/信令通道加密（如到 AAA Server、网管 NMS 的安全通道） |

> 来源：`IPFD-015004 IPSec功能特性概述_61317289.md`（"可获得性/版本支持"章节，UDG 20.5.1+）、`IPFD-016000 IPSec功能特性概述_61317289.md`（UNC 20.6.0+，**两文件 hash 完全相同 61317289，证明 C-U 对称同构**）[EV-FK-01, EV-FK-11]

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|---------|---------|---------|
| 01 | UDG 20.5.0 | 首次发布 |
| 02 | UDG 20.8.0 | 第二次发布，支持 IPv6 IPsec、IPsec NAT 穿越以及 IPsec 主备隧道功能 |

> 来源：`IPFD-015004 IPSec功能特性概述_61317289.md`（"发布历史"章节）[EV-FK-01]

### 1.4 License

**本特性无需 License 许可**。产品文档明确声明"本特性无需获得 License 许可即可获得该特性的服务"。UDG 与 UNC（IPFD-016000）两侧均无 License 控制项。

> 来源：`IPFD-015004 IPSec功能特性概述_61317289.md`（"可获得性/License 支持"章节）[EV-FK-01]

### 1.5 前置条件与依赖

| 前置条件 | 说明 |
|---------|------|
| 接口 IP 已配置 | 操作人员已登录网管，配置接口的 IP 地址 |
| 路由可达 | 隧道两端路由可达（IKE 协商前提） |
| **IPSec 服务安装** | IPSec 功能由 IPSec 服务承载，需完成 IPSec 安装（参见"软件安装 > 安装可选服务 > 安装 IPSec 服务"） |
| **VNRS 与 IPsec 微服务双配原则** | IPsec 协商用到的隧道接口、隧道接口 IP、隧道类型、VPN 以及指定本端接口建立 IPsec 隧道的接口，需在 VNRS 微服务和 IPsec 微服务上一对一配置；否则业务不通 |
| VPN 实例（可选） | 若采用 VPN 组网，需先创建 VPN 实例 |
| LoopBack 接口（GRE over IPsec 场景） | GRE 本端源接口需先创建 |

> 来源：`激活IPsec功能（普通IPv4 IPsec隧道）_01_10002.md`（"必备事项/前提条件" + "操作流程"双配说明）、`激活IPsec功能（GRE over IPsec）_01_10006.md` [EV-FK-06, EV-FK-07]

### 1.6 与其他特性的交互

| 交互类型 | 相关特性 | 交互说明 |
|---------|---------|---------|
| **组合（GRE over IPSec，★重点）** | IPFD-015002 GRE（UDG）/ IPFD-016000 GRE（UNC） | IPsec 只支持 IP 报文传输，不支持组播/广播；GRE over IPSec 先用 GRE 封装组播/广播报文，再引入 IPsec 隧道加解密，弥补双方缺陷。UDG/UNC 两侧均有独立激活脚本 |
| **源地址互斥（★重点）** | IPFD-015002 GRE | **GRE 隧道的源地址不能与 IPSec 隧道的源地址相同**（见 GRE 特性概述"应用限制"硬约束） |
| **协同（OSPF over IPSec）** | IPFD-014001 支持 OSPF | OSPF 报文（组播）通过 IPsec 加密传输，需先经 GRE 封装或直接 IPsec 引流 |
| **对称（C-U 同构）** | IPFD-016000 IPSec（UNC） | UDG 侧 IPFD-015004 与 UNC 侧 IPFD-016000 特性概述/原理文档完全同构（hash 61317289/62244157/62256396/62244156/62256279/62244160/78460643 一致），两侧命令族对称（UNC 命令路径在 IPSEC 功能管理下同构） |
| **隧道方案矩阵** | GWFD-020412/WSFD-104410 L2TP、GWFD-020411/WSFD-104411 MPLS VPN | IPSec（加密三层隧道）与 L2TP（二层 PPP 隧道）、MPLS VPN（标签隧道）并列可选 |

> 说明：IPFD-015004 特性概述原文声明"本特性不涉及与其他特性的交互"，但 GRE（IPFD-015002）特性概述和 IPSec 激活脚本明确存在 GRE over IPSec 组合场景 + 源地址互斥约束，**以 GRE 文档与激活脚本为准**。

> 来源：`IPFD-015004 IPSec功能特性概述_61317289.md`（"与其他特性的交互"章节原文"不涉及"）、`IPFD-015002 GRE特性概述_61317365.md`（"应用限制"源地址互斥 + "GRE over IPSec"场景）、`激活IPsec功能（GRE over IPsec）_01_10006.md`（组合场景激活脚本）[EV-FK-01, EV-FK-11]

### 1.7 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | IPsec 保护用户数据的私密性、完整性和真实性，同时防御重放攻击、中间人攻击等，提升业务安全性 |
| 用户 | 用户不感知该特性 |

> 来源：`IPFD-015004 IPSec功能特性概述_61317289.md`（"客户价值"章节）[EV-FK-01]

### 1.8 应用场景

- **公网安全传输**：公共网络中协议报文面临被篡改、窃取和重复发送的风险，开启 IPsec 保证端对端通信数据的私密性、完整性、真实性和防重放
- **网关对网关加密隧道**：网络 A 与网络 B 通过 Device A/B 建立 IPsec 隧道，实现 PCA/PCB 安全互访（普通 IPv4/IPv6 IPsec 场景）
- **GRE over IPSec**：组播/广播报文经 GRE 封装后引入 IPsec 加密，解决 IPsec 不支持组播/广播的问题
- **OSPF over IPSec**：OSPF 协议报文通过 IPsec 加密传输
- **主备隧道**：一主一备（热备）或一主两备（冷备），主用不可用时切换到备用
- **多 Sequence IPsec 策略**：一条策略下多个序列号，匹配不同 ACL 数据流
- **指定本端接口建立 IPsec 隧道**：不使用默认隧道接口，指定其他接口作为 IKE 协商 IP
- **NAT 穿越场景**：两端之间存在 NAT 设备时，部署 NAT 穿越（仅 ESP 隧道模式）
- **国密 IPSec**：支持 IKEv1 国密算法（SM3/SM4）+ 国密证书

> 来源：`IPFD-015004 IPSec功能特性概述_61317289.md`（"应用场景"）、9 种激活脚本（普通IPv4/普通IPv6/IPv4主备/IPv6主备/GRE over IPsec/OSPF over IPsec/多Sequence/指定本端接口 + 国密 IKEv1 系列）[EV-FK-01, EV-FK-06..09]

### 1.9 对系统的影响

该特性对用户报文会进行封装处理，**对性能有一定影响**（加密/解密/认证运算开销），详细性能影响请联系华为技术支持获取。

> 来源：`IPFD-015004 IPSec功能特性概述_61317289.md`（"对系统的影响"章节）[EV-FK-01]

### 1.10 应用限制

IPSEC 目前**不支持**以下场景：

- GREv6 over IPSecv6
- OSPFv3 over IPSecv6
- IPSecv6 地址借用
- IPV4 报文入 IPSecv6 隧道
- IPV6 报文入 IPSecv4 隧道

> 补充约束（来自 GRE 文档与激活脚本）：
> - **GRE 源地址与 IPSec 源地址互斥**（GRE 文档硬约束）
> - **NAT 穿越仅支持 ESP 隧道模式**，不支持 IPv6 组网
> - **DH 组不能配置为 None 或不配置**，建议 Dh_group19
> - **PSK 认证必须配置预共享密钥**，否则 SA 建立不成功；密钥需与对端相同
> - **IKE 对等体远程地址不能配置为地址段**
> - **ACL 只支持源 IP 和目的 IP 配置**，端口配置不生效

> 来源：`IPFD-015004 IPSec功能特性概述_61317289.md`（"应用限制"章节）、`IPsec NAT穿越_62244160.md`（约束限制）、`激活IPsec功能（普通IPv4 IPsec隧道）_01_10002.md`（步骤说明）[EV-FK-01, EV-FK-05, EV-FK-06]

### 1.11 特性规格

**本特性无特殊规格**。但可靠性章节给出主备隧道规格：

| 可靠性特性 | 规格 |
|-----------|------|
| 主备隧道-热备 | 一主一备（主备自动协商 SA，立即切换） |
| 主备隧道-冷备 | 最多一主两备（备用默认不协商 SA，切换时再协商） |

> 来源：`IPFD-015004 IPSec功能特性概述_61317289.md`（"特性规格"章节）、`IPsec可靠性_78460643.md`（主备隧道规格表）[EV-FK-01, EV-FK-04]

### 1.12 计费与话单

**本特性不涉及计费与话单**。

> 来源：`IPFD-015004 IPSec功能特性概述_61317289.md`（"计费与话单"章节）[EV-FK-01]

### 1.13 遵循标准

| 标准类别 | 标准名称 |
|---------|---------|
| RFC 2401 | Security Architecture for the Internet Protocol |
| RFC 2402 | IP Authentication Header |
| RFC 2406 | IP Encapsulating Security Payload (ESP) |
| RFC 2403 | The Use of HMAC-MD5-96 within ESP and AH |
| RFC 4868 | Using HMAC-SHA-256, HMAC-SHA-384, and HMAC-SHA-512 with IPsec |
| RFC 4305 | Cryptographic Algorithm Implementation Requirements for ESP and AH |
| RFC 4314 | IMAP4 Access Control List (ACL) Extension |

> 来源：`IPFD-015004 IPSec功能特性概述_61317289.md`（"遵循标准"章节）[EV-FK-01]

---

## 2. 核心概念

### 2.1 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| IPsec | Internet Protocol Security | IETF 制定的 IP 层安全框架协议，提供加密、完整性、真实性和防重放 |
| AH | Authentication Header（IP 协议号 51） | IP 认证头协议，提供数据源认证、数据完整性校验、防重放攻击；**不加密**；认证强度高于 ESP（覆盖报头+载荷） |
| ESP | Encapsulating Security Payload（IP 协议号 50） | IP 封装安全载荷协议，提供数据源认证、完整性、防重放、**数据加密**；认证仅覆盖载荷（不含 IP 报头） |
| IKE | Internet Key Exchange | 密钥交换协议，动态创建 SA，提供自动协商密钥、建立和维护 SA 的服务；含 IKEv1/IKEv2，**UDG 缺省 IKEv2** |
| SA | Security Association，安全联盟 | IPsec 对等体间协商建立的约定，定义安全服务策略；**单向**，双向通信至少需要 2 个 IPsec SA（Outbound + Inbound） |
| IKE SA | - | 两对等体协商建立，约定 IKE 加密/验证/认证/PRF 算法和生存周期 |
| IPsec SA | - | 在 IKE SA 保护下协商；一个 IKE SA 下可协商多个 IPsec SA；由三元组（SPI、目的 IP、安全协议号）唯一标识 |
| SPI | Security Parameter Index，安全参数索引 | 32 bit，携带在 AH/ESP 报文头中；接收方据此查找 SA；IKE 协商时用随机数生成 |
| 主模式（Main Mode） | IKEv1 第一阶段模式 | 3 次交换 6 条消息建立 IKE SA；身份信息受 DH 密钥保护，安全性高 |
| 野蛮模式（Aggressive Mode） | IKEv1 第一阶段模式 | 3 条消息建立 IKE SA；身份信息不加密，安全性低；适用于远程访问、发起者地址动态场景 |
| 快速模式（Quick Mode） | IKEv1 第二阶段模式 | 3 条消息建立 IPsec SA |
| 隧道模式（Tunnel Mode） | 报文封装模式 | **UDG 仅支持隧道模式**；原始 IP 作为负载，增加新 IP 头 + AH/ESP 头，保护整个 IP 数据报文 |
| ACL | 访问控制列表 | 定义需要 IPsec 保护的数据流（仅支持源/目的 IP） |
| IPsec 安全提议 | Security Proposal | 定义封装模式、安全协议、认证和加密算法 |
| IKE 安全提议 | IKE Proposal | 定义认证方法、认证算法、加密算法、完整性算法、DH 组、SA 生存周期 |
| IKE 对等体 | IKE Peer | 配置对端名称、预共享密钥、远程地址、交换模式等 |
| IPsec 安全策略 | Security Policy | 决定对 IP 数据包提供何种保护；含 ACL、安全提议、IKE Peer |
| DPD | Dead Peer Detection，失效对等体检测 | 检测对端是否在线；periodic（周期）/on-demand（按需）两种模式 |
| NAT 穿越 | NAT Traversal | 两端之间存在 NAT 设备时部署；在 IP 头后增加 UDP 头用于 NAT 转换；**仅 ESP 隧道模式，不支持 IPv6** |
| DH | Diffie-Hellman | 公共密钥算法，不直接传输密钥，通过数据交换计算出共享密钥 |
| PFS | Perfect Forward Secrecy，完善的前向安全性 | 一个密钥被破解不影响其他密钥；由 DH 保障，在 IKE 阶段2 增加密钥交换实现 |
| VNRS 微服务 | - | **UDG 独有架构**：负责与外部网络通信，将需保护的流量引到 IPsec 微服务加解密，并转发加解密后的流量 |
| IPsec 微服务 | - | **UDG 独有架构**：负责 IKE 协商和加解密 |
| 双配原则 | - | **UDG 独有约束**：VNRS 和 IPsec 微服务的隧道接口/IP/类型/VPN 需一对一配置 |

> 来源：`相关术语_88277392.md`（8 个核心术语）、`AH和ESP_62244157.md`（协议号 51/50）、`IKE_62256396.md`（主模式/野蛮模式/快速模式/DH/PFS）、`安全联盟（SA）_62244156.md`（SA 单向性/三元组）、`IPsec NAT穿越_62244160.md`（NAT 穿越）、`IPsec可靠性_78460643.md`（DPD/主备）、`激活IPsec功能（普通IPv4 IPsec隧道）_01_10002.md`（VNRS/IPsec 微服务双配）[EV-FK-02..08]

### 2.2 对象模型

IPFD-015004 的配置架构基于 **"ACL 数据流 → 安全提议 → IKE 对等体 → 安全策略 → 隧道接口应用"** 五层对象模型，且 UDG 独有 **VNRS 微服务 + IPsec 微服务双配架构**：

```
┌──────────────────────────────────────────────────────────────────────────┐
│ UDG（用户面）配置对象层次（VNRS 微服务 + IPsec 微服务双配架构）              │
│                                                                          │
│  ┌────────────────────────────────────────────────────────┐              │
│  │ 第1层：基础网络（VNRS 微服务）                           │              │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │              │
│  │  │ L3VPN 实例   │  │ 物理接口     │  │ LoopBack 接口│ │              │
│  │  │ ADD L3VPNINST│  │ ADD IPBINDVPN│  │ ADD INTERFACE│ │              │
│  │  │ ADD VPNINSTAF│  │ ADD IFIPV4.. │  │ ADD IFIPV4.. │ │              │
│  │  └──────────────┘  └──────────────┘  └──────────────┘ │              │
│  └────────────────────────┬───────────────────────────────┘              │
│                           │                                              │
│  ┌────────────────────────▼───────────────────────────────┐              │
│  │ 第2层：IPsec 隧道接口（VNRS + IPsec 微服务双配★关键）   │              │
│  │  VNRS 微服务：ADD INTERFACE + ADD IPSECINTFCFG(TNLTYPE=IPSEC)          │
│  │              + ADD IPBINDVPN + ADD IFIPV4ADDRESS                       │
│  │  IPsec 微服务：ADD INTERFACEIPSEC + ADD IPBINDVPNIPSEC                 │
│  │                + ADD IFIPV4ADDRESSIPSEC                                │
│  │  （两微服务 Tunnel 接口名/IP/VPN 必须完全一致）                        │
│  └────────────────────────┬───────────────────────────────┘              │
│                           │                                              │
│  ┌────────────────────────▼───────────────────────────────┐              │
│  │ 第3层：安全数据流定义（IPsec 微服务）                    │              │
│  │  ┌──────────────┐    ┌──────────────────┐              │              │
│  │  │ ACL 规则组   │ →  │ 高级 ACL 规则    │              │              │
│  │  │ ADD ACLGROUP │    │ ADD ACLRULEADV4  │              │              │
│  │  │   IPSEC      │    │   IPSEC          │              │              │
│  │  └──────────────┘    └──────────────────┘              │              │
│  │  （仅支持源 IP + 目的 IP，端口配置不生效）               │              │
│  └────────────────────────┬───────────────────────────────┘              │
│                           │                                              │
│  ┌────────────────────────▼───────────────────────────────┐              │
│  │ 第4层：安全提议与 IKE 配置（IPsec 微服务）               │              │
│  │  ┌──────────────────┐  ┌──────────────────┐            │              │
│  │  │ IPsec 安全提议   │  │ IKE 安全提议     │            │              │
│  │  │ ADD IPSECPROPOSAL│  │ ADD IKEPROPOSAL  │            │              │
│  │  │   IPSEC          │  │ (认证方法/算法/  │            │              │
│  │  │ (协议/算法/模式) │  │  DH组/SA周期)    │            │              │
│  │  └──────────────────┘  └────────┬─────────┘            │              │
│  │                                 │                       │              │
│  │  ┌──────────────────────────────▼──────────────────┐   │              │
│  │  │ IKE 对等体                                       │   │              │
│  │  │ ADD IKEPEER (PEERNAME/PRESHAREDKEY/EXCHANGEMODE/ │   │              │
│  │  │             PROPOSAL/LOWREMOTEADDR/NATTRAVERSAL) │   │              │
│  │  └──────────────────────────────┬──────────────────┘   │              │
│  └─────────────────────────────────┼──────────────────────┘              │
│                                    │                                      │
│  ┌─────────────────────────────────▼──────────────────────┐              │
│  │ 第5层：IPsec 安全策略与应用（IPsec 微服务）              │              │
│  │  ┌──────────────┐ 引用 ┌──────────────┐ 绑定 ┌────────┐│              │
│  │  │ IPsec 策略   │──→  │ 策略绑定提议 │──→   │IKE Peer││              │
│  │  │ ADD IPSEC    │     │ ADD PROPATTACH│     │ADD ATT ││              │
│  │  │   POLICY     │     │   IPSECPROPOSAL│    │  IKEPEER││             │
│  │  └──────┬───────┘     └──────────────┘      └────────┘│              │
│  │         │ 应用到 Tunnel 接口                            │              │
│  │         ▼                                                │              │
│  │  ADD IPSECINTFCFGIPSEC(Tunnel, TNLTYPE=IPSEC, POLICY)  │              │
│  └─────────────────────────────────────────────────────────┘              │
│                                                                          │
│  可选全局配置：                                                          │
│  ┌──────────────────┐  ┌──────────────────┐                            │
│  │ DPD/NAT保活配置  │  │ 静态路由（引流） │                            │
│  │ SET IKEGLOBAL    │  │ ADD SRROUTE      │                            │
│  │   CONFIG         │  │                  │                            │
│  └──────────────────┘  └──────────────────┘                            │
└──────────────────────────────────────────────────────────────────────────┘
```

核心对象说明：

| 对象 | 命令 | 作用 | UDG 独有特性 |
|------|------|------|-------------|
| **IPsec 隧道接口（Tunnel）** | `ADD INTERFACE` + `ADD IPSECINTFCFG(IPSEC)` + `ADD IPBINDVPN` + `ADD IFIPV4ADDRESS` | IPsec 隧道虚拟接口 | **VNRS/IPsec 微服务双配** |
| **L3VPN 实例** | `ADD L3VPNINST` + `ADD VPNINSTAF` | VPN 实例（可选） | 双配 |
| **ACL 规则组 + 高级 ACL 规则** | `ADD ACLGROUPIPSEC` + `ADD ACLRULEADV4IPSEC` | 定义需保护的数据流（源/目的 IP） | 仅支持源/目的 IP |
| **IPsec 安全提议** | `ADD IPSECPROPOSALIPSEC` | 定义安全协议（AH/ESP）、认证算法、加密算法、封装模式 | - |
| **IKE 安全提议** | `ADD IKEPROPOSAL` | 定义认证方法（PSK）、认证算法、加密算法、完整性算法、DH 组、SA 生存周期 | DH 组不可为 None |
| **IKE 对等体** | `ADD IKEPEER` | 配置对端名称、预共享密钥、交换模式（主/野蛮）、远程地址、NAT 穿越 | - |
| **IPsec 安全策略** | `ADD IPSECPOLICY` | 关联 ACL、策略模式（Isakmp）、序列号 | - |
| **策略绑定提议** | `ADD PROPATTACHIPSECPROPOSAL` | 安全策略引用安全提议 | - |
| **绑定 IKE 对等体** | `ADD ATTACHIKEPEER` | 安全策略绑定 IKE Peer（含优先级，支持主备） | - |
| **IPsec 接口配置（应用策略）** | `ADD IPSECINTFCFGIPSEC` | 在 Tunnel 接口上应用安全策略 | - |
| **IKE 全局配置** | `SET IKEGLOBALCONFIG` | DPD 类型/间隔/重试、NAT 保活时间 | - |
| **静态路由** | `ADD SRROUTE` | 引导需保护流量进入 IPsec 隧道；GRE over IPSec 场景引导组播/广播流量 | - |
| **GRE 隧道对象**（GRE over IPSec 场景） | `ADD GRETUNNEL`（IPFD-015002 命令） | 先建立 GRE 隧道封装组播/广播，再引入 IPsec 加密 | - |

> 来源：`激活IPsec功能（普通IPv4 IPsec隧道）_01_10002.md`（操作步骤9步 + 数据表 + 任务示例脚本）、`激活IPsec功能（GRE over IPsec）_01_10006.md`（10步含 GRETUNNEL）[EV-FK-06, EV-FK-07]

### 2.3 在接入方式场景的角色

IPFD-015004 在 APN 接入方式场景中扮演**"安全加密三层隧道"**的角色，是隧道方案矩阵中安全等级最高的方案：

1. **加密 + 认证双重保障**：ESP 提供数据加密 + 完整性 + 防重放，AH 提供强认证（覆盖报头+载荷），弥补 GRE（不加密）和 L2TP（不加密）的缺陷
2. **自动密钥协商**：IKE 协议自动协商密钥、建立和维护 SA，简化 IPSec 使用和管理；支持 DH 算法保证密钥安全分发
3. **与 GRE 组合（GRE over IPSec）**：先 GRE 封装组播/广播，再 IPSec 加密，同时解决"IPSec 不支持组播"和"GRE 不加密"两个问题
4. **高可靠性**：DPD（失效对等体检测）+ 主备隧道（热备/冷备）保障业务连续性
5. **NAT 穿越能力**：公网部署 NAT 设备场景下仍可建立 IPSec 隧道（ESP 隧道模式 + UDP 封装）

> 来源：`IPFD-015004 IPSec功能特性概述_61317289.md`（"定义/原理概述"）、`IPsec可靠性_78460643.md`、`IPsec NAT穿越_62244160.md` [EV-FK-01, EV-FK-04, EV-FK-05]

---

## 3. 原理与流程

### 3.1 实现原理（IPsec 协议组成与工作流程）

IPsec 协议包括**两个安全协议**（AH、ESP）和**一个密钥交换协议**（IKE）：

```
┌─────────────────────────────────────────────────────────────────┐
│ IPsec 协议组成                                                   │
│                                                                 │
│   ┌─────────────────────────────────────────────────────┐       │
│   │ 密钥交换协议 IKE                                    │       │
│   │ - 提供密钥管理功能                                   │       │
│   │ - 定义身份认证、协商加密算法、生成共享会话密钥的方法  │       │
│   │ - 为 IPsec 提供自动协商交换密钥、建立和维护 SA 服务  │       │
│   │ - 协商结果保留在 SA 中，供 AH/ESP 使用              │       │
│   └─────────────────────────────────────────────────────┘       │
│                                                                 │
│   ┌─────────────────────┐  ┌─────────────────────────────┐     │
│   │ 安全处理协议 AH     │  │ 安全处理协议 ESP            │     │
│   │ (IP协议号51)        │  │ (IP协议号50)                │     │
│   │ - 数据源认证        │  │ - 数据源认证                │     │
│   │ - 数据完整性校验    │  │ - 数据完整性校验            │     │
│   │ - 防重放攻击        │  │ - 防重放攻击                │     │
│   │ ★不提供加密         │  │ ★提供数据加密              │     │
│   │ (认证强度高于ESP)   │  │ (认证仅覆盖载荷，不含IP头)  │     │
│   └─────────────────────┘  └─────────────────────────────┘     │
└─────────────────────────────────────────────────────────────────┘

IPsec 工作原理（业务流程）：
  数据流源端 + 目的端 ──事先协商好的约定(SA)──→ 加密/解密数据

  1. 发送方：使用 SA 中协商的算法和密钥对报文加 ESP/AH 头并加密
  2. 接收方：根据 SPI 查找 SA，先验证（认证），再解密
```

> 来源：`IPFD-015004 IPSec功能特性概述_61317289.md`（"实现原理"章节，图1 IPsec 协议、图2 工作原理、图3 业务流程）[EV-FK-01]

### 3.2 AH 与 ESP 详解（★重点：加密+认证机制）

#### 3.2.1 AH（Authentication Header）

- **IP 协议号 51**，提供数据源认证、数据完整性校验、防报文重放，**不能防止窃听（不加密）**，适合传输非机密数据
- **认证强度高于 ESP**：AH 对报头和有效载荷都进行认证

**AH 报文头字段**：

| 字段 | 长度 | 说明 |
|------|------|------|
| Next Header | 8 bit | 下一个负载类型（隧道模式下值=4 IPv4 / 41 IPv6 / 6 TCP） |
| Payload Length | 8 bit | AH 报文头长度 |
| Reserved | 16 bit | 保留，发送方设 0 |
| **SPI** | 32 bit | 接收方据此查找 SA 数据库；"0"表示无 SA |
| **Sequence Number** | 32 bit 单增 | 防重放保护；不允许重复 |
| Authentication Data | 可变长 | 完整性校验值 ICV；IPv4 为 32 bit 整数倍，IPv6 为 64 bit 整数倍 |

**认证过程**：
- 发送方：用协商算法和密钥对 IP 报文（可变字段除外）计算 ICV，填入 Authentication Data
- 接收方：用相同算法密钥重新计算，与报文中 ICV 比较；一致=未篡改，不一致=丢弃

**AH 支持的认证算法**：SHA-1（160bit）、SHA2-256（256bit）、SHA2-384（384bit）、SHA2-512（512bit）、SM3（256bit）、MD5（128bit）；**建议 SHA2**

> 来源：`AH和ESP_62244157.md`（"AH"章节：工作原理、报文头字段、认证过程、认证算法）[EV-FK-02]

#### 3.2.2 ESP（Encapsulating Security Payload）

- **IP 协议号 50**，提供数据源认证、数据完整性校验、防重放攻击、**数据加密**
- **加密 + 认证都选时**：发送方先加密后认证，接收方先认证后解密

**ESP 报文头字段**：

| 字段 | 长度 | 说明 |
|------|------|------|
| **SPI** | 32 bit | 接收方查找 SA；"0"=无 SA |
| **Sequence Number** | 32 bit 单增 | 防重放保护 |
| IV | 可变 | 初始化向量（某些加密算法需要）；对 IV 验证但不加密 |

**ESP 报尾字段**：

| 字段 | 长度 | 说明 |
|------|------|------|
| Padding | 0-255 字节 | 填充至加密算法要求长度；可隐藏有效载荷实际长度 |
| Padding Length | 8 bit | 接收方据此去除填充 |
| Next Header | 8 bit | 封装数据类型（隧道模式=4 IP-in-IP；6=TCP） |
| Authentication Data | 变长（可选） | 完整性校验值；**仅选择验证服务时存在** |

**ESP 认证范围**（与 AH 的关键差异）：完整性检查只包括 ESP 报文头、传输层协议报头、应用数据和 ESP 报尾，**不包括 IP 报头**，因此 ESP 不能保证 IP 报头不被篡改，安全性没有 AH 高。

**ESP 加密范围**：上层传输协议信息、数据和 ESP 报尾。

**ESP 支持的算法**：
- 认证算法：SHA-1、SHA2-256/384/512、SM3、MD5
- 加密算法：AES-CBC-128/192/256、AES-GCM-128/256（加密+认证）、SM4（128bit）、AES-GMAC-128（仅认证）、DES（64bit，已不安全）

> 来源：`AH和ESP_62244157.md`（"ESP"章节：工作原理、报文头/尾字段、认证加密范围、算法清单）、`相关术语_88277392.md` [EV-FK-02]

#### 3.2.3 AH 与 ESP 的差异与组合

| 维度 | AH | ESP |
|------|----|----|
| 功能 | **仅认证**，不加密 | **认证 + 加密** |
| 认证强度 | **强**（报头+载荷） | 弱（仅载荷，不含 IP 头） |
| IP 协议号 | 51 | 50 |
| 加密 | 不支持 | 支持（AES/SM4/DES） |

**组合使用**：AH 和 ESP 可单独使用，也可结合。组合时发送方**先 ESP 封装再 AH 封装**，接收方**先 AH 解封装再 ESP 解封装**。当同时采用 AH 和 ESP 时，必须采用**相同的报文封装模式**。

> 来源：`AH和ESP_62244157.md`（"AH与ESP的差异"章节）、`报文封装模式_62256279.md` [EV-FK-02, EV-FK-03]

### 3.3 IKE 协商机制（★重点：主模式/野蛮模式）

#### 3.3.1 IKE 安全机制

IKE 具有一套自保护机制，可以在不安全的网络上安全地分发密钥、验证身份、建立 IPsec SA：

- **DH（Diffie-Hellman）交换及密钥分发**：通信双方不直接传输密钥，通过数据交换计算出共享密钥；即使第三方截获所有交换数据，也不足以计算出真正的密钥
- **完善的前向安全性 PFS**：一个密钥被破解不影响其他密钥（由 DH 算法保障，在 IKE 阶段2 协商中增加密钥交换实现）
- **身份验证**：确认通信双方身份（pre-shared key 验证方法中，验证字作为产生密钥的输入）
- **身份保护**：身份数据在密钥产生之后加密传送

#### 3.3.2 IKEv1（★主模式/野蛮模式/快速模式）

IKEv1 协商分两个阶段：

**第一阶段交换**（建立 IKE SA）定义两种模式：

```
┌─────────────────────────────────────────────────────────────────┐
│ IKEv1 第一阶段：主模式（Main Mode）                              │
│                                                                 │
│   3 次交换，6 条消息建立 IKE SA                                  │
│   ┌──────┐        ┌──────┐                                      │
│   │发起者│──①──→│响应者│  协商保护套件                          │
│   │      │←─②──│      │                                        │
│   │      │──③──→│      │  DH 公共值 + nonce                     │
│   │      │←─④──│      │                                        │
│   │      │──⑤──→│      │  身份 + 认证（受 DH 密钥保护）         │
│   │      │←─⑥──│      │                                        │
│   └──────┘        └──────┘                                      │
│   特点：密钥交换信息与身份/认证信息分离；身份受 DH 共享密钥保护   │
│        安全性高；但消息开销大                                    │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ IKEv1 第一阶段：野蛮模式（Aggressive Mode，积极模式）           │
│                                                                 │
│   仅 3 条消息建立 IKE SA                                         │
│   ┌──────┐        ┌──────┐                                      │
│   │发起者│──①──→│响应者│  保护套件+DH公共值+nonce+身份         │
│   │      │←─②──│      │  选定套件+DH公共值+nonce+身份+认证     │
│   │      │──③──→│      │  认证载荷                             │
│   └──────┘        └──────┘                                      │
│   特点：第一条消息即携带身份信息，无法对身份加密保护，安全性低   │
│        协商能力低于主模式；但适用于：                             │
│        - 远程访问（响应者无法预先知道发起者地址）                │
│        - 发起者地址动态变化场景                                  │
│        - 已知响应者策略，需快速建立 IKE SA                       │
└─────────────────────────────────────────────────────────────────┘
```

**第二阶段交换**（建立 IPsec SA）：
- 只有一种模式：**快速模式（Quick Mode）**，通过 3 条消息交换建立 IPsec SA
- 发起者发送策略 → 响应者匹配并回应协商策略和 IPsec SA 参数 → 发起者第三条消息回应 IPsec SA 参数（因为 IPsec SA 是单向的）

#### 3.3.3 IKEv2（UDG 缺省）

IKEv2 定义三种交换：**初始交换**（至少 2 次共 4 条消息协商 IKE SA + 一对 IPsec SA）、**创建子 SA 交换**（每对 IPsec SA 增加 1 次交换即 2 条消息）、**通知交换**（传递控制信息）。

**IKEv1 与 IKEv2 差异**：

| 维度 | IKEv1 | IKEv2 |
|------|-------|-------|
| 协商效率 | 主模式 6 条 + 快速模式 3 条 | 一般 4 条完成 IKE SA + 一对 IPsec SA |
| 安全性 | 存在公认密码学安全漏洞 | 修复多处漏洞，支持 IKE SA 完整性算法 |
| 认证灵活性 | - | 加入 EAP 认证，支持 re-authentication |

> **说明**：为提升系统安全性，**UDG 默认使用 IKEv2**。IKEv1 存在安全风险，可通过 `MOD IKEPEER` 修改 VERSION1=FALSE 关闭。

> 来源：`IKE_62256396.md`（"安全机制 + IKEv1 主模式/野蛮模式/快速模式 + IKEv2 三种交换 + IKEv1 vs IKEv2 差异"完整说明）[EV-FK-03]

### 3.4 安全联盟（SA）机制（★重点）

#### 3.4.1 SA 定义与类型

**SA（Security Association，安全联盟）** 是 IPsec 对等体间经协商建立起来的一种约定，定义通信双方的安全服务策略，实现对不同数据流提供不同的安全保护。SA 约定内容包括：安全协议类型、IP 报文的封装模式、认证算法、加密算法、保护 IP 报文的密钥以及密钥的生存周期。

IPsec 框架定义两种 SA：

| SA 类型 | 说明 |
|---------|------|
| **IKE SA** | 两个 IKE 对等体协商建立的协定；约定加密/验证算法、认证方法、PRF 算法、IKE SA 生存周期 |
| **IPsec SA** | 在 IKE SA 保护下协商；**一个 IPsec 通道对应一个 IKE SA**，一个 IKE SA 下可协商出多个 IPsec SA；由三元组（**SPI + 目的 IP + 安全协议号**）唯一标识 |

#### 3.4.2 SA 创建方式

| 创建方式 | 特点 |
|---------|------|
| **手工创建** | 永不老化，除非手动删除，否则一直有效 |
| **IKE 自动协商** | 具有生存周期（基于时间 / 基于流量两种）；到期前 IKE 协商新 SA；新 SA 协商好前继续用旧 SA；可手动删除 |

#### 3.4.3 SA 特征（★关键：单向性）

- **SA 是单向的**：SA 是一个单向连接，通信对等体之间的双向通讯**最少需要 2 个 IPsec SA**（一个 Outbound SA 加密方向 + 一个 Inbound SA 解密方向）
- **SA 与协议相关**：每个安全协议各需要一个 SA。若主机 A 和 B 同时使用 AH+ESP，A 需要 4 个 SA（AH 入/出 + ESP 入/出），B 同样 4 个 SA

> 来源：`安全联盟（SA）_62244156.md`（定义/创建方式/特征完整说明）、`相关术语_88277392.md`（SA/SPI/SADB/SPDB 术语）[EV-FK-04, EV-FK-08]

### 3.5 报文封装模式（隧道模式）

UDG IPsec **仅支持隧道模式（Tunnel Mode）**：将原始 IP 数据作为负载，在原始报文外面增加新的 IP 报文头，并在新 IP 报文头和原始 IP 报文头之间插入 AH 或 ESP 协议头，**保护整个 IP 数据报文**。

```
隧道模式报文格式（从外到内）：
┌───────────┬──────────┬─────────────────┬──────────────┐
│ 新 IP 头  │ AH/ESP头 │ 原始 IP 头       │ 原始 Payload │
│ (源/目的  │ (含SPI/  │ (被保护的        │              │
│  公网IP)  │  Seq等)  │   内网IP)        │              │
└───────────┴──────────┴─────────────────┴──────────────┘
```

> 约束：当安全协议同时采用 AH 和 ESP 时，AH 和 ESP 协议**必须采用相同的报文封装模式**。

> 来源：`报文封装模式_62256279.md`（"隧道模式"章节）[EV-FK-03]

### 3.6 IPsec 可靠性机制

#### 3.6.1 DPD（失效对等体检测）

IKE 协议本身没有对等体状态检测机制，SA 生存周期到期前 SA 一直存在，对等体不可达会引发"黑洞"（数据流丢弃、CPU 资源浪费、无法激活备用对等体）。DPD 使用 IPsec 流量最小化检测消息数量。

| DPD 模式 | 定义 |
|---------|------|
| **periodic（周期性检测）** | 检测间隔内未收到对端流量，以检测间隔为周期循环发送 DPD 检测报文；期间收到响应=进入新周期，未收到=重传，重传结束仍无响应=删除 SA 表项重新建立隧道 |
| **on-demand（按需检测）** | 仅当本端有加密流量发送，且发送后 check-interval 时间内未收到对端流量时，才循环发送 DPD；**本端无加密流量时不发送 DPD 报文**（与轮询模式最大区别） |

#### 3.6.2 IPsec 主备隧道

| 工作模式 | 定义 | 规格 |
|---------|------|------|
| **热备** | 主备隧道自动协商 SA；主用不可用时立即切换到备用 | 一主一备 |
| **冷备** | 主用自动协商 SA，备用默认不协商；主用不可用时切换到备用协商 SA，协商完成后传输 | 最多一主两备（根据参数设置决定优先级） |

> 来源：`IPsec可靠性_78460643.md`（DPD 两种模式 + 主备隧道两种工作模式）[EV-FK-04]

### 3.7 IPsec NAT 穿越机制

由于 NAT 设备会改变源 IP 和源端口，对 IPsec 报文和 IKE 协商造成影响（IPsec 加密 TCP/UDP 校验和导致 NAT 无法更新）。

**实现原理**：对于要穿越 NAT 的报文，IPsec 在新 IP 报文头后**增加一个 UDP 协议头**，用于 NAT 设备的地址转换；同时对 NAT 进行探测，并增加保活消息避免 NAT 转换表超时。

**约束**：
- NAT 穿越**仅适用于 ESP 隧道模式**
- **不支持 IPv6 组网**

> 来源：`IPsec NAT穿越_62244160.md`（定义/实现原理/约束限制）[EV-FK-05]

### 3.8 UDG 微服务架构（VNRS + IPsec 双配，★UDG 独有）

IPsec 功能通过 **VNRS 微服务 + IPsec 微服务**实现：

```
┌─────────────────────────────────────────────────────────────────┐
│ UDG IPsec 微服务架构（双配原则）                                 │
│                                                                 │
│   ┌─────────────────────────┐    ┌─────────────────────────┐   │
│   │ VNRS 微服务             │    │ IPsec 微服务            │   │
│   │ - 与外部网络通信         │←→│ - IKE 协商              │   │
│   │ - 将需保护流量引到IPsec │    │ - 加解密                │   │
│   │ - 转发加解密后流量       │    │                         │   │
│   └─────────────────────────┘    └─────────────────────────┘   │
│                                                                 │
│   ★双配原则：隧道接口/IP/类型/VPN/指定本端接口必须一对一配置    │
│   明文引流表 + 密文引流表（VNRS 微服务内部）                    │
│                                                                 │
│   数据流向：                                                    │
│   待加密流量 → VNRS查路由(出接口=IPsec隧道) →                    │
│   查明文引流表 → 送IPsec微服务加密 → 返回VNRS → 转发出去        │
│                                                                 │
│   IKE协商报文/加密的AH/ESP报文到达 →                            │
│   VNRS查密文引流表 → 送IPsec微服务解密/协商 →                   │
│   返回VNRS → 转发出去                                           │
└─────────────────────────────────────────────────────────────────┘
```

> 来源：`激活IPsec功能（普通IPv4 IPsec隧道）_01_10002.md`（"操作流程"VNRS/IPsec 微服务说明 + 双配原则）[EV-FK-06]

### 3.9 协议交互

| 接口 | 交互网元 | 消息类型 | 说明 |
|------|---------|---------|------|
| IKE 协商（UDP 500/4500） | 本端 IPsec 对等体 ↔ 对端 IPsec 对等体 | IKEv1/v2 协商报文（主模式/野蛮模式/快速模式/初始交换） | 建立 IKE SA 和 IPsec SA |
| ESP 数据面（IP 协议号 50） | 本端 ↔ 对端 | ESP 加密报文（隧道模式） | 加密数据传输 |
| AH 数据面（IP 协议号 51） | 本端 ↔ 对端 | AH 认证报文 | 仅认证数据传输（不加密） |
| DPD 探测 | 本端 ↔ 对端 | DPD 检测报文 + 响应 | 对等体状态检测（periodic/on-demand） |
| NAT 保活 | 本端 ↔ NAT 设备 ↔ 对端 | NAT 保活消息 | 避免 NAT 转换表超时（默认 30s） |

> 来源：`AH和ESP_62244157.md`（协议号）、`IKE_62256396.md`、`IPsec可靠性_78460643.md`、`IPsec NAT穿越_62244160.md` [EV-FK-02..05]

### 3.10 与 GRE/L2TP 的隧道对比（★重点）

| 维度 | IPFD-015004 IPSec (UDG) | IPFD-015002 GRE | GWFD-020412 L2TP (UDG) |
|------|--------------------------|-----------------|------------------------|
| **隧道层级** | 三层（网络层加密） | 三层（网络层封装） | 二层（数据链路层，封装 PPP） |
| **加密** | **有**（ESP：AES-CBC/GCM、SM4、DES） | **无** | **无** |
| **认证** | 有（AH/ESP：SHA/SM3/MD5；IKE PSK/证书） | 无（可选 GRE Key 标识） | 有（内层 PPP 的 PAP/CHAP） |
| **认证强度** | AH > ESP（AH 覆盖报头+载荷） | - | - |
| **封装开销** | 重（ESP/AH 头 + 加密运算 + 新 IP 头） | 轻量（GRE 头 + 外层 IP 头） | 中（L2TP 头 + PPP 头） |
| **对系统性能影响** | **有**（加密解密运算开销） | **无** | 有（激活时延 + L2TP 封装） |
| **License** | **无需 License** | **无需 License** | UDG **必须 License**（82200BVC LKV3G5L2TP01），UNC 无 |
| **密钥协商** | **IKE 自动协商**（DH/PFS） | 无密钥协商（可选 Key） | PPP 协商（PAP/CHAP） |
| **C-U 模式** | **C-U 对称同构**（IPFD-015004/016000 文档 hash 一致） | **C-U 对称同构** | **C-U 分工**（C 决策下发 LNS 参数，U 作 LAC 封装） |
| **UDG 架构特性** | **VNRS + IPsec 微服务双配** | 无微服务拆分 | 无微服务拆分 |
| **组播/广播支持** | **不支持**（需 GRE over IPSec 解决） | 支持 | 支持（PPP 封装） |
| **典型用途** | 安全加密隧道、GRE over IPSec、NAT 穿越 | 异种网络互通、VPN 组建、多租户共享 | 企业远程接入、LNS 远程地址分配 |
| **互斥关系** | 与 GRE 源地址互斥 | 与 IPSec 源地址互斥 | 与地址自动检测、入不转板互斥 |
| **可靠性机制** | DPD（periodic/on-demand）+ 主备（热备/冷备） | Keepalive（周期 5s，重试 3 次） | Hello 报文（60s，3 次重发） |
| **NAT 穿越能力** | 有（ESP 隧道模式 + UDP） | 无 | 有（L2TP NAT 支持） |
| **标准** | RFC 2401/2402/2403/2406/4305/4868 | RFC 1701/1702/2784 | RFC 2661/2868/5072/5571/8064 |

> 来源：综合本特性 10+ 文档 + IPFD-015002 GRE 知识文档 + GWFD-020412 L2TP 特性描述 [EV-FK-01..10]

---

## 4. 配置规则

### 4.1 激活步骤（普通 IPv4 IPsec 隧道，9 步标准流程）

```
步骤1：创建 VNRS 微服务的 VPN 和 IPsec 隧道接口，配置静态路由
  a. 创建 VPN 实例：ADD L3VPNINST + ADD VPNINSTAF
  b. 绑定 VPN 网络接口：ADD IPBINDVPN + ADD IFIPV4ADDRESS
  c. 创建 IPsec 隧道接口：ADD INTERFACE + ADD IPSECINTFCFG(TNLTYPE=IPSEC)
     + ADD IPBINDVPN + ADD IFIPV4ADDRESS
  d. 配置静态路由：ADD SRROUTE

步骤2：创建 IPsec 微服务的 VPN 和 IPsec 隧道接口（★双配）
  a. 创建 VPN 实例：ADD L3VPNINSTIPSEC + ADD VPNINSTAFIPSEC
  b. 创建 IPsec 隧道接口：ADD INTERFACEIPSEC + ADD IPBINDVPNIPSEC
     + ADD IFIPV4ADDRESSIPSEC
  （接口名/IP/VPN 必须与 VNRS 微服务一致）

步骤3：定义需要保护的数据流
  └── ADD ACLGROUPIPSEC + ADD ACLRULEADV4IPSEC
      （仅支持源 IP + 目的 IP，端口配置不生效）

步骤4：配置 IPsec 安全提议
  └── ADD IPSECPROPOSALIPSEC
      （协议 AH/ESP、认证算法、加密算法、封装模式 Tunnel）

步骤5：配置 IKE 安全提议
  └── ADD IKEPROPOSAL
      （认证方法 PSK、认证算法、加密算法、完整性算法、DH 组、SA 生存周期）
      注：DHGROUP 不能为 None，建议 Dh_group19

步骤6：配置 IKE 对等体
  └── ADD IKEPEER
      （对端名称、预共享密钥、交换模式 Main/Aggressive、远程地址、
        NAT 穿越、本地 ID 类型、VPN 实例）
      注：PSK 认证必须配置预共享密钥，且与对端相同

步骤7：配置 IPsec 安全策略
  a. 增加策略：ADD IPSECPOLICY（策略名/序列号/模式 Isakmp/ACL 编号）
  b. 引用安全提议：ADD PROPATTACHIPSECPROPOSAL
  c. 绑定 IKE 对等体：ADD ATTACHIKEPEER（含优先级，支持主备）

步骤8：应用 IPsec 安全策略
  └── ADD IPSECINTFCFGIPSEC（Tunnel 接口 + TNLTYPE=IPSEC + 策略名）

步骤9：（可选）配置 DPD 功能
  └── SET IKEGLOBALCONFIG（DPD 类型/间隔/重试 + NAT 保活时间）
```

> 来源：`激活IPsec功能（普通IPv4 IPsec隧道）_01_10002.md`（"操作步骤"9 步 + "操作流程"双配说明）[EV-FK-06]

### 4.2 MML 命令清单

#### 4.2.1 基础网络命令（VNRS 微服务，10 条）

| 命令 | 用途 | 本特性角色 |
|------|------|-----------|
| **ADD L3VPNINST** | 增加 L3VPN 实例 | 创建 VPN 实例（VNRS 微服务） |
| **ADD VPNINSTAF** | 增加 VPN 实例地址族 | 配置 VPN 地址族 |
| **ADD INTERFACE** | 增加接口 | 创建物理接口/LoopBack/IPsec Tunnel 接口（VNRS 微服务） |
| **MOD INTERFACE** | 修改接口 | 配置接口管理状态、MTU |
| **ADD IPBINDVPN** | 增加接口绑定 VPN | 接口与 VPN 实例绑定（VNRS 微服务） |
| **ADD IFIPV4ADDRESS** | 增加接口 IPv4 地址 | 配置接口 IP（VNRS 微服务） |
| **ADD IPSECINTFCFG** | 创建 IPsec 隧道接口 | Tunnel 接口协议类型=IPSEC（VNRS 微服务侧） |
| **ADD SRROUTE** | 增加静态路由 | 引导流量进入 IPsec 隧道 |
| **ADD GRETUNNEL** | 增加 GRE 隧道 | **GRE over IPSec 场景**：先建 GRE 隧道封装组播/广播（IPFD-015002 命令） |

#### 4.2.2 IPsec 微服务命令（双配，5 条）

| 命令 | 用途 | 本特性角色 |
|------|------|-----------|
| **ADD L3VPNINSTIPSEC** | 增加 L3VPN 实例（IPsec 微服务） | 创建 VPN 实例（IPsec 微服务侧，与 VNRS 双配） |
| **ADD VPNINSTAFIPSEC** | 增加 VPN 实例地址族（IPsec 微服务） | 配置 VPN 地址族（双配） |
| **ADD INTERFACEIPSEC** | 增加接口（IPsec 微服务） | 创建 IPsec Tunnel 接口（双配） |
| **ADD IPBINDVPNIPSEC** | 增加接口绑定 VPN（IPsec 微服务） | 接口与 VPN 绑定（双配） |
| **ADD IFIPV4ADDRESSIPSEC** | 增加接口 IPv4 地址（IPsec 微服务） | 配置 Tunnel 接口 IP（双配） |

#### 4.2.3 ACL 数据流定义命令（2 条）

| 命令 | 用途 | 本特性角色 |
|------|------|-----------|
| **ADD ACLGROUPIPSEC** | 增加 ACL 规则组 | 定义需保护的数据流容器 |
| **ADD ACLRULEADV4IPSEC** | 增加高级 ACL 规则 | 定义源/目的 IP 匹配（仅支持源/目的 IP，端口不生效） |

#### 4.2.4 安全提议与 IKE 配置命令（3 条）

| 命令 | 用途 | 本特性角色 |
|------|------|-----------|
| **ADD IPSECPROPOSALIPSEC** | 增加 IPsec 提议 | 定义安全协议（AH/ESP）、认证算法、加密算法、封装模式（Tunnel） |
| **ADD IKEPROPOSAL** | 增加 IKE 提议 | 定义认证方法（PSK）、认证算法、加密算法、完整性算法、DH 组、SA 生存周期 |
| **ADD IKEPEER** | 增加 IKE 对等体 | 配置对端名称、预共享密钥、交换模式（Main/Aggressive）、远程地址、NAT 穿越、本地 ID |

#### 4.2.5 IPsec 安全策略与应用命令（4 条）

| 命令 | 用途 | 本特性角色 |
|------|------|-----------|
| **ADD IPSECPOLICY** | 增加 IPsec 策略 | 关联 ACL、策略模式（Isakmp）、序列号；支持多 Sequence |
| **ADD PROPATTACHIPSECPROPOSAL** | 增加 IPsec 策略绑定提议 | 安全策略引用安全提议 |
| **ADD ATTACHIKEPEER** | 增加绑定 IKE 对等体 | 安全策略绑定 IKE Peer（含优先级 PEERPRIORITY，支持主备） |
| **ADD IPSECINTFCFGIPSEC** | 增加 IPsec 隧道接口（IPsec 微服务） | 在 Tunnel 接口上应用安全策略 |

#### 4.2.6 全局配置与调测命令（3 条）

| 命令 | 用途 | 本特性角色 |
|------|------|-----------|
| **SET IKEGLOBALCONFIG** | 设置 IKE 全局配置 | DPD 类型/间隔/重试、NAT 保活时间（NATKLI） |
| **MOD IKEPEER** | 修改 IKE 对等体 | 关闭 IKEv1（VERSION1=FALSE）、调整交换模式等 |
| **PING** | IP Ping | 验证隧道两端连通性 |

#### 4.2.7 调测查询命令（8 条）

| 命令 | 用途 |
|------|------|
| **DSP IFSTATUS** | 查询接口物理/协议状态（含 Tunnel 接口 IPv4/IPv6 协议状态） |
| **LST IFIPV4ADDRESS** | 查询 VNRS 微服务接口 IPv4 地址（双配校验） |
| **LST IFIPV4ADDRESSIPSEC** | 查询 IPsec 微服务接口 IPv4 地址（双配校验） |
| **LST IPSECINTFCFGIPSEC** | 查询 IPsec 隧道接口配置（含绑定策略） |
| **DSP IKESA** | 显示 IKE 安全联盟（SA 标识、本端/远端地址、算法、DH 组、剩余 SA 长度、IKE 版本） |
| **DSP IKEIPSECSA** | 显示 IKE IPsec 安全联盟 |
| **LST IKEPEER / LST IKEPROPOSAL / LST IPSECPOLICY / LST PROPATTACHIPSECPROPOSAL / LST IPSECPROPOSALIPSEC** | 查询各类 IPsec/IKE 配置 |

> 来源：`激活IPsec功能（普通IPv4 IPsec隧道）_01_10002.md`（操作步骤9步命令）、`调测IPsec功能_61317192.md`（8 步调测查询命令）[EV-FK-06, EV-FK-10]

### 4.3 关键参数说明

#### 4.3.1 ADD IPSECPROPOSALIPSEC 关键参数

| 参数 | 取值 | 说明 |
|------|------|------|
| PROPOSALNAME | 字符串（如 "tran1"） | Proposal 名称（本端规划） |
| IPSECPROTOCOL | Ah / Esp | IPsec 安全协议；**ESP 提供加密+认证，AH 仅认证** |
| ESPAUTHALGO | Sha2_256 等 | ESP 认证算法（SHA-1/SHA2-256/384/512/SM3/MD5） |
| ESPENCRYPTALGO | Aes_256 等 | ESP 加密算法（AES-CBC-128/192/256/AES-GCM-128/256/SM4/DES） |
| ENCAPMODE | Tunnel | 封装模式，**UDG 仅支持隧道模式** |

#### 4.3.2 ADD IKEPROPOSAL 关键参数

| 参数 | 取值 | 说明 |
|------|------|------|
| PROPOSALNUMBER | 数字（1~100，101 系统默认） | 安全提议号（**仅本端记录，无实际含义，无需与对端一致**） |
| AUTHMETHOD | Pre_share | 认证方法（预共享密钥 PSK） |
| AUTHALGORITHM | Sha2_256 等 | 认证算法 |
| ENCRALGORITHM | Aes_cbc_256 等 | 加密算法 |
| INTEGALGORITHM | Hmac_sha2_256 等 | 完整性算法（IKEv2） |
| **DHGROUP** | Dh_group19 等 | DH 组，**不能为 None 或不配置，建议 Dh_group19** |
| SADURATION | 3600（秒） | SA 持续长度 |

#### 4.3.3 ADD IKEPEER 关键参数

| 参数 | 取值 | 说明 |
|------|------|------|
| PEERNAME | 字符串（如 "b"） | 对等体名称（本端规划，Device A 指向 b，Device B 指向 a） |
| **PRESHAREDKEY** | 字符串（如 "abcde"） | **预共享密钥，PSK 认证必须配置，且与对端相同** |
| EXCHANGEMODE | Main / Aggressive | 交换模式（IKEv1 第一阶段：主模式/野蛮模式） |
| PROPOSAL | 数字 | 引用的 IKE 安全提议号 |
| LOCALIDTYPE | Ip 等 | 本地 ID 类型 |
| LOWREMOTEADDR | IP 地址 | **远程地址（对端规划），不能配置为地址段** |
| NATTRAVERSAL | TRUE / FALSE | NAT 穿越（两端存在 NAT 设备时设 TRUE） |
| INVRFNAME | 字符串 | SA 绑定 VPN 名称 |
| OUTVRFNAME | 字符串 | 远程地址 VPN 名称 |
| VERSION1 | TRUE / FALSE | IKEv1 开关（UDG 缺省 IKEv2，关闭 IKEv1 时设 FALSE） |

#### 4.3.4 ADD IPSECPOLICY 关键参数

| 参数 | 取值 | 说明 |
|------|------|------|
| POLICYNAME | 字符串（如 "map1"） | 策略名称 |
| SEQUENCENUMBER | 数字（如 10） | 序列号（支持多 Sequence） |
| POLICYMODE | Isakmp | 策略模式（IKE 协商模式） |
| TEMPLATEMODE | None | 模板模式 |
| ACLNUMBER / ACLNAME | 数字/字符串 | ACL 编号（规则组为编号时）或 ACL 名称（规则组为名称时） |

#### 4.3.5 SET IKEGLOBALCONFIG 关键参数（DPD/NAT 保活）

| 参数 | 取值 | 说明 |
|------|------|------|
| DPDTYPE | Periodic / On_demand | DPD 模式（周期/按需） |
| DPDINTERVAL | 数字（秒，如 10） | DPD 检查间隔 |
| DPDRETRYINTRVL | 数字（秒，如 3） | DPD 重试间隔 |
| NATKLI | 数字（秒，如 30） | NAT 保活时间间隔（开启 NAT 穿越时生效） |

> 来源：`激活IPsec功能（普通IPv4 IPsec隧道）_01_10002.md`（"必备事项/数据"表 + 步骤说明 + PROPOSALNUMBER 说明）、`激活IPsec功能（GRE over IPsec）_01_10006.md`（SADURATION 参数）[EV-FK-06, EV-FK-07]

### 4.4 约束条件

| 约束类型 | 约束内容 | 来源 |
|---------|---------|------|
| **GRE 源地址互斥（★关键）** | GRE 隧道源地址不能与 IPSec 隧道源地址相同 | IPFD-015002 GRE 特性概述"应用限制" |
| **不支持场景** | GREv6 over IPSecv6、OSPFv3 over IPSecv6、IPSecv6 地址借用、IPV4 报文入 IPSecv6 隧道、IPV6 报文入 IPSecv4 隧道 | 特性概述"应用限制" |
| **NAT 穿越约束** | 仅适用于 ESP 隧道模式；不支持 IPv6 组网 | NAT 穿越文档"约束限制" |
| **DH 组约束** | DHGROUP 不能为 None 或不配置，建议 Dh_group19 | 激活文档步骤5 说明 |
| **PSK 必配约束** | PSK 认证方法必须配置预共享密钥，且与对端相同，否则 SA 建立不成功 | 激活文档步骤5/6 说明 |
| **远程地址约束** | IKE 对等体远程地址不能配置为地址段 | 激活文档步骤6 说明 |
| **ACL 约束** | ACL 只支持源 IP 和目的 IP 配置，端口配置不生效 | 激活文档步骤3 说明 |
| **双配原则（★UDG 关键）** | VNRS 微服务和 IPsec 微服务的隧道接口/IP/类型/VPN/指定本端接口必须一对一配置，否则业务不通 | 激活文档"操作流程"说明 |
| **IKE 版本缺省** | UDG 同时开启 IKEv1/v2，缺省 IKEv2；对端不支持 IKEv2 时禁用 IKEv2 用 IKEv1 | 激活文档步骤6 说明 |
| **AH+ESP 同模式** | 同时采用 AH 和 ESP 时，必须采用相同的报文封装模式 | 封装模式文档 |
| **对系统性能影响** | 该特性对报文进行封装处理，对性能有一定影响 | 特性概述"对系统的影响" |

---

## 5. 配置案例

### 5.1 典型场景：普通 IPv4 IPsec 隧道建立（ESP + IKEv2 + NAT 穿越 + DPD）

**场景描述**：网络 A（10.1.1.0/24）和网络 B（10.1.2.0/24）通过 Device A 和 Device B 网关对网关组网，建立 IPsec 隧道实现 PCA（10.1.1.2）与 PCB（10.1.2.2）安全互访。启用 ESP 协议（AES-256 加密 + SHA2-256 认证）、IKEv2（PSK 认证、DH group19）、NAT 穿越、DPD 周期检测。

**配置步骤和 MML 命令序列**（保留原始 MML）：

```
=== Device A 配置脚本 ===

// 创建 VNRS 微服务的 VPN 实例。
ADD L3VPNINST:VRFNAME="vrf1";
ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;

// 绑定 VNRS 微服务与 VPN 实例，并配置接口 IP 地址。
MOD INTERFACE:IFNAME="Ethernet66/0/5", IFADMINSTATUS=up;
MOD INTERFACE:IFNAME="Ethernet66/0/6", IFADMINSTATUS=up;
ADD IPBINDVPN:IFNAME="Ethernet66/0/5", VRFNAME="vrf1";
ADD IPBINDVPN:IFNAME="Ethernet66/0/6", VRFNAME="vrf1";
ADD IFIPV4ADDRESS:IFNAME="Ethernet66/0/5", IFIPADDR="10.1.1.1", SUBNETMASK="255.255.255.0";
ADD IFIPV4ADDRESS:IFNAME="Ethernet66/0/6", IFIPADDR="172.16.163.1", SUBNETMASK="255.255.255.0";

// 创建 VNRS 微服务的 IPsec 隧道接口，绑定 VPN 并配置 IP，隧道协议配置为 IPSEC。
ADD INTERFACE:IFNAME="Tunnel10", IFADMINSTATUS=up;
ADD IPSECINTFCFG:INTERFACENAME="Tunnel10",TNLTYPE=IPSEC;
ADD IPBINDVPN:IFNAME="Tunnel10", VRFNAME="vrf1";
ADD IFIPV4ADDRESS:IFNAME="Tunnel10", IFIPADDR="192.168.1.1", SUBNETMASK="255.255.255.255";

// 配置到达目的网络 B 的静态路由并绑定 VPN。
ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.2.0",MASKLENGTH=24,DESTVRFNAME="vrf1",NEXTHOP="192.168.1.2",IFNAME="Tunnel10";
ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="192.168.1.2",MASKLENGTH=32,DESTVRFNAME="vrf1",NEXTHOP="172.16.169.2",IFNAME="Invalid0";

// 创建 IPsec 微服务的 VPN 实例（★双配）。
ADD L3VPNINSTIPSEC:VRFNAME="vrf1";
ADD VPNINSTAFIPSEC:VRFNAME="vrf1", AFTYPE=Ipv4uni;

// 创建 IPsec 微服务的 IPsec 隧道接口（★双配）。
ADD INTERFACEIPSEC:IFNAME="Tunnel10", IFADMINSTATUS=Up;
ADD IPBINDVPNIPSEC:IFNAME="Tunnel10", VRFNAME="vrf1";
ADD IFIPV4ADDRESSIPSEC:IFNAME="Tunnel10", IFIPADDR="192.168.1.1", SUBNETMASK="255.255.255.255";

// 配置高级 ACL 3000，允许 PCA 访问 PCB。
ADD ACLGROUPIPSEC:ACLNAME ="3000";
ADD ACLRULEADV4IPSEC:ACLNAME="3000",ACLRULENAME="rule_1",ACLACTION=Permit,VRFNAME="vrf1",ACLPROTOCOL=0,ACLSOURCEIP="10.1.1.2",ACLSRCWILD="0.0.0.0",ACLDESTIP="10.1.2.2",ACLDESTWILD="0.0.0.0";

// 配置名称为 tran1 的 IPsec 安全提议（ESP + AES-256 + SHA2-256 + 隧道模式）。
ADD IPSECPROPOSALIPSEC:PROPOSALNAME="tran1",ESPAUTHALGO=Sha2_256,ESPENCRYPTALGO=Aes_256,IPSECPROTOCOL=Esp,ENCAPMODE=Tunnel;

// 配置序号为 10 的 IKE 安全提议（PSK + SHA2-256 + DH group19）。
ADD IKEPROPOSAL:PROPOSALNUMBER=10,AUTHMETHOD=Pre_share, AUTHALGORITHM=Sha2_256,DHGROUP=Dh_group19;

// 配置名称为 b 的 IKE peer（对端为 Device B，启用 NAT 穿越）。
ADD IKEPEER:PEERNAME="b",PRESHAREDKEY="abcde",NATTRAVERSAL=TRUE,PROPOSAL=10,LOWREMOTEADDR="192.168.1.2",INVRFNAME="vrf1",OUTVRFNAME="vrf1";

// 配置名称为 map1、序号为 10 的 IPsec 安全策略。
ADD IPSECPOLICY:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,ACLNUMBER=3000;

// 在安全策略中引用安全提议。
ADD PROPATTACHIPSECPROPOSAL:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,IPSECPROPNAME="tran1";

// 在安全策略中引用 IKE Peer。
ADD ATTACHIKEPEER:POLICYNAME="map1",SEQUENCENUMBER=10,POLICYMODE=Isakmp,TEMPLATEMODE=None,IKEPEERNAME="b",PEERPRIORITY=1;

// 在 IPsec 隧道接口上应用安全策略 map1。
ADD IPSECINTFCFGIPSEC:INTERFACENAME="Tunnel10",TNLTYPE=IPSEC,POLICYNAME="map1";

// 配置 DPD 功能（可选，周期检测 10s 间隔，重试 3s，NAT 保活 30s）。
SET IKEGLOBALCONFIG:DPDINTERVAL=10,DPDTYPE=Periodic,DPDRETRYINTRVL=3,NATKLI=30;
```

> Device B 配置脚本对称（PEERNAME="a"，LOWREMOTEADDR="192.168.1.1"，ACLSOURCEIP/ACLDESTIP 对调），完整脚本见来源文档。

> 来源：`激活IPsec功能（普通IPv4 IPsec隧道）_01_10002.md`（"任务示例/脚本"完整原文，Device A + Device B 对称）[EV-FK-06]

### 5.2 典型场景：GRE over IPSec（组播/广播加密传输）

**场景描述**：IPsec 不支持组播/广播报文，通过 GRE over IPSec 方案：先用 GRE（Tunnel1，LoopBack1 为源接口）封装组播/广播报文为 GRE 报文，再通过路由引入 IPsec 隧道（Tunnel2）加解密。

**关键差异**（相比普通 IPv4 场景）：
- 额外创建 GRE 本端源接口 LoopBack1（如 Device A: 10.102.105.238/32）
- 额外创建 GRE 隧道接口 Tunnel1（`ADD GRETUNNEL:TNLNAME="Tunnel1",SRCTYPE=if_name,DSTIPADDR="10.102.105.224",...,TNLTYPE=gre,SRCIFNAME="LoopBack1"`）
- IPsec 隧道接口为 Tunnel2（IKE 协商 IP + GRE 本端出接口）
- ACL 匹配 GRE 源/目的地址（LoopBack IP），而非用户主机 IP
- IKE 对等体指定 EXCHANGEMODE=Main（主模式）+ LOCALIDTYPE=Ip

```
=== Device A GRE over IPSec 关键脚本片段 ===

// 创建 GRE 本地源接口 LoopBack1。
ADD INTERFACE:IFNAME="LoopBack1";
MOD INTERFACE:IFNAME="LoopBack1",IFADMINSTATUS=up,IFMTU=1500,IFDF=FALSE,IFSTATIENABLE=TRUE;
ADD IPBINDVPN:IFNAME="LoopBack1", VRFNAME="vrf1";
ADD IFIPV4ADDRESS:IFNAME="LoopBack1",IFIPADDR="10.102.105.238",SUBNETMASK="255.255.255.255",ADDRTYPE=main;

// 创建 GRE 隧道接口 Tunnel1（封装组播/广播）。
ADD INTERFACE:IFNAME="Tunnel1",IFADMINSTATUS=up,IFMTU=1500,IFDF=FALSE;
ADD IPBINDVPN:IFNAME="Tunnel1", VRFNAME="vrf1";
ADD GRETUNNEL:TNLNAME="Tunnel1",SRCTYPE=if_name,DSTIPADDR="10.102.105.224",KEEPALVEN=FALSE,TNLTYPE=gre,SRCIFNAME="LoopBack1",GREKEYEN=FALSE,CHECKSUMEN=FALSE,STATENABLE=FALSE;
ADD IFIPV4ADDRESS:IFNAME="Tunnel1",IFIPADDR="192.168.3.1",SUBNETMASK="255.255.255.0",ADDRTYPE=main;

// 创建 IPsec 隧道接口 Tunnel2（IKE 协商 + GRE 本端出接口）。
ADD INTERFACE:IFNAME="Tunnel2",IFADMINSTATUS=up,IFMTU=1500,IFDF=FALSE;
ADD IPBINDVPN:IFNAME="Tunnel2", VRFNAME="vrf1";
ADD IPSECINTFCFG:INTERFACENAME="Tunnel2",TNLTYPE=IPSEC;
ADD IFIPV4ADDRESS:IFNAME="Tunnel2",IFIPADDR="10.102.101.25",SUBNETMASK="255.255.255.255",ADDRTYPE=main;

// ACL 匹配 GRE 源/目的地址（LoopBack IP）。
ADD ACLRULEADV4IPSEC:ACLNAME="3001",ACLRULENAME="rule_1",ACLRULEID=1,ACLACTION=Permit,VRFNAME="vrf1",ACLSOURCEIP="10.102.105.238",ACLSRCWILD="0.0.0.0",ACLPROTOCOL=0,ACLDESTIP="10.102.105.224",ACLDESTWILD="0.0.0.0";

// IKE 安全提议（含 SA 持续长度 3600s + 完整性算法）。
ADD IKEPROPOSAL:PROPOSALNUMBER=1,AUTHMETHOD=Pre_share,AUTHALGORITHM=Sha2_256,ENCRALGORITHM=Aes_cbc_256,INTEGALGORITHM=Hmac_sha2_256,DHGROUP=Dh_group19,SADURATION=3600;

// IKE 对等体（主模式 + IP 本地 ID 类型）。
ADD IKEPEER:PEERNAME="b",PRESHAREDKEY="abcde",EXCHANGEMODE=Main,PROPOSAL=1,LOCALIDTYPE=Ip,LOWREMOTEADDR="10.102.101.21",INVRFNAME="vrf1",OUTVRFNAME="vrf1";

// 静态路由：GRE 流量引入 IPsec 隧道。
ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.102.105.224",MASKLENGTH=32,IFNAME="Tunnel2",NEXTHOP="10.102.101.21",PREFERENCE=60,BFDENABLE=FALSE;
ADD SRROUTE:VRFNAME="vrf1",AFTYPE=ipv4unicast,PREFIX="10.1.2.0",MASKLENGTH=24,IFNAME="Tunnel1",NEXTHOP="192.168.4.1",PREFERENCE=60,BFDENABLE=FALSE;
```

> 来源：`激活IPsec功能（GRE over IPsec）_01_10006.md`（"任务示例/脚本"完整原文，Device A + Device B 对称）[EV-FK-07]

### 5.3 场景变体（9 种激活脚本覆盖）

| 变体 | 场景说明 | 核心差异 | 激活脚本文件 |
|------|---------|---------|-------------|
| 普通 IPv4 IPsec 隧道 | 网关对网关 IPv4 加密 | ESP+IKEv2+ACL 源/目的 IP | `激活IPsec功能（普通IPv4 IPsec隧道）_01_10002.md` |
| 普通 IPv6 IPsec 隧道 | IPv6 场景加密 | IPv6 地址族 | `激活IPsec功能（普通IPv6 IPsec隧道）_01_10003.md` |
| IPv4 IPsec 主备隧道 | 高可靠性（热备/冷备） | 多 IKE Peer + PEERPRIORITY 优先级 | `激活IPsec功能（IPv4 IPsec主备隧道）_01_10004.md` |
| IPv6 IPsec 主备隧道 | IPv6 高可靠性 | IPv6 + 主备 | `激活IPsec功能（IPv6 IPsec隧道主备方式）_01_10005.md` |
| **GRE over IPSec** | 组播/广播加密 | 先 GRE 封装再 IPsec 加密 | `激活IPsec功能（GRE over IPsec）_01_10006.md` |
| OSPF over IPSec | OSPF 协议报文加密 | OSPF 引流到 IPsec | `激活IPsec功能（OSPF over IPsec）_01_10007.md` |
| 多 Sequence IPsec 策略 | 多数据流差异化保护 | 同策略名多序列号 + 多 ACL | `激活IPsec功能（多Sequence的IPsec策略）_01_10008.md` |
| 指定本端接口建立隧道 | 灵活 IKE 协商 IP | 指定非 Tunnel 接口为 IKE 协商 IP | `激活IPsec功能（指定本端接口建立IPsec隧道）_01_10009.md` |
| 国密 IPSec（IKEv1） | 国密算法场景 | SM3/SM4 + 国密证书 + IKEv1 | 5 个 `激活国密IPsec支持IKEv1功能（...）_*.md` 脚本 |

> 来源：9 类激活脚本（普通IPv4/普通IPv6/IPv4主备/IPv6主备/GRE over IPsec/OSPF over IPsec/多Sequence/指定本端接口 + 5 个国密 IKEv1 脚本）[EV-FK-06..09]

---

## 6. 验证与调测

### 6.1 验证方法

#### 6.1.1 调测前提

IPsec 功能调测用于检查采用 IKE 方式建立 IPsec 隧道的各项配置是否正确，以保证 IKE 自动协商可以正常创建和维护安全联盟，使 IPsec 功能正常运行。以普通 IPv4 IPsec 隧道场景为例。

#### 6.1.2 调测执行步骤（8 步）

```
步骤1：检查本端和对端连通性
  └── PING: IPVERSION=IPv4, DESTIPV4ADDRESS="172.16.169.1"
      预期：收到对端响应（0% 丢包）→ 步骤2
      异常：无响应 → 参见"Ping不通定位思路"

步骤2：检查本端 IPsec 隧道接口状态
  └── DSP IFSTATUS: IFNAME="Tunnel10"
      预期：接口物理状态 + 协议状态都是 Up → 步骤5
      异常：非 Up → 步骤3

步骤3：检查 VNRS 和 IPsec 微服务隧道接口 IP 是否一致（★双配校验）
  ├── LST IFIPV4ADDRESS: IFNAME="Tunnel10"        (VNRS 微服务)
  └── LST IFIPV4ADDRESSIPSEC: IFNAME="Tunnel10"   (IPsec 微服务)
      预期：两个微服务 IP 一致 → 步骤4
      异常：不一致 → 按规划修改

步骤4：检查 IPsec 隧道接口是否绑定 IPsec 策略
  └── LST IPSECINTFCFGIPSEC: INTERFACENAME="Tunnel10"
      预期：绑定策略符合规划（策略名称=map1）→ 步骤8
      异常：未绑定或错误 → 重新绑定

步骤5：检查本端和对端 IPsec 隧道接口连通性
  └── PING: IPVERSION=IPv4, DESTIPV4ADDRESS="192.168.1.2"
      预期：收到对端响应 → 步骤6
      异常：无响应 → 步骤8

步骤6：查询 IKE 安全联盟
  └── DSP IKESA:;
      预期：可查询到 IKE SA，SA 标识 ≠ NO STATE → 步骤7
      异常：未查询到或 SA 标识=NO STATE → 步骤8

步骤7：查询 IKE IPsec 安全联盟
  └── DSP IKEIPSECSA:;
      预期：可查询到 IKE IPsec SA → 调测结束
      异常：未查询到 → 可能 IPsec 安全提议配置错误 → 步骤8

步骤8：检查 IPsec 相关配置
  ├── LST IKEPEER            (查询 IKE 对等体)
  ├── LST IKEPROPOSAL        (查询 IKE 安全提议)
  ├── LST IPSECPOLICY        (查询 IPsec 策略)
  ├── LST PROPATTACHIPSECPROPOSAL  (查询策略绑定提议)
  └── LST IPSECPROPOSALIPSEC (查询 IPsec 安全提议)
      若与规划不一致，修改配置
```

#### 6.1.3 DSP IKESA 典型输出

```
                 地址类型  =  IPv4地址
                 远端地址  =  192.168.1.2
             远端地址IPV6  =  ::
                  POD名称  =  ipsecexec-pod-0172-16-1-189
                   连接ID  =  4
               SA标识  =  RD|ST
                   实例ID  =  0
                     阶段  =  1
                 本端地址  =  192.168.1.1
             本端地址IPV6  =  ::
             触发端Cookie  =  6b51edace1187e9
             回应端Cookie  =  8bc6f6612aacc1ec
                 接口名称  =  Tunnel10
                 认证方法  =  预共享
                 认证算法  =  sha2-256算法
                 加密算法  =  256位AES算法
               完整性算法  =  sha2-256算法
                     DH组  =  DH组14
               剩余SA长度  =  86295
               是否已备份  =  否
               SA建立时间  =  2021-01-08 15：08：25
            IKE对等体名称  =  1
                  IKE版本  =  版本2
            流VPN实例名称  =  _public_
        对等体VPN实例名称  =  _public_
             发送消息计数  =  2
             接收消息计数  =  2
```

> 来源：`调测IPsec功能_61317192.md`（8 步调测流程 + PING/DSP IFSTATUS/LST IFIPV4ADDRESS/DSP IKESA/DSP IKEIPSECSA 输出样例）[EV-FK-10]

### 6.2 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| IPsec 隧道状态 DOWN | 对端不可达 / 路由问题 | PING 验证本端-对端连通性；检查静态路由 ADD SRROUTE |
| IPsec 隧道状态 DOWN | VNRS/IPsec 微服务双配不一致 | LST IFIPV4ADDRESS + LST IFIPV4ADDRESSIPSEC 校验 Tunnel 接口 IP 一致性 |
| IPsec 隧道状态 DOWN | GRE 源地址与 IPSec 源地址相同 | 核对 GRE 与 IPSec 源地址规划；修改使其不同 |
| SA 建立失败（DSP IKESA 无 SA 或 NO STATE） | PSK 密钥不匹配 | LST IKEPEER 核对 PRESHAREDKEY；两端必须相同 |
| SA 建立失败 | DH 组配置为 None 或未配置 | LST IKEPROPOSAL 核对 DHGROUP；建议 Dh_group19 |
| SA 建立失败 | IKE 版本不匹配 | 核对 IKEv1/IKEv2 支持；对端不支持 IKEv2 时禁用 |
| SA 建立失败 | 远程地址配置为地址段 | LST IKEPEER 核对 LOWREMOTEADDR；必须为具体 IP |
| 数据黑洞（隧道看似 UP 但报文丢弃） | DPD 未启用，对端实际不可达 | SET IKEGLOBALCONFIG 启用 DPD；检查 DPD 计数 |
| 数据流未进入 IPsec 隧道 | ACL 配置错误或包含端口 | LST ACLRULEADV4IPSEC；**ACL 仅支持源/目的 IP，端口不生效** |
| NAT 场景下隧道建立失败 | 未启用 NAT 穿越 | ADD IKEPEER NATTRAVERSAL=TRUE；SET IKEGLOBALCONFIG NATKLI=30 |
| NAT 穿越 IPv6 不工作 | NAT 穿越不支持 IPv6 组网 | 改用 IPv4 ESP 隧道模式 |
| 主备切换失败 | 主备配置错误或优先级问题 | LST IPSECPOLICY + LST ATTACHIKEPEER 核对 PEERPRIORITY；热备/冷备模式 |
| 性能下降明显 | IPsec 封装 + 加密运算开销 | 评估流量模型；优化 ACL 减少不必要加密；联系华为技术支持 |
| IKEv1 安全风险 | IKEv1 存在公认密码学漏洞 | MOD IKEPEER VERSION1=FALSE 关闭 IKEv1，使用 IKEv2 |
| 国密场景不生效 | 未上传国密证书或未使用国密算法 | 检查国密证书上传（`上传国密IPsec证书`）+ SM3/SM4 算法配置 |

> 来源：`调测IPsec功能_61317192.md`（调测步骤异常处理）、`IPsec可靠性_78460643.md`（DPD/主备）、`IKE_62256396.md`（IKEv1 安全风险）[EV-FK-03, EV-FK-04, EV-FK-10]

---

## 7. 参考信息

### 7.1 与其他特性的关系

| 关联特性 | 特性ID | 关系说明 |
|---------|--------|---------|
| **IPSec 功能（UNC）** | IPFD-016000 | **C-U 对称同构**：两侧特性概述/原理/术语文档 hash 完全一致（61317289/62244157/62256396/62244156/62256279/62244160/78460643/88277392），命令族对称；UDG 20.5.1+，UNC 20.6.0+ |
| **GRE（UDG）** | IPFD-015002 | **组合（GRE over IPSec）+ 源地址互斥**：IPSec 不支持组播/广播，GRE over IPSec 先 GRE 封装再 IPSec 加密；GRE 源地址不能与 IPSec 源地址相同 |
| **GRE（UNC）** | （UNC 侧 GRE） | 同上（UNC 侧对称） |
| L2TP VPN（UDG） | GWFD-020412 | **隧道方案矩阵**：IPSec 为三层加密隧道，L2TP 为二层 PPP 隧道（C-U 分工、UDG 必须 License） |
| L2TP VPN（UNC） | WSFD-104410 | 同上（UNC 侧 L2TP） |
| MPLS VPN（UDG/UNC） | GWFD-020411 / WSFD-104411 | **隧道方案矩阵**：IPSec 为加密 IP 隧道，MPLS VPN 为标签隧道 |
| 支持 OSPF | IPFD-014001（UDG/UNC 共用） | **协同（OSPF over IPSec）**：OSPF 协议报文通过 IPsec 加密传输 |
| Radius 功能（UNC） | WSFD-011306 | **应用场景协同**：UNC 到 AAA Server 安全通道可使用 IPSec 加密 |

### 7.2 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 产品 | 主要贡献内容 |
|------|---------|------|-------------|
| 1 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IP基本特性/IPFD-015004 IPSec功能/IPFD-015004 IPSec功能特性概述_61317289.md` | UDG | **★特性定义**（IPsec 开放 IP 层安全框架）、客户价值（私密性/完整性/真实性/防重放）、应用场景、可获得性（**UDG 20.5.1+，无需 License**）、与其他特性交互（原文"不涉及"，实际有 GRE over IPSec）、对系统影响（封装处理，性能有一定影响）、**应用限制（5 种不支持场景）**、实现原理（IPsec 协议组成：IKE+AH+ESP，工作原理，业务流程）、计费话单（无）、特性规格（无特殊）、**遵循标准（RFC 2401/2402/2403/2406/4305/4868/4314）**、发布历史（v01 UDG 20.5.0，v02 UDG 20.8.0 支持 IPv6/NAT 穿越/主备） |
| 2 | `output/UDG_.../IPFD-015004 IPSec功能/实现原理/AH和ESP_62244157.md` | UDG | **★AH/ESP 加密+认证机制**：AH（IP 协议号 51，认证不加密，强度高于 ESP，报文头字段 SPI/Seq/Auth Data，认证算法 SHA-1/SHA2-256/384/512/SM3/MD5）、ESP（IP 协议号 50，认证+加密，报文头 SPI/Seq/IV + 报尾 Padding/Next Header/Auth Data，加密算法 AES-CBC-128/192/256/AES-GCM-128/256/SM4/DES，认证范围仅载荷不含 IP 头）、**AH vs ESP 差异**（功能/认证强度）、AH+ESP 组合（先 ESP 后 AH） |
| 3 | `output/UDG_.../IPFD-015004 IPSec功能/实现原理/IKE_62256396.md` | UDG | **★IKE 协商机制**：安全机制（DH 交换、PFS 前向安全、身份验证、身份保护）、**IKEv1 两阶段**（第一阶段主模式 6 条消息/野蛮模式 3 条消息，第二阶段快速模式 3 条消息）、IKEv2 三种交换（初始交换 4 条消息/创建子 SA/通知交换）、**IKEv1 vs IKEv2 差异**（效率/安全/认证灵活性）、**UDG 缺省 IKEv2 说明**（MOD IKEPEER VERSION1=FALSE 关闭 IKEv1） |
| 4 | `output/UDG_.../IPFD-015004 IPSec功能/实现原理/安全联盟（SA）_62244156.md` | UDG | **★SA 机制**：定义（SA 约定安全服务策略）、两种 SA（IKE SA / IPsec SA，三元组 SPI+目的IP+协议号）、创建方式（手工永不老化 / IKE 自动协商有生存周期）、**特征（单向性：双向通信至少 2 个 SA；协议相关性：AH+ESP 需 4 个 SA）** |
| 5 | `output/UDG_.../IPFD-015004 IPSec功能/实现原理/IPsec NAT穿越_62244160.md` | UDG | **NAT 穿越机制**：定义（NAT 改变源 IP/端口影响 IPsec）、实现原理（新 IP 头后增加 UDP 协议头用于 NAT 转换 + NAT 探测 + 保活消息）、**约束限制（仅 ESP 隧道模式，不支持 IPv6 组网）** |
| 6 | `output/UDG_.../IPFD-015004 IPSec功能/特性配置/激活IPsec功能（普通IPv4 IPsec隧道）_01_10002.md` | UDG | **★激活完整流程（9 步）**：操作场景（网关对网关 IPv4）、数据表（30+ 参数覆盖 ACL/Proposal/IKE/Policy 命令族）、**VNRS+IPsec 微服务双配原则**、操作步骤（VNRS VPN+Tunnel → IPsec VPN+Tunnel → ACL → IPsec 提议 → IKE 提议 → IKE Peer → IPsec 策略 → 应用 → DPD）、**完整 MML 脚本（Device A + Device B 对称）**、DH 组约束/PSK 必配/远程地址约束/ACL 端口不生效说明 |
| 7 | `output/UDG_.../IPFD-015004 IPSec功能/特性配置/激活IPsec功能（GRE over IPsec）_01_10006.md` | UDG | **GRE over IPSec 激活（10 步）**：场景（IPsec 不支持组播/广播，GRE 封装后引入 IPsec 加密）、数据表（含 EXCHANGEMODE=Main/LOCALIDTYPE=Ip/SADURATION）、操作步骤（含 GRETUNNEL 创建 + LoopBack 源接口）、**完整 MML 脚本（Device A + Device B 对称，Tunnel1 GRE + Tunnel2 IPSec）** |
| 8 | `output/UDG_.../IPFD-015004 IPSec功能/相关术语_88277392.md` | UDG | **8 个核心术语**：对等体、安全联盟（SA）、安全参数索引（SPI）、安全提议（Security Proposal）、安全策略（Security Policy）、安全联盟生成时间（Life Time）、安全联盟数据库（SADB）、安全策略数据库（SPDB） |
| 9 | `output/UDG_.../IPFD-015004 IPSec功能/实现原理/报文封装模式_62256279.md` + `IPsec可靠性_78460643.md` + 其他激活脚本（普通IPv6/IPv4主备/IPv6主备/OSPF over IPSec/多Sequence/指定本端接口/国密IKEv1系列） | UDG | 封装模式（仅隧道模式，AH+ESP 须同模式）、可靠性（DPD periodic/on-demand + 主备热备/冷备规格）、9 种激活场景变体 |
| 10 | `output/UDG_.../IPFD-015004 IPSec功能/调测IPsec功能_61317192.md` | UDG | **8 步调测流程**：PING 连通性 → DSP IFSTATUS 接口状态 → LST IFIPV4ADDRESS/IPSEC 双配校验 → LST IPSECINTFCFGIPSEC 策略绑定 → PING 隧道连通性 → DSP IKESA → DSP IKEIPSECSA → 配置检查（5 条 LST 命令）、DSP IKESA 完整输出样例（SA 标识/算法/DH 组/IKE 版本） |
| 11 | `output/UNC 20.15.2.../IPFD-016000 IPSec功能/IPFD-016000 IPSec功能特性概述_61317289.md` | UNC | **C-U 对称验证**：UNC 侧 IPFD-016000 特性概述文件 **hash=61317289 与 UDG 侧 IPFD-015004 完全相同**，证明 C-U 两侧特性定义/原理/限制/标准完全同构；**UNC 20.6.0+ 支持**（与 UDG 20.5.1+ 存在版本差异） |

### 7.3 关键术语速查

| 术语 | 全称 | 说明 |
|------|------|------|
| IPsec | Internet Protocol Security | IP 层安全框架协议 |
| AH | Authentication Header | IP 认证头（协议号 51），仅认证不加密，强度高于 ESP |
| ESP | Encapsulating Security Payload | IP 封装安全载荷（协议号 50），认证+加密 |
| IKE | Internet Key Exchange | 密钥交换协议，自动协商 SA |
| SA | Security Association | 安全联盟，**单向**，双向通信至少 2 个 |
| SPI | Security Parameter Index | 32 bit，标识 SA，携带在 AH/ESP 报文头 |
| 主模式 | Main Mode | IKEv1 阶段 1，6 条消息，身份受保护 |
| 野蛮模式 | Aggressive Mode | IKEv1 阶段 1，3 条消息，身份不加密 |
| 快速模式 | Quick Mode | IKEv1 阶段 2，3 条消息建立 IPsec SA |
| 隧道模式 | Tunnel Mode | UDG 唯一支持的封装模式，保护整个 IP 报文 |
| DPD | Dead Peer Detection | 失效对等体检测，periodic/on-demand |
| NAT 穿越 | NAT Traversal | ESP 隧道模式 + UDP 头穿越 NAT |
| DH | Diffie-Hellman | 公共密钥算法，不直接传输密钥 |
| PFS | Perfect Forward Secrecy | 完善的前向安全性 |
| VNRS 微服务 | - | UDG 独有，负责外部通信和流量引流 |
| IPsec 微服务 | - | UDG 独有，负责 IKE 协商和加解密 |
| 双配原则 | - | UDG 独有，VNRS/IPsec 微服务隧道配置一对一 |

---

## 8. 文档一致性说明（配置树 vs 产品文档）

> 配置树仅用于定位特性 ID，以下记录以产品文档实际内容为准时发现的差异与协同点，供 Stage 3 横向分析参考。

### 8.1 与任务要求中提及对象的核对（★重点澄清）

| # | 任务要求提及 | 产品文档实际 | 核对结论 |
|---|-------------|-------------|---------|
| 1 | **IPSec ESP 加密+认证机制** | **确认**：ESP（协议号 50）提供数据源认证、完整性校验、防重放、**数据加密**；加密算法 AES-CBC-128/192/256/AES-GCM-128/256/SM4/DES，认证算法 SHA-1/SHA2-256/384/512/SM3/MD5；认证范围仅载荷不含 IP 头；加密+认证都选时先加密后认证，接收方先认证后解密 | 已覆盖（见 §3.2.2） |
| 2 | **IKE 协商（主模式/野蛮模式）** | **确认**：IKEv1 阶段 1 定义主模式（3 次交换 6 条消息，身份受 DH 保护）和野蛮模式（3 条消息，身份不加密，适用于远程访问/地址动态场景）；阶段 2 快速模式 3 条消息；IKEv2 初始交换 4 条消息；**UDG 缺省 IKEv2** | 已覆盖（见 §3.3） |
| 3 | **安全联盟（SA）** | **确认**：SA 是单向的约定，定义安全服务策略；IKE SA（一对等体协商）+ IPsec SA（IKE SA 保护下，三元组 SPI+目的IP+协议号）；双向通信至少 2 个 IPsec SA（Outbound+Inbound）；创建方式手工（永不老化）/IKE 自动协商（有生存周期） | 已覆盖（见 §3.4） |
| 4 | **与 IPFD-016000（UNC 侧 IPSec）的对称关系** | **★关键发现**：UDG IPFD-015004 与 UNC IPFD-016000 的**特性概述/原理/术语文档 hash 完全相同**（61317289/62244157/62256396/62244156/62256279/62244160/78460643/88277392），证明 C-U 两侧特性定义、AH/ESP 机制、IKE 协商、SA 机制、封装模式、NAT 穿越、可靠性、术语**完全同构**。唯一差异：UDG 20.5.1+ vs UNC 20.6.0+（版本不同）；激活脚本文件 hash 略有差异（UDG `_01_10002` vs UNC `_61317238`），但命令族对称 | **确认 C-U 对称同构**（与 GRE 的 C-U 对称一致，与 L2TP 的 C-U 分工形成对比） |
| 5 | **与 GRE（015002）组合（GRE over IPSec）** | **确认**：IPSec 只支持 IP 报文，不支持组播/广播；GRE over IPSec 先用 GRE 封装组播/广播为 GRE 报文，再引入 IPSec 隧道加解密。UDG/UNC 两侧均有独立激活脚本（`激活IPsec功能（GRE over IPsec）`），GRE 隧道用 Tunnel1，IPSec 隧道用 Tunnel2，ACL 匹配 GRE 源/目的地址（LoopBack IP） | 已覆盖（见 §1.6、§5.2） |
| 6 | **IPSec 配置对象与命令（文档依据）** | **确认**：核心配置对象层次为 ACL→IPsec/IKE 提议→IKE 对等体→IPsec 策略→隧道接口应用；**UDG 独有 VNRS+IPsec 微服务双配架构**（VNRS 命令族 + IPSEC 命令族对称）；共 30+ 条 MML 命令覆盖基础网络(8)/双配(5)/ACL(2)/提议与 IKE(3)/策略与应用(4)/全局(2)/调测查询(8) | 已覆盖（见 §4.2） |
| 7 | **源地址互斥约束** | **★关键澄清**：IPFD-015004 特性概述原文声明"本特性不涉及与其他特性的交互"，**但 IPFD-015002 GRE 特性概述"应用限制"章节明确"GRE 隧道的源地址不能与 IPSec 隧道的源地址相同"**。以 GRE 文档为准，源地址互斥约束成立（GRE 侧硬约束，IPSec 侧未声明但对称生效） | **澄清**：源地址互斥来自 GRE 文档，IPSec 特性概述未声明但实际生效 |

### 8.2 与配置树/文档清单的差异

| # | 维度 | 配置树/文档清单描述 | 产品文档实际内容 | 差异类型 |
|---|------|---------------------|-----------------|---------|
| 1 | License 要求 | 文档清单标注"[★核心]" | 产品文档明确声明"**无需 License**"（UDG/UNC 两侧均无） | 澄清：IPSec 无 License，与 GRE 一致，区别于 L2TP（必须 License） |
| 2 | 版本支持 | 文档清单未明确 | UDG 20.5.1+（首次发布 20.5.0，v02 20.8.0 支持 IPv6/NAT 穿越/主备）；UNC 20.6.0+ | 补全：C-U 版本差异（UDG 早于 UNC） |
| 3 | C-U 关系 | 任务要求暗示"C-U 对称" | **确认 C-U 对称同构**（文档 hash 完全一致），两侧命令族对称；与 L2TP 的 C-U 分工模式不同 | 确认 |
| 4 | 与其他特性交互 | IPSec 特性概述声明"不涉及" | **实际存在**：(a) GRE over IPSec 组合场景（独立激活脚本）；(b) 源地址互斥（GRE 文档硬约束）；(c) OSPF over IPSec 场景 | 澄清：以 GRE 文档和激活脚本为准 |
| 5 | UDG 微服务架构 | 文档清单未提及 | **UDG 独有 VNRS + IPsec 微服务双配架构**（VNRS 负责外部通信和引流，IPsec 负责 IKE 协商和加解密），双配原则是关键约束 | 补全：UDG 架构特性，UNC 侧未提及（需 Stage 3 验证 UNC 是否同构） |
| 6 | 国密支持 | 文档清单未明确 | 存在 5 个"激活国密 IPsec 支持 IKEv1 功能"脚本（GRE over IPSec/多 Sequence/指定本端接口/普通 IPv4/普通 IPv6），支持 SM3/SM4 + 国密证书 | 补全：国密场景覆盖 |
| 7 | 文档密度 | 文档清单列 24 个文件 | UDG/UNC 各 24 文件完全对称（特性概述+6 原理+1 术语+15 激活脚本+1 调测），文档密度对称且完整 | 确认 |

### 8.3 与同域隧道特性的横向对比（★Stage 3 重点）

| # | 维度 | IPFD-015004 IPSec (UDG) | IPFD-015002 GRE | GWFD-020412 L2TP (UDG) |
|---|------|--------------------------|-----------------|------------------------|
| 1 | 隧道层级 | 三层（IP 加密） | 三层（IP 封装） | 二层（PPP 封装） |
| 2 | 加密 | **有**（ESP） | 无 | 无 |
| 3 | 认证 | 有（AH/ESP + IKE PSK/证书） | 无（可选 Key） | 有（PPP PAP/CHAP） |
| 4 | 密钥协商 | **IKE 自动协商**（DH/PFS） | 无 | PPP 协商 |
| 5 | License | **无** | 无 | UDG 必须（82200BVC） |
| 6 | C-U 模式 | **对称同构**（文档 hash 一致） | **对称同构** | **C-U 分工** |
| 7 | UDG 架构 | **VNRS+IPsec 微服务双配** | 无微服务拆分 | 无微服务拆分 |
| 8 | 组播/广播 | **不支持**（需 GRE over IPSec） | 支持 | 支持 |
| 9 | 性能影响 | 有（加密开销） | 无 | 有 |
| 10 | 可靠性 | DPD + 主备（热备/冷备） | Keepalive | Hello |
| 11 | NAT 穿越 | 有（ESP+UDP） | 无 | 有 |
| 12 | 互斥关系 | 与 GRE 源地址互斥 | 与 IPSec 源地址互斥 | 与地址自动检测、入不转板互斥 |
| 13 | 标准 | RFC 2401/2402/2403/2406/4305/4868 | RFC 1701/1702/2784 | RFC 2661/2868/5072/5571/8064 |
| 14 | 典型 NF 角色 | IPSec 端点（两侧） | PE 设备（两侧） | UDG 作 LAC，LNS 在企业网 |

---

## 附录 A：source_evidence_ids 占位映射

| evidence_id | 对应来源文件 | 主要贡献章节 |
|-------------|-------------|-------------|
| EV-FK-01 | `IPFD-015004 IPSec功能特性概述_61317289.md`（UDG） | 特性定义、客户价值、应用场景、可获得性（UDG 20.5.1+，无 License）、对系统影响（封装处理性能影响）、**应用限制（5 种不支持场景）**、实现原理（IKE+AH+ESP 协议组成）、特性规格（无特殊）、**遵循标准（RFC 2401/2402/2403/2406/4305/4868/4314）**、发布历史 |
| EV-FK-02 | `实现原理/AH和ESP_62244157.md`（UDG） | **★AH/ESP 加密+认证机制**：AH（协议号 51，认证不加密，报文头字段，认证算法）、ESP（协议号 50，认证+加密，报文头/尾字段，加密算法 AES-CBC/GCM/SM4/DES，认证范围仅载荷）、AH vs ESP 差异、AH+ESP 组合 |
| EV-FK-03 | `实现原理/IKE_62256396.md`（UDG） + `实现原理/报文封装模式_62256279.md`（UDG） | **★IKE 协商机制**：安全机制（DH/PFS/身份验证/身份保护）、IKEv1 两阶段（主模式 6 条/野蛮模式 3 条/快速模式 3 条）、IKEv2 三种交换、IKEv1 vs IKEv2 差异、**UDG 缺省 IKEv2**；隧道模式封装（UDG 唯一支持，AH+ESP 须同模式） |
| EV-FK-04 | `实现原理/IPsec可靠性_78460643.md`（UDG） | **可靠性机制**：DPD（periodic 周期/on-demand 按需两种模式）、IPsec 主备隧道（热备一主一备/冷备最多一主两备） |
| EV-FK-05 | `实现原理/IPsec NAT穿越_62244160.md`（UDG） | NAT 穿越机制：定义（NAT 影响 IPsec）、实现原理（UDP 协议头 + NAT 探测 + 保活）、**约束（仅 ESP 隧道模式，不支持 IPv6 组网）** |
| EV-FK-06 | `特性配置/激活IPsec功能（普通IPv4 IPsec隧道）_01_10002.md`（UDG） | **★激活完整 9 步流程**：操作场景（网关对网关 IPv4）、数据表（30+ 参数）、**VNRS+IPsec 微服务双配原则**、9 步操作流程、**完整 MML 脚本（Device A + Device B 对称）**、DH 组约束/PSK 必配/远程地址约束/ACL 端口不生效说明 |
| EV-FK-07 | `特性配置/激活IPsec功能（GRE over IPsec）_01_10006.md`（UDG） | **GRE over IPSec 激活 10 步**：场景（IPSec 不支持组播/广播）、数据表（含 EXCHANGEMODE/LOCALIDTYPE/SADURATION）、10 步操作流程（含 GRETUNNEL+LoopBack）、**完整 MML 脚本（Device A + Device B 对称，Tunnel1 GRE + Tunnel2 IPSec）** |
| EV-FK-08 | `相关术语_88277392.md`（UDG） | **8 个核心术语**：对等体、安全联盟（SA）、安全参数索引（SPI）、安全提议、安全策略、安全联盟生成时间、安全联盟数据库（SADB）、安全策略数据库（SPDB） |
| EV-FK-09 | 其他激活脚本（普通IPv6/IPv4主备/IPv6主备/OSPF over IPSec/多Sequence/指定本端接口 + 5 个国密 IKEv1 脚本）（UDG） | 9 种场景变体激活脚本：IPv6 场景、主备隧道（热备/冷备）、OSPF over IPSec、多 Sequence 策略、指定本端接口、国密 SM3/SM4 + 国密证书 + IKEv1 |
| EV-FK-10 | `调测IPsec功能_61317192.md`（UDG） | **8 步调测流程**：PING 连通性 → DSP IFSTATUS → LST IFIPV4ADDRESS/IPSEC 双配校验 → LST IPSECINTFCFGIPSEC → PING 隧道 → DSP IKESA → DSP IKEIPSECSA → 配置检查（5 条 LST）、DSP IKESA 完整输出样例 |
| EV-FK-11 | `IPFD-016000 IPSec功能特性概述_61317289.md`（UNC） | **C-U 对称验证**：UNC 侧 IPFD-016000 特性概述文件 **hash=61317289 与 UDG 侧完全相同**，证明 C-U 两侧特性定义/原理/限制/标准完全同构；**UNC 20.6.0+ 支持**（与 UDG 20.5.1+ 版本差异） |
