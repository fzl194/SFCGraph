# WSFD-011306 Radius功能 知识文档

> 聚焦 APN 业务域鉴权计费场景的 UNC（GGSN/PGW-C/SMF）与 RADIUS/AAA Server 之间的 Radius 协议承载与功能特性
> 上游鉴权决策特性 WSFD-011305（AUTHMODE 决定是否启用 Radius 鉴权），下游抄送特性 WSFD-011307（Radius 抄送功能）

---

## 0. 元数据（三层图谱Schema字段）

| 字段 | 取值 |
|------|------|
| feature_id | WSFD-011306 |
| feature_name | Radius功能 |
| feature_group | 鉴权计费 |
| parent_feature_id | WSFD-011305（Radius鉴权接入，配置树父节点，推断） |
| applicable_nf_map | `{"UNC": ["GGSN", "PGW-C", "SMF"]}` |
| variant_dimensions | ["AAA Server工作模式(主备1+1/按优先级选主/负荷分担轮选)", "服务器角色(鉴权AUTHENTICATION/计费ACCOUNTING)", "鉴权方式(PAP/CHAP/MS-CHAP)", "到AAA Server的组网(单平面+静态路由+BFD/双平面+OSPF+BFD/带内GRE VPN/带外GRE VPN)", "Bypass策略(立即去活DEACTIVE/放通CONTINUE/HOLDINGTIME延时去活)", "业务触发RADIUS消息(用户激活触发/特定业务L3-4层规则触发)", "域名处理(增加/剥离/位置前缀/后缀)"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-01, EV-FK-02, EV-FK-03, EV-FK-04, EV-FK-05, EV-FK-06, EV-FK-07, EV-FK-08, EV-FK-09, EV-FK-10, EV-FK-11, EV-FK-12] |
| license_required | 无（本特性无需License） |

---

## 1. 概述

### 1.1 特性定义（是什么）

UNC 与 RADIUS 服务器之间，通过 RADIUS 协议实现 **RADIUS 鉴权、RADIUS 计费、RADIUS 策略控制**三大类功能。本特性是 UNC 与外部 AAA Server 交互的"承载/管道/功能集"总集，负责定义 Radius 服务器组配置、鉴权/计费服务器模板、消息重发与超时、扩展属性、域名剥离、Bypass 策略、业务触发等 Radius 通信的全套规则。

> 来源：`WSFD-011306 Radius功能特性概述_31467848.md`（"定义"章节）

### 1.2 适用NF（UDG/UNC网元）

| 涉及NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| GGSN | 控制面（UNC，2/3G） | UNC 20.3.0及后续版本 | 封装、解封装、处理 RADIUS 计费和鉴权报文 |
| PGW-C | 控制面（UNC，4G） | UNC 20.3.0及后续版本 | 封装、解封装、处理 RADIUS 计费和鉴权报文 |
| SMF | 控制面（UNC，5G） | UNC 20.3.0及后续版本 | 封装、解封装、处理 RADIUS 计费和鉴权报文 |
| AAA Server | 外部对端网元 | 无特殊要求 | 实现对用户的鉴权和计费 |

> 来源：`WSFD-011306 Radius功能特性概述_31467848.md`（"可获得性/涉及NF"章节）

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|---------|---------|---------|
| 01 | 20.3.0 | 首次发布，支持 RADIUS 功能 |

> 来源：`WSFD-011306 Radius功能特性概述_31467848.md`（"发布历史"章节）

### 1.4 License

**本特性无需获得 License 许可即可获得该特性的服务**（文档明确声明）。

> 来源：`WSFD-011306 Radius功能特性概述_31467848.md`（"可获得性/License 支持"章节）

### 1.5 前置条件与依赖

| 前置条件 | 说明 |
|---------|------|
| APN 已配置 | 必须通过 `ADD APN` 完成增加 APN 配置，才能在 APN 下绑定 Radius 服务器组与 Client IP |
| 逻辑接口与 VPN 就绪 | Gi/SGi 逻辑接口（ADD LOGICIP/ADD LOGICINF）、VPN 实例（ADD VPNINST/ADD L3VPNINST/ADD VPNINSTAF）须按组网场景提前配置 |
| AAA Server 互通 | AAA Server 上已完成相应配置并配置到 UNC 的回程路由 |
| UPF/PGW-U 业务感知（业务触发场景） | 业务触发 RADIUS 场景需在 UPF/PGW-U 上配置好对应的 FlowFilter、Rule 等业务感知信息（C-U 一致性） |
| 接入方式决策（上游依赖） | AUTHMODE 为透明鉴权接入/非透明接入/本地鉴权接入时，**必须**配置本特性；透明接入（不鉴权）可不配 |

> 来源：`配置RADIUS功能_32909765.md`（"必备事项"）、`配置到AAA Server的数据（单平面+静态路由+BFD组网）_32044985.md`（"必备事项"）、`配置业务触发RADIUS功能_33000859.md`（"必备事项"）

### 1.6 与其他特性的交互

**特性概述明确声明"本特性不涉及与其他特性的交互"**（原文）。但功能语义上存在强关联：

| 交互类型 | 相关特性 | 交互说明 |
|---------|---------|---------|
| **上游鉴权决策** | WSFD-011305 Radius鉴权接入（UNC） | AUTHMODE 决定是否启用 Radius 鉴权：透明接入不鉴权（不需本特性鉴权）；透明鉴权接入/非透明接入/本地鉴权接入均需 Radius 鉴权（**必配本特性**） |
| **下游抄送** | WSFD-011307 支持Radius抄送功能（UNC） | Radius 鉴权/计费消息发送给 AAA Server 的同时，抄送给其他需要获取用户信息的服务器（WAP GW 等） |
| **负荷分担** | WSFD-011308 AAA负荷分担（UNC） | Radius 鉴权和计费报文按轮选方式发送给多台 AAA Server（本特性 Radius-server Group 的"负荷分担模式"由 WSFD-011308 承载） |
| **Radius 地址分配协同** | WSFD-010502 地址分配方式（UNC） | Radius 分配方式下，本特性负责 Access-Accept 中携带的用户 IP/地址池名的承载与解析 |
| **PCF/PCC 协同** | （PCF/PCRF，非本域） | 无 PCC 应用或 PCRF 异常时，UNC 采用 AAA 下发策略；PCRF 正常时 UNC 将 AAA 策略转发给 PCRF 决策 |
| **C-U 协同** | GWFD-110101 SA-Basic（UDG，业务触发场景） | 业务触发 RADIUS 场景依赖 UDG 的业务感知（L3/4 过滤器、规则）识别特定业务 |

> 来源：`WSFD-011306 Radius功能特性概述_31467848.md`（"应用场景/与其他特性的交互"章节）

### 1.7 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | RADIUS 计费功能可以实现移动运营商和 Internet 运营商分别收取费用；通过 RADIUS 鉴权过程，实现 RADIUS 用户接入，同时满足 ISP 或企业网对用户权限控制的要求；从 RADIUS 服务器获取用户和业务的属性，并在 UNC 上对用户实施该策略，从而进行灵活的用户控制 |
| 用户 | 用户不感知该特性 |

> 来源：`WSFD-011306 Radius功能特性概述_31467848.md`（"客户价值"章节）

### 1.8 应用场景

Radius 功能应用于 ADSL 上网、小区宽带上网、IP 电话、VPDN（虚拟专用拨号网）、移动电话预付费等场景。在 UNC 上，Radius 功能应用于多个特性中：

- **接入鉴权**：透明接入不需要 Radius 鉴权；非透明接入/透明鉴权接入/本地鉴权接入都需要 Radius 鉴权（→ WSFD-011305）
- **Radius 地址分配**：Radius 鉴权过程通过 AAA Server 返回的 Access-Accept 携带 IP 地址、IPv4/IPv6 地址池名称（→ WSFD-010502）
- **Radius 抄送**：Radius 鉴权和计费消息在发送给 AAA Server 同时，抄送给其他需要获取用户信息的服务器（→ WSFD-011307）
- **AAA 负荷分担**：Radius 鉴权和计费消息按轮选方式发送给多台 AAA Server（→ WSFD-011308）

> 来源：`WSFD-011306 Radius功能特性概述_31467848.md`（"应用场景"章节）

### 1.9 对系统的影响

该特性会对**每个使用 RADIUS 功能的用户进行单独处理**，使用 RADIUS 功能的用户越多，该特性对系统的影响越大。

### 1.10 应用限制

**本特性无应用限制**（文档明确声明）。

### 1.11 特性规格

| 规格名称 | 规格指标 |
|---------|---------|
| 整机最大支持 AAA server 个数 | 4000 |
| 每个 Radius-server Group 最大主用鉴权服务器数 | 16 |
| 每个 Radius-server Group 最大备用鉴权服务器数 | 16 |
| 每个 Radius-server Group 最大主用计费服务器数 | 16 |
| 每个 Radius-server Group 最大备用计费服务器数 | 16 |

> 来源：`WSFD-011306 Radius功能特性概述_31467848.md`（"特性规格"）、`实现原理_31922672.md`（"AAA Server 工作模式可配置"）

### 1.12 计费与话单

**本特性不涉及计费与话单**（本特性是 Radius 计费的承载管道，但不直接产生本地话单；计费逻辑由 AAA Server 侧完成）。

### 1.13 遵循标准

| 标准类别 | 标准编号 | 标准名称 |
|---------|---------|---------|
| 3GPP | 23.214 | Architecture enhancements for control and user plane separation of EPC nodes |
| 3GPP | 29.244 | Interface between the Control Plane and the User Plane of EPC Nodes |
| 3GPP | 23.060 | GPRS Service Description; Stage 2 |
| 3GPP | 29.060 | GPRS; GTP across the Gn and Gp interface |
| 3GPP | 29.061 | Interworking between PLMN supporting packet based services and PDN |
| IETF | 2865 | Remote Authentication Dial In User Service (RADIUS) |

> 来源：`WSFD-011306 Radius功能特性概述_31467848.md`（"遵循标准"章节）

---

## 2. 核心概念

