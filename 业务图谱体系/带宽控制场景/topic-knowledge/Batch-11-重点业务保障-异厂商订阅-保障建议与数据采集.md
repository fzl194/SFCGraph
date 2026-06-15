# Batch-11 重点业务保障：异厂商PCF订阅、保障建议与数据采集

## 1. 概述

本批次涵盖"5G Core 重点业务保障解决方案"业务专题中信令流程描述部分的三大主题域，共10个文档：

| 主题域 | 文档数 | 核心内容 |
|--------|--------|----------|
| 异厂商PCF场景数据分析订阅 | 3 | 异厂商PCF场景下数据分析的订阅、更新订阅、去订阅全生命周期 |
| 数据分析结果开放与执行 | 4 | 保障建议的新建、更新、删除三态管理 + 数据分析结果开放总览 |
| 数据采集上报 | 3 | 小区资源数据采集、用户实时位置采集、质差数据采集三类感知机制 |

这三个主题域在重点业务保障解决方案中分别承担不同角色：数据采集是感知层（感知质差、负荷、位置），保障建议是决策执行层（NWDAF决策后通知PCF执行带宽保障），异厂商PCF订阅是控制信令链路（在异厂商PCF组网下建立数据分析订阅通道）。三者构成"采集感知 -> 分析决策 -> 保障执行"的端到端闭环。

---

## 2. 核心知识点

### 知识点1：异厂商PCF场景的组网架构与双PCF链路机制

异厂商PCF场景（也称大网PCF场景）是重点业务保障解决方案的一种部署模式。该场景下存在两个PCF角色：

- **异厂商PCF（大网PCF）**：负责标准N7策略控制（签约策略、计费规则下发），是PDU会话的原始策略控制方。
- **智能PCF（本厂商PCF/UDC侧PCF）**：负责与NWDAF对接，承载N23数据分析订阅和N5保障建议通道。

**双N7链路机制**：异厂商PCF在下发智能PCC Rule后，SMF根据本地预定义规则匹配，创建**第二条N7链路**连接到智能PCF。第一条N7链路连接异厂商PCF处理标准策略，第二条N7链路连接智能PCF处理数据分析订阅和保障信令。智能PCC Rule可能与大网Rule并存。

**与典型场景的关键差异**：
- 典型场景中PCF直接通过N23接口向NWDAF订阅数据分析。
- 异厂商PCF场景中，智能PCF作为中间代理，SMF通过第二条N7链路向智能PCF发送订阅信息，再由智能PCF通过N23接口向NWDAF转发。
- N5保障建议的目标PCF由订阅时携带的`subsPcfId`（异厂商PCF实例ID）决定，而非智能PCF自身。

### 知识点2：异厂商PCF场景订阅三阶段对比

| 维度 | 订阅 | 更新订阅 | 去订阅 |
|------|------|----------|--------|
| **触发条件** | 激活时异厂商PCF下发智能PCC Rule；或用户签约套餐变更后异厂商PCF新增智能PCC Rule | 订阅事件发生变化（异厂商PCF下发新PCC Rule绑定不同订阅事件）；或异厂商PCF故障后SMF重选PCF更新PCF ID | 用户去激活（会话释放）；套餐取消导致异厂商PCF删除智能PCC Rule |
| **SMF -> 智能PCF消息** | Npcf_SMPolicyControl_Create Request | Npcf_SMPolicyControl_Update Request（携带全量订阅事件） | Npcf_SMPolicyControl_Delete Request |
| **智能PCF -> NWDAF消息** | N23接口数据分析订阅 | N23接口数据分析更新订阅 | N23接口数据分析去订阅 |
| **关键信元** | subsPcfId、needN23Subs、Ipv4Address、Ipv6AddressPrefix、ipDomain | 全量订阅事件列表 | - |
| **后续流程** | 与典型场景订阅一致 | 与典型场景更新订阅一致 | 与典型场景去订阅一致 |

