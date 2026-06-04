# 融合知识库 Part B — Nchf/N40接口、PFCP/N4接口、Gx/PCC、规则匹配、Usage Monitoring

> 本文件融合自6份知识草稿（draft-batch-01/03-02/04/05-01/05-02/07）。
> 编号从 K101 起续接 Part A。

---

## 第七章：Nchf融合计费服务（N40接口）

### K101: Nchf_ConvergedCharging四种服务操作 [协议]
> 来源: K04, K190

| 服务操作 | 功能 | 发起方 | 对应融合计费消息 | 对应4G消息 |
|----------|------|--------|------------------|------------|
| Nchf_ConvergedCharging_Create | 计费会话建立 | SMF | Charging Data Request/Response [Initial] | CCR-I / CCA-I |
| Nchf_ConvergedCharging_Update | 计费会话更新（配额申请/上报/VT等） | SMF | Charging Data Request/Response [Update] | CCR-U / CCA-U |
| Nchf_ConvergedCharging_Release | 计费会话结束 | SMF | Charging Data Request/Response [Termination] | CCR-T / CCA-T |
| Nchf_ConvergedCharging_Notify | 重授权/去活通知 | CHF | Charging Notify Request/Response | RAR / RAA |

CHF职责：配额管理、重授权触发条件下发、通知服务、接受用量报告、生成CHF-CDR话单。
SMF职责：请求并接收配额、发送用量报告、处理配额重授权或终止通知。

---

### K102: CHF选择优先级（6级） [配置]
> 来源: K08, K51, K191

SMF选择CHF的优先级从高到低：

| 优先级 | 选择方式 | 配置命令 | 说明 |
|--------|----------|----------|------|
| 1 | 基于IMSI拨测选择 | `ADD SELCHFGBYIMSI` | 拨测场景专用 |
| 2 | 基于IMSI号段选择 | - | 多CHF组负载均衡 |
| 3 | PCF下发的chargingInfo | - | 域名需查本地配置，IP直接使用 |
| 4 | UDM签约CC → 本地CHF | - | DNN/APN级CC优先于Session级CC |
| 5 | NRF发现CHF | - | 仅支持优先级/权重，不支持主备 |
| 6 | 本地配置CC选择CHF | `ADD SELECTCHFGBYCC` | 最低优先级兜底 |

---

### K103: Charging Data Request [Initial] 关键信元 [协议]
> 来源: K53, K192

Create Request关键信元：

| 信元 | 说明 |
|------|------|
| invocationSequenceNumber | 请求序号（首次为0） |
| nfConsumerIdentification | NF消费者标识（含nFIPv4/v6Address、nFName、nodeFunctionality=SMF） |
| invocationTimeStamp | 请求发送时间 |
| multipleUnitUsage | 配额管理请求/用量报告数组 |
| -- ratingGroup | 费率组标识 |
| -- requestedUnit | 配额申请（在线计费携带，离线计费不携带） |
| -- uPFID | UPF标识 |
| pDUSessionChargingInformation | PDU会话计费信息 |
| -- chargingId | PDU会话计费标识 |
| -- pduSessionInformation | 含chargingCharacteristics、startTime等 |
| -- unitCountInactivityTimer | 配额不活跃定时器 |
| notifyUri | 接收CHF Notify消息的SMF URI |

时间戳计算方式：`SET CNVRGDCHGPARA`的`TIMEROUNDMODE`参数控制——ROUNDOFF（四舍五入，默认）/ ROUNDDOWN（向下取整）。

---

### K104: Charging Data Response [Initial] 关键信元 [协议]
> 来源: K53, K193

Create Response关键信元：

| 信元 | 说明 |
|------|------|
| invocationSequenceNumber | 响应序号 |
| multipleUnitInformation | 数组 |
| -- resultCode | 结果码（SUCCESS等） |
| -- ratingGroup | 费率组标识 |
| -- grantedUnit | 授权配额（totalVolume字节 + time秒） |
| -- triggers | CHF下发的trigger全集（triggerType + triggerCategory） |
| -- timeQuotaThreshold | 时间配额门限（秒） |
| -- volumeQuotaThreshold | 流量配额门限（字节） |

Trigger类型示例：QUOTA_THRESHOLD（到达阈值）、QUOTA_EXHAUSTED（配额耗尽）。
TriggerCategory: IMMEDIATE_REPORT（立即上报）。

异常响应处理：`SET CNVRGDCHGPARA`的`BADRSPACT=CONTINUE`时，用户业务继续但不进行配额管理。

---

### K105: 在线计费与离线计费的信元差异 [隐性规则]
> 来源: K54, K194

| 维度 | 在线计费 | 离线计费 |
|------|----------|----------|
| Create Request | 含requestedUnit | **不含**requestedUnit |
| Create Response | 含grantedUnit、阈值、配额Trigger | **不含**grantedUnit/threshold/unitQuotaThreshold，不含QUOTA_THRESHOLD/QUOTA_EXHAUSTED |
| Update Request | quotaManagementIndicator=ONLINE_CHARGING，含requestedUnit | quotaManagementIndicator=OFFLINE_CHARGING，不含requestedUnit |
| PFCP Create URR | 含Volume Quota/Time Quota/Event Quota | **不含**配额信元 |

核心区别：在线计费申请配额（有配额管理），离线计费仅申请计费参数（无配额管理）。

---

### K106: 计费会话更新四种触发场景 [方案设计]
> 来源: K55, K197

| 触发场景 | 说明 | 关键流程 |
|----------|------|----------|
| UPF内部事件 | 配额耗尽/到达阈值、配额空闲时间门限、访问无配额新业务 | UPF Usage Report → SMF → CHF → 新配额 → UPF |
| SMF内部事件 | 在线配额有效时长超期（`ADD CCT`配置RG级有效时长） | SMF查询UPF用量 → CHF → 新配额 → UPF |
| 外部事件 | 接入条件更新（Serving Node变更、PRA变更、QoS改变、位置更新、时区改变、PLMN变更） | UE→SMF→UPF查询→CHF→新配额→UPF |
| CHF重授权 | 用户充值成功等场景CHF通知SMF重新申请配额 | CHF Notify → SMF查询UPF→CHF→新配额→UPF |