### 2.1 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| RADIUS | Remote Authentication Dial In User Service | AAA 协议，实现验证、授权、计费 |
| AAA | Authentication/Authorization/Accounting | 鉴权、授权、计费三类功能的统称 |
| AAA Server | - | 外部 RADIUS 服务器，UNC 的对端网元，完成对用户的鉴权和计费 |
| Radius-server Group | Radius 服务器组 | UNC 侧 Radius 服务器的组织单位，每个 APN 可绑定一个组（ADD RDSSVRGRP） |
| 主备模式（1+1） | Master-Slave 1+1 | 一主一备，仅两个鉴权/计费服务器参与工作，主正常则全部发主，否则发备 |
| 按优先级选主 | Priority-based Primary | 配置多个主服务器的优先级，按优先级顺序选择主服务器，高优先级故障才发低优先级 |
| 负荷分担（轮选） | Round-Robin Loadsharing | RADIUS 报文按轮流选择方式发送给多台 AAA Server（详见 WSFD-011308） |
| RADIUS 鉴权 | Authentication | 终端用户通过 PGW-C/SMF 到 AAA Server 进行用户身份认证 |
| RADIUS 计费 | Accounting | PGW-C/SMF 将用户上网时长和数据流量等计费信息送往 AAA Server |
| RADIUS 策略控制 | Policy Control | PGW-C/SMF 从 AAA Server 获取用户/业务属性并传递给 PGW-U/UPF，由 UPF 对业务进行控制 |
| Access-Accept | - | AAA Server 返回的鉴权接受消息，可携带用户 IP/地址池名 |
| Accounting-Request Start/Interim/Stop | - | Radius 计费请求消息：开始/ interim 更新/停止 |
| POD | Packet of Disconnect | AAA Server 主动发起的 RADIUS 消息，用于去激活用户 |
| Bypass | 旁路/放通 | Radius 服务器无响应时是否放通用户的策略 |
| Message-Authenticator | - | Radius 消息完整性与合法性校验属性 |
| CHAP/PAP/MS-CHAP | - | 三种 Radius 鉴权方式（PAP=密码认证协议；CHAP=挑战握手；MS-CHAP=微软扩展，仅 v1/v2） |
| Framed-IP / Framed-Pool | Radius 属性 | Access-Accept 中携带的用户 IP / 地址池名（用于 Radius 地址分配） |
| 3GPP 扩展属性 | - | 3GPP 29.061 协议定义的 Radius 扩展属性，UNC 可与 AAA Server 交互 |

> 来源：`WSFD-011306 Radius功能特性概述_31467848.md`、`实现原理_31922672.md`

### 2.2 对象模型

UNC 侧 Radius 功能的配置架构由"AAA Server 侧服务器体系 + APN 侧绑定体系 + 策略控制体系"三层构成：

```
┌─────────────────────────────────────────────────────────────────┐
│ AAA Server 侧服务器体系（ADD RDSSVRGRP / ADD RDSSVR）            │
│                                                                 │
│   ┌──────────────────┐                                          │
│   │ Radius-server    │ MODE=MASTER_SLAVE / ROUND_ROBIN          │
│   │ Group            │ ACCTTIMEOUT/AUTHTIMEOUT/重发次数/Down保持 │
│   │ (服务器组模板)    │                                          │
│   └────────┬─────────┘                                          │
│            │ 包含                                                │
│            ├── SERVERTYPE=AUTHENTICATION (鉴权服务器, PORT=1812) │
│            │     ├── PRIFLAG=PRIMARY 主用（最多16，可配优先级）   │
│            │     └── PRIFLAG=SECONDARY 备用（最多16）            │
│            └── SERVERTYPE=ACCOUNTING (计费服务器, PORT=1813)     │
│                  ├── PRIFLAG=PRIMARY 主用（最多16，可配优先级）   │
│                  └── PRIFLAG=SECONDARY 备用（最多16）            │
└────────────┼────────────────────────────────────────────────────┘
             │ ADD APNRDSSVRGRP (APN↔服务器组绑定)
             ▼
┌─────────────────────────────────────────────────────────────────┐
│ APN 侧绑定体系                                                   │
│                                                                 │
│   ADD APN (apn-test)                                            │
│     ├── ADD APNRDSSVRGRP  → 绑定 RDSSVRGRPNAME=isprg            │
│     ├── ADD APNRDSCLIENTIP → 鉴权 Client IP (INTFNAME=giif...)   │
│     ├── ADD APNRDSCLIENTIP → 计费 Client IP (INTFNAME=giif...)   │
│     ├── SET APNRDSACCTCTRL → 计费阈值/SRVTRIGGER/SUPPORTACCTRSP  │
│     ├── SET APNAUTHATTR   → PoD 开关/无响应处理                  │
│     └── SET APNRADIUSATTR → 域名增加/剥离                        │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ 策略控制体系（业务触发 RADIUS 场景，与 UDG 协同）                  │
│                                                                 │
│   ADD FLOWFILTER (flowfilter_1, 与 UDG 一致)                    │
│        ↓                                                        │
│   ADD RULE (rule_test1, POLICYTYPE=SRV_TRIGGER, PRIORITY=10)    │
│        ↓                                                        │
│   ADD USERPROFILE (up_test, UPTYPE=PCC)                         │
│     └── ADD RULEBINDING (up_test ↔ rule_test1)                  │
│        ↓                                                        │
│   ADD USRPROFGROUP (upg_test)                                   │
│     └── ADD UPBINDUPG (upg_test ↔ up_test)                      │
│        ↓                                                        │
│   ADD APNUSRPROFG (apn-test ↔ upg_test)                         │
└─────────────────────────────────────────────────────────────────┘
```

### 2.3 在鉴权计费场景的角色

本特性在 APN 业务域鉴权计费场景中扮演"Radius 协议承载与功能集"的角色，是 WSFD-011305（AUTHMODE 决策）的执行管道，也是 WSFD-011307（抄送）和 WSFD-011308（负荷分担）的基础平台：

```
[WSFD-011305 AUTHMODE 决策] 透明鉴权/非透明/本地接入场景
                │
                │ 需要进行 Radius 鉴权/计费
                ▼
[WSFD-011306 Radius功能] ← 本特性
   ├── Radius 鉴权承载（Access-Request/Accept/Reject）
   │     └── 承载 Radius 地址分配（Access-Accept 携带 IP/池名 → WSFD-010502）
   ├── Radius 计费承载（Accounting Start/Interim/Stop）
   │     ├── 准实时计费（时间/流量阈值触发 Interim-Update）
   │     ├── Account ON/OFF（整机重启批量清除残留用户）
   │     └── 利用 Radius 鉴权服务器计费（鉴权服务器分配地址场景）
   ├── Radius 策略控制（AAA 下发 User-profile/Rule → 传递给 UPF）
   ├── Bypass 策略（Radius 无响应时 DEACTIVE/CONTINUE/HOLDINGTIME）
   └── 业务触发 RADIUS（用户激活或特定业务 L3/4 规则触发 Accounting Start）
                │
                ├──→ [WSFD-011307 Radius 抄送] 抄送给其他服务器
                └──→ [WSFD-011308 AAA 负荷分担] 多台 AAA Server 轮选
```

具体角色：

1. **Radius 协议承载**：封装/解封装/处理 Radius 鉴权和计费报文，UNC 作 Radius Client，AAA Server 作 Radius Server
2. **服务器模板与组管理**：通过 Radius-server Group 定义主备/负荷分担工作模式、重发次数、超时时间
3. **APN 级绑定**：每个 APN 绑定一个 Radius-server Group + Client IP + 计费控制参数 + 鉴权属性
4. **策略下发承载**：承载 AAA 下发的 User-profile/Rule（预定义规则），传递给 UPF 执行
5. **地址分配协同**：承载 Radius 分配方式下 Access-Accept 携带的用户 IP/地址池名

---

## 3. 原理与流程

### 3.1 基本功能点总览

#### 3.1.1 Radius-server Group 与 AAA Server 工作模式

UNC 支持根据不同 APN 分别配置 AAA Server，每个 APN 可以绑定一个 Radius-server Group。通过 `ADD RDSSVRGRP` 命令配置 Radius-server Group 下 AAA Server 的工作模式：

| 工作模式 | 说明 | 服务器参与规则 |
|---------|------|---------------|
| **主备模式（1+1）** | 一主一备，仅两个鉴权/计费服务器参与工作 | 主正常→全部发主；主故障→全部发备。配置 1 个以上主+1 个以上备时，仅一主一备参与，其他不参与 |
| **按优先级顺序选主** | 配置多个主服务器的优先级参数，按优先级顺序选主服务器 | 仅设置优先级的主服务器参与；备服务器与无优先级主服务器不参与。高优先级故障才发低优先级 |
| **负荷分担模式（轮选）** | RADIUS 报文按轮流选择方式发送给多台 AAA Server | 该模式下主备服务器都支持参与轮选，按一主一备顺序轮选；无备用服务器时在主用服务器间轮选（详见 WSFD-011308） |

每个 Radius-server Group 最多可配置 16 个主用 + 16 个备用 RADIUS 鉴权服务器，以及 16 个主用 + 16 个备用 RADIUS 计费服务器。

> 来源：`实现原理_31922672.md`（"原理概述/APN/AAA Server 映射功能"）

#### 3.1.2 其他基本功能

- **端口号可配置**：AAA Server 目的端口可选，默认鉴权 1812、计费 1813，可选范围 1~65535（兼容现网非标端口）
- **3GPP 扩展属性支持**：支持 3GPP 29.061 协议定义的扩展属性，可与 AAA Server 交互这些属性值
- **用户名域名剥离**：根据 APN 配置决定发往 AAA 的鉴权/计费消息中用户名是否带域名；APN 配置剥离→剥离域名后发往 AAA；不剥离→不操作；APN 未配置默认不剥离
- **重发次数与超时可配**：RADIUS 计费和鉴权消息的重发次数与超时时间可配，让用户根据网络情况灵活决定

> 来源：`实现原理_31922672.md`（"原理概述"基本功能列表）

### 3.2 RADIUS 鉴权功能点

| 功能点 | 说明 |
|-------|------|
| **RADIUS 方式分配 MS IP 地址** | 移动用户所分配的 IP 是 PDP 上下文激活阶段获得的动态地址，UNC 支持通过 RADIUS 认证过程从 AAA Server 获取用户 IP（→ 与 WSFD-010502 Radius 分配方式协同） |
| **Message-Authenticator 验证** | 收到包含 Message-Authenticator 属性的交互消息时，UNC 与 AAA Server 均按协议重新计算并与消息中的值比较；不同则丢弃消息 |
| **MSISDN 等用户信息转发** | UNC 通过 RADIUS 消息向 WAP GW 等外部网元转发 MSISDN、IMSI、APN、用户 IP 等用户信息 |
| **多种鉴权方式** | 支持 PAP、CHAP、MS-CHAP（仅 v1/v2）三种；根据 UE 携带 PCO/ePCO 信元种类支持不同用户类型鉴权 |
| **AAA Bypass** | Radius 鉴权超时无响应/计费服务器无响应时，支持配置 DEACTIVE/CONTINUE/HOLDINGTIME 三种动作（见 §3.4） |
| **响应消息端口检查** | UNC 默认检查 AAA Server 返回的 Access-Accept/Access-Reject 消息的源端口（通过 SET RDSRSPADDRCHK 配置） |

**鉴权方式与支持的用户类型对照表**：

| 信元 | 鉴权方式 | 支持鉴权的用户类型 |
|------|---------|------------------|
| PCO | PAP | 普通IP用户、PPP用户、L2TP用户 |
| PCO | CHAP | 普通IP用户、PPP用户、L2TP用户 |
| PCO | MS-CHAP（仅 v1/v2） | 普通IP用户 |
| ePCO | PAP | L2TP用户 |
| ePCO | CHAP | L2TP用户 |

> 来源：`实现原理_31922672.md`（"RADIUS 鉴权包含的功能点"）

### 3.3 RADIUS 计费功能点