**订阅时机约束**：SMF必须在向异厂商PCF更新UE IP地址之后，才向智能PCF发起数据分析订阅。这是因为订阅需要携带用户IP地址（IPv4Address/IPv6AddressPrefix），UE IP必须在策略关联建立后才能获取。

**关键信元说明**：
- `subsPcfId`：当前管理PDU会话的异厂商PCF实例ID，通知NWDAF后续创建N5保障时保障消息发送的目标PCF。
- `needN23Subs`：需要触发N23订阅的事件，在SMF上通过ADD RULE命令配置。

### 知识点3：异厂商PCF故障处理机制

当异厂商PCF发生故障时，SMF收到N7接口的`504 Gateway Timeout`错误码，采取以下两种恢复策略之一：

1. **重选异厂商PCF**：完成选择后，SMF向智能PCF发起Npcf_SMPolicyControl_Update Request更新消息，携带最新的异厂商PCF ID。后续通过更新订阅流程将新PCF ID同步给NWDAF。
2. **回滚为LocalPCC**：SMF向智能PCF发起Npcf_SMPolicyControl_Delete Request，去订阅数据分析，退回到本地PCC模式。

**第二N7会话失败处理**：当SMF与智能PCF之间的第二条N7会话建立失败（消息超时或所有非2XX异常码）后，SMF不会重试建立或选择其他备用PCF。需要等待UE下次重新创建会话时，再尝试重建第二条N7会话。

### 知识点4：保障建议的三态生命周期

保障建议是NWDAF（UDC产品）向PCF发起的策略授权请求，通过N5接口（Npcf_PolicyAuthorization服务）实现，覆盖新建、更新、删除三个状态：

**新建保障建议**：

- **触发条件**：UPF检测到用户体验质差并上报NWDAF后，NWDAF综合分析满足保障条件。
- **决策方**：NWDAF发出建议，PCF最终决策是否创建专载保障。
- **消息流**：NWDAF通过N5接口发送`Npcf_PolicyAuthorization_Create_Request` -> PCF向SMF安装动态规则 -> SMF建立专载 -> PCF回复Create Response -> SMF通知规则安装成功 -> PCF向NWDAF发送Notify（携带mcResourcStatus=ACTIVE）。
- **QoS参数**：保障带宽由mirBwUl/mirBwDl（上下行保障带宽，即CIR/GBR）和marBwUl/marBwDl（上下行最大带宽，即PIR/MBR）定义，取值来源为基于智能码率识别的保障建议配置。

**更新保障建议**：

- **触发条件**：UPF持续监测用户业务质量，检测到流变更场景（新增质差流、流结束、新应用质差等）。
- **流变更场景分类**（6种场景）：

| 场景 | 描述 | NWDAF未触发保障时 | NWDAF已触发保障时 |
|------|------|-------------------|-------------------|
| 场景1 | 已有subAppId有非首条主流质差 | 合并重新判断，满足则Create | Update消息，mirBwUl/mirBwDl置0（同应用新增流GBR不叠加） |
| 场景2 | 已有appId下有新subAppId主流质差 | 合并重新判断，满足则Create | Update消息，GBR/MBR携带新subAppId配置值（不同subAppId预期独占GBR） |
| 场景3 | 新appId下有subAppId主流质差 | 合并重新判断，满足则Create | Update消息，GBR/MBR携带新subAppId配置值 |
| 场景4 | 对应subAppId流未全部结束 | 对未结束流重新判断 | Update消息删除流（fStatus=REMOVED），不回收GBR |
| 场景5 | 对应subAppId流已全结束，同appId下其他subAppId流未结束 | 对未结束流重新判断 | Update消息删除流，需回收GBR |
| 场景6 | 对应appId下所有subAppId流已结束，其他appId流未结束 | 对未结束流重新判断 | Update消息删除流，需回收GBR |