SMF上报方式：`SET CNVRGDCHGPARA`的`RPTBASEDONGU`参数——不使能时基于实际使用量上报；使能则基于GrantedUnit做配额管理，用量不超过下发配额。

UPF定时器保护：触发上报后启动定时器 = `T3RESPONSE * N3REQUEST + 4s`（`SET UPPFCPPATH`配置）；超时未收到配额更新则UPF阻塞业务。

---

### K107: Charging Data Update Request关键信元 [协议]
> 来源: K199

Update Request中的multipleUnitUsage包含：

| 信元 | 说明 |
|------|------|
| ratingGroup | 费率组 |
| requestedUnit | 配额申请（在线计费） |
| UsedUnitContainer | 已用配额容器 |

UsedUnitContainer子信元：

| 子信元 | 说明 |
|--------|------|
| totalVolume / downlinkVolume / uplinkVolume | 流量使用量 |
| time | 时长使用量 |
| quotaManagementIndicator | ONLINE_CHARGING / OFFLINE_CHARGING |
| serviceId | 服务标识 |
| triggers | 当前触发类型（仅一个，取优先级最高） |
| triggerTimestamp | 触发时间 |
| localSequenceNumber | 本地序号 |
| pDUContainerInformation | 含timeofFirstUsage/timeofLastUsage/rATType/userLocationInformation |

**隐性规则**：请求消息的triggerType只能携带一个，表示由哪个trigger触发；多个trigger同时满足时携带优先级最高的一个。

---

### K108: CHF下发的Trigger全集与优先级 [隐性规则]
> 来源: K56, K200

- CHF在Response中携带triggerType全集（如QUOTA_THRESHOLD + QUOTA_EXHAUSTED），与Request由哪个trigger触发无关
- SMF本地也可配置Trigger（`ADD PDUTRIGGER`/`ADD RGTRIGGER`），优先级低于CHF下发的
- 外部事件触发场景CHF可额外下发Session级Trigger：VOLUME_LIMIT、TIME_LIMIT、USER_LOCATION_CHANGE等
- CHF Response还可能携带：validityTime（配额有效时间）、sessionFailover（FAILOVER_SUPPORTED）、invocationResult.failureHandling（CONTINUE）

RG级VT事件合并：`SET CNVRGDCHGPARA`的`MERGERGVTSW=ENABLE`时，同时发生的RG级VT事件合并上报CHF。

---

### K109: 计费会话释放流程 [协议]
> 来源: K57, K201

UE发起释放流程：

1. UE发起PDU会话释放
2. SMF→UPF: PFCP Session Deletion Request
3. UPF→SMF: Deletion Response（携带计费统计信息）
4. SMF→CHF: ChargingDataRelease Request（含final用量）
5. CHF扣费处理，关闭CHF-CDR
6. CHF返回Release Response

Release Request特有信元：
- stopTime: PDU会话停止时间
- sessionStopIndicator: true（指示PDU会话终止）
- triggerType: FINAL（正常去活）

离线计费场景：quotaManagementIndicator=OFFLINE_CHARGING。

---

### K110: CHF Notify通知（重授权与去活） [协议]
> 来源: K59, K202

**CHF发起重授权（仅在线计费）：**

1. CHF→SMF: ChargingDataNotify Request（notificationType=REAUTHORIZATION, 含reauthorizationDetails: [{quotaManagementIndicator, ratingGroup}]）
2. SMF→CHF: Notify Response (204 No Content)
3. SMF→UPF: PFCP Session Modification（Query URR查询用量）
4. UPF→SMF: Modification Response（上报用量）
5. SMF→CHF: ChargingDataUpdate Request（请求重授权）
6. CHF→SMF: Update Response（新配额+新Trigger）

**CHF发起用户去活（所有计费类型）：**

1. CHF→SMF: Notify Request（notificationType=ABORT_CHARGING）
2. SMF→UPF: PFCP Session Deletion Request
3. UPF→SMF: Deletion Response（配额用量）
4. SMF→CHF: ChargingDataRelease Request（携带用量）
5. CHF扣费关闭CDR，返回Release Response
6. SMF发起PDU会话释放

---

### K111: 异常去活的triggerType填写规则 [隐性规则]
> 来源: K58

| 去活场景 | triggerType值 |
|----------|---------------|
| 正常去活 | FINAL |
| 异常去活（有`ADD N40DIAGTRIGGER`） | 按RELEASETRIGGER参数配置 |
| 异常去活（无N40DIAGTRIGGER，`SET CNVRGDCHGPARA` SPTABNTRIGGER=ENABLE） | AbnormalRelease |
| 异常去活（无N40DIAGTRIGGER，SPTABNTRIGGER=DISABLE） | FINAL |

优先级：`ADD N40DIAGTRIGGER` > `SET CNVRGDCHGPARA` SPTABNTRIGGER。

---

### K112: SMF维护RG与URR ID的映射关系 [原理]
> 来源: K195, K258

| 接口 | 方向 | RG/URR角色 |
|------|------|------------|
| Nchf（SMF→CHF） | SMF→CHF申请配额 | 按RG粒度申请配额，按RG或RG+SID粒度上报配额 |
| Nchf（CHF→SMF） | CHF→SMF下发配额 | 按RG粒度下发配额 |
| N4（SMF→UPF） | SMF→UPF下发URR | URR包含计费事件和计费参数，UPF按URR向SMF上报配额用量 |

关键映射规则：
- **所有RG都有对应的URR ID**
- 但URR并不都用于计费，**非计费的URR ID没有对应的RG**
- SMF负责维护RG与URR ID之间的映射关系

