# GWFD-020351 PCC基本功能 知识文档

> 场景视角：带宽控制。本文档聚焦 PCC 框架如何下发 MBR/GBR/QoS 参数、如何触发带宽管理（BWM）动作，以及 UPF 侧的完整配置规则。

---

## 概述

### 特性定义

PCC（Policy and Charging Control）是策略和计费控制。PCC 基本功能用于在用户的业务流程中实现 UE 策略、移动性策略、会话策略和计费控制，通过区分业务并进行实时 QoS 控制（含 MBR 限速、GBR 保障、门控等），合理利用网络资源，提升数据业务流量的经营价值，丰富数据业务市场营销手段。

在带宽控制场景中，PCC 基本功能是整个策略执行的入口：PCRF/PCF 做出 QoS 决策后，通过 SMF 将 MBR（Maximum Bit Rate）、GBR（Guaranteed Bit Rate）、QCI/5QI、ARP 等参数下发给 UPF，UPF 据此执行限速、保障和门控，构成端到端的带宽控制链路。

### 适用NF

| NF | 产品 | 角色 |
|----|------|------|
| PGW-U / UPF | UDG 20.0.0 及后续版本 | 用户面策略执行：业务数据流检测、流量/时长统计、QoS 控制、带宽管理（MBR/GBR 执行）、重定向 |
| PGW-C / SMF | UNC 20.0.0 及后续版本 | 策略控制执行：SDF 与 QoS 流绑定、QoS/计费/门控/转发/流量转向决策、计费话单上报 |
| PCRF / PCF | 无特殊要求 | 策略决策：基于业务的 QoS 策略、计费规则生成与下发 |
| AMF | 无特殊要求 | 接入和移动性策略执行（5G） |
| AF | 无特殊要求 | 应用功能实体：向 PCRF/PCF 传送应用级会话信息 |
| SPR / UDR | 无特殊要求 | 用户签约数据存储 |

### 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|----------|----------|----------|
| 01 | 20.0.0 | 首次发布 |

### License

| License 控制项 | License 编码 | 说明 |
|----------------|-------------|------|
| PCC 基本功能 | 82209825 LKV3G5PCCB01 | 必须获得 License 许可后才能使用本特性 |

启用命令：

```
SET LICENSESWITCH:LICITEM="LKV3G5PCCB01",SWITCH=ENABLE;
```

### 前置条件与依赖

- 完成业务感知配置（SA-Basic 等基础特性）。
- 完成加载 License（LKV3G5PCCB01）。
- PGW-U/UPF 与 PGW-C/SMF 配合作为策略执行实体，PGW-C/SMF 的配置参见 UNC 初始配置手册和 PCC 基本功能配置资料。
- 如需计费功能，需预先通过 `ADD URRGROUP` 命令配置计费属性。

### 遵循标准

| 标准类别 | 标准编号 | 标准名称 |
|----------|----------|----------|
| 3GPP | 23501 v15.2.0 | System Architecture for the 5G System; Stage 2 |
| 3GPP | 23502 v15.2.0 | Procedures for the 5G System; Stage 2 |
| 3GPP | 23503 v15.2.0 | Policy and Charging Control Framework for the 5G System; Stage 2 |
| 3GPP | 29507 v15.2.0 | 5G System; Access and Mobility Policy Control Service; Stage 3 |
| 3GPP | 29512 v15.2.0 | 5G System; Session Management Policy Control Service; Stage 3 |
| 3GPP | 29513 v15.2.0 | 5G System; Policy and Charging Control signalling flows and QoS parameter mapping; Stage 3 |

---

## 核心概念

### 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| PCC | Policy and Charging Control | 策略和计费控制，3GPP 定义的 QoS/计费/门控统一框架 |
| PCRF | Policy and Charging Rules Function | 2/3/4G 策略决策网元，通过 Gx 接口下发策略 |
| PCF | Policy Control Function | 5G 策略决策网元，通过 N7 接口下发策略 |
| PCC Rule | PCC 规则 | 一组提供策略控制或计费控制参数的信息集，含 5QI、ARP、SDF 模板、计费信息、带宽参数等 |
| QoS | Quality of Service | 服务质量，包含 QCI/5QI、ARP、MBR、GBR 等参数 |
| Gate | 门控 | 对业务流进行允许/阻断控制 |
| Flow / SDF | Service Data Flow | 业务数据流，一组具有相同 QoS 的 IP 数据流 |
| MBR | Maximum Bit Rate | 最大比特率，对业务流的上限限速 |
| GBR | Guaranteed Bit Rate | 保证比特率，对业务流的最低带宽保障 |
| AMBR | Aggregate Maximum Bit Rate | 聚合最大比特率，对 PDU 会话或 Non-GBR 承载集合的限速 |
| QCI / 5QI | QoS Class Identifier / 5G QoS Identifier | QoS 等级标识，决定延迟、丢包率等传输特性 |
| ARP | Allocation and Retention Priority | 分配和保留优先级，决定资源抢占/被抢占的优先级 |
| BWM | Bandwidth Management | 带宽管理，UPF 执行限速/保障/整形的具体动作 |
| URR | Usage Reporting Rule | 使用量上报规则，用于流量/时长统计和上报触发 |

