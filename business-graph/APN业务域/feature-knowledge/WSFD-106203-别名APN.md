# WSFD-106203 别名APN 知识文档

> 聚焦 APN 业务域别名APN（虚拟APN）机制的 UNC 侧特性
> 同一特性ID（WSFD-106203）在 UNC 不同网元角色下含义不同：SGSN/MME 侧为"协商APN→别名APN"的 DNS 解析屏蔽；GGSN/PGW-C/SMF 侧为"别名APN→真实APN"的业务资源归一
> 与 APN 基础配置/会话管理（WSFD-010501）协同：别名APN是 APN 选择/PDU 会话建立前的映射预处理环节

---

## 0. 元数据（三层图谱Schema字段）

| 字段 | 取值 |
|------|------|
| feature_id | WSFD-106203 |
| feature_name | 别名APN |
| feature_group | APN基础 |
| parent_feature_id | WSFD-010501 会话管理（UNC/SMF）（推断：别名APN是 APN 协商/PDU 会话建立前的映射预处理） |
| applicable_nf_map | `{"UNC": ["GGSN", "PGW-C", "SMF", "SGSN", "MME"]}` |
| variant_dimensions | ["网元角色视角(SGSN/MME 侧 DNS 屏蔽型 ↔ GGSN/PGW-C/SMF 侧 资源归一型)", "映射方向(协商APN→别名APN ↔ 别名APN→真实APN)", "接入代际(2G&3G SGSN / 4G MME / 4G PGW-C / 5G SMF)", "用户范围粒度(ALL_USER / 指定切片 SST+SD / IMSI前缀号段)", "License 控制项(LKV2AAPN01 GGSN/PGW-C/SMF侧 ↔ LKV2ALIASAPN02 SGSN/MME侧)"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-01, EV-FK-02, EV-FK-03, EV-FK-04, EV-FK-05, EV-FK-06, EV-FK-07, EV-FK-08, EV-FK-09, EV-FK-10] |
| license_required | 是（双License项）：<br>- GGSN/PGW-C/SMF 侧：`82200BNM LKV2AAPN01 别名APN-USM`<br>- SGSN/MME 侧：`82207546 LKV2ALIASAPN02 别名APN` |

---

## 1. 概述

### 1.1 特性定义（是什么）

别名APN（Alias APN / Virtual APN）是 UNC 为了**兼容现网中存在使用相同资源的多个APN**而提出的概念。其本质是 UNC 侧配置的 **APN 映射表**，将用户激活时携带的请求APN（协商APN）映射为目标APN（别名APN / 真实APN），以屏蔽用户侧APN差异、降低用户配置要求、共用系统资源。

**关键概念区分（同特性ID在不同网元角色下含义相反）**：

| UNC 角色 | 映射方向 | 映射前/映射后语义 | 用途 |
|---------|---------|------------------|------|
| SGSN/MME（Pre-5G 控制面） | 协商APN（真实）→ **别名APN** | 协商APN是真实的，映射后的别名APN用于 DNS 解析 | 屏蔽用户APN差异，节约DNS资源，简化网络配置 |
| GGSN/PGW-C/SMF（业务网关控制面） | **别名APN** → 真实APN | 别名APN是用户侧传来的，映射后的真实APN用于业务资源 | 不同APN共用相同系统资源，便于资源分配组合 |

> 来源：根索引 `WSFD-106203 别名APN_64082528.md`（"从SGSN/MME的角度 / 从GGSN-C/PGW-C/SMF的角度"双视角定义）；SGSN/MME 概述 `_68358224.md`（"定义"）；GGSN/PGW-C/SMF 概述 `_34797879.md`（"定义"）

### 1.2 适用NF（UNC网元）

| 涉及NF | 网元角色 | 支持版本 | 功能说明 | License |
|--------|---------|---------|---------|---------|
| SGSN | Pre-5G 控制面（2/3G） | UNC 20.3.0及后续版本 | 根据配置，将协商后的APN映射成别名APN，用于DNS解析 | LKV2ALIASAPN02 |
| MME | Pre-5G 控制面（4G） | UNC 20.0.0及后续版本 | 根据配置，将协商后的APN映射成别名APN，用于DNS解析 | LKV2ALIASAPN02 |
| GGSN | 业务网关控制面（2/3G） | UNC 20.3.0及后续版本 | 本地配置别名APN到真实APN的映射关系 | LKV2AAPN01 |
| PGW-C | 业务网关控制面（4G） | UNC 20.3.0及后续版本 | 本地配置别名APN到真实APN的映射关系 | LKV2AAPN01 |
| SMF | 业务网关控制面（5G） | UNC 20.3.0及后续版本 | 本地配置别名APN到真实APN的映射关系 | LKV2AAPN01 |

> 来源：SGSN/MME 概述 `_68358224.md`、GGSN/PGW-C/SMF 概述 `_34797879.md`（"可获得性/涉及NF"章节）

### 1.3 版本信息

**SGSN/MME 侧发布历史**：

| 特性版本 | 发布版本 | 发布说明 |
|---------|---------|---------|
| 01 | 20.0.0 | 首次发布（MME 率先支持） |

> 注：SGSN 在 UNC 20.3.0 及后续版本支持；MME 在 UNC 20.0.0 及后续版本支持。

**GGSN/PGW-C/SMF 侧发布历史**：

| 特性版本 | 发布版本 | 发布说明 |
|---------|---------|---------|
| 1 | 20.3.0 | 首次发布 |

> 来源：SGSN/MME 概述 `_68358224.md`、GGSN/PGW-C/SMF 概述 `_34797879.md`（"发布历史"章节）

### 1.4 License

本特性**必须获得 License 许可**后才能使用（与同域地址分配特性 WSFD-010502"无 License"不同）。**注意两套 License 分别对应两套网元**：

| License编号 | License名称 | 适用网元 |
|------------|------------|---------|
| 82200BNM | LKV2AAPN01 别名APN-USM | GGSN/PGW-C/SMF（业务网关控制面） |
| 82207546 | LKV2ALIASAPN02 别名APN | SGSN/MME（Pre-5G 控制面） |

激活时需通过 `SET LICENSESWITCH` 打开对应 License 项开关（如 `LICITEM="LKV2AAPN01"` 或 `LICITEM="LKV2ALIASAPN02"`）。

> 来源：GGSN/PGW-C/SMF 概述 `_34797879.md`（"License支持"）、SGSN/MME 概述 `_68358224.md`（"License支持"）、激活脚本 `_34797880.md` & `_68358227.md`

### 1.5 前置条件与依赖

**GGSN/PGW-C/SMF 侧**：

| 前置条件 | 说明 |
|---------|------|
| 阅读特性概述 | 仔细阅读 WSFD-106203 别名APN特性概述（适应于GGSN/PGW-C/SMF） |
| 配置真实APN | 已通过 `ADD APN` 配置真实APN（转换APN必须先在 ADD APN 中存在） |
| 加载License | 已加载 License 控制项 82200BNM LKV2AAPN01 别名APN-USM |

**SGSN/MME 侧**：

| 前置条件 | 说明 |
|---------|------|
| 阅读特性概述 | 仔细阅读 WSFD-106203 别名APN特性概述（适用于SGSN/MME） |
| 加载License | 已加载 License 控制项 82207546 LKV2ALIASAPN02 别名APN |
| 签约缺省APN | （调测时）测试用户的签约缺省APN需已配置 |

> 来源：激活脚本 `_34797880.md`、`_68358227.md`（"必备事项/前提条件"章节）

### 1.6 与其他特性的交互

**GGSN/PGW-C/SMF 侧**：明确声明"本特性不涉及与其他特性的交互"。

**SGSN/MME 侧**：与 WSFD-106004 请求信息纠正功能存在**顺序依赖关系**：

