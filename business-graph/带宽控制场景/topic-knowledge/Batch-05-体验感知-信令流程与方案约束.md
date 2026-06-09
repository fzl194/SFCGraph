# Batch-05: 5G Core体验感知 - 信令流程与方案约束

> **主题**: 体验感知信息采集→分析→带宽策略调整的信令流程链路
> **产品**: UDG (用户面)
> **批次**: Batch-05
> **源文档数**: 10

---

## 1. 文档概述

### 1.1 方案介绍

体验感知解决方案为运营商提供三类用户群的业务体验信息采集能力，支持按需订阅，通过用户面业务感知识别用户应用级的体验信息，将其开放给运营商的BOSS/SFTP服务器系统，为运营商提升用户体验提供数据支撑。

**三类用户群及采集场景对比**:

| 场景 | 订阅路径 | 上报路径 | 订阅事件 |
| --- | --- | --- | --- |
| 保障用户体验感知信息采集 | PCF -> NWDAF(UDC) -> SMF -> UPF 基于用户会话级订阅 | UPF -> NWDAF(UDC) -> NWDAF(UDN) -> BOSS/SFTP服务器 | QOS_ANALYSIS |
| 重点用户体验感知信息采集 | PCF -> NWDAF(UDC) -> SMF -> UPF 基于用户会话级订阅 | UPF -> NWDAF(UDN) -> BOSS/SFTP服务器 | QOS_EXP_ANALYSIS |
| 普通用户体验感知信息采集 | NWDAF(UDN) -> UPF 设备级用户抽样订阅 | UPF -> NWDAF(UDN) -> BOSS/SFTP服务器 | QOS_EXP |

**用户体验KPI指标**: 子应用级（例如抖音直播）用户体验相关的统计指标，包含上下行带宽、时延、丢包数和总包数。

**三类用户定义**:
- **重点业务保障用户**（简称保障用户）: 签约重点业务保障套餐的用户。需先部署重点业务保障解决方案，才能采集保障用户的体验感知信息。
- **重点用户**: 签约了业务体验感知套餐的重点用户，例如全球通套餐用户。
- **普通用户**: 除以上两种外，被抽样中的用户。根据配置抽样率进行用户抽样采集。

### 1.2 异厂商PCF场景概述

当运营商组网中已存在异厂商PCF时，部署华为体验感知解决方案需插入一对华为智能PCF完成数据分析订阅等智能业务。原异厂商PCF负责大网PCC策略等功能。

异厂商PCF场景的核心机制:
- 异厂商PCF在用户激活或套餐变更时，通过N7接口消息将预定义规则（智能PCC Rule）下发给SMF
- SMF根据预定义规则绑定的分析事件向智能PCF发起订阅
- 智能PCF通过N23接口向NWDAF发起订阅
- 后续订阅流程与上报流程与现网仅部署智能PCF场景（典型场景）相同

### 1.3 典型场景组网与接口

组网中实现体验感知解决方案业务功能的关键网元包括: PCF、NWDAF（分UDC和UDN）、SMF、UPF、NRF、BOSS/SFTP服务器。

**关键接口能力**:

| 通信NF | 接口 | 协议 | 功能 | 标准 |
| --- | --- | --- | --- | --- |
| PCF <-> NWDAF(UDC) | N23 | HTTP/2 + TLS | PCF调用NWDAF的EventsSubscription服务，获取体验感知分析功能 | 3GPP TS 29.520 |
| NWDAF(UDC) <-> SMF | Nsmf | HTTP/2 + TLS | NWDAF调用SMF的EventExposure服务，发送体验感知分析事件订阅 | 3GPP TS 29.508 |
| UPF <-> NWDAF(UDC) | Nupf | HTTP/2 + TLS | UPF向NWDAF通知已订阅用户业务体验监测信息 | 3GPP TS 29.564 |
| NWDAF(UDC) <-> NWDAF(UDN) | Nudn | HTTP/2 + TLS | UDC向UDN转发重点业务保障用户的体验数据 | 私有协议 |
| SMF <-> UPF | N4 | PFCP + GTP-U | SMF通过PFCP Session Modification Request消息中SRR携带私有信元下发业务体验分析等事件信息 | 3GPP TS 29.244 |
| NWDAF(UDN) <-> BOSS | - | SFTP | UDN向BOSS系统上报体验数据 | RFC 114/RFC 4253 |
| UPF <-> NWDAF(UDN) | - | 私有协议(UDP承载) | UPF向UDN上报重点用户及普通用户的体验数据 | 私有协议 |
| UPF <-> NWDAF(UDN) | Nupf | HTTP/2 + TLS | UDN通过此接口向UPF订阅普通用户的体验数据 | 私有协议 |

