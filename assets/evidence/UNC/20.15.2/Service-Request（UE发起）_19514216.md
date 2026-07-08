# Service Request（UE发起）

- [业务场景](#ZH-CN_TOPIC_0000001419514216__1.3.1.1)
- [信令流程](#ZH-CN_TOPIC_0000001419514216__1.3.2.1)
- [性能指标说明](#ZH-CN_TOPIC_0000001419514216__1.3.4.1)

#### [业务场景](#ZH-CN_TOPIC_0000001419514216)

服务请求流程用于空闲状态UE与AMF之间建立信令连接，也可以用于空闲态或连接态UE激活已建立的PDU会话的用户面连接。

当UE发起服务请求的主要目的有：

- UE处于CM-IDLE态，当有数据或者信令需要向网络侧发送，或收到PAGING消息时，触发此流程。
- UE处于CM-CONNECTED态，可通过该流程激活指定的某些PDU会话的用户面连接，用于进行数据传输。

#### [信令流程](#ZH-CN_TOPIC_0000001419514216)

![](Service Request（UE发起）_19514216.assets/zh-cn_image_0000001397354096_2.png)

1. 消息交互：UE发送[Service request](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N1接口/相关消息解释/Service request_76783789.md)给(R)AN。
  触发条件：服务请求流程用于空闲状态UE与AMF之间建立信令连接，也可以用于空闲态或连接态UE激活已建立的PDU会话的用户面连接。
  关键信元：
  | Service type | 指示服务请求类型，比如信令、数据等。 |
  | --- | --- |
  | Uplink data status | 向网络指示有上行数据待处理的保留的PDU会话。 |
  | PDU session status | 指示PDU会话标识的每个PDU会话的状态。 |
  | 5G-S-TMSI | 5G-S-TMSI信元包括AMF Set ID、AMF Pointer、5G-TMSI信息。 |
2. 消息交互：(R)AN发送[Service request](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N1接口/相关消息解释/Service request_76783789.md)给AMF。
  相关机制：(R)AN通过N2 Message消息（INITIAL UE MESSAGE）将Service request信息转发给AMF，N2 Message消息中携带N2 parameters。
3. 交互流程：NAS加密流程。
  相关机制：如果Service request消息已经进行加密及完整性保护，则不用执行此操作，如果没有加密则进行加密流程。
4. 消息交互：AMF发送[Nsmf_PDUSession_UpdateSmContext Request](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Nsmf/N11/Nsmf_PDUSession_UpdateSmContext/Nsmf_PDUSession_UpdateSmContext Request_35255324.md)给SMF。
  触发条件：如果服务请求用于激活PDU会话，则AMF给需要激活PDU会话对应的SMF发送消息请求恢复PDU会话连接，如果服务请求用于恢复信令连接，则无需执行会话相关步骤。
  关键信元：
  | ueLocation | UE的位置信息。 |
  | --- | --- |
  | upCnxState | 用于激活PDU会话的用户面连接。 |
  相关机制：AMF给需要激活的PDU会话对应的SMF发送消息，请求恢复PDU的会话连接。需要激活的PDU会话根据UE在Service request消息中Uplink data status信元指定。
5. 消息交互：SMF发送[Npcf_SMPolicyControl_Update](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Npcf/N7/Npcf_SMPolicyControl_Update_67572331.md)给PCF。
  触发条件：部署动态PCC策略，则SMF向PCF上报订阅事件，由PCF决策是否更新SM相关策略。如果没有部署动态PCC策略则由SMF本地策略决定SM相关策略。
  关键信元：
  | repPolicyCtrlReqTriggers | SMF向PCF上报发生的事件。 |
  | --- | --- |
6. 消息交互：PCF发送[Npcf_SMPolicyControl_Update](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Npcf/N7/Npcf_SMPolicyControl_Update_67572331.md)给SMF。
  触发条件：PCF根据SMF上报的会话数据和本地的用户签约数据重新进行策略判断，生成新的规则并下发。
  关键信元：
  | sessRules | 表示一组更新后的会话规则。 |
  | --- | --- |
  | pccRules | 表示一组更新后的PCC规则。 |
7. 消息交互：UPF选择流程。
  相关机制：SMF根据AMF提供的位置信息选择UPF。选择的UPF可能是当前的UPF，也可能是新UPF作为中间UPF或者是增加一个新中间UPF或者删除一个中间UPF。
8. 消息交互：SMF发送[PFCP Session Modification Request](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Modification Request_32686661.md)给PSA UPF。
  触发条件：SMF选择UPF后发送消息给PSA UPF创建隧道信息。
  关键信元：
  | Create PDR | 如果控制面功能请求用户面功能创建一个新的PDR，则该信元出现。 |
  | --- | --- |
  | Create FAR | 如果控制面功能请求用户面功能创建一个新的FAR，则该信元出现。 |
9. 消息交互：PSA UPF发送[PFCP Session Modification Response](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Modification Response_86008994.md)给SMF。
  关键信元：
  | Cause | 指示接受或拒绝相应的请求消息。 |
  | --- | --- |
  | Create PDR | 包含与PFCP会话相关的PDR信息。 |
  相关机制：如果没有I-UPF，则PSA UPF创建N3 CN隧道信息，如果SMF选择一个新的UPF作为I-UPF，或者SMF为没有I-UPF的PDU会话选择插入I-UPF时，PSA创建N9 CN隧道信息。
10. 消息交互：SMF发送[PFCP Session Establishment Request](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Establishment Request_32945585.md)给new I-UPF。
  触发条件：如果SMF选择一个新的UPF作为I-UPF，或者SMF为没有I-UPF的PDU会话选择插入I-UPF时，SMF发送消息给new I-UPF创建N9隧道信息。
  关键信元：
  | CP F-SEID | 指示控制面即SMF侧SEID，是控制面分配的标识会话的唯一标识，并用于后续信令交互。 |
  | --- | --- |
  | Create PDR | 表示Packet Detection Rule ，用于详细指示UPF针对每一条QoS Flow的流处理策略。PDR由流规则与流动作组成。 |
  | Source interface type | 接口类型。 |
  | Local F-TEID | 指示由SMF或UPF分配用户面的隧道端点标识，以及SMF分配的隧道端点标识。 |
  | Create FAR | 表示Forwarding Action Rule，用于定义流转发类动作，包括流量转发、丢弃、缓存等。FAR同PDR一样区分上下行。 |
  相关机制：SMF给new I-UPF发送此消息请求建立新的PFCP会话上下文，并将PSA UPF侧的N9 CN隧道信息传递给I-UPF。
11. 消息交互：new I-UPF发送[PFCP Session Establishment Response](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Establishment Response_85720872.md)给SMF。
  关键信元：
  | Cause | 该信元应指示接受或拒绝相应的请求消息。 |
  | --- | --- |
  | UP F-SEID | 指示用户面即UPF侧SEID，是用户面分配的标识会话的唯一标识，并用于后续信令交互。 |
  | Local F-TEID | 指示UPF分配的用户面隧道端点标识。 |
  相关机制：new I-UPF创建N3 CN隧道信息，以及N9 CN隧道信息。如果需要new I-UPF作为下行数据缓存点，则new I-UPF还会创建转发隧道信息。
12. 消息交互：SMF发送[PFCP Session Modification Request](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Modification Request_32686661.md)给PSA UPF。
  触发条件：UPF选择new I-UPF时，new I-UPF侧的N9 CN隧道信息创建后通过SMF传递到PSA UPF。
  关键信元：
  | Update PDR | 修改先前为PFCP会话创建的PDR。 |
  | --- | --- |
  | Update FAR | 修改先前为PFCP会话创建的FAR。 |
  相关机制：SMF将new I-UPF侧的N9 CN隧道信息传递到PSA UPF侧，打通PSA UPF到new I-UPF的下行数据。
13. 消息交互：PSA UPF发送[PFCP Session Modification Response](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Modification Response_86008994.md)给SMF。
  | Cause | 该信元应指示接受或拒绝相应的请求消息。 |
  | --- | --- |
14. 消息交互：SMF发送[PFCP Session Modification Request](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Modification Request_32686661.md)给old I-UPF。
  触发条件：new I-UPF创建转发隧道信息后，将隧道信息传递到old I-UPF，实现转发隧道的打通。
  关键信元：
  | Update PDR | 修改先前为PFCP会话创建的PDR。 |
  | --- | --- |
  | Update FAR | 修改先前为PFCP会话创建的FAR。 |
  相关机制：SMF将new I-UPF侧的转发隧道信息传递到old I-UPF侧。打通old I-UPF到new I-UPF的转发隧道，实现下行缓存数据传递到new I-UPF。如果UPF选择时要删除I-UPF，则SMF将PSA UPF的转发隧道信息传递到old I-UPF侧，下行缓存数据传递到PSA UPF。
15. 消息交互：old I-UPF发送[PFCP Session Modification Response](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Modification Response_86008994.md)给SMF。
  关键信元：

  | Cause | 该信元应指示接受或拒绝相应的请求消息。 |
  | --- | --- |
16. 消息交互：SMF发送[Nsmf_PDUSession_UpdateSmContext Response](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Nsmf/N11/Nsmf_PDUSession_UpdateSmContext/Nsmf_PDUSession_UpdateSmContext Response_34935436.md)给AMF。
  关键信元：
  | upCnxState | 指示用户面连接状态，比如“ACTIVATING”表示N3隧道建立中。 |
  | --- | --- |
  | n2SmInfo | 指示发送给(R)AN的N2 SM Information。传递的消息是PDU SESSION RESOURCE MODIFY REQUEST。 |
17. 消息交互：AMF发送[INITIAL CONTEXT SETUP REQUEST](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N2接口/相关消息解释/INITIAL CONTEXT SETUP REQUEST_76785539.md)（[PDU SESSION RESOURCE SETUP REQUEST](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N2接口/相关消息解释/PDU SESSION RESOURCE SETUP REQUEST_76784445.md)）给(R)AN。
  关键信元：
  | **PDU Session Resource Setup Request List** | PDU会话资源建立请求列表。 |
  | --- | --- |
  | PDU Session Resource Setup Request Transfer | SMF通过AMF透传给RAN的PDU Session Resource Setup Request Transfer IE。包含CN隧道信息等。 |
  | gTPTunnel | 指示GTP Tunnel信息，包含CN侧的隧道信息，即UPF侧IP地址和TEID。 |
18. 交互流程：(R)AN完成RRC的信令连接。
  相关机制：(R)AN根据已经激活的PDU会话的QoS信息，与UE执行RRC Connection Reconfiguration，完成RRC的信令连接。
19. 消息交互：(R)AN发送[INITIAL CONTEXT SETUP RESPONSE](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N2接口/相关消息解释/INITIAL CONTEXT SETUP RESPONSE_76783785.md)（[PDU SESSION RESOURCE SETUP RESPONSE](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N2接口/相关消息解释/PDU SESSION RESOURCE SETUP RESPONSE_76785226.md)）给AMF。
  关键信元：
  | **PDU Session Resource Setup Response List** | PDU会话资源建立响应列表。 |
  | --- | --- |
  | PDU Session Resource Setup Response Transfer | RAN通过AMF透传给SMF的PDU Session Resource Setup Response Transfer IE，包含AN隧道信息等。 |
  | gTPTunnel | 指示GTP Tunnel信息，包含AN侧的隧道信息，即(R)AN侧IP地址和TEID。 |
20. 消息交互：AMF发送[Nsmf_PDUSession_UpdateSmContext Request](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Nsmf/N11/Nsmf_PDUSession_UpdateSmContext/Nsmf_PDUSession_UpdateSmContext Request_35255324.md)给SMF。
  关键信元：
  | n2SmInfo | 从(R)AN接收到的N2 SM Information。包含AN隧道信息等。 |
  | --- | --- |
  | n2SmInfoType | N2 SM消息类型，比如PDU_RES_SETUP_RSP |
  相关机制：AMF向SMF发送消息将从(R)AN接收到的N2 SM Information转发给SMF。
21. 消息交互：SMF发送[Npcf_SMPolicyControl_Update](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Npcf/N7/Npcf_SMPolicyControl_Update_67572331.md)给PCF。
  触发条件：部署动态PCC策略，则SMF向PCF上报订阅事件，由PCF决策是否更新SM相关策略。如果没有部署动态PCC策略则由SMF本地策略决定SM相关策略。
  关键信元：
  | repPolicyCtrlReqTriggers | SMF向PCF上报发生的事件。 |
  | --- | --- |
22. 消息交互：PCF发送[Npcf_SMPolicyControl_Update](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Npcf/N7/Npcf_SMPolicyControl_Update_67572331.md)给SMF。
  触发条件：PCF根据SMF上报的会话数据和本地的用户签约数据重新进行策略判断，生成新的规则并下发。
  关键信元：
  | sessRules | 表示一组更新后的会话规则。 |
  | --- | --- |
  | pccRules | 表示一组更新后的PCC规则。 |
23. 消息交互：SMF发送[PFCP Session Modification Request](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Modification Request_32686661.md)给new I-UPF。
  触发条件：如果插入新的UPF，则SMF将AN隧道信息发送给new I-UPF。
  关键信元：
  | Update FAR | 更新下行FAR，将AN侧隧道信息发送给UPF。如果涉及多个QoS Flow则有多个FAR。 |
  | --- | --- |
  | **Update Forwarding Parameters** | 更新转发参数，将AN侧隧道信息发送给UPF。 |
  | Outer header creation | AN侧隧道信息，包括TEID和IP地址。 |
  相关机制：SMF向new I-UPF发送消息，将AN隧道信息和相应的转发规则发送给new I-UPF。new I-UPF获取到AN隧道后打通new I-UPF到UE的下行数据。
24. 消息交互：new I-UPF发送[PFCP Session Modification Response](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Modification Response_86008994.md)给SMF。
  关键信元：
  | Cause | 指示接受或拒绝相应的请求消息。 |
  | --- | --- |
25. 消息交互：SMF发送[PFCP Session Modification Request](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Modification Request_32686661.md)给PSA UPF。
  触发条件：如果没有I-UPF或者删除I-UPF，则SMF将AN隧道信息发送给PSA UPF。
  关键信元：
  | Update FAR | 更新下行FAR，将AN侧隧道信息发送给UPF。如果涉及多个QoS Flow则有多个FAR。 |
  | --- | --- |
  | **Update Forwarding Parameters** | 更新转发参数，将AN侧隧道信息发送给UPF。 |
  | Outer header creation | AN侧隧道信息，包括TEID和IP地址。 |
  相关机制：SMF向PSA UPF发送消息，将AN隧道信息和相应的转发规则发送给PSA UPF。PSA UPF获取到AN隧道后打通PSA UPF到UE的下行数据。
26. 消息交互：PSA UPF发送[PFCP Session Modification Response](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Modification Response_86008994.md)给SMF。
  关键信元：
  | Cause | 指示接受或拒绝相应的请求消息。 |
  | --- | --- |
27. 消息交互：SMF发送[Nsmf_PDUSession_UpdateSmContext Response](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/服务化接口协议/Nsmf/N11/Nsmf_PDUSession_UpdateSmContext/Nsmf_PDUSession_UpdateSmContext Response_34935436.md)给AMF。
  相关机制：如果请求成功，SMF响应状态码“204 No Content”，或者“200 OK”，如果失败或重定向，SMF返回“4xx/5xx”的HTTP状态码。
28. 消息交互：SMF发送[PFCP Session Modification Request](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Modification Request_32686661.md)给new I-UPF。
  触发条件：如果SMF选择new I-UPF，相应定时器超时后，SMF向new I-UPF发送会话修改请求，释放转发隧道资源。
29. 消息交互：new I-UPF发送[PFCP Session Modification Response](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Modification Response_86008994.md)给SMF。
  关键信元：
  | Cause | 指示接受或拒绝相应的请求消息。 |
  | --- | --- |
30. 消息交互：SMF发送[PFCP Session Modification Request](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Modification Request_32686661.md)给PSA UPF。
  触发条件：如果SMF选择PSA UPF，相应定时器超时后，SMF向PSA UPF发送会话修改请求，释放转发隧道资源。
31. 消息交互：PSA UPF发送[PFCP Session Modification Response](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Modification Response_86008994.md)给SMF。
  关键信元：
  | Cause | 指示接受或拒绝相应的请求消息。 |
  | --- | --- |
32. 消息交互：SMF发送[PFCP Session Deletion Request](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Deletion Request_86168956.md)给old I-UPF。
  触发条件：UPF选择时，如果SMF选择new I-UPF作为中间UPF，相应定时器超时后，SMF向old I-UPF发送会话释放请求，释放转发隧道资源。
  相关机制：如果SMF继续使用old I-UPF，则SMF发送会话修改请求，提供AN隧道信息给old I-UPF。
33. 消息交互：old I-UPF发送[PFCP Session Deletion Response](../../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N4接口/相关消息解释/PFCP Session Deletion Request_86168956.md)给SMF。
  关键信元：
  | Cause | 指示接受或拒绝相应的请求消息。 |
  | --- | --- |

#### [性能指标说明](#ZH-CN_TOPIC_0000001419514216)

*表1 AMF性能指标*

| 测量网元 | 测量集 | 测量单元 | 测量对象 | 测量指标 | 测量点触发消息 | 流程图打点 |
| --- | --- | --- | --- | --- | --- | --- |
| AMF | AMF 移动性管理 | N2模式业务请求 | 整机 | 1929450477 N2模式业务请求尝试次数 | SERVICE REQUEST | P2b |
| AMF | AMF 移动性管理 | N2模式业务请求 | 整机 | 1929450480 N2模式业务请求次数（上行信令） | SERVICE REQUEST | P2b |
| AMF | AMF 移动性管理 | N2模式业务请求 | 整机 | 1929450481 N2模式业务请求次数（上行数据） | SERVICE REQUEST | P2b |
| AMF | AMF 移动性管理 | N2模式业务请求 | 整机 | 1929450482 N2模式业务请求次数（移动终结业务） | SERVICE REQUEST | P2b |
| AMF | AMF 移动性管理 | N2模式业务请求 | 整机 | 1929450483 N2模式业务请求次数（紧急业务） | SERVICE REQUEST | P2b |
| AMF | AMF 移动性管理 | N2模式业务请求 | 整机 | 1929450484 N2模式业务请求次数（紧急业务回落） | SERVICE REQUEST | P2b |
| AMF | AMF 移动性管理 | N2模式业务请求 | 整机 | 1929450485 N2模式业务请求次数（高优先级业务） | SERVICE REQUEST | P2b |
| AMF | AMF会话管理 | 指定DNN的AMF会话测量 | DNN | 1929452126 指定DNN的AMF实时PDU会话数 | Nsmf_PDUSession_UpdateSmContext Response | P16a、P27a |
| AMF | AMF会话管理 | 指定DNN的AMF会话测量 | DNN | 1929452127 指定DNN的AMF平均PDU会话数 | Nsmf_PDUSession_UpdateSmContext Response | P16a、P27a |
| AMF | AMF会话管理 | 指定DNN的AMF会话测量 | DNN | 1929452128 指定DNN的AMF最大PDU会话数 | Nsmf_PDUSession_UpdateSmContext Response | P16a、P27a |
| AMF | AMF会话管理 | 指定DNN的AMF会话测量 | DNN | 1929452133 指定DNN的AMF发起的会话上下文更新请求次数 | Nsmf_PDUSession_UpdateSmContext Request | P4a、P20a |
| AMF | AMF会话管理 | 指定DNN的AMF会话测量 | DNN | 1929452134 指定DNN的AMF发起的会话上下文更新成功次数 | Nsmf_PDUSession_UpdateSmContext Response | P16a、P27a |
| AMF | AMF会话管理 | AMF会话资源 | 整机 | 1929451526 AMF实时PDU会话数 | Nsmf_PDUSession_UpdateSmContext Response | P16a、P27a |
| AMF | AMF会话管理 | AMF会话资源 | 整机 | 1929451527 AMF平均PDU会话数 | Nsmf_PDUSession_UpdateSmContext Response | P16a、P27a |
| AMF | AMF会话管理 | AMF会话资源 | 整机 | 1929451528 AMF最大PDU会话数 | Nsmf_PDUSession_UpdateSmContext Response | P16a、P27a |

*表2 SMF性能指标*

| 测量网元 | 测量集 | 测量单元 | 测量对象 | 测量指标 | 测量点触发消息 | 流程图打点 |
| --- | --- | --- | --- | --- | --- | --- |
| SMF | 服务化接口测量 | 指定局向的SMF N7接口测量 | NF局向 | 1929480679 指定局向的SMF更新SM策略请求次数 | Npcf_SMPolicyControl_Update Request | P5a |
| SMF | 服务化接口测量 | 指定局向的SMF N7接口测量 | NF局向 | 1929480680 指定局向的SMF更新SM策略成功次数 | Npcf_SMPolicyControl_Update Response | P6a |
| SMF | 服务化接口测量 | N7接口基本测量 | 整机 | 1929469378 SMF更新SM策略请求的次数 | Npcf_SMPolicyControl_Update Request | P5a |
| SMF | 服务化接口测量 | N7接口基本测量 | 整机 | 1929469379 SMF更新SM策略成功次数 | Npcf_SMPolicyControl_Update Response | P6a |
| SMF | 服务化接口测量 | N7接口返回码测量 | 整机 | 1929469698 SMF收到PCF更新SM策略失败的次数-状态码为400 | Npcf_SMPolicyControl_Update Response | P6a |
| SMF | 服务化接口测量 | N7接口返回码测量 | 整机 | 1929469699 SMF收到PCF更新SM策略失败的次数-状态码为401 | Npcf_SMPolicyControl_Update Response | P6a |
| SMF | 服务化接口测量 | N7接口返回码测量 | 整机 | 1929469700 SMF收到PCF更新SM策略失败的次数-状态码为403 | Npcf_SMPolicyControl_Update Response | P6a |
| SMF | 服务化接口测量 | N7接口返回码测量 | 整机 | 1929469701 SMF收到PCF更新SM策略失败的次数-状态码为404 | Npcf_SMPolicyControl_Update Response | P6a |
| SMF | 服务化接口测量 | N7接口返回码测量 | 整机 | 1929469702 SMF收到PCF更新SM策略失败的次数-状态码为500 | Npcf_SMPolicyControl_Update Response | P6a |
| SMF | 服务化接口测量 | N7接口返回码测量 | 整机 | 1929469703 SMF收到PCF更新SM策略失败的次数-状态码为503 | Npcf_SMPolicyControl_Update Response | P6a |
| SMF | 服务化接口测量 | N7接口返回码测量 | 整机 | 1929469704 SMF收到PCF更新SM策略失败的次数-响应超时 | Npcf_SMPolicyControl_Update Response | P6a |
| SMF | 服务化接口测量 | N7接口返回码测量 | 整机 | 1929469707 SMF收到PCF更新SM策略失败的次数-链路异常 | Npcf_SMPolicyControl_Update Response | P6a |
| SMF | 服务化接口测量 | N7接口返回码测量 | 整机 | 1929469708 SMF收到PCF更新SM策略失败的次数-状态码为其它 | Npcf_SMPolicyControl_Update Response | P6a |
| SMF | 服务化接口测量 | N7接口返回码测量 | 整机 | 1929469926 SMF收到PCF更新SM策略失败的次数-响应超时(内部响应) | Npcf_SMPolicyControl_Update Response | P6a |
| SMF | 服务化接口测量 | N7接口返回码测量 | 整机 | 1929469928 SMF收到PCF更新SM策略失败的次数-状态码为其它(内部响应) | Npcf_SMPolicyControl_Update Response | P6a |
| SMF | 服务化接口测量 | SMF指定PCF局向的N7接口测量 | SMF N7接口局向 | 1929469934 SMF N7接口向指定PCF局向发送更新SM策略请求次数 | Npcf_SMPolicyControl_Update Request | P5a |
| SMF | 服务化接口测量 | SMF指定PCF局向的N7接口测量 | SMF N7接口局向 | 1929469935 SMF N7接口从指定PCF局向接收更新SM策略成功次数 | Npcf_SMPolicyControl_Update Response | P6a |
| SMF | SMF 会话管理 | SMF 5G会话管理流程 | 整机 | 1929457413 N11(SMF)发送PDU Session Resource Setup Request Transfer消息数 | Nsmf_PDUSession_UpdateSmContext Response | P16b |
| SMF | SMF 会话管理 | SMF 5G会话管理流程 | 整机 | 1929457414 N11(SMF)接收PDU Session Resource Setup Response Transfer消息数 | Nsmf_PDUSession_UpdateSmContext Request | P20b |
| SMF | SMF 会话管理 | SMF 5G会话管理流程 | 整机 | 1929457444 N11(SMF)发送(IMS)PDU Session Resource Setup Request Transfer消息数 | Nsmf_PDUSession_UpdateSmContext Response | P16b |
| SMF | SMF 会话管理 | SMF 5G会话管理流程 | 整机 | 1929457445 N11(SMF)接收(IMS)PDU Session Resource Setup Response Transfer消息数 | Nsmf_PDUSession_UpdateSmContext Request | P20b |
| SMF | SMF 会话管理 | 指定S-NSSAI的SMF 5G会话管理流程 | S-NSSAI | 1929457508 指定S-NSSAI的N11(SMF)发送PDU Session Resource Setup Request Transfer消息数 | Nsmf_PDUSession_UpdateSMContext Response | P16b |
| SMF | SMF 会话管理 | 指定S-NSSAI的SMF 5G会话管理流程 | S-NSSAI | 1929457509 指定S-NSSAI的N11(SMF)接收PDU Session Resource Setup Response Transfer消息数 | Nsmf_PDUSession_UpdateSmContext Request | P20b |
| SMF | SMF 会话管理 | 指定S-NSSAI的SMF 5G会话管理流程 | S-NSSAI | 1929457541 指定S-NSSAI的N11(SMF)发送(IMS)PDU Session Resource Setup Request Transfer消息数 | Nsmf_PDUSession_UpdateSmContext Response | P16b |
| SMF | SMF 会话管理 | 指定S-NSSAI的SMF 5G会话管理流程 | S-NSSAI | 1929457542 指定S-NSSAI的N11(SMF)接收(IMS)PDU Session Resource Setup Response Transfer消息数 | Nsmf_PDUSession_UpdateSmContext Request | P20b |
| SMF | SMF 会话管理 | 指定DNN的SMF 5G会话管理流程 | DNN | 1929457608 指定DNN的N11(SMF)发送PDU Session Resource Setup Request Transfer消息数 | Nsmf_PDUSession_UpdateSmContext Response | P16b |
| SMF | SMF 会话管理 | 指定DNN的SMF 5G会话管理流程 | DNN | 1929457609 指定DNN的N11(SMF)接收PDU Session Resource Setup Response Transfer消息数 | Nsmf_PDUSession_UpdateSmContext Request | P20b |
| SMF | SMF 会话管理 | 指定DNN的SMF 5G会话管理流程 | DNN | 1929457641 指定DNN的N11(SMF)发送(IMS)PDU Session Resource Setup Request Transfer消息数 | Nsmf_PDUSession_UpdateSmContext Response | P16b |
| SMF | SMF 会话管理 | 指定DNN的SMF 5G会话管理流程 | DNN | 1929457642 指定DNN的N11(SMF)接收(IMS)PDU Session Resource Setup Response Transfer消息数 | Nsmf_PDUSession_UpdateSmContext Request | P20b |
| SMF | SMF 会话管理 | SMF 5G会话管理失败流程 | 整机 | 1929458823 N11(SMF)接收PDU Session Resource Setup Unsuccessful Transfer失败消息数 | Nsmf_PDUSession_UpdateSmContext Request | P20b |
| SMF | SMF 会话管理 | SMF 5G会话管理失败流程 | 整机 | 1929458824 N11(SMF)接收PDU Session Resource Setup Unsuccessful Transfer失败消息数-#28 Multiple PDU Session ID instances | Nsmf_PDUSession_UpdateSmContext Request | P20b |
| SMF | SMF 会话管理 | SMF 5G会话管理失败流程 | 整机 | 1929458825 N11(SMF)接收PDU Session Resource Setup Unsuccessful Transfer失败消息数-#39 Slice(s) not supported | Nsmf_PDUSession_UpdateSmContext Request | P20b |
| SMF | SMF 会话管理 | SMF 5G会话管理失败流程 | 整机 | 1929458826 N11(SMF)接收PDU Session Resource Setup Unsuccessful Transfer失败消息数-#42 Resources not available for the slice(s) | Nsmf_PDUSession_UpdateSmContext Request | P20b |
| SMF | SMF 会话管理 | 指定S-NSSAI的SMF 5G会话管理失败流程 | S-NSSAI | 1929459017 指定S-NSSAI的N11(SMF)接收PDU Session Resource Setup Unsuccessful Transfer失败消息数 | Nsmf_PDUSession_UpdateSmContext Request | P20b |
| SMF | SMF 会话管理 | 指定S-NSSAI的SMF 5G会话管理失败流程 | S-NSSAI | 1929459018 指定S-NSSAI的N11(SMF)接收PDU Session Resource Setup Unsuccessful Transfer失败消息数-#28 Multiple PDU Session ID instances | Nsmf_PDUSession_UpdateSmContext Request | P20b |
| SMF | SMF 会话管理 | 指定S-NSSAI的SMF 5G会话管理失败流程 | S-NSSAI | 1929459019 指定S-NSSAI的N11(SMF)接收PDU Session Resource Setup Unsuccessful Transfer失败消息数-#39 Slice(s) not supported | Nsmf_PDUSession_UpdateSmContext Request | P20b |
| SMF | SMF 会话管理 | 指定S-NSSAI的SMF 5G会话管理失败流程 | S-NSSAI | 1929459020 指定S-NSSAI的N11(SMF)接收PDU Session Resource Setup Unsuccessful Transfer失败消息数-#42 Resources not available for the slice(s) | Nsmf_PDUSession_UpdateSmContext Request | P20b |
| SMF | SMF 会话管理 | 指定DNN的SMF 5G会话管理失败流程 | DNN | 1929459217 指定DNN的N11(SMF)接收PDU Session Resource Setup Unsuccessful Transferr失败消息数 | Nsmf_PDUSession_UpdateSmContext Request | P20b |
| SMF | SMF 会话管理 | 指定DNN的SMF 5G会话管理失败流程 | DNN | 1929459218 指定DNN的N11(SMF)接收PDU Session Resource Setup Unsuccessful Transfer失败消息数-#28 Multiple PDU Session ID instances | Nsmf_PDUSession_UpdateSMContext Request | P20b |
| SMF | SMF 会话管理 | 指定DNN的SMF 5G会话管理失败流程 | DNN | 1929459219 指定DNN的N11(SMF)接收PDU Session Resource Setup Unsuccessful Transfer失败消息数-#39 Slice(s) not supported | Nsmf_PDUSession_UpdateSmContext Request | P20b |
| SMF | SMF 会话管理 | 指定DNN的SMF 5G会话管理失败流程 | DNN | 1929459220 指定DNN的N11(SMF)接收PDU Session Resource Setup Unsuccessful Transfer失败消息数-#42 Resources not available for the slice(s) | Nsmf_PDUSession_UpdateSmContext Request | P20b |
| SMF | PFCP接口测量 | PFCP会话管理流程 | 整机 | 1929459778 发送PFCP会话创建请求消息数 | PFCP Session Establishment Request | P10b、P14a |
| SMF | PFCP接口测量 | PFCP会话管理流程 | 整机 | 1929459779 接收PFCP会话创建成功响应消息数 | PFCP Session Establishment Response | P11b、P15a |
| SMF | PFCP接口测量 | PFCP会话管理流程 | 整机 | 1929459782 发送PFCP会话删除请求消息数 | PFCP Session Deletion Request | P32a |
| SMF | PFCP接口测量 | PFCP会话管理流程 | 整机 | 1929459783 接收PFCP会话删除成功响应消息数 | PFCP Session Deletion Response | P33a |
| SMF | PFCP接口测量 | PFCP会话管理流程 | 整机 | 1929459780 发送PFCP会话更新请求消息数 | PFCP Session Modification Request | P8a、P12a、P23b、P25a、P28b、P30a |
| SMF | PFCP接口测量 | PFCP会话管理流程 | 整机 | 1929459781 接收PFCP会话更新成功响应消息数 | PFCP Session Modification Response | P9a、P13a、P24b、P26a、P29b、P31a |

*表3 PCF性能指标*

| 测量网元 | 测量集 | 测量单元 | 测量对象 | 测量指标 | 测量点触发消息 | 流程图打点 |
| --- | --- | --- | --- | --- | --- | --- |
| PCF | PCF性能测量 | PCF与SMF对端实体基于结果码的性能测量 | PCFHLB | 1727317687 会话管理策略更新响应参数错误次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体基于结果码的性能测量 | PCFHLB | 1727317688 会话管理策略更新响应触发器错误次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体基于结果码的性能测量 | PCFHLB | 1727317689 会话管理策略更新响应流量映射过滤器被拒绝次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体基于结果码的性能测量 | PCFHLB | 1727317690 会话管理策略更新响应请求冲突次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体基于结果码的性能测量 | PCFHLB | 1931103983 会话管理策略更新请求次数 | Npcf_SMPolicyControl_Update Request | P5b、P21b |
| PCF | PCF性能测量 | PCF与SMF对端实体基于结果码的性能测量 | PCFHLB | 1931103984 会话管理策略更新响应200成功次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体基于结果码的性能测量 | PCFHLB | 1931103985 会话管理策略更新响应400错误请求次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体基于结果码的性能测量 | PCFHLB | 1931103986 会话管理策略更新响应401未经授权次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体基于结果码的性能测量 | PCFHLB | 1931103987 会话管理策略更新响应403禁止次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体基于结果码的性能测量 | PCFHLB | 1931104253 会话管理策略更新响应404未找到次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体基于结果码的性能测量 | PCFHLB | 1931103988 会话管理策略更新响应411需要长度次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体基于结果码的性能测量 | PCFHLB | 1931103989 会话管理策略更新响应413有效载荷过大次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体基于结果码的性能测量 | PCFHLB | 1931103990 会话管理策略更新响应415不支持的媒体类型次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体基于结果码的性能测量 | PCFHLB | 1931103991 会话管理策略更新响应500内部服务器错误次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体基于结果码的性能测量 | PCFHLB | 1931103992 会话管理策略更新响应503服务不可用次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体的性能测量 | PCFHLB | 1727317516 N7会话授权修改次数 | Npcf_SMPolicyControl_Update Request | P5b、P21b |
| PCF | PCF性能测量 | PCF与SMF对端实体的性能测量 | PCFHLB | 1727317517 N7会话授权修改成功次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体的性能测量 | PCFHLB | 1727317518 N7会话授权修改失败次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体的性能测量 | PCFHLB | 1931104250 RE_TIMEOUT通知尝试次数 | Npcf_SMPolicyControl_Update Request | P5b、P21b |
| PCF | PCF性能测量 | PCF与SMF对端实体的性能测量 | PCFHLB | 1931104251 RE_TIMEOUT通知成功次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体的性能测量 | PCFHLB | 1931104252 RE_TIMEOUT通知失败次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体的性能测量 | PCFHLB | 1931104469 N7数据会话授权修改次数 | Npcf_SMPolicyControl_Update Request | P5b、P21b |
| PCF | PCF性能测量 | PCF与SMF对端实体的性能测量 | PCFHLB | 1931104470 N7数据会话授权修改成功次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体的性能测量 | PCFHLB | 1931104471 N7数据会话授权修改失败次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体的性能测量 | PCFHLB | 1931104492 数据RE_TIMEOUT通知尝试次数 | Npcf_SMPolicyControl_Update Request | P5b、P21b |
| PCF | PCF性能测量 | PCF与SMF对端实体的性能测量 | PCFHLB | 1931104493 数据RE_TIMEOUT通知成功次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体的性能测量 | PCFHLB | 1931104494 数据RE_TIMEOUT通知失败次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体的性能测量 | PCFHLB | 1931104496 N7语音会话授权修改次数 | Npcf_SMPolicyControl_Update Request | P5b、P21b |
| PCF | PCF性能测量 | PCF与SMF对端实体的性能测量 | PCFHLB | 1931104497 N7语音会话授权修改成功次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体的性能测量 | PCFHLB | 1931104498 N7语音会话授权修改失败次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体的性能测量 | PCFHLB | 1931104519 语音RE_TIMEOUT通知尝试次数 | Npcf_SMPolicyControl_Update Request | P5b、P21b |
| PCF | PCF性能测量 | PCF与SMF对端实体的性能测量 | PCFHLB | 1931104520 语音RE_TIMEOUT通知成功次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |
| PCF | PCF性能测量 | PCF与SMF对端实体的性能测量 | PCFHLB | 1931104521 语音RE_TIMEOUT通知失败次数 | Npcf_SMPolicyControl_Update Response | P6b、P22b |

*表4 PSA UPF性能指标*

| 测量网元 | 测量集 | 测量单元 | 测量对象 | 测量指标 | 测量点触发消息 | 流程图打点 |
| --- | --- | --- | --- | --- | --- | --- |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311108 用户平面N4接口指定DNN接收的PFCP会话更新请求消息数 | PFCP Session Modification Request | P8b、P12b、P25b、P30b |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311109 用户平面N4接口指定DNN发送的PFCP会话更新响应成功消息数 | PFCP Session Modification Response | P9b、P13b、P26b、P31b |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311110 用户平面N4接口指定DNN发送的PFCP会话更新响应失败消息数 | PFCP Session Modification Response | P9b、P13b、P26b、P31b |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310908 用户平面N4接口接收的PFCP会话更新请求消息数 | PFCP Session Modification Request | P8b、P12b、P25b、P30b |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310909 用户平面N4接口发送的PFCP会话更新响应成功消息数 | PFCP Session Modification Response | P9b、P13b、P26b、P31b |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310910 用户平面N4接口发送的PFCP会话更新响应失败消息数 | PFCP Session Modification Response | P9b、P13b、P26b、P31b |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321403 用户平面指定POD接收的N4接口PFCP会话更新请求消息数 | PFCP Session Modification Request | P8b、P12b、P25b、P30b |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321404 用户平面指定POD发送的N4接口PFCP会话更新响应成功消息数 | PFCP Session Modification Response | P9b、P13b、P26b、P31b |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321405 用户平面指定POD发送的N4接口PFCP会话更新响应失败消息数 | PFCP Session Modification Response | P9b、P13b、P26b、P31b |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311008 用户平面N4接口指定切片（S-NSSAI）接收的PFCP会话更新请求消息数 | PFCP Session Modification Request | P8b、P12b、P25b、P30b |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311009 用户平面N4接口指定切片（S-NSSAI）发送的PFCP会话更新响应成功消息数 | PFCP Session Modification Response | P9b、P13b、P26b、P31b |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311010 用户平面N4接口指定切片（S-NSSAI）发送的PFCP会话更新响应失败消息数 | PFCP Session Modification Response | P9b、P13b、P26b、P31b |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314103 用户平面N4接口接收的指定控制平面PFCP会话更新请求消息数 | PFCP Session Modification Request | P8b、P12b、P25b、P30b |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314104 用户平面N4接口发送的指定控制平面PFCP会话更新响应成功消息数 | PFCP Session Modification Response | P9b、P13b、P26b、P31b |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314105 用户平面N4接口发送的指定控制平面PFCP会话更新响应失败消息数 | PFCP Session Modification Response | P9b、P13b、P26b、P31b |

*表5 new I-UPF性能指标*

| 测量网元 | 测量集 | 测量单元 | 测量对象 | 测量指标 | 测量点触发消息 | 流程图打点 |
| --- | --- | --- | --- | --- | --- | --- |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311100 用户平面N4接口指定DNN接收的PFCP会话建立请求消息数 | PFCP Session Establishment Request | P10a |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311101 用户平面N4接口指定DNN发送的PFCP会话建立响应成功消息数 | PFCP Session Establishment Response | P11a |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311102 用户平面N4接口指定DNN发送的PFCP会话建立响应失败消息数 | PFCP Session Establishment Response | P11a |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311108 用户平面N4接口指定DNN接收的PFCP会话更新请求消息数 | PFCP Session Modification Request | P23a、P28a |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311109 用户平面N4接口指定DNN发送的PFCP会话更新响应成功消息数 | PFCP Session Modification Response | P24a、P29a |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311110 用户平面N4接口指定DNN发送的PFCP会话更新响应失败消息数 | PFCP Session Modification Response | P24a、P29a |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310900 用户平面N4接口接收的PFCP会话建立请求消息数 | PFCP Session Establishment Request | P10a |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310901 用户平面N4接口发送的PFCP会话建立响应成功消息数 | PFCP Session Establishment Response | P11a |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310902 用户平面N4接口发送的PFCP会话建立响应失败消息数 | PFCP Session Establishment Response | P11a |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310908 用户平面N4接口接收的PFCP会话更新请求消息数 | PFCP Session Modification Request | P23a、P28a |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310909 用户平面N4接口发送的PFCP会话更新响应成功消息数 | PFCP Session Modification Response | P24a、P29a |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310910 用户平面N4接口发送的PFCP会话更新响应失败消息数 | PFCP Session Modification Response | P24a、P29a |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321400 用户平面指定POD接收的N4接口PFCP会话建立请求消息数 | PFCP Session Establishment Request | P10a |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321401 用户平面指定POD发送的N4接口PFCP会话建立响应成功消息数 | PFCP Session Establishment Response | P11a |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321402 用户平面指定POD发送的N4接口PFCP会话建立响应失败消息数 | PFCP Session Establishment Response | P11a |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321403 用户平面指定POD接收的N4接口PFCP会话更新请求消息数 | PFCP Session Modification Request | P23a、P28a |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321404 用户平面指定POD发送的N4接口PFCP会话更新响应成功消息数 | PFCP Session Modification Response | P24a、P29a |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321405 用户平面指定POD发送的N4接口PFCP会话更新响应失败消息数 | PFCP Session Modification Response | P24a、P29a |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311000 用户平面N4接口指定切片（S-NSSAI）接收的PFCP会话建立请求消息数 | PFCP Session Establishment Request | P10a |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311001 用户平面N4接口指定切片（S-NSSAI）发送的PFCP会话建立响应成功消息数 | PFCP Session Establishment Response | P11a |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311002 用户平面N4接口指定切片（S-NSSAI）发送的PFCP会话建立响应失败消息数 | PFCP Session Establishment Response | P11a |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311008 用户平面N4接口指定切片（S-NSSAI）接收的PFCP会话更新请求消息数 | PFCP Session Modification Request | P23a、P28a |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311009 用户平面N4接口指定切片（S-NSSAI）发送的PFCP会话更新响应成功消息数 | PFCP Session Modification Response | P24a、P29a |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311010 用户平面N4接口指定切片（S-NSSAI）发送的PFCP会话更新响应失败消息数 | PFCP Session Modification Response | P24a、P29a |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314100 用户平面N4接口接收的指定控制平面PFCP会话建立请求消息数 | PFCP Session Establishment Request | P10a |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314101 用户平面N4接口发送的指定控制平面PFCP会话建立响应成功消息数 | PFCP Session Establishment Response | P11a |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314102 用户平面N4接口发送的指定控制平面PFCP会话建立响应失败消息数 | PFCP Session Establishment Response | P11a |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314103 用户平面N4接口接收的指定控制平面PFCP会话更新请求消息数 | PFCP Session Modification Request | P23a、P28a |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314104 用户平面N4接口发送的指定控制平面PFCP会话更新响应成功消息数 | PFCP Session Modification Response | P24a、P29a |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314105 用户平面N4接口发送的指定控制平面PFCP会话更新响应失败消息数 | PFCP Session Modification Response | P24a、P29a |

*表6 old I-UPF性能指标*

| 测量网元 | 测量集 | 测量单元 | 测量对象 | 测量指标 | 测量点触发消息 | 流程图打点 |
| --- | --- | --- | --- | --- | --- | --- |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311100 用户平面N4接口指定DNN接收的PFCP会话建立请求消息数 | PFCP Session Establishment Request | P14b |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311101 用户平面N4接口指定DNN发送的PFCP会话建立响应成功消息数 | PFCP Session Establishment Response | P15b |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311102 用户平面N4接口指定DNN发送的PFCP会话建立响应失败消息数 | PFCP Session Establishment Response | P15b |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311119 用户平面N4接口指定DNN接收的PFCP会话释放请求消息数 | PFCP Session Deletion Request | P32b |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311120 用户平面N4接口指定DNN发送的PFCP会话释放响应消息数 | PFCP Session Deletion Response | P33b |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311150 用户平面N4接口指定DNN发送的PFCP会话释放响应成功消息数 | PFCP Session Deletion Response | P33b |
| UPF | N4信令测量 | 用户平面基于DNN的N4信令测量 | APN | 1914311151 用户平面N4接口指定DNN发送的PFCP会话释放响应失败消息数 | PFCP Session Deletion Response | P33b |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310900 用户平面N4接口接收的PFCP会话建立请求消息数 | PFCP Session Establishment Request | P14b |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310901 用户平面N4接口发送的PFCP会话建立响应成功消息数 | PFCP Session Establishment Response | P15b |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310902 用户平面N4接口发送的PFCP会话建立响应失败消息数 | PFCP Session Establishment Response | P15b |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310919 用户平面N4接口接收的PFCP会话释放请求消息数 | PFCP Session Deletion Request | P32b |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310920 用户平面N4接口发送的PFCP会话释放响应消息数 | PFCP Session Deletion Response | P33b |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310959 用户平面N4接口发送的PFCP会话释放响应成功消息数 | PFCP Session Deletion Response | P33b |
| UPF | N4信令测量 | 用户平面N4信令测量 | 整机 | 1914310960 用户平面N4接口发送的PFCP会话释放响应失败消息数 | PFCP Session Deletion Response | P33b |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321400 用户平面指定POD接收的N4接口PFCP会话建立请求消息数 | PFCP Session Establishment Request | P14b |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321401 用户平面指定POD发送的N4接口PFCP会话建立响应成功消息数 | PFCP Session Establishment Response | P15b |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321402 用户平面指定POD发送的N4接口PFCP会话建立响应失败消息数 | PFCP Session Establishment Response | P15b |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321406 用户平面指定POD接收的N4接口PFCP会话释放请求消息数 | PFCP Session Deletion Request | P32b |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321407 用户平面指定POD发送的N4接口PFCP会话释放响应消息数 | PFCP Session Deletion Response | P33b |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321408 用户平面指定POD发送的N4接口PFCP会话释放响应成功消息数 | PFCP Session Deletion Response | P33b |
| UPF | N4信令测量 | 用户平面基于POD的N4信令测量 | 业务POD | 1914321409 用户平面指定POD发送的N4接口PFCP会话释放响应失败消息数 | PFCP Session Deletion Response | P33b |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311000 用户平面N4接口指定切片（S-NSSAI）接收的PFCP会话建立请求消息数 | PFCP Session Establishment Request | P14b |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311001 用户平面N4接口指定切片（S-NSSAI）发送的PFCP会话建立响应成功消息数 | PFCP Session Establishment Response | P15b |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311002 用户平面N4接口指定切片（S-NSSAI）发送的PFCP会话建立响应失败消息数 | PFCP Session Establishment Response | P15b |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311012 用户平面N4接口指定切片（S-NSSAI）发送的PFCP会话释放响应成功消息数 | PFCP Session Deletion Response | P33b |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311019 用户平面N4接口指定切片（S-NSSAI）接收的PFCP会话释放请求消息数 | PFCP Session Deletion Request | P32b |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311020 用户平面N4接口指定切片（S-NSSAI）发送的PFCP会话释放响应消息数 | PFCP Session Deletion Response | P33b |
| UPF | N4信令测量 | 用户平面基于切片(S-NSSAI)的N4信令测量 | SNSSAI | 1914311050 用户平面N4接口指定切片（S-NSSAI）发送的PFCP会话释放响应失败消息数 | PFCP Session Deletion Response | P33b |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314100 用户平面N4接口接收的指定控制平面PFCP会话建立请求消息数 | PFCP Session Establishment Request | P14b |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314101 用户平面N4接口发送的指定控制平面PFCP会话建立响应成功消息数 | PFCP Session Establishment Response | P15b |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314102 用户平面N4接口发送的指定控制平面PFCP会话建立响应失败消息数 | PFCP Session Establishment Response | P15b |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314106 用户平面N4接口接收的指定控制平面PFCP会话释放请求消息数 | PFCP Session Deletion Request | P32b |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314107 用户平面N4接口发送的指定控制平面PFCP会话释放响应消息数 | PFCP Session Deletion Response | P33b |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314112 用户平面N4接口发送的指定控制平面PFCP会话释放响应成功消息数 | PFCP Session Deletion Response | P33b |
| UPF | N4信令测量 | 用户平面基于CP的N4信令测量 | CP | 1914314113 用户平面N4接口发送的指定控制平面PFCP会话释放响应失败消息数 | PFCP Session Deletion Response | P33b |
