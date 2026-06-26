# WSFD-011307 支持Radius抄送功能 知识文档

> 聚焦 APN 业务域鉴权计费场景的 UNC（GGSN/PGW-C/SMF）侧 Radius 计费消息抄送（Carbon-copy）能力
> 上游承载特性 WSFD-011306（Radius 功能，提供服务器组/服务器模板与 APN 绑定基础设施），同域并列特性 WSFD-011305（Radius 鉴权接入，鉴权决策方）

---

## 0. 元数据（三层图谱Schema字段）

| 字段 | 取值 |
|------|------|
| feature_id | WSFD-011307 |
| feature_name | 支持Radius抄送功能 |
| feature_group | 鉴权计费 |
| parent_feature_id | WSFD-011306（Radius功能，配置承载父节点；本特性复用 011306 的 RDSSVRGRP/RDSSVR/APNRDSSVRGRP 配置对象，并扩展 PRIFLAG=CARBON_COPY 服务器角色） |
| applicable_nf_map | `{"UNC": ["GGSN", "PGW-C", "SMF"]}` |
| variant_dimensions | ["抄送服务器角色(PRIFLAG=CARBON_COPY)", "抄送消息类型(Accounting Start/Interim/Stop 计费消息拷贝)", "按用户所锚定PGW-U/UPF匹配抄送服务器(ADD UPLIST4RDS+ADD RDSSVR绑定List)", "抄送服务器数量(单组最多64个)", "VPN组网方式(单平面/GRE VPN等，同011306)", "抄送服务器响应行为(不回复消息给UNC)"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-01, EV-FK-02, EV-FK-03, EV-FK-04, EV-FK-05] |
| license_required | 无（本特性无需License） |

---

## 1. 概述

### 1.1 特性定义（是什么）

RADIUS 抄送功能（RADIUS Carbon-copy）主要用于将 AAA **计费消息**在发送给 AAA Server 的同时，**抄送给其他需要获取用户信息的服务器**（抄送服务器 / Carbon-copy Server，如 WAP GW 等增值业务服务器）。

> 抄送的概念类似于 Email 中的"抄送"：UNC 发送消息给 AAA Server 的同时，将这些消息转发给其他希望获取用户信息的服务器（原文）。

> 来源：`特性概述_33741340.md`（"定义"章节）、`实现原理_33761637.md`（"相关概念"章节）

### 1.2 适用NF（UDG/UNC网元）

| 涉及NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| GGSN | 控制面（UNC，2/3G） | UNC 20.3.0及后续版本 | 将发送给 AAA Server 的计费消息拷贝一份发给抄送服务器 |
| PGW-C | 控制面（UNC，4G） | UNC 20.3.0及后续版本 | 将发送给 AAA Server 的计费消息拷贝一份发给抄送服务器 |
| SMF | 控制面（UNC，5G） | UNC 20.3.0及后续版本 | 将发送给 AAA Server 的计费消息拷贝一份发给抄送服务器 |
| AAA Server | 外部对端网元 | 无特殊需求 | 实现对用户的计费（主送方，不被本特性改变） |
| Carbon-copy Server（抄送服务器） | 外部对端网元（增值业务服务器，如 WAP GW） | 无特殊需求 | 接收 UNC 抄送的 AAA 计费消息；**不回复消息给 UNC** |

> 来源：`特性概述_33741340.md`（"可获得性/涉及NF"章节）、`调测支持RADIUS抄送功能_33769358.md`（"操作场景"明确"抄送服务器不回复消息给 UNC"）

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|---------|---------|---------|
| 01 | 20.3.0 | 首次发布，支持 RADIUS 抄送功能 |

> 来源：`特性概述_33741340.md`（"发布历史"章节）

### 1.4 License

**本特性无需获得 License 许可即可获得该特性的服务**（文档明确声明）。

> 来源：`特性概述_33741340.md`（"可获得性/License 支持"章节）

### 1.5 前置条件与依赖

| 前置条件 | 说明 |
|---------|------|
| **激活 RADIUS 功能（强依赖）** | **必须**先完成 [激活 RADIUS 功能]（WSFD-011306），即先建好 Radius Server Group、AAA 计费服务器、APN 绑定服务器组的基础配置（原文明确） |
| **调测到 AAA Server 的数据（强依赖）** | 必须先完成 [调测到 AAA Server 的数据]（WSFD-011306），确保 UNC 到主送 AAA Server 的链路连通（调测本特性的前置） |
| APN 已配置 | 必须通过 `ADD APN` 完成增加 APN 配置 |
| VPN 实例（VPN 组网场景） | 若运营商规划采用 VPN 组网，则操作员在执行本操作前应已创建相应的 VPN 实例（ADD VPNINST） |
| 抄送服务器互通 | 抄送服务器侧已完成配置并配置到 UNC 的回程路由；UNC 到抄送服务器链路连通 |

> 来源：`激活支持RADIUS抄送功能_33769357.md`（"必备事项/前提条件"）、`调测支持RADIUS抄送功能_33769358.md`（"必备事项/前提条件"）

### 1.6 与其他特性的交互

**特性概述明确声明"本特性不涉及与其他特性的交互"**（原文）。但功能语义上存在强关联（详见 §8 一致性分析）：

| 交互类型 | 相关特性 | 交互说明 |
|---------|---------|---------|
| **配置承载父节点** | WSFD-011306 Radius功能（UNC） | 本特性**复用** 011306 的配置对象（RDSSVRGRP/RDSSVR/APNRDSSVRGRP/UPLIST4RDS），并通过在 ADD RDSSVR 中扩展 `PRIFLAG=CARBON_COPY` 角色实现抄送服务器；激活本特性前**必须先激活 RADIUS 功能**（011306） |
| **鉴权决策上游** | WSFD-011305 Radius鉴权接入（UNC） | AUTHMODE 决策是否启用 Radius 鉴权；本特性只抄送**计费**消息，与鉴权决策无直接耦合 |
| **UP 主送协同** | （UDG 侧，PGW-U/UPF） | 本特性支持"根据用户所锚定的 PGW-U/UPF 给特定抄送服务器抄送"，需通过 ADD UPLIST4RDS + ADD RDSSVR 绑定 UP List 实现 |

