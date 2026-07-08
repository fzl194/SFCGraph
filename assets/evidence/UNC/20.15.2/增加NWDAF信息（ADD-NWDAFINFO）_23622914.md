# 增加NWDAF信息（ADD NWDAFINFO）

- [命令功能](#ZH-CN_MMLREF_0000001823622914__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001823622914__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001823622914__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001823622914__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001823622914)

该命令用于配置NWDAF的实例信息，如NWDAF的名称。NWDAF实例信息属于基础配置。

## [注意事项](#ZH-CN_MMLREF_0000001823622914)

- 该命令执行后立即生效。

- 最多可输入1条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0000001823622914)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001823622914)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCENAME | NWDAF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于唯一指定某一个NWDAF实例。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。本参数的构成字符只能是字母A~Z或a~z、数字0~9、下划线“_”和中划线“-”，例如，NWDAF_Instance_0。<br>默认值：无<br>配置原则：<br>本参数来源于ADD NFUUID命令中的“NF实例名称”参数。 |
| NWDAFEVENTS | NWDAF数据分析事件 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NWDAF支持的分析事件类型。<br>数据来源：本端规划<br>取值范围：<br>- QOS_ANALYSIS（QOS分析）<br>- QOS_EXP_ANALYSIS（体验感知信息分析）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001823622914)

增加NWDAF信息，NWDAF实例名称为nwdaf_Instance_1，支持的NWADFEVENTS类型为QOS_ANALYSIS。

```
ADD NWDAFINFO: INSTANCENAME="nwdaf_Instance_1", NWDAFEVENTS=QOS_ANALYSIS-1&QOS_EXP_ANALYSIS-0;
```