- **更新消息**：`Npcf_PolicyAuthorization_Update_Request`（PATCH方法，content-type: application/merge-patch+json）

**删除保障建议**：

- **触发条件**（5种）：

| 触发条件 | 说明 |
|----------|------|
| PCF通知保障失败 | 携带原因值FAILED_RESOURCES_ALLOCATION、PDU_SESSION_TERMINATION、ALL_SDF_DEACTIVATION |
| NWDAF判断无效保障 | 根据保障建议判断条件中的会话级阻塞条件判定 |
| UPF上报流结束 | subappStatus=TERMINATED，受SET QOSGUARTIMER的"N5会话延迟删除时长(秒)"控制是否延时释放 |
| NWDAF老化超时 | 超过SET QOSGUARTIMER的"Nupf会话老化时长(分钟)"未收到UPF消息 |
| 用户切换小区资源不足 | 新小区资源不足时停止保障并刷新原小区配额 |

- **消息流**：NWDAF发送`Npcf_PolicyAuthorization_Delete_Request`（POST方法，URI含/delete）-> PCF释放N5会话 -> 回复204 No Content。
- **配额管理**：删除保障时NWDAF同时刷新小区使用的配额。

### 知识点5：保障建议消息关键信元

**Create消息关键信元**：

| 信元 | 说明 |
|------|------|
| supis / ueIpv4 / ueIpv6 / ipDomain | 用户标识信息。PCF用ueIpv4/ueIpv6和ipDomain绑定N5会话和N7会话。通过软参DWORD1 BIT10和BIT11控制仅携带IPv4、仅IPv6或两者同时携带 |
| afAppId | 保障业务标识，一个afAppId表示一个业务大类（如视频直播类） |
| fDescs / fNum | 保障流描述信息和流编号 |
| mirBwUl / mirBwDl | 上下行保障带宽（GBR/CIR） |
| marBwUl / marBwDl | 上下行最大带宽（MBR/PIR） |
| n23subscriptionId | NWDAF分配的订阅ID，用于N23和N5会话关联。异厂商PCF场景不携带该信元 |
| events | NWDAF向PCF订阅的保障结果通知事件（SUCCESSFUL_RESOURCES_ALLOCATION、FAILED_RESOURCES_ALLOCATION等） |
| X-AF-Charging-Identifier | 计费标识，携带配置的RG（Rating Group）。采用保障流量独立计费方案时才携带。PCF将RG下发SMF，SMF包装为URR发送UPF |

**保障带宽的智能码率来源**：mirBwUl/mirBwDl和marBwUl/marBwDl的取值来源于"基于智能码率识别的保障建议"，即根据用户实际业务码率动态确定保障带宽，而非固定配置。

### 知识点6：数据分析结果开放与执行总览

NWDAF支持在生成分析结果后，将分析结果反馈给两类对象：

1. **分析服务使用者**：发起分析订阅/请求的网元（如PCF通过N23订阅NWDAF分析结果）。
2. **目标使用者**（Notification Target Address）：指定的通知目标地址。

数据分析结果的开放是保障建议的前提：NWDAF收到UPF质差上报后进行分析，生成分析结果，在满足保障条件时向PCF开放保障建议（即数据分析结果的执行）。

### 知识点7：数据采集三类对比

重点业务保障解决方案的数据采集分为三类，分别通过不同网元和接口获取：

