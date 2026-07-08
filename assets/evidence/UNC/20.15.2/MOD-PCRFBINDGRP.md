# 修改PCRF与PCRF Group的关联关系（MOD PCRFBINDGRP）

- [命令功能](#ZH-CN_CONCEPT_0209897097__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897097__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897097__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897097__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897097__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897097)

**适用NF：PGW-C、GGSN**

此命令用于修改指定的PCRF与PCRF分组绑定关系的参数。

#### [注意事项](#ZH-CN_CONCEPT_0209897097)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897097)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897097)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCRFGRPNAME | PCRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PCRF分组的名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD PCRFGROUP命令配置生成。 |
| PCRFHOSTNAME | PCRF主机名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PCRF的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD PCRF命令配置生成。 |
| WEIGHT | PCRF权重 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PCRF的权重。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897097)

修改Pcrf与PCRF Group的关联关系，修改PCRF组名为“abc”，PCRF名为“aaa”的权重为10：

```
MOD PCRFBINDGRP:PCRFGRPNAME="abc",PCRFHOSTNAME="aaa",WEIGHT=10;
```
