# Batch 05-02: Nchf融合计费服务 + PFCP/N4 URR + Gx计费AVP 知识草稿

## 来源文件清单

| # | 文件组 | 篇数 | 重点 |
|---|--------|------|------|
| 1 | Nchf融合计费服务操作 | 5 | 服务操作类型、会话生命周期、Notify通知 |
| 2 | N40信元 | 8 | multipleUnitUsage、配额阈值、配额保持时间 |
| 3 | PFCP/N4 URR操作与信元 | 15 | URR生命周期、测量方法、上报触发器、配额信元 |
| 4 | Gx计费相关AVP | 12 | PCC规则定义、Online/Offline、Metering-Method、Usage Monitoring |

---

## 一、Nchf融合计费服务操作

### K190: Nchf_ConvergedCharging四种服务操作
> 来源: Nchf_ConvergedCharging服务操作概述_76785317

**原理知识**

| 服务操作 | 描述 | 发起方 | 对应消息 |
|----------|------|--------|----------|
| Nchf_ConvergedCharging_Create | 计费会话建立 | SMF | Charging Data Request/Response [Initial] |
| Nchf_ConvergedCharging_Update | 计费事件触发的会话更新（申请新配额、配额上报、VT等） | SMF | Charging Data Request/Response [Update] |
| Nchf_ConvergedCharging_Release | 计费会话结束 | SMF | Charging Data Request/Response [Termination] |
| Nchf_ConvergedCharging_Notify | 重授权或去活通知 | CHF | Charging Notify Request/Response |

CHF职责：配额管理、重授权触发条件、通知服务、接受用量报告、生成CDR话单。
SMF职责：请求并接收配额、发送用量报告、处理配额重授权或终止通知。

### K191: CHF选择优先级（6级）
> 来源: 计费会话创建流程_78888683

**配置知识**

SMF选择CHF的优先级从高到低：
1. 拨测场景，ADD SELCHFGBYIMSI命令基于IMSI选择CHF
2. 配置基于IMSI号段选择CHF（多CHF主备组均衡）
3. 从PCF下发的chargingInfo属性获取（域名需查本地配置，IP直接使用）
4. 根据UDM签约CC选择本地CHF（DNN/APN级CC优先于Session级CC）
5. 通过NRF发现CHF（仅支持优先级和权重选择，不支持主备）
6. ADD SELECTCHFGBYCC命令基于本地配置的CC选择CHF

### K192: Charging Data Request [Initial]关键信元
> 来源: 计费会话创建流程_78888683

**协议知识**

Create Request关键信元：
- invocationSequenceNumber: 请求序号（首次为0）
- nfConsumerIdentification: NF消费者标识（含nFIPv4/v6Address、nFName、nodeFunctionality=SMF）
- invocationTimeStamp: 请求发送时间
- multipleUnitUsage: 配额管理请求/用量报告数组
  - ratingGroup: 费率组标识
  - requestedUnit: 配额申请（在线计费携带，离线计费不携带）
  - uPFID: UPF标识
- pDUSessionChargingInformation: PDU会话计费信息
  - chargingId: PDU会话计费标识
  - pduSessionInformation（含chargingCharacteristics、startTime等）
  - unitCountInactivityTimer: 配额不活跃定时器
- notifyUri: 接收CHF Notify消息的SMF URI

SET CNVRGDCHGPARA命令TIMEROUNDMODE参数控制时间戳计算方式：ROUNDOFF（四舍五入，默认）/ ROUNDDOWN（向下取整）。

### K193: Charging Data Response [Initial]关键信元
> 来源: 计费会话创建流程_78888683

**协议知识**

Create Response关键信元：
- invocationSequenceNumber: 响应序号
- multipleUnitInformation: 数组
  - resultCode: 结果码（SUCCESS等）
  - ratingGroup: 费率组标识
  - grantedUnit: 授权配额（totalVolume字节 + time秒）
  - triggers: CHF下发的trigger全集（triggerType + triggerCategory）
  - timeQuotaThreshold: 时间配额门限（秒）
  - volumeQuotaThreshold: 流量配额门限（字节）