| 维度 | 小区资源数据采集 | 用户实时位置采集 | 质差数据采集 |
|------|------------------|------------------|--------------|
| **数据来源** | RAN-OAM -> UDN -> UDC(NWDAF) | UPF -> NWDAF（触发SMF->AMF获取） | UPF -> NWDAF |
| **接口/协议** | SFTP/FTP获取原始数据；Nudn_DataManagement接口获取分析结果 | Nsmf_EventExposure接口订阅SCELL_CH事件；N4接口传递位置 | Nupf_EventExposure接口上报QOS_ANA事件 |
| **采集方式** | 周期性拉取 | 事件触发订阅 | 事件触发上报 |
| **数据内容** | 小区容量（上下行）、小区PRB利用率（上下行） | 用户当前所在小区NCGI | 质差事件、流结束事件、小区变更事件 |
| **触发条件** | UDC周期性向UDN请求，周期由SET UDNCTRL参数控制 | NWDAF收到UPF首条质差流后触发 | UPF检测到订阅事件（质差、流结束、小区变更） |
| **关键参数/命令** | SET UDNCTRL（小区容量有效时长、PRB利用率有效时长） | SET SMCOMMFUNC的LOCATIONCHSW、ADD APN的EXPOSURELOCRPT | SET VVIPBASICFUNC（质差上报周期，默认5秒） |

### 知识点8：小区资源数据采集机制详解

小区资源数据采集是保障决策的基础数据之一，用于判断目标小区是否有足够资源发起业务保障。

**数据流路径**：RAN-OAM --> UDN（SFTP Client获取原始无线统计数据）--> UDC/NWDAF（通过Nudn接口获取分析结果）

**UDN数据处理**：
- UDN通过SFTP/FTP协议从RAN-OAM获取上下行PRB可用数、上下行使用的PRB数量、上下行使用的GBR带宽等无线统计数据。
- UDN对小区信息进行训练，预测小区容量和小区负载情况。

**UDC拉取机制（Nudn_DataManagement接口）**：

| 获取内容 | 请求信元 | 响应信元 | 周期控制 |
|----------|----------|----------|----------|
| 小区容量 | nwdafCellCapacity（携带plmnId和nrCell_Id） | cell_CapacityInfos（含cellUpLinkCapacity、cellDownLinkCapacity） | SET UDNCTRL"小区容量有效时长(分钟)" |
| PRB利用率 | nwdafCellPrb（携带plmnId和nrCell_Id） | cell_PrbInfos（含cellUpLinkPrb、cellDownLinkPrb） | SET UDNCTRL"小区PRB利用率有效时长(分钟)" |

**有效期机制**：UDC从向UDN获取到数据开始计时，当需要使用该数据且超出有效时长时，重新向UDN获取。这是一种按需刷新机制，而非固定周期轮询。

**故障处理**：UDN主备切换后，UDC请求发到UDN备节点时返回`401 Unauthorized`。

### 知识点9：用户实时位置采集机制详解

用户实时位置采集用于在发起保障时确认用户所在小区，以便检查小区资源是否充足。

**触发条件**：NWDAF收到UPF上报的用户首条质差流后，通过Nsmf_EventExposure_Subscribe向SMF发起SCELL_CH事件订阅。

**位置获取链路**：NWDAF --> SMF（Nsmf订阅SCELL_CH）--> AMF（SMF向AMF订阅实时位置）--> SMF（AMF上报位置变更）--> UPF（N4接口传递位置）--> NWDAF（UPF通过Nupf_EventExposure_Notify上报）

**关键信元**：
- 订阅消息：event=SCELL_CH，订阅用户实时位置。SMF向NWDAF发送的订阅更新消息携带包含SCELL_CH事件的全量事件。
- 上报消息：userLocationInfo，用户位置信息。

**去订阅时机**：当用户流结束时（UPF上报结束流消息），NWDAF向SMF发起更新订阅，携带除SCELL_CH事件外的其他必须事件，SMF随之向AMF下发位置去订阅。

**License与开关依赖**：SMF向NWDAF上报用户实时位置功能依赖两个条件之一：
- 基于实时位置信息的策略控制功能License
- 实时位置上报开关：SET SMCOMMFUNC的LOCATIONCHSW参数和ADD APN的EXPOSURELOCRPT参数

当上述条件有一个不支持时，SMF向NWDAF返回`500 Internal Server Error`，携带应用原因为INSUFFICIENT_RESOURCES。

