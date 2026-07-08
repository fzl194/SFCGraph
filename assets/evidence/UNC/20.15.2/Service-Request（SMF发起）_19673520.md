# Service Request（SMF发起）

- [业务场景](#ZH-CN_TOPIC_0000001419673520__1.3.1.1)
- [信令流程](#ZH-CN_TOPIC_0000001419673520__1.3.2.1)
- [性能指标说明](#ZH-CN_TOPIC_0000001419673520__1.3.3.1)

#### [业务场景](#ZH-CN_TOPIC_0000001419673520)

服务请求流程用于空闲状态UE与AMF之间建立信令连接，也可以用于空闲态或连接态UE激活已建立的PDU会话的用户面连接。

当网络侧发起服务请求的主要场景有：

- UE处于CM-IDLE态，网络侧发送信令或者有下行数据发送给UE时，AMF会请求(R)AN在注册区内发送PAGING消息寻呼UE，UE收到寻呼消息后会发起UE触发的服务请求流程。
- UE处于CM-CONNECTED态，该流程可以用于网络侧激活PDU会话的用户面连接，用于传输数据。

#### [信令流程](#ZH-CN_TOPIC_0000001419673520)

网络侧发起服务请求可由SMSF，PCF，LMF，GMLC，NEF，AMF，UDM，SMF和UPF（如果存在）发起，如下流程以SMF发起为例。若涉及到其他网元，下图中的SMF可以被对应的网元替换。

![](Service Request（SMF发起）_19673520.assets/zh-cn_image_0000001447794293_2.png)

1. 交互流程：UPF接收到PDU会话的下行数据。
2. 消息交互：UPF发送[PFCP Session Report Request](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Report Request_33031211.md)给SMF。
  触发条件：如果UPF没有此PDU会话的AN隧道信息，则UPF缓存下行数据并通知SMF。
  关键信元：

  | Report Type | 该信元指示报告的类型。 |
  | --- | --- |
  | Downlink Data Report | 指示报告类型为下行数据报告。 |
3. 消息交互：SMF发送[PFCP Session Report Response](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Report Response_32788413.md)给UPF。
  关键信元：

  | Cause | 指示接受或拒绝相应的请求消息。 |
  | --- | --- |
4. 消息交互：SMF发送[Namf_Communication_N1N2MessageTransfer Request](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Namf/N11/Namf_Communication_N1N2MessageTransfer/Namf_Communication_N1N2MessageTransfer Request_36361278.md)给AMF。
  触发条件：UE可达情况下，SMF给AMF发送Transfer消息。
  关键信元：

  | n2InfoContainer | 传递N2 information。 |
  | --- | --- |
  | pduSessionId | N2消息类型为SM时，消息的PDU Session ID。 |
5. 消息交互：AMF发送[Namf_Communication_N1N2MessageTransfer Response](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Namf/N11/Namf_Communication_N1N2MessageTransfer/Namf_Communication_N1N2MessageTransfer Response_84800549.md)给SMF。
  关键信元：

  | Cause | 表示AMF上N1/N2消息传输处理的结果。比如ATTEMPTING_TO_REACH_UE。表示AMF已发起寻呼以到达UE，以便传递N1消息。 |
  | --- | --- |
  相关机制：
  如果UE处于CM-IDLE状态，并且AMF能够寻呼UE，则AMF向SMF发送response消息，指示AMF正在寻呼UE。
  如果UE处于CM-CONNECTED状态，则AMF向SMF发送response消息，指示N1/N2消息已经发送出去。
  如果UE处于CM-IDLE状态，且AMF确定UE不可寻呼，则AMF应发送response表示UE不可达。
  如果UE不可达则SMF发送失败指示给UPF，UPF根据指示进行相应的处理。
6. 消息交互：AMF发送[PAGING](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N2接口/相关消息解释/PAGING_76785174.md)给(R)AN。
  触发条件：
  如果UE处于CM-IDLE态，则AMF发送PAGING消息给(R)AN，在UE注册的区域范围内寻呼UE。
  如果UE处于CM-CONNECTED态，则不需要进行寻呼，AMF为PDU会话激活用户面连接，可参考Service request流程（UE发起）PDU SESSION RESOURCE SETUP REQUEST消息及后续流程。
  关键信元：

  | Message Type | 标识正在发送的消息。 |
  | --- | --- |
  | TAI | 标识一个跟踪区域。 |
7. 消息交互：(R)AN发送[PAGING](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N2接口/相关消息解释/PAGING_76785174.md)给UE。
  相关机制：(R)AN转发相关消息给UE。
8. 子流程：[Service Request（UE发起）](Service Request（UE发起）_19514216.md#ZH-CN_TOPIC_0000001419514216)。
  触发条件：UE收到寻呼请求，发起Service request流程。

#### [性能指标说明](#ZH-CN_TOPIC_0000001419673520)

*表1 AMF性能指标*

| 测量网元 | 测量集 | 测量单元 | 测量对象 | 测量指标 | 测量点触发消息 | 流程图打点 |
| --- | --- | --- | --- | --- | --- | --- |
| AMF | AMF 移动性管理 | N2模式寻呼 | 整机 | 1929450077 N2模式寻呼请求次数 | PAGING | P6b |
| AMF | AMF会话管理 | 指定DNN的AMF会话测量 | DNN | 1929452141 指定DNN的SMF触发的N2模式寻呼请求次数 | PAGING | P6b |

*表2 SMF性能指标*

| 测量网元 | 测量集 | 测量单元 | 测量对象 | 测量指标 | 测量点触发消息 | 流程图打点 |
| --- | --- | --- | --- | --- | --- | --- |
| SMF | PFCP接口测量 | PFCP会话管理流程 | 整机 | 1929459784 接收PFCP会话报告请求消息数 | PFCP Session Report Request | P2a |
| SMF | PFCP接口测量 | PFCP会话管理流程 | 整机 | 1929459785 发送PFCP会话报告成功响应消息数 | PFCP Session Report Response | P3a |
| SMF | PFCP接口测量 | PFCP会话管理流程 | 整机 | 1929459786 接收PFCP会话报告请求消息数-包含DLDR指示 | PFCP Session Report Request | P2a |
| SMF | SMF 会话管理 | SMF N11接口消息测量 | 整机 | 1929467086 SMF发送N1N2 Message Transfer请求消息数 | Namf_Communication_N1N2MessageTransfer Request | P4b |
| SMF | SMF 会话管理 | SMF N11接口消息测量 | 整机 | 1929467088 SMF接收N1N2 Message Transfer响应成功消息数 | Namf_Communication_N1N2MessageTransfer Response | P5b |
| SMF | SMF 会话管理 | SMF N11接口消息测量 | 整机 | 1929467089 SMF接收N1N2 Message Transfer响应失败消息数 | Namf_Communication_N1N2MessageTransfer Response | P5b |
| SMF | SMF 会话管理 | SMF N11接口消息测量 | 整机 | 1929467090 SMF接收N1N2 Message Transfer响应失败消息数-切换过程中暂时拒绝 | Namf_Communication_N1N2MessageTransfer Response | P5b |
| SMF | SMF 会话管理 | SMF N11接口消息测量 | 整机 | 1929467091 SMF接收N1N2 Message Transfer响应失败消息数-超时 | Namf_Communication_N1N2MessageTransfer Response | P5b |
| SMF | SMF 会话管理 | SMF N11接口消息测量 | 整机 | 1929467092 SMF接收N1N2 Message Transfer响应失败消息数-上下文不存在 | Namf_Communication_N1N2MessageTransfer Response | P5b |
| SMF | SMF 会话管理 | SMF N11接口消息测量 | 整机 | 1929467097 SMF接收N1N2 Message Transfer响应失败消息数（外部响应504 Gateway Timeout） | Namf_Communication_N1N2MessageTransfer Response | P5b |

*表3 UPF性能指标*

| 测量网元 | 测量集 | 测量单元 | 测量对象 | 测量指标 | 测量点触发消息 | 流程图打点 |
| --- | --- | --- | --- | --- | --- | --- |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311121 用户平面N4接口指定DNN发送的PFCP会话报告消息数 | PFCP Session Report Request | P2b |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311122 用户平面N4接口指定DNN接收的PFCP会话报告确认消息数 | PFCP Session Report Response | P3b |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311152 用户平面N4接口指定DNN接收的PFCP会话报告成功确认消息数 | PFCP Session Report Response | P3b |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311153 用户平面N4接口指定DNN接收的PFCP会话报告失败确认消息数 | PFCP Session Report Response | P3b |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310921 用户平面N4接口发送的PFCP会话报告消息数 | PFCP Session Report Request | P2b |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310922 用户平面N4接口接收的PFCP会话报告确认消息数 | PFCP Session Report Response | P3b |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310961 用户平面N4接口接收的PFCP会话报告成功确认消息数 | PFCP Session Report Response | P3b |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310962 用户平面N4接口接收的PFCP会话报告失败确认消息数 | PFCP Session Report Response | P3b |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321410 用户平面指定POD发送的N4接口PFCP会话报告消息数 | PFCP Session Report Request | P2b |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321411 用户平面指定POD接收的N4接口PFCP会话报告确认消息数 | PFCP Session Report Response | P3b |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321412 用户平面指定POD接收的N4接口PFCP会话报告成功确认消息数 | PFCP Session Report Response | P3b |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321413 用户平面指定POD接收的N4接口PFCP会话报告失败确认消息数 | PFCP Session Report Response | P3b |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311021 用户平面N4接口指定切片（S-NSSAI）发送的PFCP会话报告消息数 | PFCP Session Report Request | P2b |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311022 用户平面N4接口指定切片（S-NSSAI）接收的PFCP会话报告确认消息数 | PFCP Session Report Response | P3b |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311051 用户平面N4接口指定切片（S-NSSAI）接收的PFCP会话报告成功确认消息数 | PFCP Session Report Response | P3b |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311052 用户平面N4接口指定切片（S-NSSAI）接收的PFCP会话报告失败确认消息数 | PFCP Session Report Response | P3b |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314108 用户平面N4接口发送的指定控制平面PFCP会话报告消息数 | PFCP Session Report Request | P2b |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314109 用户平面N4接口接收的指定控制平面PFCP会话报告确认消息数 | PFCP Session Report Response | P3b |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314111 用户平面N4接口接收的指定控制平面PFCP会话报告成功确认消息数 | PFCP Session Report Response | P3b |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314118 用户平面N4接口接收的指定控制平面PFCP会话报告失败确认消息数 | PFCP Session Report Response | P3b |
