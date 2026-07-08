# 基于N26接口的EPS到5GS多切片时的重选（I-SMF不变，I-UPF变化的判断）

- [业务场景](#ZH-CN_CONCEPT_0000001101755474__1.3.1.1)
- [信令流程](#ZH-CN_CONCEPT_0000001101755474__1.3.2.1)

#### [业务场景](#ZH-CN_CONCEPT_0000001101755474)

多切片场景下，当UE在EPC中处于ECM-IDLE状态，UE从EPS覆盖区移动到5GS覆盖区，UE会尝试选择更优的5G网络，进行移动性注册更新流程。

当UE新所在区域超出了原来SMF的服务范围，AMF判断需要插入I-SMF，插入I-SMF后，判断插入的初始I-SMF能够支持会话需要的切片，不需要进行I-SMF的重选，但是I-SMF不变的情况下，I-UPF可能涉及变化，需要根据切片ID和TAI向NRF查询新的I-UPF，获取能够为当前服务区域提供服务的I-UPF，以保证用户会话业务的连续性。

为支持以上场景，核心网做如下相关操作：

- 支持4/5G互操作流程中的I-UPF变化的判断。

#### [信令流程](#ZH-CN_CONCEPT_0000001101755474)

UE从EPS覆盖区移动到5GS覆盖区，UE发起的移动注册更新流程将4G的传输通道切换到5G传输通道，期间进行I-SMF插入，且插入的I-SMF支持会话所需的切片，不需要进行I-SMF重选即插入的I-SMF不变，但是I-SMF不变时，I-UPF可能变化。具体流程如 [图1](基于N26接口的EPS到5GS多切片时的重选（I-SMF插入判断，I-SMF不变）_48395107.md#ZH-CN_CONCEPT_0000001148395107__zh-cn_concept_0000001101577346_fig958471992219) 所示。

本流程相对于基于N26接口的EPS到5GS多切片时的重选（I-SMF插入判断，I-SMF不变）流程，多了I-UPF变化判断流程。

**图1** 基于N26接口的EPS到5GS多切片时的重选（I-SMF不变，I-UPF变化的判断）流程

<br>

![](基于N26接口的EPS到5GS多切片时的重选（I-SMF不变，I-UPF变化的判断）_01755474.assets/zh-cn_image_0000001148375699_2.png)

1. UE触发重选流程，判断AMF是否要重分配，判断I-SMF是否需要插入，插入后I-SMF是否重选的流程消息同[基于N26接口的EPS到5GS多切片时的重选（I-SMF插入判断，I-SMF不变）](基于N26接口的EPS到5GS多切片时的重选（I-SMF插入判断，I-SMF不变）_48395107.md#ZH-CN_CONCEPT_0000001148395107)步骤[1](基于N26接口的EPS到5GS多切片时的重选（I-SMF插入判断，I-SMF不变）_48395107.md#ZH-CN_CONCEPT_0000001148395107__zh-cn_concept_0000001101577346_li53111560512)-[10](基于N26接口的EPS到5GS多切片时的重选（I-SMF插入判断，I-SMF不变）_48395107.md#ZH-CN_CONCEPT_0000001148395107__zh-cn_concept_0000001101577346_li558521885612)。
2. 如果在步骤[1](基于N26接口的EPS到5GS多切片时的重选（I-SMF插入判断，I-SMF不变）_48395107.md#ZH-CN_CONCEPT_0000001148395107__zh-cn_concept_0000001101577346_li53111560512)中，AMF进行了重分配，则后续步骤使用目标AMF进行消息交互，如果未进行AMF重分配，则使用初始AMF进行消息交互。本图中以AMF进行了重分配为例。
  I-SMF插入后不涉及重选，因此只有一个初始I-SMF。
  目标AMF给初始I-SMF发送Nsmf_PDUSession_UpdateSMContext_Request消息，将PDU **会话S-NSSAI** 携带给I-SMF。
3. I-SMF根据S-NSSAI、用户位置判断初始I-UPF需要重选，并选择一个目标I-UPF。
4. 通过N4 Session建立流程完成用户的会话偶连建立，携带**会话S-NSSAI**，请求分配I-UPF左侧N3端点和右侧N9端点，建立N4会话。
5. I-SMF向锚点SMF+PGW-C发送Nsmf_PDUSession_Update Request消息，通知锚点SMF更新PDU会话，更新I-SMF的CN Tunnel Info信息。
6. I-SMF和I-UPF进行N4 Session Modification（PFCP Session Modification Request/Response），修改N9接口CN隧道信息。
7. 锚点SMF+PGW-C回复I-SMF Nsmf_PDUSession_Update Response消息。
8. 如果当前的重选过程不需要激活用户面，则AMF收到I-SMF返回的Nsmf_PDUSession_UpdateSMContext Response消息。
9. 目标AMF发送Initial Context Setup Request（Registration accept）给NG-RAN，携带会话S-NSSAI。
10. NG-RAN响应Initial Context Setup Response。
11. UE响应Registration complete。
12. 如果注册更新流程需要激活用户面，I-SMF给AMF发送Nsmf_PDUSession_UpdateSMContext_Response消息（携带N2 Resource Setup Request），响应步骤[2](#ZH-CN_CONCEPT_0000001101755474__zh-cn_concept_0000001101617354_li10452183812394)。
13. 目标AMF发送Initial Context Setup Request（N2 Resource Setup Request）给NG-RAN。
14. NG-RAN响应Initial Context Setup Response（N2 SM Resource Setup Ack）。
15. UE响应Registration complete。
16. AMF给I-SMF发送Nsmf_PDUSession_UpdateSMContext_Request消息，将N2Sminfo（PduSessionRscSetupRsp+Ran_N3）携带给I-SMF。
17. I-SMF给目标I-UPF发送PFCP Session Modification Request消息携带Ran_N3地址，“搭车”将Ran_N3携带过去即可。
18. 目标I-UPF应答PFCP Session Modification Response消息。
19. AMF收到I-SMF返回的Nsmf_PDUSession_UpdateSMContext Response消息。
20. I-SMF向初始I-UPF发送PFCP Session Deletion Request(N4 Session Deletion Request)。初始I-UPF收到请求消息后将丢弃与该PDU会话相关的数据包，并释放与N4会话相关的所有隧道资源和上下文。
21. 初始I-UPF向I-SMF发送PFCPSessionDeletion Response(N4 Session Deletion Response)。