**补充路径**：当SMF上开启向NWDAF上报NCGI变更通知时，SMF也会直接向NWDAF上报用户实时位置，不依赖UPF转发。

### 知识点10：质差数据采集机制详解

质差数据采集是保障决策的直接触发源，UPF作为业务质量感知点向NWDAF上报质差事件。

**订阅前置**：PCF向NWDAF下发重点业务保障订阅后，NWDAF通过SMF向UPF下发保障订阅。UPF收到订阅后开始实时监测。

**UPF上报三类事件**：

| 上报场景 | 触发条件 | 上报行为 |
|----------|----------|----------|
| 应用质差 | UPF判断用户业务出现质差 | 立刻通知NWDAF；无论是否保障，持续周期性上报（默认5秒，SET VVIPBASICFUNC配置） |
| 业务流结束 | 应用中的业务流结束 | 上报结束信息，携带subAppStatus=TERMINATED |
| 用户位置变更 | 上报过质差的用户小区发生变化 | 立刻上报最新小区信息（appId为空，subAppQosMonReport为空） |

**infoIndicate信元的分支逻辑**：
- `QOS_ANA`：质差上报。UDC进入重点业务保障申请小区配额和建立保障流程，同时向UDN转发该信元。
- `QOS_EXP`：体验上报。UDC直接向UDN转发该信元，不进入重点业务保障流程。

**Nupf_EventExposure_Notify关键信元**：

| 信元 | 说明 |
|------|------|
| correlationId | NWDAF的通知关联号 |
| notificationItems.timeStamp | 事件发生时间 |
| notificationItems.ueIpv4Addr / ueIpv6Prefix | 用户IP地址 |
| notificationItems.snssai / dnn | 切片信息 / APN |
| qosAnaInfo.subAppQosQuality | 应用级是否质差，QOE_QUALITY1=用户体验差 |
| qosAnaInfo.flowQosDescs | 流描述信息 |
| qosAnaInfo.subAppStatus | 子应用状态，RUNNING / TERMINATED |
| qosAnaInfo.appId / subAppId | 应用ID（如live直播）/ 子应用ID（如tiktok_live） |
| qosAnaInfo.infoIndicate | 质差上报(QOS_ANA) / 体验上报(QOS_EXP) |
| qosAnaInfo.subAppQosMonReport | 子应用级KPI数据（上下行带宽、时延、丢包数和总包数） |
| qosAnaInfo.5qi | QosFlow的5QI，未使能上报QCI时UPF上报为0 |
| qosAnaInfo.userLocationInfo | 用户当前小区信息 |

**错误码特殊处理**：当UPF收到NWDAF返回的`404 Not Found`，UPF认为该NWDAF故障，删除该NWDAF创建的所有质差订阅信息。

---

## 3. 配置调测要点

### 3.1 关键MML命令

| 产品 | 命令 | 用途 |
|------|------|------|
| UDC | SET UDNCTRL | 配置小区容量有效时长(分钟)、小区PRB利用率有效时长(分钟) |
| UDC | SET QOSGUARTIMER | 配置N5会话延迟删除时长(秒)、Nupf会话老化时长(分钟) |
| UDG | SET VVIPBASICFUNC | 配置质差上报周期（默认5秒） |
| SMF(UNC) | ADD RULE | 配置needN23Subs需要触发N23订阅的事件 |
| SMF(UNC) | SET SMCOMMFUNC | 配置LOCATIONCHSW（实时位置上报开关） |
| SMF(UNC) | ADD APN | 配置EXPOSURELOCRPT（实时位置上报APN级开关） |
| SMF(UNC) | SET PFCPPVEXT | 配置QCI参数（是否使能向UPF上报QCI） |

### 3.2 关键信令消息

**异厂商PCF订阅链路**：

