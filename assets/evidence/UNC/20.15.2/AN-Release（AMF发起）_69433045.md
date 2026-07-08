# AN Release（AMF发起）

- [业务场景](#ZH-CN_TOPIC_0000001469433045__1.3.1.1)
- [信令流程](#ZH-CN_TOPIC_0000001469433045__1.3.2.1)
- [性能指标说明](#ZH-CN_TOPIC_0000001469433045__1.3.3.1)

#### [业务场景](#ZH-CN_TOPIC_0000001469433045)

AN Release流程用于释放逻辑NG-AP信令连接、N3用户面连接以及(R)AN RRC信令和资源。

例如当UE去注册时，AMF发起AN Release。

#### [信令流程](#ZH-CN_TOPIC_0000001469433045)

![](AN Release（AMF发起）_69433045.assets/zh-cn_image_0000001447794285_2.png)

1. 消息交互：AMF发送[UE CONTEXT RELEASE COMMAND](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N2接口/相关消息解释/UE CONTEXT RELEASE COMMAND_76785385.md)给(R)AN。
  触发条件：AMF比如当UE去注册时，发起AN Release。
  关键信元：
  | UE NGAP ID pair | UE NGAP ID对。 |
  | --- | --- |
  | Cause | 指示NGAP协议特定事件的原因。比如：deregister表示去注册。 |
2. 交互流程：(R)AN请求UE释放(R)AN连接。
  相关机制：如果(R)AN与UE之间的连接还没有完全释放，(R)AN请求UE释放(R)AN连接，并且在收到UE释放连接的确认后，(R)AN删除UE的上下文。
3. 消息交互：(R)AN发送[UE CONTEXT RELEASE COMPLETE](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N2接口/相关消息解释/UE CONTEXT RELEASE COMPLETE_76784409.md)给AMF。
  触发条件：UE相关的NG接口逻辑连接释放后(R)AN发送释放完成消息。
  关键信元：
  | AMF UE NGAP ID | 标识UE在NG接口上的关联。 |
  | --- | --- |
  | RAN UE NGAP ID | 标识RAN节点内NG接口的UE关联。 |
  | User Location Information | UE的位置信息。 |
  | **PDU Session Resource List** | PDU会话资源列表。 |
4. 消息交互：AMF发送[Nsmf_PDUSession_UpdateSmContext Request](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Nsmf/N11/Nsmf_PDUSession_UpdateSmContext/Nsmf_PDUSession_UpdateSmContext Request_35255324.md)给SMF。
  关键信元：
  | ngApCause | 该IE应指示请求修改的原因，例如请求去激活PDU会话的用户面连接的NGAP原因。 |
  | --- | --- |
  | upCnxState | 指示用户面连接状态。 |
5. 消息交互：SMF发送[PFCP Session Modification Request](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Modification Request_32686661.md)给UPF。
  关键信元：
  | **Update FAR** | 修改先前为PFCP会话创建的FAR。 |
  | --- | --- |
  相关机制：SMF指示UPF删除AN隧道信息或者UPF的隧道信息。如果释放原因为用户不活动或UE重定向，SMF应保留GBR QoS流。
6. 消息交互：UPF发送[PFCP Session Modification Response](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Modification Response_86008994.md)给SMF。
  关键信元：
  | Cause | 该信元应包含在响应消息中，原因值表示接受或拒绝相应的请求消息。 |
  | --- | --- |
7. 消息交互：SMF发送[Nsmf_PDUSession_UpdateSmContext Response](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Nsmf/N11/Nsmf_PDUSession_UpdateSmContext/Nsmf_PDUSession_UpdateSmContext Response_34935436.md)给AMF。
  关键信元：
  | upCnxState | 指示用户面连接状态。 |
  | --- | --- |

#### [性能指标说明](#ZH-CN_TOPIC_0000001469433045)

*表1 AMF性能指标*

| 测量网元 | 测量集 | 测量单元 | 测量对象 | 测量指标 | 测量点触发消息 | 流程图打点 |
| --- | --- | --- | --- | --- | --- | --- |
| AMF | AMF 移动性管理 | AN连接释放 | 整机 | 1929450679 AMF发送AN连接释放请求次数 | UE CONTEXT RELEASE COMMAND | P1b |
| AMF | AMF 移动性管理 | AN连接释放 | 整机 | 1929450680 AMF接收AN连接释放完成次数 | UE CONTEXT RELEASE COMPLETE | P3b |
| AMF | AMF会话管理 | 指定DNN的AMF会话测量 | DNN | 1929452133 指定DNN的AMF发起的会话上下文更新请求次数 | Nsmf_PDUSession_UpdateSmContext Request | P4a |
| AMF | AMF会话管理 | 指定DNN的AMF会话测量 | DNN | 1929452134 指定DNN的AMF发起的会话上下文更新成功次数 | Nsmf_PDUSession_UpdateSmContext Response | P7a |
| AMF | 服务化接口测量 | 指定局向的AMF N11接口测量 | NF局向 | 1929480479 指定N11接口的AMF发起的会话上下文更新请求次数 | Nsmf_PDUSession_UpdateSmContext Request | P4a |
| AMF | 服务化接口测量 | 指定局向的AMF N11接口测量 | NF局向 | 1929480480 指定N11接口的AMF发起的会话上下文更新成功次数 | Nsmf_PDUSession_UpdateSmContext Response | P7a |
| AMF | 服务化接口测量 | AMF指定SMF局向的N11接口测量 | AMF N11接口局向 | 1929451958 AMF N11接口向指定SMF局向发起的会话上下文更新请求次数 | Nsmf_PDUSession_UpdateSmContext Request | P4a |
| AMF | 服务化接口测量 | AMF指定SMF局向的N11接口测量 | AMF N11接口局向 | 1929451959 AMF N11接口向指定SMF局向发起的会话上下文更新成功次数 | Nsmf_PDUSession_UpdateSmContext Response | P7a |

*表2 SMF性能指标*

| 测量网元 | 测量集 | 测量单元 | 测量对象 | 测量指标 | 测量点触发消息 | 流程图打点 |
| --- | --- | --- | --- | --- | --- | --- |
| SMF | SMF 会话管理 | SMF N3用户面激活和释放流程 | 整机 | 1929458484 SMF N3用户面去激活请求次数 | Nsmf_PDUSession_UpdateSmContext Request | P4b |
| SMF | SMF 会话管理 | SMF N3用户面激活和释放流程 | 整机 | 1929458485 SMF N3用户面去激活成功次数 | Nsmf_PDUSession_UpdateSmContext Response | P7b |

*表3 UPF性能指标*

| 测量网元 | 测量集 | 测量单元 | 测量对象 | 测量指标 | 测量点触发消息 | 流程图打点 |
| --- | --- | --- | --- | --- | --- | --- |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311108 用户平面N4接口指定DNN接收的PFCP会话更新请求消息数 | PFCP Session Modification Request | P5b |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311109 用户平面N4接口指定DNN发送的PFCP会话更新响应成功消息数 | PFCP Session Modification Response | P6b |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311110 用户平面N4接口指定DNN发送的PFCP会话更新响应失败消息数 | PFCP Session Modification Response | P6b |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914314120 用户平面N4接口指定DNN接收的PFCP会话更新请求速率 | PFCP Session Modification Request | P5b |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310908 用户平面N4接口接收的PFCP会话更新请求消息数 | PFCP Session Modification Request | P5b |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310909 用户平面N4接口发送的PFCP会话更新响应成功消息数 | PFCP Session Modification Response | P6b |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310910 用户平面N4接口发送的PFCP会话更新响应失败消息数 | PFCP Session Modification Response | P6b |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310972 用户平面N4接口接收的PFCP会话更新请求速率 | PFCP Session Modification Request | P5b |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914318910 用户平面N4接口接收的PFCP会话更新请求消息数（DHCPV4消息） | PFCP Session Modification Request | P5b |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914318911 用户平面N4接口接收的PFCP会话更新请求消息数（DHCPV6消息） | PFCP Session Modification Request | P5b |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914318912 用户平面N4接口接收的PFCP会话更新请求消息数（RA消息） | PFCP Session Modification Request | P5b |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321403 用户平面指定POD接收的N4接口PFCP会话更新请求消息数 | PFCP Session Modification Request | P5b |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321404 用户平面指定POD发送的N4接口PFCP会话更新响应成功消息数 | PFCP Session Modification Response | P6b |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321405 用户平面指定POD发送的N4接口PFCP会话更新响应失败消息数 | PFCP Session Modification Response | P6b |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321416 用户平面指定POD接收的N4接口PFCP会话更新请求速率 | PFCP Session Modification Request | P5b |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311008 用户平面N4接口指定切片（S-NSSAI）接收的PFCP会话更新请求消息数 | PFCP Session Modification Request | P5b |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311055 用户平面N4接口指定切片（S-NSSAI）接收的PFCP会话更新请求速率 | PFCP Session Modification Request | P5b |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314103 用户平面N4接口接收的指定控制平面PFCP会话更新请求消息数 | PFCP Session Modification Request | P5b |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314104 用户平面N4接口发送的指定控制平面PFCP会话更新响应成功消息数 | PFCP Session Modification Response | P6b |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314105 用户平面N4接口发送的指定控制平面PFCP会话更新响应失败消息数 | PFCP Session Modification Response | P6b |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314115 用户平面N4接口接收的指定控制平面PFCP会话更新请求速率 | PFCP Session Modification Request | P5b |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314159 用户平面N4接口接收的指定控制平面PFCP会话更新请求消息数（DHCPV4消息） | PFCP Session Modification Request | P5b |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314160 用户平面N4接口接收的指定控制平面PFCP会话更新请求消息数（DHCPV6消息） | PFCP Session Modification Request | P5b |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314161 用户平面N4接口接收的指定控制平面PFCP会话更新请求消息数（RA消息） | PFCP Session Modification Request | P5b |
