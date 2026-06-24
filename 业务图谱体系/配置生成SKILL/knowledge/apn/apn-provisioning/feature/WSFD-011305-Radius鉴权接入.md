# WSFD-011305 Radius鉴权接入 知识文档

> 聚焦 APN 业务域鉴权计费场景的 UNC（GGSN/PGW-C/SMF）鉴权接入方式决策特性
> 与 WSFD-011306（Radius功能）形成"接入模式决策 + Radius执行"的强依赖组合

---

## 0. 元数据（三层图谱Schema字段）

| 字段 | 取值 |
|------|------|
| feature_id | WSFD-011305 |
| feature_name | Radius鉴权接入 |
| feature_group | 鉴权计费 |
| parent_feature_id | 无独立父节点（鉴权计费类根特性，配置树鉴权入口） |
| applicable_nf_map | `{"UNC": ["GGSN", "PGW-C", "SMF"]}` |
| variant_dimensions | ["鉴权接入方式(TRANS_NON_AUTH透明 / TRANS_AUTH透明鉴权 / NON_TRANS不透明 / LOC_AUTH本地)", "是否需Radius功能(是/否)", "用户名密码来源(UE携带PCO / UNC公用配置)", "是否支持UDM签约数据参与AAA鉴权(v02+)", "地址空间归属(运营商 / ISP或企业网)"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-01, EV-FK-02, EV-FK-03, EV-FK-04, EV-FK-05, EV-FK-06, EV-FK-07, EV-FK-08, EV-FK-09] |
| license_required | 无（本特性无需License） |

---

## 1. 概述

### 1.1 特性定义（是什么）

UNC 支持**多种接入方式**将用户接入 PDN：**透明接入（TRANS_NON_AUTH）、非透明接入（NON_TRANS）、透明鉴权接入（TRANS_AUTH）和本地鉴权接入（LOC_AUTH）** 四种。

本特性是**控制面（C 面）鉴权接入方式决策特性的总集**：SMF/PGW-C/GGSN 决定"用户以何种鉴权方式接入网络、是否调用 Radius 功能、用户名密码从哪里来"，并据此触发后续鉴权与（可选）计费流程。

> 来源：`output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011305 Radius鉴权接入/特性概述_50176278.md`（"定义"章节）

### 1.2 适用NF（UDG/UNC网元）

| 涉及NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| GGSN | 控制面（UNC，2/3G） | UNC 20.3.2及后续版本 | 2/3G 场景根据 ACCESSMODE 决定 PDP 上下文激活的鉴权方式 |
| PGW-C | 控制面（UNC，4G） | UNC 20.3.2及后续版本 | 4G 场景根据 ACCESSMODE 决定默认承载激活的鉴权方式 |
| SMF | 控制面（UNC，5G） | UNC 20.3.2及后续版本 | 5G 场景根据 ACCESSMODE 决定 PDU 会话建立的鉴权方式 |
| AAA Server | 外部鉴权/计费服务器 | 无特殊需求 | 接收 UNC 发送的鉴权/计费抄送消息（仅 NON_TRANS/TRANS_AUTH 方式需要） |

> 来源：`特性概述_50176278.md`（"可获得性/涉及NF"章节）

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|---------|---------|---------|
| 02 | 20.9.2 | 鉴权接入场景下，UNC 支持用户是否使用 UDM 的签约数据参与决策进行 AAA 鉴权（UDM 签约数据参与决策能力引入） |
| 01 | 20.3.2 | 首次发布，支持 4 种鉴权接入方式 |

> 来源：`特性概述_50176278.md`（"发布历史"章节）

### 1.4 License

**本特性无需获得 License 许可即可获得该特性的服务**（文档明确声明）。

> 来源：`特性概述_50176278.md`（"可获得性/License支持"章节）

### 1.5 前置条件与依赖

| 前置条件 | 说明 |
|---------|------|
| 已完成普通 DNN 配置 | 激活文档明确要求"已经完成配置普通 DNN" |
| 已配置 APN（ADD APN） | SET APNAUTHATTR 的 APN 参数必须已通过 ADD APN 命令配置 |
| Radius 功能（仅部分方式） | **NON_TRANS（不透明）和 TRANS_AUTH（透明鉴权）方式必须开启 WSFD-011306 Radius 功能**；TRANS_NON_AUTH 和 LOC_AUTH 方式不需要 |
| AAA Server 就绪（仅部分方式） | NON_TRANS/TRANS_AUTH 方式需 AAA Server 工作正常且鉴权信息已配置 |

> 来源：`激活Radius鉴权接入_50176279.md`（"必备事项/前提条件"）、`特性概述_50176278.md`（"与其他特性的交互"）

### 1.6 与其他特性的交互

| 交互类型 | 相关特性 | 交互说明 |
|---------|---------|---------|
| **依赖** | WSFD-011306 Radius功能（UNC） | **使用非透明接入（NON_TRANS）、透明鉴权接入（TRANS_AUTH）时必须开启 Radius 功能**（文档明确依赖关系） |
| 计费可选 | WSFD-011306 Radius功能（UNC） | NON_TRANS/TRANS_AUTH/LOC_AUTH 方式下计费可选；TRANS_NON_AUTH 不涉及计费（可选择是否计费，参见 WSFD-011306） |
| 抄送 | WSFD-011307 Radius抄送功能（UNC） | Radius 计费抄送（鉴权接入后的计费抄送链路） |

> 来源：`特性概述_50176278.md`（"与其他特性的交互"章节，明确声明对 WSFD-011306 的依赖）

### 1.7 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | 针对不同的组网，可以选择不同的接入方式，从而限定为不同用户划分不同网络服务。使用公用的用户名和密码进行认证场景下，可以减少配置过程，提高易用性。 |
| 用户 | 使用公用的用户名和密码进行认证场景下，如果没有输入用户名和密码或者输入有误的情况下仍能接入，提升体验。 |

> 来源：`特性概述_50176278.md`（"客户价值"章节）

### 1.8 应用场景

| 接入方式 | 适用场景 |
|---------|---------|
| 透明接入（TRANS_NON_AUTH） | 用户访问运营商的网络，运营商不对用户权限和计费作要求 |
| 非透明接入（NON_TRANS） | 用户访问 ISP（Internet Service Provider）或者企业网，ISP 或企业网要对用户权限有要求，并对用户进行计费 |
| 透明鉴权接入（TRANS_AUTH） | 用户访问运营商的网络，运营商使用统一的用户名和密码为用户鉴权和计费。用户在没有输入用户名和密码或者输入有误的情况下仍能保证用户接入 |
| 本地鉴权接入（LOC_AUTH） | 用户访问 ISP 或者企业网，在没有部署 AAA 鉴权服务器的情况下，仍然可以提供简单鉴权功能，满足 ISP 或企业网对用户权限的要求 |

