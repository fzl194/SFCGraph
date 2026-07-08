# 基于N26接口的EPS到5GS多切片时的重选（I-SMF插入判断，I-SMF不变）

- [业务场景](#ZH-CN_CONCEPT_0000001148395107__1.3.1.1)
- [信令流程](#ZH-CN_CONCEPT_0000001148395107__1.3.2.1)

#### [业务场景](#ZH-CN_CONCEPT_0000001148395107)

多切片场景下，当UE在EPC中处于ECM-IDLE状态，UE从EPS覆盖区移动到5GS覆盖区，UE会尝试选择更优的5G网络，进行移动性注册更新流程。

当UE所在区域超出了原来SMF的服务范围，AMF判断需要插入I-SMF，AMF需要根据切片ID和TAI向NRF查询I-SMF，获取能够为当前服务区域提供服务的I-SMF，以保证用户会话业务的连续性。

为支持以上场景，核心网做如下相关操作：

- SMF作为PGW-C在PDN Connection建立流程中通过PCO给UE分配S-NSSAI。分配S-NSSAI有两种方法，一是基于本地配置选择，二是从UDM获取签约的切片和DNN信息。推荐SMF本地根据DNN配置用于N26互操作流程的切片。
- 支持4/5G互操作流程中的I-SMF插入。
  本节介绍I-SMF插入的判断、I-SMF插入（I-SMF不变）且I-UPF无需重选过程新增的消息。
  I-SMF不变情况下，I-UPF变化的判断流程在 [基于N26接口的EPS到5GS多切片时的重选（I-SMF不变，I-UPF变化的判断）](基于N26接口的EPS到5GS多切片时的重选（I-SMF不变，I-UPF变化的判断）_01755474.md#ZH-CN_CONCEPT_0000001101755474) 章节介绍。
  I-SMF变化的判断， I-SMF变化伴随着I-UPF变化的流程在 [基于N26接口的EPS到5GS多切片时的重选（I-SMF变化的判断，伴随I-UPF变化）](基于N26接口的EPS到5GS多切片时的重选（I-SMF变化的判断，伴随I-UPF变化）_48595223.md#ZH-CN_CONCEPT_0000001148595223) 章节介绍。
- AMF支持配置互操作专用切片S-NSSAI发现I-SMF。

#### [信令流程](#ZH-CN_CONCEPT_0000001148395107)

UE从EPS覆盖区移动到5GS覆盖区，UE发起的移动注册更新流程将4G的传输通道切换到5G传输通道，期间进行I-SMF插入，且插入的I-SMF支持会话所需的切片，不需要进行I-SMF重选即插入的I-SMF不变。具体流程如 [图1](#ZH-CN_CONCEPT_0000001148395107__zh-cn_concept_0000001101577346_fig958471992219) 所示。

本流程相对于基于N26接口的EPS到5GS多切片时的重选（AMF重分配判断）流程，多了I-SMF插入流程和I-SMF不变判断流程。

**图1** 基于N26接口的EPS到5GS多切片时的重选（I-SMF插入判断，I-SMF不变）流程

<br>

![](基于N26接口的EPS到5GS多切片时的重选（I-SMF插入判断，I-SMF不变）_48395107.assets/zh-cn_image_0000001101193152_2.png)

1. UE触发重选流程和判断AMF是否要重分配流程消息同基于N26接口的EPS到5GS多切片时的重选（AMF重分配判断）步骤[1](基于N26接口的EPS到5GS多切片时的重选（AMF重分配判断）_01915294.md#ZH-CN_CONCEPT_0000001101915294__zh-cn_concept_0000001148017339_li53111560512)-[16](基于N26接口的EPS到5GS多切片时的重选（AMF重分配判断）_01915294.md#ZH-CN_CONCEPT_0000001101915294__zh-cn_concept_0000001148017339_li179837134185)。
2. 如果在步骤[1](#ZH-CN_CONCEPT_0000001148395107__zh-cn_concept_0000001101577346_li53111560512)中，AMF进行了重分配，则后续步骤使用目标AMF进行消息交互，如果未进行AMF重分配，则使用初始AMF进行消息交互。本图中以AMF进行了重分配为例。因此目标AMF根据切片信息（通过****ADD SMFSELPLCY****配置基于签约数据选择还是基于配置选择的切片 ）、用户位置判断是否需要插入I-SMF。
  图例中以配置了 **互操作专用切片S-NSSAI** 为例，标识为 **配置的S-NSSAI** 。
3. 判断需要插入I-SMF，则使用TAI和**配置的S-NSSAI**向NRF查询并选择一个I-SMF。目标AMF发送Nsmf_PDUSession_CreateSMContext Request携带该**配置的S-NSSAI**给I-SMF。
4. I-SMF根据UE位置、DNN、S-NSSAI等信息选择I-UPF。I-SMF与I-UPF建立N4会话，请求分配I-UPF左侧N3端点和右侧N9端点。通过N4 Session建立流程完成用户的会话偶连建立。
5. I-SMF发送Nsmf_PDUSession_Create Request消息携带**配置的S-NSSAI**给锚点SMF+PGW-C，获取位置信息。
6. 锚点SMF+PGW-C向锚点UPF+PGW-U发送PFCP Session Modification Request消息携带N9接口CN隧道信息。
7. 锚点UPF+PGW-U回复PFCP Session Modification Response消息。
8. 锚点SMF+PGW-C将该会话对应的切片（**会话S-NSSAI**）过Nsmf_PDUSession_Create Response消息返回给I-SMF。
9. I-SMF回复Nsmf_PDUSession_CreateSMContext Response携带**会话S-NSSAI**给AMF。AMF需要将**会话S-NSSAI**保存到用户的上下文中。
10. 目标AMF比较步骤[3](#ZH-CN_CONCEPT_0000001148395107__zh-cn_concept_0000001101577346_li49761557203015)与响应步骤[8](#ZH-CN_CONCEPT_0000001148395107__zh-cn_concept_0000001101577346_li14515812504)中的S-NSSAI是否一致。
    - 如果**互操作专用切片S-NSSAI**和**会话S-NSSAI**一致，则I-SMF无需重选。
    - 如果**互操作专用切片S-NSSAI**和**会话S-NSSAI**不一致，则需要判断I-SMF是否支持**会话S-NSSAI**。若I-SMF支持**会话S-NSSAI**，且I-UPF不需要重选，则发送更新切片信息（步骤11），否则需要重选I-SMF。涉及I-SMF重选的步骤参见[基于N26接口的EPS到5GS多切片时的重选（I-SMF变化的判断，伴随I-UPF变化）](基于N26接口的EPS到5GS多切片时的重选（I-SMF变化的判断，伴随I-UPF变化）_48595223.md#ZH-CN_CONCEPT_0000001148595223)。
11. AMF给I-SMF发送Nsmf_PDUSession_UpdateSMContext_Request消息，将PDU**会话S-NSSAI**更新给I-SMF。
12. I-UPF重选判断，I-SMF根据S-NSSAI、用户位置判断初始I-UPF不需要重选。
13. 如果当前的重选过程不需要激活用户面，I-SMF发送PFCP Session Modification Request消息。
14. I-UPF应答PFCP Session Modification Response消息。
15. AMF收到I-SMF返回的Nsmf_PDUSession_UpdateSMContext Response消息。
16. 目标AMF发送Initial Context Setup Request（Registration accept）给NG-RAN，携带**会话S-NSSAI**。
17. NG-RAN响应Initial Context Setup Response。
18. UE响应Registration complete。
19. 如果当前的重选过程需要激活用户面，I-SMF给AMF发送Nsmf_PDUSession_UpdateSMContext_Response消息（携带N2 Resource Setup Request），响应步骤[11](#ZH-CN_CONCEPT_0000001148395107__zh-cn_concept_0000001101577346_li67041414114710)。
20. 目标AMF发送Initial Context Setup Request（N2 Resource Setup Request）给NG-RAN。
21. NG-RAN响应Initial Context Setup Response（N2 SM Resource Setup Ack）。
22. UE响应Registration complete。
23. AMF给I-SMF发送Nsmf_PDUSession_UpdateSMContext_Request消息，将N2Sminfo（PduSessionRscSetupRsp+Ran_N3）携带给I-SMF。
24. I-SMF给I-UPF发送PFCP Session Modification Request消息携带Ran_N3地址，“搭车”将Ran_N3携带过去即可。
25. I-UPF应答PFCP Session Modification Response消息。
26. AMF收到I-SMF返回的Nsmf_PDUSession_UpdateSMContext Response消息。
