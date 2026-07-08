# 删除IMSI对应的HLR/HSS接口(RMV IMSIHLRHSS)

- [命令功能](#ZH-CN_MMLREF_0000001172225431__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225431__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225431__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225431__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225431__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225431__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225431)

**适用网元：SGSN、MME**

此命令用于删除IMSI对应的HLR/HSS接口。

#### [注意事项](#ZH-CN_MMLREF_0000001172225431)

- 此命令执行后立即生效。
- 此命令执行后可能会导致对应IMSI范围的用户无法附着，已经附着的用户不会受影响/被分离。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225431)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225431)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225431)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIRANGE | IMSI范围 | 可选必选说明：必选参数<br>参数含义：待删除的IMSI范围信息。<br>取值范围：<br>- “ALL IMSI(所有IMSI)”：表示该指定IMSI范围为所有IMSI。<br>- “SPECIAL IMSI(指定IMSI)”：表示该指定IMSI范围为指定IMSI。<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：待删除的IMSI前缀。<br>前提条件：当<br>“IMSIRANGE(IMSI范围)”<br>设置为<br>“SPECIAL IMSI(指定IMSI)”<br>时生效。<br>取值范围：5～15位数字<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225431)

删除一条IMSI范围为SPECIAL_IMSI，IMSI前缀为123456的记录：

RMV IMSIHLRHSS: IMSIRANGE=SPECIAL_IMSI, IMSIPRE="123456";
