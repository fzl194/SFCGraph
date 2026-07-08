# 设置主用PCRF（SET MASTERPCRF）

- [命令功能](#ZH-CN_CONCEPT_0209897094__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897094__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897094__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897094__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897094__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897094)

**适用NF：PGW-C、SMF**

此命令用于设置主用PCRF主机名。

#### [注意事项](#ZH-CN_CONCEPT_0209897094)

- 该命令执行后立即生效。
- 该命令最大记录数为100。
- 配置的PCRF必须已通过ADD PCRFBINDGRP命令绑定到PCRF组。
- 该命令设定后的数据，需要通过LST PCRFGROUP命令进行查看。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897094)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897094)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCRFGRPNAME | PCRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PCRF组的名字，要求在系统内唯一，数据来源为运营商规划。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| MASTERPCRF | 主用PCRF主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于设置主用PCRF主机名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897094)

设置主用PCRF，“PCRFGRPNAME”为“huawei”，“MASTERPCRF”为“test”：

```
SET MASTERPCRF:PCRFGRPNAME="huawei",MASTERPCRF="test";
```