### 对象模型

#### PCC 规则结构（从带宽控制视角）

PCC 规则承载了完整的 QoS 和带宽控制决策：

```
PCC Rule
  ├── 规则标识: RULENAME
  ├── QoS 参数
  │     ├── 5QI / QCI          → 决定 QoS 等级（GBR / Non-GBR）
  │     ├── ARP                → 优先级、抢占能力
  │     ├── MBR (UL/DL)        → 最大比特率（限速上限）
  │     └── GBR (UL/DL)        → 保证比特率（带宽保障）
  ├── SDF 模板
  │     └── Flow-Description    → 业务流过滤器（IP 五元组）
  ├── 策略控制信息
  │     ├── Gate (Open/Close)   → 门控状态
  │     ├── Redirect            → 重定向
  │     └── BWM Action          → 带宽管理动作
  ├── 计费信息
  │     ├── Charging Key
  │     ├── Rating Group
  │     └── Measurement Method
  └── 用量监控信息
        └── Monitoring Key
```

#### 会话规则结构

会话规则在 PDU 会话粒度控制带宽：

| 信息元素 | 带宽控制作用 |
|----------|-------------|
| Session-AMBR | PDU 会话集合的最大速率限制（Non-GBR 承载聚合限速） |
| 默认 QoS | 默认 QoS flow 的 QoS 参数（含默认 5QI/QCI、ARP） |
| 用量监控数据 | 流量/时长用量监控，达到阈值后可触发策略变更（如降速） |
| 条件数据 | 策略条件索引 |

### PCC 在带宽控制中的角色

PCC 基本功能在带宽控制链路中的位置：

```
PCRF/PCF  ──QoS决策──>  SMF  ──N4下发──>  UPF  ──执行──>  用户面流量
  |                        |                   |
  策略生成                  QoS映射             带宽控制执行
  MBR/GBR决策               PDR/FAR/QER         限速(MBR)
  QCI/5QI选择               URR构建             保障(GBR)
  ARP分配                   AMBR下发            门控(Gate)
                                                整形(Shaping)
```

**MBR/GBR 下发路径**：
1. PCRF/PCF 根据用户签约和业务需求，决定每个 SDF 的 MBR、GBR、5QI/QCI 和 ARP。
2. 通过 N7 接口（5G）或 Gx 接口（2/3/4G）将这些参数下发给 SMF。
3. SMF 进行 QoS 映射，将 SDF 绑定到 QoS flow，通过 N4 接口构建 QER（QoS Enforcement Rule）下发给 UPF。
4. UPF 收到 QER 后，对匹配的业务流执行 MBR 限速、GBR 保障和门控。

**BWM 动作触发**：
- UPF 根据 QER 中的 MBR 参数对业务流进行令牌桶限速。
- 当 MBR 设置为特定速率时，超出部分的报文将被缓存（Shaping 模式）或丢弃（Policing 模式）。
- 当 Gate 为 Close 时，阻断所有匹配的业务流。
- 当 GBR 承载的 QoS flow 建立时，UPF 为该 flow 预留带宽资源。

---

## 原理与流程

### 实现原理

PCC 基本功能的组网及接口关系：用户使用 5G 业务时，通过 LTE 或(R)AN 接入网络，PCRF/PCF 根据用户签约信息、业务信息或用户状态信息等进行决策，生成控制策略。PCRF/PCF 通过 N7 接口将 QoS 及计费策略下发给 PGW-C/SMF，PGW-C/SMF 通过 N4 接口再下发给 PGW-U/UPF，PGW-U/UPF 基于用户和业务类型进行限速和门控，并且将 QoS 信息传递给无线、核心网共同进行端到端资源管理。