> 来源：`特性概述_33741340.md`（"与其他特性的交互"章节）、`激活支持RADIUS抄送功能_33769357.md`（"前提条件"明确依赖 011306）

### 1.7 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | 替换现网 AAA Server 转发消息的方式，**降低对 AAA Server 的性能要求**；同步 AAA 信息到增值服务器，**提升增值服务能力** |
| 用户 | 用户不感知该特性 |

> 来源：`特性概述_33741340.md`（"客户价值"章节）

### 1.8 应用场景

抄送服务器通过获取 AAA 消息中携带的 **IP 地址、APN 和 MSISDN**，及时了解用户的在线状况。典型部署场景：

- 运营商部署分组交换网，在将 RADIUS 消息发往计费 AAA Server 时，需要将用户信息同时发给多个 AAA 抄送服务器（如 WAP GW 等增值业务服务器）
- 避免由 AAA Server 转发 AAA 消息（会影响 AAA Server 处理性能），改由 UNC 直接抄送

> 来源：`特性概述_33741340.md`（"应用场景"章节）、`激活支持RADIUS抄送功能_33769357.md`（"操作场景"章节）

### 1.9 对系统的影响

增加 RADIUS 抄送服务器对**系统信令处理能力有消耗**，增加的 RADIUS 抄送服务器越多，对系统信令处理能力的消耗越大。

> **注意**：用户在线时删除抄送服务器配置，可能造成抄送消息失败（文档明确警告）。

> 来源：`特性概述_33741340.md`（"对系统的影响"章节）

### 1.10 应用限制

**本特性无应用限制**（文档明确声明）。

### 1.11 特性规格

| 规格名称 | 规格指标 |
|---------|---------|
| 每个 RADIUS Server Group 最多配置计费抄送服务器个数 | **64** |

> 来源：`特性概述_33741340.md`（"特性规格"章节）

### 1.12 计费与话单

**本特性不涉及计费与话单**（本特性是 Radius 计费消息的"拷贝转发"，不直接产生本地话单；主送计费由 WSFD-011306 承载）。

### 1.13 遵循标准

| 标准类别 | 标准编号 | 标准名称 |
|---------|---------|---------|
| 3GPP | 23.214 | Architecture enhancements for control and user plane separation of EPC nodes |
| 3GPP | 29.244 | Interface between the Control Plane and the User Plane of EPC Nodes |
| IETF | 2865 | Remote Authentication Dial In User Service (RADIUS) |

> 来源：`特性概述_33741340.md`（"遵循标准"章节）

---

## 2. 核心概念

### 2.1 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| RADIUS Carbon-copy | RADIUS 抄送 | 将 AAA 计费消息在发送给 AAA Server 的同时，抄送给其他需要获取用户信息的服务器 |
| Carbon-copy Server | 抄送服务器 | 接收 UNC 抄送 AAA 计费消息的外部服务器（增值业务服务器，如 WAP GW）；**不回复消息给 UNC** |
| CARBON_COPY | 抄送角色标识 | ADD RDSSVR 命令中 PRIFLAG 参数的第三个取值（与 PRIMARY 主用、SECONDARY 备用并列），用于标识一个服务器为抄送服务器 |
| 抄送消息拷贝 | Carbon-copy Message Copy | UNC 发往计费服务器的 Accounting Start/Interim/Stop 消息的拷贝，分别发给各 Carbon-copy Server |
| UP List | PGW-U/UPF 列表 | 通过 ADD UPLIST4RDS 配置，用于按用户所锚定 PGW-U/UPF 匹配抄送服务器 |

> 来源：`特性概述_33741340.md`（"定义"）、`实现原理_33761637.md`（"相关概念"）、`激活支持RADIUS抄送功能_33769357.md`（表2 PRIFLAG=CARBON_COPY）

### 2.2 对象模型

本特性**不引入新的配置对象**，而是**复用 WSFD-011306 的 Radius 服务器组与 APN 绑定体系**，通过在 ADD RDSSVR 命令的 PRIFLAG 参数中**扩展第三个取值 CARBON_COPY** 来标识抄送服务器：

```
┌─────────────────────────────────────────────────────────────────┐
│ 复用 WSFD-011306 的 Radius-server Group（ADD RDSSVRGRP）          │
│                                                                 │
│   ┌──────────────────┐                                          │
│   │ Radius-server    │ MODE=MASTER_SLAVE / ROUND_ROBIN          │
│   │ Group            │ （与 011306 共用同一个组）                 │
│   │ (isprg)          │                                          │
│   └────────┬─────────┘                                          │
│            │ 包含（同一组内可同时存在三类服务器角色）              │
│            ├── SERVERTYPE=AUTHENTICATION (鉴权, PORT=1812)       │
│            │     ├── PRIFLAG=PRIMARY   主用                      │
│            │     └── PRIFLAG=SECONDARY 备用                      │
│            └── SERVERTYPE=ACCOUNTING (计费, PORT=1813/1819)      │
│                  ├── PRIFLAG=PRIMARY       主用计费（主送）       │
│                  ├── PRIFLAG=SECONDARY     备用计费              │
│                  └── PRIFLAG=CARBON_COPY   ★抄送服务器（本特性）  │
│                        └── 最多 64 个/组                          │
└────────────┼────────────────────────────────────────────────────┘
             │ ADD APNRDSSVRGRP (APN↔服务器组绑定，与 011306 共用)
             ▼
┌─────────────────────────────────────────────────────────────────┐
│ APN 侧绑定体系（复用 011306）                                     │
│                                                                 │
│   ADD APN (apn-test)                                            │
│     └── ADD APNRDSSVRGRP  → 绑定 RDSSVRGRPNAME=isprg            │
│           （该组内同时含主送 AAA 计费服务器 + Carbon-copy 服务器） │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ 按 PGW-U/UPF 匹配抄送服务器（可选增强，复用 011306 的 UPLIST4RDS）│
│                                                                 │
│   ADD UPLIST4RDS → 配置 PGW-U/UPF List                          │
│        ↓                                                        │
│   ADD RDSSVR (PRIFLAG=CARBON_COPY) → 抄送服务器绑定 PGW-U/UPF List│
│        ↓                                                        │
│   UNC 查用户上下文中 PGW-U/UPF Host → 按 Host 匹配抄送服务器      │
│        ↓                                                        │
│   将计费消息拷贝发给匹配到的 Carbon-copy Server1/Server2/...      │
└─────────────────────────────────────────────────────────────────┘
```

