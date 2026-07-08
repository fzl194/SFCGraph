# 删除UPF组与Diameter本端主机组的关联关系（RMV UPFGBINDLOCG）

- [命令功能](#ZH-CN_CONCEPT_0000201429420952__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000201429420952__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000201429420952__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000201429420952__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000201429420952__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000201429420952)

**适用NF：PGW-C、SMF**

此命令用于删除UPF组与Diameter本端主机组的关联关系。

#### [注意事项](#ZH-CN_CONCEPT_0000201429420952)

- 该命令执行后只对新激活用户生效。
- 删除绑定关系，在不存在其他有效绑定关系的情况下PCC用户相关的业务流程会处理失败。

#### [操作用户权限](#ZH-CN_CONCEPT_0000201429420952)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000201429420952)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGLOCGBNDGNAME | UPF组与Diameter本端主机组的绑定关系组名称 | 可选必选说明：必选参数<br>参数含义：该参数设置UPF组与Diameter本端主机组的绑定关系组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD UPFGLOCGBNDGRP命令配置生成。 |
| UPFGRPNAME | Gx UPF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及特殊字符“#”、“$”和“&”等，由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD GXUPFGROUP命令配置生成。 |
| DIAMLOCGRPNAME | Diameter本端信息组名称 | 可选必选说明：可选参数<br>参数含义：该参数用户指定Diameter本端主机组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD LOCALHOSTGRP命令配置生成。 |

#### [使用实例](#ZH-CN_CONCEPT_0000201429420952)

增加Diameter本端主机名与Diameter本端主机组的绑定关系，组名为“abc”，UPF组名为“upfgroup”，diameter本端主机组名为“locgroup”：

```
RMV UPFGBINDLOCG: UPFGLOCGBNDGNAME="abc", UPFGRPNAME="upfgroup", DIAMLOCGRPNAME="locgroup";
```