Trigger类型示例：QUOTA_THRESHOLD（到达阈值）、QUOTA_EXHAUSTED（配额耗尽）。
TriggerCategory: IMMEDIATE_REPORT（立即上报）。

异常响应处理：SET CNVRGDCHGPARA命令BADRSPACT=CONTINUE时，用户业务继续但不进行配额管理。

### K194: 在线计费与离线计费的信元差异
> 来源: 计费会话创建流程_78888683, 计费会话更新流程_78888684

**隐性规则**

在线计费（有配额管理）vs 离线计费（无配额管理）差异：

| 维度 | 在线计费 | 离线计费 |
|------|----------|----------|
| Create Request | 含requestedUnit | 不含requestedUnit |
| Create Response | 含grantedUnit、阈值、配额Trigger | 不含grantedUnit/threshold/unitQuotaThreshold，不含QUOTA_THRESHOLD/QUOTA_EXHAUSTED |
| Update Request | quotaManagementIndicator=ONLINE_CHARGING，含requestedUnit | quotaManagementIndicator=OFFLINE_CHARGING，不含requestedUnit |
| PFCP Create URR | 含Volume Quota/Time Quota/Event Quota | 不含配额信元 |

在线计费申请配额，离线计费仅申请计费参数。

### K195: SMF维护RG与URR ID的映射关系
> 来源: 计费会话创建流程_78888683

**架构知识**

- Nchf接口：SMF按RG粒度向CHF申请配额，按RG或RG+SID粒度上报配额；CHF按RG粒度下发配额
- N4接口：SMF向UPF下发URR，URR包含计费事件和计费参数，UPF按URR向SMF上报配额用量
- 映射：所有RG都有对应的URR ID，但非计费URR ID没有对应的RG

计费会话创建触发方式：默认在PDU会话建立时触发，可通过SET CHFINIT命令的CHFINIT参数配置为业务使用时触发。

### K196: UPF分配IP vs SMF分配IP的计费会话创建差异
> 来源: 计费会话创建流程_78888683

**流程差异**

- UPF分配IP：先建立PFCP会话（SMF→UPF），UPF分配IP后返回，SMF再向CHF发Create Request，然后PFCP会话修改下发URR
- SMF分配IP：SMF直接携带用户IP向CHF发Create Request，CHF返回配额后，SMF向UPF发PFCP Session Establishment（含Create PDR/FAR/URR一步到位）

### K197: 计费会话更新四种触发场景
> 来源: 计费会话更新流程_78888684

**原理知识**

| 触发场景 | 说明 |
|----------|------|
| UPF内部事件 | 配额耗尽/到达阈值、配额空闲时间门限、访问无配额新业务 |
| SMF内部事件 | 在线配额有效时长超期（ADD CCT配置RG级有效时长） |
| 外部事件 | 接入条件更新（Serving Node变更、PRA变更、QoS改变、位置更新、时区改变、PLMN变更） |
| CHF重授权 | 用户充值成功等场景CHF通知SMF重新申请配额 |

SMF上报方式：SET CNVRGDCHGPARA命令RPTBASEDONGU参数——不使能基于实际使用量上报；使能则基于GrantedUnit做配额管理，用量不超过下发配额。

### K198: Usage Report关键信元（PFCP Session Report）
> 来源: 计费会话更新流程_78888684

**协议知识**

UPF上报的Usage Report包含：
- URR ID: 标识上报的URR
- UR-SEQN: 唯一标识该URR的Usage Report
- Start Time / End Time: 起止时间
- Volume Measurement: 总流量/上行/下行
- Duration Measurement: 时长使用情况
  - ISTM=0或不携带：从UPF首次收到业务数据包开始，到业务终止结束
  - ISTM=1：从UPF首次收到授权配额成功开始，到用户去激活或配额管理实例终止
- Time of First Packet / Last Packet: 首尾包时间

配额更新超时保护：定时器=T3RESPONSE*N3REQUEST+4秒（SET UPPFCPPATH配置），超时未收到配额更新则UPF阻塞业务。

### K199: Charging Data Update Request关键信元
> 来源: 计费会话更新流程_78888684

