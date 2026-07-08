# 删除APNNI转换配置(RMV IMSIAPNCONVERT)

- [命令功能](#ZH-CN_MMLREF_0000001126305470__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305470__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305470__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305470__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305470__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305470__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305470)

**适用网元：SGSN、MME**

该命令用于删除APN（Access Point Name）转换配置。如果用户激活请求消息中携带的APN和本配置命令“OLDAPN（请求APNNI）”匹配，则用户激活请求消息中携带的APN将被替换为“NEWAPN（转换APNNI）”后再进行签约数据匹配。

#### [注意事项](#ZH-CN_MMLREF_0000001126305470)

- 该命令执行后立即生效。
- 删除后影响签约数据匹配纠正功能。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305470)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305470)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305470)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定签约用户的范围。<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>- “IMSI_RANGE(指定IMSI范围)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>时，才需要配置。<br>取值范围：1~15位数字<br>默认值：无<br>说明：根据IMSI、<br>“请求APNNI”<br>映射唯一的<br>“转换APNNI”<br>。 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI，对该IMSI所在号段进行删除。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>取值范围：1~15位数字<br>默认值：无<br>说明：根据IMSI、<br>“请求APNNI”<br>映射唯一的<br>“转换APNNI”<br>。 |
| OLDAPN | 请求APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定匹配的激活请求消息中携带的APN NI。<br>取值范围：1~62<br>默认值：无<br>说明：- “请求APNNI”由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A~Z或a~z、数字0~9和中划线“-”。例如“HUAWEI.COM”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305470)

删除 “用户范围” 为 “指定IMSI前缀” ， “IMSI前缀” 为 “123007551111111” ，且 “请求APNNI” 为 “WCDMA” 的APNNI转换记录：

RMV IMSIAPNCONVERT: SUBRANGE=IMSI_PREFIX, IMSIPRE="123007551111111", OLDAPN="WCDMA";
