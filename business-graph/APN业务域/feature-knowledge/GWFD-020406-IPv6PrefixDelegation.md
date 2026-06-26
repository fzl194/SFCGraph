# GWFD-020406 IPv6 Prefix Delegation 知识文档

> 聚焦 APN 业务域地址分配场景的 IPv6 前缀代理（Prefix Delegation, PD）特性（UDG/UPF 侧）
> ★ 在 GWFD-020401（IPv6 承载上下文）之上叠加"前缀代理"能力，使 UE 充当无线移动路由器为 LAN 侧多终端下发独立 IPv6 前缀
> ★ 与 GWFD-020403（IPv4v6 双栈）存在条件依赖、与 WSFD-104004（UNC 侧 PD）构成 C-U 协同（详见 §7）

---

## 0. 元数据（三层图谱Schema字段）

| 字段 | 取值 |
|------|------|
| feature_id | GWFD-020406 |
| feature_name | IPv6 Prefix Delegation |
| feature_group | 地址分配（IPv6功能） |
| parent_feature_id | 无独立父节点（IPv6功能目录下的独立特性；与 GWFD-020401 为"承载基础设施 / 前缀代理"分层依赖关系，与 GWFD-010105 为"地址池复用"关系，非父子关系） |
| applicable_nf_map | `{"UDG": ["PGW-U", "UPF"]}` |
| variant_dimensions | ["IPv6 delegated-prefix 分配方式（外部网元SMF/RADIUS vs 本地地址池LOCAL）", "本地地址池地址分配规则（APN-1&LOCATION-0&SMF-0 / APN-0&LOCATION-0&SMF-1 / APN-0&LOCATION-1&SMF-0 / APN-1&LOCATION-0&SMF-1组合）", "IPv6 前缀长度（49~63，<64 为 PD 标志）", "承载协议族（5GC PDU Session / EPC EPS承载 / GPRS-UMTS PDP上下文）", "下行路由发布方式（OSPFv3 用于纯IPv6场景 / OSPF 用于IPv4+IPv6混合的位置分配场景）", "DHCPv6 流程模式（快速两步 Rapid Commit / 标准四步）"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-01, EV-FK-02, EV-FK-03, EV-FK-04, EV-FK-05, EV-FK-06, EV-FK-07, EV-FK-08, EV-FK-09, EV-FK-10] |
| license_required | 82200CKF LKV3G5P6PD01 IPv6 Prefix Delegation（必须加载并使能 License 开关）；UNC 侧对应 82208006 LKV3W9V6PD11 IPv6 前缀代理 |

---

## 1. 概述

### 1.1 特性定义（是什么）

UDG 支持 **IPv6 Prefix Delegation** 功能，以便 IPv6 移动终端可以作为一个**无线移动路由器（Wireless Mobile Router / Routing Behind MS）** 来使用。UE/MS 通过单个 PDP/承载上下文/PDU 会话获取一个**网段地址（IPv6 delegated-prefix）**，用于为与其连接的 LAN 侧多台终端设备下发独立的 IPv6 地址前缀，实现家庭或小型企业用户的多终端接入。

本特性为用户提供两种 IPv6 delegated-prefix 的分配方式：

- **外部网元（SMF/RADIUS）分配用户地址场景**：SMF/PGW-C 在会话建立请求中将 UE IP Address 中 **IPv6D flag** 置位，携带 IPv6 Address 并且携带 **IPv6 Prefix Delegation Bits field** 指示 IPv6 地址前缀长度。
- **本地用户面（PGW-U/UPF）分配地址场景**：PGW-U/UPF 上配置 IPv6 地址前缀小于 64 位的地址池，SMF/PGW-C 在会话建立请求中将 UE IP Address 的 **CHV6** 置位；PGW-U/UPF 在会话建立响应中 UE IP Address 的 IPv6D flag 置位，携带 IPv6 Address 和 IPv6 Prefix Delegation Bits field。

> 说明：IPv6 Prefix Delegation 功能**不支持**从 DHCP Server 获取并分配 IPv6 delegated-prefix（文档原文明确）。

> 来源：`output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020406 IPv6 Prefix Delegation/GWFD-020406 IPv6 Prefix Delegation特性概述_79370029.md`（"定义"、"应用场景"、"原理概述"章节）[EV-FK-01]

### 1.2 适用NF（UDG/UNC网元）

| 涉及NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| MS/UE（含无线移动路由器） | 终端 | 无特殊要求 | 激活成功后，通过一个 PDP/承载上下文/PDU 会话获取一个网段地址，用于为与其连接的多台终端设备下发独立的 IPv6 地址前缀 |
| PGW-C / SMF | 控制面（UNC） | UNC 20.5.0 及后续版本 | 与 PCF、OCS、CHF 等周边网元交互，获取策略控制信息、生成话单等；为 Prefix Delegation 终端携带 IPv6D flag + IPv6 Address + IPv6 Prefix Delegation Bits field（C 侧详见 WSFD-104004） |
| **PGW-U / UPF** | **用户面（UDG，本特性作用网元）** | **UDG 20.5.0 及后续版本** | 对报文进行识别和解析，根据解析结果匹配规则，对不同 IPv6 业务进行不同的计费和动作处理；支持为 Prefix Delegation 终端分配 IPv6 地址 |
| AAA Server | 鉴权与地址分配 | 无特殊要求 | 对用户进行接入鉴权，并且在系统采用 RADIUS 地址分配方式的时候，为用户分配 IPv6 地址前缀和 IPv6 delegated-prefix |

> ★ 与 GWFD-020401（SGW-U/PGW-U/UPF 均适用）不同：本特性适用 NF 明确**仅列 PGW-U、UPF**（不含 SGW-U），因为前缀代理仅在"锚定用户面"（PGW-U/UPF）才有意义。UDG 版本要求 **20.5.0**（晚于 020401 的 20.0.0）。

> 来源：`GWFD-020406 IPv6 Prefix Delegation特性概述_79370029.md`（"可获得性-涉及NF"章节）[EV-FK-01]

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|---------|---------|---------|
| 01 | UDG 20.5.0 | 首次发布 |

> ★ 对比 GWFD-020401（20.0.0 首发）：PD 特性首发晚于承载上下文约 0.5 个大版本，符合"承载基础设施先行、高阶特性后置"的演进规律（详见 §7.2）。

> 来源：`GWFD-020406 IPv6 Prefix Delegation特性概述_79370029.md`（"发布历史"章节）[EV-FK-01]

### 1.4 License

本特性必须获得 License 许可后才能使用，对应的 License 控制项为：

| License编号 | License名称 | 适用网元 |
|------------|------------|---------|
| 82200CKF | LKV3G5P6PD01 IPv6 Prefix Delegation | UDG（PGW-U/UPF） |
| 82208006 | LKV3W9V6PD11 IPv6 前缀代理 | UNC（PGW-C/SMF） |

激活时必须通过 `SET LICENSESWITCH:LICITEM="LKV3G5P6PD01",SWITCH=ENABLE;` 打开 License 配置开关。

> 来源：`GWFD-020406 IPv6 Prefix Delegation特性概述_79370029.md`（"可获得性-License 支持"章节，UDG 侧 License）[EV-FK-01]；UNC 侧 License 见 `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104004 IPv6前缀代理/特性概述_76459525.md`（"可获得性-License支持"章节）[EV-FK-09]

### 1.5 前置条件与依赖

| 前置条件 | 说明 |
|---------|------|
| License加载并使能 | 必须加载 License 控制项 82200CKF LKV3G5P6PD01 并通过 SET LICENSESWITCH 打开开关 |
| 阅读特性根文档 | 请仔细阅读 `GWFD-020406 IPv6 Prefix Delegation_79370033.md` |
| **IPv6 承载上下文已开启（★ 文档显式依赖）** | **UDG 需要建立 IPv6 承载上下文，因此需开启 GWFD-020401 IPv6 承载上下文特性（控制项 82209828）** |
| IPv4v6 双栈接入已开启（条件依赖） | 如果需要对 IPv4v6 双栈接入用户的业务进行解析，则需要先开启 GWFD-020403 IPv4v6 双栈接入特性（控制项 82209829） |
| 数据面逻辑接口配置完成 | UDG 本端已完成数据面逻辑接口（Sa/Sc/Pa）和 N4/Sxa/Sxb 逻辑接口的配置（本地地址池场景的前置，见初始配置手册） |
| UDG/UNC 控制面地址池规划一致 | UDG 本端配置的 APN/DNN 实例应该与 C 面（SMF/SGW-C/PGW-C）配置的 APN/DNN 实例一致 |
| VPN 实例三者一致 | 地址池绑定的 VPN 实例、用户激活使用的 APN 绑定的 VPN 实例、与 PDN/DN 连接的 Gi/SGi/N6 接口的外联口绑定的 VPN 实例，三者必须一致 |
| 外部地址分配场景的 OSPFv3 路由规划 | 需规划 OSPFv3 进程号、Router ID（全网唯一）、区域标识（与对端协商）、接口名、引入路由类型（PROTOCOL=wlr） |

> 来源：`GWFD-020406 IPv6 Prefix Delegation特性概述_79370029.md`（"与其他特性的交互"章节）[EV-FK-01]；`激活外部网元地址分配的IPv6 Prefix Delegation功能_80269177.md`（"必备事项-前提条件"、"数据"章节）[EV-FK-04]；`基于APN_DNN分配地址_80250128.md`（"必备事项-前提条件"章节）[EV-FK-05]

### 1.6 与其他特性的交互（★ 文档显式列出7条）

| 交互类型 | 相关特性 | 控制项名称 | 交互说明（文档原文） |
|---------|---------|-----------|-------------------|
| **依赖** | **GWFD-020401 IPv6承载上下文** | 82209828 IPv6承载上下文 | **UDG 需要建立 IPv6 承载上下文，因此需开启 IPv6 承载上下文特性** |
| **依赖（条件）** | **GWFD-020403 IPv4v6双栈接入** | 82209829 IPv4v6双栈接入 | 如果需要对 IPv4v6 双栈接入用户的业务进行解析，则需要先开启 IPv4v6 双栈接入特性 |
| **互斥** | GWFD-020412 L2TP VPN | 82200BVC L2TP VPN | L2TP VPN 通过 LNS 设备实现了手机后路由功能，所以在同一 APN 下，L2TP VPN 和手机后路由功能无需同时部署 |
| **互斥** | GWFD-010108 / GWFD-020808 用户面地址自动检测 | - | 手机后路由用户不能做用户面地址自动检测 |
| **互斥** | NAT基本功能 | 82200DAB NAT基本功能（Mbps） | 手机后路由的用户不支持 NAT 地址转换 |
| **互斥** | GWFD-020482 入不转板功能 | - | 手机后路由用户不支持入不转板功能 |
| **互斥** | GWFD-020531 通用DNN漫游分流 | 82200GCJ LKV3G5STCA01 移动VPN智能分流园区接入 | 手机后路由用户不支持通用 DNN 漫游分流功能 |

> ★ 关键发现：本特性有 **2 条依赖**（020401 强制、020403 条件）+ **5 条互斥**（共 7 条交互），是 APN 地址分配场景中交互约束最丰富的特性之一。互斥原因高度统一："手机后路由用户"（PD 用户）与其他手机后路由方案（L2TP VPN）、地址检测/转换/分流功能冲突。

> 来源：`GWFD-020406 IPv6 Prefix Delegation特性概述_79370029.md`（"与其他特性的交互"章节）[EV-FK-01]

### 1.7 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | 基于 IPv6 场景部署，扩展业务范围，可为用户提供 IPv6 移动路由器服务，吸引有此类需求的用户 |
| 用户 | 通过 MS/UE（作为无线移动路由器）将多个终端接入网络，帮助家庭或小型企业用户实现移动接入服务 |

> 来源：`GWFD-020406 IPv6 Prefix Delegation特性概述_79370029.md`（"客户价值"章节）[EV-FK-01]

### 1.8 应用场景

华为 UDG 支持 Routing Behind MS 功能，可以满足在 **IPv4 组网条件下**通过一台无线设备（MS/UE）将多台终端设备接入网络并与网络侧设备进行双向数据业务的技术方案。

随着 IPv6 技术的迅猛发展，为了满足在 **IPv6 组网条件下**通过一台无线设备（MS/UE）将多台终端设备接入网络并与网络侧设备进行双向数据业务的技术方案，华为 UDG 提供了 IPv6 Prefix Delegation 功能，为更多的家庭或小型企业用户提供了服务，同时也丰富了 IPv6 解决方案体系，提供了更为完善的组网方案。

