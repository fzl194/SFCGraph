---
id: UNC@20.15.2@MMLCommand@SET ANONYMOUSAPN
type: MMLCommand
name: SET ANONYMOUSAPN（设置匿名APN配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: ANONYMOUSAPN
command_category: 配置类
applicable_nf:
- SMF
- GGSN
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN管理
- 匿名APN
status: active
---

# SET ANONYMOUSAPN（设置匿名APN配置）

## 功能

**适用NF：SMF、GGSN、PGW-C**

此命令用于用来针对漫游、本地、拜访用户配置是否开启APN纠错功能。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| HOMESWITCH | VISITSWITCH | ROAMINGSWITCH |
| --- | --- | --- |
| DISABLE | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOMESWITCH | 本地用户开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制开启和关闭本地用户匿名APN功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ANONYMOUSAPN查询当前参数配置值。<br>配置原则：无 |
| VISITSWITCH | 拜访用户开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制开启和关闭拜访用户匿名APN功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ANONYMOUSAPN查询当前参数配置值。<br>配置原则：无 |
| ROAMINGSWITCH | 漫游用户开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制开启和关闭漫游用户匿名APN功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ANONYMOUSAPN查询当前参数配置值。<br>配置原则：无 |
| HOMECORRECTAPN | 本地用户纠错后APN | 可选必选说明：该参数在"HOMESWITCH"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于设置本地用户通过匿名APN接入时实际使用的APN实例名。该参数在“HOMESWITCH”配置为“DISABLE”时为空。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ANONYMOUSAPN查询当前参数配置值。<br>配置原则：无 |
| ROAMCORRECTAPN | 漫游用户纠错后APN | 可选必选说明：该参数在"ROAMINGSWITCH"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于设置漫游用户通过匿名APN接入时实际使用的APN实例名。该参数在“ROAMINGSWITCH”配置为“DISABLE”时为空。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ANONYMOUSAPN查询当前参数配置值。<br>配置原则：无 |
| VISITCORRECTAPN | 拜访用户纠错后APN | 可选必选说明：该参数在"VISITSWITCH"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于设置拜访用户通过匿名APN接入时实际使用的APN实例名。该参数在“VISITSWITCH”配置为“DISABLE”时为空。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST ANONYMOUSAPN查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [匿名APN配置（ANONYMOUSAPN）](configobject/UNC/20.15.2/ANONYMOUSAPN.md)

## 使用实例

配置允许漫游用户使用匿名APN接入。

```
SET ANONYMOUSAPN: ROAMINGSWITCH=ENABLE, ROAMCORRECTAPN="isp";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置匿名APN配置（SET-ANONYMOUSAPN）_09651574.md`
