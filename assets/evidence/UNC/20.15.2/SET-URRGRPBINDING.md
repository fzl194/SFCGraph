# 设置用户模板的计费属性绑定关系（SET URRGRPBINDING）

- [命令功能](#ZH-CN_CONCEPT_0209897209__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897209__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897209__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897209__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897209__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897209)

**适用NF：PGW-C、SMF**

该命令用于设置用户模板的计费属性绑定关系。

#### [注意事项](#ZH-CN_CONCEPT_0209897209)

- 该命令执行后立即生效。
- 如果UserProfile下不绑定默认计费属性，用户的数据包按全局计费属性计费，否则不计费。
- 该命令设定后的数据，需要通过LST USERPROFILE命令进行查看。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897209)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897209)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD USERPROFILE命令配置生成。 |
| DFTURRGRPNAME | 缺省URR组名称 | 可选必选说明：可选参数<br>参数含义：指定缺省URR组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD URRGROUP命令配置生成。 |

#### [使用实例](#ZH-CN_CONCEPT_0209897209)

假如运营商希望为用户模板绑定默认计费属性：

```
SET URRGRPBINDING:USERPROFILENAME="testuserprofilename",DFTURRGRPNAME="dfturrgrp";
```