**协议知识**

Update Request中的multipleUnitUsage包含：
- ratingGroup: 费率组
- requestedUnit: 配额申请（在线计费）
- UsedUnitContainer: 已用配额容器
  - totalVolume / downlinkVolume / uplinkVolume: 流量使用量
  - time: 时长使用量
  - quotaManagementIndicator: ONLINE_CHARGING/OFFLINE_CHARGING
  - serviceId: 服务标识
  - triggers: 当前触发类型（仅一个，取优先级最高）
  - triggerTimestamp: 触发时间
  - localSequenceNumber: 本地序号
  - pDUContainerInformation: 含timeofFirstUsage/timeofLastUsage/rATType/userLocationInformation

计费请求消息的triggerType只能携带一个，表示由哪个trigger触发；多个trigger同时满足时携带优先级最高的一个。

### K200: CHF下发的Trigger全集与Trigger优先级
> 来源: 计费会话更新流程_78888684

**隐性规则**

- CHF在Response中携带triggerType全集（如QUOTA_THRESHOLD + QUOTA_EXHAUSTED），与Request由哪个trigger触发无关
- SMF本地也可配置Trigger，优先级低于CHF下发的
- 外部事件触发场景CHF可额外下发Session级Trigger：VOLUME_LIMIT、TIME_LIMIT、USER_LOCATION_CHANGE等
- CHF Response还可能携带：validityTime（配额有效时间）、sessionFailover（FAILOVER_SUPPORTED）、invocationResult.failureHandling（CONTINUE）

RG级VT事件合并：SET CNVRGDCHGPARA命令MERGERGVTSW=ENABLE时，同时发生的RG级VT事件合并上报CHF。

### K201: 计费会话释放流程
> 来源: 计费会话释放流程_78888685

**流程知识**

UE发起释放流程：
1. UE发起PDU会话释放
2. SMF向UPF发PFCP Session Deletion Request
3. UPF返回Deletion Response（携带计费统计信息）
4. SMF向CHF发ChargingDataRelease Request（含final用量）
5. CHF扣费处理，关闭CHF-CDR
6. CHF返回Release Response

Release Request特有信元：
- stopTime: PDU会话停止时间
- sessionStopIndicator: true（指示PDU会话终止）
- triggerType: FINAL（正常去活）

离线计费场景：quotaManagementIndicator=OFFLINE_CHARGING。
异常去活triggerType控制：ADD N40DIAGTRIGGER的RELEASETRIGGER参数 > SET CNVRGDCHGPARA的SPTABNTRIGGER参数（ENABLE/DISABLE控制AbnormalRelease或FINAL）。

### K202: CHF Notify通知（重授权与去活）
> 来源: 计费会话通知流程_84997604

**流程知识**

CHF发起重授权（仅在线计费）：
1. CHF→SMF: ChargingDataNotify Request
   - notificationType: REAUTHORIZATION
   - reauthorizationDetails: [{quotaManagementIndicator, ratingGroup}]
2. SMF→CHF: Notify Response (204 No Content)
3. SMF→UPF: PFCP Session Modification（Query URR查询用量）
4. UPF→SMF: Modification Response（上报用量）
5. SMF→CHF: ChargingDataUpdate Request（请求重授权）
6. CHF→SMF: Update Response（新配额+新Trigger）

CHF发起用户去活：
1. CHF→SMF: Notify Request（notificationType=ABORT_CHARGING）
2. SMF→UPF: PFCP Session Deletion Request
3. UPF→SMF: Deletion Response（配额用量）
4. SMF→CHF: ChargingDataRelease Request（携带用量）
5. CHF扣费关闭CDR，返回Release Response
6. SMF发起PDU会话释放

---

## 二、N40信元

### K203: multipleUnitUsage信元
> 来源: multipleUnitUsage_23849968

**协议知识**

- 定义：包含配额管理请求的相关参数以及/或者用量报告
- 数据类型：数组，每项包含ratingGroup、requestedUnit、usedUnitContainer、uPFID
- 应用场景：
  - ChargingDataCreate Request（创建计费资源）
  - ChargingDataUpdate Request（更新计费数据）
  - ChargingDataRelease Request（终止计费会话）
  - ChargingDataNotify Request（CHF通知更新/终止）