> 来源：`GWFD-020406 IPv6 Prefix Delegation特性概述_79370029.md`（"应用场景"章节）[EV-FK-01]

### 1.9 对系统的影响

IPv6 Prefix Delegation 特性只进行简单信元解析和路由转发，**对系统影响可忽略**（文档原文）。

> ★ 对比 GWFD-020401（承载数增加→CPU上升）：PD 特性的系统开销极低，因为它仅做信元解析和路由转发，不涉及深度报文解析或大量状态维护。

> 来源：`GWFD-020406 IPv6 Prefix Delegation特性概述_79370029.md`（"对系统的影响"章节）[EV-FK-01]

### 1.10 应用限制

- **本地地址池方式**为用户分配 IPv6 delegated-prefix 时，同一 APN 下的 IPv6 delegated-prefix 长度**必须相同**。
- **外部网元（SMF/RADIUS）为用户分配** IPv6 delegated-prefix 时，同一 APN 下的 IPv6 delegated-prefix 长度**可以不同**。
- IPv6 delegated-prefix 功能中用户分配的**地址前缀范围为 49~64 之间，不包含 64 位**（即实际范围 **49~63**）。

> ★ 关键阈值：V6PREFIXLENGTH < 64 是地址池被判定为"PD 方式分配"的标志。ADD SECTION 的 V6PREFIXLENGTH 参数文档原文："前缀长度范围为 49~64，当前缀长度小于 64 时，则表示该地址池采用 IPv6 Prefix Delegation 方式分配。" 这构成 PD 与普通 IPv6 单栈地址分配（64 位）的**唯一配置树分水岭**。

> 来源：`GWFD-020406 IPv6 Prefix Delegation特性概述_79370029.md`（"应用限制"章节）[EV-FK-01]；V6PREFIXLENGTH 阈值见各激活文档"数据"表（如 `基于APN_DNN分配地址_80250128.md`）[EV-FK-05]

### 1.11 特性规格与标准

**规格**：本特性不涉及特性规格（UDG 侧文档声明）。UNC 侧（WSFD-104004）有规格：整机支持无线路由器同时在线最大数 20,000；单用户最大支持手机后路由网段数 30。

**计费与话单**：本特性不涉及计费与话单。

遵循标准：

| 标准类别 | 标准编号 | 标准名称 |
|---------|---------|---------|
| IETF | RFC 3315 | Dynamic Host Configuration Protocol for IPv6 (DHCPv6) |
| 3GPP | 23.060 | General Packet Radio Service (GPRS) Service Description; Stage 2 |
| 3GPP | 29.244 | Interface between the Control Plane and the User Plane of EPC Nodes |

> ★ 对比 GWFD-020401（4 条 3GPP 标准，无 RFC）：PD 特性含 **RFC 3315 DHCPv6**，反映了 PD 依赖 DHCPv6 两步/四步协商流程；无 RFC 2460（IPv6 协议规范）表明协议规范仍由承载层（020402）承担。对比 UNC 侧 WSFD-104004（3GPP 23.214/29.244 + RFC 2865 RADIUS）：C-U 两侧标准集互补，U 侧重 DHCPv6（前缀分配协议），C 侧重 RADIUS（鉴权+地址下发协议）。

> 来源：`GWFD-020406 IPv6 Prefix Delegation特性概述_79370029.md`（"特性规格"、"遵循标准"、"计费与话单"章节）[EV-FK-01]；UNC 侧规格见 `特性概述_76459525.md`（"特性规格"章节）[EV-FK-09]

---

## 2. 核心概念

### 2.1 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| IPv6 Prefix Delegation (PD) | IPv6 前缀代理 | IPv6 移动终端作为无线移动路由器，通过单个会话获取网段地址，为 LAN 侧多终端下发独立 IPv6 前缀 |
| Routing Behind MS | 手机后路由 | MS/UE 后面挂接多台终端的路由方案（IPv4 版本），PD 是其 IPv6 版本 |
| IPv6 delegated-prefix | IPv6 代理前缀 | 下发给 UE 的网段地址，前缀长度 49~63（< 64） |
| IPv6D flag | IPv6 Delegation 标志位 | UE IP Address 信元中的标志位，置 1 表示该地址为 PD 地址 |
| IPv6 Prefix Delegation Bits field | IPv6 PD 前缀长度字段 | UE IP Address 信元中的字段，指示 IPv6 地址前缀长度 |
| CHV6 | Choose IPv6 标志位 | SMF/PGW-C 请求 UDG 本地分配 IPv6 地址的标志位 |
| IA_PD option | Identity Association for Prefix Delegation | DHCPv6 Solicit 消息中的选项，表示申请 IPv6 delegated-prefix |
| Rapid Commit option | DHCPv6 快速提交选项 | 携带则使用两步快速流程；不携带则使用标准四步流程 |
| Prefix Exclude Option | 前缀排除选项 | 支持使用 IPv6 delegated-prefix 段中的一个前缀地址作为链路地址与 UPF/PGW-U 进行 DHCPv6 消息交互 |
| O-flag | Other-config flag（RA 消息） | Router Advertisement 中置 1 表示后续可通过 DHCPv6 方式获取其他相关参数 |
| WLR | White Label Route（用户内部路由） | UDG 内部生成的用户下行路由，通过 OSPFv3 IMPORTROUTE 发布到骨干网 |
| OSPFv3 | OSPF version 3 | IPv6 专用 OSPF 路由协议（PD 下行路由发布主进程，纯 IPv6 场景） |
| OSPF | OSPF version 2 | IPv4 OSPF 路由协议（基于位置的 PD 场景，IPv4+IPv6 混合下行路由发布） |

### 2.2 对象模型（IPv6 PD 配置体系）

IPv6 PD 的配置架构基于"License 使能 + 地址池体系（V6PREFIXLENGTH<64）+ PD 协议交互 + 下行路由发布"的四层模型：

```
                      ┌──────────────────────────────┐
                      │   Layer 0: License 使能层      │
                      │   SET LICENSESWITCH           │
                      │   LICITEM=LKV3G5P6PD01        │
                      │   （叠加在 020401 的 V6PB01   │
                      │    和 020403 的 VDSA01 之上） │
                      └───────────────┬──────────────┘
                                      │
                                      ▼
        ┌─────────────────────────────────────────────────┐
        │  Layer 1: IPv6 承载基础设施（依赖 GWFD-020401）   │
        │  ─ 已建立 IPv6 PDP上下文/EPS承载/PDU Session       │
        │  ─ 已完成 OSPFv3 进程基础配置（020401 承担）       │
        │  ─ RA 通告机制可用                                 │
        └─────────────────────┬───────────────────────────┘
                              │
                ┌─────────────┴─────────────┐
                ▼                           ▼
   ┌────────────────────────┐   ┌────────────────────────────┐
   │ Layer 2a: 外部分配场景  │   │ Layer 2b: 本地地址池场景    │
   │ （SMF/RADIUS 决策地址） │   │ （UPF/PGW-U 本地池分配）    │
   │ ADD POOL                │   │ ADD POOL                    │
   │   POOLTYPE=EXTERNAL     │   │   POOLTYPE=LOCAL            │
   │ ADD SECTION             │   │ ADD SECTION                 │
   │   V6PREFIXLENGTH=63 ★   │   │   V6PREFIXLENGTH=63 ★       │
   │ （PD 标志：<64）         │   │ （PD 标志：<64）             │
   │ ADD POOLGROUP           │   │ ADD POOLGROUP               │
   │ ADD POOLBINDGROUP       │   │ ADD POOLBINDGROUP           │
   │ ADD APN                 │   │ ADD APN                     │
   │ ADD POOLGRPMAP          │   │ SET APNADDRESSATTR          │
   │   （APN→POOLGROUP）     │   │ ADD POOLGRPMAP              │
   │                         │   │   （APN/SMF/LOCATION→POOLGROUP）│
   │ CHV6 由 SMF 置位        │   │ ADD CPNODEID（SMF 场景）    │
   │ IPv6D/Prefix Bits       │   │ SET IPALLOCRULE             │
   │   由 SMF/AAA 置位       │   │ SET IPALLOCBYSMFGLBSW        │
   └───────────┬────────────┘   │   （SMF 场景）               │
               │                │ ADD LACGROUP/LACID          │
               │                │ SET IPALLOCBYLOCGLBSW        │
               │                │   （LOCATION 场景）           │
               │                └─────────────┬──────────────┘
               │                              │
               └──────────────┬───────────────┘
                              │
                              ▼
              ┌──────────────────────────────┐
              │  Layer 3: IPv6 PD 下行路由发布 │
              │  （纯 IPv6 场景）              │
              │  ADD OSPFV3 (进程)             │
              │    PROCID=6, ROUTERID          │
              │    BFDALLINTFFLG=TRUE         │
              │    VPNINSCAPSIMFLG=TRUE ★     │
              │    VIRTUALSYSFLAG=TRUE        │
              │  ADD OSPFV3AREA                │
              │  ADD OSPFV3INTERFACE           │
              │    DRPRI=0                     │
              │  ADD OSPFV3IMPORTROUTE         │
              │    PROTOCOL=wlr ★              │
              │  ──────────────────────────    │
              │  （位置分配 IPv4+IPv6 混合场景）│
              │  ADD OSPF (IPv4 侧下行路由)    │
              │  ADD OSPFAREA                  │
              │  ADD OSPFNETWORK               │
              │  ADD OSPFIMPORTROUTE PROTOCOL=wlr│
              │  ADD ADRLOCWHITELST（白名单）  │
              └──────────────────────────────┘
```

核心配置对象说明：

| 对象 | 作用 | IPv6 PD 场景角色 |
|------|------|----------------|
| **ADD POOL (POOLTYPE)** | 地址池类型 | **EXTERNAL（外部分配）/ LOCAL（本地分配）二选一，决定 PD 地址来源** |
| **ADD SECTION (V6PREFIXLENGTH)** | IPv6 前缀长度 | **★ PD 标志：取值 49~63（<64）即表示该地址池采用 PD 方式分配** |
| ADD POOLGROUP | 地址池组 | 组织多个 POOL，支持 IPV6ALLOCPRIALG 优先级算法 |
| ADD POOLBINDGROUP | 地址池绑定到地址池组 | 按优先级绑定 |
| ADD APN | APN/DNN 实例 | 全网规划，与 C 面一致 |
| SET APNADDRESSATTR | APN 地址分配属性 | SUPPORTIPV4=ENABLE, SUPPORTIPV6=ENABLE（双支持） |
| ADD POOLGRPMAP | 地址池组映射 | APN/SMF/LOCATION → POOLGROUP 的映射规则 |
| ADD CPNODEID | SMF NodeID | SMF 场景必备，标识 SMF 实例（IPV4NODEID/IPV6NODEID/FQDNNODEID 三选一） |
| SET IPALLOCRULE | 地址分配规则 | 三级规则（FIRSTRULE/SECONDRULE/THIRDRULE），APN/LOCATION/SMF 任意组合 |
| SET IPALLOCBYSMFGLBSW | 基于 SMF 分配全局开关 | SMF 场景必配 |
| ADD LACGROUP / ADD LACID | LAC 位置区组 | LOCATION 场景必备 |
| SET IPALLOCBYLOCGLBSW | 基于位置区分配全局开关 | LOCATION 场景必配 |
| ADD CONFLICTIPV6 | 冲突 IPv6 地址 | 标识已使用的 IPv6 地址（如示例 fc00:...:fcee:0:0:0:1/63），不参与分配 |
| ADD ADRLOCWHITELST | 位置区地址分配白名单 | LOCATION 场景可选，白名单用户不基于位置区分配 |
| **ADD OSPFV3 / IMPORTROUTE** | **OSPFv3 进程 + 引入 WLR** | **★ PD 纯 IPv6 下行路由发布核心（继承自 020401，但增加 BFD/VIRTUALSYSFLAG 等参数）** |
| ADD OSPF / IMPORTROUTE | OSPF 进程 + 引入 WLR | LOCATION 场景的 IPv4 侧下行路由发布（IPv4+IPv6 混合） |
| ADD VPNINST | VPN 实例 | 地址池/APN/外联口三者 VPN 必须一致 |

### 2.3 在 APN 地址分配场景的角色

GWFD-020406 在 APN 地址分配场景中扮演"**IPv6 前缀代理高阶层**"的角色，建立在 GWFD-020401 承载基础设施之上，与 GWFD-020403（双栈使能）、GWFD-010105（地址池体系）协同：

