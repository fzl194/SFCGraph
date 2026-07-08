# Service Request流程

- [流程示意](#ZH-CN_TOPIC_0000001589144933__1.3.3.1)
- [信令流程](#ZH-CN_TOPIC_0000001589144933__1.3.4.1)
- [性能指标说明](#ZH-CN_TOPIC_0000001589144933__1.3.5.1)

Service Request流程分为UE侧触发和网络侧触发。由于网络侧触发的Service Request流程不涉及RedCap的变更，因此本章节以UE侧触发，且AMF，SMF不变的Service Request为例。

空闲态用户发起SR流程，gNodeB给AMF发送的INITIAL UE MESSAGE中携带RedCap Indication。

#### [流程示意](#ZH-CN_TOPIC_0000001589144933)

**图1** Service Request流程示意图

<br>

![](Service Request流程_89144933.assets/zh-cn_image_0000001637743849.png)

#### [信令流程](#ZH-CN_TOPIC_0000001589144933)

**图2** RedCap用户Service Request流程图

<br>

![](Service Request流程_89144933.assets/zh-cn_image_0000001637863889.png)

该流程相较于Service Request接入流程，主要差异点集中在如下步骤，其余步骤请参见 **[Service Request（UE发起）](../../../../../../../快速入门/协议与流程/5G Core信令分析/业务流程/连接管理/Service Request（UE发起）_47633569.md)** 流程。

1. **Step 1&Step 2**：UE发送**[Service request](../../../../../../../快速入门/协议与流程/5G Core信令分析/消息及信元/非服务化接口协议/N1接口/相关消息解释/Service request_76783789.md)**给(R)AN，(R)AN通过N2 Message消息（INITIAL UE MESSAGE携带RedCap Indication信元）将Service Request信息转发给AMF。AMF收到此信元以后，与本地用户上下文中的RedCap指示进行对比判断是否发生RatType变更，具体判断逻辑请见[AMF判断RatType变更逻辑](AMF判断RatType变更逻辑_38240620.md)。
  为实现此流程，AMF上的RedCap功能命令 **SET AMFREDCAPFUNC** 的参数 **REDCAPSW** 需要打开。

  > **说明**
  > AMF可以用 **SET AMFREDCAPFUNC** 的参数 **NTYSMFPLCY** 配置向空闲态PDU会话关联的SMF通知RatType的策略。
2. **Step 4：**若发生RatType变更，AMF向SMF发送在Nsmf_PDUSession_UpdateSMContext Request消息携带最新的RatType通知SMF。AMF判断是否发生RatType变更逻辑请见[AMF判断RatType变更逻辑](AMF判断RatType变更逻辑_38240620.md)。
  为实现此流程，SMF上的SMF上RedCap开关 **SET SMFFUNC** 的 **REDCAPSW** 参数需要打开；AMF上的RedCap功能命令 **SET AMFREDCAPFUNC** 的参数 **RATCMPTSW** 需要取值为"SMF"，参数 **NTYSMFPLCY** 需取值为"IMMEDIATELY_NOTIFY_ON_CHANGE"。
3. **Step 5**：若发生RatType变更，SMF向PCF发送.Npcf_SMPolicyControlAPI_SmPolicyControlUpdate Request消息携带最新的RatType通知PCF。
  为实现此流程，SMF上的 **SET REDCAPRATVALUE** 的 **PCF** 参数需配置为“NR_REDCAP”。
4. **Step 8**：若发生RatType变更，SMF通过消息PFCP Session Modification Request携带最新的RatType通知PSA用户接入类型。
  为实现此流程，需要配置 **SET SMFFUNC** 的 **REDCAPSW** 参数为打开， ****SET REDCAPRATVALUE**** 的 **UPF** 参数需配置为“NR_REDCAP”。
5. **Step 10**：若发生RatType变更，SMF通过消息PFCP Session Modification Request携带最新的RatType通知新I-UPF用户接入类型。
  为实现此流程，需要配置 **SET SMFFUNC** 的 **REDCAPSW** 参数为打开， **SET REDCAPRATVALUE** 的 **UPF** 参数需配置为“NR_REDCAP”。

#### [性能指标说明](#ZH-CN_TOPIC_0000001589144933)

*表1 AMF性能指标*

| 测量网元 | 测量集 | 测量单元 | 测量对象 | 测量指标 | 测量点触发消息 | 流程图打点 |
| --- | --- | --- | --- | --- | --- | --- |
| AMF | AMF 移动性管理 | AMF RedCap用户初业务流程 | 整机 | 1929452360 RedCap用户N2模式业务请求尝试次数 | Service Request | P2b |