计费会话创建触发方式：默认在PDU会话建立时触发，可通过`SET CHFINIT`命令的`CHFINIT`参数配置为业务使用时触发。

---

### K113: UPF分配IP vs SMF分配IP的计费会话创建差异 [方案设计]
> 来源: K196

- **UPF分配IP**：先建立PFCP会话（SMF→UPF），UPF分配IP后返回，SMF再向CHF发Create Request，然后PFCP会话修改下发URR
- **SMF分配IP**：SMF直接携带用户IP向CHF发Create Request，CHF返回配额后，SMF向UPF发PFCP Session Establishment（含Create PDR/FAR/URR一步到位）

---

### K114: N40关键信元——multipleUnitUsage [协议]
> 来源: K203

- 定义：包含配额管理请求的相关参数以及/或者用量报告
- 数据类型：数组，每项包含ratingGroup、requestedUnit、usedUnitContainer、uPFID
- 应用场景：ChargingDataCreate/Update/Release Request、ChargingDataNotify Request
- 参考：3GPP TS 32.291

---

### K115: N40关键信元——quotaManagementIndicator [协议]
> 来源: K204

- 定义：表示重授权通知是否用于配额管理控制
- 枚举值：ONLINE_CHARGING（要求配额管理控制）/ OFFLINE_CHARGING（无配额管理控制）
- 应用场景：ChargingDataNotify Request（CHF→SMF通知消息）

---

### K116: N40关键信元——quotaHoldingTime [协议]
> 来源: K205

- 定义：限制配额保持时间（秒），同时限制时间配额和流量配额
- 含义：当观察不到与配额相关的流量时，SMF认为该配额已过期
- 特殊值：0表示不使用该机制
- 默认值：信元不存在时使用SMF本地配置的默认值
- 应用场景：ChargingDataCreate Response

---

### K117: N40关键信元——配额阈值三件套 [协议]
> 来源: K206

| 信元 | 含义 | 单位 | 数据类型 |
|------|------|------|----------|
| timeQuotaThreshold | 授权的时间配额阈值 | 秒 | 整型 |
| volumeQuotaThreshold | 授权的流量配额阈值 | 字节 | 无符号整型 [0, 2^64-1] |
| unitQuotaThreshold | 授权的事件计费配额阈值 | 次 | 整型 |

均出现在ChargingDataCreate Response中，由CHF下发给SMF。阈值到达时触发QUOTA_THRESHOLD事件，SMF向CHF更新计费会话。

---

### K118: N40关键信元——qosFlowsUsageReports [协议]
> 来源: K207

- 定义：每个QFI的容器清单，包含上报用量
- 子信元：qFI、startTimestamp、endTimestamp、downlinkVolume、uplinkVolume
- 应用场景：ChargingDataCreate Request

---

### K119: N40关键信元——rANSecondaryRATUsageReport [协议]
> 来源: K208

- 定义：指示无线侧上报的Secondary RAT usage值
- 子信元：rANSecondaryRATType（如NR）、qosFlowsUsageReports
- 应用场景：ChargingDataCreate Request

---

### K120: 多UPF配额管理 [方案设计]
> 来源: K64

华为融合计费只支持CHF管理方式：每个UPF独立配额。

- SMF在每个UPF基础上请求配额（`Multiple Unit Usage`携带`UPF ID`）
- 哪个UPF请求配额，配额就授予哪个UPF
- I-UPF和UL CL UPF不下发配额
- 只有主锚点(PSA1)和辅助锚点(PSA2)需要配额管理

---

### K121: MEC计费流程 [方案设计]
> 来源: K65

架构：UL CL + PSA1(主锚点) + PSA2(辅锚点)
- UL CL UPF没有计费规则，不进行计费
- PSA1和PSA2各自独立申请配额
- SMF按UPF独立请求CHF（携带UPF ID）
- 本地DN通过PSA2，互联网通过PSA1

---

## 第八章：PFCP/N4接口与URR

### K122: URR定义与关键参数 [原理]
> 来源: K47

URR（Usage Reporting Rule / 使用量上报规则）：SMF通过N4(PFCP)向UPF下发的规则，指示UPF测量和报告网络资源使用情况。

- 测量维度：流量(Volume)、时长(Duration)、事件(Event)
- 上报触发：阈值到达、周期性、应请求上报

URR关键参数：URR ID, Measurement Method, Reporting Triggers, Volume Quota, Time Quota, Volume Threshold, Time Threshold, Linked URR ID, Measurement Information。

---

### K123: URR生命周期——Create/Update/Remove [协议]
> 来源: K209, K210, K211

**Create URR**必选信元：URR ID、Measurement Method、Reporting Triggers。

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

**Update URR**与Create URR的差异：
- URR ID仍为必选（标识要修改的URR）
- 其余信元为条件必选（"如果需要修改xxx，该信元应出现"）
- 新增FAR ID for Quota Action：URR中新增配额且UPF支持配额动作时可能出现
- Aggregated URRs在Update时提供完整列表（替换而非增量）

**Remove URR**仅包含一个必选信元：URR ID。用于去激活或删除PFCP会话中的URR，触发PFCP Session Modification Response上报终止用量报告（TERMR触发）。

---

### K124: URR ID信元与编码规则 [协议]
> 来源: K212

- 功能：在PFCP会话配置的所有URR中唯一标识一个URR
- 第5字节bit8含义：
  - 0：Rule由控制面功能（SMF）动态分配
  - 1：Rule在用户面功能（UPF）中预定义

---

### K125: Usage Report Trigger完整编码（3字节位图） [协议]
> 来源: K213

**第5字节（bit1-8）：**

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

**第6字节（bit1-8）：**

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

**第7字节：** bit1: EVEQU（事件配额耗尽），bit2-8备用。

至少一个bit为1，可多个bit同时为1。

---