**带宽控制关键传递**：
- SMF 将 SDF 映射到 QoS flow 时，同时确定该 flow 是 GBR 还是 Non-GBR 承载。
- 对于 GBR flow：UPF 执行 GBR 保障 + MBR 限速。
- 对于 Non-GBR flow：UPF 执行 Session-AMBR 聚合限速。
- UPF 对下行数据包进行传输层标记（QFI），无线侧据 QFI 进行无线资源调度。

### 业务流程

#### 用户接入时 PCC 关键流程

当用户发起注册流程接入 5G 网络时：

1. AMF 和 PGW-C/SMF 分别发起 PCRF/PCF 发现和选择流程。
2. 选定 PCRF/PCF 后，发起 AM 策略关联建立和 SM 策略关联建立流程。
3. 获取相应的策略（含 PCC 规则）及策略事件上报触发器。
4. 部署执行策略。
5. PGW-C/SMF 在收到 SM 策略后进行 QoS 映射，将相应的 QoS 信息下发给 PGW-U/UPF、RAN 和 UE，进行端到端的 QoS 控制。

#### PDU 会话建立（带宽控制视角）

| 步骤 | 动作 | 带宽控制相关 |
|------|------|-------------|
| 1 | SMF 基于收到的 SM 策略，将 SDF 映射到 QoS flow | 确定 GBR/Non-GBR、5QI、MBR、GBR |
| 2 | SMF 通过 N4 接口下发 QoS 计费策略给 UPF | 下发 PDR（检测规则）、QER（QoS 执行规则，含 MBR/GBR）、URR（用量上报）、FAR（转发规则） |
| 3 | UPF 基于收到的 SDF 将用户面数据和 QoS flow 匹配 | 建立 MBR 令牌桶、GBR 带宽预留 |
| 4 | UPF 对下行数据包进行传输层标记（QFI） | 标记 QFI 供无线侧调度 |
| 5 | UPF 对 PDU 会话集合的最大速率进行控制 | 执行 Session-AMBR 限速 |
| 6 | UPF 对 PDU 进行流量统计 | 支持计费和用量监控 |

#### PDU 会话修改（带宽动态调整）

在用户使用业务过程中，当满足触发器条件时（如用户签约信息更改或用户接入位置改变），PCRF/PCF 或 AMF/PGW-C/SMF 可分别发起策略关联更新流程，从而更新相应策略。

| 场景 | 触发方式 | 带宽调整内容 |
|------|---------|-------------|
| 用户套餐变更 | PCRF/PCF 发起 SM 策略更新 | 修改 MBR/GBR/QCI，动态提速或降速 |
| 用量监控触发 | UPF 上报用量（VOLTH/VOLQU 等） | PCRF/PCF 据此调整限速策略（如 FUP 降速） |
| 漫游切换 | AM 策略更新 | 可能影响 QoS 策略归属网络 |

**关键规则**：一条消息中存在对同一个预定义 rule 的安装和删除操作时，UPF 对该 rule 执行安装操作（安装优先于删除）。

#### PDU 会话释放

当 PCRF/PCF 检测到 UE 签约信息删除、UE 从网络去注册或满足其他触发器条件时，发起策略关联释放流程。UPF 将丢弃与该 PDU 会话相关的数据包，并释放与 N4 会话相关的所有隧道资源和上下文（含带宽资源释放）。

### 2/3/4/5G PCC 功能差异

| 差异点 | 2/3/4G | 5G |
|--------|--------|-----|
| **关键网元** | AF, SPR, PCRF, PGW(PCEF) | AF, UDR, PCF, AMF, PGW-C/SMF, UPF |
| **接口** | Gx | N7, N15, N4 |
| **协议** | 基于 Diameter 的 Gx 应用协议 | PFCP 协议（N4）、HTTPS（N7, N15） |
| **策略类型** | 会话管理策略 | 会话管理策略（SM 策略）、接入和移动性策略（AM 策略）、选网和路由策略（UE 策略） |
| **漫游支持** | 策略在归属网络生成 | 策略在归属网络生成 + 策略在访问网络生成 |
| **主要流程** | IP-CAN 会话流程、专有承载流程 | PCF 发现和选择、AM 策略关联流程、SM 策略关联流程、PFD 管理流程 |
| **规则来源** | PCRF 下发、AAA Server 下发、本地配置 | PCF 下发、本地配置 |
| **规则分类** | 动态规则、预定义规则、预定义规则组（即本地 UserProfile） | 动态规则、预定义规则（可匹配预定义规则或 UserProfile，将 4G 的预定义规则和预定义规则组统一） |

### 协议交互

#### Gx 接口（2/3/4G）

- 基于 Diameter 协议的 Gx 应用。
- PCRF 通过 Gx 接口向 PGW（PCEF）下发 PCC 规则。
- 消息类型：CCR（Credit-Control-Request）、CCA、RAR、RAA。

