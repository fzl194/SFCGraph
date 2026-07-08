---
id: UDG@20.15.2@MMLCommand@SET APNAFFUNC
type: MMLCommand
name: SET APNAFFUNC（设置APN防欺诈功能）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APNAFFUNC
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务防欺诈
- APN防欺诈功能
status: active
---

# SET APNAFFUNC（设置APN防欺诈功能）

## 功能

**适用NF：PGW-U、UPF**

![](设置APN防欺诈功能（SET APNAFFUNC）_82837800.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，误配后会影响系统性能，和具体规则匹配到的用户数有关。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。

此命令用于在指定APN下配置是否启用防欺诈功能。当用户需要开启或关闭指定APN下的防欺诈开关时配置。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 系统最多支持配置10000条。
- 对于每个APN，初始的防欺诈开关为DISABLE。
- 误配后会影响系统性能，和具体规则匹配到的用户数有关。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| ISENABLE | 防欺诈开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN防欺诈功能开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能防欺诈功能。<br>- ENABLE：使能防欺诈功能。<br>默认值：无<br>配置原则：<br>- 如果运营商希望开启APN下的防欺诈功能，则需要将此参数设为ENABLE。只有开启了防欺诈功能的用户，防欺诈配置才能生效。<br>- 如果运营商不希望开启APN下的防欺诈功能，则需要将此参数设为DISABLE。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNAFFUNC]] · APN防欺诈功能（APNAFFUNC）

## 使用实例

假如运营商需要开启指定APN防欺诈功能，则配置命令如下：

```
SET APNAFFUNC:APN="abc",ISENABLE=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-APNAFFUNC.md`