> 来源：`特性概述_50176278.md`（"应用场景"章节）

### 1.9 对系统的影响

**本特性对系统无影响**（文档明确声明）。

### 1.10 应用限制

**PPP（Point-to-Point Protocol）用户暂不支持本地鉴权功能**（即 LOC_AUTH 方式不适用于 PPP 用户，文档明确限制）。

> 来源：`特性概述_50176278.md`（"应用限制"章节）

### 1.11 特性规格

**本特性无特殊规格**（文档明确声明）。

### 1.12 计费与话单

**本特性不涉及计费与话单**（鉴权接入决策本身不计费；具体计费由可选的 WSFD-011306 Radius 功能承担）。

### 1.13 遵循标准

| 标准类别 | 标准编号 | 标准名称 |
|---------|---------|---------|
| 3GPP | 23.060 | General Packet Radio Service (GPRS) Service Description |
| 3GPP | 29.060 | GPRS; GPRS Tunnelling Protocol (GTP) across the Gn and Gp interface |
| 3GPP | 29.061 | Interworking between PLMN supporting packet based services and PDN |
| 3GPP | 24.008 | Mobile radio interface Layer 3 specification; Core network protocols |
| 3GPP | 23.214 | Architecture enhancements for control and user plane separation of EPC nodes |
| 3GPP | 29.244 | Interface between the Control Plane and the User Plane of EPC Nodes |

> 来源：`特性概述_50176278.md`（"遵循标准"章节）

---

## 2. 激活

> 本特性无独立 License。激活即"配置使能"：通过 SET APNAUTHATTR 命令为指定 APN 配置鉴权接入模式（ACCESSMODE）及公用用户名/密码。

### 2.1 激活通用前置条件

- 已阅读 `WSFD-011305 Radius鉴权接入特性概述`
- 已经完成配置普通 DNN
- 已通过 **ADD APN** 配置目标 APN（SET APNAUTHATTR 的 APN 参数来源）
- 若选择 NON_TRANS 或 TRANS_AUTH 方式 → 必须先完成 **WSFD-011306 Radius 功能** 的激活与 AAA Server 数据配置

> 来源：`激活Radius鉴权接入_50176279.md`（"必备事项"章节）

### 2.2 通用激活步骤骨架（1步核心命令）

```
步骤1：配置 APN 鉴权属性
  └── SET APNAUTHATTR
        ├── APN              → 已通过 ADD APN 配置的 APN 名称
        ├── ACCESSMODE       → 4种鉴权方式之一（TRANS_AUTH / TRANS_NON_AUTH / NON_TRANS / LOC_AUTH）
        ├── COMMONUSERNAME   → 公用用户名（TRANS_AUTH/LOC_AUTH/NON_TRANS 均可能使用）
        ├── COMMONUSERPASS   → 公用密码
        └── CFMCOMMUSERPASS  → 确认公用密码（需与 COMMONUSERPASS 一致）
```

> 来源：`激活Radius鉴权接入_50176279.md`（"操作步骤"章节）

### 2.3 4种鉴权方式激活参数矩阵

| ACCESSMODE | 中文 | 鉴权必要性 | Radius功能依赖 | COMMONUSERNAME/PASS | UE PCO携带 | 调测脚本来源 |
|-----------|------|-----------|---------------|---------------------|-----------|-------------|
| TRANS_NON_AUTH | 透明不鉴权 | 不鉴权 | **否** | 不强制 | 不需要 | 调测透明接入_95351130.md |
| TRANS_AUTH | 透明鉴权 | UNC 用公用账密到AAA鉴权 | **是（必须）** | **必配**（UNC 用此账密代鉴权） | 不需要 | 调测透明鉴权接入_95351132.md |
| NON_TRANS | 不透明接入 | UE 携账密，UNC 到 AAA 鉴权 | **是（必须）** | 可选（可继续配置鉴权使用的用户名和密码） | **需要**（PCO 携带用户名密码） | 调测非透明接入_95351131.md |
| LOC_AUTH | 本地鉴权 | UNC 本地匹配 UE 携带的账密 | **否** | **必配**（作为本地匹配基准） | **需要**（PCO 携带用户名密码） | 调测本地鉴权接入_95351133.md |

> 来源：`激活Radius鉴权接入_50176279.md`（ACCESSMODE 取值说明）、`特性概述_50176278.md`（4 种方式原理）、各调测文档（Radius依赖依据：调测透明鉴权/非透明接入均要求"AAA Server工作正常"且引用 WSFD-011306 配置；调测透明接入/本地鉴权未要求 AAA Server）

---

## 3. 原理

### 3.1 4种鉴权方式精确语义（★重点）

#### 3.1.1 透明接入（TRANS_NON_AUTH）

**语义**：用户在接入 UNC 时**无需鉴权**。

典型场景是运营商充当 Internet 服务提供商 ISP，直接向用户提供业务（电子邮件、主页浏览等）。用户在 PDP 上下文/缺省承载/PDU 会话创建过程中无需发送任何鉴权请求，UNC 也无需发起用户鉴权/授权过程。

- **Radius 鉴权**：不需要
- **计费**：可选（参考 WSFD-011306）
- **地址空间**：运营商的地址空间（HLR/HSS/UDM 签约静态地址，或创建阶段获取动态地址）

> 来源：`特性概述_50176278.md`（"原理概述/透明接入"章节）

#### 3.1.2 非透明接入（NON_TRANS）

**语义**：用户在接入 UNC 时**必须进行鉴权**。

UNC 提供到 Radius 服务器的用户身份认证。认证服务器属于用户所要连接的 ISP 或者企业网。用户需要在创建过程中**发送鉴权请求**，UNC 会向归属于 ISP/企业网的 AAA 服务器请求用户鉴权。用户的鉴权请求信息在 **PCO（Protocol Configuration Option，协议配置选项）**中携带。UNC 上获得 Radius 鉴权的结果和其他 PCO 申请内容（如主备 DNS 等）都应携带在 PCO 中作为响应发送给用户。

- **Radius 鉴权**：**必须**，UNC 支持 **PAP 和 CHAP** 两种 Radius 鉴权方式
- **Radius 功能依赖**：**是**（必须开启 WSFD-011306）
- **计费**：可选（Radius 服务器同时可具有计费功能）
- **用户名密码来源**：**UE 在 PCO 中携带**（用户主动输入）
- **地址空间**：ISP 或企业网的地址空间（静态或动态）
- **UDM 签约数据参与决策（v02+）**：UNC 支持用户是否使用 UDM 的签约数据参与决策进行 AAA 鉴权；若使用，UNC 支持配置用户是否使用 UDM 签约的 AAA 地址进行鉴权