| 交互类型 | 相关特性 | 控制项 | 交互说明 |
|---------|---------|--------|---------|
| 影响 | WSFD-106004 请求信息纠正功能（适用于SGSN、MME） | 82205928 请求信息纠正功能 | 用户激活消息中携带错误APN时，**先执行请求APN的纠正功能，再执行别名APN纠正**（顺序约束） |

> 来源：GGSN/PGW-C/SMF 概述 `_34797879.md`、SGSN/MME 概述 `_68358224.md`（"与其他特性的交互"章节）

### 1.7 客户价值

**GGSN/PGW-C/SMF 侧**：

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | GPRS/UMTS/EPC/5G网络中，运营商**不需要全网修改APN的规划和配置**，减少了运营商网络配置和维护管理的复杂度 |
| 用户 | 用户无需在终端上做任何修改，不同APN下的用户就可以共享系统资源 |

**SGSN/MME 侧**：

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | ① 运营商合并和重组场景下，将早期多个APN映射成别名APN，**节约DNS资源**，减少配置复杂度；② 网络业务扩展场景下，将部分优质客户的原有特定业务APN映射为别名APN提供服务，或将漫游地用户的特定业务APN映射为别名APN，**区分本地用户提供区别服务**，可操作性更高 |
| 用户 | 运营商网络调整或者新业务扩展时，用户无需做任何修改 |

> 来源：GGSN/PGW-C/SMF 概述 `_34797879.md`、SGSN/MME 概述 `_68358224.md`（"客户价值"章节）

### 1.8 应用场景

**别名APN主要适用于以下场景**（两套网元共享的场景表述）：

1. **运营商合并和重组**：为了兼容现网中使用相同资源的多个APN，可将某APN的业务映射到另一APN上（多APN归一）
2. **网络改建时新规划APN**：为了不影响原规划APN的使用，只需将原规划的APN映射到新规划APN上即可
3. **网络业务扩展**（SGSN/MME侧）：将部分优质客户的原有特定业务APN映射为别名APN提供服务，或将漫游地用户的特定业务APN映射为别名APN，区分本地用户提供区别服务

**驱动问题**：终端上的APN设置多种多样，而运营商对这些终端提供相同的APN业务。如果在UNC上配置众多的APN或者通知用户更改配置，都将提高运营成本。通过别名APN功能，将所有已知的APN都映射为同一个APN进行业务。

> 来源：GGSN/PGW-C/SMF 概述 `_34797879.md`（"应用场景"）、SGSN/MME 概述 `_68358224.md`（"应用场景"）、根索引 `_64082528.md`

### 1.9 对系统的影响

| 网元侧 | 影响说明 |
|--------|---------|
| GGSN/PGW-C/SMF | 随着别名APN接入用户数的增加，系统资源占用会一直增大，**CPU占用率会相应上升** |
| SGSN/MME | 本特性对系统无影响 |

> 来源：GGSN/PGW-C/SMF 概述 `_34797879.md`、SGSN/MME 概述 `_68358224.md`（"对系统的影响"章节）

### 1.10 应用限制

**GGSN/PGW-C/SMF 侧关键限制**：当某个别名APN下**还存在用户或会话时，该别名APN不允许直接删除**，执行 `RMV APNALIAS` UNC会拒绝该请求。如果想删除此类别名APN，需要**先锁定此别名APN，再批量去激活该别名APN下用户，最后删除别名APN**。

**SGSN/MME 侧关键限制**：别名APN转换后，后续的PDP激活请求等消息中携带的是别名APN，S-CDR中采用的也是别名APN。**目前系统默认后续的PDP激活请求等消息和S-CDR中携带的是别名APN，无法通过参数修改**。

> 来源：GGSN/PGW-C/SMF 概述 `_34797879.md`、SGSN/MME 概述 `_68358224.md`（"应用限制"章节）

### 1.11 特性规格

**GGSN/PGW-C/SMF 侧规格**：

| 规格名称 | 规格指标 |
|---------|---------|
| 支持最大别名APN数量 | 1000 个 |
| 一个APN下最多可以配置的APN别名数 | 500 个 |

**SGSN/MME 侧规格**：

| 规格名称 | 规格指标 |
|---------|---------|
| APN映射表支持的映射记录数 | 1024 条 |

> 来源：GGSN/PGW-C/SMF 概述 `_34797879.md`、SGSN/MME 概述 `_68358224.md`（"特性规格"章节）

### 1.12 计费与话单

| 网元侧 | 计费与话单 |
|--------|-----------|
| GGSN/PGW-C/SMF | 使用别名APN功能时，**可以配置话单中使用的APN类型为别名APN或者真实APN**（通过 SET APNREPORTATTR 将真实APN的 PCF/CHF 配置为 SERVICE） |
| SGSN/MME | 本特性不涉及计费与话单（但 S-CDR 中默认采用别名APN，无法修改） |

> 来源：GGSN/PGW-C/SMF 概述 `_34797879.md`（"计费与话单"）、SGSN/MME 概述 `_68358224.md`（"计费与话单"）、激活脚本 `_34797880.md`

### 1.13 遵循标准

**GGSN/PGW-C/SMF 侧遵循标准**（SGSN/MME 侧"不涉及标准约束"）：

| 标准类别 | 标准编号 | 标准名称 |
|---------|---------|---------|
| 3GPP | 23.060 | General Packet Radio Service (GPRS) Service Description; Stage 2 |
| 3GPP | 29.060 | GPRS; GPRS Tunnelling Protocol (GTP) across the Gn and Gp interface |
| 3GPP | 29.061 | Interworking between PLMN supporting packet based services and PDN |
| 3GPP | 23.214 | Architecture enhancements for control and user plane separation of EPC nodes |
| 3GPP | 29.244 | Interface between the Control Plane and the User Plane of EPC Nodes |

> 来源：GGSN/PGW-C/SMF 概述 `_34797879.md`、SGSN/MME 概述 `_68358224.md`（"遵循标准"章节）

---

## 2. 核心概念

### 2.1 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| APN | Access Point Name | GPRS/UMTS/EPS系统定义的网络标识，既是路由标识（寻址GGSN/PGW-C）又是业务域标识（区分外部PDN/业务类型） |
| APN NI | APN Network Identifier | APN的必选部分，标识外部数据网络类型，需在HSS签约。本特性在2/3/4G场景中均指APN NI |
| APN OI | APN Operator Identifier | APN的可选部分，标识运营商类型，格式符合DNS规范，使用".gprs"结尾 |
| DNN | Data Network Name | 5G场景中的APN等价物。3GPP TS23.501 R15定义DNN与APN具有相同含义和信息 |
| 别名APN | Alias APN / Virtual APN | UNC映射表中的APN别名，用于屏蔽用户侧APN差异或共用系统资源 |
| 真实APN | Real APN / Convert APN | GGSN/PGW-C/SMF侧映射后的目标APN，承载实际业务资源 |
| 转换APN | ConvertAPN（CONVERTAPN） | ADD APNALIAS 命令参数，等同于真实APN |
| 协商APN | Negotiated APN | SGSN/MME侧经签约匹配（失败则经APN纠错）后的APN，是真实的APN |
| IMSI前缀 | IMSI_PREFIX | SGSN/MME侧基于IMSI最长匹配原则匹配用户的号段 |
| 切片 | SST + SD | 5G切片标识（SST=切片业务类型，SD=切片细分标识），5G用户按切片匹配别名APN |

> 来源：根索引 `_64082528.md`、SGSN/MME 概述 `_68358224.md` 与 GGSN/PGW-C/SMF 概述 `_34797879.md`（"原理概述/相关概念"章节）

### 2.2 APN的双重角色（路由标识 vs 业务域标识）

APN 在网络中具有两个根本作用，别名APN在两侧的语义差异正是源于这两个作用：

