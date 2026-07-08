# X2-based handover, intra-MME, with S-GW change

- [业务模型](#ZH-CN_CONCEPT_0000001130512070__1.4.1.1)
- [信令流程图](#ZH-CN_CONCEPT_0000001130512070__1.4.2.1)
- [流程说明](#ZH-CN_CONCEPT_0000001130512070__1.4.3.1)

#### [业务模型](#ZH-CN_CONCEPT_0000001130512070)

MME不变、S-GW改变的情况下，UE从源eNodeB切换到目标eNodeB的基于X2接口的切换流程。

#### [信令流程图](#ZH-CN_CONCEPT_0000001130512070)

S-GW改变的X2-based切换流程如 [图1](#ZH-CN_CONCEPT_0000001130512070__zh-cn_concept_0130779010_fig1) 所示。

**图1** S-GW改变的X2-based切换流程图

<br>

![](X2-based handover, intra-MME, with S-GW change_30512070.assets/zh-cn_image_0147311525.png)

#### [流程说明](#ZH-CN_CONCEPT_0000001130512070)

S-GW改变的X2-based切换（GTPC based S5/S8）详细流程如下：

1. 目标eNodeB向MME发送[Path Switch Request](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S1-MME/相关消息解释/Path Switch Request_30779139.md)消息通知其UE已经改变小区，消息包含目标小区的小区全局标识（TAI+ECGI）和所转换的EPS承载列表。MME决定S-GW重定位并根据目标TAI选择一个新的S-GW。
2. MME为每个PDN连接向目标S-GW发送[Create Session Request](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S11/相关消息解释/Create Session Request_30779578.md)消息，消息包含：bearer context(s) with PDN GW addresses和上行流PGW的TEID(for GTP-based S5/S8)、eNodeB address(es)和已经接受的EPS承载的下行用户面TEID、the Protocol Type over S5/S8、Serving Network、UE Time Zone。
  目标Serving GW将S-GW addresses和TEIDs for the uplink traffic分配给S1_U参考点（一个承载分配一个TEID的原则）。如果PDN GW请求UE位置信息，MME也会在此消息中包含User Location Information信元。
  MME使用 [1](#ZH-CN_CONCEPT_0000001130512070__zh-cn_concept_0130779010_li1) 中获取的EPS承载列表来确定目标eNodeB不能接受的专有承载，MME通过承载释放过程释放不被接受的专有承载。如果S-GW接收到了已经拒绝承载的下行数据分组，则S-GW丢弃该下行分组，不向MME发送下行链路数据通知（Downlink Data Notification）消息。
  如果目标eNodeB不能接受一个PDN连接的缺省承载，并且有多个PDN连接激活着，MME必须认为这个PDN连接的所有承载是要释放的，通过MME请求的PDN连接释放过程执行。如果目标eNodeB不能接受任何一个缺省承载，MME必须发起去附着过程和删除会话请求过程。
3. 目标S-GW为来自P-GW的下行业务分配S-GW地址和TEIDs (一个承载分配一个TEID的原则) 。S-GW为未能接受的承载分配S5/S8接口上的下行TEID。目标S-GW为每个PDN连接向P-GW发送[Modify Bearer Request](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S5_S8/相关消息解释/Modify Bearer Request_30779716.md)消息，消息包含：Serving GW addresses for user plane and TEID(s)、Serving Network。如果步骤[2](#ZH-CN_CONCEPT_0000001130512070__zh-cn_concept_0130779010_li2)中有User Location Information信元和/或UE Time Zone信元，则S-GW也在此信息中携带这两个信元。
4. P-GW更新其承载上下文并向S-GW返回[Modify Bearer Response](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S5_S8/相关消息解释/Modify Bearer Response_30779717.md)消息。PDN GW开始使用新接收到的地址和TEID向目标GW发送下行数据包。这些下行数据包将使用目标Serving GW到目标eNodeB的新的下行链路。Serving GW为失败的承载分配TEID，并告知MME。
5. 目标S-GW向MME发送[Create Session Response](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S11/相关消息解释/Create Session Response_30779579.md)消息。MME启动一个定时器，该定时器在[8](#ZH-CN_CONCEPT_0000001130512070__zh-cn_concept_0130779010_li8)中使用。
6. MME向目标eNodeB响应[Path Switch Request Acknowledge](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S1-MME/相关消息解释/Path Switch Request Acknowledge_30779140.md)消息，消息包含：Serving GW addresses and uplink TEID(s) for user plane。
  如果UE-AMBR发生了变化，例如，关联到同一个APN的所有EPS承载被目标eNodeB拒绝，MME将在发送给目标eNodeB的Path Switch Request Ack消息中提供更新后的UE-AMBR值。目标eNodeB开始使用新Serving GW地址和TEID转发随后的上行包。
  如果一些EPS承载在核心网中没有成功转换，MME必须在Path Switch Request Ack消息中指示未能建立的承载，并发起承载释放过程以释放未能建立的EPS承载对应的核心网资源。目标eNodeB必须删除所通知的核心网未能建立的承载上下文。
7. 目标eNodeB向源eNodeB发送Release Resource消息，通知切换成功，并触发资源释放。
8. 当[5](#ZH-CN_CONCEPT_0000001130512070__zh-cn_concept_0130779010_li5)中的定时器超时，MME向源S-GW发送[Delete Session Request](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S11/相关消息解释/Delete Session Request_30779585.md)消息释放源S-GW中的承载，消息包含：Cause。Cause指示S-GW不要向P-GW发起承载删除流程。
9. 源S-GW向MME响应[Delete Session Response](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S11/相关消息解释/Delete Session Response_30779586.md)消息。
10. 当[TAU from E-UTRAN to E-UTRAN, intra-MME, without S-GW change](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/业务流程/移动性管理/TAU_RAU/TAU from E-UTRAN to E-UTRAN, intra-MME, without S-GW change_30778968.md)中的任何一个条件满足时，UE发起TAU流程。
