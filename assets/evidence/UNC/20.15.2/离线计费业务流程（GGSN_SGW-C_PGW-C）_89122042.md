# 离线计费业务流程（GGSN/SGW-C/PGW-C）

- [离线计费流程](#ZH-CN_TOPIC_0289122042__1.3.2.1)
- [CG交互流程](#ZH-CN_TOPIC_0289122042__1.3.3.1)

> **说明**
> 离线计费适用于GGSN、SGW、PGW，此处以EPC网络为例详细介绍具体实现，2/3G网络实现原理相同部分不再重复介绍，仅适用于SGSN的原理内容单独章节介绍。

#### [离线计费流程](#ZH-CN_TOPIC_0289122042)

离线计费流程如 [图1](#ZH-CN_TOPIC_0289122042__fig1498485792219) 所示。

**图1** 离线计费流程

<br>

![](离线计费业务流程（GGSN_SGW-C_PGW-C）_89122042.assets/zh-cn_image_0292358300_2.png)

1. 用户发起承载建立请求。
2. SGW-C/PGW-C发送PFCP Session Establishment Request消息，请求建立PFCP会话。消息中携带Create URR（Usage Reporting Rule）信元组，指示计费相关信息。Create URR包含的主要子信元如[表1](#ZH-CN_TOPIC_0289122042__table5217133513420)：
  *表1 Create URR包含的主要子信元*

  | 子信元 | 信元解释 |
  | --- | --- |
  | URR ID | 唯一标识一个Create URR。 |
  | Measurement Method | 标识计费方式，包括流量计费、时长计费或事件计费。 |
  | Reporting Triggers | 标识计费上报的触发条件，包含Periodic Reporting（定期上报）、Volume Threshold（流量阈值）、Time Threshold（时间阈值）、Linked Usage Reporting（关联URR）等。 |
  | Volume Threshold | 标识流量阈值，包含总流量、上行流量和下行流量。 |
  | Time Threshold | 标识时间阈值。 |
  | Event Threshold | 标识事件阈值。 |
  | Linked URR ID | 上报某个URR时，也会上报其关联的URR，例如A link B，当B上报时，也会上报A。 |
3. SGW-U/PGW-U返回PFCP Session Establishment Response消息，PFCP会话建立成功。
4. 用户承载建立成功。
5. 用户访问数据业务，当到达下发的阈值时，SGW-U/PGW-U发送PFCP Session Report Request消息，消息中携带Usage Report信元组，记录用户使用的流量、时间等信息。Usage Report包含的主要子信元如[表2](#ZH-CN_TOPIC_0289122042__table18994141118495)：
  *表2 Usage Report包含的主要子信元*

  | 子信元 | 信元解释 |
  | --- | --- |
  | URR ID | 标识上报的URR。 |
  | UR-SEQN | 唯一标识URR的Usage Report。 |
  | Start Time | 起始时间。 |
  | End Time | 结束时间。 |
  | Volume Measurement | 标识流量使用情况，包含总流量、上行流量和下行流量。 |
  | Duration Measurement | 标识时长使用情况。 |
  | Time of First Packet | 首包时间。 |
  | Time of Last Packet | 尾包时间。 |
6. SGW-C/PGW-C返回PFCP Session Report Response响应消息。
7. SGW-C/PGW-C在话单中记录用户使用的流量、承载的持续时间等信息，当达到话单关闭条件后产生原始话单，通过Data Record Transfer Request消息将话单发送到CG，话单详细信息请参考[离线计费话单（GGSN/SGW-C/PGW-C）](../../../../../业务专题/5G Core 计费解决方案/计费解决方案概述/计费原理/Ga_Gy接口离线_在线计费/Ga接口离线计费原理/离线计费话单（GGSN_SGW-C_PGW-C）_01_10017.md)。
8. CG返回Data Record Transfer Response响应消息。

#### [CG交互流程](#ZH-CN_TOPIC_0289122042)

SGW-C/PGW-C与CG之间交互的消息如 [图2](#ZH-CN_TOPIC_0289122042__fig1364310619378) 所示。

**图2** SGW-C/PGW-C与CG的交互流程

<br>

![](离线计费业务流程（GGSN_SGW-C_PGW-C）_89122042.assets/zh-cn_image_0292358297_2.png)

SGW-C/PGW-C采用向CG服务器池中的CG发送消息的方式探测CG的状态，机制如下：

1. SGW-C/PGW-C在配置完CG数据后（ **ADD CG** ），会主动向CG发送Node Alive Request消息，如果没有收到Node Alive Response响应消息，则重发，直到收到响应为止。
2. SGW-C/PGW-C会根据Echo消息响应情况判断链路状态。SGW-C/PGW-C固定每隔一分钟发送Echo Request消息给CG，缺省3次（通过 **SET CDRTRANSFER** 设置）没有收到CG响应，则认为物理链路状态异常，触发告警 **ALM-81021 CG无响应** ，否则认为正常。
3. SGW-C/PGW-C产生话单后，如果CG状态正常，会将话单发送到CG；如果UNC没有收到话单响应消息，则根据重发时间间隔和重发次数（通过 **SET CDRTRANSFER** 设置）发送话单，超时后会认为CG状态不正常。
4. CG故障或负载过重的情况下，会给SGW-C/PGW-C发送Redirection Request消息，通知SGW-C/PGW-C将话单重定向到另外一个CG上。

根据上述链路通断判断机制，SGW-C/PGW-C对与CG的链路状态进行采样统计，分别统计采样周期内链路通、断次数。当通断次数比高于门限值80%时，则认为链路状态是高通态；当在80%～50%之间时认为是低通态；当在50%以下时认为是阻塞态。

根据SGW-C/PGW-C与CG链路通断比动态、平滑调整话单传送速率，可以避免急停急起对CG的冲击，也可大幅度降低对CG链路闪断的误判。

- 高通态时允许话单发送，允许历史缓存话单发送。
- 低通态时允许话单发送，但不允许历史缓存话单发送。
- 阻塞态时禁止话单发送。