```
┌─────────────────────────────────────────────────────────────┐
│ APN 作为路由标识（SGSN/MME 侧）                              │
│                                                             │
│   SGSN/MME ──协商APN──> DNS服务器 ──> GGSN/PGW-C IP 地址     │
│                                                             │
│   ★ 别名APN 用途：屏蔽用户APN差异，节约DNS资源              │
│   ★ 映射方向：协商APN（真实）→ 别名APN（用于DNS解析）       │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ APN 作为业务域标识（GGSN/PGW-C/SMF 侧）                     │
│                                                             │
│   GGSN/PGW-C/SMF ──真实APN──> 外部PDN / 业务域              │
│                                                             │
│   ★ 别名APN 用途：不同APN共用相同系统资源                   │
│   ★ 映射方向：别名APN（用户传来）→ 真实APN（业务资源）      │
└─────────────────────────────────────────────────────────────┘
```

> 来源：根索引 `WSFD-106203 别名APN_64082528.md`（图1 APN作为路由标识 / 图2 APN作为业务域标识）

### 2.3 对象模型

**GGSN/PGW-C/SMF 侧配置对象体系**：

```
┌───────────────────────────────────────────────────────────────┐
│ UNC（GGSN/PGW-C/SMF）侧别名APN配置体系                         │
│                                                               │
│   ┌──────────────┐                                            │
│   │ 真实APN      │ ← ADD APN（转换APN必须先存在）              │
│   │ (apn5)       │   + SET APNREPORTATTR（PCF/CHF=SERVICE）   │
│   └──────┬───────┘                                            │
│          │                                                    │
│          │ 多对一映射（不同别名APN可指向同一真实APN）          │
│          │                                                    │
│   ┌──────┴───────────────────────────────────────────┐        │
│   │ 别名APN映射表（ADD APNALIAS）                     │        │
│   │ ┌────────────────────────────────────────────┐   │        │
│   │ │ ALIASAPN="apn1" → CONVERTAPN="apn5"        │   │        │
│   │ │ ALIASAPN="apn2" → CONVERTAPN="apn5"        │   │        │
│   │ │ （SUBRANGE=ALL_USER / SPECIFIC_NS[SST+SD]）│   │        │
│   │ └────────────────────────────────────────────┘   │        │
│   └──────────────────────────────────────────────────┘        │
│                                                               │
│   生命周期管理：                                               │
│   ├── LCK APNALIAS  （锁定，禁止新用户接入）                  │
│   ├── DEA SMCTX     （批量去活该别名APN下用户）               │
│   ├── RMV APNALIAS  （删除别名APN配置，需无活跃会话）         │
│   └── SET DEACTIVERATE （配置批量去活速率 RATE=1000）         │
└───────────────────────────────────────────────────────────────┘
```

**SGSN/MME 侧配置对象体系**：

```
┌───────────────────────────────────────────────────────────────┐
│ UNC（SGSN/MME）侧别名APN配置体系                               │
│                                                               │
│   ┌──────────────────────────────────────────────────┐        │
│   │ 别名APN映射表（ADD ALIASAPN）                     │        │
│   │ ┌────────────────────────────────────────────┐   │        │
│   │ │ IMSIPRE="12345" + OLDAPN="example.com"     │   │        │
│   │ │           ↓                                 │   │        │
│   │ │ NEWAPN="huawei.com"（别名APN，用于DNS）     │   │        │
│   │ │ （SUBRANGE=IMSI_PREFIX，按IMSI最长匹配）    │   │        │
│   │ └────────────────────────────────────────────┘   │        │
│   └──────────────────────────────────────────────────┘        │
│                                                               │
│   生命周期管理：                                               │
│   ├── MOD ALIASAPN  （修改别名APN配置）                       │
│   ├── RMV ALIASAPN  （删除别名APN配置）                       │
│   └── LST ALIASAPN  （查询别名APN配置）                       │
└───────────────────────────────────────────────────────────────┘
```

> 来源：参考信息 `_34797882.md`、`_68358229.md`；激活脚本 `_34797880.md`、`_68358227.md`

### 2.4 在 APN 业务域的角色

别名APN 在 APN 业务域的接入与会话管理链路中扮演**映射预处理**的角色，位于 APN 协商之后、PDU 会话建立/DNS 解析之前：

```
用户终端（UE/MS）
    │
    │ 携带请求APN
    ▼
[SGSN/MME] APN 签约匹配
    │  匹配失败 → APN 纠错（WSFD-106004）
    │  匹配成功 → 协商APN
    ▼
[SGSN/MME] ★ 别名APN映射（WSFD-106203 SGSN/MME侧）
    │  按IMSI最长匹配 + 协商APN 查映射表
    │  命中 → 映射为别名APN（用于DNS解析寻址GGSN/PGW-C）
    │  未命中 → 仍用协商APN
    ▼
DNS 解析 → 寻址到 GGSN/PGW-C/SMF
    │
    ▼
[GGSN/PGW-C/SMF] 接收用户侧传来的APN（视为别名APN）
    │
    ▼
[GGSN/PGW-C/SMF] ★ 别名APN映射（WSFD-106203 GGSN/PGW-C/SMF侧）
    │  按用户范围（ALL_USER / 切片）查别名APN映射表
    │  命中 → 映射为真实APN（用于业务资源、统计、计费）
    │  未命中 → 仍用别名APN
    ▼
基于真实APN 的 PDU 会话建立 / 业务承载 / 计费 / QoS 策略
```

**与 APN 基础配置/会话管理（WSFD-010501）的关系**：

1. **依赖关系**：别名APN是 APN 协商（WSFD-010501 内的 APN 选择子流程）之后的**映射预处理环节**，位于 PDU 会话建立之前
2. **资源共用**：GGSN/PGW-C/SMF 侧通过别名APN→真实APN映射，让多个APN共用 WSFD-010501 配置的真实APN系统资源（计费、QoS、安全策略）
3. **DNS寻址协同**：SGSN/MME 侧映射后的别名APN用于 DNS 解析寻址 GGSN/PGW-C，间接影响 WSFD-010501 中"为PDU会话选择UPF"（WSFD-107010）的网元选择输入
4. **统计归一**：GGSN/PGW-C/SMF 侧映射后，所有别名APN的业务**以真实APN的信息进行统计**，便于统一监控运维

> 来源：根索引 `_64082528.md`、GGSN/PGW-C/SMF 概述 `_34797879.md`（图1 别名APN原理图）、SGSN/MME 概述 `_68358224.md`（图1 针对用户IMSI将协商的APN配置映射成别名APN）

---

## 3. 原理与流程

### 3.1 GGSN/PGW-C/SMF 侧实现原理（别名APN→真实APN 资源归一）

UNC 提供**别名APN到真实APN的配置映射**，将用户激活时携带的请求APN（视为别名APN）映射到真实APN上激活，使用真实APN上的业务。

**核心机制**：
- 配置 APN"apn1"和"apn2"为 APN"apn5"的别名
- 别名APN"apn1"和"apn2"在 UNC 上**使用与 APN"apn5"相同的资源**
- 并且**以 APN"apn5"的信息进行统计**

**映射关系约束**：
- 别名APN与转换APN为**多对一**的关系（多个别名可指向同一真实APN）
- 不同的转换APN下**不能配置相同的别名APN**（5G切片场景例外：不同切片下不同转换APN可配置相同别名APN）
- 别名APN**不能**与 ADD APN 中已配置的APN相同
- 转换APN**必须**已经在 ADD APN 中配置

**用户范围匹配（5G切片感知）**：
- 5G用户：先使用指定切片（SST+SD）查询，如果未查询到，再对所有用户查询
- 2/3/4G用户：直接对所有用户查询

> 来源：GGSN/PGW-C/SMF 概述 `_34797879.md`（"原理概述/特性原理"）、激活脚本 `_34797880.md`（操作步骤说明）

