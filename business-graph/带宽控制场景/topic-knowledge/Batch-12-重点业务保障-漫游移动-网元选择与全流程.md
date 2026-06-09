# Batch-12: 重点业务保障 — 漫游移动、网元选择与全流程

## 1. 概述

本批次覆盖"5G Core 重点业务保障解决方案"业务专题中信令流程描述部分的最后一批核心文档，聚焦三大主线：

1. **跨NWDAF服务区漫游与移动管理**：涵盖建设初期（部分区域未部署NWDAF或UPF未完成智能化改造）和建设完成（跨省漫游目标方案，源/目标NWDAF协作）两个阶段。建设初期以锚点NWDAF单网元管理TAI变更、区域进出和拜访地阈值保障为核心；建设完成阶段引入源NWDAF与目标NWDAF的双角色协作模型，实现分析服务跨省转移、质差数据转发与保障建议级联。

2. **网元选择机制**：涵盖SMF选择（部署前期AMF通过智能分流关键字"multidomain"发现智能SMF/PGW-C）、UPF选择（两种模式：基于PCF指示选择智能UPF、基于预定义规则选择UPF），以及网元选择概述（NF间服务发现的Model A/B/C/D统一视图）。

3. **端到端全流程与信令流程总览**：重点业务保障全流程图将前述所有机制串联为一张完整的端到端业务图景，信令流程描述章节首页明确了4G/5G双模支持的总体约束。

这些文档共同回答了"用户签约重点业务保障后，从会话激活、网元选择、质差检测、保障建议、专载创建到跨区域移动保障连续性"的完整生命周期问题。

---

## 2. 核心知识点

### 2.1 跨NWDAF服务区移动（建设初期）—— 锚点NWDAF单网元管理

**适用条件**：建设初期，部分区域未部署NWDAF或UPF未完成智能化改造。

**核心机制**：锚点NWDAF（即用户初始激活时PCF发现的NWDAF）始终负责该用户的质差保障分析，即使在用户移动后也不发生分析服务转移。关键差异在于根据用户当前TAI是否在锚点NWDAF的服务区域/TA区域内来动态调整保障策略。

**两类保障场景**：

- **用户移动至不支持保障的区域**：NWDAF取消质差分析事件订阅（QOS_ANA），仅保留TAI变更事件订阅（SAREA_CH）。如果当前已有N5保障，NWDAF向PCF发起删除N5保障消息。用户回到支持区域后，NWDAF重新订阅质差事件，恢复正常保障。
- **用户移出NWDAF pool但仍在配置TA区域内**：NWDAF采用本地配置的**拜访地GBR保障阈值**进行保障分析（通过软参"BYTE3 配置用户在拜访地使用GBR配额的阈值"设置），而非本地阈值（`SET QOSGUARCOND`命令配置的阈值）。

**关键判定路径**：
- 用户TAI在 `ADD NFTAI` / `ADD TAIRANGELIST` 配置范围内 → 正常保障（本地阈值）
- 用户TAI在 `ADD SRVTAI` / `ADD SRVTAIRANGE` 范围但不在 `ADD NFTAI` 范围 → 拜访地阈值保障
- 用户TAI都不在上述范围 → 取消质差订阅

**PCF侧SMF白名单控制**：PCF在发起N23订阅前判断用户初始接入的SMF是否在配置的支持保障SMF ID列表中。如果不在，即使后续用户移动至支持保障的区域也不会发起N23订阅，需在支持区域重新激活后才能正常保障。

### 2.2 跨NWDAF服务区移动（建设完成）—— 源/目标NWDAF双角色协作

**适用条件**：跨省漫游目标方案已部署，多省NWDAF协同工作。

**角色转换模型**：当用户移出锚点NWDAF（归属省NWDAF）的服务区域时，锚点NWDAF将自身角色切换为**源NWDAF**，通过用户最新TAI发现**目标NWDAF**（拜访省NWDAF），并将质差保障分析服务转移至目标NWDAF。

**核心分工**：
- **源NWDAF**（归属省）：负责与A-SMF/A-UPF交互（订阅质差数据、TAI变更、AMF ID变更），向PCF转发保障建议，向目标NWDAF转发质差数据
- **目标NWDAF**（拜访省）：负责质差保障决策分析（综合无线小区容量和负载），向源NWDAF输出保障建议

