# 配置用户属性过滤条件（ADD USRATTRCOND）

- [命令功能](#ZH-CN_CONCEPT_0000202546767424__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000202546767424__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000202546767424__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000202546767424__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000202546767424__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000202546767424)

**适用NF：PGW-U、UPF**

该命令用于增加用户属性过滤条件。

#### [注意事项](#ZH-CN_CONCEPT_0000202546767424)

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为4800。
- 该命令中CONDNAME相同ITEMID不同的过滤项目之间为或关系。即只要有一个过滤项目匹配成功，则认为该过滤条件匹配成功。一个过滤项目中CONTENTTYPE不同的过滤内容之间为与关系。即该过滤项目中所有过滤内容需要都匹配成功，才认为该过滤项目匹配成功。
- CONDNAME、ITEMID、CONTENTTYPE唯一确定一条记录。

#### [操作用户权限](#ZH-CN_CONCEPT_0000202546767424)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000202546767424)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONDNAME | 过滤条件名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置过滤条件名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该命令最多可配置16个CONDNAME。 |
| ITEMID | 过滤条件项目索引 | 可选必选说明：必选参数<br>参数含义：该参数用于设置用户过滤条件项目索引。<br>数据来源：本端规划<br>取值范围：整数类型 ，取值范围是1~4294967295。<br>默认值：无<br>配置原则：无 |
| CONTENTTYPE | 内容类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置过滤条件内容类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- USER_PROFILE：用户模板。<br>- APN：APN。<br>- RAT：RAT类型。<br>- MSISDN：MSISDN。<br>默认值：无<br>配置原则：无 |
| APNNAME | APN名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONTENTTYPE”配置为“APN”时为必选参数。<br>参数含义：该参数用于设置APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD APN命令配置生成。<br>- 每个CONDNAME下最多可配置100个APN作为过滤条件。 |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONTENTTYPE”配置为“USER_PROFILE”时为必选参数。<br>参数含义：该参数用于设置用户模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD USERPROFILE命令配置生成。<br>- 每个CONDNAME下最多可配置100个USERPROFILE作为过滤条件。 |
| RATTYPE | RAT类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONTENTTYPE”配置为“RAT”时为必选参数。<br>参数含义：该参数用于设置RAT类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- RESERVED：预留RAT类型。<br>- UTRAN：无线接入类型为UMTS陆地无线接入网。<br>- GERAN：无线接入类型为GSM/EDGE无线接入网。<br>- WLAN：无线接入类型为无线局域网。<br>- GAN：无线接入类型为通用接入网络 。<br>- HSPAE：无线接入类型为增强型高速分组接入。<br>- EUTRAN：无线接入类型为演进UMTS陆地无线接入网。<br>- VIRTUAL：无线接入类型为Virtual。<br>- EUTRANNBIOT：无线接入类型为EUTRAN-NB-IoT。<br>- LTEM：无线接入类型为LTE-M。<br>- NR：无线接入类型为NR。<br>- REDCAPNR：无线接入类型为RedCap-NR。<br>默认值：无<br>配置原则：每个CONDNAME下最多可配置100个RATTYPE作为过滤条件。 |
| MSISDN | MSISDN | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONTENTTYPE”配置为“MSISDN”时为必选参数。<br>参数含义：该参数用于设置MSISDN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 MSISDN号的组成： 1、用户注册的国家的Country Code (CC) 2、国家移动号，组成如下：National Destination Code (NDC)；Subscriber Number (SN)。<br>默认值：无<br>配置原则：每个CONDNAME下最多可配置100个MSISDN作为过滤条件。 |

#### [使用实例](#ZH-CN_CONCEPT_0000202546767424)

运营商需要增加一个用户属性过滤条件，要求过滤用户模板是up1的用户：

```
ADD USRATTRCOND: CONDNAME="user_cond1", ITEMID=1, CONTENTTYPE=USER_PROFILE, USERPROFILENAME="up1";
```