- 参考：3GPP TS 32.291

### K204: quotaManagementIndicator信元
> 来源: quotaManagementIndicator_72169837

**协议知识**

- 定义：表示重授权通知是否用于配额管理控制
- 枚举值：
  - ONLINE_CHARGING：要求配额管理控制
  - OFFLINE_CHARGING：无配额管理控制
- 应用场景：ChargingDataNotify Request（CHF→SMF通知消息）

### K205: quotaHoldingTime信元
> 来源: quotaHoldingTime_72049977

**协议知识**

- 定义：限制配额保持时间（秒），同时限制时间配额和流量配额
- 含义：当观察不到与配额相关的流量时，SMF认为该配额已过期
- 特殊值：0表示不使用该机制
- 默认值：信元不存在时使用SMF本地配置的默认值
- 应用场景：ChargingDataCreate Response

### K206: timeQuotaThreshold / volumeQuotaThreshold / unitQuotaThreshold
> 来源: timeQuotaThreshold_23530108, volumeQuotaThreshold_71969833, unitQuotaThreshold_71849841

**协议知识**

| 信元 | 含义 | 单位 | 数据类型 |
|------|------|------|----------|
| timeQuotaThreshold | 授权的时间配额阈值 | 秒 | 整型 |
| volumeQuotaThreshold | 授权的流量配额阈值 | 字节 | 无符号整型 [0, 2^64-1] |
| unitQuotaThreshold | 授权的事件计费配额阈值 | 次 | 整型 |

均出现在ChargingDataCreate Response中，由CHF下发给SMF。阈值到达时触发QUOTA_THRESHOLD事件，SMF向CHF更新计费会话。

### K207: qosFlowsUsageReports信元
> 来源: qosFlowsUsageReports_23690008

**协议知识**

- 定义：每个QFI的容器清单，包含上报用量
- 子信元：qFI、startTimestamp、endTimestamp、downlinkVolume、uplinkVolume
- 应用场景：ChargingDataCreate Request

### K208: rANSecondaryRATUsageReport信元
> 来源: rANSecondaryRATUsageReport_23689980

**协议知识**

- 定义：指示无线侧上报的Secondary RAT usage值
- 子信元：rANSecondaryRATType（如NR）、qosFlowsUsageReports
- 应用场景：ChargingDataCreate Request

---

## 三、PFCP/N4 URR操作与信元

### K209: Create URR完整信元列表
> 来源: Create URR_32945593

**协议知识**

Create URR必选信元：URR ID、Measurement Method、Reporting Triggers。

条件必选信元（按需出现）：

| 信元 | 触发条件 |
|------|----------|
| Volume Threshold | 使用流量测量且需要流量阈值上报 |
| Volume Quota | 使用流量测量且需要提供流量配额 |
| Event Threshold | 使用事件测量且需要事件阈值上报 |
| Event Quota | 使用事件测量且需要事件配额 |
| Time Threshold | 使用时间测量且需要时间阈值上报 |
| Time Quota | 使用时间测量且需要时间配额 |
| Quota Holding Time | 时间/流量/事件测量中，不活动期间不传包时需要 |
| Inactivity Detection Time | 使用时间测量，不活动时需挂起时间测量 |
| Linked URR ID | 需要链接使用报告 |
| Measurement Information | Inactive/Reduced/ISTM标志位为1时 |
| Aggregated URRs | URR支持信用池 |
| FAR ID for Quota Action | 有配额且UPF支持配额动作特性 |

可选信元：Monitoring Time及其Subsequent系列（Subsequent Volume/Time/Event Threshold/Quota）。

### K210: Update URR信元与Create URR差异
> 来源: Update URR_32945595

**协议知识**

Update URR与Create URR相比：
- URR ID仍为必选（标识要修改的URR）
- 其余信元为条件必选（"如果需要修改xxx，该信元应出现"）
- 新增FAR ID for Quota Action：URR中新增Volume/Time/Event Quota且UPF支持配额动作时可能出现，当耗尽URR配额时包含替代流量标识符
- Aggregated URRs在Update时提供完整列表（替换而非增量）