### 2.3 在鉴权计费场景的角色

本特性在 APN 业务域鉴权计费场景中扮演"Radius 计费消息旁路抄送"的角色，是 WSFD-011306（Radius 功能承载）的**并行扩展能力**（不是 011306 的子能力，而是与之并列、共享配置对象的独立特性，详见 §8.3）：

```
[WSFD-011306 Radius功能] 主送计费消息
   ├── UNC → AAA Server（主送计费，Accounting Start/Interim/Stop）
   │
   └──→ [WSFD-011307 Radius 抄送] ★本特性
          └── UNC → Carbon-copy Server1/Server2/...（拷贝同一份计费消息）
                ├── 不回复消息给 UNC
                ├── 抄送服务器通过消息中 IP/APN/MSISDN 了解用户在线状况
                └── 支持按用户所锚定 PGW-U/UPF 匹配抄送服务器
```

具体角色：

1. **计费消息旁路抄送**：UNC 在向 AAA 计费服务器发送 Accounting Start/Interim/Stop 消息的同时，将消息拷贝发给一组抄送服务器
2. **卸载 AAA Server 转发负担**：替换"由 AAA Server 转发 AAA 消息给增值服务器"的旧模式，避免影响 AAA Server 处理性能
3. **增值信息同步**：抄送服务器通过 AAA 消息中的 IP/APN/MSISDN 同步获取用户在线状况，支撑增值服务
4. **按 UP 匹配（可选）**：支持根据用户所锚定的 PGW-U/UPF 给特定的抄送服务器抄送，实现多 UPF 场景下的精细化抄送路由

---

## 3. 原理与流程

### 3.1 基本原理

**未启用 RADIUS 抄送功能时**：由 AAA Server 转发 AAA 消息给增值服务器，会影响 AAA Server 的处理性能（原文图1所示）。

**启用 RADIUS 抄送功能时**：由 UNC 直接发送 AAA 消息拷贝给抄送服务器，**不影响 AAA Server 的处理能力**（原文图2所示）。

> 来源：`特性概述_33741340.md`（"原理概述"章节）、`实现原理_33761637.md`（"原理概述"章节）

### 3.2 UNC 支持的抄送功能

| 功能点 | 说明 |
|-------|------|
| **按 PGW-U/UPF 匹配抄送服务器** | UNC 根据用户所锚定的 PGW-U/UPF 给特定的抄送服务器抄送 AAA 消息 |
| **UP List 绑定抄送服务器** | 通过 `ADD UPLIST4RDS` 配置 PGW-U/UPF List，通过 `ADD RDSSVR`（PRIFLAG=CARBON_COPY）配置抄送服务器绑定 PGW-U/UPF List，实现将多个 PGW-U/UPF Host 绑定到抄送服务器上 |
| **基于用户上下文查找** | 当 UNC 给 AAA Server 发计费消息时，会查找用户上下文中记录的用户当前所在 PGW-U/UPF Host，根据 Host 匹配抄送服务器，然后将计费消息抄送给该服务器 |
| **抄送消息类型** | Accounting Start（开始计费）、Accounting Interim-Update（更新计费）、Accounting Stop（结束计费）三类计费消息均抄送 |
| **抄送服务器响应行为** | 抄送服务器**不回复消息给 UNC**（与主送 AAA Server 不同，主送 AAA Server 会回应 Accounting Response） |

> 来源：`实现原理_33761637.md`（"UNC 支持如下功能"）、`调测支持RADIUS抄送功能_33769358.md`（"操作场景"明确不回复）

### 3.3 业务流程（17 步，抄送 Start/Interim/Stop）

RADIUS 抄送功能的业务流程覆盖用户激活、在线更新、去激活三个阶段的计费消息抄送：

```
【激活阶段：抄送 Start】
1. UE 给 UNC 发送 PDP 激活请求
2. UNC 根据配置获取鉴权服务器 IP/端口，给鉴权服务器发送鉴权请求
3. 鉴权服务器回应确认消息
4. 鉴权成功后，UNC 根据配置获取计费服务器 IP/端口，给计费服务器发送开始计费请求（Start）
5. UNC 根据用户当前所在的 PGW-U/UPF host 匹配抄送服务器 ★
6. UNC 将发送给计费服务器的开始计费请求拷贝，分别发给 Carbon-copy Server1、Carbon-copy Server2 ★
7. 计费服务器回应确认消息
8. UNC 向 UE 回应激活成功消息

【在线更新阶段：抄送 Interim-Update】
9. UNC 向计费服务器发起更新请求（Interim-Update）
10. UNC 根据用户当前所在的 PGW-U/UPF host 匹配抄送服务器 ★
11. UNC 根据配置判断，需要分别给 Carbon-copy Server1、Carbon-copy Server2 发送 Interim-Update 消息 ★
12. 计费服务器回应更新确认消息

【去激活阶段：抄送 Stop】
13. UE 给 UNC 发送 PDP 去激活请求，并得到激活响应
14. 去激活成功后，UNC 根据配置获取计费服务器 IP/端口，给计费服务器发送结束计费请求（Stop）
15. UNC 根据用户当前所在的 PGW-U/UPF host 匹配抄送服务器 ★
16. UNC 将发送给计费服务器的结束计费请求拷贝，分别发给 Carbon-copy Server1、Carbon-copy Server2 ★
17. 计费服务器回应确认消息
```