#### N7 接口（5G）

- 基于 HTTP/2 的 RESTful API。
- PCF 通过 N7 接口向 SMF 下发 SM 策略。
- 关键消息：
  - `Npcf_SMPolicyControl_Update` response
  - `Npcf_SMPolicyControl_UpdateNotify` request
- 触发器可由 PCRF/PCF 在上述消息中下发给 SMF。

#### N4 接口（5G，SMF-UPF）

- 基于 PFCP（Packet Forwarding Control Protocol）协议。
- SMF 通过 N4 接口向 UPF 下发 PDR/FAR/QER/URR 等规则。
- 关键消息：
  - `PFCP Session Establishment Request/Response`
  - `PFCP Session Modification Request/Response`
  - `PFCP Session Deletion Request/Response`

---

## 配置规则

### 激活步骤

UPF 侧 PCC 基本功能的完整激活流程（动态 PCC 和本地 PCC 共用）：

| 步骤 | 操作 | MML 命令 | 说明 |
|------|------|---------|------|
| 1 | 打开 License 配置开关 | `SET LICENSESWITCH` | 启用 PCC 基本功能 |
| 2 | 配置 PCC 策略组 | `ADD PCCPOLICYGRP` | 关联 URR 组（计费用） |
| 3 | 配置流过滤器 | `ADD FLOWFILTER` | 定义业务流检测模板 |
| 4 | 配置三四层过滤条件 | `ADD FILTER` + `ADD FLTBINDFLOWF` | 定义具体过滤规则 |
| 5 | 配置规则 | `ADD RULE` | 绑定流过滤器和策略组 |
| 6 | 配置规则与用户模板的绑定 | `ADD USERPROFILE` + `ADD RULEBINDING` | 建立 UserProfile |
| 7 | 刷新生效 | `SET REFRESHSRV` | **必须最后执行** |

### UPF 侧 PCC 配置对象层级

```
UserProfile（用户模板）
  └── RULEBINDING（规则绑定）
        └── RULE（规则）
              ├── FILTERINGMODE（匹配模式：FLOWFILTER）
              │     └── FLOWFILTER（流过滤器）
              │           ├── FLTBINDFLOWF（过滤器绑定）
              │           │     └── FILTER（三四层过滤器）或 L7FILTER（七层过滤器）
              │           └── PROTBINDFLOWF（协议绑定）
              └── POLICYNAME（策略名称）
                    └── PCCPOLICYGRP（PCC策略组）
                          └── URRGROUPNAME（URR组名称，计费时需要）
```

### MML 命令清单

| 命令 | 用途 | 关键参数 |
|------|------|---------|
| `SET LICENSESWITCH` | 设置 License 开关 | LICITEM="LKV3G5PCCB01", SWITCH=ENABLE |
| `ADD PCCPOLICYGRP` | 增加 PCC 策略组 | PCCPOLICYGRPNM, URRGROUPNAME |
| `ADD FLOWFILTER` | 增加流过滤器 | FLOWFILTERNAME |
| `ADD FILTER` | 增加三四层过滤器 | FILTERNAME, L34PROTTYPE, L34PROTOCOL |
| `ADD FLTBINDFLOWF` | 增加流过滤器与过滤器的绑定 | FLOWFILTERNAME, FILTERNAME |
| `ADD RULE` | 增加规则 | RULENAME, POLICYTYPE=PCC, FILTERINGMODE, FLOWFILTERNAME, PRIORITY, POLICYNAME |
| `ADD USERPROFILE` | 增加用户模板 | USERPROFILENAME |
| `ADD RULEBINDING` | 增加用户模板和规则的绑定 | USERPROFILENAME, RULENAME |
| `ADD QOSPROP` | 增加 QoS 属性 | 用于配置 QoS 参数 |
| `SET REFRESHSRV` | 业务刷新 | REFRESHTYPE=ALL |
| `LST LICENSESWITCH` | 查询 License 开关 | LICITEM |
| `LST USERPROFILE` | 查询用户模板 | - |
| `LST RULEBINDING` | 查询规则绑定 | - |
| `LST RULE` | 查询规则 | - |
| `LST FLOWFILTER` | 查询流过滤器 | - |
| `LST FLTBINDFLOWF` | 查询过滤器绑定 | - |
| `LST FILTER` | 查询过滤器 | - |
| `LST PROTBINDFLOWF` | 查询协议绑定 | - |
| `LST L7FILTER` | 查询七层过滤器 | - |
| `LST PCCPOLICYGRP` | 查询 PCC 策略组 | - |
| `LST URRGROUP` | 查询 URR 组 | - |
| `LST URR` | 查询 URR | - |
| `EXP MML` | 导出 MML 配置文件 | 用于问题排查和信息收集 |