### K126: Measurement Method信元 [协议]
> 来源: K214

- 功能：指示测量网络资源使用情况的方法
- 第5字节编码：
  - bit1 DURAT：时长测量
  - bit2 VOLUM：流量测量
  - bit3 EVENT：事件测量
  - bit4-8：备用
- 至少一个bit为1，可多个bit同时为1（如DURATION_VOLUME对应DURAT+VOLUM）

---

### K127: Volume Measurement信元 [协议]
> 来源: K215

- 功能：指示测量的话务量
- 第5字节编码：
  - bit1 TOVOL：Total Volume字段存在
  - bit2 ULVOL：Uplink Volume字段存在
  - bit3 DLVOL：Downlink Volume字段存在
- Total/Uplink/Downlink Volume编码为Unsigned64，单位字节

---

### K128: Duration Measurement信元 [协议]
> 来源: K216

- 功能：指示已用时间
- 单位：秒

---

### K129: Volume Quota与Time Quota信元 [协议]
> 来源: K217, K218

**Volume Quota：**
- 功能：指示UPF需要监控的流量配额
- 编码同Volume Measurement（TOVOL/ULVOL/DLVOL标志位+对应值）
- Unsigned64类型，单位字节

**Time Quota：**
- 功能：指示UPF需要监控的时间配额
- 单位：秒

---

### K130: Reporting Triggers信元（N4接口） [协议]
> 来源: K219

N4接口的Reporting Triggers编码与Usage Report Trigger基本一致但略有差异：

- 第5字节：PERIO/VOLTH/TIMTH/QUHTI/START/STOPT/DROTH/LIUSA
- 第6字节：VOLQU/TIMQU/ENVCL/MACAR/EVETH/EVEQU

与Usage Report Trigger的差异：第5字节bit8是LIUSA（非IMMER），第6字节bit3是ENVCL（非TERMR），bit4是MACAR（非MONIT），无第7字节。

---

### K131: Quota Holding Time信元（N4接口） [协议]
> 来源: K49, K205, K220

- 功能：指示配额保持时间
- 单位：秒
- 含义：在给定不活动期间没有收到数据包时，不再允许数据包传输，触发QUHTI上报
- 特殊值：QHT=0禁用该机制
- 适用于流量和时长计费

**在线计费**：QHT到期=SMF不请求配额，配额仅在下一次业务活动时请求。
**离线计费**：QHT到期=触发关闭当前业务容器。
**N40接口**：CHF在Create Response中下发quotaHoldingTime，SMF映射到N4的Quota Holding Time下发给UPF。

---

### K132: Aggregated URRs信元（信用池机制） [协议]
> 来源: K221

- 功能：支持URR信用池（多个URR共享同一配额）
- 子信元：
  - Aggregated URR ID：共享信用池的聚合URR ID（必选）
  - Multiplier：乘法器，应用于测量抽象业务单元从信用池中消耗的流量（必选）
- 使用场景：多个业务共享一个总配额池，按不同权重消耗

---

### K133: Linked URR ID信元 [协议]
> 来源: K222

- 功能：指示Linked URR的ID
- 机制：上报某个URR时，也会上报其关联的URR。例如A link B，当B上报时也会上报A
- 可存在多个相同类型的信元表示与该URR相关的多个链接URR

---

### K134: Subsequent Volume Quota信元 [协议]
> 来源: K223

- 功能：指示UPF在监控时间（Monitoring Time）之后仍需要监控的流量配额
- 编码同Volume Quota（TOVOL/ULVOL/DLVOL标志位+对应值）
- 前提：存在Monitoring Time信元且使用基于流量的测量

---

### K135: Usage Report信元（PFCP Session Report） [协议]
> 来源: K198

UPF上报的Usage Report包含：

| 信元 | 说明 |
|------|------|
| URR ID | 标识上报的URR |
| UR-SEQN | 唯一标识该URR的Usage Report |
| Start Time / End Time | 起止时间 |
| Volume Measurement | 总流量/上行/下行 |
| Duration Measurement | 时长使用情况 |
| Time of First Packet / Last Packet | 首尾包时间 |

Duration Measurement的ISTM标志位说明：
- ISTM=0或不携带：从UPF首次收到业务数据包开始，到业务终止结束
- ISTM=1：从UPF首次收到授权配额成功开始，到用户去激活或配额管理实例终止

配额更新超时保护：定时器 = T3RESPONSE * N3REQUEST + 4秒（`SET UPPFCPPATH`配置），超时未收到配额更新则UPF阻塞业务。

---

## 第九章：Gx/PCC策略与计费

### K136: PCC规则类别与一致性要求 [配置]
> 来源: K63, K159

| 规则类别 | PCF | SMF | UPF |
|---------|-----|-----|-----|
| 动态规则 | 定义名称+内容，下发 | 传递 | 执行 |
| 预定义规则 | 定义名称（与SMF匹配） | 匹配名称，传递 | 匹配本地配置，执行 |
| 预定义规则组 | 名称与SMF UserProfile匹配 | 定义UserProfile包含多条规则 | 匹配UserProfile，按优先级执行 |
| 本地规则 | 无关联 | 定义UserProfile | 匹配并执行 |

优先级：PCF全局优先级。相同优先级时动态>预定义。

一致性要求（SMF与UPF必须匹配）：UserProfile name、Rule name、URR ID。

---

### K137: Charging-Rule-Definition AVP结构 [协议]
> 来源: K224

Charging-Rule-Definition（AVP 1003, Grouped类型）定义PCRF发送给PCEF的PCC规则：

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

---

### K138: Charging-Rule-Install与Charging-Rule-Remove [协议]
> 来源: K225

**Charging-Rule-Install**（AVP 1001, Grouped）：
- 功能：激活、安装或修改PCC规则（PCRF→PCEF）
- 安装新规则或修改已安装规则：使用Charging-Rule-Definition
- 激活预定义规则：使用Charging-Rule-Name或Charging-Rule-Base-Name
- GPRS场景：包含Bearer-Identifier
- 可含Rule-Activation-Time/Rule-Deactivation-Time控制生效时间

