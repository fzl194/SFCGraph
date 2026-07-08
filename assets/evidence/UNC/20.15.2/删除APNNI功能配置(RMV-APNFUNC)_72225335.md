# 删除APNNI功能配置(RMV APNFUNC)

- [命令功能](#ZH-CN_MMLREF_0000001172225335__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225335__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225335__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225335__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225335__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225335__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225335)

**适用网元：SGSN**

该命令用于删除APNNI功能。

#### [注意事项](#ZH-CN_MMLREF_0000001172225335)

无。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225335)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225335)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225335)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN网络标识。<br>数据来源：整网规划<br>取值范围：长度不超过62的字符串<br>默认值： 无<br>配置原则：<br>- APN网络标识由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。<br>说明：- APN网络标识不区分大小写。<br>- APNNI在APN中所处的位置，例如：huawei1.com.mnc.mcc.gprs，其中NI= huawei1.com， OI= mnc.mcc.gprs。 |
| APNPURPOSE | APN用途 | 可选必选说明：必选参数<br>参数含义：该参数决定了该APNNI所属用户是VIP用户。<br>数据来源：整网规划<br>取值范围：<br>- “VIP(VIP用户)”:标识该APNNI所属用户为VIP用户。<br>默认值： 无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225335)

删除APNNI为"huawei1.com"的VIP用户：

RMV APNFUNC: APNNI="huawei1.com", APNPURPOSE=VIP;