### 参数说明

#### PCC 策略组参数

| 参数 | 说明 | 约束 |
|------|------|------|
| PCCPOLICYGRPNM | PCC 策略组名称 | 存在多条数据时，该参数不能相同 |
| URRGROUPNAME | URR 组名称 | 当需要计费时必须配置，需已通过 `ADD URRGROUP` 命令配置 |

#### 规则参数

| 参数 | 说明 | 取值/约束 |
|------|------|----------|
| RULENAME | 规则名称 | 与 SMF 上配置的规则名称相同；存在多条数据时，该参数+策略类型不能完全相同 |
| POLICYTYPE | 策略类型 | PCC 基本功能使用 **PCC** |
| FILTERINGMODE | 流过滤器模式 | **FLOWFILTER** |
| FLOWFILTERNAME | 流过滤器名称 | 需已通过 `ADD FLOWFILTER` 命令定义 |
| PRIORITY | 全局优先级 | 仅对 PCC 用户生效。**优先级值越小，优先级越高**。优先级相同时：动态规则 > 预定义规则 > 本地规则 |
| POLICYNAME | 策略名称 | 需已通过 `ADD PCCPOLICYGRP` 命令定义 |

#### 三四层过滤器参数

| 参数 | 说明 | 取值样例 |
|------|------|---------|
| FILTERNAME | 过滤器名称 | 不同过滤器之间不能重复，如 "filter_test" |
| L34PROTTYPE | 三四层 IPv4 协议输入类型 | STRING |
| L34PROTOCOL | 三四层协议类型 | ANY（表示 Any to any，匹配所有报文） |

#### QoS 参数（通过 PCC 规则/QER 携带）

| 参数 | 说明 | 带宽控制作用 |
|------|------|-------------|
| 5QI / QCI | QoS 等级标识 | 决定是 GBR（5QI 1-4, 65-67）还是 Non-GBR（5QI 5-9, 69-79）承载，影响延迟和丢包率 |
| ARP | 分配和保留优先级 | 优先级值 1-15，值越小优先级越高；决定资源紧张时是否抢占低优先级 flow 的带宽 |
| MBR (UL/DL) | 最大比特率 | UPF 令牌桶限速上限，超出部分缓存或丢弃 |
| GBR (UL/DL) | 保证比特率 | UPF 为该 flow 预留的最低带宽保障 |
| Session-AMBR | 会话聚合最大比特率 | 对 PDU 会话内所有 Non-GBR flow 的聚合限速 |

### 约束条件

| 约束 | 说明 |
|------|------|
| 流过滤器必须绑定过滤条件 | 流过滤器必须至少绑定一个 filter 或一个 l7filter，否则所有报文都匹配不上该流过滤器 |
| UserProfile 名称一致性 | 预定义规则组或本地规则时，UPF 上的 UserProfile 名称与 SMF 上的 UserProfile 名称需要一致 |
| 规则名称一致性 | 预定义规则时，UPF 上的规则名称与 SMF 上的规则名称需要一致 |
| URR 标识一致性 | 对于同一 rule（rule 名称+策略类型唯一标识一条 rule），UPF 上的 URR 标识和 SMF 上的 URR 标识需要一致 |
| REFRESHSRV 必须执行 | 配置完成后必须执行 `SET REFRESHSRV:REFRESHTYPE=ALL` 将 Filter 和 UserProfile 置为生效 |
| 系统性能影响 | 使用 PCC 功能，系统性能将下降；用户激活时 SMF 需与 PCRF/PCF 交互，激活性能将下降；UPF 需动态处理策略，增加报文处理时延 |

---

## 配置案例

### 典型场景1：动态 PCC 策略（PCF 下发）含完整 MML

**场景描述**：网络中已部署 PCRF/PCF，用户需要激活为 PCC 用户。PCF 动态下发 QoS 决策（含 MBR/GBR），SMF 传递给 UPF 执行带宽控制。本例配置 3/4 层 any to any 的 filter（所有报文匹配）。

