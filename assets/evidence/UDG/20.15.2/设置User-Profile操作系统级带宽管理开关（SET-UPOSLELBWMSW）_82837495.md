# 设置User Profile操作系统级带宽管理开关（SET UPOSLELBWMSW）

- [命令功能](#ZH-CN_CONCEPT_0182837495__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837495__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837495__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837495__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837495__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837495)

**适用NF：PGW-U、UPF**

如果运营商希望设置以操作系统类型匹配相应带宽控制策略，可使用该命令来设置User Profile下操作系统级带宽管理开关。

#### [注意事项](#ZH-CN_CONCEPT_0182837495)

- 该命令执行后立即生效。
- 该命令最大记录数为105000。
- 此命令的生效范围限于User Profile。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837495)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837495)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | User Profile名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定User Profile名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD USERPROFILE命令配置生成。<br>- 配置的USERPROFILENAME必须是系统已经存在的UserProfile对象名称。 |
| ISENABLE | User Profile操作系统级带宽管理开关 | 可选必选说明：必选参数<br>参数含义：User Profile操作系统级带宽管理开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）User Profile下操作系统级带宽管理开关。<br>- ENABLE：使能（开启）User Profile操作系统级带宽管理开关。<br>- INHERIT：继承SET APNOSLELBWMSW命令的ISENABLE参数配置。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837495)

假如运营商需使能名称为“testuserprofile”的User Profile的操作系统带宽管理功能：

```
SET UPOSLELBWMSW: USERPROFILENAME="testuserprofile", ISENABLE=ENABLE;
```