**Charging-Rule-Remove**（AVP 1002, Grouped）：
- 功能：去激活或删除PCC规则（PCRF→PCEF）
- 使用Charging-Rule-Name删除特定PCC规则
- 使用Charging-Rule-Base-Name去激活预定义规则组

---

### K139: Online AVP与Offline AVP [协议]
> 来源: K158, K226

**Online AVP**（AVP 1009, 枚举型）：
- DISABLE_ONLINE (0)：PCC规则在线计费接口禁用
- ENABLE_ONLINE (1)：PCC规则在线计费接口使能
- 在initial CCR中：指示PCEF预配置的在线计费方式是否可用
- 在initial CCA中：指示默认在线计费方式，PCRF下发的优先级高于PCEF预配置

**Offline AVP**（AVP 1008, 枚举型）：
- DISABLE_OFFLINE (0)：PCC规则离线计费接口禁用
- ENABLE_OFFLINE (1)：PCC规则离线计费接口使能
- 规则同Online AVP

**互斥规则**：offline和online不能同时为true，但可同时为false（不计费）。两者都不存在或都为false时，使用PDU会话的默认计费方法。PCF下发的优先级高于SMF本地配置。

---

### K140: Metering-Method AVP [协议]
> 来源: K227

Metering-Method AVP（AVP 1007, 枚举型）定义离线计费的计量参数：

| 取值 | 含义 |
|------|------|
| DURATION (0) | 测量持续时间 |
| VOLUME (1) | 测量流量 |
| DURATION_VOLUME (2) | 同时测量持续时间和流量 |

- PCEF在decentralized unit determination中将该AVP用于在线计费
- 删除后之前提供的信息保持有效；之前未提供则使用PCEF预配置的默认计量方法

---

### K141: Reporting-Level AVP [协议]
> 来源: K228

Reporting-Level AVP（AVP 1011, 枚举型）定义PCEF上报配额的等级：

| 取值 | 含义 | 条件 |
|------|------|------|
| SERVICE_IDENTIFIER_LEVEL (0) | 基于SID+RG联合等级 | CRD中提供Service-Identifier和Rating-Group |
| RATING_GROUP_LEVEL (1) | 基于费率组等级 | CRD中提供Rating-Group |

未携带但之前已提供，则之前的值保持有效。未携带且之前未提供，使用PCEF预配置的默认上报等级。

---

### K142: Rating-Group AVP [协议]
> 来源: K229

Rating-Group AVP（AVP 432, Unsigned32类型）：
- 包含费率组的标识
- 同一费率类型的所有业务属于同一费率组
- 请求相关的特定费率组被联合的Service-Context-Id和Rating-Group AVPs唯一标识
- 参考：RFC 4006 8.29章节

---

### K143: Event-Trigger AVP关键计费触发器 [协议]
> 来源: K233

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
| 26/27 | TAI_CHANGE | TAI变更 |
| 27/28 | ECGI_CHANGE | ECGI变更 |
| 28/29 | CHARGING_CORRELATION_EXCHANGE | 上报接入网计费标识 |
| 26/33 | USAGE_REPORT | 配额监控上报 |
| 39 | APPLICATION_START | 应用流量检测开始 |
| 40 | APPLICATION_STOP | 应用流量检测结束 |
| 45 | ACCESS_NETWORK_INFO_REPORT | 接入网络信息上报 |
| 101 | TETHERING_REPORT | Tethering检测上报 |
| 1003 | CELL_CONGESTION_CHANGE | 小区状态变更（华为私有） |

USAGE_REPORT触发器与Usage Monitoring（FUP）直接关联：PCRF下发Monitoring-Key+Granted-Service-Unit，PCEF上报Used-Service-Unit。

---

### K144: PCF下发的计费参数全集（ChargingData） [原理]
> 来源: K157

PCF通过ChargingData动作组下发计费参数：

| 参数 | 含义 | 必选 |
|------|------|------|
| chgId | 计费控制策略数据标识 | 必选(1次) |
| meteringMethod | 离线计量方式：DURATION/VOLUME/DURATION_VOLUME/EVENT | 可选 |
| offline | 是否离线计费 | 可选 |
| online | 是否在线计费 | 可选 |
| ratingGroup | 费率组(RG) | 可选 |
| reportingLevel | 上报级别：SER_ID_LEVEL/RAT_GR_LEVEL/SPON_CON_LEVEL | 可选 |
| serviceId | 服务标识(SID) | 可选 |
| sponsorId | 赞助商标识 | 可选 |
| sdfHandl | 在线等待信用响应时是否允许通过 | 可选(仅在线) |

---

### K145: 5G动态规则必配动作组 [配置]
> 来源: K160

5G DynamicPccRule完整配置需7种动作类型：

1. FlowDescription（流描述）
2. FlowInformation（流信息）
3. TrafficControlData（flowStatus=enabled，配流描述时必须配）
4. Arp（优先级参数）
5. QoSData（带宽参数：5qi, maxbrUl, maxbrDl）
6. UsageMornitoringData（配额监控键值，业务关联配额时必须通过5G动作组下发）
7. DynamicPccRule（汇总动作）

4G/5G差异：条件组Object选择4G选"IPSession"，5G选"SmfSession"；策略类型4G为"Gx Policy"，5G为"N7 Policy"。

---

### K146: 三种规则类型对比（动态/预定义/本地） [原理]
> 来源: K16, K159