### 3.2 SGSN/MME 侧实现原理（协商APN→别名APN DNS屏蔽）

UNC 支持运营商根据 **IMSI的最长匹配原则**，针对用户IMSI将协商的APN配置映射成别名APN。

**APN转换过程（7步）**：

1. UNC 获取用户的IMSI和请求的APN信息
2. 对用户请求的APN进行**签约匹配**
   - 匹配成功 → UNC采用签约APN进行下一步
   - 匹配失败 → UNC进行 **APN纠错**（参见 WSFD-106004）以获取协商的APN，然后采用协商的APN进行下一步
3. 采用获取的用户IMSI信息**匹配别名APN映射表中的用户IMSI**
4. 查看用户是否在配置的 **IMSI号段** 内
5. 如果在配置的IMSI号段内，再查看**协商的APN是否在别名APN映射表**
6. 如果在映射表中，则**根据配置将协商的APN映射成别名APN**
7. 否则仍使用协商的APN

**关键性质**：别名APN在 **APN协商之后** 进行转换，因此**别名APN无需在HLR中签约**。转换后，后续的PDP激活请求等消息中携带的是别名APN，S-CDR中采用的也是别名APN。

> 来源：SGSN/MME 概述 `_68358224.md`（"原理概述/APN转换过程"）

### 3.3 SGSN/MME 侧应用举例（IMSI最长匹配 + 映射决策表）

运营商进行业务合并，别名APN映射表中配置的IMSI前缀为 `460001`，原始APN（test1.com, test2.com, test3.com）对应别名APN（huawei.com），未配置APN（test4.com）。

| 用户IMSI与协商APN | IMSI号段匹配 | APN映射表匹配 | 处理结果 | DNS查询使用的APN |
|------------------|-------------|---------------|---------|----------------|
| (460001001, test1.com) | 在号段内（460001前缀匹配） | test1.com 在映射表 | 映射为 huawei.com | **huawei.com** |
| (460001002, test2.com) | 在号段内（460001前缀匹配） | test2.com 在映射表 | 映射为 huawei.com | **huawei.com** |
| (460000000, test3.com) | **不在号段内**（460001前缀不匹配） | test3.com 在映射表 | 不进行别名APN转换 | test3.com |
| (460001003, test4.com) | 在号段内（460001前缀匹配） | **test4.com 不在映射表** | 不进行别名APN转换 | test4.com |

**双条件约束**：IMSI号段匹配 AND 协商APN在映射表中，两个条件**同时满足**才执行别名APN转换。

> 来源：SGSN/MME 实现原理 `_68358226.md`（表1 映射协商的APN）

### 3.4 业务流程（端到端别名APN映射）

端到端的别名APN映射流程（综合两侧）：

```
┌──────────────────────────────────────────────────────────────┐
│ 1. 用户激活请求                                               │
│    UE/MS 携带请求APN 发起附着/PDN激活/PDU会话建立             │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│ 2. SGSN/MME 侧 APN 协商（WSFD-010501 APN选择子流程）         │
│    2a. 签约匹配（HLR/HSS）                                   │
│    2b. 匹配失败 → APN纠错（WSFD-106004，先于别名APN）         │
│    2c. 输出：协商APN（真实APN）                              │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│ 3. SGSN/MME 侧 别名APN映射（本特性，LKV2ALIASAPN02）          │
│    3a. 按IMSI最长匹配查IMSI号段                              │
│    3b. 查协商APN是否在映射表                                 │
│    3c. 双条件命中 → 映射为别名APN（用于DNS）                 │
│    3d. 未命中 → 仍用协商APN                                  │
│    注：别名APN无需在HLR签约                                  │
└────────────────────────┬─────────────────────────────────────┘
                         │ 使用映射后APN 发起DNS查询
                         ▼
┌──────────────────────────────────────────────────────────────┐
│ 4. DNS 解析（寻址GGSN/PGW-C/SMF）                            │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│ 5. GGSN/PGW-C/SMF 侧 别名APN映射（本特性，LKV2AAPN01）        │
│    5a. 将用户侧传来的APN视为别名APN                          │
│    5b. 按用户范围（ALL_USER / 切片SST+SD）查别名APN映射表    │
│    5c. 命中 → 映射为真实APN                                  │
│    5d. 未命中 → 仍用别名APN                                  │
│    注：5G用户先按切片查，未中再按ALL_USER查                  │
└────────────────────────┬─────────────────────────────────────┘
                         │ 使用真实APN
                         ▼
┌──────────────────────────────────────────────────────────────┐
│ 6. 业务执行（基于真实APN）                                   │
│    - 真实APN 的系统资源共用（计费/QoS/安全/业务控制）         │
│    - 以真实APN 信息进行统计                                  │
│    - 话单中APN类型可配置为别名APN或真实APN（SET APNREPORTATTR）│
│    - 完成 PDU 会话建立（WSFD-010501）                        │
└──────────────────────────────────────────────────────────────┘
```

### 3.5 协议交互

| 接口 | 交互网元 | 消息类型 | 说明 |
|------|---------|---------|------|
| Gr/S6a（2/3/4G） | SGSN/MME ↔ HLR/HSS | 签约数据查询 | 获取用户签约APN，用于APN协商 |
| 内部 | UNC（SGSN/MME）内部 | IMSI+APN映射 | 按IMSI最长匹配查别名APN映射表 |
| DNS（Gn/Gp接口） | SGSN/MME ↔ DNS | DNS解析 | 使用别名APN（SGSN/MME侧）寻址GGSN/PGW-C |
| 内部 | UNC（GGSN/PGW-C/SMF）内部 | 别名APN查表 | 按用户范围查别名APN→真实APN映射表 |
| N7/Gx | PCF/PCRF ↔ SMF/PGW-C | 策略下发 | 基于真实APN执行策略（SET APNREPORTATTR PCF=SERVICE） |
| Gy | SMF/PGW-C ↔ CHF | 计费交互 | 基于真实APN（SET APNREPORTATTR CHF=SERVICE） |

---

## 4. 配置规则

### 4.1 激活步骤

#### 4.1.1 GGSN/PGW-C/SMF 侧激活步骤（6步）

```
步骤1：打开License开关
  └── SET LICENSESWITCH:LICITEM="LKV2AAPN01",SWITCH=ENABLE

步骤2：配置真实APN
  └── ADD APN:APN="apn5"

步骤3：配置真实APN的上报属性（自动生成SET APNREPORTATTR记录）
  └── SET APNREPORTATTR:APN="apn5",PCF=SERVICE,CHF=SERVICE

步骤4：配置别名APN和转换APN
  └── ADD APNALIAS:SUBRANGE=ALL_USER,ALIASAPN="apn1",CONVERTAPN="apn5"
  └── ADD APNALIAS:SUBRANGE=ALL_USER,ALIASAPN="apn2",CONVERTAPN="apn5"
  （5G切片场景：SUBRANGE=SPECIFIC_NS,SST=1,SD=123123）

步骤5（可选）：批量去活前锁定别名APN
  └── LCK APNALIAS:...,LOCKED=ENABLE,APNTYPE=ALIAS_APN

步骤6（可选）：删除别名APN（需无活跃会话）
  └── RMV APNALIAS:...,APNTYPE=ALIAS_APN
```

> 来源：激活脚本 `_34797880.md`（"操作步骤"）

#### 4.1.2 SGSN/MME 侧激活步骤（3步）

```
步骤1：打开License开关
  └── SET LICENSESWITCH:LICITEM="LKV2ALIASAPN02",SWITCH=ENABLE

步骤2：添加别名映射表的记录
  └── ADD ALIASAPN:SUBRANGE=IMSI_PREFIX,IMSIPRE="12345",
                 OLDAPN="example.com",NEWAPN="huawei.com"

步骤3（可选）：修改/删除/查询别名APN
  ├── MOD ALIASAPN
  ├── RMV ALIASAPN
  └── LST ALIASAPN
```

