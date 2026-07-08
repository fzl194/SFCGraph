# 设置APN Radius服务器组（ADD APNRDSSVRGRP）

- [命令功能](#ZH-CN_CONCEPT_0209896735__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896735__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896735__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896735__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896735__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896735)

**适用NF：PGW-C、SMF**

该命令用来添加指定APN实例下绑定的RADIUS服务器组。

#### [注意事项](#ZH-CN_CONCEPT_0209896735)

- 该命令执行后立即生效。
- 该命令最大记录数为10000。
- 一个APN只能绑定一个RADIUS服务器组。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896735)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896735)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| RDSSVRGRPNAME | RADIUS Server Group名称 | 可选必选说明：必选参数<br>参数含义：RADIUS服务器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：该参数使用ADD RDSSVRGRP命令配置生成。 |
| COPYINTERIMUPD | 抄送Interim-Update Request | 可选必选说明：可选参数<br>参数含义：配置是否抄送中间话单。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：DISABLE<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209896735)

添加APN Radius服务器组，APN为apntest，Radius服务器组名为rgtest，命令为：

```
ADD APNRDSSVRGRP:APN="apntest",RDSSVRGRPNAME="rgtest";
```
