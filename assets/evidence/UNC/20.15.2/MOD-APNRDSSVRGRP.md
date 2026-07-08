# 修改APN Radius服务器组（MOD APNRDSSVRGRP）

- [命令功能](#ZH-CN_CONCEPT_0209896736__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896736__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896736__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896736__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896736__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896736)

**适用NF：PGW-C、SMF**

该命令用来修改指定APN实例下绑定RADIUS服务器组，RADIUS服务器组包括鉴权服务器和计费服务器。

#### [注意事项](#ZH-CN_CONCEPT_0209896736)

- 该命令执行后立即生效。
- 该命令执行后，可能导致老的Radius服务器组会话残留，请确认无对应APN会话后再执行。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896736)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896736)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| RDSSVRGRPNAME | RADIUS Server Group名称 | 可选必选说明：可选参数<br>参数含义：RADIUS服务器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| COPYINTERIMUPD | 抄送Interim-Update Request | 可选必选说明：可选参数<br>参数含义：配置是否抄送中间话单。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：该参数使用ADD RDSSVRGRP命令配置生成。 |

#### [使用实例](#ZH-CN_CONCEPT_0209896736)

修改APN Radius服务器组，APN为apntest，Radius服务器组名为rgtest，命令为：

```
MOD APNRDSSVRGRP:APN="apntest",RDSSVRGRPNAME="rgtest",COPYINTERIMUPD=ENABLE;
```