| 维度 | 动态规则 | 预定义规则 | 本地规则 |
|------|----------|------------|----------|
| 规划位置 | PCF | UPF+SMF+PCF | UPF+SMF |
| 策略决策者 | PCF | PCF | SMF |
| 流条件 | PCF配置 | UPF配置 | UPF配置 |
| 流动作 | PCF配置 | UPF配置 | UPF配置 |
| 规则名一致性 | 不需要 | PCF/SMF/UPF三侧一致 | SMF/UPF两侧一致 |
| 业务识别 | 不识别（非定向流） | UPF识别（三四层+七层） | UPF识别 |
| 计费控制 | PCF通过ChargingData下发 | UPF本地配置计费动作 | UPF本地配置 |
| 七层支持 | **不支持** | **支持** | **支持** |
| 适用场景 | 非定向流、达量限速 | 定向流（需识别特定业务） | PCF故障降级方案 |

使用场景：
- 有PCF → 动态规则+预定义规则
- 无PCF或PCF故障 → 本地规则
- 需要七层匹配 → 必须用预定义规则或本地规则

---

## 第十章：规则匹配与业务识别

### K147: 过滤条件体系 [原理]
> 来源: K14

| 过滤条件类型 | 说明 |
|------------|------|
| 三四层过滤 | 网络层/传输层协议、端口号、IP地址 |
| 七层过滤 | URL、User-Agent、method等应用层关键字段 |
| 协议/协议组 | HTTP、RTSP等应用层协议或协议组合 |
| 流过滤器 | 以上三种的组合，实现过滤逻辑 |

关键规则：
- 每条规则只能绑定一个流过滤器
- 流过滤器是其他过滤条件的集合
- 报文必须符合规则下**所有**过滤条件才算匹配成功

---

### K148: 策略类型分类 [原理]
> 来源: K15

| 策略类型 | 含义 | 典型用途 |
|---------|------|---------|
| PCC | 计费与策略控制 | 计费、禁止访问、重定向 |
| BWM | 带宽管理 | 带宽分类、限速 |
| HEADEN | 头增强 | HTTP/RTSP报文头插入字段 |
| WEBPROXY | Web代理 | 服务器地址池设置 |
| SMARTREDIRECT | 智能重定向 | CaptivePortal、DNS重写 |

关键规则：一条规则只能绑定一条策略；可按绑定的策略类型分类规则（PCC规则、BWM规则等）。

---

### K149: 规则匹配原则 [原理]
> 来源: K17, K254

1. 所有报文按规则优先级逐条匹配
2. 报文必须符合一条规则**所有**过滤条件才算成功匹配
3. **不同类型**的规则会同时匹配，每种类型至多匹配一条
4. 多个PDR时取优先级最高的PDR
5. 动态PDR与预定义PDR优先级相同时，**动态PDR优先级高于预定义PDR**

匹配维度：
- 不同类型规则间独立匹配（PCC/BWM/HEADEN各自匹配）
- 同类型规则间按优先级先后匹配，直到有一条匹配成功或全部失败

---

### K150: UPF支持的流动作组合 [原理]
> 来源: K18

UPF支持的"流"动作：计费、带宽管理、头增强、QoS等。
- 支持单个动作（仅计费）
- 支持多个动作组合（计费+FUP等）

---

### K151: 静态规则的关键一致性约束 [配置]
> 来源: K19

对于同一个预定义规则：
1. PCF、SMF和UPF上**规则标识名称**必须一致
2. SMF和UPF上的**URR ID**必须一致

这是配置正确性的前提条件。

**隐性规则**：SMF配预定义规则级则UPF配规则级；SMF配规则组级则UPF须配规则组级。

---

### K152: 预定义规则安装流程 [协议]
> 来源: K20

1. 用户开机 → PDU会话创建请求
2. SMF选择PCF → 建立SM策略偶联 → 获取SM策略
3. PCF决策 → 向SMF下发**预定义规则名称**（如Prerule01、Prerule02等）+ 动态规则 + Triggers
4. SMF选择UPF → 会话建立请求（携带预定义规则名称）
5. UPF安装预定义规则及动态规则 → 返回响应

UPF成功安装后：对接收到的报文进行业务识别 → 判断是否满足规则中的过滤条件 → 满足后按照规则关联的动作处理。

---

### K153: Usage Monitoring机制 [方案设计]
> 来源: K21

在PCF侧：向SMF下发UmData（Usage Monitoring Data），用于监控业务使用量；根据累计流量决定下发/删除规则。

在SMF侧：将UmData转换成MK（Monitoring Key）URR传递给UPF；达到上报阈值时将UPF上报的业务流量转发给PCF。

在UPF侧：对匹配的业务流量统计到对应的流量统计容器（URR）中；达到上报阈值时向SMF上报。

方案设计示例（A视频专项流量包）：
- 套餐1（视频专项）：优先计入30G A视频流量，URL+七层匹配，PCC策略
- 套餐2（视频FUP）：每天2000M以内100Mbps，超过后25Mbps，需规则动态替换
- 套餐3（通用流量）：三四层any+七层any，PCC策略
- 套餐4（通用FUP）：20G以内50Mbps，超过后1Mbps，需规则动态替换

---

### K154: 流量触发的规则动态替换 [方案设计]
> 来源: K22

当用户流量累计达到阈值时，PCF会动态更新规则：

1. PCF更新规则（删除旧规则，安装新规则）
2. SMF/UPF删除旧规则并安装新规则
3. 新规则生效后，后续报文按新策略处理

示例：
- A视频流量累计达2000M → 删除Prerule02(100Mbps) → 安装Prerule03(25Mbps)
- 通用流量累计达20G → 删除Prerule05(50Mbps) → 安装Prerule06(1Mbps)

---

### K155: 动态规则不支持七层的根本原因 [原理]
> 来源: K23

PCF作为策略控制实体，不处理用户数据报文，因此不具备七层识别能力。
UPF作为业务感知及策略执行的实体，支持通过协议特征库/解析库识别业务。

对于需要七层识别（如A视频业务的HTTP+URL特征）的场景，**必须使用预定义规则或本地规则**。

---