| 功能点 | 说明 |
|-------|------|
| **RADIUS 非实时计费** | UNC 与外部数据网 Radius 服务器交互完成 Radius 计费流程，实现移动运营商与 Internet 运营商分别收费；可根据不同 APN 分别配置 |
| **RADIUS 准实时计费** | 根据用户的上网时间和流量门限触发，通过 Accounting-Request Interim-Update 消息发送到 AAA Server |
| **计费响应开关** | 控制未收到 Accounting Start Response 时是否去激活 PDP；关闭时先激活后去激活（高峰期频繁），UNC 提供计费消息流控（阈值内先激活后去激活，超阈值直接去激活） |
| **Account ON/OFF 消息** | 基于 APN 发送 Account ON/OFF 消息，用于 UNC 整机重启场景下通知 AAA 快速批量清除残留用户 |
| **利用 Radius 鉴权服务器计费** | 针对部分运营商 AAA 鉴权服务器分配地址需要计费消息 accounting 确认的场景；UNC 将计费消息发往用户的鉴权响应服务器以协助分配/回收地址；支持二次上下文、PBU 主备倒换、不计鉴权服务器状态 |
| **计费响应端口检查** | UNC 默认检查 AAA Server 返回的 Accounting Response 消息的源端口 |
| **基于 PGW-U/UPF 主送 Radius 计费/鉴权** | 通过 ADD UPLIST4RDS 配置 PGW-U/UPF List，通过 ADD RDSSVR 配置主送服务器绑定 List，实现按用户所锚定 PGW-U/UPF 发送特定 AAA 消息；多 UPF 场景只处理主锚点 UPF 的计费事件，辅锚点仅做流量累加 |

> 来源：`实现原理_31922672.md`（"RADIUS 计费包含的功能点"）

### 3.4 AAA Bypass 处理策略（Radius 服务器无响应）

针对 Radius 鉴权超时无响应与计费服务器无响应，UNC 提供三档动作策略：

| 场景 | 相关命令/参数 | 动作类型 |
|------|--------------|---------|
| Radius 鉴权超时无响应 | `SET APNAUTHATTR` AAANORSPCTRL | **DEACTIVE**（立即去活）/ **HOLDINGTIME=0**（放通用户）/ **HOLDINGTIME≠0**（延时去活） |
| Radius 计费服务器无响应 | `SET APNRDSACCTCTRL` DEACTIVE | **CONTINUE**（放通用户）/ **DEACTIVE**（立即去活）/ **SUPPORTACCTRSP=ENABLE**（等待计费开始响应，超时则激活失败）/ **SUPPORTACCTRSP=DISABLE**（不等待响应直接应答激活成功，超时按 DEACTIVE 判断） |
| Radius 服务器无响应紧急处理 | `SET FHBYPASS`（故障场景一键放通，优先级最高） | HOLDINGTIME=0 放通 / HOLDINGTIME≠0 延时去活 |

**动作类型说明**：

- **立即去活（DEACTIVE）**：本地配置命令参数为 DEACTIVE 时，不允许用户继续激活，网关立即去活用户
- **放通用户（CONTINUE 或 HOLDINGTIME=0）**：用户仍可激活成功并保持在线，直到用户主动下线。HOLDINGTIME 取值范围 0~1440
- **延时去活（HOLDINGTIME≠0）**：用户激活成功并保持在线，HOLDINGTIME 超时后网关主动发起去活。为防止 AAA 故障后瞬时大批量集中去活引发信令激增，可通过 ADJUSTRANGE 参数使去活时间在范围内随机延迟，实现离散去活

**SET FHBYPASS 注意事项**：
- 仅用于故障场景下的紧急处理，优先级高于 SET APNAUTHATTR:AAANORSPCTRL 与 SET APNRDSACCTCTRL:DEACTIVE 的 Bypass 配置
- 配置将影响用户激活状态，**只有在获得客户书面认可后方可使用**
- 采用放通用户动作类型时，**用户地址分配方式不能是 RADIUS 分配**

> 来源：`实现原理_31922672.md`（"AAA Bypass"章节、表2 Bypass处理策略）

### 3.5 RADIUS 策略控制功能点

#### 3.5.1 从 AAA 获得用户和业务属性

- **用户属性**：用户的预付费/后付费属性
- **业务属性**：用户签约业务列表，UNC 识别并限制用户只能访问业务列表中的业务
- **下发流程**：用户激活时，AAA 将用户属性和业务策略下发给 UNC，并由 UNC 传递给 PGW-U/UPF；PGW-U/UPF 根据外部实体下发的信息对业务进行控制和处理
- **业务策略优先级**（从高到低）：AAA 服务器 > 本地 APN > 本地 GLOBAL；AAA Server 失效时使用本地业务策略

#### 3.5.2 AAA 下发策略规则

对于部署 PCRF 成本较高/网络复杂的运营商，UNC 支持通过扩展 AAA 鉴权响应消息实现策略下发：

- **适用场景**：无 PCC 应用（某 PDP 的 PCC 功能通过 AAA 鉴权响应消息指示不使能，或 PCRF 状态异常）
- **PCRF 正常时**：UNC 将 AAA 下发策略转发给 PCRF 做参考，由 PCRF 决策后向 UNC 发送新策略
- **规则映射**：AAA 下发的 Charging-rule-base-name 对应本地 User-profile；Charging-rule-name 对应本地 Rule。UNC 据此激活本地配置的**预定义规则**（不支持动态规则）
- **冲突处理**：同一会话同时存在 AAA 下发与本地配置策略时，**以 AAA 下发为准**；AAA 未下发则以本地配置为准；同时下发多个 User-profile 时使用第一个绑定的策略

#### 3.5.3 其他策略控制

- **RAT 触发属性更新**：通过 UNC 配置控制 RAT 改变时是否触发 Accounting Interim Update Message，通知其他网元用户接入网络的变化
- **基于 RADIUS POD 消息去激活**：支持 AAA Server 主动发起的 POD 消息去激活用户；支持 POD 合法性检查（仅接收配置 Server IP 的 POD）；可根据 Acct-Session-Id + 3GPP-Teardown-Indicator 去活，或为兼容非 3GPP 扩展 AAA 根据接入侧接口 IP + Charging ID 去活
- **业务触发 RADIUS 消息**：UNC 支持用户激活过程中或访问特定业务时给 AAA Server 发送 RADIUS 消息，使 AAA Server 获取用户信息（详见 §3.6）

> 来源：`实现原理_31922672.md`（"RADIUS 策略控制包含的功能点"）

### 3.6 业务触发 RADIUS 消息

UNC 支持两种业务触发 RADIUS 消息方式（通过 `SET APNRDSACCTCTRL` 的 SRVTRIGGER 参数配置）：

| 触发方式 | 触发时机 | 消息等待行为 |
|---------|---------|------------|
| **用户激活过程中发送** | 用户激活过程中给 AAA Server 发送 RADIUS Accounting-Request Start 消息 | 发送后**不等待** AAA Server 返回应答，只是将用户信息通过消息携带给 AAA Server；此消息不对用户激活过程产生任何影响 |
| **访问特定业务时发送** | 激活过程中不发送；当用户访问了特定业务时，UNC 根据 L3/4 层业务匹配规则判断出需要发送 | 此时发送 RADIUS Accounting-Request Start 消息携带用户信息；支持通过 BUFFERTIMEVALUE 参数配置等待 RADIUS 响应消息的时长 |

> 来源：`实现原理_31922672.md`（"支持业务触发 RADIUS 消息"）

### 3.7 业务流程（激活/去激活）

Radius 业务流程包含激活流程与去激活流程（详见产品文档图1/图2）：

```
Radius 业务激活流程（简）：
  UE → UNC(PDP/承载/PDU激活) → UNC 发起 Radius Access-Request
    → AAA Server 鉴权 → Access-Accept/Reject
  鉴权通过 → UNC 发起 Radius Accounting-Request Start
    → AAA Server 计费响应（可选等待）
  UNC 回应激活成功应答 → 用户上线
  （业务过程中按时间/流量阈值触发 Accounting-Request Interim-Update）

Radius 业务去激活流程（简）：
  用户主动下线 / POD 触发 / Bypass 超时
    → UNC 发起 Radius Accounting-Request Stop
    → AAA Server 释放地址/计费收尾
  UNC 去激活用户
  （UNC 整机重启场景：基于 APN 发送 Account ON/OFF 批量清除残留用户）
```

> 来源：`WSFD-011306 Radius功能特性概述_31467848.md`（"原理概述/业务流程"图2、图3）、`实现原理_31922672.md`（"业务流程"图1、图2）

### 3.8 到 AAA Server 的组网方式（4 种变体）

UNC 与 AAA Server 之间的组网提供 4 种场景，核心差异在 L3VPN 实例划分、Gi 接口绑定、路由方式与可靠性：

| 组网场景 | L3VPN 划分 | 路由方式 | 可靠性 | 典型用途 |
|---------|-----------|---------|--------|---------|
| **单平面 + 静态路由 + BFD** | vpn_pdn（数据）+ vpn_aaa（Radius 信令） | 静态路由 | BFD | 简单组网，Radius 信令与数据报文分离出接口 |
| **双平面 + OSPF 动态路由 + BFD** | vpn_pdn + vpn_aaa | OSPF 动态路由 | BFD | 双平面冗余，动态路由收敛 |
| **带内组网 GRE VPN** | 通过 GRE 隧道承载 | GRE 隧道 | GRE | Radius 信令与数据报文共用通道，通过 GRE 隧道隔离 |
| **带外组网 GRE VPN** | vpn_pdn + vpn_aaa，GRE 隧道承载 Radius | GRE 隧道 | GRE | Radius 信令走独立通道（带外），通过 GRE 隔离 |

**通用配置对象**（所有组网均涉及）：
- `ADD L3VPNINST` + `ADD VPNINSTAF`：L3VPN 实例（VRFNAME=vpn_pdn/vpn_aaa，VRFRD=100:1/200:1）
- `ADD VPNINST`：业务侧 VPN 实例
- `ADD LOGICIP` + `ADD LOGICINF`：Gi 逻辑接口（giif1/0/0 用于鉴权 AAA、giif1/0/1 用于计费 AAA，绑定 vpn_aaa）
- `ADD RDSSVRGRP` + `ADD RDSSVR`：Radius 服务器组与服务器
- `ADD APN` + `ADD APNRDSCLIENTIP` + `ADD APNRDSSVRGRP`：APN 级绑定

> 来源：`配置到AAA Server的数据（单平面+静态路由+BFD组网）_32044985.md`（其余三种组网变体在该场景基础上增加 OSPF 动态路由 / GRE 隧道配置，命令骨架一致）

---

## 4. 配置规则

### 4.1 激活步骤（配置 RADIUS 功能，9 步主流程）