```
// 1. 打开 PCC 基本功能 License 配置开关
SET LICENSESWITCH:LICITEM="LKV3G5PCCB01",SWITCH=ENABLE;

// 2. 配置三四层过滤器和流过滤器（Any to Any，匹配所有报文）
ADD FILTER:FILTERNAME="filter_test",L34PROTTYPE=STRING,L34PROTOCOL=ANY;
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_test";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",FILTERNAME="filter_test";

// 3. 配置 PCC 策略组（当需要计费时配置 URRGROUPNAME）
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pg_test",URRGROUPNAME="urrgp_test";

// 4. 配置规则（绑定流过滤器和策略组）
ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,
  FILTERINGMODE=FLOWFILTER,
  FLOWFILTERNAME="flowfilter_test",
  PRIORITY=65535,
  POLICYNAME="pg_test";

// 5. 配置规则与用户模板的绑定关系
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";

// 6. 将新配置的 Filter 和 UserProfile 置为生效
SET REFRESHSRV:REFRESHTYPE=ALL;
```

**工作原理**：
1. 用户注册时，SMF 发起与 PCF 的 SM 策略关联建立。
2. PCF 根据用户签约和业务策略，下发 PCC 规则（含 5QI、ARP、MBR、GBR 等参数）。
3. SMF 将 PCC 规则映射为 N4 接口的 PDR/QER/URR/FAR，下发给 UPF。
4. UPF 收到规则后，对匹配的业务流执行 QoS 控制（MBR 限速、GBR 保障）、流量统计和计费。
5. 当触发器条件满足时（如用量达到阈值），UPF 上报用量，PCF 可动态调整 MBR（如 FUP 降速）。

### 典型场景2：本地 PCC 策略（无 PCF 场景）

**场景描述**：网络中无 PCRF/PCF，通过特定 APN 激活的用户需要激活为 PCC 用户。SMF 通过 UserProfile 名称激活 UPF 本地静态配置的规则来实现计费和策略控制。

```
// 命令序列与动态 PCC 完全相同
SET LICENSESWITCH:LICITEM="LKV3G5PCCB01",SWITCH=ENABLE;

ADD FILTER:FILTERNAME="filter_test",L34PROTTYPE=STRING,L34PROTOCOL=ANY;
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_test";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",FILTERNAME="filter_test";

ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pg_test",URRGROUPNAME="urrgp_test";

ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,
  FILTERINGMODE=FLOWFILTER,
  FLOWFILTERNAME="flowfilter_test",
  PRIORITY=65535,
  POLICYNAME="pg_test";

ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";

SET REFRESHSRV:REFRESHTYPE=ALL;
```

**与动态 PCC 的关键差异**：

| 对比维度 | 动态 PCC | 本地 PCC |
|----------|---------|---------|
| 前提条件 | 网络中有 PCRF/PCF | 网络中无 PCRF/PCF，通过特定 APN 激活 |
| 规则定义方 | PCRF/PCF 定义策略，SMF 传递 | SMF 定义策略，仅下发规则名称 |
| 动态规则 | 支持：PCF 下发业务流特征及精细化管理动作 | 不支持 |
| 预定义规则 | UPF/SMF/PCF 上需定义相同的规则标识 | UPF/SMF 上需定义相同的规则组标识 |
| 规则实时更新 | PCF 可以随时删除旧规则、安装新规则 | SMF 不支持实时更新规则 |
| 带宽控制灵活性 | 高：可根据实时用量动态调整 MBR/GBR | 低：带宽参数静态配置，修改后需刷新 |

---

## 验证与调测

### 验证方法

#### 验证前置条件

- 完成激活 PCC 基本功能配置。
- 准备测试终端。
- 准备 OM Portal 跟踪工具。
- 获取测试终端使用的 APN 名称（可使用 `LST APN` 命令查询）。

#### 验证流程

**步骤1：查询 License 开关状态**

```
LST LICENSESWITCH:LICITEM="LKV3G5PCCB01";
```
- SWITCH 为 ENABLE：继续下一步。
- SWITCH 为 DISABLE：执行 `SET LICENSESWITCH` 打开。

**步骤2：检查 UPF 上的配置是否正确**

执行以下命令逐项验证配置一致性：

```
LST USERPROFILE;
LST RULEBINDING;
LST RULE;
LST FLOWFILTER;
LST FLTBINDFLOWF;
LST FILTER;
LST PROTBINDFLOWF;
LST L7FILTER;
LST PCCPOLICYGRP;
LST URRGROUP;
LST URR;
```

配置一致性检查要求：
- 预定义规则组或本地规则时：UPF 上的 UserProfile 名称与 SMF 上的 UserProfile 名称需要一致。
- 预定义规则时：UPF 上的规则名称与 SMF 上的规则名称需要一致。
- 同一 rule（rule 名称+策略类型唯一标识一条 rule）：UPF 上的 URR 标识和 SMF 上的 URR 标识需要一致。