| 消息 | 接口 | 方向 | 用途 |
|------|------|------|------|
| Npcf_SMPolicyControl_Create Request | N7 | SMF -> 智能PCF | 发起数据分析订阅 |
| Npcf_SMPolicyControl_Update Request | N7 | SMF -> 智能PCF | 发起数据分析更新订阅 |
| Npcf_SMPolicyControl_Delete Request | N7 | SMF -> 智能PCF | 发起数据分析去订阅 |
| Nnwdaf_AnalyticsSubscription | N23 | 智能PCF -> NWDAF | NWDAF数据分析订阅/更新/去订阅 |

**保障建议链路**：

| 消息 | 接口 | 方向 | 用途 |
|------|------|------|------|
| Npcf_PolicyAuthorization_Create Request | N5 | NWDAF -> PCF | 新建保障建议（POST /app-sessions） |
| Npcf_PolicyAuthorization_Update Request | N5 | NWDAF -> PCF | 更新保障建议（PATCH /app-sessions/{id}） |
| Npcf_PolicyAuthorization_Delete Request | N5 | NWDAF -> PCF | 删除保障建议（POST /app-sessions/{id}/delete） |
| Npcf_PolicyAuthorization_Notify Request | N5 | PCF -> NWDAF | 保障结果通知（资源分配成功/失败/会话终止） |

**数据采集链路**：

| 消息 | 接口 | 方向 | 用途 |
|------|------|------|------|
| Nudn_DataManagement_Retrieval Request | Nudn | UDC -> UDN | 获取小区容量/PRB利用率 |
| Nsmf_EventExposure_Subscribe | Nsmf | NWDAF -> SMF | 订阅SCELL_CH事件（用户实时位置） |
| Nupf_EventExposure_Notify Request | Nupf | UPF -> NWDAF | 上报质差/流结束/小区变更事件 |

### 3.3 关键检查点

1. **N7第二会话建立检查**：N7接口当前在线的智能会话数（测量指标1929469721），确认第二条N7链路是否成功建立。
2. **N5会话状态检查**：N5接口当前在线的订阅会话数（测量指标1916338219），确认保障建议是否成功创建。
3. **N5会话成功率**：策略授权创建请求次数(1916338182) vs 成功次数(1916338183)，关注400/403/500/503/504错误码分布。
4. **小区资源获取检查**：NWDAF向CloudUDN获取小区容量/PRB利用率请求次数(1916338222/1916338224) vs 成功次数(1916338223/1916338225)，关注401错误码（UDN主备切换）。
5. **质差上报检查**：NWDAF接收UPF的QOS_ANA事件通知次数(1916338199)，细分为流质差(1916338200)、流结束(1916338202)、小区变更(1916338203)。
6. **SCELL_CH订阅检查**：SMF接收SCELL_CH订阅更新请求次数(1929445705 N11 / 1929445731 N16a)，关注500错误码（License/开关不支持）。
7. **保障结果通知检查**：NWDAF接收PCF通知中资源分配成功(1916338189) vs 失败(1916338190)，资源分配失败触发保障建议删除。

### 3.4 常见故障排查

| 故障现象 | 可能原因 | 排查方向 |
|----------|----------|----------|
| 第二条N7会话建立失败 | 智能PCF不可达、预定义规则未匹配 | 检查SMF预定义规则配置、智能PCF服务状态 |
| N5保障建议被PCF拒绝(403) | afAppId本地未匹配、N5会话数达License上限 | 检查PCF侧业务标识配置、License资源 |
| N5保障建议被PCF拒绝(500) | 无可绑定的N7会话 | 检查PCF是否收到对应的N7会话创建 |
| 小区容量获取失败(401) | UDN主备切换 | 检查UDN主备状态，确认请求发到主节点 |
| 实时位置获取失败(500) | License不支持或开关未开启 | 检查SET SMCOMMFUNC LOCATIONCHSW、ADD APN EXPOSURELOCRPT |
| UPF删除NWDAF全部订阅 | NWDAF返回404 | NWDAF服务状态检查、订阅信息是否丢失 |