**信令交互链路（省际转移时）**：
1. 源NWDAF向目标NWDAF发送 `Nnwdaf_EventsSubscription_Subscribe`（POST），携带 QOS_ANALYSIS、appIds、源NWDAF ID（nwdafId信元）、关联标识
2. 目标NWDAF向源NWDAF发送 `Nnwdaf_DataManagement_Subscribe`（POST），订阅质差数据
3. 质差数据通过 `Nnwdaf_DataManagement_Notify` 从源NWDAF转发至目标NWDAF
4. 保障建议通过 `Nnwdaf_EventsSubscription_Notify` 从目标NWDAF传递至源NWDAF
5. 源NWDAF向PCF转发保障建议，PCF不感知跨省漫游流程
6. 保障结果通过 `Nnwdaf_EventsSubscription_Subscribe`（PUT）的 n5EvsNotif 信元从源NWDAF通知目标NWDAF

**AMF ID范围控制**：
- 关闭Always漫游开关 + AMF ID/省份白名单（`ADD ROAMSRVAMF` / `ADD ROAMSRVPROV`）：适用于支持NWDAF的省份较少时，减少无用信令
- 开启Always漫游开关 + AMF ID/省份黑名单（`ADD ROAMBLKAMF` / `ADD ROAMBLKPROV`）：适用于大部分省份都支持NWDAF时

### 2.3 跨省漫游六大场景

文档定义了六种完整的跨省漫游场景，构成保障连续性的全覆盖：

| 场景 | 描述 | 关键行为 |
|------|------|----------|
| 场景1 | 用户在归属省NWDAF服务区域内激活 | 典型非漫游场景，正常保障 |
| 场景2 | 从归属省移至省外NWDAF支持区域 | 源NWDAF转移分析至目标NWDAF |
| 场景3 | 在两个省外NWDAF服务区域连续移动 | 源NWDAF向新目标NWDAF转移，同时取消旧目标NWDAF |
| 场景4 | 从省外回到省内NWDAF服务区域 | 源NWDAF恢复自身NWDAF形态，取消目标NWDAF订阅 |
| 场景5 | 移至省外但无可用目标NWDAF | 取消质差及小区变更订阅，保留TAI/AMF ID变更订阅，等待后续移动至可用区域 |
| 场景6 | 用户在省外激活 | PCF根据锚点SMF ID是否在配置列表内决定是否下发N23订阅 |

**场景3的链式转移特征**：用户从省B移动至省C时，源NWDAF（省A）保持源形态不变，将分析从旧目标（省B）切换至新目标（省C），同时执行旧目标的取消订阅和新目标的订阅创建。这保证了一跳转移模式，不会因连续跨省而累积多层NWDAF链路。

### 2.4 跨省漫游对既有信令流程的影响

文档系统性地分析了跨省漫游对6类既有信令流程的影响：

| 流程 | 影响程度 | 变更要点 |
|------|----------|----------|
| 质差数据分析更新订阅 | 有变更 | 周期更新：源NWDAF通过PUT向目标NWDAF转发；appIds变更：涉及appId删除时需级联删除已创建的保障并刷新配额 |
| 质差数据分析去订阅 | 有变更 | 多了源NWDAF与目标NWDAF之间的取消订阅交互链路 |
| 采集质差数据 | 有变更 | UPF上报质差后，源NWDAF需转发给目标NWDAF，由目标NWDAF决策保障 |
| 采集小区资源数据 | 无影响 | 获取无线小区负载数据的网元为目标NWDAF，流程本身不变 |
| 采集用户实时位置 | 无影响 | 小区位置变更订阅仍由源NWDAF向A-SMF发起 |
| 新建/更新/删除保障建议 | 有变更 | 决策网元为目标NWDAF，结果通过Notify通知源NWDAF，再由源NWDAF向PCF转发 |

**小区GBR配额管理在跨省漫游中的行为**：当用户小范围移动（小区变更但不跨省），UPF向源NWDAF上报，源NWDAF转发至目标NWDAF，目标NWDAF刷新小区GBR保障配额（释放旧小区配额、增加新小区配额）。

### 2.5 网元选择概述 —— NF间服务发现统一视图

重点业务保障解决方案涉及多个NF间的寻址和选择场景，文档提供了统一的发现方式矩阵：