> 来源：`特性概述_50176278.md`（"原理概述/非透明接入"章节）

#### 3.1.3 透明鉴权接入（TRANS_AUTH）

**语义**：在用户接入 UNC 时，**UNC 使用系统配置的用户名和密码去鉴权服务器为用户进行鉴权**。

又称为**匿名接入**。由 UNC 在网络侧使用该 APN 下配置的**公用的用户名和密码**发送鉴权请求到 AAA Server，并从 AAA Server 获取控制用户的属性，以便对终端灵活控制。UNC 支持基于 APN 配置默认的用户名和密码，当用户以该 APN 接入且 APN 配置为透明鉴权时，UNC 直接使用该 APN 下配置的公用账密作为用户的账密，到 Radius 服务器上鉴权。

- **Radius 鉴权**：**必须**，UNC 支持 **PAP 和 CHAP** 两种方式
- **Radius 功能依赖**：**是**（必须开启 WSFD-011306）
- **计费**：可选
- **用户名密码来源**：**UNC 本地 APN 公用配置**（用户不感知，无需输入）
- **地址空间**：ISP 或企业网的地址空间（静态或动态）
- **UDM 签约数据参与决策（v02+）**：同非透明接入，支持配置

> 来源：`特性概述_50176278.md`（"原理概述/透明鉴权接入"章节）

#### 3.1.4 本地鉴权接入（LOC_AUTH）

**语义**：在用户接入 UNC 时，**UNC 使用系统配置的用户名和密码与用户接入时携带的 PCO 的密码进行匹配**为用户进行鉴权。

适用场景：用户通过运营商网络访问 ISP/企业网时，运营商通过在 UNC 本地配置的公用账密对用户进行鉴权。在 ISP/企业网**没有部署 AAA 鉴权服务器**不能提供鉴权功能的情况下，由运营商提供本地鉴权接入功能，保证接入安全性。用户在创建过程中需发送携带的用户名和密码，UNC 根据本地配置对用户进行用户名和密码的**匹配**。

- **Radius 鉴权**：**不需要**（本地完成，不调用 Radius）
- **Radius 功能依赖**：**否**
- **计费**：不涉及（本地鉴权场景）
- **用户名密码来源**：**UE 在 PCO 中携带** + UNC 本地公用配置**匹配**
- **地址空间**：同其他方式（静态或动态）
- **应用限制**：**PPP 用户暂不支持本地鉴权**（文档明确限制）

> 来源：`特性概述_50176278.md`（"原理概述/本地鉴权接入"、应用限制章节）

### 3.2 4种方式相同点/不同点对照（文档原文）

| 方式 | 相同点 | 不同点 |
| --- | --- | --- |
| 透明接入 | 均可使用 HLR/HSS/UDM 签约静态地址或创建阶段动态地址 | **无需对用户进行鉴权和计费**，用户不需要进行用户名和密码输入操作 |
| 非透明接入 | 同上 | **需要对用户进行鉴权和计费（计费可选）**，用户进行用户名和密码输入操作 |
| 透明鉴权接入 | 同上 | **需要对用户进行鉴权和计费（计费可选）**，用户**不需要**进行用户名和密码输入操作，UNC 使用统一的用户名和密码为用户鉴权 |
| 本地鉴权接入 | 同上 | **需要对用户进行鉴权**，用户需要进行用户名和密码输入操作，UNC 使用统一的用户名和密码为用户鉴权 |

> 来源：`特性概述_50176278.md`（"原理概述"末尾对照表）

### 3.3 ★AUTHMODE 4方式与 Radius 功能联动矩阵（核心结论）

| AUTHMODE | 是否需 Radius 功能（WSFD-011306） | 鉴权执行方 | 用户名密码来源 | AAA Server 是否必配 | 计费可选 |
|----------|----------------------------------|-----------|---------------|---------------------|---------|
| **TRANS_NON_AUTH（透明接入）** | **否** | 无鉴权 | 不适用 | 否 | 是（参考 WSFD-011306） |
| **TRANS_AUTH（透明鉴权接入）** | **是（必须）** | UNC→AAA Server（UNC 代发） | UNC APN 公用配置 | **是** | 是 |
| **NON_TRANS（不透明接入）** | **是（必须）** | UNC→AAA Server（UE 账密透传） | UE PCO 携带 | **是** | 是 |
| **LOC_AUTH（本地鉴权接入）** | **否** | UNC 本地匹配 | UE PCO + UNC 本地公用配置 | 否 | 否（本地鉴权不涉及计费） |

**联动结论（文档依据）**：

- **TRANS_AUTH 与 NON_TRANS 必须开启 Radius 功能**：`特性概述_50176278.md`"与其他特性的交互"章节明确声明"**使用非透明接入、透明鉴权接入时必须开启 Radius 功能**"。调测文档进一步佐证：调测透明鉴权接入（_95351132.md）和调测非透明接入（_95351131.md）的"必备事项"均要求"AAA Server 工作正常，用户的鉴权信息已在 AAA Server 上配置"，且数据准备表中引用 `配置RADIUS功能_32909765.md`。
- **TRANS_NON_AUTH 与 LOC_AUTH 不需要 Radius 功能**：调测透明接入（_95351130.md）和调测本地鉴权接入（_95351133.md）的"必备事项"均**未要求** AAA Server 工作正常，数据准备表也**未引用** WSFD-011306 的配置；本地鉴权文档进一步强调"在没有部署 AAA 鉴权服务器的情况下"使用。
- **Radius 鉴权协议**：TRANS_AUTH 和 NON_TRANS 方式下，UNC 支持 **PAP 和 CHAP** 两种 Radius 鉴权方式。

> 来源：`特性概述_50176278.md`（交互、原理章节）、`调测透明鉴权接入_95351132.md`、`调测非透明接入_95351131.md`、`调测透明接入_95351130.md`、`调测本地鉴权接入_95351133.md`

### 3.4 业务流程（鉴权接入决策与执行）