**流程要点**：

- 主送（UNC → AAA 计费服务器）与抄送（UNC → Carbon-copy Server）**并行发生**，抄送是主送的拷贝
- 三类计费消息（Start / Interim-Update / Stop）均触发抄送流程
- 每次抄送前都重新根据用户当前 PGW-U/UPF host 匹配抄送服务器（支持用户移动性场景下的抄送路由更新）
- 抄送服务器**不回应**任何确认消息给 UNC（步骤中无 Carbon-copy Server 回应环节）

> 来源：`实现原理_33761637.md`（"业务流程"图3，17 步原文）

---

## 4. 配置规则

### 4.1 激活步骤（配置 RADIUS 抄送功能，6 步主流程）

```
步骤1：配置 AAA 服务器组（复用 011306 命令）
  └── ADD RDSSVRGRP
        ├── RDSSVRGRPNAME=isprg
        └── MODE=MASTER_SLAVE / ROUND_ROBIN

步骤2：创建 VPN 实例（VPN 组网场景，复用 011306）
  └── ADD VPNINST
        └── VPNINSTANCE=vpntest

步骤3（可选）：配置 UP 列表（按 PGW-U/UPF 匹配抄送服务器）
  └── ADD UPLIST4RDS
        ※ 用于将多个 PGW-U/UPF Host 绑定到抄送服务器

步骤4：配置 AAA 计费服务器 + 抄送服务器（关键步骤）
  └── ADD RDSSVR （可执行多次，配置多个服务器）
        ├── 主用计费服务器：  PRIFLAG=PRIMARY
        ├── 备用计费服务器：  PRIFLAG=SECONDARY
        └── ★抄送服务器：     PRIFLAG=CARBON_COPY （最多 64 个/组）

步骤5：配置 APN
  └── ADD APN
        └── APN=apn-test

步骤6：配置 APN 下绑定 AAA 服务器组（与 011306 共用绑定）
  └── ADD APNRDSSVRGRP
        ├── APN=apn-test
        └── RDSSVRGRPNAME=isprg（该组内同时含主送 + 抄送服务器）
```

> 来源：`激活支持RADIUS抄送功能_33769357.md`（"操作步骤"6 步）

### 4.2 MML命令清单

#### 4.2.1 本特性核心命令（复用 011306 命令集，无新增命令）

| 命令 | 用途 | 关键参数（本特性关注点） |
|------|------|-------------------------|
| **ADD RDSSVRGRP** | 增加 Radius 服务器组（与 011306 共用） | RDSSVRGRPNAME, MODE |
| **ADD RDSSVR** | 增加 RADIUS 服务器（★本特性核心命令） | RDSSVRGRPNAME, SERVERTYPE=ACCOUNTING, IPVERSION, SERVERIPV4, PORT, VPNINSTANCE, CIPHERKEY, **PRIFLAG=CARBON_COPY**（抄送角色）/ PRIMARY / SECONDARY |
| **ADD UPLIST4RDS** | 向 RADIUS 服务器使用的 UP 列表中增加 UP（按 PGW-U/UPF 匹配抄送服务器） | UP List 配置 |
| **ADD APNRDSSVRGRP** | 设置 APN Radius 服务器组（与 011306 共用绑定） | APN, RDSSVRGRPNAME |
| ADD APN | 增加 APN 配置 | APN |
| ADD VPNINST | 增加 VPN 实例（VPN 组网场景） | VPNINSTANCE |
| **LST APNRDSSVRGRP** | 查询 APN Radius 服务器组（调测用） | APN |
| **LST RDSSVR** | 查询 RADIUS 服务器（调测用，核对抄送服务器配置） | RDSSVRGRPNAME |
| EXP MML | 导出 MML 配置文件（故障收集） | - |

> 来源：`WSFD-011307 支持Radius抄送功能参考信息_33769359.md`（"命令"章节，完整命令清单）

#### 4.2.2 命令清单说明

本特性**未引入任何新命令**，全部复用 WSFD-011306 的命令集。核心扩展点在于 `ADD RDSSVR` 命令的 `PRIFLAG` 参数**新增第三个取值 `CARBON_COPY`**（011306 文档中仅描述 PRIMARY/SECONDARY 两种）。

> 来源：`WSFD-011307 支持Radius抄送功能参考信息_33769359.md`、对照 `WSFD-011306 Radius功能参考信息_15542176.md`

### 4.3 关键参数说明

#### 4.3.1 ADD RDSSVR 关键参数（本特性关注点）

| 参数 | 取值样例 | 说明 |
|------|---------|------|
| RDSSVRGRPNAME | isprg | 所属 Radius Server Group（与主送 AAA 服务器同一组） |
| SERVERTYPE | **ACCOUNTING** | 抄送服务器配置为 ACCOUNTING 类型（抄送的是计费消息） |
| IPVERSION | IPV4 | 服务器 IP 版本 |
| SERVERIPV4 | 192.168.8.183 | 抄送服务器 IPv4 地址（与 AAA 计费服务器 IP 不同） |
| PORT | 1819 | 抄送服务器端口（样例使用 1819，与主送 AAA 默认 1813 可不同，需与对端协商） |
| VPNINSTANCE | vpntest | 所属 VPN 实例（VPN 组网场景必配） |
| CIPHERKEY | ***** | 服务器密钥（加密的，与对端协商） |
| **PRIFLAG** | **CARBON_COPY** | ★**抄送服务器角色标识**（本特性核心参数，与 PRIMARY/SECONDARY 并列的第三个取值） |