**NWDAF双角色说明**:
- **NWDAF(UDC)**: 即NWDAF-FE（前端），负责接收PCF的N23订阅、向SMF发起Nsmf订阅、接收UPF的保障用户体验数据并转发给UDN
- **NWDAF(UDN)**: 即NWDAF CloudUDN，负责接收普通用户订阅任务配置、向UPF下发设备级抽样订阅、接收重点/普通用户体验数据、向BOSS上报单据

---

## 2. 核心知识点：信令流程

### 2.1 普通用户体验感知信息采集流程

**业务场景**: 对普通用户进行体验感知信息采集。PCF不参与普通用户流程，订阅直接由NWDAF(UDN)向UPF发起。

**订阅与上报信令流程**:

1. **订阅下发**: 在NWDAF(UDN)上创建普通用户订阅任务，配置体验单据抽样率、订阅有效时长、dnn、snssai、app、ratType和备UDN南向接入IP地址。

2. **Nupf订阅**: UDN通过`Nupf_EventExposure_Subscribe Request`消息向UPF下发设备级普通用户的体验感知订阅。关键信元:

| 信元名称 | 信元解释 |
| --- | --- |
| nfId | UDN的NF实例标识 |
| type | 订阅类型，当前流程为QOS_EXP |
| dnn | 订阅的dnn信息，通过OM配置获取，未配置则不过滤（所有dnn都上报） |
| snssai | 订阅的snssai信息，通过OM配置获取，未配置则不过滤（所有snssai都上报） |
| appIds | 业务标识，可同时监控多个业务id，一个appId表示一个业务大类（如视频直播类），通过UDN侧OM配置获取 |
| reportingUrgency | UPF向UDN上报普通用户体验数据的频率 |
| sessRatio | 上报普通用户体验单据的抽样率，通过UDN侧OM配置获取 |
| ratType | 订阅的制式，通过UDN侧OM配置获取 |
| mainReportIpList | 主UDN上的Collector IP列表，通过UDN侧OM配置获取 |
| slaveReportIpList | 备UDN上的Collector IP列表，通过UDN侧OM配置获取 |

3. **体验数据上报**: UPF在感知到订阅事件发生后，通过与UDN之间的NupfR接口（私有协议，UDP承载），向主UDN上报普通用户的体验数据。

4. **单据生成与推送**: UDN将单据生成用户所需格式，通过SFTP协议发送给BOSS/SFTP服务器。

5. **去订阅**: 在UDN上删除订阅任务后，UDN向UPF取消订阅。

**话务统计指标**:
- P1: NWDAF向UPF发送的事件订阅请求次数（指标ID 1916338407）
- P2: NWDAF接收UPF的事件订阅成功次数（指标ID 1916338408）
- P3: NWDAF向BOSS上报体验单据成功的文件个数（指标ID 1916338410）

### 2.2 重点用户体验感知信息采集流程

**业务场景**: 对重点用户进行体验感知信息采集。本流程中描述的PCF均为智能PCF。

**与保障用户流程的核心区别**: 订阅事件不同。保障分析订阅事件为`QOS_ANALYSIS`，体验分析订阅事件为`QOS_EXP_ANALYSIS`。

#### 2.2.1 订阅流程

1. **PCF向NWDAF订阅（N23接口）**:
   - PCF在用户激活时，根据用户签约信息、SMF上报的RAT、智能UPF选择结果综合判断是否满足下发条件
   - 满足条件时，基于用户初始TAI服务发现寻址NWDAF
   - 通过`Nnwdaf_EventsSubscription Subscribe Request`消息，携带Analytics ID为`QOS_EXP_ANALYSIS`向NWDAF下发体验分析订阅

   **PCF综合判断条件**:
   - 用户为签约的套餐用户
   - 用户当前接入的RAT为配置支持的
   - 会话激活流程中，选择的UPF为智能UPF

   **N23订阅关键信元**:

| 信元名称 | 信元解释 |
| --- | --- |
| notificationURI | NWDAF分析通知目标 |
| smfId | SMF的NF instance ID，NWDAF通过此信元来寻址SMF |
| supis | 订阅的会话标识，supi和pduSeId唯一确定一个PDU会话 |
| pduSeId | 订阅的会话标识，supi和pduSeId唯一确定一个PDU会话 |
| appIds | 业务标识，可同时监控多个业务id，一个appId表示一个业务大类（如视频直播类） |
| event | 订阅的事件为QOS_EXP_ANALYSIS |
| status | 订阅状态: NORMAL（正常订阅）/ SUSPEND（暂停当前订阅，NWDAF保留会话但向SMF取消订阅） |

