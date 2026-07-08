# 增加IPDOMAIN组（ADD BSFIPDOMAINGRP）

- [命令功能](#ZH-CN_MMLREF_0000001875982828__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001875982828__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001875982828__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001875982828__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001875982828)

该命令用于配置IPDOMAIN组。

## [注意事项](#ZH-CN_MMLREF_0000001875982828)

- 该命令执行后立即生效。

- 最多可输入25000条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0000001875982828)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001875982828)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPNAME | IPDOMAIN组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPDOMAIN组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：无 |
| IPDOMAIN | IPDOMAIN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IPDOMAIN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001875982828)

在IPDOMAIN组"ipdomaingroup1"中新增IPDOMAIN信息"Domain_0"：

```
ADD BSFIPDOMAINGRP: GRPNAME="ipdomaingroup1", IPDOMAIN="Domain_0";
```