```
步骤1：配置 AAA 服务器组与重发/超时
  └── ADD RDSSVRGRP
        ├── MODE=MASTER_SLAVE / ROUND_ROBIN
        ├── ACCTTIMEOUT / ACCTRETRANSMIT / AUTHTIMEOUT / AUTHRETRANSMIT
        └── ACCTSVRTOUT / ACCTSVRDTIME / AUTHSVRTOUT / AUTHSVRDTIME

步骤2：配置鉴权 AAA 服务器（PORT=1812）
  └── ADD RDSSVR SERVERTYPE=AUTHENTICATION, PRIFLAG=PRIMARY/SECONDARY, PRIORITY=...

步骤3（可选）：配置 UP 列表（按 PGW-U/UPF 主送）
  └── ADD UPLIST4RDS

步骤4（可选）：配置计费 AAA 服务器（PORT=1813）
  └── ADD RDSSVR SERVERTYPE=ACCOUNTING, PRIFLAG=PRIMARY/SECONDARY, PRIORITY=...

步骤5：配置 Radius 参数
  a. SET RDSACCTREQVSA        → 计费 AAA 服务器组私有扩展属性（3GPP/3GPP2）
  b. (可选) SET RDSACCTREQATTR → 计费 AAA 服务器可选消息属性
  c. (可选) SET RDSAUTHREQVSA  → 鉴权请求携带私有扩展属性
  d. (可选) MOD RDSSVRGRP      → 修改 Radius 服务器组可选计费消息属性
  e. ADD APNRDSCLIENTIP        → APN 下绑定鉴权 Client IP（INTFNAME）
                                ※ 没有配置 Client IP，该 APN 用户激活失败
  f. ADD APNRDSSVRGRP          → APN 下绑定 AAA 服务器组
  g. (可选) SET APNRDSACCTCTRL → APN 级计费阈值/业务触发/SUPPORTACCTRSP
  h. (可选) SET APNAUTHATTR    → 开启 RADIUS PoD 功能
  i. (可选) SET APNRADIUSATTR  → 域名增加/剥离（前缀/后缀）

步骤6（可选，故障紧急）：一键放通
  └── SET FHBYPASS
        ※ 优先级高于 SET APNAUTHATTR:AAANORSPCTRL 与 SET APNRDSACCTCTRL:DEACTIVE
        ※ 需客户书面认可

步骤7（可选）：配置 Specific APN（指定上报 APN）
  └── ADD SPECIFICAPNVAL

步骤8（可选）：配置 Radius 响应消息源端口检查
  └── SET RDSRSPADDRCHK（默认开启，有防火墙/NAT 时需关闭）
```

> 来源：`配置RADIUS功能_32909765.md`（"操作步骤"）

### 4.2 MML命令清单

#### 4.2.1 Radius 服务器与组核心命令

| 命令 | 用途 | 关键参数 |
|------|------|---------|
| ADD RDSSVRGRP | 增加 Radius 服务器组 | RDSSVRGRPNAME, MODE=MASTER_SLAVE/ROUND_ROBIN, ACCTTIMEOUT/ACCTRETRANSMIT/AUTHTIMEOUT/AUTHRETRANSMIT, ACCTSVRTOUT/ACCTSVRDTIME/AUTHSVRTOUT/AUTHSVRDTIME |
| ADD RDSSVR | 增加 RADIUS 服务器 | RDSSVRGRPNAME, SERVERTYPE=AUTHENTICATION/ACCOUNTING, IPVERSION, SERVERIPV4, PORT(1812/1813), VPNINSTANCE, CIPHERKEY, PRIFLAG=PRIMARY/SECONDARY, PRIORITY, CIPHERKEYCNFM |
| MOD RDSSVRGRP | 修改 Radius 服务器组 | （可选计费消息属性等） |
| MOD RDSSVR | 修改 RADIUS 服务器 | - |
| LST RDSSVRGRP | 查询 Radius 服务器组 | - |

#### 4.2.2 APN 级 Radius 绑定命令

| 命令 | 用途 | 关键参数 |
|------|------|---------|
| ADD APNRDSSVRGRP | 设置 APN Radius 服务器组 | APN, RDSSVRGRPNAME |
| ADD APNRDSCLIENTIP | 增加 APN Radius Client IP 接口 | APN, AUTHORACCT=AUTHENTICATION/ACCOUNTING, INTFNAME |
| SET APNRDSACCTCTRL | 设置 APN RADIUS 计费控制参数 | APN, TIMETHRESHOLD, VOLUMETHRESHOLD, SUPPORTACCTRSP, SUPPORTACCTUPD, RATTRIGGER, SRVTRIGGER, BUFFERTIMEVALUE, DEACTIVE |
| SET APNAUTHATTR | 设置 APN 鉴权属性配置 | APN, AAANORSPCTRL, DISCONNECT（PoD 开关） |
| SET APNRADIUSATTR | 设置 APN RADIUS 配置（域名） | APN, DOMAINNAMEACT=ADD_ENABLE_STRIP_DISABLE, DOMAINNAMEPOS=SUFFIX |

#### 4.2.3 Radius 信元控制命令

| 命令 | 用途 |
|------|------|
| SET RDSACCTREQVSA | 设置 RADIUS 计费服务器组的私有扩展属性（3GPP/3GPP2） |
| SET RDSACCTREQATTR | 设置 RADIUS 计费服务器可选消息属性 |
| SET RDSAUTHREQVSA | 设置 RADIUS 鉴权请求携带的私有扩展属性 |
| SET RDSRSPADDRCHK | 设置全局 RADIUS 响应消息源 IP/端口检查配置 |

#### 4.2.4 Bypass 与紧急处理命令

| 命令 | 用途 | 优先级说明 |
|------|------|-----------|
| SET FHBYPASS | 设置失败旁路处理（故障场景一键放通） | **最高**（高于 APNAUTHATTR 与 APNRDSACCTCTRL） |

#### 4.2.5 业务触发 RADIUS 相关命令（独立子场景）

| 命令 | 用途 |
|------|------|
| ADD APN | 增加 APN 配置（业务触发场景需先建 APN） |
| SET APNRDSACCTCTRL | 使能业务触发 RADIUS（SRVTRIGGER=ENABLE） |
| ADD FLOWFILTER | 增加流过滤器（需与 UPF/PGW-U 一致） |
| ADD RULE | 增加规则（POLICYTYPE=SRV_TRIGGER） |
| ADD USERPROFILE | 增加用户模板（UPTYPE=PCC） |
| ADD RULEBINDING | 增加用户模板与规则绑定 |
| ADD USRPROFGROUP | 增加用户模板组 |
| ADD UPBINDUPG | 增加用户模板组与用户模板绑定 |
| ADD APNUSRPROFG | 增加 APN 用户模板组绑定 |

#### 4.2.6 UP 主送与组网基础命令

| 命令 | 用途 |
|------|------|
| ADD UPLIST4RDS | 向 RADIUS 服务器使用的 UP 列表中增加 UP（按 PGW-U/UPF 主送） |
| ADD L3VPNINST / ADD VPNINSTAF / ADD VPNINST | L3VPN 实例与业务 VPN 实例 |
| ADD LOGICIP / ADD LOGICINF | 逻辑 IP 与逻辑接口（Gi 接口） |
| ADD INTERFACE / ADD IPBINDVPN / ADD IFIPV4ADDRESS / ADD IFIPV6ADDRESS | 接口与 IP 配置 |
| ADD GRETUNNEL | GRE 隧道（带内/带外 GRE VPN 组网） |
| ADD SRROUTE / ADD SRROUTE6 | IPv4/IPv6 静态路由 |
| ADD ACLGROUP / ADD ACLRULEADV4 | ACL 规则组与高级 ACL |
| ADD IPSECPROPOSAL / ADD IPSECINTFCFG | IPsec 提议与隧道接口 |
| ADD SPECIFICAPNVAL | 增加 Specific APN 映射（指定上报 APN） |

#### 4.2.7 业务策略命令（AAA 下发策略映射用）

| 命令 | 用途 |
|------|------|
| ADD RULE / ADD USERPROFILE / ADD RULEBINDING / ADD USRPROFGROUP / ADD UPBINDUPG / ADD APNUSRPROFG | 业务模板体系（对应 AAA 下发 Charging-rule-base-name / charging-rule-name） |

#### 4.2.8 调测与查询命令

| 命令 | 用途 |
|------|------|
| TST AAA | 测试 AAA 服务器（UNC 到 AAA Server 的 Radius 探测） |
| DSP ROUTE | 显示 IPv4 路由表（查 UNC 到 AAA Server 路由） |
| LST APNUSRPROFG / LST RULEBINDING / LST RULE | 查询业务策略组合绑定关系（业务触发调测） |
| EXP MML | 导出 MML 配置文件（故障收集） |

> 来源：`WSFD-011306 Radius功能参考信息_15542176.md`（"命令"章节，完整命令清单）

### 4.3 关键参数说明

#### 4.3.1 ADD RDSSVRGRP 关键参数（服务器组与超时/重发）

| 参数 | 取值样例 | 说明 |
|------|---------|------|
| RDSSVRGRPNAME | isprg | Radius Server Group 名称 |
| MODE | MASTER_SLAVE / ROUND_ROBIN | 工作模式：主备 / 轮选负荷分担（按优先级选主通过多个主服务器 PRIORITY 实现） |
| SIGOPTACCTMSG | DISABLE | 支持可选计费消息开关 |
| ACCTTIMEOUT | 10 | Radius Accounting Request 超时时间（秒） |
| ACCTRETRANSMIT | 5 | Radius Accounting Request 重发次数 |
| AUTHTIMEOUT | 10 | Radius Authentication Request 超时时间（秒） |
| AUTHRETRANSMIT | 5 | Radius Authentication Request 重发次数 |
| ACCTSVRTOUT | 12 | Radius 计费服务器超时时长（秒） |
| ACCTSVRDTIME | 180 | Radius 计费服务器 Down 状态保持时长（秒） |
| AUTHSVRTOUT | 12 | Radius 鉴权服务器超时时长（秒） |
| AUTHSVRDTIME | 180 | Radius 鉴权服务器 Down 状态保持时长（秒） |

#### 4.3.2 ADD RDSSVR 关键参数（鉴权/计费服务器模板）

| 参数 | 取值样例 | 说明 |
|------|---------|------|
| RDSSVRGRPNAME | isprg | 所属 Radius Server Group |
| SERVERTYPE | **AUTHENTICATION** / **ACCOUNTING** | 服务器角色：鉴权（PORT=1812）/ 计费（PORT=1813） |
| IPVERSION | IPV4 | 服务器 IP 版本 |
| SERVERIPV4 | 10.168.10.1 | 服务器 IPv4 地址（与 AAA Server 实际 IP 一致） |
| PORT | 1812（鉴权）/ 1813（计费） | 服务器端口，可选范围 1~65535 |
| VPNINSTANCE | vpn1 / vpn_aaa | 所属 VPN 实例（带外/GRE 组网时必配） |
| CIPHERKEY | ***** | 服务器密钥（加密的）；鉴权与计费 AAA 服务器的密钥可以不同；同一 IP+VPN 的 Server 在不同组里的密钥不需限制 |
| PRIFLAG | **PRIMARY** / SECONDARY | 主备用类型 |
| PRIORITY | 1 | 服务器优先级（按优先级选主模式生效） |
| CIPHERKEYCNFM | ***** | 确认服务器密钥 |

#### 4.3.3 ADD APNRDSCLIENTIP 关键参数（APN Client IP）

| 参数 | 取值样例 | 说明 |
|------|---------|------|
| APN | apn-test | APN 名称 |
| AUTHORACCT | **AUTHENTICATION** / **ACCOUNTING** | 鉴权或计费请求消息的 Radius Client IP（需分别配置） |
| INTFNAME | giif1/0/1 | 接口名称（已通过 ADD LOGICINF 配置） |

> **关键约束**：如果没有配置 Client IP，则该 APN 用户激活失败（文档明确）。

#### 4.3.4 SET APNRDSACCTCTRL 关键参数（APN 级计费控制）