```
┌──────────────────────────────────────────────────────────────┐
│ Layer A: IPv6 承载上下文基础设施层（GWFD-020401，License V6PB01）│
│   - 支持 IPv6 PDP上下文/EPS承载/PDU Session/QoS Flow 的       │
│     激活、去激活、更新                                          │
│   - 用户面 IPv6 承载（透明转发）                              │
│   - RA 通告机制                                                │
│   - IPv6 下行路由发布基础（OSPFv3 + WLR）                      │
└──────────────────────────┬───────────────────────────────────┘
                           │ 被以下 IPv6 高阶特性依赖
                           ▼
┌──────────────────────────────────────────────────────────────┐
│ Layer B1: IPv6 前缀代理高阶层（GWFD-020406，License P6PD01） ★│
│   - UE 作为无线移动路由器                                      │
│   - IPv6 前缀长度 49~63（<64）                                 │
│   - IPv6D flag + Prefix Delegation Bits field + DHCPv6 协商   │
│   - 为 LAN 侧多终端下发独立 IPv6 地址前缀（家庭/小企业场景）   │
└──────────────────────────┬───────────────────────────────────┘
                           │ 与以下特性协同（条件依赖或并列）
                           ▼
┌──────────────────────────────────────────────────────────────┐
│ Layer B2: IPv4v6 双栈使能层（GWFD-020403，License VDSA01）    │
│   - 条件依赖：若 PD 用户为 IPv4v6 双栈且需业务解析，必须开启   │
│   - 与 PD 共享 RA 通告机制描述                                 │
└──────────────────────────┬───────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────┐
│ Layer C: 地址池体系层（GWFD-010105）                           │
│   - POOL/SECTION/POOLGROUP/POOLGRPMAP 复用                    │
│   - PD 仅通过 V6PREFIXLENGTH<64 区分普通 IPv6 池               │
└──────────────────────────────────────────────────────────────┘
```

具体角色：

1. **前缀代理能力叠加**：GWFD-020406 在 GWFD-020401 的 IPv6 承载之上叠加"前缀代理"能力，使一个会话可承载一个网段（而非单个 IPv6 地址）。
2. **网段地址分配**：通过 V6PREFIXLENGTH<64 的地址池配置，让 UDG 本地池或外部网元为 UE 分配一个网段，UE 再为 LAN 侧终端从该网段分配 64 位前缀。
3. **C-U 协同关键节点**：本特性是 UDG 侧实现，依赖 UNC 侧 WSFD-104004 的控制面决策（CHV6/IPv6D/Prefix Bits 信元携带），两者通过 PFCP Session Establishment/Report 消息协同完成 PD 流程（详见 §3.2、§7.4）。

---

## 3. 原理与流程

### 3.1 实现原理：IPv6 前缀代理机制

#### 3.1.1 IPv6 PD 地址分配双场景机制

IPv6 Prefix Delegation 功能中 UDG 为用户分配携带 IPv6 地址前缀长度的 IPv6 地址，按照地址分配方式分为以下两个场景：

**场景一：外部用户（SMF、Radius Server）分配用户地址**

```
SMF/PGW-C                PGW-U/UPF              AAA Server
   │                         │                       │
   │  1.鉴权请求（Framed-IPv6-Prefix 等）             │
   ├─────────────────────────────────────────────────►│
   │                         │                       │
   │  2.鉴权响应             │                       │
   │  携带 IPv6 Address      │                       │
   │  置位 IPv6D flag        │                       │
   │  携带 Prefix Delegation │                       │
   │  Bits field（前缀长度） │                       │
   │◄─────────────────────────────────────────────────┤
   │                         │                       │
   │  3.PFCP Session         │                       │
   │  Establishment Request  │                       │
   │  UE IP Address:         │                       │
   │   IPv6D=1 ★             │                       │
   │   IPv6 Address=<前缀>  │                       │
   │   Prefix Bits=<49~63>  │                       │
   ├────────────────────────►│                       │
   │                         │                       │
   │  4.PFCP Session         │                       │
   │  Establishment Response │                       │
   │  （透传 IPv6D/Address/  │                       │
   │   Prefix Bits）         │                       │
   │◄────────────────────────┤                       │
```

**场景二：本地用户面（PGW-U/UPF）分配地址**

```
SMF/PGW-C                PGW-U/UPF              LOCAL POOL
   │                         │                       │
   │  1.PFCP Session         │                       │
   │  Establishment Request  │                       │
   │  UE IP Address:         │                       │
   │   CHV6=1 ★              │                       │
   │   （请求本地分配 IPv6） │                       │
   ├────────────────────────►│                       │
   │                         │                       │
   │                         │  2.从 V6PREFIXLENGTH<64│
   │                         │    的 LOCAL 池中      │
   │                         │    分配网段地址       │
   │                         ├──────────────────────►│
   │                         │                       │
   │                         │  3.网段地址返回       │
   │                         │  （前缀长度 49~63）   │
   │                         │◄──────────────────────┤
   │                         │                       │
   │  4.PFCP Session         │                       │
   │  Establishment Response │                       │
   │  UE IP Address:         │                       │
   │   IPv6D=1 ★             │                       │
   │   IPv6 Address=<前缀>  │                       │
   │   Prefix Bits=<49~63>  │                       │
   │   （由 UPF 置位）       │                       │
   │◄────────────────────────┤                       │
```

> ★ 关键区别：场景一 IPv6D 由 SMF/AAA 置位（C 面决策）；场景二 CHV6 由 SMF 置位请求，IPv6D 由 UPF 在响应中置位（U 面决策）。

> 来源：`GWFD-020406 IPv6 Prefix Delegation特性概述_79370029.md`（"原理概述"章节）[EV-FK-01]

#### 3.1.2 UE IP Address 信元结构

IP Address 信元结构如特性概述"图2 UE IP Address 信元结构"所示，关键信元：

| 信元字段 | 含义 | PD 场景取值 |
|---------|------|------------|
| CHV6 | Choose IPv6 标志位（SMF→UPF 请求本地分配） | 1（场景二必置位） |
| IPv6D | IPv6 Delegation 标志位 | 1（PD 标识，两场景响应中必置位） |
| IPv6 Address | IPv6 地址（网段起始地址） | 全网规划的池中地址 |
| IPv6 Prefix Delegation Bits field | IPv6 PD 前缀长度 | 49~63 |

> 来源：`GWFD-020406 IPv6 Prefix Delegation特性概述_79370029.md`（"原理概述-图2"章节）[EV-FK-01]

#### 3.1.3 DHCPv6 前缀代理协商机制（UE 获取 delegated-prefix 后的二次流程）

UE 获取 IPv6 地址前缀后，发起 DHCPv6 地址分配流程（RFC 3315）：

**快速两步流程（携带 Rapid Commit option）**：

```
UE/MS                    UPF/PGW-U              SMF/PGW-C
   │                         │                       │
   │  DHCPv6 Solicit         │                       │
   │  携带:                  │                       │
   │   - IA_PD option ★      │                       │
   │   - Rapid Commit option │                       │
   │   - Prefix Exclude Opt  │                       │
   ├────────────────────────►│                       │
   │                         │  PFCP Session Report  │
   │                         │  Request              │
   │                         ├──────────────────────►│
   │                         │  PFCP Session Report  │
   │                         │  Response             │
   │                         │◄──────────────────────┤
   │  DHCPv6 Reply           │                       │
   │  携带:                  │                       │
   │   - IPv6 delegated-prefix                      │
   │   - Prefix Exclude Option │                    │
   │◄────────────────────────┤                       │
```

**标准四步流程（未携带 Rapid Commit option）**：在 Solicit 后增加 DHCPv6 Advertise（UPF→UE）和 DHCPv6 Request（UE→UPF），共四步。

DHCPv6 携带的关键 option：

| Option | 含义 | UDG 处理行为 |
|--------|------|-------------|
| **IA_PD option** | 申请 IPv6 delegated-prefix | **只支持每个 UE 分配一个 IPv6 delegated-prefix 段**；若 UE 携带多个 IA_PD，仅第一个分配，其余返回 "NoPrefixAvail" 状态码 |
| Rapid Commit option | 申请快速两步流程 | 携带则两步；不携带则四步 |
| Prefix Exclude Option | 链路地址排除 | 支持 delegated-prefix 段中一个前缀地址作为链路地址与 UPF 交互；UE 不携带也按携带处理 |
| T1/T2 定时器 | 续约定时器 | **固定 0xFFFFFFFF**（代表 delegated-prefix 一直有效，不需要更新） |
| preferred-lifetime / valid-lifetime | IA_PD Prefix 生命周期 | **固定 0xFFFFFFFF**（一直有效） |

> ★ 关键设计：PD 的 delegated-prefix **永久有效（0xFFFFFFFF）**，与普通 DHCPv6 地址的有限租期不同，反映了移动路由器场景的稳定性需求。

> 来源：`5GC业务流程_79707829.md`、`EPC业务流程_79707828.md`、`GPRS_UMTS业务流程_79707827.md`（步骤9-21 + 说明段落，三个文档内容一致，仅网元名不同）[EV-FK-02][EV-FK-03][EV-FK-04... 实际为 flow 文件，编号见 §7.5]

#### 3.1.4 IPv6 下行路由发布机制（继承自 GWFD-020401 并增强）

PD 用户接入后，UDG 内部生成 WLR 用户下行路由。本特性通过 OSPFv3 的 IMPORTROUTE 功能将 WLR 路由发布到骨干网。

相比 GWFD-020401 的 OSPFv3 配置，本特性的 OSPFV3 命令增加了以下参数（反映 PD 场景的组网复杂度）：

| 参数 | 取值 | 说明（PD 场景约束） |
|------|------|-------------------|
| BFDALLINTFFLG | TRUE | 使能 BFD（PD 用户对下行可靠性要求高） |
| VPNINSCAPSIMFLG | TRUE | **固定取值**：去使能 VPN 路由环路检测；支持 VPN 多实例必须取消环路检查，否则 OSPFv3 路由引入失败 |
| VIRTUALSYSFLAG | TRUE | OSPFv3 共网段虚拟系统使能（共网段组网必备） |
| DRPRI | 0 | OSPFv3INTERFACE 接口优先级为 0，不参与 DR/BDR 选举（避免 VNF 被选为 DR/BDR） |
| PROTOCOL | wlr | 引入 WLR 路由（继承 020401 的"必须选 wlr，不能只选 wlr_sp/wlr_ud"约束） |

> 来源：`激活外部网元地址分配的IPv6 Prefix Delegation功能_80269177.md`（"操作步骤"步骤3、"任务示例-脚本"）[EV-FK-04]；OSPFV3 参数约束见"数据"表说明列

### 3.2 业务流程（端到端 IPv6 PD 接入，以 5GC 为例）

基于 GWFD-020406 文档的 5GC 业务流程（EPC/GPRS-UMTS 流程结构一致，仅网元名不同），IPv6 PD 用户端到端接入流程分为两大阶段：

```
┌─────────────────────────────────────────────────────────────────┐
│ 阶段A：UE 获取 IPv6 前缀流程（PDU 会话建立 + PFCP 协商）          │
└─────────────────────────────────────────────────────────────────┘

1. UE 发起 PDU 会话请求（请求 IPv6 接入）
        │
        ▼
2. AMF → SMF：Nsmf_PDUSession_CreateSMContext Request
        │
        ▼
3. SMF → AAA Server：鉴权请求
   ★ P1：AAA Server 鉴权响应携带 IPv6 Address + IPv6D=1 + Prefix Bits
        │  （AAA 支持 PD 终端分配，场景一）
        ▼
4. AAA Server → SMF：鉴权响应（含 IPv6 PD 信息）
        │
        ▼
5. SMF → UPF：PFCP Session Establishment Request
   ★ P2：SMF 携带 IPv6 Address + IPv6D=1 + Prefix Bits（场景一）
      或 CHV6=1（场景二，请求 UPF 本地分配）
        │
        ▼
6. UPF → SMF：PFCP Session Establishment Response
   ★ P3：UPF 携带 IPv6 Address + IPv6D=1 + Prefix Bits
      （场景二由 UPF 填充；场景一透传 SMF/AAA 的值）
        │
        ▼
7. SMF → AMF：Nsmf_PDUSession_CreateSMContext Response
8. AMF ↔ SMF：Nsmf_PDUSession_N1N2Message Transfer
        │
        ▼
9. UE → UPF：ICMPv6 Router Solicitation（发起 IPv6 自动配置协商）
        │
        ▼
10. UPF → SMF：PFCP Session Report Request（上报 IPv6 协商请求）
11. SMF → UPF：PFCP Session Report Response
        │
        ▼
12. UPF → UE：ICMPv6 Router Advertisement
    携带分配给 UE 的 IPv6 地址前缀
    ★ O-flag=1（表示后续可通过 DHCPv6 获取其他参数）

┌─────────────────────────────────────────────────────────────────┐
│ 阶段B：UE 发起 DHCPv6 地址分配流程（获取 delegated-prefix）       │
└─────────────────────────────────────────────────────────────────┘

13. UE → UPF：DHCPv6 Solicit
    携带 IA_PD option + Rapid Commit option + Prefix Exclude Option
        │
        ▼
14~15. UPF ↔ SMF：PFCP Session Report Request/Response（上报 DHCPv6 信息）
        │
        ▼
16. （仅标准四步）UPF → UE：DHCPv6 Advertise
17. （仅标准四步）UE → UPF：DHCPv6 Request
18~19. （仅标准四步）UPF ↔ SMF：PFCP Session Report Request/Response
        │
        ▼
20. UPF → UE：DHCPv6 Reply
    携带 IPv6 delegated-prefix + Prefix Exclude Option
        │
        ▼
21. UE 下的终端设备申请接入时
    ★ UE 为其从 IPv6 delegated-prefix 段中分配 64 位前缀
    （UE 充当路由器，为 LAN 侧终端二次分配）
```