> 来源：`激活支持RADIUS抄送功能_33769357.md`（"数据/表2 计费服务器配置"）

#### 4.3.2 ADD RDSSVRGRP / ADD APNRDSSVRGRP / ADD UPLIST4RDS 参数

与 WSFD-011306 完全一致，参见 WSFD-011306-Radius功能.md §4.3.1（RDSSVRGRP）、§4.3.2（RDSSVR 主备）、APNRDSSVRGRP（APN↔服务器组绑定）。本特性不改变这些命令的参数语义。

### 4.4 约束条件

| 约束类型 | 约束内容 |
|---------|---------|
| **前置强依赖** | 必须先完成 [激活 RADIUS 功能]（WSFD-011306），否则本特性无承载基础 |
| **前置调测依赖** | 调测本特性前必须先完成 [调测到 AAA Server 的数据]（WSFD-011306），确保主送链路连通 |
| **抄送服务器数量上限** | 每个 RADIUS Server Group 最多配置 **64** 个计费抄送服务器 |
| **抄送服务器角色** | 抄送服务器通过 PRIFLAG=CARBON_COPY 标识，与 PRIMARY/SECONDARY 同组共存 |
| **抄送消息范围** | 抄送的是**计费消息**（Accounting Start/Interim/Stop），不抄送鉴权消息（Access-Request/Accept/Reject） |
| **抄送服务器响应** | 抄送服务器**不回复消息给 UNC**（与主送 AAA Server 不同） |
| **在线删除风险** | 用户在线时删除抄送服务器配置，**可能造成抄送消息失败**（文档明确警告） |
| **系统信令消耗** | 增加的抄送服务器越多，对系统信令处理能力消耗越大 |
| **AAA 服务器参数一致性** | UNC 配置的主送 AAA Server IP/端口/Key 必须与 AAA Server 网元一致（继承 011306 约束） |
| **抄送服务器互通** | UNC 到抄送服务器链路必须连通；本端路由配置和抄送服务器配置需正确 |

> 来源：`特性概述_33741340.md`（"特性规格/对系统的影响"）、`激活支持RADIUS抄送功能_33769357.md`（"前提条件"）、`调测支持RADIUS抄送功能_33769358.md`（"操作步骤"）

---

## 5. 配置案例

### 5.1 典型场景：配置抄送鉴权消息和计费消息（1 主 + 1 备 + 1 抄送）

**场景描述**：UNC 上配置一个主备模式的 Radius 服务器组 isprg，包含主用计费 AAA 服务器（192.168.8.181:1819）、备用鉴权 AAA 服务器（192.168.8.182:1819）以及 **1 个抄送服务器**（192.168.8.183:1819，PRIFLAG=CARBON_COPY），并在 apn-test 下绑定该服务器组。VPN 实例 vpntest 用于抄送服务器组网。

**MML命令序列（原样保留）**：

```
//配置AAA服务器组、使用的APN

ADD RDSSVRGRP: RDSSVRGRPNAME="isprg", MODE=MASTER_SLAVE, SIGOPTACCTMSG=DISABLE;

ADD VPNINST: VPNINSTANCE="vpntest";

//配置AAA计费服务器。

ADD RDSSVR: RDSSVRGRPNAME="isprg", SERVERTYPE=ACCOUNTING, IPVERSION=IPV4, SERVERIPV4="192.168.8.181", PORT=1819, VPNINSTANCE="vpntest", CIPHERKEY="*****", PRIFLAG=PRIMARY;

ADD RDSSVR: RDSSVRGRPNAME="isprg", SERVERTYPE=AUTHENTICATION, IPVERSION=IPV4, SERVERIPV4="192.168.8.182", PORT=1819, VPNINSTANCE="vpntest", CIPHERKEY="*****", PRIFLAG=SECONDARY;

ADD RDSSVR: RDSSVRGRPNAME="isprg", SERVERTYPE=AUTHENTICATION, IPVERSION=IPV4, SERVERIPV4="192.168.8.183", PORT=1819, VPNINSTANCE="vpntest", CIPHERKEY="*****", PRIFLAG=CARBON_COPY;

//配置APN下绑定AAA服务器组。

ADD APN: APN="apn-test";
ADD APNRDSSVRGRP: APN="apn-test",RDSSVRGRPNAME="isprg";
```

**脚本要点解读**：

- 同一个 Radius Server Group `isprg` 内同时存在三类服务器：PRIMARY（主用计费）、SECONDARY（备用鉴权）、**CARBON_COPY（抄送）**
- 抄送服务器与主送 AAA 服务器共用同一个组、同一个 APN 绑定（ADD APNRDSSVRGRP 只绑一次）
- 抄送服务器通过 `PRIFLAG=CARBON_COPY` 唯一标识，无需额外命令开关"启用抄送"
- 多个抄送服务器时，重复执行 ADD RDSSVR（PRIFLAG=CARBON_COPY）即可（最多 64 个/组）

> 来源：`激活支持RADIUS抄送功能_33769357.md`（"任务示例"脚本，原样保留）

### 5.2 场景变体对照

| 变体 | 核心差异 | 关键命令/参数 | 文档覆盖度 |
|------|---------|--------------|-----------|
| 单抄送服务器（基础场景） | 1 个 CARBON_COPY 服务器 | ADD RDSSVR PRIFLAG=CARBON_COPY | 完整脚本（场景一） |
| 多抄送服务器 | 多个 CARBON_COPY 服务器（最多 64/组） | 重复 ADD RDSSVR PRIFLAG=CARBON_COPY | 命令支持，无独立脚本 |
| 按 PGW-U/UPF 匹配抄送 | 抄送服务器绑定 UP List | ADD UPLIST4RDS + ADD RDSSVR | 仅原理，无独立脚本 |
| VPN 组网抄送 | 抄送服务器走 VPN 实例 | ADD VPNINST + ADD RDSSVR VPNINSTANCE | 完整脚本（场景一） |