| 参数 | 取值样例 | 说明 |
|------|---------|------|
| APN | apn-test | APN 名称 |
| TIMETHRESHOLD | 30 | 时间阈值（分），准实时计费触发 |
| VOLUMETHRESHOLD | 20 | 流量阈值（千字节），准实时计费触发 |
| SUPPORTACCTRSP | **ENABLE** / DISABLE | 是否等待计费开始响应消息后才回应激活成功应答（ENABLE：等待，超时激活失败；DISABLE：不等待，超时按 DEACTIVE 判断） |
| SUPPORTACCTUPD | ENABLE | MME/SGSN/SGW 发起 PDP 上下文更新时是否支持发送计费更新 |
| RATTRIGGER | ENABLE | RAT 变化触发计费更新消息 |
| SRVTRIGGER | **ENABLE** / DISABLE | 业务报文（通过 3/4 层规则配置）时触发计费请求消息（业务触发 RADIUS 总开关） |
| BUFFERTIMEVALUE | 2 | 业务报文延时时间（秒），业务触发 RADIUS 发送时等待响应时长 |
| DEACTIVE | CONTINUE / DEACTIVE | 计费服务器请求超时是否去活用户 |

#### 4.3.5 SET APNAUTHATTR 关键参数（APN 鉴权属性）

| 参数 | 取值样例 | 说明 |
|------|---------|------|
| APN | apn-test | APN 名称 |
| AAANORSPCTRL | DEACTIVE / HOLDINGTIME | AAA 鉴权服务器无响应处理（立即去活/延时去活/放通） |
| DISCONNECT | **ENABLE** | DM 开关，配置是否支持 RADIUS PoD 功能 |

#### 4.3.6 SET APNRADIUSATTR 关键参数（域名处理）

| 参数 | 取值样例 | 说明 |
|------|---------|------|
| APN | apn-test | APN 名称 |
| DOMAINNAMEACT | **ADD_ENABLE_STRIP_DISABLE** | 增加或剥离域名（同时开启两个功能需执行该命令两次） |
| DOMAINNAMEPOS | SUFFIX | 域名位置：前缀 / 后缀（分隔符由 SET DOMAINSEPARATOR 配置） |

#### 4.3.7 SET FHBYPASS 关键参数（故障紧急一键放通）

| 参数 | 说明 |
|------|------|
| HOLDINGTIME | 取值 0~1440；0=放通用户；非 0=延时去活 |
| ADJUSTRANGE | 使用户在 ADJUSTRANGE 时长范围内随机延迟去活，避免集中去活引发信令激增 |

> **优先级最高**：高于 SET APNAUTHATTR:AAANORSPCTRL 与 SET APNRDSACCTCTRL:DEACTIVE；需客户书面认可；采用放通用户时地址分配方式不能是 Radius 分配。

### 4.4 约束条件

| 约束类型 | 约束内容 |
|---------|---------|
| Client IP 必配 | 没有配置 Client IP（ADD APNRDSCLIENTIP），该 APN 用户**激活失败** |
| AAA Server 参数一致性 | UNC 配置的 AAA Server 的 IP 地址、端口、Key **必须**与 AAA Server 网元配置一致 |
| AAA Server 最大数量 | 整机最大支持 4000 个 AAA Server |
| 单组服务器数 | 每个 Radius-server Group 最多 16 主 + 16 备鉴权服务器，以及 16 主 + 16 备计费服务器 |
| 端口范围 | AAA Server 目的端口可选范围 1~65535，默认鉴权 1812、计费 1813 |
| 主备模式参与数 | 1+1 主备仅两个鉴权/计费服务器参与工作；配置多个时仅一主一备参与 |
| 按优先级选主参与规则 | 仅设置优先级的主服务器参与；备服务器与无优先级主服务器不参与 |
| Bypass 放通约束 | 采用放通用户动作类型时，用户**地址分配方式不能是 RADIUS 分配** |
| SET FHBYPASS 使用约束 | 仅用于故障场景紧急处理；需客户书面认可；优先级最高 |
| MS-CHAP 用户类型限制 | MS-CHAP（仅 v1/v2）只支持普通 IP 用户（PCO 信元）；PAP/CHAP 支持普通 IP/PPP/L2TP 用户 |
| AAA 下发策略限制 | AAA 下发的策略目前只支持**预定义规则**，不支持动态规则 |
| AAA 与本地策略冲突 | 同一会话同时存在 AAA 下发与本地策略时，**以 AAA 下发为准** |
| 多 User-profile 下发 | 同时下发多个 User-profile 时，使用第一个 User-profile 下绑定的策略 |
| 业务触发 C-U 一致性 | 业务触发 RADIUS 场景的 FlowFilter/Rule 需与 UPF/PGW-U 上配置一致 |
| 业务触发 APN 既有用户 | 业务策略组合绑定 APN 后，对该 APN 已存在用户无效，只对后续激活的用户生效 |
| 响应端口检查默认开启 | 如组网部署防火墙/NAT 或 AAA 响应修改 IP/Port，需关闭 SET RDSRSPADDRCHK |

> 来源：`配置RADIUS功能_32909765.md`、`实现原理_31922672.md`、`WSFD-011306 Radius功能特性概述_31467848.md`

---

## 5. 配置案例

### 5.1 典型场景一：配置 RADIUS 功能（主备模式 + 主用鉴权/计费 AAA 服务器）

**场景描述**：UNC 上开启 RADIUS 功能，配置一个主备模式的 Radius 服务器组 isprg，包含主用鉴权 AAA 服务器（10.168.10.1:1812）和主用计费 AAA 服务器（10.168.10.1:1813），并在 apn-test 下绑定该服务器组、Client IP、计费控制参数。

**MML命令序列（原样保留）**：

```
//配置AAA服务器组。
ADD RDSSVRGRP: RDSSVRGRPNAME="isprg", MODE=MASTER_SLAVE, SIGOPTACCTMSG=DISABLE, ACCTTIMEOUT=10, ACCTRETRANSMIT=5, AUTHTIMEOUT=10, AUTHRETRANSMIT=5, ACCTSVRTOUT=12, ACCTSVRDTIME=180, AUTHSVRTOUT=12, AUTHSVRDTIME=180;

//配置鉴权AAA服务器。
ADD RDSSVR: RDSSVRGRPNAME="isprg", SERVERTYPE=AUTHENTICATION, IPVERSION=IPV4, SERVERIPV4="10.168.10.1", PORT=1812, VPNINSTANCE="vpn1", CIPHERKEY="*****", PRIFLAG=PRIMARY, PRIORITY=1, CIPHERKEYCNFM="*****";

//配置计费AAA服务器。
ADD RDSSVR: RDSSVRGRPNAME="isprg", SERVERTYPE=ACCOUNTING, IPVERSION=IPV4, SERVERIPV4="10.168.10.1", PORT=1813, VPNINSTANCE="vpn1", CIPHERKEY="*****", PRIFLAG=PRIMARY, PRIORITY=1, CIPHERKEYCNFM="*****";

//配置RADIUS参数。
SET RDSACCTREQVSA: RDSSVRGRPNAME="isprg",THREEGPP=ENABLE,THREEGPP2=DISABLE;

ADD APNRDSCLIENTIP: APN="apn-test",AUTHORACCT=AUTHENTICATION,INTFNAME="giif1/0/1";
ADD APNRDSCLIENTIP: APN="apn-test",AUTHORACCT=ACCOUNTING,INTFNAME="giif1/0/1";

ADD APNRDSSVRGRP: APN="apn-test",RDSSVRGRPNAME="isprg";

SET APNRDSACCTCTRL: APN="apn-test",TIMETHRESHOLD=30,VOLUMETHRESHOLD=20,SUPPORTACCTRSP=ENABLE,SUPPORTACCTUPD=ENABLE,RATTRIGGER=ENABLE,SRVTRIGGER=ENABLE,BUFFERTIMEVALUE=2;

SET APNRADIUSATTR:APN="apn-test",DOMAINNAMEACT=ADD_ENABLE_STRIP_DISABLE,DOMAINNAMEPOS=SUFFIX;

SET APNAUTHATTR: APN="apn-test", DISCONNECT=ENABLE;
```

> 来源：`配置RADIUS功能_32909765.md`（"任务示例"脚本，原样保留）

### 5.2 典型场景二：配置到 AAA Server 的数据（单平面 + 静态路由 + BFD，带外组网）

**场景描述**：AAA Server 位于 Internet 中，UNC 与计费/鉴权 AAA 服务器采用带外组网（到 PDN 的数据报文与到 AAA 的 Radius 信令报文使用不同出接口、绑定不同 VPN）。配置 vpn_pdn（数据）与 vpn_aaa（Radius 信令）两个 L3VPN，Gi 接口 giif1/0/0（10.8.20.1）用于鉴权 AAA，giif1/0/1（10.8.20.2）用于计费 AAA，AAA 服务器组 isprg 采用轮选模式。

**MML命令序列（原样保留）**：

```
//参考 配置静态路由+BFD组网（IPv4） 配置对应的组网。

//创建L3VPN实例。
//1.数据报文所属的L3VPN实例。
ADD L3VPNINST: VRFNAME ="vpn_pdn";
ADD VPNINSTAF: VRFNAME ="vpn_pdn",AFTYPE=ipv4uni,VRFRD="100:1", VRFLABELMODE=perRoute;

//2.RADIUS信令报文所属的L3VPN实例。
ADD L3VPNINST: VRFNAME ="vpn_aaa";
ADD VPNINSTAF: VRFNAME="vpn_aaa", AFTYPE=ipv4uni, VRFRD="200:1", VRFLABELMODE=perRoute;

//创建VPN实例。
ADD VPNINST: VPNINSTANCE ="vpn_pdn";
ADD VPNINST:VPNINSTANCE="vpn_aaa";

//配置Gi接口。
//1.配置Giif1/0/0接口。
ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.1", VPNINSTNAME="vpn_aaa";
ADD LOGICINF:NAME="giif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_aaa";

//2.配置Giif1/0/1接口。
ADD LOGICIP: IPVERSION=IPv4, LOGICIPV4="10.8.20.2", VPNINSTNAME="vpn_aaa";
ADD LOGICINF:NAME="giif1/0/1",IPVERSION=IPV4,IPV4ADDRESS1="10.8.20.2",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn_aaa";

//配置鉴权/计费AAA服务器。
ADD RDSSVRGRP: RDSSVRGRPNAME="isprg", MODE=ROUND_ROBIN, SIGOPTACCTMSG=DISABLE;

ADD RDSSVR: RDSSVRGRPNAME="isprg", SERVERTYPE=AUTHENTICATION, IPVERSION=IPV4, SERVERIPV4="10.168.10.1", PORT=1812, VPNINSTANCE="vpn_aaa", CIPHERKEY="*****", PRIFLAG=PRIMARY, CIPHERKEYCNFM="*****";

ADD RDSSVR: RDSSVRGRPNAME="isprg", SERVERTYPE=ACCOUNTING, IPVERSION=IPV4, SERVERIPV4="10.168.10.1", PORT=1813, VPNINSTANCE="vpn_aaa", CIPHERKEY="*****", PRIFLAG=PRIMARY, CIPHERKEYCNFM="*****";

ADD APN: APN="apn1", HASVPN=ENABLE, VPNINSTANCE="vpn_pdn", HASVPNIPV6=DISABLE, RESTORPGWSWITCH=INHERIT, REACWITHDEL=DISABLE;

ADD APNRDSCLIENTIP: APN="apn1",AUTHORACCT=AUTHENTICATION,INTFNAME="giif1/0/0";
ADD APNRDSCLIENTIP: APN="apn1",AUTHORACCT=ACCOUNTING,INTFNAME="giif1/0/1";

ADD APNRDSSVRGRP: APN="apn1",RDSSVRGRPNAME="isprg";
```