### K211: Remove URR信元
> 来源: Remove URR_33031223

**协议知识**

Remove URR仅包含一个必选信元：URR ID。
用于去激活或删除PFCP会话中的URR，触发PFCP Session Modification Response上报终止用量报告（TERMR触发）。

### K212: URR ID信元
> 来源: URR ID_86168984

**协议知识**

- 功能：在PFCP会话配置的所有URR中唯一标识一个URR
- 第5字节bit8含义：
  - 0：Rule由控制面功能（SMF）动态分配
  - 1：Rule在用户面功能（UPF）中预定义

### K213: Usage Report Trigger完整编码（3字节位图）
> 来源: Usage Report Trigger_85720890

**协议知识**

第5字节（bit1-8）：
| bit | 名称 | 含义 |
|-----|------|------|
| 1 | PERIO | 定期上报 |
| 2 | VOLTH | 流量阈值到达 |
| 3 | TIMTH | 时间阈值到达 |
| 4 | QUHTI | 配额保持时间超时（无报文） |
| 5 | START | 流量开始 |
| 6 | STOPT | 流量结束 |
| 7 | DROTH | 下行丢弃流量达阈值 |
| 8 | IMMER | 立即上报 |

第6字节（bit1-8）：
| bit | 名称 | 含义 |
|-----|------|------|
| 1 | VOLQU | 流量配额耗尽 |
| 2 | TIMQU | 时间配额耗尽 |
| 3 | LIUSA | 关联使用报告（Linked URR触发） |
| 4 | TERMR | 终止报告（会话删除/URR删除） |
| 5 | MONIT | 监控时间到达 |
| 6 | ENVCL | 信封关闭 |
| 7 | MACAR | MAC地址上报 |
| 8 | EVETH | 事件阈值到达 |

第7字节bit1: EVEQU（事件配额耗尽），bit2-8备用。

至少一个bit为1，可多个bit同时为1。

### K214: Measurement Method信元
> 来源: Measurement Method_86168972

**协议知识**

- 功能：指示测量网络资源使用情况的方法
- 第5字节编码：
  - bit1 DURAT：时长测量
  - bit2 VOLUM：流量测量
  - bit3 EVENT：事件测量
  - bit4-8：备用
- 至少一个bit为1，可多个bit同时为1（如DURATION_VOLUME对应DURAT+VOLUM）

### K215: Volume Measurement信元
> 来源: Volume Measurement_86009018

**协议知识**

- 功能：指示测量的话务量
- 第5字节编码：
  - bit1 TOVOL：Total Volume字段存在
  - bit2 ULVOL：Uplink Volume字段存在
  - bit3 DLVOL：Downlink Volume字段存在
- Total/Uplink/Downlink Volume编码为Unsigned64，单位字节

### K216: Duration Measurement信元
> 来源: Duration Measurement_86168982

**协议知识**

- 功能：指示已用时间
- 单位：秒

### K217: Volume Quota信元
> 来源: Volume Quota_32945611

**协议知识**

- 功能：指示UPF需要监控的流量配额
- 编码同Volume Measurement（TOVOL/ULVOL/DLVOL标志位+对应值）
- Unsigned64类型，单位字节

### K218: Time Quota信元
> 来源: Time Quota_85720898

**协议知识**

- 功能：指示UPF需要监控的时间配额
- 单位：秒

### K219: Reporting Triggers信元（N4接口）
> 来源: Reporting Triggers_85849372

**协议知识**

N4接口的Reporting Triggers编码与Usage Report Trigger基本一致但略有差异：

第5字节：PERIO/VOLTH/TIMTH/QUHTI/START/STOPT/DROTH/LIUSA
第6字节：VOLQU/TIMQU/ENVCL/MACAR/EVETH/EVEQU

与Usage Report Trigger的差异：第5字节bit8是LIUSA（非IMMER），第6字节bit3是ENVCL（非TERMR），bit4是MACAR（非MONIT），无第7字节。