> 来源：激活脚本 `_68358227.md`（"操作步骤"）

### 4.2 MML命令清单

#### 4.2.1 GGSN/PGW-C/SMF 侧核心命令（参考信息5条 + 关联命令）

| 命令 | 用途 | 关键参数 |
|------|------|---------|
| ADD APN | 增加APN配置（配置真实APN，转换APN必须先存在） | APN |
| ADD APNALIAS | 增加APN别名配置 | SUBRANGE, ALIASAPN, CONVERTAPN, （5G）SST/SD |
| LCK APNALIAS | 锁定APN别名配置（去活/删除前必须锁定） | SUBRANGE, ALIASAPN, CONVERTAPN, LOCKED, APNTYPE=ALIAS_APN |
| DEA SMCTX | 去激活或者停止去活SM上下文（批量去活别名APN下用户） | ACTIONTYPE=START_DEA, DEATYPE=APN, APNTYPE=REQUESTED, APN |
| SET DEACTIVERATE | 设置去激活用户承载的速率 | RATE=1000 |
| RMV APNALIAS | 删除APN别名配置（需无活跃会话） | SUBRANGE, ALIASAPN, CONVERTAPN, APNTYPE=ALIAS_APN |
| SET APNREPORTATTR | 设置APN的上报属性（自动生成，配真实APN的PCF/CHF=SERVICE） | APN, PCF, CHF |
| SET LICENSESWITCH | 设置License项的开关 | LICITEM, SWITCH |
| LST APNALIAS | 查询APN别名配置（辅助） | - |
| LST APN | 查询APN配置（辅助，验证转换APN存在） | - |

> 来源：参考信息 `_34797882.md`、激活脚本 `_34797880.md`

#### 4.2.2 SGSN/MME 侧核心命令（参考信息4条 + 关联命令）

| 命令 | 用途 | 关键参数 |
|------|------|---------|
| ADD ALIASAPN | 增加别名APN配置 | SUBRANGE=IMSI_PREFIX, IMSIPRE, OLDAPN, NEWAPN |
| MOD ALIASAPN | 修改别名APN配置 | - |
| RMV ALIASAPN | 删除别名APN配置 | - |
| LST ALIASAPN | 查询别名APN配置 | - |
| SET LICENSESWITCH | 设置License项的开关 | LICITEM, SWITCH |
| DSP COMMMCTX | 显示移动性管理上下文（调测） | QUERYOPT=BYIMSI, IMSI |
| DSP SMCTX | 显示承载上下文（调测，验证APN映射生效） | QUERYOPT=BYIMSI, IMSI, IDTYPE |

> 来源：参考信息 `_68358229.md`、激活脚本 `_68358227.md`、调测脚本 `_68358228.md`

### 4.3 参数说明

#### 4.3.1 ADD APNALIAS 关键参数（GGSN/PGW-C/SMF 侧）

| 参数 | 取值 | 说明 |
|------|------|------|
| SUBRANGE | ALL_USER / SPECIFIC_NS | 用户范围。ALL_USER=所有用户；SPECIFIC_NS=指定切片（5G） |
| SST | 整数（如1） | 切片业务类型（Slice/Service Type），SUBRANGE=SPECIFIC_NS时必填 |
| SD | 整数（如123123） | 切片细分标识（Slice Differentiator），SUBRANGE=SPECIFIC_NS时必填 |
| ALIASAPN | 字符串（如"apn1"） | 别名APN名称，**不能**与ADD APN中已配置的APN相同 |
| CONVERTAPN | 字符串（如"apn5"） | 转换APN（真实APN），**必须**已在ADD APN中配置 |

#### 4.3.2 ADD ALIASAPN 关键参数（SGSN/MME 侧）

| 参数 | 取值 | 说明 |
|------|------|------|
| SUBRANGE | IMSI_PREFIX | 用户范围（按IMSI前缀匹配） |
| IMSIPRE | 字符串（如"12345"） | IMSI前缀，按最长匹配原则匹配用户 |
| OLDAPN | 字符串（如"example.com"） | 原始APN NI（协商APN） |
| NEWAPN | 字符串（如"huawei.com"） | 转换APN NI（别名APN，用于DNS解析） |

#### 4.3.3 SET APNREPORTATTR 关键参数（话单APN类型控制）

| 参数 | 取值 | 说明 |
|------|------|------|
| APN | 字符串 | 真实APN名称 |
| PCF | **SERVICE** / 其他 | 上报给PCF的APN名。SERVICE表示使用真实APN的业务名 |
| CHF | **SERVICE** / 其他 | 上报给CHF的APN名。SERVICE表示使用真实APN的业务名 |

> 注：每次执行 ADD APN 时会自动增加对应的 SET APNREPORTATTR 配置记录，需手动将真实APN的 PCF 和 CHF 配置为 SERVICE。

#### 4.3.4 DEA SMCTX 关键参数（批量去活）

| 参数 | 取值 | 说明 |
|------|------|------|
| ACTIONTYPE | START_DEA | 操作类型（开始去活） |
| DEATYPE | APN | 去活方式（按APN批量去活） |
| APNTYPE | REQUESTED | APN类型 |
| APN | 字符串（如"apn1"） | 别名APN名称 |

### 4.4 约束条件

| 约束类型 | 约束内容 | 适用侧 |
|---------|---------|--------|
| 别名APN唯一性 | ADD APNALIAS 中别名APN**不能**与 ADD APN 中已配置的APN相同 | GGSN/PGW-C/SMF |
| 转换APN存在性 | ADD APNALIAS 中转换APN**必须**已在 ADD APN 中配置 | GGSN/PGW-C/SMF |
| 多对一映射 | 别名APN与转换APN为多对一关系；**不同转换APN下不能配置相同别名APN**（5G切片例外） | GGSN/PGW-C/SMF |
| 删除约束 | 别名APN下**还存在用户或会话时不允许直接删除**；需先 LCK → 批量 DEA SMCTX → RMV | GGSN/PGW-C/SMF |
| 数量上限 | 全系统最多 1000 个别名APN；一个APN下最多 500 个APN别名 | GGSN/PGW-C/SMF |
| 映射表上限 | APN映射表支持 1024 条映射记录 | SGSN/MME |
| 双条件约束 | IMSI号段匹配 **AND** 协商APN在映射表中，两条件同时满足才转换 | SGSN/MME |
| HLR签约豁免 | 别名APN在APN协商之后转换，**无需在HLR中签约** | SGSN/MME |
| S-CDR固化 | S-CDR中默认采用别名APN，**无法通过参数修改** | SGSN/MME |
| 顺序约束 | 用户携带错误APN时，**先执行APN纠错（WSFD-106004），再执行别名APN纠正** | SGSN/MME |
| 5G切片查询顺序 | 5G用户**先按指定切片查询，未中再按ALL_USER查询** | GGSN/PGW-C/SMF |
| License分离 | 两套License分别对应两套网元，不可混淆（LKV2AAPN01 vs LKV2ALIASAPN02） | 全部 |
| APN NI语义 | 2/3/4G场景中本特性提到的APN均指APN NI；5G场景指DNN | 全部 |

> 来源：GGSN/PGW-C/SMF 概述 `_34797879.md`、SGSN/MME 概述 `_68358224.md`、激活脚本 `_34797880.md` & `_68358227.md`

---

## 5. 配置案例

### 5.1 典型场景一：GGSN/PGW-C/SMF 侧多APN归一（运营商合并重组）

**场景描述**：运营商合并和重组时，为了兼容现网中使用相同资源的多个APN，配置别名APN"apn1"和"apn2"，转换后的真实APN为"apn5"。这样不同APN下的用户都可以共用 apn5 的系统资源（计费、QoS、统计等）。

