# 设置基于APN的应用参数（SET APNAPPPARA）

- [命令功能](#ZH-CN_CONCEPT_0274982441__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0274982441__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0274982441__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0274982441__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0274982441__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0274982441)

**适用NF：PGW-U、UPF**

该命令用于配置APN的app规则匹配条件。

#### [注意事项](#ZH-CN_CONCEPT_0274982441)

- 该命令执行后立即生效。
- 系统最多支持配置10000条。
- 初始值均为INHERIT。

#### [操作用户权限](#ZH-CN_CONCEPT_0274982441)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0274982441)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：用于指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：APN实例名称是通过ADD APN命令配置的。 |
| APPRVALIDCOND | App规则生效条件 | 可选必选说明：必选参数<br>参数含义：用于指定APN的用户访问app时，配置app规则生效的条件。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- INHERIT：继承全局配置。设置此选项，表明该生效条件是继承SET GLBAPPPARA命令中参数APPRVALIDCOND的取值范围。<br>- N4_INDICATION：根据N4接口下发的Application ID作为app规则的匹配条件。<br>- N4_UNRELATED：不论N4接口是否下发Application ID，均进行app规则匹配。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0274982441)

该命令用于设置APN的app规则匹配条件，针对指定的APN进行参数设置，APPRVALIDCOND设置为INHERIT。使用命令：

```
SET APNAPPPARA: APN="apn1", APPRVALIDCOND=INHERIT;
```