```
┌──────────────────────────────────────────────────────────────┐
│ UNC（C 面：GGSN/PGW-C/SMF） - WSFD-011305                     │
│ 鉴权接入方式决策方：根据 APN 的 ACCESSMODE 决定鉴权路径        │
│                                                              │
│   用户发起 PDP上下文/缺省承载/PDU会话 创建请求                │
│                          │                                   │
│           ┌──────────────┼──────────────┐                    │
│           ▼              ▼              ▼                    │
│   ┌──────────────┐ ┌─────────────┐ ┌──────────────┐          │
│   │TRANS_NON_AUTH│ │ TRANS_AUTH  │ │  NON_TRANS   │          │
│   │  透明接入    │ │ 透明鉴权    │ │  不透明接入  │          │
│   │  无鉴权      │ │ UNC公用账密 │ │  UE PCO账密  │          │
│   │  ↓           │ │  ↓          │ │  ↓           │          │
│   │  直接接入    │ │ 发往AAA     │ │ 透传至AAA    │          │
│   └──────┬───────┘ └──────┬──────┘ └──────┬───────┘          │
│          │                │               │                  │
│          │         ┌──────┴───────────────┘                  │
│          │         │  需要 WSFD-011306 Radius功能             │
│          │         ▼                                         │
│          │   AAA Server（Radius鉴权，PAP/CHAP）              │
│          │         │                                         │
│          │         ▼                                         │
│   ┌──────┴─────────┴──────────────┐                          │
│   │  鉴权通过 → 用户接入          │                          │
│   └───────────────────────────────┘                          │
│                                                              │
│   ┌──────────────────────────────────────┐                   │
│   │  LOC_AUTH 本地鉴权（独立路径）        │                   │
│   │  UE PCO 账密 ↔ UNC 本地公用配置 匹配 │                   │
│   │  匹配通过 → 接入；不通过 → 拒绝      │                   │
│   │  （不调用 Radius，不涉及 AAA Server） │                   │
│   └──────────────────────────────────────┘                   │
└──────────────────────────────────────────────────────────────┘
```

> 来源：综合 `特性概述_50176278.md`（原理章节）与 4 个调测文档的鉴权执行路径构建

### 3.5 ★与 WSFD-010301（鉴权功能）/ WSFD-108007（终端二次鉴权）的关系（文档依据）

| 关联特性 | 关系类型 | 文档依据 / 关系说明 |
|---------|---------|---------------------|
| **WSFD-010301 鉴权功能**（UNC） | **底层鉴权协议层 vs. 接入鉴权决策层（互补，非直接依赖）** | WSFD-010301 是 UNC 的**基础鉴权功能**（2/3G、4G、5G 三代鉴权流程：5G AKA、EAP AKA' 等），覆盖**接入层鉴权（UE ↔ HSS/UDM/ARPF）**；WSFD-011305 是**应用层/APN 级 Radius 鉴权接入方式决策**（UE/UNC ↔ AAA Server）。两者鉴权对象不同：WSFD-010301 是 SIM/USIM 卡身份鉴权（5G AKA/EAP AKA'），WSFD-011305 是用户名密码鉴权（PAP/CHAP via Radius 或本地匹配）。WSFD-011305 文档**未直接引用** WSFD-010301，二者为并列的鉴权体系。本特性文档中"UDM 签约数据参与 AAA 鉴权"（v02+）涉及与 UDM 数据交互，属应用层与签约数据的联动，与 WSFD-010301 底层接入鉴权无直接耦合。 |
| **WSFD-108007 终端二次鉴权**（UNC，MEC解决方案） | **企业 AAA 场景的鉴权增强（互补）** | WSFD-108007 是**终端二次鉴权**特性，适用于**企业 AAA 场景**（DN-AAA 对访问企业数据网络的终端进行二次认证）。与本特性关系：本特性（WSFD-011305）的 **NON_TRANS（不透明接入）** 方式是 UE 一次鉴权到 ISP/企业 AAA；WSFD-108007 是**会话建立后访问特定 DN 时的二次鉴权**（针对企业数据网络）。两者鉴权时机不同（接入时 vs. 访问 DN 时）、鉴权对象不同（接入 AAA vs. 企业 DN-AAA）。WSFD-011305 文档**未直接引用** WSFD-108007，二者为不同时点的鉴权特性。 |

> 来源：`特性概述_50176278.md`（本特性"与其他特性的交互"仅声明对 WSFD-011306 的依赖，未提及 WSFD-010301/WSFD-108007）；关系说明基于特性语义与文档清单分类（WSFD-010301 属安全管理功能/鉴权功能，WSFD-108007 属 MEC 解决方案/终端二次鉴权）；WSFD-010301 与 WSFD-108007 的具体文档依据见各自特性概述（Stage 3 横向分析时进一步验证）

---

## 4. 配置

### 4.1 配置对象（UNC 侧 APN 鉴权属性）

```
┌───────────────────────────────────────────────────────────────┐
│ UNC 侧 APN 鉴权属性体系                                        │
│                                                               │
│   ┌────────────────────────────────────────────────────┐      │
│   │  APN（前置：ADD APN 已配置）                       │      │
│   │                      │                             │      │
│   │                      ▼                             │      │
│   │  SET APNAUTHATTR（APN鉴权属性，每APN一条）         │      │
│   │    ├── APN                  APN名称                │      │
│   │    ├── ACCESSMODE           4种鉴权方式之一        │      │
│   │    ├── COMMONUSERNAME       公用用户名             │      │
│   │    ├── COMMONUSERPASS       公用密码               │      │
│   │    └── CFMCOMMUSERPASS      确认公用密码           │      │
│   └────────────────────────────────────────────────────┘      │
│                                                               │
│   LST APNAUTHATTR（查询验证）                                 │
└───────────────────────────────────────────────────────────────┘

依赖（仅 TRANS_AUTH / NON_TRANS 方式）：
┌───────────────────────────────────────────────────────────────┐
│ WSFD-011306 Radius功能体系（独立特性，本特性依赖）             │
│   ├── Radius Server Group（RDSSVRGRPNAME）                    │
│   ├── AAA Server（SERVERIPV4 / CIPHERKEY）                    │
│   └── 到 AAA Server 的网络数据（单平面/双平面/GRE VPN）        │
└───────────────────────────────────────────────────────────────┘
```

### 4.2 MML命令清单

#### 4.2.1 核心命令（参考信息列出的2条）

| 命令 | 用途 | 关键参数/说明 |
|------|------|---------------|
| **SET APNAUTHATTR** | 设置 APN 鉴权属性配置 | APN, ACCESSMODE, COMMONUSERNAME, COMMONUSERPASS, CFMCOMMUSERPASS |
| **LST APNAUTHATTR** | 查询 APN 鉴权属性配置 | APN（用于调测验证） |

> 来源：`WSFD-011305 Radius鉴权接入参考信息_50176281.md`（"命令"章节）

#### 4.2.2 调测辅助命令

| 命令 | 用途 | 来源 |
|------|------|------|
| DSP PDUSESSION | 显示 PDU 会话（查 IMSI 对应会话是否创建成功） | 4 个调测文档步骤3 |
| LST RDSSVRGRP | 查询 Radius 服务器组（仅 TRANS_AUTH/NON_TRANS 调测用） | 调测透明鉴权/非透明接入步骤7 |
| EXP MML | 导出 MML 配置文件（故障收集） | 4 个调测文档末步 |