> ★ 流程要点：
> - **两阶段分离**：先获取 IPv6 前缀（PDU 会话建立），再获取 delegated-prefix（DHCPv6）。这与 GWFD-020401 的"单阶段承载建立"不同。
> - **C-U 三次协同点**：P1（AAA→SMF）、P2（SMF→UPF 请求）、P3（UPF→SMF 响应），每次都携带 IPv6D/IPv6 Address/Prefix Bits 三元组。
> - **UE 二次分配**：UE 拿到 /49~63 网段后，**为 LAN 侧终端分配 64 位前缀**（UE 充当路由器）。

> 来源：`5GC业务流程_79707829.md`（步骤1-21 + 说明段落）[EV-FK-02]；EPC/GPRS-UMTS 流程结构相同，见 `EPC业务流程_79707828.md`、`GPRS_UMTS业务流程_79707827.md`[EV-FK-03][EV-FK-04]

### 3.3 协议交互

| 接口 | 交互网元 | 消息类型 | 说明 |
|------|---------|---------|------|
| N4（5G）/ Sxa / Sxb（4G） | SMF/PGW-C ↔ UPF/PGW-U | PFCP Session Establishment Request/Response | **C-U 协同主通道**：CHV6（请求本地分配）、IPv6D+Address+Prefix Bits（携带或返回 PD 信息） |
| N4 / Sxa / Sxb | UPF → SMF/PGW-C | PFCP Session Report Request | UPF 上报 RS 协商请求、DHCPv6 Solicit/Request 信息 |
| N4 / Sxa / Sxb | SMF/PGW-C → UPF | PFCP Session Report Response | C 面响应 RS/DHCPv6 上报 |
| Uu / 空口 | UE → UPF/PGW-U | ICMPv6 Router Solicitation | UE 发起 IPv6 自动配置（可选触发） |
| Uu / 空口 | UPF/PGW-U → UE | ICMPv6 Router Advertisement | **UPF 通告 IPv6 前缀 + O-flag=1**（共享自 GWFD-020401 RA 机制） |
| Uu / 空口 | UE → UPF/PGW-U | DHCPv6 Solicit（IA_PD + Rapid Commit + Prefix Exclude） | UE 申请 delegated-prefix |
| Uu / 空口 | UPF/PGW-U → UE | DHCPv6 Reply（delegated-prefix + Prefix Exclude） | UPF 返回 delegated-prefix |
| Uu / 空口（UE-LAN） | UE → LAN 终端 | （UE 内部二次分配 64 位前缀） | UE 作为路由器为 LAN 侧终端分配 |
| Gi/SGi/N6 | UPF/PGW-U ↔ DN | IPv6 报文透明传输 | LAN 终端 → UE → UPF → DN 双向数据 |
| 骨干网 | UDG ↔ 骨干网路由器 | OSPFv3 LSA（引入 WLR） | IPv6 PD 用户下行路由发布到骨干网 |
| AAA（5G/EPC/GPRS） | SMF/PGW-C ↔ AAA Server | RADIUS Access-Request/Accept | **C 侧 WSFD-104004 依赖**：AAA 为 PD 终端分配 IPv6 前缀（Framed-IPv6-Prefix） |

> 来源：`5GC业务流程_79707829.md`（完整流程含 PFCP/ICMPv6/DHCPv6 消息）[EV-FK-02]；AAA 接口见 `特性概述_76459525.md`（UNC 侧 WSFD-104004 "与其他特性的交互-依赖 Radius功能"）[EV-FK-09]

---

## 4. 配置规则

### 4.1 激活步骤（5 种变体的统一抽象）

IPv6 PD 特性的激活流程按"外部分配 vs 本地地址池"两大类、本地地址池再细分为 4 种地址分配规则，共 5 种激活变体：

```
通用前置（所有变体）
  └── SET LICENSESWITCH:LICITEM="LKV3G5P6PD01",SWITCH=ENABLE

变体分类：
├── 【变体1：外部网元地址分配】（SMF/RADIUS 决策地址）
│   ├── （可选）白名单检测：ADD VPNINST/POOLGROUP/POOL(EXTERNAL)/SECTION/POOLBINDGROUP/APN/POOLGRPMAP
│   └── 手机下行路由：ADD OSPFV3/OSPFV3AREA/OSPFV3INTERFACE/OSPFV3IMPORTROUTE
│
├── 【变体2：本地地址池 - 基于 APN/DNN】（UPF 本地池，APN 映射）
│   ├── ADD VPNINST/APN
│   ├── SET APNADDRESSATTR（SUPPORTIPV4=ENABLE, SUPPORTIPV6=ENABLE）
│   ├── ADD POOL(LOCAL)/SECTION(V6PREFIXLENGTH=63 ★)/POOLGROUP/POOLBINDGROUP
│   ├── （可选）ADD CONFLICTIPV6
│   ├── ADD POOLGRPMAP（APN→POOLGROUP）
│   ├── SET IPALLOCRULE（FIRSTRULE=APN-1&LOCATION-0&SMF-0）
│   └── 手机下行路由（OSPFv3 系列，同变体1）
│
├── 【变体3：本地地址池 - 基于 SMF】（UPF 本地池，SMF 映射）
│   ├── 同变体2前置
│   ├── ADD CPNODEID（SMF NodeID）
│   ├── ADD POOLGRPMAP（SMF→POOLGROUP）
│   ├── SET IPALLOCRULE（FIRSTRULE=APN-0&LOCATION-0&SMF-1）
│   ├── SET IPALLOCBYSMFGLBSW（SWITCH=ENABLE）
│   └── 手机下行路由（OSPFv3 系列）
│
├── 【变体4：本地地址池 - 基于 SMF+APN/DNN】（UPF 本地池，SMF+APN 组合映射）
│   ├── 同变体3前置（支持多 APN/多 POOLGROUP）
│   ├── ADD POOLGRPMAP（SMF+APN→POOLGROUP，可配置多组映射）
│   ├── SET IPALLOCRULE（FIRSTRULE=APN-1&LOCATION-0&SMF-1, SECONDRULE=APN-0&LOCATION-0&SMF-1）
│   ├── SET IPALLOCBYSMFGLBSW（SWITCH=ENABLE）
│   └── 手机下行路由（OSPFv3 系列）
│
└── 【变体5：本地地址池 - 基于位置】（UPF 本地池，LAC/TAC 位置映射）
    ├── 同变体2前置
    ├── （可选）ADD TACGROUP/S1TACID/N2TACID（TAC 位置）
    ├── ADD LACGROUP/LACID（LAC 位置）
    ├── ADD POOLGRPMAP（LOCATIONGRP→POOLGROUP）
    ├── SET IPALLOCRULE（FIRSTRULE=APN-0&LOCATION-1&SMF-0）
    ├── SET IPALLOCBYLOCGLBSW（SWITCH=ENABLE）
    ├── 手机下行路由（IPv4 侧 OSPF + OSPFIMPORTROUTE，因 IPv4+IPv6 混合）
    └── （可选）ADD ADRLOCWHITELST（白名单，不参与位置分配）
```

> ★ 关键观察：
> - **变体1-4 的下行路由用 OSPFv3**（纯 IPv6 PD 用户），**变体5 用 OSPF**（IPv4，因位置分配场景 SUPPORTIPV4+SUPPORTIPV6 双栈，IPv4 侧需 OSPF）。
> - 变体2-5 共享本地地址池体系（POOL/SECTION/POOLGROUP/POOLGRPMAP），与 GWFD-010105 的地址池体系完全复用，**唯一区别是 V6PREFIXLENGTH<64**。
> - 变体5 是唯一跨 GWFD-020406 + GWFD-020421（基于位置的地址分配）的混合场景，License 实际激活脚本使用 LKV3G5LBAA01（基于位置）而非 LKV3G5P6PD01（见 §8 一致性说明）。

> 来源：`激活外部网元地址分配的IPv6 Prefix Delegation功能_80269177.md`（操作步骤3步）[EV-FK-04]；`基于APN_DNN分配地址_80250128.md`（操作步骤6步）[EV-FK-05]；`基于SMF分配地址_80250129.md`（操作步骤7步）[EV-FK-06]；`基于SMF+APN_DNN分配地址_80250130.md`（操作步骤7步）[EV-FK-07]；`基于位置分配地址_52579205.md`（操作步骤10步）[EV-FK-08]

### 4.2 MML命令清单

#### 4.2.1 本特性参考信息列出的 MML 命令（5条，全为地址池体系）

| 命令 | 用途 | IPv6 PD 场景关联 |
|------|------|----------------|
| ADD POOL | 增加地址池 | **POOLTYPE=EXTERNAL/LOCAL 二选一；V6PREFIXLENGTH<64 为 PD 标志** |
| ADD SECTION | 增加地址段 | **V6PREFIXLENGTH=49~63 为 PD 标志** |
| ADD POOLGROUP | 增加地址池组 | 组织多个 POOL，IPV6ALLOCPRIALG 使能优先级 |
| ADD POOLBINDGROUP | 绑定地址池到地址池组 | 按优先级绑定（PRIORITY 参数） |
| ADD POOLGRPMAP | 增加地址池组映射关系 | APN/SMF/LOCATION → POOLGROUP 映射 |

> ★ 对比 GWFD-020401（参考信息列 5 条 OSPFv3 命令）：GWFD-020406 参考信息列 5 条地址池命令。两者命令集**完全不重叠**，证实"承载基础设施（路由发布） vs 前缀代理（地址池体系）"的职责分工。PD 激活脚本同时使用两套命令（地址池 + OSPFv3），是"叠加"关系。

> 来源：`GWFD-020406 IPv6 Prefix Delegation参考信息_79370035.md`（"命令"章节）[EV-FK-02]

#### 4.2.2 激活脚本实际使用的命令（按变体统计）

| 变体 | 命令数 | 命令清单 |
|------|--------|---------|
| 变体1（外部分配） | ~11 | SET LICENSESWITCH, ADD VPNINST, ADD POOLGROUP, ADD POOL(EXTERNAL), ADD SECTION, ADD POOLBINDGROUP, ADD APN, ADD POOLGRPMAP, ADD OSPFV3, ADD OSPFV3AREA, ADD OSPFV3INTERFACE, ADD OSPFV3IMPORTROUTE |
| 变体2（APN/DNN） | ~14 | 变体1 + SET APNADDRESSATTR, ADD CONFLICTIPV6, SET IPALLOCRULE（POOL 改 LOCAL） |
| 变体3（SMF） | ~17 | 变体2 + ADD CPNODEID, SET IPALLOCBYSMFGLBSW |
| 变体4（SMF+APN） | ~19 | 变体3（多 POOL/POOLGROUP/POOLGRPMAP，多级 IPALLOCRULE） |
| 变体5（位置） | ~17 | 变体2 + ADD LACGROUP, ADD LACID, SET IPALLOCBYLOCGLBSW, ADD ADRLOCWHITELST；下行路由改 OSPF 系列（ADD OSPF/OSPFAREA/OSPFNETWORK/OSPFIMPORTROUTE） |

> 来源：各激活文档"任务示例-脚本"章节 [EV-FK-04]~[EV-FK-08]

### 4.3 参数说明（★ 核心参数）

#### 4.3.1 SET LICENSESWITCH 关键参数

| 参数 | 取值 | 说明 |
|------|------|------|
| LICITEM | LKV3G5P6PD01 | 固定取值，IPv6 PD License 项 |
| SWITCH | ENABLE | 固定取值，打开开关 |