---

## 6. 验证与调测

### 6.1 调测 RADIUS 抄送功能

#### 6.1.1 调测前提与目的

当运营商部署分组交换网，在将 RADIUS 消息发往计费 AAA Server 时，需要将用户信息同时发给多个 AAA 抄送服务器。调测目的是验证计费消息是否正确抄送给抄送服务器。

> 适用：GGSN、PGW-C、SMF
> **关键**：抄送服务器**不回复消息给 UNC**（调测判定依据与主送不同）

#### 6.1.2 调测执行步骤（7 步）

**步骤1**：打开接入侧镜像接口上的抓包工具，准备抓取测试终端的出入报文。

**步骤2**：测试终端使用 "apn-test" APN 接入网络。
- 成功接入 → 执行步骤3
- 无法接入 → 调测 UNC 的接入功能

**步骤3**：查看计费消息是否抄送给抄送服务器（参考文档图1"计费消息"示意图）。
- 消息发送正确（源地址、目的地址、消息 ID 及各消息信元正确）→ 调测结束
- 消息发送有误 → 执行步骤4

**步骤4**：执行 `LST APNRDSSVRGRP`、`LST RDSSVR` 命令检查相应 APN 对应的服务器组配置是否正确。
- 正确 → 执行步骤5
- 不正确 → 参考 [激活支持RADIUS抄送功能] 重新配置，再次执行步骤2

**步骤5**：检查 UNC 到 AAA Server 抄送服务器的通信是否正常。
- 正常 → 执行步骤7
- 不正常 → 执行步骤6

**步骤6**：检查本端路由配置和抄送服务器的配置是否正确。
- 正确 → 执行步骤7
- 不正确 → 重新配置本端到抄送服务器的路由和抄送服务器上的配置，再次执行步骤2

**步骤7**：收集信息并寻求技术支持。
- a. 在 OM Portal 上创建用户跟踪任务并执行步骤1，保存报文
- b. 执行 `EXP MML` 命令将当前配置数据导出为 MML 脚本文件并保存
- c. 收集并保存上述所有查询信息
- d. 查看并收集对端设备配置及接口状态信息
- e. 收集归纳所有信息并联系华为技术支持解决

> 来源：`调测支持RADIUS抄送功能_33769358.md`（"操作步骤"7 步）

### 6.2 告警参考

**本特性无相关告警**（文档明确声明）。

> 来源：`WSFD-011307 支持Radius抄送功能参考信息_33769359.md`（"告警"章节）

### 6.3 测量指标

**本特性无相关测量指标**（文档明确声明）。

> 来源：`WSFD-011307 支持Radius抄送功能参考信息_33769359.md`（"测量指标"章节）

### 6.4 软参

**本特性无相关软参**（文档明确声明）。

> 来源：`WSFD-011307 支持Radius抄送功能参考信息_33769359.md`（"软参"章节）

### 6.5 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| 计费消息未抄送给抄送服务器 | APN 服务器组配置错误（未包含 CARBON_COPY 服务器） | `LST APNRDSSVRGRP` + `LST RDSSVR` 核对配置；参考激活章节重新配置 |
| 计费消息未抄送给抄送服务器 | UNC 到抄送服务器链路不通 | 检查本端路由配置和抄送服务器配置；检查 UNC 到抄送服务器通信 |
| 抄送消息失败 | 用户在线时删除了抄送服务器配置（文档明确警告） | 避免在线删除；如需删除先让用户去活 |
| 抄送消息目的地址/端口错误 | 抄送服务器 IP/端口与对端协商不一致 | `LST RDSSVR` 核对 SERVERIPV4/PORT/VPNINSTANCE；与抄送服务器网元配置比对 |
| 系统信令处理能力下降 | 抄送服务器数量过多 | 评估抄送服务器数量；单组不超过 64 个 |
| 按 UP 匹配抄送不生效 | UPLIST4RDS / 抄送服务器绑定的 UP List 配置错误 | `LST UPLIST4RDS` 核对 UP List；核对用户所在 PGW-U/UPF Host |
| 测试终端无法接入 | 主送 AAA 链路异常（前置依赖） | 调测 UNC 的接入功能；参考 WSFD-011306 调测到 AAA Server 数据 |

> 来源：综合 `调测支持RADIUS抄送功能_33769358.md`（"操作步骤"）、`特性概述_33741340.md`（"对系统的影响"）

---

## 7. 参考信息

### 7.1 与其他特性的关系

| 关联特性 | 特性ID | 关系说明 |
|---------|--------|---------|
| **Radius 功能（配置承载父节点）** | WSFD-011306（UNC） | **强依赖**：本特性复用 011306 的 RDSSVRGRP/RDSSVR/APNRDSSVRGRP/UPLIST4RDS 配置对象；激活本特性前**必须**先激活 011306 的 RADIUS 功能；核心扩展点是 ADD RDSSVR 的 PRIFLAG 新增 CARBON_COPY 取值 |
| **Radius 鉴权接入（鉴权决策上游）** | WSFD-011305（UNC） | 间接关联：011305 的 AUTHMODE 决策是否启用 Radius 鉴权；本特性只抄送计费消息，与鉴权决策无直接耦合 |
| **AAA 负荷分担** | WSFD-011308（UNC） | 并列：011308 扩展 MODE=ROUND_ROBIN 轮选；本特性扩展 PRIFLAG=CARBON_COPY 抄送；两者都基于 011306 的服务器组，但扩展维度不同 |
| **会话管理（宿主）** | WSFD-010501（UNC） | 间接关联：抄送挂在 PDP/PDU 会话激活/更新/去活流程的计费消息上 |