**配置步骤和MML命令序列（原样保留）**：

```
// 1. 开启别名APN功能License。
SET LICENSESWITCH:LICITEM="LKV2AAPN01",SWITCH=ENABLE;

// 2. 配置真实APN并配置APN的上报属性。
ADD APN: APN="apn5";
SET APNREPORTATTR: APN="apn5", PCF=SERVICE, CHF=SERVICE;

// 3. 别名APN名称为"apn1"和"apn2"，配置真实APN为"apn5"。
ADD APNALIAS:SUBRANGE=ALL_USER,ALIASAPN="apn1",CONVERTAPN="apn5";
ADD APNALIAS:SUBRANGE=ALL_USER,ALIASAPN="apn2",CONVERTAPN="apn5";
```

> 来源：激活脚本 `_34797880.md`（"任务示例"）

### 5.2 典型场景二：SGSN/MME 侧 IMSI号段+APN映射（DNS屏蔽）

**场景描述**：添加别名APN映射表的记录，将APN"example.com"映射为别名APN"huawei.com"（用于DNS解析），针对IMSI前缀为"12345"的用户生效。

**配置步骤和MML命令序列（原样保留）**：

```
//设置别名APN License开关为"ENABLE"。
SET LICENSESWITCH: LICITEM="LKV2ALIASAPN02", SWITCH=ENABLE;

//添加别名APN映射表的记录，将APN(example.com)映射为别名APN（huawei.com）。
ADD ALIASAPN: SUBRANGE=IMSI_PREFIX, IMSIPRE="12345", OLDAPN="example.com", NEWAPN="huawei.com";
```

> 来源：激活脚本 `_68358227.md`（"任务示例"）

### 5.3 典型场景三：5G切片感知的别名APN（SMF侧）

**场景描述**：5G场景中为指定切片（SST=1, SD=123123）下的用户配置别名APN"apn1"映射到真实APN"apn5"。

**MML命令序列（按激活文档参数构造）**：

```
SET LICENSESWITCH:LICITEM="LKV2AAPN01",SWITCH=ENABLE;
ADD APN: APN="apn5";
SET APNREPORTATTR: APN="apn5", PCF=SERVICE, CHF=SERVICE;
ADD APNALIAS:SUBRANGE=SPECIFIC_NS,SST=1,SD=123123,ALIASAPN="apn1",CONVERTAPN="apn5";
```

> 来源：基于激活脚本 `_34797880.md` 数据表参数（SST/SD）构造，5G用户查询顺序：先按切片查，未中再按ALL_USER查

### 5.4 典型场景四：别名APN锁定+批量去活+删除（生命周期管理）

**场景描述**：当运营商不希望用户使用指定APN别名"apn1"时，需先锁定 → 批量去活该别名APN下用户 → 删除别名APN。

**MML命令序列（原样保留关键步骤）**：

```
// 1. 锁定别名APN
LCK APNALIAS:SUBRANGE=ALL_USER,ALIASAPN="apn1",CONVERTAPN="apn5",
            LOCKED=ENABLE,APNTYPE=ALIAS_APN;

// 2. 配置批量去活速率
SET DEACTIVERATE:RATE=1000;

// 3. 批量去活该别名APN下用户
DEA SMCTX:ACTIONTYPE=START_DEA,DEATYPE=APN,APNTYPE=REQUESTED,APN="apn1";

// 4. 删除别名APN
RMV APNALIAS:SUBRANGE=ALL_USER,ALIASAPN="apn1",CONVERTAPN="apn5",
            APNTYPE=ALIAS_APN;
```

> 来源：激活脚本 `_34797880.md`（操作步骤6 + 数据表）

### 5.5 场景变体对照

| 变体 | 网元侧 | 核心差异 | 关键命令 |
|------|--------|---------|---------|
| 多APN归一（2/3/4G） | GGSN/PGW-C | SUBRANGE=ALL_USER，多别名→一真实 | ADD APNALIAS SUBRANGE=ALL_USER |
| 5G切片感知 | SMF | SUBRANGE=SPECIFIC_NS+SST+SD，切片优先查询 | ADD APNALIAS SUBRANGE=SPECIFIC_NS |
| IMSI号段匹配 | SGSN/MME | 按IMSI最长匹配 + OLDAPN→NEWAPN（DNS屏蔽） | ADD ALIASAPN SUBRANGE=IMSI_PREFIX |
| 网络改建APN切换 | GGSN/PGW-C/SMF | 原规划APN→新规划APN（一对一同名映射） | ADD APNALIAS（单别名） |
| 漫游用户区分 | SGSN/MME | 漫游地APN→本地别名APN，区分服务 | ADD ALIASAPN（按号段区分漫游地） |
| 别名APN下线 | GGSN/PGW-C/SMF | 锁定+批量去活+删除（生命周期管理） | LCK→DEA SMCTX→RMV |

---

## 6. 验证与调测

### 6.1 验证方法

#### 6.1.1 GGSN/PGW-C/SMF 侧调测（5步）

**调测目的**：确保别名APN功能可以正常使用。

**调测数据**：

| 类别 | 参数名称 | 取值样例 | 获取方法 |
|------|---------|---------|---------|
| 用户信息查询 | MSISDN | 8613812345678 | 测试终端自带 |
| 测试终端使用的APN | APN名称 | apn1 / apn2 | 已配置数据中获取（LST APNALIAS查询） |

**工具**：测试终端、OM Portal

**操作步骤**：

1. 进入"MML命令行-UNC"窗口
2. 查询UNC上虚拟APN对应的License配置开关是否打开
   - 如果"SWITCH"为"ENABLE"，请执行步骤3
   - 如果"SWITCH"为"DISABLE"，则执行 `SET LICENSESWITCH` 命令打开License开关
3. 测试终端 8613812345678 分别使用不同的APN"apn1"和"apn2"接入网络
   - 如果测试终端成功接入网络，请执行步骤4
   - 如果测试终端无法接入网络，请调测UNC的接入功能
4. 通过测试终端的MSISDN查看测试终端激活时使用的APN
   - 如果测试终端使用不同的APN接入UNC，在UNC上显示的 **"APN name"都为"apn5"**，则测试终端接入成功，调测结束
   - 如果"APN name"不是"apn5"，请执行步骤5寻求技术支持
5. 收集信息并寻求技术支持
   - a. 执行 `EXP MML` 命令将当前配置数据导出为MML脚本文件并保存
   - b. 收集并保存上述所有查询信息
   - c. 查看并收集对端设备配置及接口状态信息
   - d. 收集归纳所有信息并联系华为技术支持解决

> 来源：调测脚本 `_34797881.md`（"操作步骤"）

#### 6.1.2 SGSN/MME 侧调测（5步）

**调测前提**：以激活脚本任务实例为例，IMSI为 `460011234567890` 的用户签约的缺省APN为"example.com"。

**调测数据**：

| 类别 | 参数名称 | 取值样例 | 获取方法 |
|------|---------|---------|---------|
| 用户信息查询 | IMSI | 460011234567890 | 测试终端自带 |

**工具**：OM Portal跟踪

**操作步骤**：

1. 进入"MML命令行-UNC"窗口
2. 执行 `LST LICENSESWITCH` 命令查询License配置开关是否已打开
   - 如果"SWITCH"为"ENABLE"，请执行步骤3
   - 如果"SWITCH"为"DISABLE"，请执行 `SET LICENSESWITCH` 命令打开License开关
3. 用户发起初始附着，携带APN为"example.com"、PDN类型与缺省APN的子集
   - **预期结果**：用户附着成功
4. 查询用户的MM上下文：`DSP COMMMCTX:QUERYOPT=BYIMSI,IMSI=IMSI;`
   - **预期结果**：用户处于 EMM-REGISTERED 状态
