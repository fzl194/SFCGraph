# 删除APN优先级配置(RMV PDPFILTERAPN)

- [命令功能](#ZH-CN_MMLREF_0000001172345285__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172345285__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172345285__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172345285__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172345285__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172345285__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172345285)

**适用网元：SGSN**

该命令用于删除APN优先级配置。APN优先级可以用于在RAU或者RELOCATION流程中指示新侧保留PDP的顺序。高优先级APN对应的PDP会优先保留，低优先级APN对应的PDP会在切换后主动删掉。

#### [注意事项](#ZH-CN_MMLREF_0000001172345285)

- 该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172345285)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172345285)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172345285)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>该参数用于指定PDP过滤功能适用的用户范围。参考<br>[**SET PDPFILTERCTL**](设置PDP过滤功能参数(SET PDPFILTERCTL)_26145688.md)<br>命令。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “LOCAL_USER(本网用户)”<br>- “FOREIGN_USER(外网用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件: 该参数在“用户范围”参数配置为“IMSI_PREFIX(指定IMSI前缀)”时生效。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字字符串。<br>默认值：无 |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定APNNI名称。<br>数据来源：整网规划<br>取值范围：1～62位字符串。<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172345285)

删除一个APN优先级记录，“用户范围”为“ALL_USER(所有用户)”，“APNNI”为“huawei1.com”：

RMV PDPFILTERAPN: SUBRANGE=ALL_USER, APNNI="huawei1.com";
