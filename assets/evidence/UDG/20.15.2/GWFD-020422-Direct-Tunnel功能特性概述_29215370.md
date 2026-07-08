# GWFD-020422 Direct Tunnel功能特性概述

- [适用NF](#ZH-CN_CONCEPT_0229215370__1.4.1.1)
- [定义](#ZH-CN_CONCEPT_0229215370__1.4.2.1)
- [客户价值](#ZH-CN_CONCEPT_0229215370__1.4.3.1)
- [应用场景](#ZH-CN_CONCEPT_0229215370__1.4.4.1)
- [可获得性](#ZH-CN_CONCEPT_0229215370__1.4.5.1)
- [对系统的影响](#ZH-CN_CONCEPT_0229215370__1.4.6.1)
- [应用限制](#ZH-CN_CONCEPT_0229215370__1.4.7.1)
- [与其他特性的交互](#ZH-CN_CONCEPT_0229215370__1.4.8.1)
- [原理概述](#ZH-CN_CONCEPT_0229215370__1.4.9.1)
- [特性规格](#ZH-CN_CONCEPT_0229215370__1.4.10.1)
- [遵循标准](#ZH-CN_CONCEPT_0229215370__1.4.11.1)
- [发布历史](#ZH-CN_CONCEPT_0229215370__1.4.12.1)

#### [适用NF](#ZH-CN_CONCEPT_0229215370)

PGW-U

#### [定义](#ZH-CN_CONCEPT_0229215370)

随着3G业务不断的开展，以及HSPA等技术的应用，UMTS网络越来越需要提高用户面处理能力。原有的网络是分别在RNC与SGSN、SGSN与PGW-U之间建立GTP-U通道的（ Indirect Tunnel ）。为此，RNC、SGSN以及PGW-U等网元需要同时增强相应的用户面处理性能，这样会增加运营商的资金投入和运营成本。

#### [客户价值](#ZH-CN_CONCEPT_0229215370)

| 受益方 | 受益描述 |
| --- | --- |
| 运营商 | - 节约UP用户面资源，减少相关运营投资和运营费用。<br>- 实现了信令面和用户面分离，便于以后升级到EPC网络。<br>- 用户面的扩容不再需要升级SGSN，只需要升级PGW-U和RNC，从而提高了网络的可扩容性。 |
| 用户 | 减少用户数据时延，提升用户体验。 |

#### [应用场景](#ZH-CN_CONCEPT_0229215370)

为了减少运营商的投资费用和运营费用，以及便于后续的网络扩容，3GPP提出了Direct Tunnel解决方案。Direct Tunnel功能将RNC与SGSN、SGSN与PGW-U之间用户面的两段隧道（ Indirect Tunnel ）优化为一段隧道，优化后用户面转发不经过SGSN，而直接在RNC和PGW-U之间建立GTP-U隧道，通过节省用户面资源降低了运营商的资金投入和运营成本，同时也优化了UMTS网络用户面的性能。

#### [可获得性](#ZH-CN_CONCEPT_0229215370)

**涉及网元**

| **涉及网元** | **支持版本** | **功能说明** |
| --- | --- | --- |
| RNC | 无特殊要求 | 支持在RNC和PGW-U之间建立GTP-U隧道。 |
| SGSN | V100R018C10及后续版本 | 支持在PDP Context的激活、保留以及业务更新流程中向PGW-C发送Update PDP Context消息。 |
| PGW-C | UNC 20.3.0及后续版本 | 支持在PDP Context的激活、保留以及业务更新流程中向PGW-U发送PFCP Session Modification Request。 |
| PGW-U | UDG 20.3.0及后续版本 | 支持在RNC和PGW-U之间建立GTP-U隧道。 |
| BSS/RAN | 无特殊要求 | - |

**License支持**

本特性只有获得了License许可后才能获得该特性的服务，对应的License控制项为 “82200BLC LKV3G5DTTL01 Direct Tunnel功能”。

#### [对系统的影响](#ZH-CN_CONCEPT_0229215370)

性能影响程度：中

> **说明**
> 性能影响程度都是基于华为默认SA模型基础上评估。

- 对于信令面，SGSN在PDP Context的激活、保留以及Service Request流程中增加了向PGW-C发送Update PDP Context消息以及PGW-C发送PFCP Session Modification消息的操作，增加了SGSN、PGW-C和PGW-U的信令处理负荷。
- 对于用户面，PGW-U的数据直接发送到RNC，减少了SGSN的处理以及数据传递的时延，从而可以提高用户体验；同时还减少了SGSN用户面资源。

详细性能影响需要基于流量模型进行评估，请联系华为技术支持获取服务。

#### [应用限制](#ZH-CN_CONCEPT_0229215370)

如下场景下，不能部署Direct Tunnel解决方案：

- 对漫游用户，需要使用拜访网络中的SGSN用户面的功能，SGSN需要对用户流量计费，用于运营商之间的结算。
- GTP V0不能携带DT扩展标识，只能使用Indirect Tunnel方式。
- 在2G用户业务、非HPLMN和MVNO用户业务等场景下，只能使用Indirect Tunnel方式。

#### [与其他特性的交互](#ZH-CN_CONCEPT_0229215370)

本特性与其他特性无交互关系。

#### [原理概述](#ZH-CN_CONCEPT_0229215370)

**组网架构**

UMTS网络使用Direct Tunnel解决方案后，原来的网络结构发生变化：RNC与PGW-U之间直接建立用户面隧道，同时也支持原来的 Indirect Tunnel 机制，具体的网络结构如 [图1](#ZH-CN_CONCEPT_0229215370__fig20) 所示。

**图1** Direct Tunnel网络架构示意图

<br>

![](GWFD-020422 Direct Tunnel功能特性概述_29215370.assets/zh-cn_image_0229215372.png)

<br>

**协议栈**

- 用户面
    - 协议栈
      UMTS网络使用Direct Tunnel解决方案后，用户面的协议栈也发生变化：需要增加RNC与PGW-U之间进行用户面数据交互的协议栈。使用 Indirect Tunnel 的用户面协议栈结构如 [图2](#ZH-CN_CONCEPT_0229215370__fig21) 所示。
      **图2** Indirect Tunnel 用户面协议栈结构示意图

      <br>

      ![](GWFD-020422 Direct Tunnel功能特性概述_29215370.assets/zh-cn_image_0229215374.png "点击放大")

      <br>
      使用Direct Tunnel的用户面协议栈结构如 [图3](#ZH-CN_CONCEPT_0229215370__fig2) 所示。
      **图3** Direct Tunnel用户面协议栈结构示意图

      <br>

      ![](GWFD-020422 Direct Tunnel功能特性概述_29215370.assets/zh-cn_image_0229215378.png "点击放大")

      <br>
- 信令面
    - 协议栈
      UMTS网络使用Direct Tunnel解决方案后，信令面的协议栈未发生变化。使用Direct Tunnel的信令面协议栈结构如 [图4](#ZH-CN_CONCEPT_0229215370__fig3) 、 [图5](#ZH-CN_CONCEPT_0229215370__fig24) 所示。
      **图4** Direct Tunnel信令面Iu接口协议栈结构示意图

      <br>

      ![](GWFD-020422 Direct Tunnel功能特性概述_29215370.assets/zh-cn_image_0229215379.png)

      <br>
      **图5** Direct Tunnel信令面Gn接口协议栈结构示意图

      <br>

      ![](GWFD-020422 Direct Tunnel功能特性概述_29215370.assets/zh-cn_image_0229215380.png)

      <br>

**业务流程**

- 一次PDP Context激活流程
  SGSN收到来自MS的Activate PDP Context Request消息，并完成RNC与PGW-U之间Direct Tunnel的建立。消息流程图如 [图6](#ZH-CN_CONCEPT_0229215370__fig1) 所示。
  **图6** 一次PDP Context激活流程

  <br>

  ![](GWFD-020422 Direct Tunnel功能特性概述_29215370.assets/zh-cn_image_0231152594.png)
    1. MS向SGSN发送Activate PDP Context Request消息。
    2. SGSN分配用户面IP地址、TEID，并通过Create PDP Context Request消息发送到PGW-C。
    3. PGW-C发送PFCP Session Establishment Request消息给PGW-U，消息中携带SGSN用户面IP地址、TEID。PGW-U回应PFCP Session Establishment Response消息给PGW-C，消息中携带PGW-U用户面IP地址、TEID。
    4. PGW-C回应Create PDP Context Response消息到SGSN，消息中携带PGW-U的用户面IP地址、TEID。
    5. SGSN根据配置信息判断是否启用Direct Tunnel。启用Direct Tunnel，SGSN发送RAB Assignment Request消息到RNC，消息中包含PGW-U用户面IP地址、TEID等信息。RAN与MS建立无线承载后，RNC发送RAB Assignment Response消息到SGSN，消息中携带RNC用户面IP地址、TEID。
    6. 如果RAN的跟踪功能激活，则SGSN会向RAN发送Invoke Trace消息，消息中的Trace Reference和Trace Type取值来自HLR或者OMC的跟踪信息。
    7. SGSN发送Update PDP Context Request消息给PGW-C，消息中携带RNC用户面IP地址、RNC用户面TEID，以及DTI=True(指示启用Direct Tunnel)，用以建立PGW-U和RNC之间的用户面。
    8. PGW-C发送PFCP Session Modification Request消息给PGW-U，消息中携带RNC用户面IP地址、RNC用户面TEID。PGW-U回应PFCP Session Modification Response消息到PGW-C。
    9. PGW-C向SGSN返回Update PDP Context Response消息。如果PGW-C更新PDP Context成功，SGSN更新本地数据库的信息，继续保留原来保存的RNC、PGW-U以及SGSN的用户面IP地址、TEID等信息。如果PGW-C更新PDP Context失败，则SGSN发起去激活流程删除所创建的资源，同时建立Direct Tunnel失败统计数。
    10. SGSN向MS发送Activate PDP Context Accept消息完成此次激活流程。
  此后，MS可以进行上下行业务：上行业务数据由RNC直接发送到PGW-U，下行业务数据由PGW-U直接发送到RNC。
  > **说明**
  > Direct Tunnel与 Indirect Tunnel 消息流程差异：
  >
  > - 修改流程[5](#ZH-CN_CONCEPT_0229215370__DT1)中的RAB Assignment Request消息，消息中会携带PGW-U用户面IP地址和TEID。
  > - 新增流程[7](#ZH-CN_CONCEPT_0229215370__DT2)中的Update PDP Context Request消息，Update PDP Context Request消息中携带RNC的用户面IP地址、TEID以及为True的DTI标记。
- RAB释放流程
  Indirect Tunnel 场景下，SGSN收到来自RNC的RAB Release消息，SGSN启动PDP保留过程，SGSN释放RAN侧资源，但继续保留SGSN与PGW-U之间的连接。在Direct Tunnel场景下，SGSN与PGW-U之间没有用户面连接，所以SGSN需更新与PGW-U之间的连接。消息流程图如 [图7](#ZH-CN_CONCEPT_0229215370__fig4) 所示。
  **图7** RAB释放流程

  <br>

  ![](GWFD-020422 Direct Tunnel功能特性概述_29215370.assets/zh-cn_image_0231157613.png)
    1. RAN向SGSN发送RAB Release Request消息启动流程。
    2. SGSN发送Update PDP Context Request消息到PGW-C，消息中携带SGSN用户面IP地址、TEID以及为False的DTI标记，建立SGSN和PGW-U间的GTP隧道。
    3. PGW-C发送PFCP Session Modification Request消息到PGW-U，消息中携带SGSN用户面IP地址、TEID。PGW-U发送PFCP Session Modification Response消息到PGW-C。
    4. PGW-C向SGSN返回Update PDP Context Response消息，PDP Context更新成功。如果PGW-C更新PDP Context失败，则SGSN发起去激活流程删除所创建的资源。
    5. SGSN向RAN发送RAB Assignment Request消息释放RAN侧无线承载资源。
    6. RAN释放与MS间的无线承载资源。
    7. RAN向SGSN返回RAB Assignment Response消息确认其释放结束。
  > **说明**
  > Direct Tunnel与 Indirect Tunnel 消息流程差异：新增流程 [2](#ZH-CN_CONCEPT_0229215370__DT15) 中的Update PDP Context消息，Update PDP Context Request消息中携带SGSN的用户面IP地址、TEID以及为False的DTI标记。
- MS发起的Service Request流程
  SGSN收到MS发送Service Request（Service Type = Data）消息后，判定Direct Tunnel特性已经启用，则完成RNC与PGW-U之间GTP-U通道的建立。消息流程图如 [图8](#ZH-CN_CONCEPT_0229215370__fig6) 所示。
  **图8** MS发起的Service Request流程

  <br>

  ![](GWFD-020422 Direct Tunnel功能特性概述_29215370.assets/zh-cn_image_0231159690.png)
    1. 如果不存在CS域话务量，MS建立一个RRC连接。
    2. MS向SGSN发送Service Request消息，消息中的Service Type指明所申请的业务类型为Data。此时在MS和SGSN之间将会建立信令连接，同时分配激活的PDP Context资源（如RAB）。
    3. 如果是处于PMM-IDLE状态的MS初始化Service Request，SGSN将会执行安全功能。
    4. 如果是处于PMM-IDLE状态的MS初始化Service Request，且Service Type为Data，SGSN将会向MS返回Service Accept消息。
      同时SGSN判断已经为该PDP启动了Direct Tunnel功能，则在Radio Access Bearer Assignment Request消息中将PGW-U的用户面IP地址、TEID发送给RNC建立无线接入承载。
    5. RNC通过RRC建立无线承载。
    6. RRC无线承载建立完成后，服务RNC向SGSN返回Radio Access Bearer Assignment Response消息，消息中携带RNC用户面IP地址、TEID。
    7. 如果消息中指示RNC创建无线承载失败，则SGSN向PGW-C发送Delete PDP Context Request消息并删除所创建的资源。反之，SGSN判断已经为该PDP启动了Direct Tunnel功能，则向PGW-C发送Update PDP Context Request消息指示其建立与RNC的用户面连接，消息中携带RNC的用户面IP地址、TEID以及为True的DTI标记。
    8. PGW-C发送PFCP Session Modification Request消息到PGW-U，消息中携带RNC用户面IP地址、TEID。PGW-C收到PGW-U的PFCP Session Modification Response响应消息，向SGSN返回Update PDP Context Response消息，Service Request流程成功结束。如果PGW-C更新失败，则SGSN发起去激活流程，删除所创建的资源并建立Direct Tunnel失败的统计数。
    9. MS开始传送上行链路分组数据。
  > **说明**
  > Direct Tunnel与 Indirect Tunnel 消息流程差异：
  >
  > - 修改流程[4](#ZH-CN_CONCEPT_0229215370__DT12)中的RAB Assignment Request消息，消息中会携带PGW-U用户面IP地址和TEID。
  > - 新增流程[7](#ZH-CN_CONCEPT_0229215370__DT3)中的Update PDP Context Request消息，Update PDP Request消息中携带RNC的用户面IP地址、TEID以及为True的DTI标记。
- 网络发起的Service Request流程
  SGSN收到某MS的下行链路分组数据，并且该MS处于PMM-IDLE状态，SGSN判定Direct Tunnel特性已经启用，则完成RNC与PGW-U之间GTP-U通道的建立，并释放原来所创建的用户面资源。消息流程图如 [图9](#ZH-CN_CONCEPT_0229215370__fig7) 所示。
  **图9** 网络发起的Service Request流程

  <br>

  ![](GWFD-020422 Direct Tunnel功能特性概述_29215370.assets/zh-cn_image_0231159709.png)
    1. SGSN收到了处于PMM-IDLE状态的MS的下行链路PDP PDU（Packet Data Unit）。
    2. SGSN发现相关的PDP Context已经被激活，但是RAB处于无效状态，同时SGSN判断已经为该PDP启动了Direct Tunnel功能，则通过RNC向MS发起寻呼。
    3. MS与RNC之间建立起一条RRC连接。
    4. RRC连接建立后，MS向SGSN发送Service Request消息，消息中的Service Type为“Paging Response”。
    5. SGSN将执行安全模式流程。
    6. SGSN完成安全模式流程后，会在Radio Access Bearer Assignment Request消息中将PGW-U的用户面IP地址、TEID发送给RNC建立无线接入承载。RNC建立无线接入承载后，向SGSN返回Radio Access Bearer Assignment Response消息。
    7. SGSN判断已经为该PDP启动了Direct Tunnel功能，则向PGW-C发送Update PDP Context Request消息指示其建立与RNC的用户面连接，消息中携带RNC的用户面IP地址、TEID以及为True的DTI标记。如果消息中指示RNC创建无线承载失败，则SGSN向PGW-C发送Delete PDP Context Request消息并删除所创建的资源。
    8. PGW-C发送PFCP Session Modification Request消息到PGW-U，消息中携带SGSN用户面IP地址、TEID。收到PGW-U的PFCP Session Modification Response响应消息，PGW-C向SGSN返回Update PDP Context Response消息，Service Request流程成功结束。如果PGW-C更新失败，则SGSN发起去激活流程，删除所创建的资源。
    9. SGSN向MS发送下行分组数据。
  > **说明**
  > 对于实时类业务如流媒体、会话业务，在RAB释放、Iu释放过程中，PDP Context继续被保留；PDP Context不被保留时，SGSN会把QoS标志置为无效，同时通知PGW-U将上下行速率都更新为0 kbit/s。在以上情况下，不能由MS或网络发起的Service Request流程来完成RAB的重建，而需要由MS发起PDP Context的修改流程或去激活流程来完成。
  >
  > Direct Tunnel与 Indirect Tunnel 消息流程差异：
  >
  > - 修改流程[6](#ZH-CN_CONCEPT_0229215370__DT12)中的RAB Assignment Request消息，消息中会携带PGW-U用户面IP地址和TEID。
  > - 新增流程[7](#ZH-CN_CONCEPT_0229215370__DT4)中的Update PDP Context Request消息，Update PDP Request消息中携带RNC的用户面IP地址、TEID以及为True的DTI标记。
- SGSN间路由区更新流程
  Direct Tunnel特性对处于PMM-IDLE状态的MS的SGSN间路由区更新流程没有影响，对处于PMM-CONNECTED状态的MS的Inter SGSN RAU流程，新、旧SGSN需要创建用户资源将RNC缓存的下行分组数据转发到目标RNC并保证数据的完好无损；同时新SGSN需要建立与PGW-U之间的GTP通道。消息流程图如 [图10](#ZH-CN_CONCEPT_0229215370__fig9) 所示。
  **图10** SGSN间路由区更新流程

  <br>

  ![](GWFD-020422 Direct Tunnel功能特性概述_29215370.assets/zh-cn_image_0234842838.png)
    1. 新SGSN收到来自新RNC的RAU Request消息。
    2. 新SGSN发送SGSN Context Request消息到旧SGSN，用于从旧SGSN获得相关Context信息。
    3. 旧SGSN发送SRNS Context Request消息到旧RNC，执行SRNS Context Procedure，用于旧SGSN从旧RNC中获取SRNS Context信息。
    4. 旧RNC将SRNS Context Response消息发送给旧SGSN。
    5. 旧SGSN将SGSN Context Response消息发送给新SGSN。
    6. 新SGSN根据MS的当前状态，决定是否执行Security Function过程。
    7. 新SGSN向旧SGSN发送SGSN Context Acknowledge消息，主要用于通知旧SGSN可以开始进行数据转发了。
    8. 旧SGSN发送SRNS Data Forward Command消息给旧RNC，通知转发旧RNC中的用户面数据。消息中通知RNC的是旧SGSN的用户面地址和TEID信息。
    9. 旧RNC将用户面数据转发到旧SGSN。
    10. 旧SGSN将用户面数据转发到新SGSN。
    11. 新SGSN发送Update PDP Context Request (SGSN Addr，TEID，DTI=False不启用Direct Tunnel)消息给PGW-C。
    12. PGW-C发送PFCP Session Modification Request (SGSN Addr，TEID)消息给PGW-U。
    13. PGW-U发送PFCP Session Modification Response消息给PGW-C。
    14. PGW-C向新SGSN发送Update PDP Context Response消息。
    15. 新SGSN执行Update Location Procedure，主要从HLR获取相关签约信息。
    16. 旧SGSN会收到来自HLR的Cancel Location Request消息，并执行Cancel Location Procedure过程。
    17. 旧SGSN发送Iu Release Command消息给旧RNC。
    18. 旧RNC转发完数据以后，发送Iu Release Complete消息给旧SGSN。
    19. 新SGSN发送RAU Accept消息给新RNC。
    20. 新RNC发送RAU Complete消息给新SGSN。
  > **说明**
  > 在 Indirect Tunnel 的Inter RAU Procedure处理过程中，SGSN原来需要向PGW-C发送了Update PDP Context Request消息，所以Direct Tunnel处理过程没有增加消息。
  >
  > 与 Indirect Tunnel 的处理过程相比，Intra RAU Procedure处理过程中，如果启动Direct Tunnel，在SGSN和PGW-C之间增加了Update PDP Context消息，主要将SGSN用户面地址和TEID通知PGW-C。
- SGSN内服务RNS重定位流程
  Direct Tunnel场景的SGSN内服务RNS重定位流程中，SGSN需要直接建立PGW-U与目标RNC之间的GTP通道。消息流程图如 [图11](#ZH-CN_CONCEPT_0229215370__fig10) 所示。
  **图11** SGSN内服务RNS重定位流程

  <br>

  ![](GWFD-020422 Direct Tunnel功能特性概述_29215370.assets/zh-cn_image_0234854832.png)
    1. 源RNC决定执行服务RNS重定位流程。这时上下行链路的用户数据流过以下通道：MS与源RNS之间的无线承载通道，源RNC与SGSN之间的GTP-U通道，SGSN与PGW-U之间的GTP-U通道。
    2. 源RNC向SGSN发送Relocation Required消息，消息中包含了重定位协调、安全功能以及RRC协议上下文等必要的信息。
    3. SGSN根据原来建立的Direct Tunnel承载信息中获取PGW-U用户面IP地址、TEID信息，然后将这些信息包含在Relocation Request消息中发送给目标RNC。目标RNC完成无线接入承载的建立后，向SGSN发送Relocation Request Acknowledge消息。
    4. SGSN向源RNC发送Relocation Command消息，并告知其关于数据转发的一些相关信息。
    5. 源RNC将用户面数据转发到目标RNC。
    6. 源RNC向目标RNC发送Relocation Commit消息。
    7. 目标RNC向SGSN发送Relocation Detect消息。
    8. 目标RNC向MS发送RAN Mobility Information消息，消息中包含了UE以及CN的一些信息元素。MS向目标RNC返回确认消息。
    9. 目标RNC向SGSN发送Relocation Complete消息。
    10. SGSN收到消息后向源RNC发送Iu Release Command消息。源RNC上数据转发的定时器超时后，源RNC会回复Iu Release Complete消息。
    11. SGSN向PGW-C发送Update PDP Context Request消息通知其修改PDP Context的相关信息，消息中包含目标RNC的用户面IP地址、TEID以及DTI标志。
    12. PGW-C向PGW-U发送PFCP Session Modification Request消息，消息中包含RNC的用户IP地址、TEID。PGW-U发送PFCP Session Modification Response消息给PGW-C。
    13. PGW-C更新完成后向SGSN返回Update PDP Context Response消息。
  > **说明**
  > Direct Tunnel与 Indirect Tunnel 消息流程差异：新增流程 [11](#ZH-CN_CONCEPT_0229215370__DT10) 中的Update PDP Context消息，Update PDP Context Request消息中指明RNC的用户面IP地址、TEID以及DTI标记。
  >
  > 如果SGSN不支持DT，也会有出现流程 [11](#ZH-CN_CONCEPT_0229215370__DT10) 的情况，例如：从Source RNC切换到TargetRNC后，QoS发生了改变等。流程 [3](#ZH-CN_CONCEPT_0229215370__DT9) 中的Relocation Request消息和流程 [11](#ZH-CN_CONCEPT_0229215370__DT10) 中的Update PDP Context Request消息中携带的是SGSN的用户面IP地址。
- SGSN间服务RNS重定位流程
  Direct Tunnel场景的SGSN间服务RNS重定位流程中，新SGSN需要直接建立PGW-U与目标RNC之间的GTP通道。消息流程图如 [图12](#ZH-CN_CONCEPT_0229215370__fig11) 所示。
  **图12** SGSN间服务RNS重定位流程

  <br>

  ![](GWFD-020422 Direct Tunnel功能特性概述_29215370.assets/zh-cn_image_0234857866.png)
    1. 源RNC决定执行服务RNS重定位流程。这时上下行链路的用户数据流过以下通道：MS与源RNS之间的无线承载通道，源RNC与SGSN之间的GTP-U通道，SGSN与PGW-U之间的GTP-U通道。
    2. 源RNC向旧SGSN发送Relocation Required消息，消息中包含了重定位协调、安全功能以及RRC协议上下文等必要的信息。
    3. 旧SGSN向新SGSN发送Forward Relocation Request消息，消息中包含PDP Context的相关信息。
    4. 新SGSN根据Forward Relocation Request消息中的GCSI以及其它相关信息判断系统启用了Direct Tunnel特性，然后将PGW-U用户面IP地址、TEID信息包含在Relocation Request消息中发送给目标RNC。目标RNC完成无线接入承载的建立后，向新SGSN发送Relocation Request Acknowledge消息。
    5. 新SGSN向旧SGSN返回Forward Relocation Response消息。
    6. 旧SGSN向源RNC发送Relocation Command消息，并告知其关于数据转发的一些相关信息。
    7. 源RNC将用户面数据转发到目标RNC。
    8. 源RNC向目标RNC发送Relocation Commit消息。
    9. 目标RNC向新SGSN发送Relocation Detect消息。
    10. 目标RNC向MS发送RAN Mobility Information消息，消息中包含了UE以及CN的一些信息元素。
    11. 目标RNC向新SGSN发送Relocation Complete消息。
    12. 新SGSN向旧SGSN发送Forward Relocation Complete消息告知数据转发完成。旧SGSN向新SGSN返回Forward Relocation Complete Acknowledge消息。
    13. 新SGSN向PGW-C发送Update PDP Context Request消息通知其修改PDP Context的相关信息，消息中携带目标RNC的用户面IP地址、TEID以及DTI标志。
    14. PGW-C向PGW-U发送PFCP Session Modification Request消息，消息中包含RNC的用户IP地址、TEID。PGW-U发送PFCP Session Modification Response消息给PGW-C。
    15. PGW-C更新完成后向新SGSN返回Update PDP Context Response消息。
    16. 旧SGSN向源RNC发送Iu Release Command消息。源RNC上数据转发的定时器超时后，源RNC会回复Iu Release Complete消息。
  > **说明**
  > Direct Tunnel与 Indirect Tunnel 消息流程差异：修改流程 [13](#ZH-CN_CONCEPT_0229215370__DT7) 中的Update PDP Context Request消息，Update PDP Context Request消息中携带RNC的用户面IP地址、TEID以及DTI标记。
  >
  > 如果新SGSN不支持DT，流程 [4](#ZH-CN_CONCEPT_0229215370__DT8) 中的Relocation Request消息和流程 [13](#ZH-CN_CONCEPT_0229215370__DT7) 中的Update PDP Context Request消息中携带的是SGSN的用户面IP地址。
- SGSN间A/Gb模式到Iu模式改变流程
  MS的PDP在2G系统中运行于 Indirect Tunnel 场景下。在从2G系统改变到3G系统的过程结束后，如果MS需要传送上行链路数据，则会向新SGSN（3G）发起Service Request流程，新SGSN（3G）直接建立PGW-U与RNC之间的GTP-U隧道，并释放原来使用的用户面资源。消息流程图如 [图13](#ZH-CN_CONCEPT_0229215370__fig15) 所示。
  **图13** SGSN间A/Gb模式到Iu模式改变流程

  <br>

  ![](GWFD-020422 Direct Tunnel功能特性概述_29215370.assets/zh-cn_image_0234859180.png)
    1. MS或RAN决定进行系统间改变操作使MS连接到一个使用Iu模式的新小区。MS向新SGSN（3G）发送Routing Area Update Request消息发起路由区更新。
    2. SGSN（3G）向SGSN（2G）发送SGSN Context Request消息查询该MS的相关PDP Context。
    3. SGSN（2G）向SGSN（3G）发送SGSN Context Response消息返回该MS的相关PDP Context。
    4. SGSN（3G）会执行安全功能的流程，成功后会创建相关的用户面资源（继续使用原来的SGSN用户面TEID、IP地址）。
    5. SGSN（3G）向SGSN（2G）发送SGSN Context Acknowledge消息，消息中包含SGSN（3G）的用户面TEID、IP地址，告知其已准备好接收属于已激活PDP Context的分组数据。
    6. SGSN（2G）将缓存的GTP-PDU数据转发给SGSN（3G）。
    7. SGSN（3G）向PGW-C发送Update PDP Context Request消息通知其更新PDP Context的相关信息，消息中携带SGSN（3G）的用户面TEID、IP地址和为False的DTI（不启动Direct Tunnel）。
    8. PGW-C向PGW-U发送PFCP Session Modification Request消息，消息中包含SGSN（3G）的用户面IP、TEID。PGW-U发送PFCP Session Modification Response消息给PGW-C。
    9. PGW-C更新完成后向SGSN（3G）返回Update PDP Context Response消息。
    10. SGSN（2G）执行Cancel Location流程。
    11. SGSN（3G）执行Update GPRS Location流程。
    12. SGSN（3G）向MS发送Routing Area Update Accept消息。
    13. MS向SGSN（3G）发送Routing Area Update Complete消息以确认TMSI的重分配。
    14. MS需要传送上行链路分组数据，则向SGSN（3G）发送Service Request消息，Service Type参数为Data。
    15. SGSN（3G）判断已将为该PDP启动了Direct Tunnel功能，则在RAB Assignment Request消息中将PGW-U用户面TEID、IP地址等信息发送给RNC。
    16. RNC建立与MS之间的无线承载。
    17. RNC向SGSN（3G）返回RAB Assignment Response消息，消息中携带有RNC用户面IP地址、TEID。
    18. SGSN（3G）判断已将为该PDP启动了Direct Tunnel功能，则向PGW-C发送Update PDP Context Request消息，消息中包含RNC用户面TEID、IP地址以及为True的DTI标志。
    19. PGW-C向PGW-U发送PFCP Session Modification Request消息，消息中包含RNC用户面IP、TEID。PGW-U发送PFCP Session Modification Response消息给PGW-C。
    20. PGW-C更新完成后向SGSN（3G）返回Update PDP Context Response消息。
  > **说明**
  > Direct Tunnel与 Indirect Tunnel 消息流程差异：
  >
  > - 修改流程[15](#ZH-CN_CONCEPT_0229215370__DT6)中的RAB Assignment Request消息，消息中指明PGW-U的用户面IP地址、TEID。
  > - 新增流程[18](#ZH-CN_CONCEPT_0229215370__DT14)中的Update PDP Context消息，Update PDP Context Request消息中指明RNC的用户面IP地址、TEID以及DTI标记。
  >
  > Iu模式到A/Gb模式改变流程，需要修改为 Indirect Tunnel 方式，没有新增消息，只是流程 [15](#ZH-CN_CONCEPT_0229215370__DT6) 中的RAB Assignment Request消息和流程 [18](#ZH-CN_CONCEPT_0229215370__DT14) 中的Update PDP Context Request消息携带的是SGSN的用户面IP地址、TEID。
- Direct Tunnel变更为Indirect Tunnel流程
  MS激活时使用Direct Tunnel模式，当需要修改为Indirect Tunnel模式时，SGSN发起本流程。消息流程图如 [图14](#ZH-CN_CONCEPT_0229215370__fig17) 所示。
  **图14** Direct Tunnel变更为Indirect Tunnel处理流程

  <br>

  ![](GWFD-020422 Direct Tunnel功能特性概述_29215370.assets/zh-cn_image_0231160883.png)
    1. SGSN向PGW-C发送Update PDP Context Request消息，消息中携带SGSN用户面IP地址和TEID。
    2. PGW-C向PGW-U发送PFCP Session Modification Request消息，消息中携带SGSN用户面IP地址、TEID。
    3. PGW-U向PGW-C响应PFCP Session Modification Response消息。
    4. PGW-C向SGSN响应Update PDP Context Response消息。
    5. SGSN向RNC发送RAB Assignment Request消息，消息中携带SGSN用户面IP地址、TEID。
    6. RNC修改与MS之间的无线承载资源。
    7. RNC向SGSN响应RAB Assignment Response消息。
- 错误指示流程
  > **说明**
  > 如果SGSN升级到支持Direct Tunnel的版本，而RNC、PGW-U没有升级到支持Direct Tunnel的版本，由Error Indication消息所引起的MS、SGSN的PDP Context的挂起可以由RNC发起的Iu Release流程，MS发起的Service Request、Detach以及Inter SGSN RAU等流程进行恢复。
  在Direct Tunnel的运行场景下，下行数据由PGW-U发送到RNC，当PGW-U收到RNC发送的Error Indication消息后，需要通知SGSN进行相关处理以避免PGW-U、RNC中的PDP Context被删除，以及SGSN、MS中的PDP Context被挂起。消息流程图如 [图15](#ZH-CN_CONCEPT_0229215370__fig16) 所示。
  **图15** PGW-U收到RNC的Error Indication消息处理流程

  <br>

  ![](GWFD-020422 Direct Tunnel功能特性概述_29215370.assets/zh-cn_image_0231161359.png)
    1. PGW-U向RNC发送下行链路数据。
    2. RNC没有找到下行链路数据相关的PDP Context，则向PGW-U发送Error Indication消息。
    3. PGW-U收到Error Indication消息向PGW-C发送PFCP Session Report Request消息。
    4. PGW-C发送PFCP Session Report Response响应消息给PGW-U。
    5. PGW-C向SGSN发送Update PDP Context Request消息，消息中设置了E1比特位。
    6. SGSN发现Update PDP Context Request消息中设置了E1比特位，且已经为该PDP启动了Direct Tunnel功能，则使用原来保留的用户面TEID以及IP地址创建与PGW-U之间的用户面资源，然后向PGW-C返回Update PDP Context Response消息，消息中包含SGSN用户面的TEID、IP地址以及为False的DTI标志。
    7. PGW-C向PGW-U发送PFCP Session Modification Request消息，消息中携带SGSN用户面IP地址、TEID。
    8. PGW-U向PGW-C响应PFCP Session Modification Response消息。
    9. Service Request Procedure过程。可以是MS发起的Service Request Procedure或网络侧发起的Service Request Procedure。

#### [特性规格](#ZH-CN_CONCEPT_0229215370)

本特性无特殊规格。

#### [遵循标准](#ZH-CN_CONCEPT_0229215370)

| 标准类别 | 标准名称 |
| --- | --- |
| 3GPP | 3GPP TS 23.060 General Packet Radio Service (GPRS) Service Description; Stage 2 |
| 3GPP | 3GPP TS 29.060 General Packet Radio Service (GPRS); GPRS Tunnelling Protocol (GTP) across the Gn and Gp interface |

#### [发布历史](#ZH-CN_CONCEPT_0229215370)

| 特性版本 | 发布版本 | 发布说明 |
| --- | --- | --- |
| 01 | 20.3.0 | 首次发布，Direct Tunnel特性。 |
