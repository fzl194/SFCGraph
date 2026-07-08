---
id: UDG@20.15.2@MMLCommand@SET APNCFTEMPLATE
type: MMLCommand
name: SET APNCFTEMPLATE（设置APN内容过滤模板）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APNCFTEMPLATE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- APN 内容过滤模板绑定配置
status: active
---

# SET APNCFTEMPLATE（设置APN内容过滤模板）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置或者修改APN的内容过滤模板。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 系统最多支持配置10000个APN内容过滤模板。
- 每个APN只可绑定一个内容过滤模板。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNAME | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| CFTEMPLATENAME | 内容过滤模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置内容过滤模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD CFTEMPLATE命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNCFTEMPLATE]] · APN内容过滤模板（APNCFTEMPLATE）

## 关联任务

- [[UDG@20.15.2@Task@0-00254]]

## 使用实例

配置APN的内容过滤模板：

```
SET APNCFTEMPLATE: APNNAME="test", CFTEMPLATENAME="testcftemplate";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-APNCFTEMPLATE.md`
