# CG组网可靠性（GGSN/SGW-C/PGW-C）

- [组网可靠性-CG负荷分担](#ZH-CN_TOPIC_0295094695__1.3.1.1)
- [负载可靠性-CG过载保护](#ZH-CN_TOPIC_0295094695__1.3.2.1)

#### [组网可靠性-CG负荷分担](#ZH-CN_TOPIC_0295094695)

GGSN/SGW-C/PGW-C可以通过两种方式选择CG：PCRF下发、在本地CG服务器池中选择，优先使用PCRF下发的CG，如 [图1](#ZH-CN_TOPIC_0295094695__fig089083516105) 所示。本地CG服务器支持配置CG服务器组，基于号段选择CG组。配置了CG组的CG服务器选择如 [图2](#ZH-CN_TOPIC_0295094695__fig15871819204619) 所示。

**图1** CG选择

<br>

![](CG组网可靠性（GGSN_SGW-C_PGW-C）_95094695.assets/zh-cn_image_0295097996_2.png)

**图2** 包含CG组的CG选择

<br>

![](CG组网可靠性（GGSN_SGW-C_PGW-C）_95094695.assets/zh-cn_image_0000002079088726_2.png)

*表1 CG选择方式及负荷分担方式*

| CG选择方式 | 方式说明 | CG负荷分担方式 | 负荷分担方式说明 |
| --- | --- | --- | --- |
| PCRF下发CG | PCC用户激活时，PCRF通过CCA-I消息的Primary-Charging-Collection-Function-Name AVP和Secondary-Charging-Collection-Function-Name AVP下发主备CG的IP地址和端口号给GGSN/SGW-C/PGW-C，GGSN/SGW-C/PGW-C将用户话单优先发送给PCRF下发的CG。<br>PCRF<br>下发的主备CG必须在GGSN/SGW-C/PGW-C本地已经配<br>置<br>才生效，如果PCRF下发的主备CG状态都为不可用（CG故障或过载），GGSN/SGW-C/PGW-C在本地CG服务器池中选择CG。 | - | - |
| 本地CG服务器选择CG | GGSN/SGW-C/PGW-C从对应话单版本的CG服务器池中，选择状态正常、优先级最高的CG作为发送对象。<br>在GGSN/SGW-C/PGW-C上通过将CG的优先级配置为相同值即可实现CG负荷分担，各CG共同负荷分担全部用户产生的话单。GGSN/SGW-C/PGW-C支持的CG负荷分担选择算法有两种<br>，通过**SET CDRTRANSFER**进行设置<br>。<br>GGSN/SGW-C/PGW-C支持配置CG组。如果配置了CG组，则通过号段匹配CG组。如果匹配上CG组，则在CG组内按上述原则选择CG。如果未匹配上CG组，但配置了全局CG组，则在全局CG组内按上述原则选择CG。否则，GGSN/SGW-C/PGW-C在非CG组的CG中选择状态正常、优先级最高的CG作为发送对象。 | 基于负载的负荷分担 | 用户激活时，GGSN/SGW-C/PGW-C从状态正常、优先级最高的CG中选择负载（待发送话单）最少的CG。发送话单时，无论激活时选定的CG状态是否正常，均从状态正常、优先级最高的CG中选择负载最少的CG发送话单。<br>该种方式下，对于相同优先级的CG，先配置的CG会优先被选择，后配置的CG则最后被选择，因此没有进行完全意义上的负荷分担。由于是基于负载发送话单，同一个用户的话单有可能会被发往不同的CG，处理速度快的CG接收的话单会相对多些。 |
| 本地CG服务器选择CG | GGSN/SGW-C/PGW-C从对应话单版本的CG服务器池中，选择状态正常、优先级最高的CG作为发送对象。<br>在GGSN/SGW-C/PGW-C上通过将CG的优先级配置为相同值即可实现CG负荷分担，各CG共同负荷分担全部用户产生的话单。GGSN/SGW-C/PGW-C支持的CG负荷分担选择算法有两种<br>，通过**SET CDRTRANSFER**进行设置<br>。<br>GGSN/SGW-C/PGW-C支持配置CG组。如果配置了CG组，则通过号段匹配CG组。如果匹配上CG组，则在CG组内按上述原则选择CG。如果未匹配上CG组，但配置了全局CG组，则在全局CG组内按上述原则选择CG。否则，GGSN/SGW-C/PGW-C在非CG组的CG中选择状态正常、优先级最高的CG作为发送对象。 | 基于用户的负荷分担 | 用户激活时，GGSN/SGW-C/PGW-C从状态正常、优先级最高的CG中依次选择CG。发送话单时，如果激活时选择的CG状态正常，则向此CG发送话单；如果激活时选择的CG状态不正常，则重新从状态正常、优先级最高的CG中依次选择CG发送话单。<br>该种方式下，对于相同优先级的CG，同一个用户的话单每次都发往同一个CG，不同用户的话单发送时则会轮选CG，CG负荷分担效果会更明显。 |

如果PCRF下发的CG无效，本地CG服务器池也没有可用的CG，GGSN/SGW-C/PGW-C会将生成的话单先缓存在本地。

#### [负载可靠性-CG过载保护](#ZH-CN_TOPIC_0295094695)

GGSN/SGW-C/PGW-C提供WAL（Windows Access Limit）过载保护算法，当检测出CG当前待处理负荷超出配置的WAL值时（通过 **ADD CG** 命令的“wal值”参数配置），则将该CG置为不可用，将后续的负荷转移到其他CG上处理。