### 7.2 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011307 支持Radius抄送功能/特性概述_33741340.md` | 适用NF（GGSN/PGW-C/SMF + AAA Server + 抄送服务器）、定义（RADIUS Carbon-copy 将 AAA 计费消息抄送给其他服务器）、客户价值（降低 AAA Server 性能要求、同步增值服务）、应用场景（抄送服务器获取 IP/APN/MSISDN 了解用户在线状况）、可获得性（UNC 20.3.0+，无 License）、与其他特性交互（无）、对系统影响（增加抄送服务器消耗信令处理能力、在线删除风险）、应用限制（无）、原理概述（UNC 开启抄送功能图1）、特性规格（每 Group 最多 64 个抄送服务器）、遵循标准（3GPP 23.214/29.244 + RFC 2865）、发布历史（v01 20.3.0） |
| 2 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011307 支持Radius抄送功能/实现原理_33761637.md` | 抄送概念（类似 Email 抄送）、未启用 vs 启用对比（图1/图2）、UNC 支持功能（按 PGW-U/UPF 匹配抄送服务器、ADD UPLIST4RDS + ADD RDSSVR 绑定 UP List、基于用户上下文 PGW-U/UPF Host 查找匹配抄送服务器）、17 步业务流程图（图3：激活抄送 Start → 在线更新抄送 Interim-Update → 去激活抄送 Stop，含按 host 匹配抄送服务器步骤） |
| 3 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011307 支持Radius抄送功能/激活支持RADIUS抄送功能_33769357.md` | 6 步激活操作流程（ADD RDSSVRGRP → ADD VPNINST → ADD UPLIST4RDS 可选 → ADD RDSSVR → ADD APN → ADD APNRDSSVRGRP）、前提条件（必须先激活 RADIUS 功能 WSFD-011306、VPN 实例就绪、APN 已配置）、整体配置表与计费服务器配置表（PRIFLAG=PRIMARY/SECONDARY/CARBON_COPY 三种角色）、关键参数（SERVERTYPE=ACCOUNTING、PORT=1819、VPNINSTANCE、CIPHERKEY）、完整 MML 脚本（isprg 组含 1 主用计费 + 1 备用鉴权 + 1 抄送服务器 PRIFLAG=CARBON_COPY） |
| 4 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011307 支持Radius抄送功能/WSFD-011307 支持Radius抄送功能参考信息_33769359.md` | MML 命令清单（7 条：ADD RDSSVRGRP/RDSSVR/APNRDSSVRGRP/UPLIST4RDS、LST APNRDSSVRGRP/RDSSVR、EXP MML，全部复用 011306 命令集，无新增命令）、无告警、无软参、无测量指标 |
| 5 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/组网功能/WSFD-011307 支持Radius抄送功能/调测支持RADIUS抄送功能_33769358.md` | 7 步调测流程（接入侧镜像抓包、测试终端 apn-test 接入、查看计费消息是否抄送、LST APNRDSSVRGRP/RDSSVR 核对配置、检查 UNC 到抄送服务器通信、检查路由与抄送服务器配置、收集信息寻求支持）、关键说明（抄送服务器不回复消息给 UNC）、调测工具（测试终端 + 镜像接口抓包工具 + OM Portal 追踪） |

### 7.3 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| RADIUS Carbon-copy | RADIUS 抄送 | 将 AAA 计费消息抄送给其他需要获取用户信息的服务器 |
| Carbon-copy Server | 抄送服务器 | 接收 UNC 抄送 AAA 计费消息的外部服务器；不回复消息给 UNC |
| CARBON_COPY | 抄送角色标识 | ADD RDSSVR 命令 PRIFLAG 参数的第三个取值（与 PRIMARY/SECONDARY 并列） |
| UP List | PGW-U/UPF 列表 | ADD UPLIST4RDS 配置，用于按用户所锚定 PGW-U/UPF 匹配抄送服务器 |
| Start/Interim-Update/Stop | 计费消息三阶段 | 开始/更新/结束计费请求，三类消息均触发抄送 |

---

## 8. 文档一致性说明（配置树 vs 产品文档 vs 关联特性）

> 配置树仅用于定位特性 ID，以下记录以产品文档实际内容为准时发现的差异与协同点，供 Stage 3 横向分析参考。

### 8.1 与配置树/文档清单的差异

| # | 维度 | 配置树/文档清单描述 | 产品文档实际内容 | 差异类型 |
|---|------|---------------------|-----------------|---------|
| 1 | 特性定位 | 文档清单标题："Radius抄送功能（辅助）" | 产品文档定义："将 AAA 计费消息在发送给 AAA Server 的同时，抄送给其他需要获取用户信息的服务器" | 一致：清单与文档定位匹配 |
| 2 | 优先级 | 文档清单标注"[辅助]" | 产品文档内容完整（5 篇文档覆盖概述/原理/激活/调测/参考） | 补全：虽为辅助特性，但文档完整度与核心特性相当 |
| 3 | License要求 | 文档清单未明确 | 产品文档明确声明"**本特性无需获得 License 许可**" | 一致：与同域 011306 一致，均无 License |
| 4 | 命令清单规模 | 文档清单暗示核心命令较少 | 参考信息列出 **7 条命令**（全部复用 011306，无新增） | 澄清：本特性零新增命令，全部复用 011306 命令集 |
| 5 | 告警/软参/测量指标 | 文档清单未提及 | 产品文档明确声明**三项均无**（无告警、无软参、无测量指标） | 补全：本特性可观测性弱，调测依赖抓包 + LST 命令 |

### 8.2 与 WSFD-011305（Radius 鉴权接入）的关系

| # | 维度 | WSFD-011305（鉴权决策） | WSFD-011307（Radius 抄送） | 关系 |
|---|------|------------------------|---------------------------|------|
| 1 | 角色定位 | AUTHMODE 决策方：决定是否启用 Radius 鉴权 | 计费消息抄送方：抄送给增值服务器 | **无直接耦合**：011307 只抄送计费消息，与鉴权决策无关 |
| 2 | 消息范围 | 鉴权消息（Access-Request/Accept/Reject） | 计费消息（Accounting Start/Interim/Stop） | 不重叠 |
| 3 | 触发依赖 | AUTHMODE 配置 | 不依赖 AUTHMODE（依赖 011306 的计费消息发送） | 独立 |