#### 4.3.2 ADD POOL 关键参数（★ PD 标志）

| 参数 | 取值样例 | 说明 |
|------|---------|------|
| POOLNAME | testpool | 本端规划，地址池名 |
| **POOLTYPE** | **EXTERNAL / LOCAL** | **★ 外部分配场景=EXTERNAL；本地池场景=LOCAL** |
| IPVERSION | IPV6 | 固定，PD 仅支持 IPv6 |
| CHECKIPVALID | ENABLE | 外部场景白名单检测（可选） |
| HASVPN | ENABLE | 绑定 VPN |
| VPNINSTANCE | vpn1 | 与 APN/外联口 VPN 一致 |

#### 4.3.3 ADD SECTION 关键参数（★★ PD 核心标志）

| 参数 | 取值样例 | 说明 |
|------|---------|------|
| POOLNAME | testpool | 关联的地址池 |
| SECTIONNUM | 1 | 地址段号 |
| IPVERSION | IPV6 | 固定 |
| V6PREFIXSTART | fc00:0000:0000:fcee:0000:0000:0000:0000 | 全网规划，起始地址 |
| V6PREFIXEND | fc00:0000:0000:fcef:ffff:ffff:ffff:ffff | 全网规划，结束地址 |
| **V6PREFIXLENGTH** | **63（示例）/ 49~63** | **★★ 全网规划，前缀长度范围 49~64；当前缀长度小于 64 时，则表示该地址池采用 IPv6 Prefix Delegation 方式分配（PD 唯一配置标志）** |

#### 4.3.4 SET APNADDRESSATTR 关键参数

| 参数 | 取值 | 说明 |
|------|------|------|
| APN | apn-test2 | 关联 APN |
| SUPPORTIPV4 | ENABLE | 支持 IPv4（双栈） |
| SUPPORTIPV6 | ENABLE | 支持 IPv6（PD 必备） |

#### 4.3.5 ADD POOLGRPMAP 关键参数（映射规则多变体）

| 参数 | 变体2(APN) | 变体3(SMF) | 变体4(SMF+APN) | 变体5(LOCATION) |
|------|-----------|-----------|---------------|----------------|
| MAPPINGNAME | mapping1 | mapping3 | mapping3/mapping30 | mapping1 |
| APN | apn-test2 | - | apn-test3 / - | - |
| SMF | - | smfnode1 | smfnode1 | - |
| LOCATIONGRPTYPE | - | - | - | LAC |
| LOCATIONGRPNAME | - | - | - | lac1 |
| POOLGROUPNAME | poolgroup1 | poolgroup3 | poolgroup3/poolgroup30 | poolgroup1 |

#### 4.3.6 SET IPALLOCRULE 关键参数（地址分配规则）

| 参数 | 变体2(APN) | 变体3(SMF) | 变体4(SMF+APN) | 变体5(LOCATION) |
|------|-----------|-----------|---------------|----------------|
| FIRSTRULESW | ENABLE | ENABLE | ENABLE | ENABLE |
| **FIRSTRULE** | **APN-1&LOCATION-0&SMF-0** | **APN-0&LOCATION-0&SMF-1** | **APN-1&LOCATION-0&SMF-1** | **APN-0&LOCATION-1&SMF-0** |
| SECONDRULESW | DISABLE | DISABLE | ENABLE | DISABLE |
| SECONDRULE | - | - | APN-0&LOCATION-0&SMF-1 | - |
| THIRDRULESW | DISABLE | DISABLE | DISABLE | DISABLE |

> 规则含义：`APN-x&LOCATION-y&SMF-z` 中 x/y/z=1 表示启用该维度匹配，0 表示不启用。例：`APN-1&LOCATION-0&SMF-1` = 按"APN+SMF"组合映射地址池组。

#### 4.3.7 ADD OSPFV3 / OSPFV3IMPORTROUTE 关键参数（PD 增强）

| 参数 | 取值样例 | 说明（PD 场景约束） |
|------|---------|-------------------|
| PROCID | 6 | 本端规划，OSPFv3 进程号 |
| ROUTERID | 10.8.25.1 | **全网规划，Router ID 必须全网唯一** |
| VRFNAME | vpn1 | 全网规划 |
| BFDALLINTFFLG | TRUE | 使能 BFD（PD 增强，020401 无此参数） |
| **VPNINSCAPSIMFLG** | **TRUE** | **固定取值：去使能 VPN 路由环路检测；必须配置，否则 OSPFv3 路由引入失败（PD 增强）** |
| VIRTUALSYSFLAG | TRUE | 共网段虚拟系统使能（共网段组网必备） |
| AREAID | 0.0.0.5 | 与对端协商 |
| IFNAME | Eth-trunk1.1 | 全网规划，外联口 |
| DRPRI | 0 | 不参与 DR/BDR 选举（避免 VNF 被选） |
| TOPOID | 0 | 全网规划 |
| **PROTOCOL** | **wlr** | **本端规划，引入 WLR 路由（继承 020401 约束）** |

### 4.4 告警、软参与测量指标

| 项 | 文档声明 |
|----|---------|
| 告警 | 本特性无相关告警 |
| 软参 | 本特性无相关软参 |
| **测量指标** | **3 个 PD 专属指标**（★ 与 020401 无指标不同）：1) 用户平面当前在线 IPv6 PD 会话数；2) 用户平面平均在线 IPv6 PD 会话数；3) 用户平面最大在线 IPv6 PD 会话数 |

> ★ 关键发现：PD 特性虽无告警/软参，但**有 3 个专属测量指标**（会话数当前/平均/最大），可用于 PD 容量规划与监控。UNC 侧规格：整机支持无线路由器同时在线最大数 20,000；单用户最大支持手机后路由网段数 30。

> 来源：`GWFD-020406 IPv6 Prefix Delegation参考信息_79370035.md`（"告警"、"软参"、"测量指标"章节）[EV-FK-02]；UNC 规格见 `特性概述_76459525.md`[EV-FK-09]

### 4.5 约束条件

| 约束类型 | 约束内容 |
|---------|---------|
| License 强制要求 | 必须加载 82200CKF LKV3G5P6PD01 并通过 SET LICENSESWITCH 打开开关 |
| **GWFD-020401 前置（★ 强制依赖）** | **必须先开启 GWFD-020401 IPv6 承载上下文（82209828），否则 PD 无法建立承载** |
| GWFD-020403 前置（条件依赖） | 若 PD 用户为 IPv4v6 双栈且需业务解析，必须先开启 GWFD-020403（82209829） |
| **V6PREFIXLENGTH PD 标志** | **ADD SECTION 的 V6PREFIXLENGTH 取值 49~63（<64）即表示 PD 方式；=64 为普通 IPv6 单栈** |
| 本地池同 APN 前缀长度一致 | 本地地址池方式分配时，同一 APN 下的 IPv6 delegated-prefix 长度必须相同 |
| 外部分配同 APN 前缀长度可异 | 外部网元（SMF/RADIUS）分配时，同一 APN 下的前缀长度可以不同 |
| DHCP Server 不支持 | IPv6 PD 功能不支持从 DHCP Server 获取并分配 IPv6 delegated-prefix |
| 单 UE 单 delegated-prefix | DHCPv6 Solicit 多 IA_PD option 时，仅第一个分配，其余返回 NoPrefixAvail |
| delegated-prefix 永久有效 | T1/T2/preferred-lifetime/valid-lifetime 固定 0xFFFFFFFF，不需更新 |
| VPN 三者一致 | 地址池/APN/外联口 VPN 实例必须一致 |
| Router ID 全网唯一 | OSPFv3 ROUTERID 必须全网唯一 |
| VPNINSCAPSIMFLG 固定 TRUE | 必须去使能 VPN 路由环路检测，否则 OSPFv3 路由引入失败 |
| WLR 路由发布完整性 | OSPFV3IMPORTROUTE PROTOCOL=wlr，不能只选 wlr_sp/wlr_ud（继承 020401） |
| **5 条互斥约束** | **与 L2TP VPN、用户面地址自动检测、NAT、入不转板、通用DNN漫游分流互斥**（手机后路由用户） |
| APN/DNN 与 C 面一致 | UDG 本端 APN/DNN 实例应与 C 面（SMF/SGW-C/PGW-C）一致 |

---

## 5. 配置案例

### 5.1 典型场景1：外部网元地址分配的 IPv6 PD（SMF/RADIUS 决策地址）

**场景描述**：运营商支持基于外部网元（SMF/AAA）为 UE 分配地址时激活本特性。SMF/PGW-C 在 PFCP 请求中携带 IPv6D + Address + Prefix Bits，UDG 透传并建立 PD 承载。

**配置步骤和 MML 命令序列（原样保留文档脚本）**：

```
//配置外部地址分配时的白名单检测功能。

ADD VPNINST:VPNINSTANCE="vpn1";

ADD POOLGROUP: POOLGRPNAME="poolgroup1";

ADD POOL
:POOLNAME="testpool",POOLTYPE=EXTERNAL,IPVERSION=IPV6,CHECKIPVALID=ENABLE,HASVPN=ENABLE,VPNINSTANCE="vpn1";
ADD SECTION:POOLNAME="testpool",SECTIONNUM=1,IPVERSION=IPV6,V6PREFIXSTART="fc00:0000:0000:fcee:0000:0000:0000:0000",V6PREFIXEND="fc00:0000:0000:fcef:ffff:ffff:ffff:ffff", V6PREFIXLENGTH=63;

ADD POOLBINDGROUP:POOLGROUPNAME="poolgroup1", POOLNAME="testpool";

ADD APN
:APN="apn-test",HASVPN=ENABLE,VPNINSTANCE="vpn1";

ADD POOLGRPMAP: MAPPINGNAME="mapping1", APN="apn-test", POOLGROUPNAME="poolgroup1";

//配置手机下行路由。

ADD OSPFV3:PROCID=6,VRFNAME="vpn1",ROUTERID="10.8.25.1",BFDALLINTFFLG=TRUE,VPNINSCAPSIMFLG=TRUE,VIRTUALSYSFLAG=TRUE;

ADD OSPFV3AREA:PROCID=6,AREAID="0.0.0.5";

ADD OSPFV3INTERFACE:PROCID=6,AREAID="0.0.0.5",IFNAME="Eth-trunk1.1",DRPRI=0,VIRTUALSYSFLAG=TRUE, CFGROUTERIDFLAG=FALSE;

ADD OSPFV3IMPORTROUTE:PROCID=6,TOPOID=0,PROTOCOL=wlr;
```

> 来源：`激活外部网元地址分配的IPv6 Prefix Delegation功能_80269177.md`（"任务示例-脚本"章节，原样保留）[EV-FK-04]

**脚本要点解读**：

| 配置片段 | IPv6 PD 语义 |
|---------|---------|
| `ADD POOL POOLTYPE=EXTERNAL` | **外部地址分配场景标志**（SMF/AAA 决策地址） |
| `ADD SECTION V6PREFIXLENGTH=63` | **★★ PD 标志：前缀长度 < 64 表示 PD 方式分配** |
| `CHECKIPVALID=ENABLE` | 开启静态地址白名单检测（外部场景可选） |
| `ADD POOLGRPMAP APN→POOLGROUP` | APN 映射地址池组（无 SMF/LOCATION 维度） |
| `ADD OSPFV3 VPNINSCAPSIMFLG=TRUE` | **固定取值，去使能 VPN 环路检测（PD 增强）** |
| `ADD OSPFV3IMPORTROUTE PROTOCOL=wlr` | 引入 WLR 路由发布到骨干网 |

### 5.2 典型场景2：本地地址池基于 APN/DNN 分配的 IPv6 PD

**场景描述**：UPF/PGW-U 本地池为 UE 动态分配 IPv6 PD 地址，第一优先级按 APN 映射的地址范围分配。IPv6 地址 fc00:...:fcee:0:0:0:1/63 已使用，配置为冲突地址不参与分配。

**配置步骤和 MML 命令序列（原样保留文档脚本）**：