### K220: Quota Holding Time信元
> 来源: Quota Holding Time_32788437

**协议知识**

- 功能：指示配额保持时间
- 单位：秒
- 含义：在给定不活动期间没有收到数据包时，不再允许数据包传输，触发QUHTI上报

### K221: Aggregated URRs信元（信用池机制）
> 来源: Aggregated URRs_85720880

**协议知识**

- 功能：支持URR信用池（多个URR共享同一配额）
- 子信元：
  - Aggregated URR ID：共享信用池的聚合URR ID（必选）
  - Multiplier：乘法器，应用于测量抽象业务单元从信用池中消耗的流量（必选）
- 使用场景：多个业务共享一个总配额池，按不同权重消耗

### K222: Linked URR ID信元
> 来源: Linked URR ID_85849384

**协议知识**

- 功能：指示Linked URR的ID
- 机制：上报某个URR时，也会上报其关联的URR。例如A link B，当B上报时也会上报A
- 可存在多个相同类型的信元表示与该URR相关的多个链接URR

### K223: Subsequent Volume Quota信元
> 来源: Subsequent Volume Quota_85849388

**协议知识**

- 功能：指示UPF在监控时间（Monitoring Time）之后仍需要监控的流量配额
- 编码同Volume Quota（TOVOL/ULVOL/DLVOL标志位+对应值）
- 前提：存在Monitoring Time信元且使用基于流量的测量

---

## 四、Gx计费相关AVP

### K224: Charging-Rule-Definition AVP结构
> 来源: Charging-Rule-Definition_30780110

**协议知识**

Charging-Rule-Definition（AVP 1003, Grouped类型）定义PCRF发送给PCEF的PCC规则，包含计费相关子信元：

| 子信元 | 类型 | 计费相关 |
|--------|------|----------|
| Charging-Rule-Name | 必选 | 规则唯一标识 |
| Service-Identifier | 可选 | 服务标识(SID) |
| Rating-Group | 可选 | 费率组(RG) |
| Flow-Information | 可选 | 业务流信息 |
| Reporting-Level | 可选 | 上报级别 |
| Online | 可选 | 在线计费使能 |
| Offline | 可选 | 离线计费使能 |
| Metering-Method | 可选 | 计量方式 |
| Monitoring-Key | 可选 | 配额监控键 |
| Precedence | 可选 | 优先级 |

规则：如果可选AVP被删除但之前已提供，之前的信息保留有效。Flow-Information/Flows AVP如果重新提供则替换所有之前的值。

### K225: Charging-Rule-Install与Charging-Rule-Remove
> 来源: Charging-Rule-Install_30780111, Charging-Rule-Remove_30780115

**协议知识**

Charging-Rule-Install（AVP 1001, Grouped）：
- 功能：激活、安装或修改PCC规则（PCRF→PCEF）
- 安装新规则或修改已安装规则：使用Charging-Rule-Definition
- 激活预定义规则：使用Charging-Rule-Name或Charging-Rule-Base-Name
- GPRS场景：包含Bearer-Identifier
- 可含Rule-Activation-Time/Rule-Deactivation-Time控制生效时间

Charging-Rule-Remove（AVP 1002, Grouped）：
- 功能：去激活或删除PCC规则（PCRF→PCEF）
- 使用Charging-Rule-Name删除特定PCC规则
- 使用Charging-Rule-Base-Name去激活预定义规则组

### K226: Online AVP与Offline AVP
> 来源: Online_30780172, Offline_30780170

**协议知识**

Online AVP（AVP 1009, 枚举型）：
- DISABLE_ONLINE (0)：PCC规则在线计费接口禁用
- ENABLE_ONLINE (1)：PCC规则在线计费接口使能
- 在Charging-Rule-Definition中：定义PCC规则是否使能在线计费
- 在initial CCR中：指示PCEF预配置的在线计费方式是否可用
- 在initial CCA中：指示默认在线计费方式，PCRF下发的优先级高于PCEF预配置

