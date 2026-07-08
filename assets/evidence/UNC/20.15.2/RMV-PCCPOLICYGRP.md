# 删除PCC策略组（RMV PCCPOLICYGRP）

- [命令功能](#ZH-CN_CONCEPT_0209897175__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897175__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897175__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897175__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897175__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897175)

**适用NF：PGW-C、SMF**

此命令用于删除PCC策略组。

不输入条件，表示删除所有未被引用的PCC策略组。当配置量较大时单次执行可能无法删除全部记录，需要执行多次。

#### [注意事项](#ZH-CN_CONCEPT_0209897175)

- 该命令执行后立即生效。
- 通过命令LST RULE查询Rule记录，如果有引用了该PccPolicyGrp的Rule的记录存在，则不允许删除该PccPolicyGrp记录。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897175)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897175)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCCPOLICYGRPNM | PCC策略组名称 | 可选必选说明：可选参数<br>参数含义：设置PCC策略组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897175)

删除名称为TestPccPolicyGrpName的PCC策略组：

```
RMV PCCPOLICYGRP:PCCPOLICYGRPNM ="TestPccPolicyGrpName";
```