```
//打开本特性的License配置开关。

SET LICENSESWITCH:LICITEM="LKV3G5P6PD01",SWITCH=ENABLE;

//基于APN使能地址分配属性。

ADD VPNINST:VPNINSTANCE="vpn1";

ADD APN
:APN="apn-test2",HASVPN=ENABLE,VPNINSTANCE="vpn1";
SET APNADDRESSATTR:APN="apn-test2",SUPPORTIPV4=ENABLE,SUPPORTIPV6=ENABLE;

//配置地址池绑定到地址池组。

ADD POOL
:POOLNAME="testpool",POOLTYPE=LOCAL,IPVERSION=IPV6, HASVPN=ENABLE,VPNINSTANCE="vpn1";

ADD SECTION:POOLNAME="testpool",SECTIONNUM=1,IPVERSION=IPV6,V6PREFIXSTART="fc00:0000:0000:fcee:0000:0000:0000:0000",V6PREFIXEND="fc00:0000:0000:fcef:ffff:ffff:ffff:ffff", V6PREFIXLENGTH=63;

ADD POOLGROUP: POOLGRPNAME="poolgroup1", IPV4ALLOCPRIALG=ENABLE, IPV6ALLOCPRIALG=ENABLE;

ADD POOLBINDGROUP: POOLGROUPNAME="poolgroup1", POOLNAME="testpool", PRIORITY=10;
ADD CONFLICTIPV6:POOLNAME="testpool",V6PREFIX="fc00:0000:0000:fcee:0000:0000:0000:0001", V6PREFIXLENGTH=63;

//配置APN与地址池组的映射关系。

ADD POOLGRPMAP: MAPPINGNAME="mapping1", APN="apn-test2", POOLGROUPNAME="poolgroup1";

//配置地址分配规则。

SET IPALLOCRULE: FIRSTRULESW=ENABLE, FIRSTRULE=APN-1&LOCATION-0&SMF-0, SECONDRULESW=DISABLE, THIRDRULESW=DISABLE;

//配置手机下行路由。

ADD OSPFV3:PROCID=6,VRFNAME="vpn1",ROUTERID="10.8.25.1",BFDALLINTFFLG=TRUE,VPNINSCAPSIMFLG=TRUE,VIRTUALSYSFLAG=TRUE;

ADD OSPFV3AREA:PROCID=6,AREAID="0.0.0.5";

ADD OSPFV3INTERFACE:PROCID=6,AREAID="0.0.0.5",IFNAME="Eth-trunk1.1",DRPRI=0,VIRTUALSYSFLAG=TRUE, CFGROUTERIDFLAG=FALSE;

ADD OSPFV3IMPORTROUTE:PROCID=6,TOPOID=0,PROTOCOL=wlr;
```

> 来源：`基于APN_DNN分配地址_80250128.md`（"任务示例-脚本"章节，原样保留）[EV-FK-05]

**脚本要点解读**：

| 配置片段 | IPv6 PD 语义 |
|---------|---------|
| `SET LICENSESWITCH LKV3G5P6PD01` | 打开 PD License 开关（前置必配） |
| `ADD POOL POOLTYPE=LOCAL` | **本地地址池场景标志**（UPF 本地分配） |
| `ADD SECTION V6PREFIXLENGTH=63` | **★★ PD 标志** |
| `SET APNADDRESSATTR SUPPORTIPV4+SUPPORTIPV6=ENABLE` | APN 双栈支持（PD 用户多为双栈） |
| `ADD CONFLICTIPV6 V6PREFIXLENGTH=63` | 冲突地址配置（前缀长度必须与池一致） |
| `SET IPALLOCRULE FIRSTRULE=APN-1&LOCATION-0&SMF-0` | 第一优先级按 APN 映射分配 |

### 5.3 场景变体（4 种本地池 + 1 种外部）

| 变体 | 场景说明 | 核心差异（vs 变体2） |
|------|---------|--------------------|
| 变体1（外部） | SMF/AAA 决策地址 | POOLTYPE=EXTERNAL；无 SET APNADDRESSATTR；白名单检测可选 |
| 变体2（APN/DNN） | UPF 本地池，APN 映射 | POOLTYPE=LOCAL；FIRSTRULE=APN-1&LOCATION-0&SMF-0 |
| 变体3（SMF） | UPF 本地池，SMF 映射 | +ADD CPNODEID；+SET IPALLOCBYSMFGLBSW；FIRSTRULE=APN-0&LOCATION-0&SMF-1 |
| 变体4（SMF+APN） | UPF 本地池，SMF+APN 组合 | 多组 POOLGRPMAP；SECONDRULESW=ENABLE；支持多级回退 |
| 变体5（位置） | UPF 本地池，LAC/TAC 映射 | +ADD LACGROUP/LACID；+SET IPALLOCBYLOCGLBSW；+ADD ADRLOCWHITELST；**下行路由改 OSPF（IPv4 侧）**；License 用 LKV3G5LBAA01（见 §8） |

> ★ 关键对比：变体1-4 下行路由用 OSPFv3（纯 IPv6 PD），变体5 用 OSPF（IPv4，因位置场景双栈）。这是判定"是否混合场景"的配置树分水岭。

> 来源：`基于SMF分配地址_80250129.md`[EV-FK-06]；`基于SMF+APN_DNN分配地址_80250130.md`[EV-FK-07]；`基于位置分配地址_52579205.md`[EV-FK-08]

---

## 6. 验证与调测

### 6.1 验证方法

#### 6.1.1 调测前提与目的

用户激活分 IPv6 代理前缀时，需要调测该功能，确保用户可以正常接入。适用于 PGW-U、UPF。

**前提条件**：
- 已完成"激活外部网元地址分配的 IPv6 PD 功能"或"激活本地地址池分配的 IPv6 PD 功能"之一
- 已阅读特性根文档

#### 6.1.2 调测数据准备

| 类别 | 参数名称 | 取值样例 | 获取方法 |
|------|---------|---------|---------|
| 用户信息查询 | 用户IMSI（IMSI） | 460000123456789 | 测试终端自带 |
| 测试终端使用的APN | APN/DNN实例名（APN） | apn-test2 | 已配置数据中获取 |

工具：测试终端

#### 6.1.3 调测执行步骤

**步骤1**：打开接入侧/DN 侧镜像接口上的第三方抓包工具，准备抓取测试终端的出入报文。

**步骤2**：执行 `LST LICENSESWITCH` 命令，查询 IPv6 PD 的特性开关是否打开。

```
LST LICENSESWITCH: LICITEM="LKV3G5P6PD01";
```

判断规则：
- 如果 "SWITCH" 为 "ENABLE" → 执行步骤3
- 如果 "SWITCH" 为 "DISABLE" → 执行 `SET LICENSESWITCH:LICITEM="LKV3G5P6PD01",SWITCH=ENABLE;` 打开开关

**步骤3**：测试终端使用 "apn-test2" APN 发起接入网络请求。

**步骤4**：执行 `DSP SESSIONINFO` 命令，查看测试终端的 IP 地址是否在 UDG 本地规划的地址池内。

```
DSP SESSIONINFO:QUERYTYPE=IMSI,IMSI="460000123456789";
```

预期输出（原样保留文档示例）：

```
......
 -------------------------------
                                 IMSI  =  460000123456789
                                     ......         
                                    APN  =  apn-test2
                                     ......								
                               PDP Type  =  IPv6 
                                     ......    
                      IPv6 Address type  =  
  UPF ALLOC IP ADDRESS

                       IPv6 PDP address  =  fc00:0:0:fcee:0:0:0:0
                  IPV6 Delegated Prefix  =  
  fc00:0:0:fcee:0:0:0:0/63

                                     ......       
 (Number of results = 1)
---    END
```

判断规则：
- 如果测试终端激活成功，且使用的 "IPv6 PDP address" 和 **"IPV6 Delegated Prefix"** 在规划的地址池内 → 测试终端接入成功，调测结束
- 如果测试终端激活成功，但使用的 "IPv6 PDP address" 不在规划的地址池内 → 执行步骤5

**步骤5**：收集信息并寻求技术支持。
- a. 在 OM Portal 上创建用户跟踪任务并保存报文
- b. 执行 `EXP MML` 命令将当前配置数据导出为 MML 脚本文件并保存
- c. 收集并保存上述所有查询信息
- d. 收集归纳所有信息并联系华为技术支持解决

> 来源：`调测IPv6 Prefix Delegation_79370030.md`（"操作步骤"章节）[EV-FK-10]

### 6.2 验证要点（IPv6 PD 三字段判断）

与 GWFD-020401（IPv6 单栈二元组）、GWFD-020403（双栈三元组）不同，IPv6 PD 调测需**同时验证三个字段**：

| 验证字段 | 期望值 | 判读 |
|---------|-------|------|
| PDP Type | **IPv6** | 必须为 IPv6（PD 仅支持 IPv6 单栈承载，双栈业务解析另需 020403） |
| IPv6 PDP address | fc00:0:0:fcee:0:0:0:0（在池内） | 网段起始地址在 V6PREFIXLENGTH<64 的段内 |
| **IPV6 Delegated Prefix** | **fc00:0:0:fcee:0:0:0:0/63** | **★★ PD 专属字段：显示带前缀长度的 delegated-prefix，/63（或 49~63）确认为 PD 用户** |
| IPv6 Address type | UPF ALLOC IP ADDRESS | 标识地址由 UPF 本地分配（本地池场景） |

> ★ 对比：
> - GWFD-020401：二元组（PDP Type=IPv6 + IPv6 PDP address）
> - GWFD-020403：三元组（PDP Type=IPv4v6 + IPv4 PDP address + IPv6 PDP address）
> - **GWFD-020406：四字段（PDP Type=IPv6 + IPv6 PDP address + IPV6 Delegated Prefix + IPv6 Address type）**，其中 **IPV6 Delegated Prefix 是 PD 唯一标志**（带 /49~63 前缀长度）

### 6.3 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| 用户激活失败，PDP Type 不为 IPv6 | License 未加载或 SET LICENSESWITCH 未使能 | LST LICENSESWITCH 确认 LKV3G5P6PD01=ENABLE；LST LICENSE 确认 License 文件加载 |
| **IPV6 Delegated Prefix 为空** | **V6PREFIXLENGTH 配置为 64（未触发 PD）；或 DHCPv6 流程未完成** | **LST SECTION 确认 V6PREFIXLENGTH=49~63；抓包确认 DHCPv6 Solicit/Reply 流程** |
| PDP Type=IPv6 但前缀长度为 64 | ADD SECTION 的 V6PREFIXLENGTH 配置错误 | 修改 V6PREFIXLENGTH 为 49~63（<64） |
| IPv6 PDP address 不在池内 | 地址池映射规则错误（POOLGRPMAP/IPALLOCRULE 不匹配） | LST POOLGRPMAP 确认 APN/SMF/LOCATION 映射；LST IPALLOCRULE 确认规则 |
| 本地池同 APN 前缀长度不一致 | 违反应用限制（本地池方式同 APN 必须相同） | 统一同 APN 下所有 SECTION 的 V6PREFIXLENGTH |
| DHCPv6 Solicit 多 IA_PD 只分配一个 | 单 UE 单 delegated-prefix 约束（文档设计） | 预期行为，其他 IA_PD 返回 NoPrefixAvail |
| 双栈 PD 用户业务解析失败 | 未开启 GWFD-020403（条件依赖） | LST LICENSESWITCH 确认 LKV3G5VDSA01=ENABLE |
| OSPFv3 路由引入失败 | VPNINSCAPSIMFLG 未配置为 TRUE | 修改 ADD OSPFV3 VPNINSCAPSIMFLG=TRUE（固定取值） |
| OSPFv3 邻居异常 | VNF 被选为 DR/BDR | 确认 ADD OSPFV3INTERFACE DRPRI=0 |
| 下行路由只发布部分用户 | OSPFV3IMPORTROUTE 未用 wlr 而用了 wlr_sp/wlr_ud | 修改 PROTOCOL=wlr（继承 020401 约束） |
| PD 用户与 L2TP VPN 冲突 | 同 APN 下同时部署（互斥） | 二选一：PD 或 L2TP VPN |
| PD 用户 NAT 失败 | PD 用户不支持 NAT（互斥） | PD 用户不配置 NAT |
| 弱覆盖场景掉话率上升 | eNodeB 无法下发 RA 给终端（UNC 侧文档声明） | 参考 UNC 侧 WSFD-104004 对系统影响说明 |
| IPv6 Address type 显示非 UPF ALLOC | 外部场景由 SMF/AAA 分配（预期） | 外部分配场景下正常，非 UPF 本地分配 |

---

## 7. 参考信息

### 7.1 ★ 与其他特性的关系（IPv6 PD 协同全景）