2. **NWDAF向PCF返回响应**: 携带订阅标识。

3. **NWDAF向SMF订阅（Nsmf接口）**:
   - NWDAF判断需要对重点用户进行体验分析订阅
   - 基于smfId向NRF寻址SMF
   - 通过`Nsmf_EventExposure_Subscribe Request`消息向SMF订阅QoS_EXP分析事件

   **Nsmf订阅关键信元**:

| 信元名称 | 信元解释 |
| --- | --- |
| notifId | NWDAF的通知关联号 |
| appIds | 业务标识，可同时监控多个业务id |
| event | 订阅的事件为QOS_EXP（与PCF向NWDAF订阅时的QOS_EXP_ANALYSIS为同一事件的不同名称） |
| pduSeId | 订阅的会话标识 |
| supi | 订阅的会话标识 |
| nwdafInfo | UDC经过SMF向UPF携带的体验数据上报地址（UDP地址），通过UDC的**ADD UDPADDR**命令配置，UDC根据与UDN的SBI接口状态确认可用的主UDN，将主UDN IP携带到nwdafInfo信元中 |

4. **SMF向UPF订阅（N4接口）**:
   - SMF基于supi和pduSeId定位PDU会话
   - 通过`PFCP Session Modification Request`消息通知UPF订阅体验分析事件

5. **UPF响应并启动采集**: UPF向SMF返回响应消息，并启动该用户的业务体验分析。

6. **SMF向NWDAF返回成功**: SMF收到UPF订阅成功消息后，向NWDAF返回订阅成功消息。

#### 2.2.2 RAT切换触发的订阅更新

PCF支持在RAT切换时触发订阅更新流程:

- **QOS_EXP_ANALYSIS订阅默认只在5G生效**
- RAT切换为不生效时: PCF发起N23更新流程（非取消订阅），携带`status`为`SUSPEND`暂停订阅。NWDAF保留N23订阅会话，但向SMF取消订阅。
- RAT切换恢复为有效时: PCF携带`status`为`NORMAL`恢复订阅。NWDAF收到后向SMF发起QOS_EXP订阅。

#### 2.2.3 体验数据上报

- UPF在感知到订阅事件后，通过与UDN之间的NupfR接口上报重点用户的体验数据
- UDN将单据生成用户所需格式，通过SFTP协议发送给BOSS/SFTP服务器

#### 2.2.4 去订阅流程

1. PCF通过`Nnwdaf_EventsSubscription_Unsubscribe Request`消息向NWDAF取消体验分析订阅
2. NWDAF向PCF返回成功
3. NWDAF通过`Nsmf_EventExposure_Unsubscribe Request`消息向SMF去订阅（SMF检测信元异常或subID找不到时返回错误码）
4. SMF通过`PFCP_Session_Modification Request`通知UPF取消对应的数据采集和上报
5. UPF取消订阅并向SMF回复响应
6. SMF向NWDAF回复去订阅成功

**重点用户流程话务统计**:

| 打点 | 指标 | 测量单元 | 测量集 |
| --- | --- | --- | --- |
| P1 | QOS_EXP_ANALYSIS事件订阅创建/更新请求次数 | N23接口基本测量 | NWDAF订阅管理 |
| P2 | QOS_EXP_ANALYSIS事件订阅创建成功率 | KPI | KPI |
| P3 | QOS_EXP事件订阅创建/更新请求次数 | Nsmf事件开放接口基本测量 | NWDAF订阅管理 |
| P7 | QOS_EXP事件订阅创建成功率 | KPI | KPI |
| P8 | NWDAF向BOSS上报体验单据成功的文件个数 | Nudn接口基本测量 | Nudn接口测量 |
| P4 | SMF接收QOS_EXP订阅事件的请求次数（N11/N16a） | SMF能力开放接口基本测量 | SMF会话管理 |
| P5 | VVIP接收的上报NWDAF的流消息数/用户消息数 | 智能板VVIP业务测量 | 智能板APP业务测量 |

### 2.3 保障用户体验感知信息采集流程

**业务场景**: 对重点业务保障用户进行体验感知信息采集。

**与重点用户流程的核心区别**:
- 保障用户的订阅/更新/去订阅流程复用重点业务保障解决方案的流程（事件为`QOS_ANALYSIS`）
- 保障用户的体验数据上报路径不同: UPF先上报给NWDAF(UDC)，再由UDC通过Nudn接口转发给UDN

#### 2.3.1 订阅流程

保障用户的体验分析订阅/更新订阅流程同重点业务保障的订阅/更新订阅流程（事件为`QOS_ANALYSIS`），涉及信令链路: PCF -> NWDAF(UDC) -> SMF -> UPF。

