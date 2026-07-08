# 修改APNNI转换配置(MOD IMSIAPNCONVERT)

- [命令功能](#ZH-CN_MMLREF_0000001172345257__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172345257__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172345257__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172345257__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172345257__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172345257__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172345257)

**适用网元：SGSN、MME**

该命令用于修改APN（Access Point Name）转换配置。如果用户激活请求消息中携带的APN和本配置命令“OLDAPN（请求APNNI）”匹配，则用户激活请求消息中携带的APN将被替换为“NEWAPN（转换APNNI）”后再进行签约数据匹配。

#### [注意事项](#ZH-CN_MMLREF_0000001172345257)

- 该命令执行后立即生效。
- 此配置涉及请求信息纠正功能特性（特性编号：WSFD-106004，License部件编码：LKV2RINCOR02），执行命令请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172345257)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172345257)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172345257)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定签约用户的范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>- “IMSI_RANGE(指定IMSI范围)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1~15位数字<br>默认值：无<br>说明：根据<br>“IMSI前缀”<br>、<br>“请求APNNI”<br>映射唯一的<br>“转换APNNI”<br>。 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI，对该IMSI所在的号段进行修改。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1~15位数字<br>默认值：无<br>说明：根据<br>“IMSI”<br>、<br>“请求APNNI”<br>映射唯一的<br>“转换APNNI”<br>。 |
| OLDAPN | 请求APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定匹配的激活请求消息中携带的APN NI。<br>数据来源：整网规划<br>取值范围：1~62<br>默认值：无<br>说明：- “请求APNNI”由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A~Z或a~z、数字0~9和中划线“-”。例如“HUAWEI.COM”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。 |
| APNCONVERT | APN转换 | 可选必选说明：可选参数<br>参数含义：该参数用于设置APN转换规则。<br>数据来源：整网规划<br>取值范围：<br>- “WILDCARD_SUBSCRIPTION_USER(对签约了野卡APN的用户启用)”：表示对签约了野卡APN的用户启用。<br>- “NO_WILDCARD_SUBSCRIPTION_USER(对未签约野卡APN的用户启用)”：表示对未签约野卡APN的用户启用。<br>- “ALL_USER(对号段内的用户都启用)”：表示对号段内的用户都启用。<br>默认值：无 |
| NEWAPN | 转换APNNI | 可选必选说明：可选参数<br>参数含义：该参数用于指定进行转换后的APNNI。<br>数据来源：整网规划<br>取值范围：1~62<br>默认值：无<br>说明：- “转换APNNI”由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。例如“HUAWEI.COM”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于增加配置命令的描述信息。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172345257)

修改 “用户范围” 为 “指定IMSI前缀” ， “IMSI前缀” 为 “123007551111111” ， “请求APNNI” 为 “WCDMA” ，且 “转换APNNI” 为 “HUAWEI1.COM” 的APNNI转换记录。

MOD IMSIAPNCONVERT: SUBRANGE=IMSI_PREFIX, IMSIPRE="123007551111111", OLDAPN="WCDMA", NEWAPN="HUAWEI1.COM";
