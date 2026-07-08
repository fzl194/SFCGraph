---
id: UDG@20.15.2@MMLCommand@ADD USERSELPLCY
type: MMLCommand
name: ADD USERSELPLCY（添加用户策略选择）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: USERSELPLCY
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 64
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- 用户策略选择
status: active
---

# ADD USERSELPLCY（添加用户策略选择）

## 功能

**适用NF：UPF**

该命令用来添加用户选择策略，应用于该策略选定用户的性能统计。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为64。
- 当前版本不支持配置的类型为USERID的用户策略。
- 执行ADD USERSELPLCY前，应该先执行ADD USERSELATTR或ADD USERSELRANGE，添加用户选择属性或用户选择范围。
- 如果一个用户选择属性中配置了多个区域码，若将此用户选择属性绑定到当前的用户策略，则该用户选择属性中配置的所有区域码都将被绑定到当前的用户策略。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 用户选择策略名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户选择策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、“_”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| POLICYTYPE | 策略类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- USERID：用户id列表。<br>- USERANGE：用户范围。<br>默认值：无<br>配置原则：<br>- USERID：指定策略类型为用户ID，如IMSI、IMEI、MSISDN。<br>- USERRANGE：指定策略包含用户选择属性或用户选择范围。 |
| USERRANGE | 用户选择范围名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“POLICYTYPE”配置为“USERANGE”时为可选参数。<br>参数含义：用户选择策略所绑定的用户范围条件名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该USERRANGE必须已经使用命令ADD USERSELRANGE配置过。<br>- 在执行ADD USERSELPLCY命令时，参数USERRANGE和USERATTR至少输入一个。 |
| USERATTR | 用户选择属性名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“POLICYTYPE”配置为“USERANGE”时为可选参数。<br>参数含义：用户选择策略所绑定的用户属性条件（TAC/RAN/ LACRAC列表）名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该USERATTR必须已经使用命令ADD USERSELATTR配置过。<br>- 在执行ADD USERSELPLCY命令时，参数USERRANGE和USERATTR至少输入一个。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@USERSELPLCY]] · 用户策略选择（USERSELPLCY）

## 使用实例

当运营商需要配置一个基于区域性能统计的用户选择策略：

```
ADD USERSELPLCY: POLICYNAME="beijing", POLICYTYPE=USERANGE, USERRANGE="haidian", USERATTR="zhongguancun";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-USERSELPLCY.md`
