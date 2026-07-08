# 删除Gb模式接入限制参数(RMV GBARD)

- [命令功能](#ZH-CN_MMLREF_0000001172345071__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172345071__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172345071__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172345071__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172345071__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172345071__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172345071)

**适用网元：SGSN**

该命令用于删除Gb模式接入限制记录。

#### [注意事项](#ZH-CN_MMLREF_0000001172345071)

该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172345071)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172345071)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172345071)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：待删除记录的用户范围。<br>取值范围：<br>- “ALL_USER(所有用户)”：表示该指定用户范围为所有用户。<br>- “SPECIAL_IMSIPRE(指定IMSI前缀)”：表示该用户范围为指定IMSI前缀。<br>- “SPECIAL_IMSI_RANGE(指定IMSI范围)”：表示该用户范围为指定IMSI范围。<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的IMSI前缀的信息。使用时按照IMSI完全匹配进行查询。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>设置为<br>“SPECIAL_IMSIPRE(指定IMSI前缀)”<br>时生效。<br>取值范围：1～15位数字<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于删除指定IMSI所在号段的记录。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>设置为<br>“SPECIAL_IMSI_RANGE(指定IMSI范围)”<br>时生效。<br>取值范围：1～15位数字<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172345071)

1. 删除所有用户的接入限制记录：
  RMV GBARD: SUBRANGE=ALL_USER;
2. 删除IMSI前缀为123456的接入限制记录：
  RMV GBARD: SUBRANGE=SPECIAL_IMSIPRE, IMSIPRE="123456";
