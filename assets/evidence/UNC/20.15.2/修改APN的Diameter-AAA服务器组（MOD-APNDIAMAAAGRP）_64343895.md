# 修改APN的Diameter AAA服务器组（MOD APNDIAMAAAGRP）

- [命令功能](#ZH-CN_MMLREF_0264343895__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0264343895__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0264343895__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0264343895__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0264343895)

**适用NF：PGW-C**

此命令用于修改对应的Diameter AAA组和APN的绑定关系。当新建立的non-3GPP会话需要到其他的Diameter AAA下进行鉴权时，操作员可以执行此命令修改该绑定关系。

## [注意事项](#ZH-CN_MMLREF_0264343895)

- 该命令执行后对新接入的non-3GPP会话生效。

- 当修改Diameter AAA组和APN的绑定关系时，已经建立的non-3GPP会话不受影响，但新建立的non-3GPP会话将按更新后的绑定关系进行关联Diameter AAA的选取。

#### [操作用户权限](#ZH-CN_MMLREF_0264343895)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0264343895)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ' ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD APN**](../../../接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>命令配置生成。 |
| GROUPNAME | Diameter AAA组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter AAA组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD DIAMAAAGRP**](../Diameter AAA组/增加Diameter AAA服务器组（ADD DIAMAAAGRP）_64343820.md)<br>命令配置生成。 |

## [使用实例](#ZH-CN_MMLREF_0264343895)

根据网络规划，修改Diameter AAA组和APN的绑定关系，将名称为“diametergroup1”的Diameter AAA组绑定到名称为“apn”的APN实例下：

```
MOD APNDIAMAAAGRP:APN="apn",GROUPNAME="diametergroup1";
```