---

## 4. 与带宽控制的关系

本批次文档描述的信令流程和数据采集机制，是带宽控制场景中"智能保障"链路的完整技术实现：

### 4.1 感知层：质差感知驱动带宽保障

质差数据采集是整个保障流程的起点。UPF作为业务质量感知点，实时监测用户业务质量（通过subAppQosMonReport中的上下行带宽、时延、丢包率等KPI）。当检测到质差（QOE_QUALITY1）时触发保障链路。带宽控制场景中的"带宽不足导致体验差"问题，正是通过这一机制被感知和触发处理的。

### 4.2 决策层：保障建议中的带宽参数

保障建议（Npcf_PolicyAuthorization_Create/Update）中携带的QoS参数直接实现了带宽控制：
- **mirBwUl/mirBwDl**（上下行保障带宽/CIR/GBR）：保障用户至少获得的带宽，对应带宽控制中的"保障带宽"。
- **marBwUl/marBwDl**（上下行最大带宽/MBR/PIR）：限制用户最大可用带宽，对应带宽控制中的"限速带宽"。
- **智能码率识别**：保障带宽取值基于智能码率识别，即根据用户实际业务码率动态确定，而非固定配置。这是带宽控制从静态配置向动态智能保障演进的关键。
- **GBR叠加规则**：同一应用新增流时mirBw置0（GBR不叠加）；不同subAppId预期独占GBR（携带新配置值）。这是带宽控制中多流带宽管理的重要规则。

### 4.3 控制信令层：异厂商PCF场景的策略下发路径

在异厂商PCF场景中，带宽控制的策略下发路径更为复杂：
- 标准策略（计费、签约QoS）通过第一条N7链路（异厂商PCF）下发。
- 智能保障策略（动态保障带宽、专载建立）通过第二条N7链路（智能PCF）+ N5接口（NWDAF->PCF）下发。
- N5保障建议的目标PCF是异厂商PCF（由subsPcfId指定），保障执行由异厂商PCF向SMF安装动态规则完成。

### 4.4 资源管理层：小区资源与带宽保障的联动

小区资源数据采集是带宽保障能否执行的前提条件：
- NWDAF在发起保障前必须检查目标小区的容量和PRB利用率，判断是否有足够资源。
- 用户切换小区时，新小区资源不足会导致保障删除（停止保障并刷新原小区配额）。
- 小区资源数据通过UDN的预测模型获取（非实时原始数据），存在有效期机制，过期需重新获取。

### 4.5 整体闭环

```
UPF质差感知 (质差数据采集)
    |
    v
NWDAF分析决策 (数据分析结果开放)
    |
    +-- 检查小区资源 (小区资源数据采集)
    +-- 检查用户位置 (用户实时位置采集)
    |
    v
NWDAF发起保障建议 (新建/更新保障建议, 携带带宽参数)
    |
    v
PCF决策执行 -> SMF安装动态规则 -> 专载建立
    |
    v
UPF执行带宽保障 (GBR/MBR限速)
    |
    v
UPF持续监测 -> 质差持续/流变更/流结束 (更新保障建议)
    |
    v
保障结束 (删除保障建议, 释放资源, 刷新配额)
```

---

## 5. 关键术语