#### 2.3.2 体验数据上报

UPF在质差前、质差时以及保障后上报重点业务体验感知信息。

**UPF向UDC上报的关键信元**（`Nupf_EventExposure_Notify Request`消息）:

| 信元名称 | 信元解释 |
| --- | --- |
| timeStamp | 事件发生的时间 |
| startTime | 统计周期开始的时间戳 |
| eventType | 通知的事件类型 |
| snssai | PDU Session所在切片 |
| dnn | PDU Session所在APN/DNN |
| supi | 用户的IMSI |
| gpsi | 用户的MSISDN |
| ueIpv4Addr / ueIpv6Prefix | 用户IP地址 |
| ratType | 用户接入的网络类型 |
| infoIndicate | 标识当前UPF上报的Notify是质差上报还是体验上报。QOS_ANA时UDC进入保障流程同时向UDN转发；QOS_EXP时UDC直接向UDN转发，不进入保障流程 |
| appId | 应用ID（如直播） |
| subAppId | 子应用ID（如抖音） |
| subAppQosMonReport | 子应用级KPI数据，包含上下行带宽、时延、丢包数和总包数 |
| subAppStatus | 子应用状态: RUNNING（运行中）/ TERMINATED（流结束） |
| subAppQosQuality | 标识子应用级是否发生质差。infoIndicate=QOS_EXP时不携带；infoIndicate=QOS_ANA时携带 |

**UDC向UDN转发（`Nudn_DataManagement_Storage Request`消息）**:

UDC收到UPF数据后，通过Nudn接口向UDN转发，关键转发字段:

| 字段名称 | 字段描述 |
| --- | --- |
| timeStamp | 单据生成时间 |
| startTime | 统计周期开始的时间戳 |
| gpsi | 用户手机号MSISDN/GPSI |
| dnn | UPF上报的dnn |
| S-NSSAI | UPF上报的S-NSSAI |
| RAT | UPF上报的ratType |
| qCIOr5Qi | UPF上报的5qi |
| expOptFlg | 保障优化Flag，当前已保障状态置1 |
| expOptStartTime | 保障开始时间 |
| appId / subAppId | UPF上报的应用ID/子应用ID |
| appStatus | RUNNING（至少一条流存在）/ TERMINATED（最后一条流结束） |
| subAppQosQuality | Nupf消息的subAppQosQuality |
| tai | mcc+mnc+plmnId |
| cellId | mcc+mnc+nrCellId |
| delay_An / delay_Dn | Nupf消息的subAppQosMonReport.delayAn / delayDn |
| bandwidth_Ul / bandwidth_Dl | Nupf消息的subAppQosMonReport.bandwidthUl / bandwidthDl |
| pkg_Ul / pkg_Dl | Nupf消息的subAppQosMonReport.packetTotalUl / packetTotalDl |
| discardPkg_Ul / discardPkg_Dl | Nupf消息的subAppQosMonReport.packetLossUl / packetLossDl |

#### 2.3.3 去订阅流程

保障用户的体验分析去订阅流程同重点业务保障的去订阅流程（事件为`QOS_ANALYSIS`）。

**保障用户流程话务统计**:

| 打点 | 指标 | 测量单元 | 测量集 |
| --- | --- | --- | --- |
| P5 | VVIP上报给NWDAF的未发生质差的单据数/体验单据数 | 智能板VVIP业务测量 | 智能板APP业务测量 |
| P1 | NWDAF接收PCF发送的QOS_ANALYSIS事件订阅创建成功率 | KPI | KPI |
| P3 | NWDAF接收SMF回复的QOS_ANA事件订阅创建成功次数 | Nsmf事件开放接口基本测量 | NWDAF重点业务保障管理 |
| P6 | NWDAF接收UPF发送的QOS_ANA事件订阅通知请求次数（含INFOINDICATE为QOS_EXP） | Nupf事件开放接口基本测量 | NWDAF重点业务保障管理 |
| P8/P9 | NWDAF向CloudUDN上报重点业务体验感知信息请求/成功次数 | Nudn接口基本测量 | Nudn接口测量 |

### 2.4 异厂商PCF场景数据分析订阅

**业务场景**: 异厂商PCF向SMF下发智能PCC Rule后，SMF根据智能PCC Rule创建第二条N7链路，通过第二条N7链路向智能PCF下发订阅信息。

#### 2.4.1 激活场景的订阅下发