#### 4.2.3 前置依赖命令（来自其他特性）

| 命令 | 用途 | 来源特性 |
|------|------|---------|
| ADD APN | 增加 APN 配置（SET APNAUTHATTR 的 APN 来源） | 会话管理域 |
| ADD RDSSVRGRP / 配置RADIUS功能 | Radius 服务器组配置（TRANS_AUTH/NON_TRANS 前置） | WSFD-011306 |

### 4.3 关键参数说明

#### 4.3.1 SET APNAUTHATTR 关键参数（ACCESSMODE 4种取值）

| 参数 | 取值 | 说明 |
|------|------|------|
| APN | 字符串（如 huawei.com） | APN 名称，需已通过 ADD APN 配置 |
| **ACCESSMODE** | **TRANS_AUTH** | 透明鉴权：指定为透明并需要鉴权。这种鉴权方式对用户是透明的，不需要用户感知，鉴权使用的用户名和密码一般由 UNC 配置 |
| **ACCESSMODE** | **TRANS_NON_AUTH** | 透明不鉴权：指定为透明不需要鉴权。这种接入方式不需要去 RADIUS 服务器鉴权 |
| **ACCESSMODE** | **NON_TRANS** | 不透明：指定为不透明接入，需要鉴权。这种鉴权方式可以继续配置鉴权使用的用户名和密码 |
| **ACCESSMODE** | **LOC_AUTH** | 本地鉴权：指定为本地鉴权。这种接入方式不需要去 RADIUS 服务器鉴权，通过 UNC 完成鉴权功能 |
| COMMONUSERNAME | 字符串（如 huawei123） | 公用用户名（UNC 公用配置） |
| COMMONUSERPASS | 字符串（如 123） | 公用密码 |
| CFMCOMMUSERPASS | 字符串（如 123） | 确认公用密码，需与 COMMONUSERPASS 保持一致 |

> 来源：`激活Radius鉴权接入_50176279.md`（数据表 ACCESSMODE 取值说明，原文逐字保留）

#### 4.3.2 ACCESSMODE 取值语义速查

| 取值 | 中文 | 鉴权 | Radius | 账密来源 | PPP用户支持 |
|------|------|------|--------|---------|------------|
| TRANS_NON_AUTH | 透明不鉴权 | 否 | 否 | 不适用 | 是 |
| TRANS_AUTH | 透明鉴权 | 是（UNC 代发） | **是** | UNC 公用配置 | 是 |
| NON_TRANS | 不透明 | 是（UE 透传） | **是** | UE PCO | 是 |
| LOC_AUTH | 本地鉴权 | 是（本地匹配） | 否 | UE PCO + UNC 本地 | **否（限制）** |

### 4.4 约束条件

| 约束类型 | 约束内容 |
|---------|---------|
| **PPP 用户限制** | **PPP（Point-to-Point Protocol）用户暂不支持本地鉴权功能**（即 LOC_AUTH 方式不适用于 PPP 用户，文档明确应用限制） |
| Radius 功能强依赖 | 使用 NON_TRANS、TRANS_AUTH 方式时**必须开启 WSFD-011306 Radius 功能**，否则鉴权无法执行 |
| AAA Server 必要性 | NON_TRANS/TRANS_AUTH 方式下 AAA Server 必须工作正常且用户鉴权信息已配置 |
| APN 前置 | SET APNAUTHATTR 的 APN 必须已通过 ADD APN 配置 |
| DNN 前置 | 激活前必须已完成配置普通 DNN |
| COMMONUSERPASS 一致性 | CFMCOMMUSERPASS 必须与 COMMONUSERPASS 保持一致 |

> 来源：`特性概述_50176278.md`（应用限制、与其他特性的交互）、`激活Radius鉴权接入_50176279.md`（必备事项）

---

## 5. 配置案例

### 5.1 典型场景一：透明鉴权接入（TRANS_AUTH，运营商统一账密场景）

**场景描述**：运营商需要对透明接入的用户进行 Radius 鉴权以获取用户属性用于更加灵活的控制用户。配置 APN 为 huawei.com 的鉴权属性，接入模式为**透明鉴权接入**，公用的用户名和密码分别为 huawei123 和 123。当用户以该 APN 接入时，UNC 直接使用该 APN 下配置的公用的用户名和密码为用户的用户名和密码，到 Radius 服务器进行鉴权。

**MML命令序列（原样保留）**：

```
//配置APN鉴权属性。
SET APNAUTHATTR: APN="huawei.com", ACCESSMODE=TRANS_AUTH, COMMONUSERNAME="huawei123", COMMONUSERPASS="123", CFMCOMMUSERPASS="123";
```

**配套依赖配置（来自 WSFD-011306，本特性必须）**：

```
// Radius 服务器组与 AAA Server 数据（参见 WSFD-011306 配置RADIUS功能_32909765.md）
// RDSSVRGRPNAME=isprg, SERVERIPV4=10.168.10.1, CIPHERKEY=ispchina
```

> 来源：`激活Radius鉴权接入_50176279.md`（"任务示例"完整脚本）、`调测透明鉴权接入_95351132.md`（数据准备表 AAA Server 参数）

### 5.2 典型场景二：其他 3 种方式的配置变体（基于 ACCESSMODE 取值切换）

**场景描述**：通过修改 SET APNAUTHATTR 的 ACCESSMODE 参数即可切换为其他 3 种鉴权方式。

**MML命令变体**：

```
// 变体A：透明接入（无鉴权，最简）
SET APNAUTHATTR: APN="huawei.com", ACCESSMODE=TRANS_NON_AUTH;
// 说明：不需要 Radius 功能；COMMONUSERNAME/PASS 非强制

// 变体B：非透明接入（UE 携账密，UNC 透传 AAA 鉴权）
SET APNAUTHATTR: APN="huawei.com", ACCESSMODE=NON_TRANS, COMMONUSERNAME="huawei123", COMMONUSERPASS="123", CFMCOMMUSERPASS="123";
// 说明：必须开启 Radius 功能；用户在 PCO 中携带账密，UNC 透传至 AAA

// 变体C：本地鉴权接入（UNC 本地匹配，不调 Radius）
SET APNAUTHATTR: APN="huawei.com", ACCESSMODE=LOC_AUTH, COMMONUSERNAME="huawei123", COMMONUSERPASS="123", CFMCOMMUSERPASS="123";
// 说明：不需要 Radius 功能；UE PCO 携账密与 UNC 本地公用配置匹配；PPP 用户不支持
```