### K156: PDR核心定义与信息构成 [原理]
> 来源: K250

PDR（Packet Detection Rule，流检测规则）是SMF在PFCP会话建立过程中下发给UPF的，用于指示UPF识别流及流处理动作的属性集合。

| 参数 | 说明 |
|------|------|
| PDI（Packet Detection Information） | 流匹配信息，包含报文方向（source interface: 0=上行, 1=下行）和filter（SDF Filter / Application ID）。入口数据流量的对应字段与PDI中所有匹配条件全部匹配则命中 |
| FAR ID | 指示转发动作FAR ID（转发动作包含转发、缓存、重传、丢弃等） |
| QER ID | 指示流控类动作的QER ID（流控类动作如CAR） |
| URR ID | 指示统计上报类动作的URR ID |
| Precedence | PDR优先级 |
| Activate Predefined Rules | 预定义规则名称 |

PDI/FAR/QER/URR通过PDR聚合：PDI负责匹配，FAR/QER/URR分别负责转发/流控/计费动作。

---

### K157: PDR两大类型——动态PDR与预定义PDR [原理]
> 来源: K251

| 类型 | 组成 | 特点 |
|------|------|------|
| 动态PDR | PDI + FAR + QER + URR + Precedence | 所有匹配条件和动作由SMF动态下发 |
| 预定义PDR | PDI + FAR + QER + URR + Precedence + Activate Predefined Rules | 携带预定义规则名，UPF匹配本地配置 |

预定义PDR的关键特性：
- 一条预定义PDR可携带多个Activate Predefined Rules
- Activate Predefined Rules可以是UPF/PGW-U本地配置的userprofile名称，或者是本地配置的rule名称

---

### K158: PDR匹配机制——数据流转发过程中的匹配位置 [方案设计]
> 来源: K253

1. **PDR下发**：SMF向UPF下发一组PDR（通过PFCP Session Establishment Request消息），至少包含一个access类型PDR（上行）和一个core类型PDR（下行）
2. **报文到达**：用户数据报文发送至UPF
3. **会话匹配**：UPF对用户报文进行PDR匹配，查找用户所属PDU Session
4. **PDR命中**：UPF根据PDR优先级、报文关键信息（域名、IP等）进行PDR匹配
5. **动作执行**：UPF根据PDR中的相关信息或本地配置的相关规则信息，执行数据流的相关动作并转发

---

### K159: 动态PDR的两种匹配方式——动态rule vs ADC rule [原理]
> 来源: K255

| 方式 | SDF filter | Application ID | 匹配逻辑 | 动作执行 |
|------|-----------|----------------|----------|----------|
| 动态rule | 携带转发匹配条件 | 不携带 | 按SDF filter匹配报文 | 按PDR中对应动作执行流转发 |
| ADC rule | "Permit out ip from any to assigned" | 携带 | 根据Application ID匹配本地配置的Flowfilter/Flowfilter Group | 按本地的Flowfilter/Flowfilter Group配置执行流动作 |

关键区别：动态rule直接用SDF filter匹配报文字段；ADC rule通过Application ID间接匹配本地配置的Flowfilter/Flowfilter Group。

---

### K160: 预定义PDR匹配方式 [原理]
> 来源: K256

- UPF根据Activate Predefined Rules值匹配本地配置的**userprofile**或本地配置的**rule**
- 命中该PDR后，UPF按照userprofile或rule进行带宽、计费等策略控制

---

### K161: PDR与本地规则的映射关系（分流场景） [原理]
> 来源: K257

在分流特性中，PDR通过Application ID与本地配置的分流规则建立映射关系：

- 映射方式：PDR中的Application-ID值对应本地分流规则的flowfilter或flowfiltergroup名称
- 执行顺序：数据报文先匹配flowfilter/flowfiltergroup，根据Application-ID检索到分流PDR，然后按照PDR中的FAR（转发规则）、QER（QoS规则）执行策略动作
- 即：**报文 → flowfilter/flowfiltergroup匹配 → App ID → 检索PDR → 执行FAR/QER/URR动作**

---

## 第十一章：Usage Monitoring与FUP

### K162: Usage-Monitoring-Information AVP结构 [协议]
> 来源: K230

Usage-Monitoring-Information AVP（AVP 1067, Grouped类型）包含配额监控信息：

| 子信元 | 功能 |
|--------|------|
| Monitoring-Key | 监控键值，标识一个配额监控实例 |
| Granted-Service-Unit | CHF/PCRF授权的服务单元（配额） |
| Used-Service-Unit | PCEF/SMF已使用的服务单元 |
| Usage-Monitoring-Level | 监控级别（Session级/PCC规则级） |
| Usage-Monitoring-Report | 上报指示 |
| Usage-Monitoring-Support | 监控支持指示 |

---

### K163: Usage-Monitoring-Level AVP [协议]
> 来源: K231

Usage-Monitoring-Level AVP（AVP 1068, 枚举型）：

| 取值 | 含义 |
|------|------|
| SESSION_LEVEL (0) | 配额监控实例应用于整个IP-CAN会话（会话级FUP） |
| PCC_RULE_LEVEL (1) | 配额监控实例应用于一个或多个PCC规则（业务级FUP） |

默认值：未提供时指示PCC_RULE_LEVEL (1)。

---

### K164: Usage-Monitoring-Report AVP [协议]
> 来源: K232

Usage-Monitoring-Report AVP（AVP 1069, 枚举型）：
- USAGE_MONITORING_REPORT_REQUIRED (0)：PCRF指示PCEF应该上报累积流量
- 用于PCRF在RAR/CCA中请求PCEF上报特定监控键值的累积流量（无论门限是否到达）

---

### K165: 会话级FUP vs 业务级FUP对比 [原理]
> 来源: K169

