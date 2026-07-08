---
id: UDG@20.15.2@MMLCommand@RMV USERSELPLCY
type: MMLCommand
name: RMV USERSELPLCY（删除用户策略选择）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: USERSELPLCY
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- 用户策略选择
status: active
---

# RMV USERSELPLCY（删除用户策略选择）

## 功能

**适用NF：UPF**

该命令用来删除指定的用户选择策略。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 用户选择策略名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户选择策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、“_”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@USERSELPLCY]] · 用户策略选择（USERSELPLCY）

## 使用实例

当运营商需要删除一个用户选择策略：

```
RMV USERSELPLCY: POLICYNAME="beijing";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-USERSELPLCY.md`