Offline AVP（AVP 1008, 枚举型）：
- DISABLE_OFFLINE (0)：PCC规则离线计费接口禁用
- ENABLE_OFFLINE (1)：PCC规则离线计费接口使能
- 规则同Online AVP

### K227: Metering-Method AVP
> 来源: Metering-Method_30780162

**协议知识**

Metering-Method AVP（AVP 1007, 枚举型）定义离线计费的计量参数：

| 取值 | 含义 |
|------|------|
| DURATION (0) | 测量持续时间 |
| VOLUME (1) | 测量流量 |
| DURATION_VOLUME (2) | 同时测量持续时间和流量 |

- PCEF在decentralized unit determination中将该AVP用于在线计费
- 删除后之前提供的信息保持有效；之前未提供则使用PCEF预配置的默认计量方法

### K228: Reporting-Level AVP
> 来源: Reporting-Level_30780217

**协议知识**

Reporting-Level AVP（AVP 1011, 枚举型）定义PCEF上报配额的等级：

| 取值 | 含义 | 条件 |
|------|------|------|
| SERVICE_IDENTIFIER_LEVEL (0) | 基于SID+RG联合等级 | CRD中提供Service-Identifier和Rating-Group |
| RATING_GROUP_LEVEL (1) | 基于费率组等级 | CRD中提供Rating-Group |

- 未携带但之前已提供，则之前的值保持有效
- 未携带且之前未提供，使用PCEF预配置的默认上报等级

### K229: Rating-Group AVP
> 来源: Rating-Group_30780210

**协议知识**

Rating-Group AVP（AVP 432, Unsigned32类型）：
- 包含费率组的标识
- 同一费率类型的所有业务属于同一费率组
- 请求相关的特定费率组被联合的Service-Context-Id和Rating-Group AVPs唯一标识
- 参考：RFC 4006 8.29章节

### K230: Usage-Monitoring-Information AVP
> 来源: Usage-Monitoring-Information_30780269

**协议知识**

Usage-Monitoring-Information AVP（AVP 1067, Grouped类型）包含配额监控信息：

| 子信元 | 功能 |
|--------|------|
| Monitoring-Key | 监控键值，标识一个配额监控实例 |
| Granted-Service-Unit | CHF/PCRF授权的服务单元（配额） |
| Used-Service-Unit | PCEF/SMF已使用的服务单元 |
| Usage-Monitoring-Level | 监控级别（Session级/PCC规则级） |
| Usage-Monitoring-Report | 上报指示 |
| Usage-Monitoring-Support | 监控支持指示 |

### K231: Usage-Monitoring-Level AVP
> 来源: Usage-Monitoring-Level_30780270

**协议知识**

Usage-Monitoring-Level AVP（AVP 1068, 枚举型）：

| 取值 | 含义 |
|------|------|
| SESSION_LEVEL (0) | 配额监控实例应用于整个IP-CAN会话（会话级FUP） |
| PCC_RULE_LEVEL (1) | 配额监控实例应用于一个或多个PCC规则（业务级FUP） |

- 默认值：未提供时指示PCC_RULE_LEVEL (1)

### K232: Usage-Monitoring-Report AVP
> 来源: Usage-Monitoring-Report_30780271

**协议知识**

Usage-Monitoring-Report AVP（AVP 1069, 枚举型）：
- USAGE_MONITORING_REPORT_REQUIRED (0)：PCRF指示PCEF应该上报累积流量
- 用于PCRF在RAR/CCA中请求PCEF上报特定监控键值的累积流量（无论门限是否到达）

### K233: Event-Trigger AVP关键计费触发器
> 来源: Event-Trigger_30780128

**协议知识**

Event-Trigger AVP（AVP 1006, 枚举型）与计费相关的关键触发器：

