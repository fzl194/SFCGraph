---
id: UDG@20.15.2@MMLCommand@ADD UPAPNDIAMAAAG
type: MMLCommand
name: ADD UPAPNDIAMAAAG（增加APN的Diameter AAA服务器组）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: UPAPNDIAMAAAG
command_category: 配置类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
max_records: 10000
category_path:
- 用户面服务管理
- Diameter AAA管理
- 服务器配置
- APN的Diameter AAA组
status: active
---

# ADD UPAPNDIAMAAAG（增加APN的Diameter AAA服务器组）

## 功能

**适用NF：UPF**

此命令用于将Diameter AAA组绑定到指定APN上。当指定APN下需要建立会话时，操作员可以执行此命令将Diameter AAA组绑定到APN上，当该APN的用户激活时，系统选择将该分组下的Diameter AAA进行业务处理。

## 注意事项

- 该命令执行后对新接入的会话生效。
- 该命令最大记录数为10000。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ' ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| GROUPNAME | Diameter AAA组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter AAA组名。<br>数据来源：本端规划<br>取值范围：不区分大小写，不支持空格。<br>默认值：无<br>配置原则：该参数使用ADD UPDIAMAAAGRP命令配置生成。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@UPAPNDIAMAAAG]] · APN的Diameter AAA服务器组（UPAPNDIAMAAAG）

## 使用实例

根据网络规划，将名称为“diametergroup”的Diameter AAA组绑定到名称为“apn”的APN实例下：

```
ADD UPAPNDIAMAAAG:APN="apn",GROUPNAME="diametergroup";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-UPAPNDIAMAAAG.md`