> 来源：`配置到AAA Server的数据（单平面+静态路由+BFD组网）_32044985.md`（"任务示例"脚本，原样保留）

### 5.3 典型场景三：配置业务触发 RADIUS 功能（访问特定业务时发送 Radius 消息）

**场景描述**：用户访问 www.huawei.com 时，UNC 发送 RADIUS Accounting-Request Start 消息，携带用户信息发送给 AAA Server。需要在 apn-test 下使能业务触发 RADIUS 功能（SRVTRIGGER=ENABLE），并配置业务规则（POLICYTYPE=SRV_TRIGGER）、用户模板、用户模板组、APN 绑定关系。业务规则需与 UDG 侧一致。

**MML命令序列（原样保留）**：

```
//配置业务触发RADIUS功能。
ADD APN: APN="apn-test";
SET APNRDSACCTCTRL: APN="apn-test",SRVTRIGGER=ENABLE;

//配置业务规则（为了确保该功能生效，请在UDG上配置相同的业务规则，并绑定该业务触发使用的流过滤器。流过滤器的配置请参考UDG上内容感知相关章节。）。
ADD RULE: RULENAME="rule_test1", POLICYTYPE=SRV_TRIGGER, PRIORITY=50;

//配置业务策略组合。
ADD USERPROFILE: USERPROFILENAME="up_test", UPTYPE=PCC;
ADD RULEBINDING: USERPROFILENAME="up_test", RULENAME="rule_test1";
ADD USRPROFGROUP: USERPROFGNAME="upg_test";
ADD UPBINDUPG: USERPROFGNAME="upg_test", UPBINDTYPE=DEFAULT, USERPROFILENAME="up_test";
ADD APNUSRPROFG: APN="apn-test", USERPROFGNAME="upg_test";
```

> 来源：`配置业务触发RADIUS功能_33000859.md`（"任务示例"脚本，原样保留）

### 5.4 场景变体对照

| 变体 | 核心差异 | 关键命令/参数 | 文档覆盖度 |
|------|---------|--------------|-----------|
| 主备模式 Radius 配置 | MODE=MASTER_SLAVE，一主一备 | ADD RDSSVRGRP MODE=MASTER_SLAVE + ADD RDSSVR PRIFLAG=PRIMARY | 完整脚本（场景一） |
| 轮选负荷分担模式 | MODE=ROUND_ROBIN，轮选发送 | ADD RDSSVRGRP MODE=ROUND_ROBIN（详见 WSFD-011308） | 完整脚本（场景二） |
| 按优先级选主 | 多个主服务器 PRIORITY 参数 | ADD RDSSVR PRIORITY=1/2/3... | 仅原理，无独立脚本 |
| 单平面+静态路由+BFD（带外） | vpn_pdn + vpn_aaa，Gi 双接口 | ADD L3VPNINST/VPNINSTAF/VPNINST + LOGICINF | 完整脚本（场景二） |
| 双平面+OSPF+BFD | 在单平面基础上增加 OSPF 动态路由 | （在场景二基础上增加 OSPF 配置） | 场景变体 |
| 带内组网 GRE VPN | GRE 隧道承载 Radius 信令 | ADD GRETUNNEL | 场景变体 |
| 带外组网 GRE VPN | vpn_pdn + vpn_aaa + GRE 隧道 | ADD GRETUNNEL + ADD VPNINST | 场景变体 |
| 业务触发 RADIUS | 用户激活或特定业务触发 Accounting Start | SET APNRDSACCTCTRL SRVTRIGGER=ENABLE + ADD RULE POLICYTYPE=SRV_TRIGGER | 完整脚本（场景三） |
| Radius 地址分配 | Access-Accept 携带用户 IP/池名 | （通过 Radius 鉴权流程承载，无独立脚本） | 仅原理（详见 WSFD-010502） |
| AAA 下发策略 | Charging-rule-base-name / charging-rule-name | ADD USERPROFILE/RULE/RULEBINDING | 仅原理 |
| Bypass 紧急放通 | 故障场景一键放通 | SET FHBYPASS（需客户书面认可） | 仅原理 |

---

## 6. 验证与调测

### 6.1 调测 UNC 到 AAA Server 的数据通信

#### 6.1.1 调测前提与目的

当运营商部署分组交换网、新增 UNC 或 AAA Server 时，UNC 和 AAA Server 完成互通数据配置后，需要检查 UNC 与 AAA Server 之间的链路是否连通。

> 适用：GGSN、PGW-C、SMF

#### 6.1.2 调测执行步骤（6 步）

**步骤1**：执行 `TST AAA` 命令调测 UNC 到 AAA Server 的数据通信。

```
TST AAA: SERVERTYPE=ACCOUNTING, IPVERSION=IPV4, IPADDRESS="10.1.128.23";
TST AAA: SERVERTYPE=AUTHENTICATION, VPNINSTANCE="test_vpn", IPVERSION=IPV4, IPADDRESS="10.1.128.23";
```

- 返回检测成功消息 → 通信正常，调测结束
- 检测无响应消息 → 执行步骤2

**步骤2**：执行 `NGPING` 命令查看 UNC 到 AAA Server 的连接是否正常。
- **关键**：务必指定源地址 SRCIPV4ADDR 为 UNC 的 Gi 接口 IP 地址（否则只能检查物理连接）；使用 VPN 组网时还需指定 VPNNAME
- 收到对端响应 → 连接正常，执行步骤3
- 出现 timeout → 链路不通，执行步骤4

**步骤3**：执行 `LST RDSSVRGRP` 查看 UNC 上 AAA 服务器组配置是否与规划值及 AAA Server 配置一致，Radius-Server Group 与 APN 绑定关系是否配置完成。
- **关键约束**：UNC 上配置的 AAA Server 的 IP 地址、端口、Key 必须和 AAA Server 网元配置一致
- 一致 → 执行步骤5
- 不一致 → 参考"配置 RADIUS 功能"重新配置

**步骤4**：检查 UNC 到 AAA Server 的互通（路由/可靠性组网/VPN 组网逐项调测），再次执行步骤1。

**步骤5**：查看是否存在告警 ID "100197"（RADIUS 鉴权服务器无响应）或 "81020"（RADIUS 计费服务器无响应）。
- 产生告警 → 参考 ALM-100197 / ALM-81020 处理步骤
- 无告警 → 执行步骤6

**步骤6**：收集信息寻求技术支持（EXP MML 导出配置 + 保存所有查询信息 + 联系华为技术支持）。

> 来源：`调测到AAA Server的数据_32027181.md`（"操作步骤"）

### 6.2 调测业务触发 RADIUS 功能

#### 6.2.1 调测执行步骤（5 步）

**步骤1**：OM Portal 上选择 Gi/SGi 接口跟踪，参数配置对话框中选择 "ACCT"，跟踪 RADIUS 计费消息。

**步骤2**：测试终端使用 "apn-test" APN 接入网络。
- 成功接入 → 执行步骤3
- 无法接入 → 调测 UNC 的接入功能

**步骤3**：使用测试终端访问 www.huawei.com（配置中触发的业务网页），查看 UNC 是否给业务网关发送了 RADIUS 计费消息（源地址、目的地址、消息 ID 正确则调测成功）。

**步骤4**：检查 APN 下业务触发 RADIUS 相关配置是否正确：
- `LST APNUSRPROFG:APN="apn-test";` 查询 APN 绑定的 User-profile
- `LST RULEBINDING:USERPROFILENAME="up_test";` 查询 User-profile 绑定的 Rule（策略类型应为 SRV_TRIGGER）
- `LST RULE:RULENAME="rule_test1";` 查询 Rule 配置（流过滤器名称、全局优先级）

**步骤5**：收集信息寻求技术支持（OM Portal 用户跟踪任务 + EXP MML 导出 + 联系华为技术支持）。

> 来源：`调测业务触发RADIUS功能_32050952.md`（"操作步骤"及命令返回示例）

### 6.3 告警参考

| 告警ID | 告警名称 | 触发条件 | 影响 |
|--------|---------|---------|------|
| ALM-81020 | RADIUS 计费服务器无响应 | Radius 计费服务器超时无响应 | 用户计费流程异常，可能触发 Bypass 策略 |
| ALM-100197 | RADIUS 鉴权服务器无响应 | Radius 鉴权服务器超时无响应 | 用户鉴权流程异常，可能触发 Bypass 策略 |

> 来源：`WSFD-011306 Radius功能参考信息_15542176.md`（"告警"章节）

### 6.4 测量指标

| 指标 | 说明 |
|------|------|
| Gi 接口 AAA 计费性能测量 | Gi/SGi 接口 Radius 计费流程性能 |
| AAA 鉴权流程 | Gi/SGi 接口 Radius 鉴权流程性能 |
| AAA 鉴权会话资源 | Radius 鉴权会话资源占用 |

> 来源：`WSFD-011306 Radius功能参考信息_15542176.md`（"测量指标"章节）

### 6.5 软参

| 软参 | 说明 |
|------|------|
| BYTE95 | 控制是否对鉴权响应消息携带的 Message-Authenticator 属性进行验证 |
| BIT662 | 控制基于消息的负荷分担模式下，UNC 发送 Accounting-Interim-Update 和 Accounting-Stop 消息时，首次发送是否固定向发送 Accounting-Start 消息的 Radius 计费服务器发消息 |
| BIT1915 | 用于控制用户激活 AAA 下发地址池 |
| DWORD1018 BIT6 | SMF/PGW-C/GGSN 控制 Access Request 消息 framed-ipv6-prefix 填写方式 |
| DWORD1038 BIT23 | 控制 Access Request 消息中 framed-interface-id 填写方式 |
| DWORD1038 BIT27 | 控制 UNC 是否处理 Access Accept 和 CoA Request 消息中的特定信元 |
| DWORD1039 BIT2 0-1 | 控制 UNC 给 AAA 发送的 Access Request 消息中是否携带 GprsQosProfile 信元 |
| DWORD1039 BIT5 0-1 | 控制在透明不鉴权且 APNBYTE10 不为 1 场景下，UNC 发给 AAA 的 Accounting Request Start 消息中 user-name 信元的填写方式 |

> 来源：`WSFD-011306 Radius功能参考信息_15542176.md`（"软参"章节）

