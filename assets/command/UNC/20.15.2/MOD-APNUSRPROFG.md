---
id: UNC@20.15.2@MMLCommand@MOD APNUSRPROFG
type: MMLCommand
name: MOD APNUSRPROFG（修改APN用户模板组绑定关系）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: APNUSRPROFG
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- APN用户模板组绑定
status: active
---

# MOD APNUSRPROFG（修改APN用户模板组绑定关系）

## 功能

**适用NF：PGW-C、SMF**

本命令用于修改一组APN实例与UsrProfGroup的绑定关系。

## 注意事项

- 该命令执行后立即生效。
- 每个APN只能绑定一个UsrProfGroup。
- 要配置此命令，需要首先配置ADD APN和ADD USRPROFGROUP。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN对象名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：配置的APN必须是系统已经存在的APN对象名称。 |
| USERPROFGNAME | 用户模板组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD USRPROFGROUP命令配置生成。<br>- 配置的USERPROFGNAME必须是系统已经存在的UsrProfGroup对象名称。 |

## 操作的配置对象

- [APN用户模板组绑定关系（APNUSRPROFG）](configobject/UNC/20.15.2/APNUSRPROFG.md)

## 使用实例

修改ApnUsrProfG配置，Apn名称为apn1，USERPROFGNAME为usrprofilegroup1：

```
MOD APNUSRPROFG:APN="apn1",USERPROFGNAME="usrprofilegroup1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改APN用户模板组绑定关系（MOD-APNUSRPROFG）_09897225.md`