| 术语 | 全称/解释 |
|------|-----------|
| NWDAF | Network Data Analytics Function，网络数据分析功能。本文档中指NWDAF-FE，即UDC产品 |
| UDC | User Data Convergence，UDC产品，承担NWDAF-FE角色，负责数据分析、决策和保障建议 |
| UDN | CloudUDN，云化用户数据网络，承担NWDAF的数据训练和预测（如小区容量预测） |
| 智能PCF | 本厂商PCF（UDC侧），在异厂商PCF场景中作为N23/N5通道代理 |
| 异厂商PCF | 大网PCF，负责标准N7策略控制，是PDU会话的原始策略控制方 |
| N5接口 | PCF与AF（NWDAF作为AF角色）之间的Npcf_PolicyAuthorization服务接口，用于保障建议下发 |
| N7接口 | SMF与PCF之间的Npcf_SMPolicyControl服务接口，用于策略控制 |
| N23接口 | PCF与NWDAF之间的数据分析订阅接口 |
| Nudn接口 | UDC(NWDAF)与UDN之间的数据管理接口，用于获取小区资源分析结果 |
| Nupf接口 | UPF事件开放接口，UPF通过该接口向NWDAF上报质差等事件 |
| Nsmf接口 | SMF事件开放接口，NWDAF通过该接口向SMF订阅事件（如SCELL_CH） |
| 保障建议 | NWDAF向PCF发起的策略授权请求，建议对质差用户进行专载带宽保障 |
| 专载 | Dedicated Bearer/QoS Flow，为特定业务流建立的保证比特率承载 |
| GBR | Guaranteed Bit Rate，保证比特率，对应mirBwUl/mirBwDl |
| MBR | Maximum Bit Rate，最大比特率，对应marBwUl/marBwDl |
| afAppId | Application Function Application Identifier，保障业务标识（业务大类） |
| subAppId | 子应用标识（如抖音直播），用于流级粒度管理 |
| SCELL_CH | SCell Change事件，用户实时位置（小区）变更事件 |
| QOS_ANA | QoS Analysis事件类型，UPF向NWDAF上报的质差分析事件 |
| QOE_QUALITY1 | 用户体验差的标识值，UPF判断用户业务出现质差时使用 |
| PRB | Physical Resource Block，物理资源块，小区无线资源利用率的度量单位 |
| NCGI | NR Cell Global Identifier，5G小区全局标识 |
| RAN-OAM | Radio Access Network Operations Administration and Maintenance，无线接入网操作维护管理 |
| 智能PCC Rule | 异厂商PCF下发的特殊PCC规则，SMF据此匹配预定义规则并创建第二条N7链路到智能PCF |
| LocalPCC | 本地PCC模式，异厂商PCF故障回滚时使用的本地策略控制模式 |

---

## 6. 知识来源

本知识文档融合提炼自以下10个产品文档：

| 序号 | 文件名 | 主题域 |
|------|--------|--------|
| 1 | 异厂商PCF场景数据分析去订阅_89667528.md | 异厂商PCF场景订阅 |
| 2 | 异厂商PCF场景数据分析更新订阅_89507680.md | 异厂商PCF场景订阅 |
| 3 | 异厂商PCF场景数据分析订阅_89667540.md | 异厂商PCF场景订阅 |
| 4 | 删除保障建议_24818325.md | 保障建议 |
| 5 | 新建保障建议_24818333.md | 保障建议 |
| 6 | 更新保障建议_24938209.md | 保障建议 |
| 7 | 数据分析结果开放与执行_24818357.md | 数据分析结果开放（总览） |
| 8 | 采集小区资源数据_24818341.md | 数据采集上报 |
| 9 | 采集用户实时位置_48275154.md | 数据采集上报 |
| 10 | 采集质差数据_24938237.md | 数据采集上报 |

**原始路径前缀**：`output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/信令流程描述/`

**相关文档引用**（文中提及但不在本批次范围内）：
- 典型场景数据分析订阅_24938205.md（典型场景订阅流程参考）
- 典型场景数据分析更新订阅_76978878.md（典型场景更新订阅流程参考）
- 典型场景数据分析去订阅_24818321.md（典型场景去订阅流程参考）
- 重点业务保障管理_76819142.md（保障判断条件原理）
- 基于智能码率识别的保障建议_46646592.md（保障带宽取值来源）
- 小区容量评估和负载预测_24938257.md（UDN预测模型）
- 重点业务保障解决方案的计费原理_19118572.md（保障流量独立计费）
- 保障建议判断条件_46822962.md（无效保障判断条件）