| 维度 | 会话级FUP | 业务级FUP |
|------|-----------|-----------|
| 监控范围 | 用户所有业务 | 特定业务(三四层/七层) |
| N7信元位置 | sessRules.refUmData | PccRule.refUmData |
| URR绑定 | 关联到**所有PDR** | 绑定到**指定业务流PDR** |
| MONITORINGKEY | 动态规则时由PCF下发 | ADD URR中必选配置 |
| UNC/UDG配置量 | 仅需License开关 | 需完整三件套+两套策略 |
| License(UNC) | LKV3W9PCBT12 | LKV2FUPSAT01 |
| License(UDG) | LKV3G5PCBT01 | LKV3G5FPBS01 |

---

### K166: FUP配额驱动策略切换机制 [方案设计]
> 来源: K170

FUP核心机制：配额状态驱动策略切换：

1. **初始**：PCF下发流量阈值 + 规则（高优先级，低费率/免费）
2. **阈值耗尽**：UPF检测VOLTH触发，上报Usage Report → SMF转发PCF
3. **PCF决策**：
   - 配额未耗尽 → 下发新阈值，维持当前规则
   - 配额耗尽 → **不下发新阈值**(refUmData=NULL)，更新QoS(限速/重定向)，切换到低优先级规则(高费率)

**隐性规则**：FUPSESSIONEXC=ENABLE的业务流量**不参与会话级FUP累计**，避免双重计量。

---

### K167: 业务级FUP三件套扩展模型 [配置]
> 来源: K171

业务级FUP是标准三件套的**扩展版本**，需配配额耗尽前/后**两套策略**：

**三组URR：**
1. urr_mk：URRID=1000, USAGERPTMODE=MONITORINGKEY, MONITORINGKEY="2001"（累计流量监控）
2. urr_basic：URRID=2000, USAGERPTMODE=ONLINE, RG=10（配额耗尽前，免费）
3. urr_exhaust：URRID=3000, USAGERPTMODE=ONLINE, RG=20（配额耗尽后，1元/M）

**两套PCCPOLICYGRP：**
- cg_basic：绑定urrg_basic(urr_mk + urr_basic)，FUPSESSIONEXC=ENABLE
- cg_exhaust：绑定urrg_exhaust(urr_mk + urr_exhaust)，FUPSESSIONEXC=ENABLE

**两条RULE：** rule_test1(绑定cg_basic, PRIORITY=30) + rule_test2(绑定cg_exhaust, PRIORITY=40)

---

### K168: FUP URR ID与UMID映射机制 [原理]
> 来源: K172

SMF建立URR ID与UMID之间的映射：
- 预定义规则：通过ADD URR命令配置URR ID和MONITORINGKEY
- 动态规则：SMF直接将PCF下发的UMID转换为URR ID

映射流转路径：UPF检测VOLTH触发 → Usage Report(含URR ID, Volume Measurement) → SMF通过URR ID→UMID映射 → Npcf_SMPolicyControl_Update(accuUsageReports含refUmId, volUsage) → PCF决策

---

## 附录：跨协议映射关系摘要

### Gx → Nchf → N4 参数映射链

| Gx AVP | Nchf N40信元 | N4 PFCP信元 |
|--------|-------------|-------------|
| Online=ENABLE_ONLINE | quotaManagementIndicator=ONLINE_CHARGING | Create URR含Volume/Time/Event Quota |
| Online=DISABLE_ONLINE | quotaManagementIndicator=OFFLINE_CHARGING | Create URR不含配额信元 |
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
| (配额相关) | QUOTA_THRESHOLD | VOLTH / TIMTH |
| (配额相关) | QUOTA_EXHAUSTED | VOLQU / TIMQU |
| (配额保持) | - | QUHTI |

---

## 知识统计

| 章节 | 知识条目 | 数量 |
|------|----------|------|
| 第七章：Nchf融合计费服务 | K101-K121 | 21 |
| 第八章：PFCP/N4接口与URR | K122-K135 | 14 |
| 第九章：Gx/PCC策略与计费 | K136-K146 | 11 |
| 第十章：规则匹配与业务识别 | K147-K161 | 15 |
| 第十一章：Usage Monitoring与FUP | K162-K168 | 7 |
| **合计** | K101-K168 | **68** |

### 按类型统计

| 类型 | 数量 | 编号 |
|------|------|------|
| [协议] | 30 | K101, K103, K104, K107, K109, K110, K114-K119, K123-K125, K127-K130, K132-K135, K137, K138, K140-K143, K152, K162-K164 |
| [原理] | 17 | K112, K122, K144, K146-K150, K155-K157, K159-K161, K165, K168 |
| [隐性规则] | 4 | K105, K108, K111, K151 |
| [方案设计] | 10 | K106, K113, K120-K121, K153, K154, K158, K166 |
| [配置] | 7 | K102, K123, K136, K145, K151, K167 |

### 融合去重记录

| 新编号 | 融合来源 | 说明 |
|--------|----------|------|
| K101 | K04 + K190 | 四种服务操作合并 |
| K102 | K08 + K51 + K191 | CHF选择优先级保留6级版本 |
| K103 | K53 + K192 | Create Request信元合并 |
| K104 | K53 + K193 | Create Response信元合并 |
| K105 | K54 + K194 | 在线/离线信元差异合并 |
| K106 | K55 + K197 | Update触发场景合并 |
| K108 | K56 + K200 | Trigger全集与优先级合并 |
| K109 | K57 + K201 | Release流程合并 |
| K110 | K59 + K202 | Notify通知合并 |
| K112 | K195 + K258 | RG与URR ID映射合并 |
| K123 | K209 + K210 + K211 | URR生命周期三阶段合并 |
| K131 | K49 + K205 + K220 | QHT三来源合并 |
| K136 | K63 + K159 | PCC规则类别合并 |
| K139 | K158 + K226 | Online/Offline AVP合并 |
| K146 | K16 + K159 | 三种规则类型对比合并 |
| K149 | K17 + K254 | 规则匹配原则合并 |
