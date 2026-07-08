# S1-based handover, intra-MME, with S-GW change

- [业务模型](#ZH-CN_CONCEPT_0000001176391825__1.4.1.1)
- [信令流程图](#ZH-CN_CONCEPT_0000001176391825__1.4.2.1)
- [流程说明](#ZH-CN_CONCEPT_0000001176391825__1.4.3.1)

#### [业务模型](#ZH-CN_CONCEPT_0000001176391825)

MME不变、S-GW改变的情况下，UE从源eNodeB切换到目标eNodeB的基于S1接口的切换流程。

#### [信令流程图](#ZH-CN_CONCEPT_0000001176391825)

MME不变、S-GW改变的S1-based切换流程如 [图1](#ZH-CN_CONCEPT_0000001176391825__zh-cn_concept_0130779014_fig1) 所示。

**图1** MME不变、S-GW改变的S1-based切换流程图

<br>

![](S1-based handover, intra-MME, with S-GW change_76391825.assets/zh-cn_image_0147311597.png)

#### [流程说明](#ZH-CN_CONCEPT_0000001176391825)

MME不变、S-GW改变的S1-based切换（GTPC based S5/S8）详细流程如下：

1. 源eNodeB向目标eNodeB发起S1-based handover，原因可能如下：
  到目标eNodeB没有X2连接。
  目标侧eNodeB告知源eNodeB之前的X2-based handover失败。
  源eNodeB收到动态信息。
2. 源eNodeB向MME发送[Handover Required](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S1-MME/相关消息解释/Handover Required_30779127.md)消息请求切换，消息包含：Direct Forwarding Path Availability、Source to Target transparent container、target eNodeB Identity、CSG ID、CSG access mode、S1AP Cause。Source to Target transparent container指示了执行数据转发的承载列表，Direct Forwarding Path Availability指示了从源eNodeB到目标eNodeB是否可以进行直接转发。
3. MME确认源S-GW是否可以继续为UE服务。如果不能，就选择一个新的S-GW。
  MME为每个PDN连接向目标S-GW发送 [Create Session Request](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S11/相关消息解释/Create Session Request_30779578.md) 消息，消息包含：bearer context(s) with PDN GW addresses and TEIDs (for GTP-based S5/S8) at the PDN GW(s) for uplink traffic、Serving Network。
  目标Serving GW将S-GW addresses和TEIDs for the uplink traffic分配给S1_U参考点（一个承载分配一个TEID的原则）。
4. 目标S-GW向MME返回[Create Session Response](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S11/相关消息解释/Create Session Response_30779579.md)消息。
5. MME向目标eNodeB发送[Handover Request](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S1-MME/相关消息解释/Handover Request_30779125.md)消息在目标eNodeB上创建UE上下文，包含承载信息和安全上下文，消息包含：EPS Bearers to Setup、AMBR、S1AP Cause、Source to Target transparent container、CSG ID、CSG Membership Indication、Handover Restriction List。
  对于每一个EPS承载，Bearers to Setup包含Serving GW address and uplink TEID for user plane and EPS Bearer QoS。如果直接转发标志位（direct forwarding flag）指示直接转发不可用，MME发现在源eNodeB和目标eNodeB之间没有数据直接转发的连接，则对于每一个EPS承载，Bearers to Setup需要包含“Data forwarding not possible”指示。
  S1AP Cause指示从MME收到的RAN Cause。
6. 目标eNodeB向MME发送[Handover Request Ackownledge](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S1-MME/相关消息解释/Handover Request Ackownledge_30779126.md)消息，消息包含：EPS Bearer Setup list、EPS Bearers failed to setup list Target to Source transparent container。
  EPS Bearer Setup list是一张列表，包含地址和S1-U参考点上分配给目标eNodeB下行流量的TEID(一个承载分配一个TEID的原则)，如果必要的话也会包含地址和接受转发数据的TEID。
  如果UE-AMBR发生了变化，例如，关联到同一个APN的所有EPS承载被目标eNodeB拒绝，MME重新计算新UE-AMBR，并告知目标eNodeB。
  > **说明**
  > 如果所有default EPS bearers都被目标eNodeB拒绝，则MME拒绝handover。
7. **可选：**如果使用间接转发且S-GW重定位，MME向目标S-GW发送[Create Indirect Data Forwarding Tunnel Request](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S11/相关消息解释/Create Indirect Data Forwarding Tunnel Request_30779576.md)消息建立转发参数，消息包含：target eNodeB addresses and TEIDs for forwarding。
8. **可选：**目标S-GW向MME响应[Create Indirect Data Forwarding Tunnel Response](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S11/相关消息解释/Create Indirect Data Forwarding Tunnel Response_30779577.md)消息，消息包含：target Serving GW addresses and TEIDs for forwarding。间接转发可能经过不同于锚定UE数据的S-GW进行转发。
9. **可选：**如果采用间接转发（[Handover Required](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S1-MME/相关消息解释/Handover Required_30779127.md)消息中未携带Direct Forwarding Path Availability），MME向S-GW发送[Create Indirect Data Forwarding Tunnel Request](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S11/相关消息解释/Create Indirect Data Forwarding Tunnel Request_30779576.md)消息建立转发参数，消息包含：target eNodeB addresses and TEIDs for forwarding。S-GW重定位的情况下，消息包括到目标S-GW的隧道标识。
10. **可选：**S-GW向MME响应[Create Indirect Data Forwarding Tunnel Response](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S11/相关消息解释/Create Indirect Data Forwarding Tunnel Response_30779577.md)消息，消息包含：Serving GW addresses and TEIDs for forwarding。间接转发可能会经过不同于锚点S-GW的其他S-GW转发。
11. MME向源eNodeB发送[Handover Command](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S1-MME/相关消息解释/Handover Command_30779122.md)消息，消息包含：Target to Source transparent container、Bearers subject to forwarding、Bearers to Release。Bearers subject to forwarding包含地址和用于转发的TEID列表。Bearers to Release包含需要释放的承载列表。
  Handover Command由Target to Source transparent container构成，并发送给UE。在收到消息之后，UE将删除没有收到目标小区中相关EPS无线承载的EPS承载。MME Status Transfer
12. **可选：**源eNodeB向MME发送[eNB Status Transfer](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S1-MME/相关消息解释/eNB Status Transfer_30779110.md)消息，MME向目标eNodeB发送[1.3.2.2.25-MME Status Transfer](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S1-MME/相关消息解释/MME Status Transfer_86461950.md)消息，该消息传递E-RAB对应的PDCP和HFN状态信息。如果没有E-RAB采用PDCP状态保存机制，则源eNodeB可能不会发送此消息。
13. 源eNodeB使用直接转发从源eNodeB到目标eNodeB转发下行链路数据。
14. 源eNodeB使用间接转发从源eNodeB到目标eNodeB转发下行链路数据。
15. UE成功地同步到目标小区后，向目标eNodeB发送Handover Confirm消息。
  从源eNodeB转发的下行数据包可以发送给UE，同样，从UE发出的上行数据包可以转发给target Serving GW，到达PDN GW。
16. 目标eNodeB向MME发送[Handover Notify](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S1-MME/相关消息解释/Handover Notify_30779124.md)消息，消息包含：TAI+ECGI。MME启动一个定时器来监视源eNodeB和S-GW重定位情形下的源S-GW的资源的释放情况。
17. MME为每个PDN连接向目标S-GW发送[Modify Bearer Request](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S11/相关消息解释/Modify Bearer Request_30779591.md)消息，消息包含：eNodeB address and TEID allocated at the target eNodeB for downlink traffic on S1-U for the accepted EPS bearers。如果PDN GW请求了UE's location或者User CSG information（由UE上下文判断），MME也会在这条信息中包含这两个信元。如果UE的时区（Time Zone）发生了改变，MME在信息中包含UE Time Zone信元。
  MME将根据 [MME发起承载去激活（MME Initiated Dedicated Bearer Deactivation）](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/业务流程/会话管理/承载去激活（Bearer Deactivation）/MME发起承载去激活（MME Initiated Dedicated Bearer Deactivation）_30779047.md) 所属，触发承载释放流程，将释放non-accepted专有承载。Serving GW如果收到的non-accepted承载下行数据包，将丢弃这部分下行数据包，也不会向MME发送Downlink Data Notification。
  如果PDN连接的默认承载未被target eNodeB接受，并且没有激活的PDN连接，则MME将按照PDN连接的所有承载都未被接受来处理。MME触发MME请求的PDN释放流程（MME requested PDN disconnection procedure）来释放这些PDN连接。
18. 目标S-GW为来自P-GW的下行通道分配地址和TEIDs，并为每个PDN连接向P-GW发送[Modify Bearer Request](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S5_S8/相关消息解释/Modify Bearer Request_30779716.md)消息，消息包含：Serving GW addresses for user plane and TEID(s)、Serving Network。如果步骤[17](#ZH-CN_CONCEPT_0000001176391825__zh-cn_concept_0130779014_li21)包含了User Location Information信元、UE Time Zone信元或者User CSG Information信元，S-GW也会在此信息中包含。对于non-accepted承载，Serving GW也会为之分配基于S5/S8的下行TEID。
19. P-GW更新本地上下文并向目标S-GW返回[Modify Bearer Response](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S5_S8/相关消息解释/Modify Bearer Response_30779717.md)消息。PDN GW使用最新收到的地址和TEID，向target GW发送下行包。这些下行包将使用target Serving GW到target eNodeB的最新下行链路。
20. 目标S-GW向MME发送[Modify Bearer Response](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S11/相关消息解释/Modify Bearer Response_30779592.md)消息。
21. [TAU from E-UTRAN to E-UTRAN, intra-MME, with S-GW change](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/业务流程/移动性管理/TAU_RAU/TAU from E-UTRAN to E-UTRAN, intra-MME, with S-GW change_30778970.md)中所列举的任何一个条件满足，UE将发起TAU流程。
  > **说明**
  > 从handover消息收到的承载上下文中，MME得知这是UE执行的Handover流程，因此MME只执行TAU流程的子集。
22. 当[16](#ZH-CN_CONCEPT_0000001176391825__zh-cn_concept_0130779014_li18)中的定时器超时，MME向源eNodeB发送[UE Context Release Command](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S1-MME/相关消息解释/UE Context Release Command_30779158.md)消息。
23. 源eNodeB释放与UE相关的资源并向MME响应[UE Context Release Complete](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S1-MME/相关消息解释/UE Context Release Complete_30779162.md)消息。
24. 当[16](#ZH-CN_CONCEPT_0000001176391825__zh-cn_concept_0130779014_li18)中的定时器超时，且MME在Forward Relocation Response消息中收到S-GW改变指示，则MME向S-GW发送[Delete Session Request](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S11/相关消息解释/Delete Session Request_30779585.md)消息删除EPS承载资源，消息包含：Cause、 LBI。Cause指示S-GW变更及S-GW不要向P-GW发起承载删除流程。
25. S-GW向MME响应[Delete Session Response](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S11/相关消息解释/Delete Session Response_30779586.md)消息。
26. **可选：**如果使用间接转发且[16](#ZH-CN_CONCEPT_0000001176391825__zh-cn_concept_0130779014_li18)中的定时器超时，MME向源S-GW发送[Delete Indirect Data Forwarding Tunnel Request](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S11/相关消息解释/Delete Indirect Data Forwarding Tunnel Request_30779583.md)消息，释放[9](#ZH-CN_CONCEPT_0000001176391825__zh-cn_concept_0130779014_li11)中为间接转发分配的临时资源。
27. **可选：**源S-GW向MME响应[Delete Indirect Data Forwarding Tunnel Response](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S11/相关消息解释/Delete Indirect Data Forwarding Tunnel Response_30779584.md)消息。
28. **可选：**如果使用间接转发且[16](#ZH-CN_CONCEPT_0000001176391825__zh-cn_concept_0130779014_li18)中的定时器超时，MME向目标S-GW发送[Delete Indirect Data Forwarding Tunnel Request](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S11/相关消息解释/Delete Indirect Data Forwarding Tunnel Request_30779583.md)消息，释放[7](#ZH-CN_CONCEPT_0000001176391825__zh-cn_concept_0130779014_li8)中为间接转发分配的临时资源。
29. **可选：**目标S-GW向MME响应[Delete Indirect Data Forwarding Tunnel Response](../../../../../../../快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/S11/相关消息解释/Delete Indirect Data Forwarding Tunnel Response_30779584.md)消息。