| 取值 | 名称 | 计费关联 |
|------|------|----------|
| 0 | SGSN_CHANGE | SGSN变更触发PCC规则更新 |
| 2 | RAT_CHANGE | RAT变更触发PCC规则更新 |
| 4 | PLMN_CHANGE | PLMN变更触发PCC规则更新 |
| 13 | USER_LOCATION_CHANGE | 用户位置变更（CGI/SAI/RAI/TAI/ECGI） |
| 14 | NO_EVENT_TRIGGERS | PCRF不需要事件触发通知 |
| 17 | REVALIDATION_TIMEOUT | 重新验证超时触发 |
| 25 | UE_TIME_ZONE_CHANGE | UE时区变更 |
| 26/27 | TAI_CHANGE | TAI变更（R940=27, R970=26） |
| 27/28 | ECGI_CHANGE | ECGI变更 |
| 28/29 | CHARGING_CORRELATION_EXCHANGE | 上报接入网计费标识 |
| 26/33 | USAGE_REPORT | 配额监控上报（R940=26, R970=33） |
| 39 | APPLICATION_START | 应用流量检测开始 |
| 40 | APPLICATION_STOP | 应用流量检测结束 |
| 45 | ACCESS_NETWORK_INFO_REPORT | 接入网络信息上报 |
| 101 | TETHERING_REPORT | Tethering检测上报 |
| 1003 | CELL_CONGESTION_CHANGE | 小区状态变更（华为私有） |

USAGE_REPORT触发器与Usage Monitoring（FUP）直接关联：PCRF下发Monitoring-Key+Granted-Service-Unit，PCEF上报Used-Service-Unit。

---

## 统计表

| 段 | 知识条目 | 数量 | 来源篇数 |
|----|----------|------|----------|
| 一、Nchf融合计费服务操作 | K190-K202 | 13 | 5 |
| 二、N40信元 | K203-K208 | 6 | 8 |
| 三、PFCP/N4 URR操作与信元 | K209-K223 | 15 | 15 |
| 四、Gx计费相关AVP | K224-K233 | 10 | 12 |
| **合计** | K190-K233 | **44** | **40** |

---

## 跨协议映射关系摘要

### Gx→Nchf→N4参数映射链

| Gx AVP | Nchf N40信元 | N4 PFCP信元 |
|--------|-------------|-------------|
| Online=ENABLE_ONLINE | quotaManagementIndicator=ONLINE_CHARGING | Create URR含Volume/Time/Event Quota |
| Online=DISABLE_ONLINE | quotaManagementIndicator=OFFLINE_CHARGING | Create URR不含配额信元 |
| Offline=ENABLE_OFFLINE | (离线路径) | (离线路径) |
| Metering-Method=DURATION | grantedUnit.time | Time Quota |
| Metering-Method=VOLUME | grantedUnit.totalVolume | Volume Quota |
| Metering-Method=DURATION_VOLUME | grantedUnit.time+totalVolume | Time Quota+Volume Quota |
| Rating-Group | multipleUnitUsage.ratingGroup | (SMF映射到URR ID) |
| Reporting-Level=SERVICE_IDENTIFIER_LEVEL | UsedUnitContainer.serviceId+ratingGroup | (N4无对应，SMF层处理) |
| Reporting-Level=RATING_GROUP_LEVEL | UsedUnitContainer.ratingGroup | (N4无对应，SMF层处理) |
| Monitoring-Key | (5G: UsageMonitoringData动作组) | (5G: 独立UM URR) |
| Usage-Monitoring-Level=SESSION_LEVEL | (5G: 会话级UM) | (5G: 会话级UM URR) |
| Usage-Monitoring-Level=PCC_RULE_LEVEL | (5G: 业务级UM) | (5G: 业务级UM URR) |

### Trigger映射链

| Gx Event-Trigger | Nchf Trigger Type | N4 Reporting Trigger |
|-------------------|-------------------|---------------------|
| USAGE_REPORT | (Usage Monitoring机制) | (配额阈值/耗尽触发) |
| USER_LOCATION_CHANGE | USER_LOCATION_CHANGE | (SMF层Query URR) |
| REVALIDATION_TIMEOUT | VALIDITY_TIME | (SMF本地定时器) |
| CHARGING_CORRELATION_EXCHANGE | - | (N4 Session Report) |
| (配额相关) | QUOTA_THRESHOLD | VOLTH/TIMTH |
| (配额相关) | QUOTA_EXHAUSTED | VOLQU/TIMQU |
| (配额保持) | - | QUHTI |
