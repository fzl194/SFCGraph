# 设置Sdup消息重传参数(SET SDAPRETRSMT)

- [命令功能](#ZH-CN_MMLREF_0000001126307104__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126307104__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126307104__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126307104__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126307104__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126307104__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126307104)

**适用网元：MME**

本命令用于控制Sdup接口的消息传输可靠性管理的参数。

#### [注意事项](#ZH-CN_MMLREF_0000001126307104)

- 该命令执行后立即生效。
- 此命令最大记录数为4。
- 恢复管理类消息的T-Response和N-Request数值配置，需要结合对应的端到端业务流程的时间决定。
- 链路管理类消息的T-Response和N-Request数值配置，（T-Response*N-Request）的结果应小于“Sdup接口探测间隔时长”，此参数见[**SET SDAPINTF**](../Sdup接口参数管理/设置Sdup接口参数(SET SDAPINTF)_26147292.md)。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126307104)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126307104)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126307104)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SMSGCLS | Sdup接口消息分类 | 可选必选说明：必选参数<br>参数含义：本参数用于选择Sdup接口消息分类。<br>数据来源：本端规划<br>取值范围：<br>- “LNKM(链路管理类消息)”，包括“SDAP Echo Request”。<br>- “DUPM(备份管理类消息)”，包括“Create User Information Request”、“Update User Information Request”、“Delete User Information Request”、“Create Subscription Information Request”、“Update Subscription Information Request”、“Delete Subscription Information Request”。<br>- “RESM(恢复管理类消息)”，包括“Restore User Information Request”、“IDR Information Inquiry Request”、“Paging Information Inquiry Request”、“Subscription Data Inquiry Request”。<br>- “OTHERS(其他消息)”，包括“Restart Notification”。<br>系统初始设置值：无 |
| TRSP | T-RESPONSE | 可选必选说明：可选参数<br>参数含义：该参数用于指定等待消息响应的时长。如果发送的请求消息在“T-RESPONSE”的时间内未收到响应，并且发送次数小于“N-REQUEST”，则重新发送该请求消息。<br>数据来源：本端规划<br>取值范围：1s~10s<br>系统初始设置值：见“说明”<br>说明：T-RESPONSE的初始值：<br>- 链路管理类消息：5<br>- 备份管理类消息：5<br>- 恢复管理类消息：1<br>- 其他消息：5 |
| NREQ | N-REQUEST | 可选必选说明：可选参数<br>参数含义：该参数用于指定请求消息的最大发送次数。<br>数据来源：本端规划<br>取值范围：1~5<br>系统初始设置值：见“说明”<br>说明：T-RESPONSE的初始值：<br>- 链路管理类消息：4<br>- 备份管理类消息：4<br>- 恢复管理类消息：1<br>- 其他消息：4 |

#### [使用实例](#ZH-CN_MMLREF_0000001126307104)

当TRSP=1, NREQ=1，设置Sdup接口的消息传输可靠性管理的参数：

SET SDAPRETRSMT: SMSGCLS=RESM, TRSP=1, NREQ=1;
