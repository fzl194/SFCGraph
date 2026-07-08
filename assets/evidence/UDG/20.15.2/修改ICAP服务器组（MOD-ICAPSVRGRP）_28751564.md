# 修改ICAP服务器组（MOD ICAPSVRGRP）

- [命令功能](#ZH-CN_CONCEPT_0000203228751564__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000203228751564__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000203228751564__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000203228751564__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000203228751564__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000203228751564)

**适用NF：PGW-U、UPF**

该命令用于修改一个ICAP Server Group实例。

#### [注意事项](#ZH-CN_CONCEPT_0000203228751564)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000203228751564)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000203228751564)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ICAPSVRGRPNAME | ICAP服务器组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICAP Server Group的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。不区分大小写。<br>默认值：无<br>配置原则：无 |
| ICAPSERVERTYPE | ICAP服务器类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICAP Server服务器类型。<br>数据来源：本端规划<br>取值范围：<br>- URL_FILTERING：支持URL过滤的ICAP服务器。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000203228751564)

修改指定ICAP Server Group名为isg2的ICAP Server Group实例：

```
MOD ICAPSVRGRP: ICAPSVRGRPNAME="isg2",ICAPSERVERTYPE=URL_FILTERING;
```
