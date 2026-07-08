# 删除QoS属性（RMV QOSPROP）

- [命令功能](#ZH-CN_CONCEPT_0209897165__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897165__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897165__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897165__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897165__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897165)

**适用NF：PGW-C、SMF**

该命令用来删除所有或者某个QoS配置。

#### [注意事项](#ZH-CN_CONCEPT_0209897165)

- 该命令执行后立即生效。
- 在删除QoS属性执行RMV QOSPROP命令前需要确定QOSPROPNAME名称是否被引用，使用LST PCCPOLICYGRP和LST L2RULE命令参看QOSPROPNAME名称是否被引用，若被引用则执行RMV QOSPROP命令失败，在删除被引用对象记录才能执行成功。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897165)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897165)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROPNAME | QoS属性名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定QoS属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897165)

删除名称为“test”的QoS属性时，命令为：

```
RMV QOSPROP:QOSPROPNAME="test";
```
