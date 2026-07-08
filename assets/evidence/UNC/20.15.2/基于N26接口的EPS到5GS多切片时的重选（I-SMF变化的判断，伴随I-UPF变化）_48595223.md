# 基于N26接口的EPS到5GS多切片时的重选（I-SMF变化的判断，伴随I-UPF变化）

- [业务场景](#ZH-CN_CONCEPT_0000001148595223__1.3.1.1)
- [信令流程](#ZH-CN_CONCEPT_0000001148595223__1.3.2.1)

#### [业务场景](#ZH-CN_CONCEPT_0000001148595223)

多切片场景下，当UE在EPC中处于ECM-IDLE状态，UE从EPS覆盖区移动到5GS覆盖区，UE会尝试选择更优的5G网络，进行移动性注册更新流程。

当UE新所在区域超出了原来SMF的服务范围，AMF判断需要插入I-SMF，插入I-SMF后，插入的初始I-SMF不支持会话需要的切片，需要进行I-SMF的重选，I-SMF变化肯定伴随着I-UPF变化。为支持以上场景，核心网做如下相关操作：

- 支持4/5G互操作流程中的I-SMF重选，并伴随I-UPF重选流程。

#### [信令流程](#ZH-CN_CONCEPT_0000001148595223)

UE从EPS覆盖区移动到5GS覆盖区，UE发起的移动注册更新流程将4G的传输通道切换到5G传输通道，期间进行I-SMF插入，且插入的I-SMF不支持会话所需的切片，需要进行I-SMF重选伴随I-UPF重选具体流程如 [图1](基于N26接口的EPS到5GS多切片时的重选（I-SMF插入判断，I-SMF不变）_48395107.md#ZH-CN_CONCEPT_0000001148395107__zh-cn_concept_0000001101577346_fig958471992219) 所示。

本流程相对于基于N26接口的EPS到5GS多切片时的重选（I-SMF插入判断，I-SMF不变）流程，多了I-SMF变化和I-UPF变化的流程。

**图1** 基于N26接口的EPS到5GS多切片时的重选（I-SMF变化，伴随I-UPF变化）流程

<br>

![](基于N26接口的EPS到5GS多切片时的重选（I-SMF变化的判断，伴随I-UPF变化）_48595223.assets/zh-cn_image_0000001148463391_2.png)

1. UE触发重选流程，判断AMF是否要重分配，判断I-SMF是否需要插入，插入后I-SMF是否重选的流程消息同[基于N26接口的EPS到5GS多切片时的重选（I-SMF插入判断，I-SMF不变）](基于N26接口的EPS到5GS多切片时的重选（I-SMF插入判断，I-SMF不变）_48395107.md#ZH-CN_CONCEPT_0000001148395107)步骤[1](基于N26接口的EPS到5GS多切片时的重选（I-SMF插入判断，I-SMF不变）_48395107.md#ZH-CN_CONCEPT_0000001148395107__zh-cn_concept_0000001101577346_li53111560512)-[9](基于N26接口的EPS到5GS多切片时的重选（I-SMF插入判断，I-SMF不变）_48395107.md#ZH-CN_CONCEPT_0000001148395107__zh-cn_concept_0000001101577346_li14515812504)。
2. 如果在步骤[1](基于N26接口的EPS到5GS多切片时的重选（I-SMF插入判断，I-SMF不变）_48395107.md#ZH-CN_CONCEPT_0000001148395107__zh-cn_concept_0000001101577346_li53111560512)中，AMF进行了重分配，则后续步骤使用目标AMF进行消息交互，如果未进行AMF重分配，则使用初始AMF进行消息交互。本图中以AMF进行了重分配为例。
  目标AMF比较 **配置的S-NSSAI** 和 **会话S-NSSAI** 不一致，判断I-SMF是否支持 **会话S-NSSAI** 。I-SMF不支持 **会话S-NSSAI** ，需要通过TAI和会话切片信息重选I-SMF。
3. 目标AMF发送Nsmf_PDUSession_CreateSMContext Request携带**会话S-NSSAI**给目标I-SMF。
4. 目标I-SMF向初始I-SMF发送Nsmf_PDUSession_Context Request请求会话上下文。
5. 初始I-SMF向目标I-SMF发送Nsmf_PDUSession_Context Response。
6. I-SMF的变化肯定伴随着I-UPF的变化。目标I-SMF根据S-NSSAI、用户位置重选I-UPF。
7. 目标I-SMF和目标I-UPF进行N4 Session Establishment（PFCP Session Establishment Request/Response），请求分配I-UPF左侧N3端点和右侧N9端点，建立N4会话。
8. 目标I-SMF向锚点SMF+PGW-C发送Nsmf_PDUSession_Update Request消息。来通知锚点SMF更新PDU会话，更新I-SMF的CN Tunnel Info信息。
9. 锚点SMF+PGW-C和锚点UPF+PGW-U进行N4 Session Modification（PFCP Session Modification Request/Response），修改N9接口CN隧道信息。
10. 锚点SMF+PGW-C向目标I-SMF响应Nsmf_PDUSession_Update Response消息。
11. 目标I-SMF向目标AMF响应Nsmf_PDUSession_CreateSMContext Response。
12. 目标AMF向初始I-SMF发送Nsmf_PDUSession_ReleaseSMContext消息。
13. 如果注册更新流程需要激活用户面，完成Ran_N3隧道地址交换，同[基于N26接口的EPS到5GS多切片时的重选（I-SMF不变，I-UPF变化的判断）](基于N26接口的EPS到5GS多切片时的重选（I-SMF不变，I-UPF变化的判断）_01755474.md#ZH-CN_CONCEPT_0000001101755474)流程步骤[12](基于N26接口的EPS到5GS多切片时的重选（I-SMF不变，I-UPF变化的判断）_01755474.md#ZH-CN_CONCEPT_0000001101755474__zh-cn_concept_0000001101617354_li3577910102815)-[21](基于N26接口的EPS到5GS多切片时的重选（I-SMF不变，I-UPF变化的判断）_01755474.md#ZH-CN_CONCEPT_0000001101755474__zh-cn_concept_0000001101617354_li117533185344)。
