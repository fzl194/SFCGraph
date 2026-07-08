# 修改Tm接口消息T3N3参数(MOD TMT3N3)

- [命令功能](#ZH-CN_CONCEPT_0000001289174552__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001289174552__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0000001289174552__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0000001289174552__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0000001289174552__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0000001289174552__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001289174552)

**适用网元：MME**

本命令用于修改Tm接口消息T3N3参数。

#### [注意事项](#ZH-CN_CONCEPT_0000001289174552)

- 该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_CONCEPT_0000001289174552)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0000001289174552)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001289174552)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TMMSGCFGMODE | Tm接口消息配置模式 | 可选必选说明：必选参数<br>参数含义：本参数用于选择Tm接口消息配置方式。<br>数据来源：全网规划<br>取值范围：<br>- “TMMSG_ALL（Tm接口消息全集）”<br>- “SPECIAL_TM_MSG（指定Tm接口消息）”<br>默认值 ：无 |
| TMMSG | Tm接口消息 | 可选必选说明：条件必选参数<br>前提条件：该参数在“指定Tm接口消息”参数配置为“SPECIAL_TM_MSG”后生效。<br>参数含义：Tm接口消息列表。<br>数据来源：全网规划<br>取值范围：<br>- “ECHO（Echo Request）”<br>- “STRT_ENB_TA_INFO_UPDATE_REQ（Start eNB TA Information Update Request）”<br>- “UPDATE_ENB_TA_INFO_REQ（Update eNodeB TA Information Request）”<br>- “TRK_GP_UL_S1_DT_NTF（Trunk Group UL S1 Direct Transfer Notification）”<br>- “TRK_USR_ATT_REQ（Trunk User Attach Request）”<br>- “TRK_USR_DET_REQ（Trunk User Detach Request）”<br>- “TRK_USR_HO_REQ（Trunk User Handover Request）”<br>- “TRK_USR_HO_NTF（Trunk User Handover Notification）”<br>- “TRK_USR_TAU_REQ（Trunk User TAU Request）”<br>- “TRK_USR_SR_REQ（Trunk User Service Request）”<br>- “NODE_ST_NTF（NE Status Notification）”<br>默认值 ：无 |
| TRSP | T-RESPONSE(s) | 可选必选说明：可选参数<br>参数含义：该参数用于指定等待一条T3请求消息的响应消息的最大时长。如果请求消息没有在“TRSP”内收到响应，并且发送次数小于“NREQ”，则重新发送该请求消息。<br>数据来源：全网规划<br>取值范围：1~20<br>默认值 ：无 |
| NREQ | N-REQUEST(times) | 可选必选说明：可选参数<br>参数含义：该参数用于指定Tm接口发送一条请求消息的最大尝试次数。<br>数据来源：本端规划<br>取值范围：1~5<br>默认值 ：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001289174552)

修改Tm消息类型为用户会话类消息，在7s内，MME发送一条请求消息的最大尝试数为2次：

```
MOD TMT3N3: TMMSGCFGMODE=TMMSG_ALL, TRSP=7, NREQ=2;
```