| 服务请求方 | 服务提供方 | 发现方式 | 关键信元 |
|-----------|-----------|----------|----------|
| PCF | NWDAF | Model A/B/D | tai（初始TAI）、eventId=QOS_ANALYSIS |
| NWDAF | SMF | Model A/B | smfid（PCF在N23请求中携带） |
| SMF | NWDAF | NA | SMF记录NWDAF的notifUri |
| SMF | UPF | 见UPF选择章节 | upfSelectRules（PCF下发） |
| UPF | NWDAF | NA | SMF通过N4的Event Notification URL携带 |
| NWDAF | PCF | Model A/B/D | target-nf-instance-id |
| 源NWDAF | 目标NWDAF | Model A/B/C/D | tai（最新TAI）、eventId=QOS_ANALYSIS |

**Model说明**：Model A为直接NRF查询；Model B为通过消费者缓存的服务发现；Model C为服务间接发现（通过NRF转发）；Model D为配置数据发现。

**源NWDAF→目标NWDAF是唯一使用Model C的场景**，反映了跨NWDAF发现需要间接寻址的特殊性。

### 2.6 SMF选择 —— 部署前期方案

**适用条件**：全省SMF未全部升级到配套版本时。当全省SMF都升级后，使用AMF基于DNN/切片的常规SMF选择方案即可。

**核心原理**：智能SMF复用智能分流SMF，AMF通过智能分流关键字"**multidomain**"发现并选择支持选择智能板UPF的SMF/PGW-C。

**关键步骤**：
1. UDM侧签约园区业务：通用DNN + 专用DNN（含"multidomain"关键字）
2. MME/AMF通过注册流程获取签约数据
3. 从专用DNN中解析"multidomain"关键字
4. 4G场景：MME基于通用DNN + "multidomain"构造APN域名，DNS解析智能分流PGW-C S5-C地址
5. 5G场景：AMF基于通用DNN通过NRF发现SMF，基于"multidomain"优选具有智能分流能力的SMF
6. MME/AMF在会话请求中携带通用DNN给智能分流SMF/PGW-C

### 2.7 UPF选择 —— 两种模式

**模式一：基于PCF指示选择智能UPF**

适用于正式部署方案，PCF通过N7接口直接控制SMF的UPF选择：

1. SMF向PCF发起策略创建请求
2. PCF根据用户签约信息，在 `Npcf_SMPolicyControlAPI_SmPolicyControlCreate_Response` 中下发 `upfSelectRules`，其中 `upfSelectId=select_ai_upf`，`reportInd=true`
3. SMF根据指示选择智能UPF
4. SMF通过 `Npcf_SMPolicyControlAPI_SmPolicyControlUpdate_Request` 上报选择结果（`upfSelectRuleReports`），`upfStatus=ACTIVE`（成功）或 `INACTIVE`（失败）
5. PCF根据上报结果决定是否下发重点业务保障订阅

**支持PDU会话建立后新签约业务**：PCF通过 `SmPolicyControlUpdateNotify` 消息下发UPF选择指示；若当前锚点UPF不满足条件，触发会话重建。

**支持签约业务取消**：PCF下发取消指示，向NWDAF取消订阅，但保持已选择的智能UPF至会话释放。

**模式二：基于预定义规则选择UPF**

1. PCF下发预定义规则（用户模板），例如 `testuserprofilename`
2. SMF将PCF下发的预定义规则名与本地配置的用户模板名匹配，匹配成功则选择智能UPF
3. SMF根据本地UPF选择规则（如 `rule1` 绑定 `QOSANA-1&QOSEXP-1`）和UPF-规则绑定关系选择候选UPF
4. SMF再根据容量等信息从候选中选择最终UPF
5. SMF在PFCP Session Modification Request的SRR IE中携带私有信元 `Qos_Analysis`

### 2.8 重点业务保障全流程 —— 端到端串联

重点业务保障全流程图将以上所有机制串联为一张端到端业务视图，完整覆盖：

