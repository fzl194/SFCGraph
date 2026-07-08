# 删除ApnAlias配置（RMV APNALIAS）

- [命令功能](#ZH-CN_CONCEPT_0186526641__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0186526641__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0186526641__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0186526641__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0186526641__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0186526641)

**适用NF：SGW-U、PGW-U、UPF**

![](删除ApnAlias配置（RMV APNALIAS）_86526641.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该操作会删除别名APN，可能导致用户激活失败。

该命令用于删除ApnAlias配置。当运营商不希望用户使用指定APN别名的时候，需要删除配置的APN别名，该命令可以实现此功能。

#### [注意事项](#ZH-CN_CONCEPT_0186526641)

- 该命令执行后立即生效。
- 与APN对象绑定，删除APN对象中的记录，则绑定关系也要解除。

#### [操作用户权限](#ZH-CN_CONCEPT_0186526641)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0186526641)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNTYPE | APN类型 | 可选必选说明：必选参数<br>参数含义：该参数决定输入名称是真实APN还是APN别名。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALIAS_APN：指示输入APN别名。<br>- REAL_APN：指示输入真实APN。<br>默认值：无<br>配置原则：<br>- 如果运营商希望输入真实APN，则把ApnType置成REAL_APN。<br>- 如果运营商希望输入APN别名，则把ApnType置成ALIAS_APN。 |
| ALIASNAME | APN别名的配置 | 可选必选说明：条件必选参数<br>前提条件：该参数在“APNTYPE”配置为“ALIAS_APN”时为必选参数。<br>参数含义：该参数用于指定APN别名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及特殊字符“_”、“#”、“$”和“&”，不区分大小写。<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“APNTYPE”配置为“REAL_APN”时为必选参数。<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及特殊字符“_”、“#”、“$”和“&”，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0186526641)

- 假设运营商不希望用户使用名为“test2”的APN别名时，需要删除APN别名的配置：
  ```
  RMV APNALIAS:APNTYPE=ALIAS_APN,ALIASNAME="test2";
  ```
- 假设运营商希望删除配置APN名称为“ma”的所有APN别名时，使用该命令：
  ```
  RMV APNALIAS:APNTYPE=REAL_APN,APN="ma";
  ```