1. SMF发送`Npcf_SMPolicyControl_Create Request`给异厂商PCF，获取PCC规则
2. 异厂商PCF回复`Npcf_SMPolicyControl_Create Response`给SMF，携带**智能PCC Rule**，用于SMF匹配本地配置的预定义规则名称，匹配则后续创建第二条N7链路到智能PCF
3. SMF根据预定义规则选择UPF后与UPF建立用户面隧道，SMF/UPF等为用户分配UE IP
4. SMF向异厂商PCF发送`Npcf_SMPolicyControl_Update Request`消息携带UeIp更新UE IP
5. **SMF向智能PCF发送`Npcf_SMPolicyControl_Create Request`进行数据分析订阅**

   **关键信元**:

| 信元名称 | 信元解释 |
| --- | --- |
| subsPcfId | 当前管理该PDU会话的大网签约PCF实例ID（异厂商PCF），用于通知NWDAF后续创建N5保障时保障消息发送的目标PCF |
| needN23Subs | 需要触发N23订阅的事件，通过SMF上ADD RULE命令配置 |
| Ipv4Address | Ipv4类型的UeIp |
| Ipv6AddressPrefix | Ipv6类型的UeIp |
| ipDomain | 分配给用户的IPv4地址域标识 |

6. 智能PCF收到数据分析订阅后，通过N23接口向NWDAF发起数据分析订阅，后续流程与典型场景相同

#### 2.4.2 套餐更新场景的订阅下发

与激活场景的区别: 用户激活时异厂商PCF未携带智能PCC Rule，后续套餐变更时异厂商PCF才在`Npcf_SMPolicyControl_Update Response`中携带智能PCC Rule，SMF再向智能PCF发起订阅。

### 2.5 异厂商PCF场景数据分析更新订阅

**两种更新场景**:

1. **订阅事件发生变化**: 异厂商PCF向SMF更新智能PCC Rule后，SMF向智能PCF下发更新订阅信息（携带全量订阅事件），智能PCF通过N23接口向NWDAF发起更新订阅。SMF侧不同PCC Rule绑定不同订阅事件。

2. **异厂商PCF故障重选**: SMF重选异厂商PCF后，向智能PCF更新PCF ID。

**异厂商PCF故障处理（504错误码）**:
- SMF收到`504 Gateway Timeout`错误码
- 若重选异厂商PCF: 完成选择后SMF向智能PCF发送`Npcf_SMPolicyControl_Update Request`，携带最新异厂商PCF ID
- 若异厂商PCF回滚为LocalPCC: SMF向智能PCF发送`Npcf_SMPolicyControl_Delete Request`去订阅数据分析

**双N7会话约束**: SMF与智能PCF之间第二个N7会话产生失败后（消息超时，所有非2XX异常码），SMF不会重试建立或选择备用PCF，需等UE下次重新创建会话时再尝试。

### 2.6 异厂商PCF场景数据分析去订阅

**两种触发场景**:

1. **用户去激活引起**: SMF感知用户去激活 -> 向异厂商PCF请求删除SM策略关联（`Npcf_SMPolicyControl_Delete Request`） -> 删除策略关联后 -> SMF向智能PCF发送`Npcf_SMPolicyControl_Delete Request`发起数据分析去订阅

2. **异厂商PCF删除智能PCC Rule引起**: 异厂商PCF根据用户套餐变化，在`Npcf_SMPolicyControl_Update Response`中删除PCC Rule -> SMF向智能PCF发送`Npcf_SMPolicyControl_Delete Request`发起数据分析去订阅

后续流程（智能PCF向NWDAF去订阅等）与典型场景相同。

---

## 3. 方案约束与影响

### 3.1 体验感知通用约束

| 约束 | 影响 | 规避措施 |
| --- | --- | --- |
| 普通用户场景一个UPF不支持接收多个NWDAF(UDN)下发的订阅消息 | 无直接影响 | UDN与UPF对接规划时确保一个UPF仅对接一对UDN（主备），保证仅主UDN向UPF下发订阅 |
| 普通用户场景UDN更新订阅后，更新后的策略在UPF侧对**已激活用户不生效**，仅对新激活用户生效 | UDN更新的订阅存在不会完全立即生效的场景 | 无 |
| 重点用户场景UDC需要通过SMF向UPF携带体验数据上报的UDP地址，当此地址不可用或UDN不可用时，UDC**不会更新订阅** | UDN侧地址变化，对于已下发订阅不会生效 | 无 |

### 3.2 异厂商PCF场景特有约束

