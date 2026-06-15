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