### 6.6 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| APN 用户激活失败 | 该 APN 未配置 Client IP（ADD APNRDSCLIENTIP） | 补配 ADD APNRDSCLIENTIP（AUTHENTICATION + ACCOUNTING 都需配） |
| TST AAA 检测无响应 | UNC 到 AAA Server 链路不通 | NGPING 指定 SRCIPV4ADDR=Gi接口IP；检查路由/VPN/可靠性组网 |
| TST AAA 检测无响应 | AAA Server IP/端口/Key 不一致 | LST RDSSVRGRP 核对配置；与 AAA Server 网元配置比对 |
| RADIUS 鉴权/计费服务器无响应告警 | AAA Server 故障或网络中断 | 参考 ALM-100197 / ALM-81020；必要时 SET FHBYPASS 紧急放通（需客户认可） |
| 业务触发 RADIUS 不生效 | APN 已有用户（策略组合绑定 APN 后对已有用户无效） | 用户重新激活；或只对后续激活用户生效 |
| 业务触发 RADIUS 不生效 | Rule 的 FlowFilter 与 UDG 不一致 | LST RULE 核对流过滤器名称；UDG 侧同步配置 |
| Bypass 放通后用户 IP 异常 | 放通时用户地址分配方式是 Radius 分配（不允许） | 放通场景需确保地址分配方式非 Radius 分配 |
| AAA 下发策略不生效 | AAA 下发的是动态规则（不支持） | AAA 下发仅支持预定义规则（Charging-rule-base-name/charging-rule-name 对应本地 User-profile/Rule） |
| 响应消息端口检查失效 | 组网有防火墙/NAT 或 AAA 修改 IP/Port | SET RDSRSPADDRCHK 关闭端口检查 |
| 集中去活引发信令激增 | AAA 故障后 HOLDINGTIME 超时大批量去活 | 配置 ADJUSTRANGE 使去活时间随机延迟 |

> 来源：综合 `调测到AAA Server的数据_32027181.md`、`调测业务触发RADIUS功能_32050952.md`、`实现原理_31922672.md`、`配置RADIUS功能_32909765.md`

---

## 7. 参考信息

### 7.1 与其他特性的关系

| 关联特性 | 特性ID | 关系说明 |
|---------|--------|---------|
| **Radius 鉴权接入（上游鉴权决策）** | WSFD-011305（UNC） | AUTHMODE 决策：透明接入不鉴权（不需本特性鉴权）；透明鉴权接入/非透明接入/本地鉴权接入**必配本特性** Radius 鉴权 |
| **Radius 抄送功能（下游）** | WSFD-011307（UNC） | 本特性发送给 AAA Server 的同时，抄送给其他需要获取用户信息的服务器（WAP GW 等） |
| **AAA 负荷分担** | WSFD-011308（UNC） | 本特性 Radius-server Group 的"负荷分担模式"（MODE=ROUND_ROBIN）具体由 WSFD-011308 承载 |
| **地址分配方式（Radius 分配协同）** | WSFD-010502（UNC） | Radius 分配方式下，本特性承载 Access-Accept 携带的用户 IP/IPv4 池名/IPv6 池名 |
| **鉴权功能（基础鉴权）** | WSFD-010301（UNC） | 本域基础鉴权特性（5G AKA/EAP AKA'），与 Radius 鉴权（外网 AAA）互补 |
| **终端二次鉴权（企业 AAA）** | WSFD-108007（UNC） | 企业 AAA 场景的终端二次鉴权，依赖本特性的 Radius 承载 |
| **SA-Basic（业务触发 RADIUS 依赖）** | GWFD-110101（UDG） | 业务触发 RADIUS 场景依赖 UDG 业务感知提供 L3/4 过滤器与规则识别 |
| **会话管理（宿主）** | WSFD-010501（UNC） | PDU 会话建立的宿主特性，Radius 鉴权/计费挂在会话激活/去活流程上 |