> 说明：激活文档仅提供了 TRANS_AUTH 方式的完整任务示例脚本（场景一）；其他 3 种方式的脚本基于 ACCESSMODE 取值说明和调测文档数据准备表推导，参数集与 TRANS_AUTH 一致，仅 ACCESSMODE 值不同。

> 来源：`激活Radius鉴权接入_50176279.md`（ACCESSMODE 取值定义）、4 个调测文档（各方式数据准备与必备事项）

### 5.3 场景变体对照（含 Radius 依赖）

| 变体 | ACCESSMODE | Radius功能 | AAA Server | 调测脚本完整度 |
|------|-----------|-----------|-----------|---------------|
| 透明接入 | TRANS_NON_AUTH | 不需要 | 不需要 | 完整（_95351130.md） |
| 透明鉴权接入 | TRANS_AUTH | **需要** | **需要** | 完整（_95351132.md） |
| 不透明接入 | NON_TRANS | **需要** | **需要** | 完整（_95351131.md） |
| 本地鉴权接入 | LOC_AUTH | 不需要 | 不需要 | 完整（_95351133.md，**PPP 用户不支持**） |

---

## 6. 验证与调测

### 6.1 调测通用流程（4 种方式共性 + 差异）

#### 6.1.1 通用调测前提

- 已阅读 `WSFD-011305 Radius鉴权接入特性概述`
- 已完成 `激活Radius鉴权接入`（SET APNAUTHATTR）
- 适用于 GGSN、PGW-C、SMF
- TRANS_AUTH/NON_TRANS 方式额外要求：AAA Server 工作正常，用户的鉴权信息已在 AAA Server 上配置

> 来源：4 个调测文档（"必备事项/前提条件"章节）

#### 6.1.2 通用调测执行步骤（4种方式共有的核心3步）

**步骤1**：测试终端使用 "huawei.com" APN 接入网络（TRANS_AUTH/NON_TRANS/LOC_AUTH 方式下需设置用户名密码；TRANS_NON_AUTH 无需）。

**步骤2**：进入 "MML命令行-UNC" 窗口，执行 **DSP PDUSESSION** 查询用户会话：

```
DSP PDUSESSION:QUERYTYPE=IMSI, IMSI="123000123456789", DSPINFOTYPE=DETAILED, WLNETWKTYPE=NW5G, PDUSESSIONID=5, QFI=1;
RETCODE = 0  操作成功  

结果如下  
--------------  
             IMSI = 123000123456789
                ...
         APN或者DNN = huawei.com
                ...
(结果个数 = 1) 
---    END
```

- 预期结果：用户接入成功并创建会话，"APN或者DNN" 与实际规划值一致 → 调测结束
- 非预期结果：用户创建会话失败，或 "APN或者DNN" 与规划值不一致 → 进入排查步骤

**步骤3**：执行 **LST APNAUTHATTR** 查询 APN 鉴权属性，核对 ACCESSMODE 与规划值一致。

> 来源：`调测Radius鉴权接入_50176280.md`（通用调测）、4 个子方式调测文档

#### 6.1.3 TRANS_AUTH/NON_TRANS 方式的鉴权消息跟踪（额外步骤）

对透明鉴权接入和非透明接入，调测文档额外要求在 OM Portal 建立用户跟踪，检查 UNC 向 AAA Server 发送的 **"Access Request"** 鉴权请求消息：

- **透明鉴权接入**：检查 "user-name" 是否与规划值一致（UNC 公用配置）、"user-password" 是否加密
- **非透明接入**：检查 "user-name" 是否与 PCO 信元携带的用户名一致、"user-password" 是否加密

若 user-name 不一致或密码未加密 → 执行 LST RDSSVRGRP 查询 Radius 服务器组配置，参考 WSFD-011306 重新配置。

> 来源：`调测透明鉴权接入_95351132.md`（步骤5、图1 Access Request 鉴权请求消息）、`调测非透明接入_95351131.md`（步骤5）

#### 6.1.4 LOC_AUTH 方式的本地匹配验证（额外步骤）

对本地鉴权接入，调测文档额外要求：

**步骤4**：查看终端设置的用户名和密码是否正确。
- 正确 → 执行 LST APNAUTHATTR 核对配置
- 不正确 → 重新设置用户名和密码，重新接入

> 来源：`调测本地鉴权接入_95351133.md`（步骤4）

### 6.2 告警参考

| 告警ID | 告警名称 | 触发条件 | 影响 |
|--------|---------|---------|------|
| ALM-100197 | RADIUS鉴权服务器无响应 | UNC 向 AAA Server 发送鉴权请求无响应（仅 TRANS_AUTH/NON_TRANS 方式相关） | 鉴权失败，用户无法接入 |

> 来源：`WSFD-011305 Radius鉴权接入参考信息_50176281.md`（"告警"章节）

### 6.3 软参

| 软参 | 说明 |
|------|------|
| BIT1934 | 控制 UNC 是否解析 AAA 响应的 Access Accept 消息中的 called-station-id 信元 |
| BIT1734 | 控制在鉴权请求消息中携带的 nas-port 是否唯一 |
| BIT219 | 控制 Access Request 消息中是否携带 NAS-Port 信元 |
| DWORD28 | 控制 access request 和 accounting request 消息中是否携带 NAS-Port 信元 |

> 来源：`WSFD-011305 Radius鉴权接入参考信息_50176281.md`（"软参"章节）

### 6.4 测量指标

**本特性无相关测量指标**（参考信息明确声明）。

> 来源：`WSFD-011305 Radius鉴权接入参考信息_50176281.md`（"测量指标"章节）

### 6.5 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| 透明接入/本地鉴权接入失败 | ACCESSMODE 配置错误 | LST APNAUTHATTR 核对 ACCESSMODE 是否为 TRANS_NON_AUTH/LOC_AUTH |
| 透明鉴权接入/非透明接入失败 | Radius 功能未开启或 AAA Server 不可达 | 确认 WSFD-011306 已激活；LST RDSSVRGRP 核对服务器组；检查 ALM-100197 告警 |
| 非透明接入鉴权失败 | UE 未在 PCO 中携带正确的用户名密码 | 查看终端用户名密码设置；检查 Access Request 中 user-name 与 PCO 携带是否一致 |
| 透明鉴权接入鉴权失败 | UNC 公用账密与 AAA Server 配置不匹配 | LST APNAUTHATTR 核对 COMMONUSERNAME/PASS；在 AAA Server 核对账密 |
| 本地鉴权接入鉴权失败 | UE PCO 账密与 UNC 本地公用配置不匹配 | 查看终端用户名密码；LST APNAUTHATTR 核对本地公用配置 |
| 本地鉴权接入 PPP 用户失败 | **PPP 用户不支持本地鉴权**（应用限制） | 改用 NON_TRANS 或 TRANS_AUTH 方式 |
| 鉴权请求消息异常 | NAS-Port 信元控制问题 | 检查 BIT219、BIT1734、DWORD28 软参 |
| Access Accept 解析问题 | called-station-id 信元解析控制 | 检查 BIT1934 软参 |

