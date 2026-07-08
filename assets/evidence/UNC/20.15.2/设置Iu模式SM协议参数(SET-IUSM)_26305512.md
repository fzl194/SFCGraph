# 设置Iu模式SM协议参数(SET IUSM)

- [命令功能](#ZH-CN_MMLREF_0000001126305512__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305512__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305512__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305512__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305512__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305512__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305512)

![](设置Iu模式SM协议参数(SET IUSM)_26305512.assets/notice_3.0-zh-cn_2.png)

修改IUSM协议配置信息，可能导致某些类型的会话无法激活成功。

**适用网元：SGSN**

该命令用于设置IUSM协议配置信息，定义了激活流程相关定时器的值。

#### [注意事项](#ZH-CN_MMLREF_0000001126305512)

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 修改IUSM协议配置信息，可能导致某些类型的会话无法激活成功。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305512)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305512)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305512)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| T3385 | T3385（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定网络侧激活定时器时长。在网络侧向MS发送一条ACTIVATE PDP CONTEXT REQUEST消息时启动，网络侧收到ACTIVATE PDP CONTEXT ACCEPT/REJECT消息时终止，或者在网络侧向MS发送一条REQUEST SECONDARY PDP CONTEXT ACTIVATION消息时启动，网络侧收到REQUEST SECONDARY PDP CONTEXT ACTIVATION REJECT/ACTIVATE PDP CONTEXT REQUEST消息终止，超时后，将会重发ACTIVATE PDP CONTEXT REQUEST/REQUEST REQUEST SECONDARY PDP CONTEXT ACTIVATION消息，重发次数由<br>“N3385(times)”<br>来控制。当达到最大重发次数，则流程失败。<br>数据来源：本端规划<br>取值范围：1s～86400s<br>系统初始设置值：8s |
| N3385 | N3385（times） | 可选必选说明：可选参数<br>参数含义：该参数用于指定重发ACTIVATE PDP CONTEXT REQUEST消息的次数。<br>数据来源：整网规划<br>取值范围：0times～5times<br>系统初始设置值：4times |
| T3386 | T3386（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定网络侧设置定时器时长。在网络侧向MS发送一条MODIFY PDP CONTEXT REQUEST消息时启动，当网络侧收到MODIFY PDP CONTEXT ACCEPT/REJECT消息时终止，终止后，将会根据接收到的消息不同来决定流程是成功还是失败。<br>数据来源：本端规划<br>取值范围：1s～86400s<br>系统初始设置值：8s |
| N3386 | N3386（times） | 可选必选说明：可选参数<br>参数含义：该参数用于指定重发MODIFY PDP CONTEXT REQUEST消息的次数。<br>数据来源：整网规划<br>取值范围：0times～5times<br>系统初始设置值：4times |
| T3395 | T3395（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定网络侧去激活定时器时长。在网络侧向MS发送一条DEACTIVATE PDP CONTEXT REQUEST消息时启动，当网络侧收到DEACTIVATE PDP CONTEXT ACCEPT/REJECT消息时终止，终止后，将会根据接收到的消息不同来决定流程是成功还是失败。<br>数据来源：本端规划<br>取值范围：1s～86400s<br>系统初始设置值：8s |
| N3395 | N3395（times） | 可选必选说明：可选参数<br>参数含义：该参数用于指定重发DEACTIVATE PDP CONTEXT REQUEST消息的次数。<br>数据来源：整网规划<br>取值范围：0times～5times<br>系统初始设置值：4times |

#### [使用实例](#ZH-CN_MMLREF_0000001126305512)

设置一条 “T3385(s)” 为 “10s” ， “T3386(s)” 为 “10s” 的3GSM协议配置记录：

SET IUSM: T3385=10, T3386=10;
