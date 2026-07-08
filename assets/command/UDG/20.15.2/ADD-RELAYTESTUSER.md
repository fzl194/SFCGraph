---
id: UDG@20.15.2@MMLCommand@ADD RELAYTESTUSER
type: MMLCommand
name: ADD RELAYTESTUSER（增加媒体中继拨测用户）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: RELAYTESTUSER
command_category: 配置类
applicable_nf:
- UPF
- PGW-U
effect_mode: ''
is_dangerous: false
max_records: 1000
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继拨测用户配置
status: active
---

# ADD RELAYTESTUSER（增加媒体中继拨测用户）

## 功能

**适用NF：UPF、PGW-U**

该命令用于增加媒体中继拨测用户。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 该命令最大记录数为1000。
- 删除APN和UserProfile时，会删除RelayTestUser相关的配置。
- 不允许配置APN和IMSI相同或APN和MSISDN相同的记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TESTUSERNAME | 拨测用户名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定拨测用户名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |
| APNNAME | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD APN命令配置生成。<br>- 该参数使用ADD APN命令配置生成。 |
| USERTYPE | 用户类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：表示用户的IMSI号。<br>- MSISDN：表示用户的MSISDN号。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERTYPE”配置为“IMSI”时为必选参数。<br>参数含义：该参数用于表示拨测用户的IMSI号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。必须全部为整数。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：条件必选参数<br>前提条件：该参数在“USERTYPE”配置为“MSISDN”时为必选参数。<br>参数含义：该参数用于表示拨测用户的MSISDN号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。必须全部为整数，且不能为“19”。 MSISDN号的组成： 1、用户注册的国家的Country Code (CC) 2、国家移动号，组成如下：National Destination Code (NDC)；Subscriber Number (SN)。<br>默认值：无<br>配置原则：无 |
| RELAYFUNC | 媒体中继功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制指定用户使能或不使能媒体中继功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Disable：不使能为媒体中继用户。<br>- Enable：使能为媒体中继用户。<br>默认值：无<br>配置原则：无 |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“RELAYFUNC”配置为“Enable”时为必选参数。<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及“,”、“;”、“"”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD USERPROFILE命令配置生成。<br>- 该参数使用ADD USERPROFILE命令配置生成。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RELAYTESTUSER]] · 媒体中继拨测用户（RELAYTESTUSER）

## 使用实例

增加媒体中继拨测用户：

```
ADD RELAYTESTUSER:TESTUSERNAME="user01",APNNAME="apn",USERTYPE=IMSI,IMSI="460011223344551",RELAYFUNC=Enable,USERPROFILENAME="profile01";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-RELAYTESTUSER.md`
