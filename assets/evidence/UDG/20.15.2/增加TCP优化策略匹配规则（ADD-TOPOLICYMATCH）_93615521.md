# 增加TCP优化策略匹配规则（ADD TOPOLICYMATCH）

- [命令功能](#ZH-CN_CONCEPT_0000204493615521__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000204493615521__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000204493615521__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000204493615521__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000204493615521__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000204493615521)

**适用NF：PGW-U、UPF**

该命令用于增加TCP优化策略匹配规则，实现基于小区/IMSI/RAT类型的TCP优化参数定制化功能。

#### [注意事项](#ZH-CN_CONCEPT_0000204493615521)

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 该命令最大记录数为100。
- 在同一条TCP优化策略匹配命令中，CellGroupName/IMSIGroupName/RATtype之间为与关系，即配置的所有条件均匹配中，才认为匹配中TCP优化策略。
- CellGroupName/IMSIGroupName/RATtype三个可选参数中至少有一个有值。

#### [操作用户权限](#ZH-CN_CONCEPT_0000204493615521)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000204493615521)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLGROUPNAME | 小区组名称 | 可选必选说明：可选参数<br>参数含义：指定小区组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD CELLBINDGRP命令配置生成。 |
| IMSIGROUPNAME | IMSI 组名称 | 可选必选说明：可选参数<br>参数含义：指定IMSI组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD IMSIBINDGRP命令配置生成。 |
| RATTYPE | RAT类型 | 可选必选说明：可选参数<br>参数含义：无线接入技术类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- UTRAN：3G用户。<br>- EUTRAN：4G用户。<br>- NR：5G用户。<br>默认值：无<br>配置原则：无 |
| POLICYID | 策略ID | 可选必选说明：必选参数<br>参数含义：策略ID。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～7。<br>默认值：无<br>配置原则：该参数使用ADD TOPOLICYCFG命令配置生成。 |

#### [使用实例](#ZH-CN_CONCEPT_0000204493615521)

运营商需要增加一个小区组名称为TestCellGroupName，策略ID为1的策略匹配规则：

```
ADD TOPOLICYMATCH: CELLGROUPNAME="TestCellGroupName",POLICYID=1;
```