| 约束 | 影响 | 规避措施 |
| --- | --- | --- |
| 仅支持N7接入的用户（包括Gx转N7） | 不支持Gx接入的用户 | 不涉及 |
| 保障用户签约套餐通过PCC Rule划分 | SMF通过PCC Rule识别保障用户，触发后续NWDAF分析业务相关流程 | 不涉及 |
| 当前方案仅支持配置**一个**重点业务保障套餐，不支持基于用户粒度差异化保障 | 不涉及 | 不涉及 |
| 双N7接口策略约束（见下文详述） | 第二个N7会话异常时SMF不重试 | 不涉及 |
| 异厂商PCF场景下NWDAF不支持从RAN-OAM获取小区容量和PRB利用率，不支持预测 | NWDAF不能根据预测的小区容量和PRB利用率判断是否发起保障建议 | NWDAF本地配置小区容量 |

**双N7接口策略详细约束**:
- SMF创建第二个N7会话时，不考虑智能PCF选择失败、会话创建失败、会话更新响应等异常
- SMF在创建第二个N7会话时上报ratType、位置、AMF ID信元，后续更新消息中不再上报
- SMF不支持智能PCF向SMF发送`Npcf_SMPolicyControl_UpdateNotify`消息触发的智能PCF重选
- SMF不支持第二N7会话failover处理
- SMF只在第一个N7会话创建时同时触发创建第二个N7会话，后续不再跟第二个N7接口做后续交互
- SMF仅接受来自大网PCF下发的策略

---

## 4. 配置与调测要点

### 4.1 保障用户上报周期配置

- 默认上报周期: 5分钟
- 配置方式一: UDG的 **SET VVIPBASICFUNC** 命令中的"非质差上报周期（秒）"参数
- 配置方式二: UDG的 **ADD APPPOLICYCTRL** 命令中的"基于应用的非质差上报周期"参数

### 4.2 重点用户上报周期配置

- 默认上报周期: 5分钟
- 配置方式: UDG的 **SET EXPBASICFUNC** 命令中的"体验业务上报周期（秒）"参数

### 4.3 普通用户上报周期配置

- 默认上报周期: 5分钟
- 配置方式: UDG的 **SET EXPBASICFUNC** 命令中的"体验业务上报周期（秒）"参数

### 4.4 UDC上报地址配置

- 通过UDC的 **ADD UDPADDR** 命令配置体验数据上报的UDP地址
- UDC根据与UDN的SBI接口状态确认可用的主UDN，将主UDN IP携带到nwdafInfo信元中
- 当UDN地址不可用时UDC不会更新订阅（约束）

### 4.5 SMF预定义规则配置

- 异厂商PCF场景中，通过SMF的 **ADD RULE** 命令配置needN23Subs事件
- 智能PCC Rule匹配SMF本地配置的预定义规则名称后触发第二条N7链路创建

### 4.6 UDN侧OM配置项

- 普通用户抽样率（sessRatio）
- 订阅有效时长
- dnn、snssai、app、ratType
- 主备UDN南向接入IP地址
- 主备UDN Collector IP列表（mainReportIpList / slaveReportIpList）

### 4.7 UDN单据打包配置

- NWDAF(UDN)支持基于周期或者大小将单据打包
- 通过SFTP发送到BOSS/SFTP服务器

### 4.8 错误码处理要点

**N23接口（PCF <-> NWDAF）错误码**:
- 400 Bad Request: 信元异常（MANDATORY_IE_INCORRECT / OPTIONAL_IE_INCORRECT / MANDATORY_IE_MISSING）
- 404 Not Found: 订阅任务不存在（SUBSCRIPTION_NOT_FOUND）
- 500 Internal Server Error: License不支持（INSUFFICIENT_RESOURCES）
- 504 Gateway Timeout: NWDAF内部服务不可用

**Nsmf接口（NWDAF <-> SMF）错误码**:
- 400: 信元异常
- 404: subId找不到对应订阅（SUBSCRIPTION_NOT_FOUND）
- 500: 配置未开启/超最大值/UPF SRR安装失败（SYSTEM_FAILURE/INSUFFICIENT_RESOURCES）
- 504: UPF未响应超时

**Nupf接口（UPF <-> NWDAF/UDC）错误码**:
- 400: 参数缺失、格式错误
- 404: 订阅信息不存在，UPF收到404则认为NWDAF故障，删除该NWDAF下发的所有质差分析订阅
- 504: NWDAF内部服务不可用

**N4接口（SMF <-> UPF）错误码**:
- 错误码3: SRR更新失败，UPF仍向SMF返回成功响应但携带失败的SRR ID

**Nudn接口（UDC <-> UDN）错误码**:
- 401 Unauthorized: UDN主备切换，请求发到运行备节点

---

## 5. 与带宽控制的关系

### 5.1 体验感知信息采集→分析→带宽策略调整链路

体验感知解决方案为带宽控制场景提供了上游数据输入，构成完整的闭环链路:

```
体验感知信息采集 (UPF识别应用+采集KPI)
    ↓
体验数据上报 (UPF -> NWDAF -> BOSS/SFTP)
    ↓
体验分析 (BOSS/NWDAF分析带宽、时延、丢包等KPI)
    ↓
策略决策 (PCF/网络管理系统根据分析结果调整带宽策略)
    ↓
带宽执行 (UPF执行调整后的带宽控制规则)
```

### 5.2 带宽相关KPI指标

体验感知采集的KPI中与带宽控制直接相关的指标:

| KPI指标 | 信元来源 | 带宽控制关联 |
| --- | --- | --- |
| 上行带宽 (bandwidth_Ul) | subAppQosMonReport.bandwidthUl | 反映实际上行带宽使用情况，用于评估带宽策略效果 |
| 下行带宽 (bandwidth_Dl) | subAppQosMonReport.bandwidthDl | 反映实际下行带宽使用情况，用于评估带宽策略效果 |
| 时延 (delay_An / delay_Dn) | subAppQosMonReport.delayAn / delayDn | 带宽不足可能导致排队时延增大 |
| 丢包数 (discardPkg_Ul / discardPkg_Dl) | subAppQosMonReport.packetLossUl / packetLossDl | 带宽限速可能导致丢包 |
| 总包数 (pkg_Ul / pkg_Dl) | subAppQosMonReport.packetTotalUl / packetTotalDl | 用于计算丢包率 |

### 5.3 三类用户与带宽控制的分层关系

| 用户类型 | 采集路径 | 带宽控制策略关联 |
| --- | --- | --- |
| 保障用户 | PCF -> NWDAF(UDC) -> SMF -> UPF | 保障用户在质差时触发保障流程（QOS_ANALYSIS），可能涉及带宽资源重新分配；体验数据（QOS_EXP）同时上报 |
| 重点用户 | PCF -> NWDAF(UDC) -> SMF -> UPF | 重点用户的体验数据上报给BOSS后，运营商可据此调整带宽策略（如提速/降速） |
| 普通用户 | NWDAF(UDN) -> UPF（设备级抽样） | 普通用户抽样数据用于统计分析整体网络带宽使用趋势，为带宽控制策略提供基线参考 |

### 5.4 infoIndicate双通道机制与带宽控制

保障用户流程中的`infoIndicate`信元区分两种数据通道:

- **infoIndicate=QOS_ANA**: 触发UDC进入重点业务保障流程（申请小区配额、建立保障），可能与带宽资源分配直接相关
- **infoIndicate=QOS_EXP**: 仅体验数据上报，UDC直接转发给UDN，不触发保障流程

### 5.5 异厂商PCF场景对带宽控制的影响

异厂商PCF负责大网PCC策略（包括带宽控制策略），智能PCF负责数据分析订阅:
- 带宽控制策略由异厂商PCF通过第一条N7链路下发
- 体验感知分析通过第二条N7链路（SMF -> 智能PCF -> NWDAF）完成
- 两条链路独立运作，带宽控制与体验感知互不干扰
- 但当异厂商PCF故障时（504），SMF可能触发LocalPCC回滚，导致去订阅数据分析，体验感知功能暂停

---

## 6. 关键概念术语

| 术语 | 解释 |
| --- | --- |
| 体验感知 | 通过用户面业务感知识别用户应用级的体验信息（带宽、时延、丢包、总包数） |
| 保障用户 | 签约重点业务保障套餐的用户，订阅事件为QOS_ANALYSIS |
| 重点用户 | 签约业务体验感知套餐的重点用户（如全球通），订阅事件为QOS_EXP_ANALYSIS |
| 普通用户 | 非签约用户中被抽样采集的用户，订阅类型为QOS_EXP |
| QOS_ANALYSIS | 质差分析事件，保障用户专用，触发时可能进入保障流程 |
| QOS_EXP_ANALYSIS | 体验分析事件，重点用户专用，仅采集体验数据 |
| QOS_EXP | NWDAF向SMF订阅时使用的事件名称，与QOS_EXP_ANALYSIS为同一事件 |
| NWDAF(UDC) | NWDAF前端，即UDC产品，负责N23/Nsmf接口交互和保障用户数据转发 |
| NWDAF(UDN) | NWDAF CloudUDN，负责设备级抽样订阅、体验数据接收和BOSS单据上报 |
| 智能PCF | 华为PCF，异厂商PCF场景中负责数据分析订阅等智能业务 |
| 异厂商PCF | 非华为PCF，负责大网PCC策略功能 |
| 智能PCC Rule | 异厂商PCF场景中由异厂商PCF下发的规则，SMF据此匹配预定义规则并创建第二条N7链路 |
| 智能UPF | 支持体验感知业务的UPF（即UDG），PCF判断UPF为智能UPF时才下发订阅 |
| infoIndicate | 保障用户上报消息中的标识信元，区分质差上报(QOS_ANA)和体验上报(QOS_EXP) |
| subAppQosMonReport | 子应用级KPI数据容器，包含带宽、时延、丢包、总包数等指标 |
| needN23Subs | 异厂商PCF场景中SMF向智能PCF携带的N23订阅事件标识，通过ADD RULE命令配置 |
| subsPcfId | 当前管理PDU会话的大网签约PCF实例ID，用于NWDAF后续创建N5保障时确定目标PCF |
| nwdafInfo | Nsmf订阅消息中信元，携带UDN的UDP上报地址，通过ADD UDPADDR命令配置 |
| NupfR接口 | UPF向UDN上报重点用户和普通用户体验数据的私有协议接口（UDP承载） |