```
用户签约重点业务保障
  ↓
PDU会话激活
  ↓
[网元选择阶段]
  ├─ SMF选择（部署前期：multidomain关键字；部署完成：常规选择）
  ├─ UPF选择（PCF指示 or 预定义规则）
  └─ PCF根据UPF选择结果决定是否下发保障订阅
  ↓
PCF发现NWDAF（基于初始TAI）→ N23 QoS_ANALYSIS订阅
  ↓
NWDAF向A-SMF订阅事件（SAREA_CH / SCNN_CH / QOS_ANA）
A-SMF通过N4转发给A-UPF
  ↓
[质差检测阶段]
  ├─ A-UPF检测质差并上报
  └─ NWDAF判断是否发起保障建议
  ↓
[保障执行阶段]
  ├─ NWDAF向PCF发起GBR保障建议
  ├─ PCF决策并创建专载
  └─ PCF通知NWDAF保障结果
  ↓
[移动保障阶段]
  ├─ 建设初期：锚点NWDAF动态调整（区域进出、拜访地阈值）
  ├─ 建设完成：源/目标NWDAF协作（分析转移、质差转发、建议级联）
  └─ 小区变更：GBR配额刷新（释放旧小区、分配新小区）
  ↓
[保障生命周期管理]
  ├─ 周期更新 / appIds变更
  ├─ 去订阅 / 专载删除
  └─ 签约取消 / 会话释放
```

### 2.9 4G/5G双模支持约束

信令流程描述章节首页明确了关键约束：本解决方案同时支持4G和5G用户的重点业务保障。以5G用户为例描述信令流程，4G用户的消息流程及信元描述一致，区别在于网元为融合形态（如SMF为SMF+PGW-C）。4G场景依赖UDC产品的 `SET NWDAFCTRL` 命令中"是否支持4G场景下质差保障及体验上报"参数配置。4G/5G切换场景有独立的业务流程处理。

---

## 3. 配置调测要点

### 3.1 NWDAF服务区域配置（UDC产品）

| MML命令 | 用途 | 说明 |
|---------|------|------|
| `ADD NFTAI` | 配置NWDAF支持的服务区域（NF级TA） | 决定NWDAF的"服务区域"范围 |
| `ADD TAIRANGELIST` | 配置TAI范围列表 | 与ADD NFTAI配合定义服务区域 |
| `ADD SRVTAI` | 配置NWDAF支持的TA区域 | 决定"TA区域"范围（比服务区域更宽） |
| `ADD SRVTAIRANGE` | 配置TA区域范围 | 与ADD SRVTAI配合 |
| `SET QOSGUARCOND` | 配置本地GBR保障条件/阈值 | 锚点NWDAF服务区域内使用 |
| `SET NWDAFCTRL` | NWDAF控制参数 | Always漫游开关、ROAMINGSW漫游目标方案开关、4G质差保障开关 |

### 3.2 跨省漫游AMF ID范围控制

| MML命令 | 用途 | 适用场景 |
|---------|------|----------|
| `ADD ROAMSRVAMF` | AMF ID白名单 | 支持省份少时，减少无用服务发现信令 |
| `ADD ROAMSRVPROV` | 省份白名单 | 同上，按省份粒度控制 |
| `ADD ROAMBLKAMF` | AMF ID黑名单 | 支持省份多时，排除少量不支持省份 |
| `ADD ROAMBLKPROV` | 省份黑名单 | 同上，按省份粒度排除 |

### 3.3 软参数控制

| 软参 | 作用 |
|------|------|
| DWORD1 BIT4 | 控制NWDAF收到PCF发起QoS分析订阅后是否向SMF订阅SAREA_CH事件 |
| DWORD1 BIT5 | 控制是否向SMF订阅SCNN_CH（服务CN节点内位置变更）事件 |
| BYTE3 | 配置用户在拜访地使用GBR配额的阈值（建设初期拜访地保障） |

### 3.4 PCF侧关键配置

- PCF需配置支持保障业务的SMF ID列表，决定是否发起N23订阅
- PCF通过 `upfSelectRules` 控制SMF选择智能UPF：`upfSelectId=select_ai_upf`，`reportInd=true`
- SMF上报结果通过 `upfSelectRuleReports` 信元：`upfStatus=ACTIVE/INACTIVE`

### 3.5 SMF侧预定义规则配置（模式二）

- SMF本地配置用户模板名称（如 `testuserprofilename`），与PCF下发的预定义规则匹配
- UPF选择规则（如 `rule1` 绑定 `QOSANA-1&QOSEXP-1`），定义规则与UPF能力绑定关系
- UPF-规则绑定关系（如 UPF1绑定rule1，UPF2绑定rule2）
- PFCP Session Modification Request的SRR IE中携带私有信元 `Qos_Analysis`