| 关联特性 | 特性ID | 关系类型 | 关系说明（文档依据） |
|---------|--------|---------|-------------------|
| **IPv6 承载上下文** | **GWFD-020401（UDG）** | **★ 强制依赖（文档显式）** | **文档原文**：UDG 需要建立 IPv6 承载上下文，因此需开启 IPv6 承载上下文特性（82209828）。PD 建立在 020401 承载基础设施之上（详见 §7.2） |
| **IPv4v6 双栈接入** | **GWFD-020403（UDG）** | **条件依赖（文档显式）** | **文档原文**：如果需要对 IPv4v6 双栈接入用户的业务进行解析，则需要先开启 IPv4v6 双栈接入特性（82209829）。详见 §7.3 |
| 用户面地址分配 | GWFD-010105（UDG） | 地址池体系复用 | PD 复用 POOL/SECTION/POOLGROUP/POOLGRPMAP 地址池体系，仅通过 V6PREFIXLENGTH<64 区分 |
| 地址分配方式（父节点） | GWFD-010104（UDG） | 体系归类 | 地址分配方式总览，PD 属于地址分配体系下的 IPv6 功能分支 |
| 基于位置的地址分配 | GWFD-020421（UDG） | 混合场景 | 变体5（基于位置的 PD）跨 020406 + 020421，License 用 LKV3G5LBAA01 |
| 会话管理 | GWFD-010101（UDG） | 宿主流程 | PDU 会话建立是 PD 流程的宿主 |
| **IPv6 前缀代理（UNC 侧）** | **WSFD-104004（UNC）** | **★ C-U 协同（对应特性）** | **C 侧控制面决策（CHV6/IPv6D/Prefix Bits），U 侧（本特性）执行地址分配与路由转发**。详见 §7.4 |
| IPv6 承载上下文（UNC 侧） | WSFD-104001（UNC） | 控制面承载对应 | C 侧 IPv6 承载建立（PD 的承载前置） |
| IPv4v6 双栈接入（UNC 侧） | WSFD-104002（UNC） | 控制面双栈对应 | C 侧双栈使能（条件依赖的 C 侧对应） |
| L2TP VPN | GWFD-020412（UDG） | **互斥** | 同 APN 下 L2TP VPN 与手机后路由无需同时部署 |
| 用户面地址自动检测 | GWFD-010108（UDG） | **互斥** | 手机后路由用户不能做用户面地址自动检测 |
| NAT 基本功能 | （UDG） | **互斥** | 手机后路由用户不支持 NAT |
| 入不转板功能 | GWFD-020482（UDG） | **互斥** | 手机后路由用户不支持入不转板 |
| 通用 DNN 漫游分流 | GWFD-020531（UDG） | **互斥** | 手机后路由用户不支持通用 DNN 漫游分流 |

### 7.2 ★ GWFD-020406 与 GWFD-020401 的关系（文档显式强制依赖）

**结论：GWFD-020406（IPv6 PD）显式强制依赖 GWFD-020401（IPv6 承载上下文）。GWFD-020401 是 PD 的前置条件。**

#### 7.2.1 文档依据（GWFD-020406 原文）

GWFD-020406 的"与其他特性的交互"章节明确列出：

> | 依赖 | GWFD-020401 IPv6承载上下文 | 82209828 IPv6承载上下文 | UDG 需要建立 IPv6 承载上下文，因此需开启 IPv6 承载上下文特性。 |

> 来源：`GWFD-020406 IPv6 Prefix Delegation特性概述_79370029.md`（"与其他特性的交互"章节）[EV-FK-01]

#### 7.2.2 依赖关系定位

| 维度 | GWFD-020401（IPv6 承载上下文） | GWFD-020406（IPv6 PD） |
|------|------------------------------|----------------------|
| 核心职责 | **承载基础设施**：IPv6 承载的激活/去激活/更新、透明转发、下行路由发布 | **前缀代理**：UE 作为无线移动路由器，将 IPv6 前缀下发给 LAN 侧多终端 |
| License要求 | 82209828 LKV3G5V6PB01 | 82200CKF LKV3G5P6PD01 |
| 发布版本 | UDG 20.0.0 | UDG 20.5.0（晚于 020401） |
| IPv6 前缀长度 | 不涉及（由 010105 地址池决定，64 位为主） | **49~63**（< 64，PD 专用） |
| 适用 NF | SGW-U/PGW-U/UPF | **仅 PGW-U/UPF**（不含 SGW-U） |
| 参考信息命令 | 5 条 OSPFv3 路由命令 | 5 条地址池命令（POOL/SECTION 系列） |
| 测量指标 | 无 | 3 个 PD 专属会话数指标 |
| 文档显式依赖 | 无（向上不显式声明） | **显式依赖 GWFD-020401** |

#### 7.2.3 关系图

```
GWFD-020401 IPv6 承载上下文（License LKV3G5V6PB01，承载基础设施层）
   │
   │  提供 IPv6 承载基础设施：
   │  - IPv6 PDP上下文/EPS承载/PDU Session/QoS Flow 激活/去激活/更新
   │  - 用户面 IPv6 承载（透明转发）
   │  - RA 通告机制（与 PD 共享）
   │  - IPv6 下行路由发布基础（OSPFv3 + WLR）
   │
   ▼ 被依赖（GWFD-020406 文档显式声明，强制）
   │
GWFD-020406 IPv6 Prefix Delegation（License LKV3G5P6PD01，前缀代理层）
   │
   │  在 020401 基础上叠加：
   │  - UE 作为无线移动路由器
   │  - IPv6 前缀长度 < 64（49~63）
   │  - IPv6D flag + Prefix Delegation Bits field + DHCPv6 协商
   │  - 为 LAN 侧多终端下发独立 IPv6 地址前缀（家庭/小企业场景）
   │  - OSPFv3 增强（BFD/VIRTUALSYSFLAG/VPNINSCAPSIMFLG）
   │
   ▼
完整的 IPv6 移动路由器场景（家庭/小企业多终端接入）
```

#### 7.2.4 实践配置意义

部署 IPv6 PD 时，需**同时激活两个特性**：
1. 先激活 GWFD-020401（License LKV3G5V6PB01 + IPv6 承载基础设施）
2. 再激活 GWFD-020406（License LKV3G5P6PD01 + V6PREFIXLENGTH<64 的地址池 + DHCPv6 PD 协议交互）

PD 的前缀代理能力建立在 GWFD-020401 的 IPv6 承载之上；没有 020401 的承载基础设施，PD 的前缀代理无法落地为真正的用户承载。

### 7.3 ★ GWFD-020406 与 GWFD-020403 的关系（条件依赖）

**结论：GWFD-020406 与 GWFD-020403 是条件依赖关系。若 PD 用户为 IPv4v6 双栈且需业务解析，必须先开启 GWFD-020403。**

#### 7.3.1 文档依据

GWFD-020406 的"与其他特性的交互"章节：

> | 依赖 | GWFD-020403 IPv4v6双栈接入 | 82209829 IPv4v6双栈接入 | 如果需要对 IPv4v6 双栈接入用户的业务进行解析，则需要先开启 IPv4v6 双栈接入特性。 |

#### 7.3.2 前缀长度阈值与双栈切换的关键连接

| 场景 | IPv6 前缀长度 | 是否 PD | 是否双栈 | 需开启特性 |
|------|-------------|--------|---------|-----------|
| 普通 IPv6 单栈 | 64 | 否 | 否 | 020401 + 010105 |
| **IPv6 PD 单栈** | **49~63** | **是** | **否** | **020401 + 020406 + 010105** |
| IPv4v6 双栈（普通） | 64（IPv6 侧） | 否 | 是 | 020401 + 020403 + 010105 |
| **IPv4v6 双栈 PD** | **49~63（IPv6 侧）** | **是** | **是** | **020401 + 020403 + 020406 + 010105** |

> ★ 关键阈值：**V6PREFIXLENGTH = 64 是 PD 与非 PD 的分水岭；PDP Type = IPv4v6 是双栈与单栈的分水岭**。两者独立，可组合出 4 种场景。SET APNADDRESSATTR 中 SUPPORTIPV4=ENABLE + SUPPORTIPV6=ENABLE 标识双栈 APN，结合 V6PREFIXLENGTH<64 标识 PD，共同判定"双栈 PD"场景（需 4 个特性全开）。

### 7.4 ★ GWFD-020406（UDG）与 WSFD-104004（UNC）的 C-U 协同

**结论：GWFD-020406（U 侧 PD）与 WSFD-104004（C 侧 PD）构成 C-U 协同，通过 PFCP + ICMPv6 + DHCPv6 三类消息完成端到端 PD 流程。**

#### 7.4.1 C-U 职责分工

| 职责 | WSFD-104004（UNC/C 侧） | GWFD-020406（UDG/U 侧） |
|------|------------------------|------------------------|
| License | 82208006 LKV3W9V6PD11 | 82200CKF LKV3G5P6PD01 |
| 适用 NF | GGSN-C/SGW-C/PGW-C/SMF | PGW-U/UPF |
| 地址决策 | 本地池或 RADIUS 决策 IPv6 delegated-prefix | 透传（外部场景）或本地池分配（LOCAL 场景） |
| PFCP 请求信元 | 携带 CHV6 / IPv6D + Address + Prefix Bits | 解析信元，建立 PD 承载 |
| RA 通告 | - | UPF 向 UE 发送 Router Advertisement（O-flag=1） |
| DHCPv6 | 通过 PFCP Report 参与 | UPF 与 UE 直接 DHCPv6 Solicit/Reply 交互 |
| 下行路由 | - | OSPFv3 + IMPORTROUTE WLR 发布到骨干网 |
| 依赖 | WSFD-104001（承载）、WSFD-011306（Radius）、WSFD-104002（双栈） | GWFD-020401（承载）、GWFD-020403（双栈条件） |
| 标准 | 3GPP 23.214/29.244 + RFC 2865（RADIUS） | 3GPP 23.060/29.244 + RFC 3315（DHCPv6） |

#### 7.4.2 C-U 协同三次关键信元交互（P1/P2/P3）

基于 5GC/EPC/GPRS-UMTS 三个业务流程文档（内容一致，仅网元名不同）：

| 协同点 | 方向 | 消息 | 信元 | 决策方 |
|--------|------|------|------|--------|
| **P1** | AAA Server → SMF/PGW-C | 鉴权响应 | IPv6D=1 + IPv6 Address + Prefix Bits | AAA Server（外部场景） |
| **P2** | SMF/PGW-C → UPF/PGW-U | PFCP Session Establishment Request | IPv6D=1（外部场景）或 CHV6=1（本地场景） + Address + Prefix Bits | SMF/PGW-C |
| **P3** | UPF/PGW-U → SMF/PGW-C | PFCP Session Establishment Response | IPv6D=1 + Address + Prefix Bits（本地场景由 UPF 填充） | UPF/PGW-U（本地场景）或透传（外部场景） |

> ★ C-U 协同本质：C 侧决策"是否 PD、前缀多长"，U 侧执行"分配哪个具体前缀、如何路由"。两者通过 UE IP Address 信元的 IPv6D/CHV6/Prefix Bits 三字段完成意图传递。

#### 7.4.3 C-U 依赖对称性观察

| 依赖项 | C 侧（WSFD-104004） | U 侧（GWFD-020406） | 对称性 |
|--------|---------------------|---------------------|--------|
| IPv6 承载上下文 | 依赖 WSFD-104001 | 依赖 GWFD-020401 | ★ 对称（C-U 两侧都强制依赖各自承载特性） |
| 双栈接入 | 依赖 WSFD-104002（条件） | 依赖 GWFD-020403（条件） | ★ 对称（条件依赖对称） |
| Radius 功能 | **依赖 WSFD-011306（强制）** | 无（U 侧不直接交互 AAA） | ★ 不对称（C 侧独有，因 RADIUS 鉴权在 C 面） |

> ★ 关键发现：C-U 两侧的承载依赖和双栈依赖**完全对称**，但 **RADIUS 依赖仅 C 侧强制**（U 侧不直接与 AAA 交互，通过 PFCP 间接受益）。这反映了"C 面负责鉴权与外部地址决策、U 面负责本地分配与转发"的职责分工。