> 来源：综合 4 个调测文档（排查步骤）、参考信息（告警/软参）、特性概述（应用限制）

---

## 7. 参考信息

### 7.1 与其他特性的关系

| 关联特性 | 特性ID | 关系类型 | 关系说明 |
|---------|--------|---------|---------|
| **Radius功能** | **WSFD-011306（UNC）** | **依赖（文档明确）** | **使用 NON_TRANS（不透明）、TRANS_AUTH（透明鉴权）时必须开启 Radius 功能**；Radius 服务器组、AAA Server 数据、PAP/CHAP 协议均由 WSFD-011306 提供 |
| Radius抄送功能 | WSFD-011307（UNC） | 鉴权后计费抄送 | Radius 计费抄送链路（鉴权接入成功后的计费抄送） |
| 鉴权功能 | WSFD-010301（UNC） | 互补（非直接依赖） | WSFD-010301 是底层接入鉴权（UE↔HSS/UDM，5G AKA/EAP AKA'）；本特性是应用层/APN级 Radius 鉴权接入决策（UE/UNC↔AAA，PAP/CHAP）。两者鉴权对象不同，并列的鉴权体系 |
| 终端二次鉴权 | WSFD-108007（UNC，MEC） | 互补（不同时点） | WSFD-108007 是会话建立后访问企业 DN 时的二次鉴权（DN-AAA）；本特性是接入时的一次鉴权。鉴权时机与对象不同 |
| 用户数据管理 | WSFD-010400（UNC） | UDM数据联动 | v02+ 特性"用户是否使用 UDM 签约数据参与 AAA 鉴权"涉及 UDM 签约数据交互 |
| 地址分配方式 | WSFD-010502（UNC） | 地址空间联动 | NON_TRANS/TRANS_AUTH 方式下用户地址属 ISP/企业网地址空间；TRANS_NON_AUTH 属运营商地址空间 |
| 会话管理 | WSFD-010501（UNC） | 宿主特性 | PDP上下文/缺省承载/PDU会话 创建过程中触发鉴权接入决策 |

> 来源：`特性概述_50176278.md`（"与其他特性的交互"明确依赖 WSFD-011306）；WSFD-010301/WSFD-108007 关系基于特性语义与文档分类（Stage 3 横向验证）

### 7.2 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011305 Radius鉴权接入/特性概述_50176278.md` | 适用NF（GGSN/PGW-C/SMF + AAA Server）、4种鉴权接入方式定义（透明/非透明/透明鉴权/本地鉴权）、4种方式相同点/不同点对照表、原理详解（PCO/PAP/CHAP/Radius/UDM签约数据参与决策）、应用场景（4种方式适用场景）、可获得性（UNC 20.3.2+，无License）、与其他特性交互（**依赖WSFD-011306**）、应用限制（**PPP用户不支持本地鉴权**）、对系统影响（无）、计费与话单（不涉及）、特性规格（无）、遵循标准（6个3GPP标准）、发布历史（v01 20.3.2 / v02 20.9.2 UDM签约数据参与AAA鉴权） |
| 2 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011305 Radius鉴权接入/WSFD-011305 Radius鉴权接入参考信息_50176281.md` | MML命令清单（2条：SET APNAUTHATTR、LST APNAUTHATTR）、告警（ALM-100197 RADIUS鉴权服务器无响应）、软参（4个：BIT1934/BIT1734/BIT219/DWORD28）、测量指标（无） |
| 3 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011305 Radius鉴权接入/激活Radius鉴权接入_50176279.md` | 激活流程、必备事项（已完成普通DNN、ADD APN前置）、SET APNAUTHATTR数据表（ACCESSMODE 4种取值精确语义：TRANS_AUTH/TRANS_NON_AUTH/NON_TRANS/LOC_AUTH）、COMMONUSERNAME/COMMONUSERPASS/CFMCOMMUSERPASS参数、透明鉴权接入完整MML脚本（huawei.com + huawei123/123） |
| 4 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011305 Radius鉴权接入/调测Radius鉴权接入/调测透明接入_95351130.md` | 透明接入（TRANS_NON_AUTH）调测流程、DSP PDUSESSION查询、LST APNAUTHATTR核对、**未要求AAA Server**（证明透明接入不依赖Radius功能） |
| 5 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011305 Radius鉴权接入/调测Radius鉴权接入/调测透明鉴权接入_95351132.md` | 透明鉴权接入（TRANS_AUTH）调测流程、**要求AAA Server工作正常**（证明依赖Radius功能）、数据准备引用WSFD-011306配置RADIUS功能、OM Portal用户跟踪Access Request消息验证（user-name一致、user-password加密）、LST RDSSVRGRP查询服务器组 |
| 6 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011305 Radius鉴权接入/调测Radius鉴权接入/调测非透明接入_95351131.md` | 非透明接入（NON_TRANS）调测流程、**要求AAA Server工作正常**（证明依赖Radius功能）、UE携带用户名密码接入、Access Request消息验证（user-name与PCO一致、user-password加密） |
| 7 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011305 Radius鉴权接入/调测Radius鉴权接入/调测本地鉴权接入_95351133.md` | 本地鉴权接入（LOC_AUTH）调测流程、**未要求AAA Server**（证明本地鉴权不依赖Radius功能）、公用用户名密码数据准备（来自激活配置）、终端用户名密码核对步骤 |
| 8 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011305 Radius鉴权接入/调测Radius鉴权接入_50176280.md` | 通用调测入口、3步通用流程（终端接入→DSP PDUSESSION→LST APNAUTHATTR） |
| 9 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011305 Radius鉴权接入_50176277.md` | 特性根索引文件（仅标题，无实质内容） |