---

## 7. 信令流程对比总结

### 7.1 三类用户采集流程差异

| 维度 | 保障用户 | 重点用户 | 普通用户 |
| --- | --- | --- | --- |
| 订阅发起方 | PCF | PCF | NWDAF(UDN) |
| 订阅链路 | PCF->NWDAF(UDC)->SMF->UPF | PCF->NWDAF(UDC)->SMF->UPF | NWDAF(UDN)->UPF |
| 订阅粒度 | 用户会话级 | 用户会话级 | 设备级用户抽样 |
| 订阅事件 | QOS_ANALYSIS | QOS_EXP_ANALYSIS | QOS_EXP |
| 上报链路 | UPF->NWDAF(UDC)->NWDAF(UDN)->BOSS | UPF->NWDAF(UDN)->BOSS | UPF->NWDAF(UDN)->BOSS |
| 是否需保障方案 | 是 | 否 | 否 |
| RAT切换支持 | 支持更新 | 支持更新（默认仅5G生效） | 设备级订阅不涉及 |
| 上报周期配置 | SET VVIPBASICFUNC / ADD APPPOLICYCTRL | SET EXPBASICFUNC | SET EXPBASICFUNC |
| 默认上报周期 | 5分钟 | 5分钟 | 5分钟 |

### 7.2 典型场景 vs 异厂商PCF场景

| 维度 | 典型场景 | 异厂商PCF场景 |
| --- | --- | --- |
| PCF数量 | 1个（智能PCF） | 2个（异厂商PCF + 智能PCF） |
| N7链路 | 1条（SMF <-> PCF） | 2条（SMF <-> 异厂商PCF + SMF <-> 智能PCF） |
| 智能PCC Rule | 不涉及 | 异厂商PCF下发，SMF据此创建第二条N7链路 |
| 订阅触发 | PCF直接向NWDAF订阅 | SMF通过第二条N7链路向智能PCF订阅，智能PCF再向NWDAF订阅 |
| 策略来源 | 智能PCF | 异厂商PCF（大网策略） |
| 故障处理 | 标准处理 | 异厂商PCF故障时SMF可重选或回滚LocalPCC |
| 数据上报路径 | 与典型场景相同 | 与典型场景相同 |

---

## 8. 知识来源

| 序号 | 源文档 | 原始路径 |
| --- | --- | --- |
| 1 | 方案介绍_72546024.md | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/方案介绍_72546024.md |
| 2 | 典型场景组网与接口_34250333.md | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/组网与接口/典型场景组网与接口_34250333.md |
| 3 | 普通用户体验感知信息采集流程_34250341.md | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/信令流程描述/普通用户体验感知信息采集流程_34250341.md |
| 4 | 重点用户体验感知信息采集流程_90530626.md | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/信令流程描述/重点用户体验感知信息采集流程_90530626.md |
| 5 | 保障用户体验感知信息采集流程_90690562.md | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/信令流程描述/保障用户体验感知信息采集流程_90690562.md |
| 6 | 异厂商PCF场景数据分析订阅_95218746.md | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/信令流程描述/异厂商PCF场景数据分析订阅_95218746.md |
| 7 | 异厂商PCF场景数据分析更新订阅_30778141.md | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/信令流程描述/异厂商PCF场景数据分析更新订阅_30778141.md |
| 8 | 异厂商PCF场景数据分析去订阅_95378626.md | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/信令流程描述/异厂商PCF场景数据分析去订阅_95378626.md |
| 9 | 体验感知通用约束与影响_90530622.md | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/方案约束与影响/体验感知通用约束与影响_90530622.md |
| 10 | 异厂商PCF场景约束与影响_30937789.md | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/方案约束与影响/异厂商PCF场景约束与影响_30937789.md |
