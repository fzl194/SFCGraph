# 修改IMSI Direct Tunnel配置(MOD IMSIDT)

- [命令功能](#ZH-CN_MMLREF_0000001172225727__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225727__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225727__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225727__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225727__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225727__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225727)

**适用网元：SGSN**

此命令用于修改IMSI DT属性信息表中的某个IMSI的DT属性信息。

#### [注意事项](#ZH-CN_MMLREF_0000001172225727)

- 此命令执行后立即生效。
- 用户要使用DT功能还需满足RNC、GGSN和APNNI支持DT功能。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225727)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225727)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225727)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定签约用户的范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>- “IMSI_RANGE（指定IMSI范围）”<br>默认值：无<br>配置原则：使用时首先按照用户的IMSI在<br>“IMSI_PREFIX（指定IMSI前缀）”<br>或<br>“IMSI_RANGE（指定IMSI范围）”<br>进行查询，如果查询成功则使用该记录对应的配置；如果查询失败，则查询<br>“所有用户”<br>对应的配置记录，如果查询成功则使用<br>“所有用户”<br>的配置，如果查询还失败，则默认支持DT。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：当<br>“用户范围”<br>为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：1～15位十进制字符串<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI，对该IMSI所在号段进行修改。<br>前提条件：当<br>“用户范围”<br>为<br>“IMSI_RANGE（指定IMSI范围）”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：1～15位十进制字符串<br>默认值：无 |
| DT | 启用Direct Tunnel | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否启用基于IMSI的DT功能。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>配置原则：<br>- 取值为“NO(否)”时，表示不启用基于IMSI的DT功能。<br>- 取值为“YES(是)”时，表示启用基于IMSI的DT功能。<br>说明：- 当参数设置为“YES(是)”时，“支持Direct Tunnel功能”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-104506，License部件编码：LKV2DIRTUN02）。 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225727)

修改一条 “用户范围” 为 “指定IMSI前缀” ， “IMSI前缀” 为 “123456” ， “启用Direct Tunnel” 为 “YES” 的IMSI DT权限属性记录：

MOD IMSIDT: SUBRANGE=IMSI_PREFIX, IMSIPRE="123456", DT=YES;