**步骤3：创建用户跟踪任务**

在 UDG（PGW-U/UPF）上创建用户跟踪任务。

**步骤4：激活用户并跟踪消息**

激活用户，在跟踪消息中检查 N4 接口交互。

**步骤5：检查 N4 接口消息**

- 查看消息跟踪中是否存在 N4 接口的 `PFCP Session Establishment Request` 消息。
- 检查激活响应消息 `PFCP Session Establishment Response` 中的返回码 Cause 是否为 `request-accepted (1)`。
- SMF 通过 N4 接口向 UPF 下发 PDR/FAR/QER/URR 等信息。

**结果判定**：
- N4 消息存在且返回码为 `request-accepted (1)`：PCC 用户 PDU 会话激活成功。
- N4 消息不存在：UDG 未收到 PCC 用户的 PDU 会话激活请求，需检查 UNC（PGW-C/SMF）上的配置。
- N4 消息存在但返回码不为 `request-accepted (1)`：PDU 会话激活失败，基于 Cause 的失败原因进行分析。

**步骤6：业务验证**

用户终端打开浏览器，访问 HTTP 业务。UPF 根据 SMF 下发的策略，对业务进行处理（转发/带宽控制/流量统计等）。

### 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|----------|---------|---------|
| N4 接口消息不存在 | UNC（PGW-C/SMF）配置问题 | 检查 UNC 上的配置是否正确，修改后重新激活用户 |
| PFCP Session Establishment Response 返回码不为 request-accepted (1) | UPF 配置错误或资源不足 | 基于 Cause 失败原因进行分析 |
| 配置不一致导致策略不生效 | UPF 与 SMF 侧配置不匹配 | 使用 LST 命令逐项比对 UserProfile 名称、规则名称、URR 标识 |
| 业务策略不生效 | Filter 未生效或 REFRESHSRV 未执行 | 检查 `SET REFRESHSRV` 是否已执行；检查流过滤器是否绑定了过滤条件 |
| 带宽控制未达到预期速率 | QER 中 MBR/GBR 参数未正确下发或映射 | 跟踪 N4 消息，检查 QER 中是否包含正确的 MBR/GBR 值 |
| PCC 用户激活慢 | SMF 需与 PCRF/PCF 交互获取策略 | 属正常行为，用户激活性能受 PCRF/PCF 响应时延影响 |

### 问题升级

如无法自行解决，执行以下信息收集：
1. 执行 `EXP MML` 命令将当前配置数据导出为 MML 脚本文件并保存。
2. 收集并保存所有查询信息。
3. 收集归纳所有信息并联系华为技术支持。

---

## 参考信息

### 接口与信元

#### Event Trigger 机制

PCC 架构中定义了 Event Trigger，当相应事件发生时，SMF 触发对应 Event Trigger，并向 PCRF/PCF 申请更新策略。SMF 支持通过 URR（使用量上报规则）设置 UPF 的上报事件触发点。

| Event Trigger | 含义 | 关联 IE | 带宽控制关联 |
|---------------|------|---------|-------------|
| PERIO (Periodic Reporting) | UPF 基于测量周期定时发起上报 | Measurement Period | 周期性上报用量，PCF 据此可定期调整限速 |
| VOLTH (Volume Threshold) | UPF 基于流量阈值发起上报 | Volume Threshold | 流量达到阈值时上报，PCF 可触发降速（FUP） |
| TIMTH (Time Threshold) | UPF 基于时长阈值发起上报 | Time Threshold | 时长达到阈值时上报，PCF 可触发策略变更 |
| QUHTI (Quota Holding Time) | UPF 基于配额保持时间发起上报 | Quota Holding Time | 配额超时上报，触发重新授权 |
| START (Start of Traffic) | UPF 在感知到业务开始时发起上报 | NA | 业务开始时触发策略下发（如动态提速） |
| STOPT (Stop of Traffic) | UPF 在感知到业务结束时发起上报 | NA | 业务结束时触发策略清理 |
| DROTH (Dropped DL Traffic Threshold) | UPF 基于下行丢包阈值发起上报 | Dropped DL Traffic Threshold | 因 MBR 限速导致丢包超过阈值时上报 |
| LIUSA (Linked Usage Reporting) | UPF 基于关联 URR ID 协同触发上报 | Linked URR ID | 关联 URR 上报时协同触发 |
| VOLQU (Volume Quota) | UPF 基于流量配额耗尽发起上报 | Volume Quota | 配额耗尽时上报，PCF 可停止服务或降速 |
| TIMQU (Time Quota) | UPF 基于时长配额耗尽发起上报 | Time Quota | 时长配额耗尽时上报 |
| ENVCL (Envelope Closure) | UPF 基于信封测量周期发起上报 | NA | 信封关闭时上报 |
| MACAR (MAC Addresses Reporting) | UPF 在检测 UE 上行报文源 MAC 时发起上报 | NA | MAC 地址上报 |
| EVETH (Event Threshold) | UPF 基于事件阈值发起上报 | Event Information | 事件数超阈值时上报 |