5. 查询用户的SM上下文：`DSP SMCTX:QUERYOPT=BYIMSI,IMSI=IMSI,IDTYPE=BYBEARID/NSAPI;`
   - **预期结果**：SM上下文中的信息正确，**使用的APN为"huawei.com"**（别名APN，证明映射生效）

> 来源：调测脚本 `_68358228.md`（"操作步骤"）

### 6.2 告警参考

**本特性无相关告警**（两侧参考信息均明确声明）。

> 来源：参考信息 `_34797882.md`、`_68358229.md`（"告警"章节）

### 6.3 测量指标

**本特性无相关测量指标**（两侧参考信息均明确声明）。

### 6.4 软参

**本特性无相关软参**（两侧参考信息均明确声明）。

### 6.5 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| 别名APN映射不生效（GGSN/PGW-C/SMF） | License开关未打开 | `LST LICENSESWITCH` 查询；`SET LICENSESWITCH LICITEM="LKV2AAPN01"` 打开 |
| 别名APN映射不生效（SGSN/MME） | License开关未打开 | `LST LICENSESWITCH` 查询；`SET LICENSESWITCH LICITEM="LKV2ALIASAPN02"` 打开 |
| 别名APN接入后 UNC 显示APN不是真实APN | SET APNREPORTATTR 未配置 PCF/CHF=SERVICE | 检查 `LST APNREPORTATTR`，补配 `SET APNREPORTATTR PCF=SERVICE,CHF=SERVICE` |
| RMV APNALIAS 被拒绝 | 别名APN下还存在用户或会话 | 按"LCK→DEA SMCTX→RMV"三步走；先 `LCK APNALIAS LOCKED=ENABLE`，再批量去活 |
| 5G切片用户别名APN未生效 | 切片SST/SD配置错误或查询顺序问题 | 5G先按切片查，未中再按ALL_USER查；核对 SST/SD 取值 |
| SGSN/MME 别名APN未映射 | IMSI不在配置号段内 OR 协商APN不在映射表 | 双条件约束：核对 IMSIPRE 最长匹配 + OLDAPN 是否在映射表 |
| SGSN/MME APN纠错未执行 | 用户携带错误APN时纠错顺序问题 | 纠错（WSFD-106004）先于别名APN，核对 License 82205928 是否加载 |
| 用户无法接入 | 真实APN未在 ADD APN 中配置 | `LST APN` 查转换APN是否存在；补配 ADD APN |
| 别名APN与真实APN重名 | ADD APNALIAS 别名APN与 ADD APN 配置重复 | 别名APN不能与ADD APN中已配置APN相同，需改名 |

---

## 7. 参考信息

### 7.1 与其他特性的关系

| 关联特性 | 特性ID | 关系说明 |
|---------|--------|---------|
| 会话管理（UNC/SMF） | WSFD-010501 | 宿主特性：别名APN是PDU会话建立前的APN映射预处理环节；映射后基于真实APN建立PDU会话 |
| 会话管理（UDG/UPF） | GWFD-010101 | 用户面执行方：基于真实APN执行PDU会话的建立/释放 |
| 请求信息纠正功能（SGSN/MME） | WSFD-106004 | **顺序依赖**：用户携带错误APN时，先执行APN纠错，再执行别名APN纠正（SGSN/MME侧明确交互） |
| 用户数据管理 | WSFD-010400 | APN协商的签约数据来源（HLR/HSS/UDM）；别名APN无需在HLR签约（SGSN/MME侧） |
| 用户接入控制功能 | WSFD-106003 | APN接入权限控制；别名APN映射后的真实APN需通过接入权限校验 |
| 地址分配方式（UNC） | WSFD-010502 | 同属APN基础类；地址分配基于真实APN的资源共用 |
| UPF选择 | WSFD-107010 | SMF为PDU会话选择UPF（基于真实APN） |
| APN基础（UDG侧） | GWFD-010105/GWFD-010104 | 用户面地址分配执行方，基于真实APN |

### 7.2 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/会话管理功能/WSFD-106203 别名APN_64082528.md` | 根索引：APN双重角色（路由标识/业务域标识）、SGSN/MME vs GGSN/PGW-C/SMF 双视角别名APN定义差异、5G DNN与APN等价（3GPP TS23.501 R15）、APN NI与APN OI语义 |
| 2 | `UNC 20.15.2.../WSFD-106203 别名APN/别名APN（适用于GGSN_PGW-C_SMF）/WSFD-106203 别名APN特性概述（适应于GGSN_PGW-C_SMF）_34797879.md` | GGSN/PGW-C/SMF侧：适用NF（GGSN/PGW-C/SMF UNC 20.3.0+）、定义（别名APN→真实APN资源归一）、客户价值、应用场景（运营商合并重组、网络改建）、License 82200BNM LKV2AAPN01、对系统影响（CPU上升）、应用限制（RMV APNALIAS需无会话）、原理（图1 多别名共用真实APN资源）、计费（话单APN类型可配置）、规格（1000个别名APN，一APN下500别名）、遵循标准（5个3GPP）、发布历史（v1 20.3.0） |
| 3 | `UNC 20.15.2.../别名APN（适用于GGSN_PGW-C_SMF）/WSFD-106203 别名APN参考信息（适用于GGSN_PGW-C_SMF）_34797882.md` | GGSN/PGW-C/SMF侧：MML命令清单（5条：ADD APN/ADD APNALIAS/LCK APNALIAS/DEA SMCTX/SET DEACTIVERATE）、告警（无）、软参（无）、测量指标（无） |
| 4 | `UNC 20.15.2.../别名APN（适用于GGSN_PGW-C_SMF）/激活别名APN_34797880.md` | GGSN/PGW-C/SMF侧激活：别名APN获取和映射流程图、6步操作步骤（SET LICENSESWITCH→ADD APN→SET APNREPORTATTR→ADD APNALIAS→[LCK→DEA→RMV]）、完整任务示例MML脚本（apn1/apn2→apn5）、ADD APNALIAS 5个约束（多对一/不可重名/转换APN必须存在等）、5G切片SUBRANGE=SPECIFIC_NS+SST+SD查询顺序 |
| 5 | `UNC 20.15.2.../别名APN（适用于GGSN_PGW-C_SMF）/调测别名APN_34797881.md` | GGSN/PGW-C/SMF侧调测：5步调测流程（LST LICENSESWITCH→接入→查APN name应为真实APN→EXP MML）、MSISDN 8613812345678 测试用例、验证标准"APN name都为apn5" |
| 6 | `UNC 20.15.2.../别名APN（适用于SGSN_MME）/WSFD-106203 别名APN特性概述（适用于SGSN_MME）_68358224.md` | SGSN/MME侧：适用NF（SGSN UNC 20.3.0+/MME UNC 20.0.0+）、定义（协商APN→别名APN DNS屏蔽）、客户价值（节约DNS资源/漫游地区分服务）、应用场景、License 82207546 LKV2ALIASAPN02、与WSFD-106004顺序依赖（先纠错后别名）、对系统无影响、应用限制（S-CDR默认别名APN无法修改）、APN转换7步流程、IMSI最长匹配、HLR签约豁免、规格（1024条映射）、发布历史（v01 20.0.0 MME率先） |
| 7 | `UNC 20.15.2.../别名APN（适用于SGSN_MME）/WSFD-106203 别名APN参考信息（适用于SGSN_MME）_68358229.md` | SGSN/MME侧：MML命令清单（4条：ADD/MOD/RMV/LST ALIASAPN）、告警（无）、软参（无）、测量指标（无） |
| 8 | `UNC 20.15.2.../别名APN（适用于SGSN_MME）/实现原理_68358226.md` | SGSN/MME侧原理：IMSI最长匹配应用举例（IMSI前缀460001+test1/2/3.com→huawei.com）、4种用户请求场景转换决策表、双条件约束（IMSI号段 AND APN映射表） |
| 9 | `UNC 20.15.2.../别名APN（适用于SGSN_MME）/激活别名APN_68358227.md` | SGSN/MME侧激活：3步操作（SET LICENSESWITCH→ADD ALIASAPN）、ADD ALIASAPN参数（SUBRANGE=IMSI_PREFIX/IMSIPRE/OLDAPN/NEWAPN）、任务示例MML脚本（example.com→huawei.com, IMSIPRE=12345） |
| 10 | `UNC 20.15.2.../别名APN（适用于SGSN_MME）/调测别名APN_68358228.md` | SGSN/MME侧调测：5步调测流程（LST LICENSESWITCH→初始附着携带example.com→DSP COMMMCTX查EMM-REGISTERED→DSP SMCTX验证APN=huawei.com）、IMSI 460011234567890测试用例 |