### 3.6 关键信令消息清单

| 接口 | 消息 | 用途 |
|------|------|------|
| Nsmf (N11) | Nsmf_EventExposure_Subscribe (POST/PUT) | NWDAF向SMF订阅/更新事件 |
| Nsmf (N11) | Nsmf_EventExposure_Notify | SMF向NWDAF通知事件（TAI/AMF ID变更、质差） |
| Nnwdaf | Nnwdaf_EventsSubscription_Subscribe (POST/PUT) | 源NWDAF向目标NWDAF订阅质差分析 |
| Nnwdaf | Nnwdaf_EventsSubscription_Notify | 目标NWDAF向源NWDAF发送保障建议 |
| Nnwdaf | Nnwdaf_EventsSubscription_Unsubscribe | 取消质差分析订阅 |
| Nnwdaf | Nnwdaf_DataManagement_Subscribe (POST/PUT) | 目标NWDAF向源NWDAF订阅质差数据 |
| Nnwdaf | Nnwdaf_DataManagement_Notify | 源NWDAF向目标NWDAF转发质差数据 |
| Nnwdaf | Nnwdaf_DataManagement_Unsubscribe | 取消质差数据订阅 |
| N7 (Npcf) | SmPolicyControlCreate_Response | PCF下发upfSelectRules |
| N7 (Npcf) | SmPolicyControlUpdate_Request | SMF上报upfSelectRuleReports |
| N7 (Npcf) | SmPolicyControlUpdateNotify | PCF向SMF下发UPF选择变更指示 |
| N5 (Npcf) | PolicyAuthorization_Delete | NWDAF向PCF删除保障建议/专载 |
| N4 (PFCP) | Session Modification Request | SMF向UPF下发订阅（SRR IE携带Qos_Analysis） |

### 3.7 关键事件类型

| 事件 | 含义 | 订阅时机 |
|------|------|----------|
| SAREA_CH | 服务区域位置变更（TAI变更） | 初始订阅时即订阅，用于NWDAF跟踪用户位置 |
| SCNN_CH | 服务CN节点内位置变更（AMF ID变更） | 建设完成方案新增，用于判断是否触发省际转移 |
| QOS_ANA | 质差分析事件 | 进入支持区域后订阅，离开支持区域时取消 |
| SCELL_CH | 小区变更事件 | 首条质差流后订阅，用于小区GBR配额管理 |

---

## 4. 与带宽控制的关系

本批次文档描述的重点业务保障机制与带宽控制场景存在深层的架构关联：

### 4.1 保障执行的物理基础

重点业务保障的核心执行手段是创建GBR专载（Guaranteed Bit Rate专用承载），这本质上就是一种**带宽保障机制**——为特定用户的特定业务流保证最低带宽。NWDAF的保障建议（N5接口）最终体现为PCF决策的GBR QoS参数下发，包括上下行GBR、MBR、5QI等参数，与带宽控制中的URR/PCC策略执行机制高度一致。

### 4.2 网元选择决定保障策略执行位置

- SMF选择决定会话锚定在哪个SMF（智能SMF vs 普通SMF）
- UPF选择决定质差检测和流量管控的执行点（智能UPF vs 普通UPF）
- 这直接影响带宽控制策略能否在该会话上生效——只有选择了支持QoS分析能力的智能UPF，才能实现基于质差反馈的动态带宽调整

### 4.3 漫游场景下的保障连续性

跨NWDAF服务区漫游（无论建设初期还是建设完成方案）解决的核心问题是：当用户移动到不同区域时，如何保持带宽保障策略的连续性。建设初期通过拜访地阈值实现降级保障；建设完成方案通过源/目标NWDAF协作实现完整保障。这对带宽控制场景中的跨区域策略一致性具有参考意义。

### 4.4 小区GBR配额管理与带宽资源管理

文档中反复出现的"小区GBR保障配额"概念——释放旧小区配额、分配新小区配额——本质上就是无线侧的带宽资源管理机制。目标NWDAF在决策保障时需要综合考虑无线小区的容量和负载，这与带宽控制中的承载资源分配逻辑直接相关。

### 4.5 PCC规则与保障建议的联动

