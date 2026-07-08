# 删除Tm接口指定消息T3N3参数(RMV TMT3N3)

- [命令功能](#ZH-CN_CONCEPT_0000001289014960__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001289014960__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0000001289014960__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0000001289014960__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0000001289014960__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0000001289014960__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001289014960)

**适用网元：MME**

本命令用于删除指定Tm接口消息T3N3参数。不能用于删除TM路径的T3和N3系统初始设置值，初始设置值请在 **ADD TMT3N3** 命令查看。

#### [注意事项](#ZH-CN_CONCEPT_0000001289014960)

- 该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_CONCEPT_0000001289014960)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0000001289014960)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001289014960)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TMSPECIALMSGCFG | 指定Tm接口消息 | 可选必选说明：必选参数<br>参数含义：指定具体的Tm接口消息设置T3N3参数。<br>数据来源：全网规划<br>取值范围：<br>- “SPECIAL_TM_MSG（指定Tm接口消息）”<br>默认值 ：无 |
| TMMSG | Tm接口消息 | 可选必选说明：条件必选参数<br>前提条件：该参数在“指定Tm接口消息”参数配置为“SPECIAL_TM_MSG”后生效。<br>参数含义：Tm接口消息列表。<br>数据来源：全网规划<br>取值范围：<br>- “ECHO（Echo Request）”<br>- “STRT_ENB_TA_INFO_UPDATE_REQ（Start eNB TA Information Update Request）”<br>- “UPDATE_ENB_TA_INFO_REQ（Update eNodeB TA Information Request）”<br>- “TRK_GP_UL_S1_DT_NTF（Trunk Group UL S1 Direct Transfer Notification）”<br>- “TRK_USR_ATT_REQ（Trunk User Attach Request）”<br>- “TRK_USR_DET_REQ（Trunk User Detach Request）”<br>- “TRK_USR_HO_REQ（Trunk User Handover Request）”<br>- “TRK_USR_HO_NTF（Trunk User Handover Notification）”<br>- “TRK_USR_TAU_REQ（Trunk User TAU Request）”<br>- “TRK_USR_SR_REQ（Trunk User Service Request）”<br>- “NODE_ST_NTF（NE Status Notification）”<br>默认值 ：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001289014960)

删除Tm接口Trunk User Attach Request消息T3N3参数：

```
RMV TMT3N3: TMSPECIALMSGCFG=SPECIAL_TM_MSG, TMMSG=TRK_USR_ATT_REQ;
```