### 7.3 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| Alias APN | 别名APN / 虚拟APN | UNC映射表中的APN别名，两侧语义不同（SGSN/MME=DNS屏蔽映射后；GGSN/PGW-C/SMF=用户传来的待映射APN） |
| Real APN / Convert APN | 真实APN / 转换APN | GGSN/PGW-C/SMF侧映射后的目标APN，承载实际业务资源 |
| Negotiated APN | 协商APN | SGSN/MME侧经签约匹配（或APN纠错）后的APN，是真实的APN |
| APN NI | APN Network Identifier | APN网络标识（必选），2/3/4G本特性均指此 |
| APN OI | APN Operator Identifier | APN运营商标识（可选），".gprs"结尾 |
| DNN | Data Network Name | 5G场景APN等价物 |
| IMSI_PREFIX | IMSI前缀 | SGSN/MME侧按最长匹配匹配用户的号段 |
| SST | Slice/Service Type | 5G切片业务类型 |
| SD | Slice Differentiator | 5G切片细分标识 |
| SUBRANGE | 用户范围 | 区分ALL_USER/SPECIFIC_NS/IMSI_PREFIX的匹配范围 |
| APNTYPE=ALIAS_APN | 别名APN类型 | LCK/RMV APNALIAS命令中的类型标识 |
| APNTYPE=REQUESTED | 请求APN类型 | DEA SMCTX命令中的类型标识 |
| S-CDR | SGSN-CDR | SGSN的话单记录，默认采用别名APN |

---

## 8. 文档一致性说明（配置树 vs 产品文档 vs 同域特性）

> 配置树仅用于定位特性 ID，以下记录以产品文档实际内容为准时发现的关键差异与协同点，供 Stage 3 横向分析参考。

### 8.1 与配置树/文档清单的差异

| # | 维度 | 配置树/文档清单描述 | 产品文档实际内容 | 差异类型 |
|---|------|---------------------|-----------------|---------|
| 1 | 特性定位 | "别名APN/虚拟APN(APN聚合与重定向)" | 同一特性ID在**两套网元下映射方向相反**：SGSN/MME=协商APN→别名APN（DNS屏蔽）；GGSN/PGW-C/SMF=别名APN→真实APN（资源归一） | **关键澄清**：清单"聚合与重定向"实际包含两种反向语义，须分网元讨论 |
| 2 | License 数量 | 文档清单未细化 | **两套License分别对应两套网元**：LKV2AAPN01（GGSN/PGW-C/SMF）+ LKV2ALIASAPN02（SGSN/MME） | 补全：清单未提及双License |
| 3 | MML命令差异 | 文档清单未区分 | 两侧命令**完全不同**：GGSN/PGW-C/SMF=ADD APNALIAS；SGSN/MME=ADD ALIASAPN（注意 APNALIAS vs ALIASAPN 命名差异） | 补全：命令前缀/后缀差异 |
| 4 | 发布版本 | 文档清单未细化 | MME率先20.0.0支持；SGSN/GGSN/PGW-C/SMF在20.3.0支持 | 补全：版本时序差异 |
| 5 | 规格差异 | 文档清单未细化 | GGSN/PGW-C/SMF=1000别名+500别名/APN；SGSN/MME=1024条映射记录 | 补全：两侧规格体系不同 |

### 8.2 与同域 APN 基础特性的协同

| # | 维度 | WSFD-010501（会话管理） | WSFD-106203（别名APN） | 协同关系 |
|---|------|------------------------|------------------------|---------|
| 1 | 流程位置 | PDU会话建立/释放主流程 | APN协商之后、PDU会话建立之前 | **预处理依赖**：别名APN是会话管理的映射前置环节 |
| 2 | APN角色 | 使用最终APN（真实APN）建立会话 | 提供别名APN→真实APN映射 | **输入依赖**：WSFD-010501 使用 WSFD-106203 映射后的真实APN |
| 3 | 资源共用 | 基于APN配置计费/QoS/安全策略 | 多别名共用一真实APN资源 | **资源归一**：别名APN让多APN共用WSFD-010501的资源策略 |
| 4 | 统计维度 | 按APN统计会话/流量 | GGSN/PGW-C/SMF侧映射后**以真实APN信息统计** | **统计归一**：所有别名APN业务归到真实APN监控 |
| 5 | DNS寻址 | 不直接涉及 | SGSN/MME侧映射后别名APN用于DNS解析寻址GGSN/PGW-C | **寻址协同**：间接影响WSFD-010501的网元选择 |
| 6 | 网元选择 | WSFD-107010 UPF选择（基于APN） | SGSN/MME侧影响DNS解析结果（选哪个GGSN/PGW-C/SMF） | **网元选择协同**：影响SMF为PDU会话选择UPF的输入 |

### 8.3 关键发现：同特性ID的双视角语义反转

**最重要的发现**：WSFD-106203 是同一特性ID下**两套网元语义反转**的特殊情况：

| 维度 | SGSN/MME 侧 | GGSN/PGW-C/SMF 侧 |
|------|-------------|-------------------|
| 映射方向 | 协商APN → 别名APN | 别名APN → 真实APN |
| "别名APN"含义 | 映射后的目标APN（用于DNS） | 用户传来的待映射APN |
| "真实APN"含义 | 映射前的协商APN | 映射后的目标APN（业务资源） |
| 用途 | DNS解析屏蔽 | 业务资源归一 |
| 匹配维度 | IMSI最长匹配 + 协商APN | 用户范围（ALL_USER/切片）+ 别名APN |
| 命令族 | ADD ALIASAPN | ADD APNALIAS |
| License | LKV2ALIASAPN02 | LKV2AAPN01 |
| HLR签约 | 别名APN无需签约 | 转换APN必须已配置（ADD APN） |
| 规格 | 1024条映射 | 1000别名+500/APN |

**Stage 3 建议**：在三层图谱实例化时，建议将本特性拆分为两个 Feature 变体节点（或通过 variant_dimensions 的"网元角色视角"维度区分），避免在规则匹配时产生语义混淆。

---

## 附录 A：与同域其他特性的对照速查表

| 对照维度 | WSFD-106203（别名APN） | WSFD-010501（会话管理） | WSFD-010502（地址分配方式） |
|---------|------------------------|------------------------|---------------------------|
| 网元角色 | GGSN/PGW-C/SMF + SGSN/MME | SMF（5G）/ PGW-C（4G）/ GGSN（2/3G） | GGSN/PGW-C/SMF |
| 核心用途 | APN映射预处理 | PDU会话建立/释放主流程 | 地址分配决策 |
| License | 双License（LKV2AAPN01 + LKV2ALIASAPN02） | - | 无License |
| MML命令 | ADD APNALIAS / ADD ALIASAPN | （会话管理命令族） | ADD ADDRPOOL/SECTION等 |
| 流程位置 | APN协商后、会话建立前 | 主流程 | 会话建立中的地址分配子流程 |
| 与WSFD-010501关系 | 预处理依赖（映射前置） | 宿主 | 子流程协同 |