### 7.5 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 | evidence_id |
|------|---------|-------------|-------------|
| 1 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020406 IPv6 Prefix Delegation_79370033.md` | 特性根索引文件（仅标题，无实质内容） | - |
| 2 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020406 IPv6 Prefix Delegation/GWFD-020406 IPv6 Prefix Delegation特性概述_79370029.md` | 适用NF（PGW-U/UPF + PGW-C/SMF + MS/UE + AAA）、定义（IPv6移动路由器）、客户价值、应用场景（IPv6组网多终端接入）、可获得性（License 82200CKF LKV3G5P6PD01、UDG 20.5.0+）、**与其他特性交互（7条：2依赖+5互斥）**、对系统影响（可忽略）、应用限制（V6PREFIXLENGTH 49~63、本地池同APN一致）、原理概述（双场景+UE IP Address信元）、计费话单（不涉及）、特性规格（无）、遵循标准（RFC 3315 + 3GPP 23.060/29.244）、发布历史（01@20.5.0） | EV-FK-01 |
| 3 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/IPv6功能/GWFD-020406 IPv6 Prefix Delegation/GWFD-020406 IPv6 Prefix Delegation参考信息_79370035.md` | **MML命令清单（5条：ADD POOL/SECTION/POOLGROUP/POOLBINDGROUP/POOLGRPMAP，全为地址池体系）**、告警（无）、软参（无）、**测量指标（3个PD专属会话数指标）** | EV-FK-02 |
| 4 | `UDG_Product_Documentation_CH_20.15.2/.../GWFD-020406 IPv6 Prefix Delegation/实现原理/5GC业务流程_79707829.md` | **5GC PD业务流程（21步两阶段）**：PDU会话建立+PFCP协商（步骤1-12）+DHCPv6地址分配（步骤13-21）；P1/P2/P3三次信元协同；IA_PD/Rapid Commit/Prefix Exclude option说明；T1/T2/lifetime固定0xFFFFFFFF；UE为LAN终端分配64位前缀 | EV-FK-03 |
| 5 | `UDG_Product_Documentation_CH_20.15.2/.../GWFD-020406 IPv6 Prefix Delegation/实现原理/EPC业务流程_79707828.md` | EPC PD业务流程（22步，结构与5GC一致，网元为MME/SGW/PGW-C/PGW-U） | EV-FK-04 |
| 6 | `UDG_Product_Documentation_CH_20.15.2/.../GWFD-020406 IPv6 Prefix Delegation/实现原理/GPRS_UMTS业务流程_79707827.md` | GPRS/UMTS PD业务流程（21步，网元为SGSN/PGW-C/PGW-U/MS） | EV-FK-05 |
| 7 | `UDG_Product_Documentation_CH_20.15.2/.../GWFD-020406 IPv6 Prefix Delegation/激活外部网元地址分配的IPv6 Prefix Delegation功能_80269177.md` | **变体1激活（外部分配）**：操作场景、数据（EXTERNAL池+V6PREFIXLENGTH=63+OSPFv3全套参数含BFDALLINTFFLG/VPNINSCAPSIMFLG/VIRTUALSYSFLAG）、操作步骤3步、任务示例脚本（11条MML） | EV-FK-06 |
| 8 | `UDG_Product_Documentation_CH_20.15.2/.../GWFD-020406 IPv6 Prefix Delegation/激活本地地址池分配的IPv6 Prefix Delegation功能/基于APN_DNN分配地址_80250128.md` | **变体2激活（APN/DNN）**：LOCAL池+APNADDRESSATTR+IPALLOCRULE(APN-1&LOCATION-0&SMF-0)+CONFLICTIPV6+OSPFv3；操作步骤6步；脚本（14条MML） | EV-FK-07 |
| 9 | `UDG_Product_Documentation_CH_20.15.2/.../GWFD-020406 IPv6 Prefix Delegation/激活本地地址池分配的IPv6 Prefix Delegation功能/基于SMF分配地址_80250129.md` | **变体3激活（SMF）**：CPNODEID+IPALLOCRULE(APN-0&LOCATION-0&SMF-1)+IPALLOCBYSMFGLBSW；操作步骤7步；脚本（17条MML） | EV-FK-08 |
| 10 | `UDG_Product_Documentation_CH_20.15.2/.../GWFD-020406 IPv6 Prefix Delegation/激活本地地址池分配的IPv6 Prefix Delegation功能/基于SMF+APN_DNN分配地址_80250130.md` | **变体4激活（SMF+APN）**：多POOLGRPMAP+多级IPALLOCRULE(FIRSTRULE=APN-1&LOCATION-0&SMF-1, SECONDRULE=APN-0&LOCATION-0&SMF-1)；操作步骤7步；脚本（19条MML） | EV-FK-09 |
| 11 | `UDG_Product_Documentation_CH_20.15.2/.../GWFD-020406 IPv6 Prefix Delegation/激活本地地址池分配的IPv6 Prefix Delegation功能/基于位置分配地址_52579205.md` | **变体5激活（位置）**：LACGROUP/LACID+IPALLOCBYLOCGLBSW+ADRLOCWHITELST；**下行路由改OSPF（IPv4侧）**；前提条件指向GWFD-020421；License用LKV3G5LBAA01；操作步骤10步；脚本（17条MML） | EV-FK-10 |
| 12 | `UDG_Product_Documentation_CH_20.15.2/.../GWFD-020406 IPv6 Prefix Delegation/调测IPv6 Prefix Delegation_79370030.md` | 调测方法：LST LICENSESWITCH + DSP SESSIONINFO；**PD四字段验证（PDP Type=IPv6 + IPv6 PDP address + IPV6 Delegated Prefix + IPv6 Address type）**；预期输出示例（fc00:0:0:fcee:0:0:0:0/63）；故障收集EXP MML | - |
| 13（交叉引用，C 侧） | `output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-104004 IPv6前缀代理/特性概述_76459525.md` | **★ C-U 协同关键交叉引用**：UNC 侧 PD 特性概述，License 82208006 LKV3W9V6PD11；适用 NF（GGSN-C/SGW-C/PGW-C/SMF）；**依赖 WSFD-104001（承载）+ WSFD-011306（Radius，强制）+ WSFD-104002（双栈，条件）**；原理（Radius方式/本地池方式两种）；规格（整机20000无线路由器，单用户30网段）；遵循标准（3GPP 23.214/29.244 + RFC 2865 RADIUS） | EV-FK-09 |

> 注：source_evidence_ids 字段使用 EV-FK-01 ~ EV-FK-10 占位（对应序号 2-11 的 10 个 UDG 侧核心文档），C 侧交叉引用（序号13）供 §7.4 C-U 协同分析使用。

### 7.6 关键术语（汇总）

| 术语 | 全称 | 说明 |
|------|------|------|
| IPv6 PD | IPv6 Prefix Delegation | IPv6 前缀代理，UE 作为无线移动路由器下发前缀 |
| Routing Behind MS | 手机后路由 | MS/UE 后挂多终端的路由方案（IPv4 版本），PD 是 IPv6 版本 |
| IPv6 delegated-prefix | IPv6 代理前缀 | 下发给 UE 的网段地址，前缀 49~63（<64） |
| IPv6D flag | IPv6 Delegation 标志位 | UE IP Address 信元中标识 PD 的标志 |
| CHV6 | Choose IPv6 | SMF 请求 UPF 本地分配 IPv6 的标志 |
| Prefix Delegation Bits field | PD 前缀长度字段 | UE IP Address 信元中指示前缀长度（49~63） |
| IA_PD option | Identity Association for PD | DHCPv6 申请 delegated-prefix 的选项 |
| Rapid Commit option | DHCPv6 快速提交 | 携带则两步流程，否则四步 |
| Prefix Exclude Option | 前缀排除 | delegated-prefix 段中一个前缀作链路地址 |
| O-flag | RA Other-config flag | RA 中置 1 表示后续可 DHCPv6 获取参数 |
| WLR | White Label Route | UDG 内部用户下行路由，通过 OSPFv3 IMPORTROUTE 发布 |
| OSPFv3 | OSPF version 3 | IPv6 专用 OSPF（PD 纯 IPv6 下行路由） |
| OSPF | OSPF version 2 | IPv4 OSPF（位置场景 IPv4+IPv6 混合下行路由） |
| V6PREFIXLENGTH | IPv6 前缀长度 | **★ PD 标志：< 64（49~63）为 PD；= 64 为普通 IPv6** |
| LKV3G5P6PD01 | IPv6 PD License（U 侧） | License 82200CKF，本特性强制要求 |
| LKV3W9V6PD11 | IPv6 前缀代理 License（C 侧） | License 82208006，UNC 侧 WSFD-104004 强制要求 |
| VPNINSCAPSIMFLG | VPN 路由环路检测去使能 | **固定 TRUE**，否则 OSPFv3 路由引入失败 |

---

## 8. 文档一致性说明（配置树 vs 产品文档）

> 配置树仅用于定位特性ID，以下记录以产品文档实际内容为准时发现的潜在不一致或重点澄清，供 Stage 3 横向分析参考。

| # | 维度 | 配置树/文档清单描述 | 产品文档实际内容 | 差异类型 |
|---|------|---------------------|-----------------|---------|
| 1 | 适用 NF | 文档清单标注"UDG/UPF" | 产品文档适用 NF 明确**仅 PGW-U、UPF**（不含 SGW-U），与 GWFD-020401（含 SGW-U）不同 | ★ 范围澄清（PD 仅锚定用户面） |
| 2 | 与GWFD-020401关系 | 配置树未呈现 | **★ GWFD-020406 文档显式强制依赖 GWFD-020401**（UDG 需要建立 IPv6 承载上下文）；020401 是 PD 前置条件 | ★ 显式依赖（见 §7.2） |
| 3 | 与GWFD-020403关系 | 配置树未呈现 | **★ GWFD-020406 文档显式条件依赖 GWFD-020403**（若双栈用户需业务解析）；V6PREFIXLENGTH=64 是 PD/非PD分水岭，PDP Type=IPv4v6 是双栈分水岭，两者独立组合 | ★ 条件依赖（见 §7.3） |
| 4 | 与WSFD-104004关系（C-U） | 配置树未呈现 | **★ C-U 协同**：C 侧 WSFD-104004 决策（CHV6/IPv6D/Prefix Bits），U 侧 GWFD-020406 执行；承载依赖和双栈依赖 C-U 对称，RADIUS 依赖仅 C 侧强制 | ★ C-U 协同（见 §7.4） |
| 5 | 互斥特性 | 配置树未呈现 | **★ 5 条互斥**（L2TP VPN、用户面地址自动检测、NAT、入不转板、通用DNN漫游分流），原因统一为"手机后路由用户"约束 | ★ 互斥约束丰富 |
| 6 | 前缀长度阈值 | 文档清单标注"IPv6前缀代理(PD)" | 产品文档：V6PREFIXLENGTH 范围 49~64，**< 64（即 49~63）为 PD 标志**；应用限制原文"49~64之间，不包含64位" | ★ 阈值澄清（=64 为普通 IPv6，非 PD） |
| 7 | 双栈 PD 切换 | 配置树未呈现 | SET APNADDRESSATTR SUPPORTIPV4+SUPPORTIPV6=ENABLE + V6PREFIXLENGTH<64 共同判定"双栈 PD"场景，需 020401+020403+020406+010105 四特性全开 | ★ 场景组合澄清 |
| 8 | MML命令体系 | （无配置树描述） | 参考信息列 5 条地址池命令（POOL 系列）；激活脚本实际使用 11~19 条（变体差异）；**与 GWFD-020401 的 5 条 OSPFv3 命令完全不重叠**，证实职责分工 | 文档内部分工明确 |
| 9 | 测量指标 | （无配置树描述） | **3 个 PD 专属会话数指标**（当前/平均/最大在线 IPv6 PD 会话数），与 GWFD-020401（无指标）不同；UNC 侧规格：整机 20000 无线路由器，单用户 30 网段 | PD 专属容量指标 |
| 10 | 遵循标准集 | （无配置树描述） | U 侧：RFC 3315（DHCPv6）+ 3GPP 23.060/29.244（3条）；C 侧：3GPP 23.214/29.244 + RFC 2865（RADIUS）（3条）；**U 侧重 DHCPv6，C 侧重 RADIUS**，标准集互补 | C-U 标准对称性 |
| 11 | 变体5 License 不一致 | 变体5 属于 GWFD-020406 激活文档 | **变体5（基于位置）激活脚本使用 `SET LICENSESWITCH:LICITEM="LKV3G5LBAA01"`（基于位置的地址分配 License），而非 LKV3G5P6PD01（PD License）**；前提条件指向 GWFD-020421 而非 GWFD-020406 根文档 | ★★ 潜在文档错误或混合场景设计，Stage 3 需澄清：变体5 是否实际属于 GWFD-020421 的 IPv6 扩展而非 GWFD-020406？ |
| 12 | RA 机制归属 | （无配置树描述） | PD 业务流程中 UPF 发送 RA（步骤12）与 GWFD-020401/020403 共享描述；RA 实际归属哪个 License 控制（V6PB01/VDSA01/P6PD01）需 Stage 3 验证 | 潜在文档复用 |
| 13 | 系统影响不对称 | （无配置树描述） | U 侧（GWFD-020406）声明"对系统影响可忽略"；C 侧（WSFD-104004）声明"弱覆盖场景掉话率增加"（UE 需通过 UPF 透传 RS） | C-U 影响不对称，需 Stage 3 验证 |