#### N4 接口下发规则类型

| 规则类型 | 全称 | 带宽控制作用 |
|---------|------|-------------|
| PDR | Packet Detection Rule | 业务流检测规则，定义哪些报文匹配该 flow |
| FAR | Forwarding Action Rule | 转发动作规则，定义转发、丢弃、缓存等行为 |
| QER | QoS Enforcement Rule | QoS 执行规则，**核心带宽控制规则**，携带 MBR/GBR/QFI/Gate 参数 |
| URR | Usage Reporting Rule | 使用量上报规则，用于流量/时长统计和阈值上报 |

#### 相关软参

| 软参 | 说明 |
|------|------|
| BIT440 | 控制动态业务签约场景，service-property 匹配失败时的报文动作 |

### 与其他特性的关系

| 相关特性 | 关系说明 |
|---------|---------|
| GWFD-010201 QoS 与流量管理 | PDU 会话建立时，SMF 基于 QoS 及业务需求将 SDF 映射到 QoS flow 上，详见该特性 |
| GWFD-110311 基于业务感知的带宽控制 | PCC 基本功能为其提供策略执行框架，SA 触发的 BWM 动作通过 PCC 规则下发 |
| GWFD-020358 业务触发的 QoS 保证 | 基于 PCC 框架触发专有 QoS flow（对应 4G 专有承载）的建立、修改、删除 |
| WSFD-109101 PCC基本功能（UNC） | UNC 侧 PCC 基本功能，与本特性构成控制面-用户面 PCC 完整链路 |

### 对系统的影响

- 使用 PCC 功能，系统性能将下降，具体下降程度需要根据具体话务模型进行分析。
- 用户激活时，SMF 需要与 PCRF/PCF 进行交互，获取用户策略并转换为 N4 接口的 PDR 下发到 UPF，用户激活性能将下降。
- UPF 需要动态处理 PCRF/PCF 下发的策略，将影响系统的报文处理过程，增加报文处理时延。

---

## 知识来源

### 文档清单

| 序号 | 源文件路径 | 贡献内容 |
|------|-----------|---------|
| 1 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/GWFD-020351 PCC基本功能特性概述_47011385.md` | 适用NF、定义、客户价值、应用场景、可获得性（涉及NF角色与功能、License）、与其他特性交互、对系统影响、原理概述、遵循标准、发布历史 |
| 2 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/GWFD-020351 PCC基本功能参考信息_79592737.md` | 相关 MML 命令清单、软参（BIT440）、告警与测量信息 |
| 3 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/实现原理/相关概念_72244993.md` | 策略分类（AM/UE/SM策略详解）、触发器概念、规则分类与各网元职责（动态/预定义/预定义规则组/本地规则）、条件与动作、SDF定义 |
| 4 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/实现原理/业务流程_47013470.md` | PCC业务流程（PDU会话建立/修改/释放）、策略关联建立流程、安装与删除操作优先级规则 |
| 5 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/实现原理/Event Trigger_47013472.md` | 13种Event Trigger定义、含义与关联IE（PERIO/VOLTH/TIMTH/QUHTI/START/STOPT/DROTH/LIUSA/VOLQU/TIMQU/ENVCL/MACAR/EVETH） |
| 6 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/实现原理/2_3_4_5G PCC功能差异_47013471.md` | 2/3/4G与5G PCC差异对比（网元、接口、协议、策略类型、漫游、流程、规则来源、规则分类） |
| 7 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/激活PCC基本功能/配置动态PCC功能_74096530.md` | 动态PCC配置场景、规则分类（动态/预定义/预定义规则组）、配置步骤、参数说明、配置案例 |
| 8 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/激活PCC基本功能/配置本地PCC功能_74096529.md` | 本地PCC配置场景、与动态PCC差异、配置步骤、参数说明、配置案例 |
| 9 | `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/调测PCC基本功能_42369277.md` | 验证流程、License检查、配置一致性检查、N4接口消息验证、问题排查、信息收集 |