### 7.3 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| AUTHMODE / ACCESSMODE | 鉴权接入模式 | SET APNAUTHATTR 参数，4种取值：TRANS_NON_AUTH/TRANS_AUTH/NON_TRANS/LOC_AUTH |
| TRANS_NON_AUTH | 透明接入（透明不鉴权） | 用户接入 UNC 时无需鉴权 |
| TRANS_AUTH | 透明鉴权接入（匿名接入） | UNC 使用系统配置公用账密到 AAA 鉴权 |
| NON_TRANS | 非透明接入（不透明接入） | UE PCO 携账密，UNC 到 AAA 鉴权 |
| LOC_AUTH | 本地鉴权接入 | UNC 本地匹配 UE PCO 账密，不调 Radius |
| PCO | Protocol Configuration Option（协议配置选项） | 用户在创建过程中携带鉴权请求信息的字段 |
| PAP | Password Authentication Protocol | Radius 鉴权协议之一（明文密码，UNC 支持） |
| CHAP | Challenge Handshake Authentication Protocol | Radius 鉴权协议之一（挑战应答，UNC 支持） |
| AAA Server | Authentication/Authorization/Accounting Server | 鉴权/授权/计费服务器，与客户端交互使用 Radius 协议（即 Radius Server） |
| COMMONUSERNAME/PASS | 公用用户名/密码 | UNC APN 级公用配置，TRANS_AUTH 代发、LOC_AUTH 本地匹配基准 |
| ALM-100197 | RADIUS鉴权服务器无响应 | Radius 鉴权服务器无响应告警 |
| UDM 签约数据参与 AAA 鉴权 | v02+ 特性 | UNC 支持用户是否使用 UDM 签约数据参与决策进行 AAA 鉴权 |

---

## 8. 文档一致性说明（配置树 vs 产品文档）

> 配置树仅用于定位特性 ID，以下记录以产品文档实际内容为准时发现的关键结论，供 Stage 3 横向分析参考。

### 8.1 与配置树/文档清单的差异

| # | 维度 | 配置树/文档清单描述 | 产品文档实际内容 | 差异类型 |
|---|------|---------------------|-----------------|---------|
| 1 | 鉴权方式分类 | 文档清单标题："AUTHMODE鉴权方式(透明/透明鉴权/不透明/本地)" | 产品文档"定义"章节明确 **4种接入方式**：透明接入、非透明接入、透明鉴权接入、本地鉴权接入；MML 参数名为 **ACCESSMODE**（非 AUTHMODE） | 命名差异：清单用 AUTHMODE，文档实际参数为 ACCESSMODE；4 种方式一致 |
| 2 | License要求 | 文档清单标注"[★核心]" | 产品文档明确声明"**本特性无需获得License许可**" | 差异：与同域★核心需License特性不同，本特性无License |
| 3 | Radius依赖 | 文档清单未细化 | 产品文档"与其他特性交互"明确：**仅 NON_TRANS、TRANS_AUTH 依赖 WSFD-011306**；TRANS_NON_AUTH、LOC_AUTH 不依赖 | 补全：4 种方式的 Radius 依赖差异是核心结论 |
| 4 | PPP用户限制 | 文档清单未提及 | 产品文档"应用限制"明确：**PPP 用户暂不支持本地鉴权功能** | 补全：LOC_AUTH 方式的重要约束 |
| 5 | 与其他鉴权特性关系 | 文档清单列 WSFD-010301/WSFD-108007 | 本特性文档**未直接引用** WSFD-010301/WSFD-108007（仅引用 WSFD-011306） | 推断关系：基于特性语义推断，Stage 3 横向验证 |

### 8.2 ★AUTHMODE 4方式与 Radius 功能联动核心结论（文档依据汇总）

| 联动维度 | TRANS_NON_AUTH | TRANS_AUTH | NON_TRANS | LOC_AUTH | 文档依据 |
|---------|----------------|------------|-----------|----------|---------|
| Radius 功能依赖 | **否** | **是（必须）** | **是（必须）** | **否** | 特性概述"与其他特性的交互"明确声明；4 个调测文档"必备事项"佐证（TRANS_AUTH/NON_TRANS 要求 AAA Server，TRANS_NON_AUTH/LOC_AUTH 不要求） |
| AAA Server 必要性 | 否 | 是 | 是 | 否 | 同上 |
| 鉴权协议 | 无 | PAP/CHAP via Radius | PAP/CHAP via Radius | UNC 本地匹配 | 特性概述"原理概述"章节 |
| 计费可选 | 是（参考WSFD-011306） | 是 | 是 | 否 | 特性概述"原理概述"各方式描述 |
| PPP 用户支持 | 是 | 是 | 是 | **否（限制）** | 特性概述"应用限制"章节 |

**核心联动结论**：

- **需要 Radius 功能（WSFD-011306）的鉴权方式**：**TRANS_AUTH（透明鉴权接入）** 和 **NON_TRANS（不透明接入）** —— 这两种方式必须开启 Radius 功能，AAA Server 必须工作正常。
- **不需要 Radius 功能的鉴权方式**：**TRANS_NON_AUTH（透明接入）** 和 **LOC_AUTH（本地鉴权接入）** —— 这两种方式不调用 Radius，前者无鉴权，后者 UNC 本地匹配。
- **PPP 用户约束**：仅 **LOC_AUTH（本地鉴权）** 方式不支持 PPP 用户，其他 3 种方式均支持。

---

## 附录 A：AUTHMODE 4方式速查表

| 维度 | TRANS_NON_AUTH（透明） | TRANS_AUTH（透明鉴权） | NON_TRANS（不透明） | LOC_AUTH（本地鉴权） |
|------|----------------------|-----------------------|--------------------|--------------------|
| 中文 | 透明接入 | 透明鉴权接入（匿名） | 非透明接入 | 本地鉴权接入 |
| 鉴权 | 否 | 是（UNC→AAA） | 是（UE→UNC→AAA） | 是（UNC本地） |
| Radius功能 | 不需要 | **必须** | **必须** | 不需要 |
| 账密来源 | 不适用 | UNC公用配置 | UE PCO携带 | UE PCO + UNC本地 |
| 用户感知 | 无 | 无（匿名） | 需输入账密 | 需输入账密 |
| 计费 | 可选 | 可选 | 可选 | 不涉及 |
| 地址空间 | 运营商 | ISP/企业网 | ISP/企业网 | 同其他 |
| PPP用户 | 支持 | 支持 | 支持 | **不支持** |
| 适用场景 | 运营商自营 | 运营商统一账密 | ISP/企业网AAA | 无AAA的ISP/企业网 |
| UDM签约参与(v02+) | - | 支持 | 支持 | - |

---

## 附录 B：source_evidence_ids 占位映射

| Evidence ID | 对应来源 |
|------------|---------|
| EV-FK-01 | 特性概述_50176278.md |
| EV-FK-02 | 参考信息_50176281.md |
| EV-FK-03 | 激活Radius鉴权接入_50176279.md |
| EV-FK-04 | 调测透明接入_95351130.md |
| EV-FK-05 | 调测透明鉴权接入_95351132.md |
| EV-FK-06 | 调测非透明接入_95351131.md |
| EV-FK-07 | 调测本地鉴权接入_95351133.md |
| EV-FK-08 | 调测Radius鉴权接入_50176280.md |
| EV-FK-09 | 特性根索引_50176277.md（仅标题） |
