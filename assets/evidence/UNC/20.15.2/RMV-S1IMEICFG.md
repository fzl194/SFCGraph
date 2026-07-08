# 删除S1模式IMEI配置（RMV S1IMEICFG）

- [命令功能](#ZH-CN_MMLREF_0000001172345235__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172345235__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172345235__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172345235__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172345235__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172345235__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172345235)

**适用网元：MME**

该命令用于删除EUTRAN指定号段用户的获取和检查IMEI的策略。

#### [注意事项](#ZH-CN_MMLREF_0000001172345235)

- 该命令执行后立即生效。
- 只能删除指定号段用户的IMEI配置，而不能删除默认的IMEI配置。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172345235)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172345235)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172345235)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定签约用户的范围。<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>- “IMSI_RANGE（指定IMSI范围）”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：只有<br>“用户范围”<br>为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时，该参数才有效。<br>取值范围：1～15位十进制数字<br>默认值：无<br>说明：需要修改或者删除已通过<br>[**ADD S1IMEICFG**](增加S1模式IMEI配置(ADD S1IMEICFG)_26305448.md)<br>命令配置的用户范围为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>、IMSI前缀为<br>“ALL_USER”<br>的记录时，需要执行<br>**MOD/RMV S1IMEICFG**<br>命令，用户范围设置为<br>“ALL_USER（所有用户）”<br>。 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI，对该IMSI所在号段进行删除。<br>前提条件：只有<br>“用户范围”<br>为<br>“IMSI_RANGE（指定IMSI范围）”<br>时，该参数才有效。<br>取值范围：1～15位十进制数字<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172345235)

删除IMSI前缀为“123456”的EUTRAN用户的IMEI配置：

RMV S1IMEICFG:SUBRANGE=IMSI_PREFIX, IMSIPRE="123456";