### 8.3 ★与 WSFD-011306（Radius 功能）的关系：独立功能 vs 子能力（重点澄清）

| # | 维度 | 证据 | 结论 |
|---|------|------|------|
| 1 | **配置对象** | 本特性**复用** 011306 的 RDSSVRGRP/RDSSVR/APNRDSSVRGRP/UPLIST4RDS 四类对象，**未引入任何新配置对象** | 共享配置对象 |
| 2 | **命令清单** | 本特性 7 条命令**全部复用** 011306（参考信息章节对比），**零新增命令** | 共享命令集 |
| 3 | **核心扩展点** | 唯一扩展是 `ADD RDSSVR` 的 `PRIFLAG` 参数**新增第三个取值 `CARBON_COPY`**（011306 文档仅描述 PRIMARY/SECONDARY） | **参数级扩展** |
| 4 | **特性独立性** | 本特性有**独立的特性 ID（WSFD-011307）**、独立的特性概述/实现原理/激活/调测/参考信息 5 篇文档、独立的业务流程图（17 步） | **独立特性** |
| 5 | **激活独立性** | 激活本特性需**先激活 011306**（明确前置条件），但激活本特性本身是独立操作（配置 CARBON_COPY 服务器） | 独立激活步骤 |
| 6 | **功能定位** | 011306 是"Radius 协议承载与功能集总集"（鉴权+计费+策略控制）；011307 是"计费消息旁路抄送"专项能力 | **定位不同** |
| 7 | **客户价值** | 011306 客户价值覆盖鉴权/计费/策略控制全局；011307 客户价值聚焦"卸载 AAA Server 转发负担 + 增值信息同步" | 价值点不同 |

**综合结论**：**WSFD-011307 是独立特性，不是 WSFD-011306 的子能力**。两者关系是"**配置对象共享 + 参数级扩展**"的并行扩展特性：011306 提供基础配置对象（服务器组/服务器模板/APN 绑定/UP List），011307 通过在 ADD RDSSVR 的 PRIFLAG 参数中新增 CARBON_COPY 取值实现抄送服务器角色，两者在同一 Radius Server Group 内共存。

**文档依据**：

- 011306 文档中 ADD RDSSVR 的 PRIFLAG 参数描述仅含 `PRIMARY / SECONDARY` 两种（见 WSFD-011306-Radius功能.md §4.3.2）
- 011307 文档的激活配置表中 PRIFLAG 取值为 `PRIMARY / SECONDARY / CARBON_COPY` 三种（见 `激活支持RADIUS抄送功能_33769357.md` 表2）
- 011307 参考信息列出的 7 条命令与 011306 参考信息中的命令**完全重叠**（无新增）
- 011307 特性概述有独立的定义/客户价值/应用场景/原理/业务流程，**不是 011306 文档的子章节**

### 8.4 抄送配置对象清单（复用 011306）

| 配置对象 | 命令 | 本特性的使用方式 | 与 011306 的差异 |
|---------|------|-----------------|-----------------|
| Radius 服务器组 | ADD RDSSVRGRP | 与主送 AAA 服务器共用同一组 | 无差异 |
| Radius 服务器模板 | ADD RDSSVR | 配置抄送服务器时 PRIFLAG=CARBON_COPY | **PRIFLAG 新增第三取值** |
| APN↔服务器组绑定 | ADD APNRDSSVRGRP | 与主送共用同一绑定 | 无差异 |
| UP 列表 | ADD UPLIST4RDS | 可选，用于按 PGW-U/UPF 匹配抄送服务器 | 无差异（011306 已有此命令） |
| VPN 实例 | ADD VPNINST | VPN 组网场景使用 | 无差异 |
| APN | ADD APN | 与 011306 共用 | 无差异 |

---

## 附录 A：抄送配置速查表

| 配置维度 | 命令 | 关键参数 | 取值/样例 |
|---------|------|---------|----------|
| 服务器组（共用） | ADD RDSSVRGRP | RDSSVRGRPNAME, MODE | isprg, MASTER_SLAVE |
| 主用计费服务器 | ADD RDSSVR | PRIFLAG=PRIMARY, SERVERTYPE=ACCOUNTING | 192.168.8.181:1819 |
| 备用服务器 | ADD RDSSVR | PRIFLAG=SECONDARY | 192.168.8.182:1819 |
| **★抄送服务器** | **ADD RDSSVR** | **PRIFLAG=CARBON_COPY** | 192.168.8.183:1819 |
| 抄送服务器上限 | （规格） | 每 Group 最多 | 64 个 |
| VPN 绑定（抄送） | ADD RDSSVR | VPNINSTANCE | vpntest |
| UP List（按 UP 匹配） | ADD UPLIST4RDS | - | 可选 |
| APN 绑定（共用） | ADD APNRDSSVRGRP | APN, RDSSVRGRPNAME | apn-test, isprg |

---

## 附录 B：抄送消息流程速查

| 阶段 | 主送（UNC → AAA Server） | 抄送（UNC → Carbon-copy Server） | 抄送服务器响应 |
|------|--------------------------|----------------------------------|---------------|
| 激活 | Accounting Start | Accounting Start 拷贝 → Carbon-copy Server1/2 | **不回复** |
| 在线更新 | Accounting Interim-Update | Accounting Interim-Update 拷贝 → Carbon-copy Server1/2 | **不回复** |
| 去激活 | Accounting Stop | Accounting Stop 拷贝 → Carbon-copy Server1/2 | **不回复** |

---

**文档版本**：v1.0（Stage 2 知识提取，基于 5 篇产品文档）
**提取时间**：2026-06-22
**关键发现**：见返回报告
