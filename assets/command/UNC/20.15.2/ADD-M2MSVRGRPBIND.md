---
id: UNC@20.15.2@MMLCommand@ADD M2MSVRGRPBIND
type: MMLCommand
name: ADD M2MSVRGRPBIND（增加M2M服务器组绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: M2MSVRGRPBIND
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- M2M
- M2M服务器组绑定关系
status: active
---

# ADD M2MSVRGRPBIND（增加M2M服务器组绑定关系）

## 功能

**适用NF：PGW-C、SMF**

该命令用来配置指定APN实例、UPF组与M2M服务器组的绑定关系。

## 注意事项

- 该命令执行后立即生效。

- 单独APN实例只能绑定一个M2M服务器组。APN与UPF组名称结合时，只能绑定一个M2M服务器组。APN实例和UPF组均能匹配的M2M服务器组优先级高。

- 最多可输入20000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | M2M服务器组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定M2M服务器组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：<br>该参数使用ADD M2MSERVERGRP命令配置生成。 |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| UPFGRPNAME | UPF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD M2MUPGROUP命令生成。 |

## 操作的配置对象

- [M2M服务器组绑定关系（M2MSVRGRPBIND）](configobject/UNC/20.15.2/M2MSVRGRPBIND.md)

## 使用实例

增加APN与M2M服务器组的绑定，APN为isp，M2M服务器为m2msrvgroup01：

```
ADD M2MSVRGRPBIND:  GROUPNAME="m2msrvgroup01",APN="isp";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加M2M服务器组绑定关系（ADD-M2MSVRGRPBIND）_73321227.md`