PCF在保障建议场景中通过PCC规则创建专载，涉及GBR/MBR参数、5QI、ARP优先级等QoS参数。这些参数与带宽控制场景中PCCPOLICYGRP/PCCRULE配置的参数体系完全一致，说明两者共享底层的QoS执行框架。

---

## 5. 关键术语

| 术语 | 简释 |
|------|------|
| NWDAF | Network Data Analytics Function，网络数据分析功能。本方案中指NWDAF-FE（即UDC产品） |
| NWDAF服务区域 | NWDAF配置的支持保障的TA范围，通过 `ADD NFTAI` / `ADD TAIRANGELIST` 定义 |
| TA区域 | NWDAF配置的更宽泛的TA范围，通过 `ADD SRVTAI` / `ADD SRVTAIRANGE` 定义 |
| 锚点NWDAF | 用户初始激活时PCF发现的NWDAF，建设初期方案中始终由其负责保障分析 |
| 源NWDAF | 跨省漫游目标方案中，用户移出服务区域后锚点NWDAF切换的角色，负责与A-SMF/PCF交互 |
| 目标NWDAF | 跨省漫游目标方案中，用户拜访地的NWDAF，负责质差决策分析和保障建议生成 |
| A-SMF / A-UPF | 锚点SMF / 锚点UPF，用户初始激活时选定的SMF/UPF，后续移动不改变锚点 |
| N23接口 | PCF与NWDAF之间的接口，PCF通过该接口发起QoS_ANALYSIS分析订阅 |
| N5接口 | NWDAF与PCF之间的接口，NWDAF通过该接口向PCF发送保障建议 |
| SAREA_CH | Service Area Change，服务区域位置变更事件（TAI变更） |
| SCNN_CH | Serving CN Node Change，服务CN节点内位置变更事件（AMF ID变更） |
| QOS_ANA | QoS Analysis，质差分析事件，UPF检测到质差后上报 |
| SCELL_CH | Serving Cell Change，小区变更事件，用于小区GBR配额管理 |
| GBR保障 | Guaranteed Bit Rate保障，为核心业务流保证最低带宽的QoS机制 |
| 拜访地GBR阈值 | 用户移出锚点NWDAF服务区域但仍在TA区域内时，NWDAF使用的替代GBR阈值 |
| multidomain | 智能分流关键字，SMF选择方案中用于发现智能SMF/PGW-C |
| 智能UPF | 支持质差分析能力的UPF（含智能板），是重点业务保障的前提条件 |
| Model A/B/C/D | NRF服务发现的四种模式，分别表示直接查询、缓存查询、间接发现和配置数据发现 |
| ROAMINGSW | 漫游目标方案开关，`SET NWDAFCTRL` 命令参数 |
| Always漫游开关 | `SET NWDAFCTRL` 命令参数，控制是否默认进行服务发现（配合黑名单/白名单） |

---

## 6. 知识来源

| 序号 | 文件名 | 主题 |
|------|--------|------|
| 1 | 跨NWDAF服务区域移动（建设初期）_02770065.md | 建设初期跨NWDAF服务区移动的信令流程、话务统计、消息样例 |
| 2 | 跨省漫游关键业务流程_44655789.md | 建设完成方案跨省漫游的完整信令流程（26步）、错误码、消息样例 |
| 3 | 跨省漫游场景总览_09137018.md | 六大跨省漫游场景的业务逻辑总览（含图示） |
| 4 | 跨省漫游对信令流程的影响_09027092.md | 跨省漫游对6类既有信令流程的影响分析 |
| 5 | SMF选择_21725142.md | 部署前期AMF通过multidomain关键字选择智能SMF的方案 |
| 6 | 基于PCF指示选择智能UPF_91173900.md | PCF通过upfSelectRules指示SMF选择智能UPF的信令流程 |
| 7 | 基于预定义规则选择UPF_94646348.md | 基于PCF预定义规则和SMF本地模板匹配选择UPF的方案 |
| 8 | 网元选择概述_97571937.md | NF间服务发现的统一矩阵（Model A/B/C/D）和通信模式 |
| 9 | 重点业务保障全流程_88226505.md | 端到端重点业务保障全流程图（典型场景） |
| 10 | 信令流程描述_76819174.md | 信令流程描述章节首页，4G/5G双模支持约束 |