### 7.2 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/特性概述_31467848.md` | 适用NF（GGSN/PGW-C/SMF + AAA Server）、定义（Radius 鉴权/计费/策略控制三大功能）、客户价值、应用场景（接入鉴权/Radius地址分配/抄送/负荷分担四类）、可获得性（UNC 20.3.0+，无License）、与其他特性交互（无）、对系统影响（按用户单独处理）、应用限制（无）、特性规格（整机最大4000 AAA Server）、遵循标准（3GPP 23.214/29.244/23.060/29.060/29.061 + RFC 2865）、发布历史（v01 20.3.0）、Radius 业务激活/去活流程图 |
| 2 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/实现原理_31922672.md` | APN/AAA Server 映射、AAA Server 工作模式（主备1+1/按优先级选主/负荷分担轮选）、端口可配、3GPP扩展属性、域名剥离、重发超时可配；Radius 鉴权功能点（地址分配/Message-Authenticator/MSISDN转发/PAP-CHAP-MSCHAP三方式及支持用户类型表/AAA Bypass三档策略/响应端口检查）；Radius 计费功能点（非实时/准实时/计费响应开关/Account ON-OFF/利用鉴权服务器计费/多UPF主送）；Radius 策略控制功能点（用户业务属性/AAA下发策略/RAT触发/POD去活/业务触发Radius两种方式）；激活/去活业务流程图 |
| 3 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/WSFD-011306 Radius功能参考信息_15542176.md` | MML命令清单（40+条：ADD RDSSVRGRP/RDSSVR/APNRDSSVRGRP/APNRDSCLIENTIP、SET APNAUTHATTR/APNRDSACCTCTRL/APNRADIUSATTR/RDSACCTREQVSA/RDSAUTHREQVSA/RDSRSPADDRCHK/FHBYPASS、ADD UPLIST4RDS、L3VPN/VPN/Gi接口/GRE/静态路由/ACL/IPSec 全套组网基础命令、ADD RULE/USERPROFILE/RULEBINDING 等业务策略命令、TST AAA/DSP ROUTE/LST 等调测命令）、告警（ALM-81020 计费无响应、ALM-100197 鉴权无响应）、软参（8个：BYTE95/BIT662/BIT1915/DWORD1018 BIT6/DWORD1038 BIT23/BIT27/DWORD1039 BIT2/BIT5）、测量指标（3个：Gi接口AAA计费性能/AAA鉴权流程/AAA鉴权会话资源） |
| 4 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/激活RADIUS功能/配置RADIUS功能_32909765.md` | 配置RADIUS功能完整9步操作步骤、整体配置/鉴权AAA服务器/计费AAA服务器三张参数表、ADD RDSSVRGRP（MODE/ACCTTIMEOUT/AUTHTIMEOUT/ACCTSVRTOUT/AUTHSVRDTIME等10+超时重发参数）、ADD RDSSVR（SERVERTYPE=AUTHENTICATION/ACCOUNTING、PORT=1812/1813、PRIFLAG、PRIORITY、VPNINSTANCE、CIPHERKEY）、SET RDSACCTREQVSA、ADD APNRDSCLIENTIP（AUTHORACCT=AUTHENTICATION/ACCOUNTING必配，否则激活失败）、ADD APNRDSSVRGRP、SET APNRDSACCTCTRL（TIMETHRESHOLD/VOLUMETHRESHOLD/SUPPORTACCTRSP/SRVTRIGGER/BUFFERTIMEVALUE）、SET APNRADIUSATTR（DOMAINNAMEACT/DOMAINNAMEPOS）、SET APNAUTHATTR（DISCONNECT=ENABLE PoD开关）、SET FHBYPASS（故障紧急优先级最高需客户书面认可）、完整MML脚本（主备模式 isprg） |
| 5 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/激活RADIUS功能/配置业务触发RADIUS功能_33000859.md` | 业务触发RADIUS功能独立子场景、SET APNRDSACCTCTRL SRVTRIGGER=ENABLE、ADD RULE POLICYTYPE=SRV_TRIGGER、ADD USERPROFILE UPTYPE=PCC、ADD RULEBINDING/USRPROFGROUP/UPBINDUPG/APNUSRPROFGROUP 业务策略组合、C-U一致性（FlowFilter/Rule需与UPF/PGW-U一致）、APN既有用户无效只对后续激活用户生效、www.huawei.com 触发场景完整MML脚本 |
| 6 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/激活RADIUS功能/配置到AAA Server的数据（单平面+静态路由+BFD组网）_32044985.md` | 单平面+静态路由+BFD组网场景（带外组网：数据报文与Radius信令不同出接口不同VPN）、ADD L3VPNINST/VPNINSTAF（vpn_pdn VRFRD=100:1、vpn_aaa VRFRD=200:1）、ADD VPNINST、ADD LOGICIP/LOGICINF（giif1/0/0=10.8.20.1鉴权、giif1/0/1=10.8.20.2计费）、ADD RDSSVRGRP MODE=ROUND_ROBIN、ADD RDSSVR VPNINSTANCE=vpn_aaa、ADD APN HASVPN+VPNINSTANCE=vpn_pdn、ADD APNRDSCLIENTIP INTFNAME、ADD APNRDSSVRGRP、完整带外组网MML脚本 |
| 7 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/激活RADIUS功能/配置到AAA Server的数据（双平面+OSPF动态路由+BFD组网 ）_31879931.md` | 双平面+OSPF动态路由+BFD组网变体（在单平面基础上增加 OSPF 动态路由配置） |
| 8 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/激活RADIUS功能/配置到AAA Server的数据（带内组网GRE VPN）_32723577.md` | 带内组网 GRE VPN 变体（Radius 信令与数据报文共用通道，通过 GRE 隧道隔离，ADD GRETUNNEL） |
| 9 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/激活RADIUS功能/配置到AAA Server的数据（带外组网GRE VPN）_32050904.md` | 带外组网 GRE VPN 变体（vpn_pdn+vpn_aaa+GRE 隧道，Radius 信令走独立通道通过 GRE 隔离） |
| 10 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/调测到AAA Server的数据_32027181.md` | 6步调测流程（TST AAA 探测、NGPING 指定SRCIPV4ADDR=Gi接口IP+VPNNAME、LST RDSSVRGRP 核对IP/端口/Key一致性、路由/可靠性/VPN逐项调测、查ALM-100197/81020告警、EXP MML导出寻求支持） |
| 11 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能/调测业务触发RADIUS功能_32050952.md` | 5步业务触发调测流程（OM Portal Gi/SGi跟踪ACCT、测试终端apn-test接入、访问www.huawei.com查Radius计费消息、LST APNUSRPROFG/RULEBINDING/RULE 核对策略组合、收集信息）、LST命令返回示例（用户模板组/规则绑定/规则信息） |
| 12 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011306 Radius功能_14755851.md` | 特性根索引文件（仅标题导航，无实质内容） |

### 7.3 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| RADIUS | Remote Authentication Dial In User Service | AAA 协议（RFC 2865） |
| AAA | Authentication/Authorization/Accounting | 鉴权、授权、计费 |
| AAA Server | - | UNC 的 Radius 对端网元，完成用户鉴权和计费 |
| Radius-server Group | - | UNC 侧 Radius 服务器组织单位，每个 APN 绑定一个 |
| PRIFLAG | 主备用类型 | PRIMARY 主用 / SECONDARY 备用 |
| PRIORITY | 服务器优先级 | 按优先级选主模式生效 |
| AUTHORACCT | 鉴权或计费 | APNRDSCLIENTIP 参数：AUTHENTICATION/ACCOUNTING |
| SRVTRIGGER | 业务报文触发计费请求 | 业务触发 RADIUS 总开关 |
| SUPPORTACCTRSP | 等待计费开始响应 | ENABLE 等待（超时激活失败）/ DISABLE 不等待 |
| BUFFERTIMEVALUE | 业务报文延时时间 | 业务触发 RADIUS 等待响应时长 |
| DOMAINNAMEACT | 域名增加或剥离 | ADD_ENABLE_STRIP_DISABLE（同时开启需执行两次） |
| AAANORSPCTRL | AAA 鉴权服务器无响应处理 | DEACTIVE/HOLDINGTIME |
| HOLDINGTIME | 延时去活时长 | 取值 0~1440；0=放通，非 0=延时去活 |
| ADJUSTRANGE | 去活时间随机延迟范围 | 避免集中去活引发信令激增 |
| PoD | Packet of Disconnect | AAA Server 主动发起的去激活消息 |
| Account ON/OFF | - | UNC 整机重启场景通知 AAA 批量清除残留用户 |
| Framed-IP / Framed-Pool | Radius 属性 | Access-Accept 携带的用户 IP / 地址池名 |
| Charging-rule-base-name | - | AAA 下发策略，对应本地 User-profile |
| charging-rule-name | - | AAA 下发策略，对应本地 Rule |

---

## 8. 文档一致性说明（配置树 vs 产品文档 vs 关联特性）

> 配置树仅用于定位特性 ID，以下记录以产品文档实际内容为准时发现的差异与协同点，供 Stage 3 横向分析参考。

### 8.1 与配置树/文档清单的差异

| # | 维度 | 配置树/文档清单描述 | 产品文档实际内容 | 差异类型 |
|---|------|---------------------|-----------------|---------|
| 1 | 特性定位 | 文档清单标题："Radius服务器配置(透明鉴权/不透明接入时必配)" | 产品文档定义："UNC 与 RADIUS 服务器之间，通过 RADIUS 协议实现 RADIUS 鉴权、RADIUS 计费、RADIUS 策略控制" | 一致：清单与文档定位匹配 |
| 2 | 鉴权决策归属 | 文档清单暗示本特性决定鉴权 | **鉴权决策（AUTHMODE）实际在 WSFD-011305**；本特性是 Radius 协议承载与功能集 | 澄清：本特性不决策鉴权方式，仅承载 Radius 鉴权/计费/策略 |
| 3 | License要求 | 文档清单标注"[★核心]" | 产品文档明确声明"**本特性无需获得License许可**" | 差异：与同域★核心需License特性不同，本特性无License |
| 4 | 命令清单规模 | 文档清单暗示核心命令较少 | 参考信息列出 **40+ 条命令**（含 Radius 核心 + 组网基础 + 业务策略 + 调测） | 补全：命令清单规模远超预期，含 L3VPN/GRE/IPSec/ACL 全套组网基础命令 |
| 5 | 组网场景数 | 文档清单未细分 | 产品文档提供 **4 种到 AAA Server 的组网场景**（单平面+静态路由+BFD/双平面+OSPF+BFD/带内GRE VPN/带外GRE VPN） | 补全：组网场景需在 Stage 3 横向分析 |
| 6 | 业务触发子场景 | 文档清单未提及 | 产品文档提供**独立的业务触发 RADIUS 功能配置场景**（POLICYTYPE=SRV_TRIGGER） | 补全：业务触发是独立子场景，需 C-U 协同（UDG 侧 FlowFilter/Rule 一致） |

### 8.2 与 WSFD-011305（AUTHMODE 鉴权决策）的联动

| # | 维度 | WSFD-011305（鉴权决策） | WSFD-011306（Radius功能承载） | 联动关系 |
|---|------|------------------------|------------------------------|---------|
| 1 | 角色定位 | AUTHMODE 决策方：决定是否启用 Radius 鉴权 | Radius 协议承载方：承载鉴权/计费/策略控制 | **决策-承载分工**：011305 决策，011306 承载 |
| 2 | 透明接入 | 透明接入不鉴权 | 本特性鉴权功能不被触发 | 透明接入**不需本特性鉴权**（但可能仍需 Radius 计费） |
| 3 | 透明鉴权接入 | 透明鉴权接入需 Radius 鉴权 | **必配本特性** Radius 鉴权 | 强依赖 |
| 4 | 非透明接入 | 非透明接入需 Radius 鉴权 | **必配本特性** Radius 鉴权 | 强依赖 |
| 5 | 本地鉴权接入 | 本地鉴权接入需 Radius 鉴权 | **必配本特性** Radius 鉴权 | 强依赖 |
| 6 | 配置耦合点 | AUTHMODE 配置 | ADD APNRDSSVRGRP（APN↔Radius服务器组） | 配置树父子关系推断（Stage 3 验证） |

### 8.3 与 WSFD-011307（Radius 抄送）的关系

| # | 维度 | WSFD-011306（Radius功能） | WSFD-011307（Radius抄送） | 关系 |
|---|------|--------------------------|--------------------------|------|
| 1 | 消息流向 | UNC → AAA Server（主送） | UNC → AAA Server（主送）+ 其他服务器（抄送） | **抄送是主送的并行扩展** |
| 2 | 触发基础 | 本特性发送 Radius 鉴权/计费消息 | 在本特性发送消息的同时，抄送给其他需要获取用户信息的服务器（如 WAP GW） | 011307 依赖 011306 的消息发送基础 |
| 3 | 利用鉴权服务器计费场景 | 本特性支持"利用 Radius 鉴权服务器计费" | 部署计费抄送服务器时，UNC 将计费消息发给鉴权服务器同时抄送给计费抄送服务器 | 协同：本特性"利用鉴权服务器计费"与 011307 抄送功能可叠加 |

### 8.4 与 WSFD-010502（地址分配方式）的 Radius 分配协同

| # | 维度 | WSFD-011306（Radius功能承载） | WSFD-010502（Radius分配方式决策） | 协同关系 |
|---|------|------------------------------|----------------------------------|---------|
| 1 | 角色定位 | Radius 协议承载（Access-Request/Accept） | Radius 分配方式决策方（4种分配方式之一） | **承载-决策分工**：011306 承载，010502 决策采用 Radius 分配 |
| 2 | IP/池名来源 | Access-Accept 消息携带 | Radius 分配方式的 IP 来自 Access-Accept | 011306 是 010502 Radius 分配方式的承载管道 |
| 3 | Bypass 放通约束 | 放通时用户地址分配方式不能是 Radius 分配 | - | **反向约束**：若采用 Radius 分配方式，则不能使用 Bypass 放通 |
| 4 | BIT1915 软参 | 控制用户激活 AAA 下发地址池 | - | 软参层面的协同开关 |

### 8.5 与 GWFD-110101（SA-Basic）的 C-U 协同（业务触发场景）

| # | 维度 | WSFD-011306（UNC，业务触发 RADIUS） | GWFD-110101（UDG，SA-Basic） | 协同关系 |
|---|------|-------------------------------------|------------------------------|---------|
| 1 | 业务识别 | UNC 配置 ADD RULE POLICYTYPE=SRV_TRIGGER | UDG 进行 L3/4 业务识别（FlowFilter） | **C-U 协同**：UDG 识别业务，UNC 触发 Radius 消息 |
| 2 | 规则一致性 | ADD FLOWFILTER / ADD RULE 需与 UDG 一致 | UDG 侧 FlowFilter/Rule | **C-U 数据一致性硬约束**（配置业务触发 RADIUS 明确要求） |
| 3 | 文档原文 | "为了确保该功能生效，请在UDG上配置相同的业务规则，并绑定该业务触发使用的流过滤器" | - | 文档明确引用 UDG 内容感知章节 |

---

## 附录 A：Radius 服务器配置速查表

| 配置维度 | 命令 | 关键参数 | 默认值/样例 |
|---------|------|---------|------------|
| 服务器组 | ADD RDSSVRGRP | RDSSVRGRPNAME, MODE | isprg, MASTER_SLAVE/ROUND_ROBIN |
| 鉴权服务器模板 | ADD RDSSVR | SERVERTYPE=AUTHENTICATION, PORT | 1812 |
| 计费服务器模板 | ADD RDSSVR | SERVERTYPE=ACCOUNTING, PORT | 1813 |
| 主备标识 | ADD RDSSVR | PRIFLAG | PRIMARY/SECONDARY |
| 优先级（按优先级选主） | ADD RDSSVR | PRIORITY | 1/2/3... |
| VPN 绑定 | ADD RDSSVR | VPNINSTANCE | vpn_aaa |
| 密钥 | ADD RDSSVR | CIPHERKEY/CIPHERKEYCNFM | 鉴权与计费可不同 |
| 超时（计费请求） | ADD RDSSVRGRP | ACCTTIMEOUT | 10 秒 |
| 重发（计费请求） | ADD RDSSVRGRP | ACCTRETRANSMIT | 5 次 |
| 超时（鉴权请求） | ADD RDSSVRGRP | AUTHTIMEOUT | 10 秒 |
| 重发（鉴权请求） | ADD RDSSVRGRP | AUTHRETRANSMIT | 5 次 |
| 服务器 Down 超时 | ADD RDSSVRGRP | ACCTSVRTOUT/AUTHSVRTOUT | 12 秒 |
| 服务器 Down 保持 | ADD RDSSVRGRP | ACCTSVRDTIME/AUTHSVRDTIME | 180 秒 |
| APN 绑定服务器组 | ADD APNRDSSVRGRP | APN, RDSSVRGRPNAME | apn-test, isprg |
| APN Client IP（鉴权） | ADD APNRDSCLIENTIP | AUTHORACCT=AUTHENTICATION, INTFNAME | giif1/0/0 |
| APN Client IP（计费） | ADD APNRDSCLIENTIP | AUTHORACCT=ACCOUNTING, INTFNAME | giif1/0/1 |
| 计费阈值（时间） | SET APNRDSACCTCTRL | TIMETHRESHOLD | 30 分 |
| 计费阈值（流量） | SET APNRDSACCTCTRL | VOLUMETHRESHOLD | 20 千字节 |
| 等待计费响应 | SET APNRDSACCTCTRL | SUPPORTACCTRSP | ENABLE/DISABLE |
| 业务触发开关 | SET APNRDSACCTCTRL | SRVTRIGGER | ENABLE/DISABLE |
| PoD 开关 | SET APNAUTHATTR | DISCONNECT | ENABLE |
| 域名处理 | SET APNRADIUSATTR | DOMAINNAMEACT, DOMAINNAMEPOS | ADD_ENABLE_STRIP_DISABLED, SUFFIX |
| Bypass 紧急放通 | SET FHBYPASS | HOLDINGTIME, ADJUSTRANGE | 0~1440（需客户认可） |
| 响应端口检查 | SET RDSRSPADDRCHK | - | 默认开启（有 NAT/防火墙时关闭） |

---

## 附录 B：Radius 鉴权方式与用户类型对照速查

| UE 携带信元 | 鉴权方式 | 支持的用户类型 |
|------------|---------|---------------|
| PCO | PAP | 普通IP、PPP、L2TP |
| PCO | CHAP | 普通IP、PPP、L2TP |
| PCO | MS-CHAP（v1/v2） | 普通IP |
| ePCO | PAP | L2TP |
| ePCO | CHAP | L2TP |

---

**文档版本**：v1.0（Stage 2 知识提取，基于 12 篇产品文档）
**提取时间**：2026-06-22
**关键发现**：见返回报告
