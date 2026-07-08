---
id: UDG@20.15.2@MMLCommand@MOD UPAPNDIAMAAAG
type: MMLCommand
name: MOD UPAPNDIAMAAAG（修改APN的Diameter AAA服务器组）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: UPAPNDIAMAAAG
command_category: 配置类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: true
category_path:
- 用户面服务管理
- Diameter AAA管理
- 服务器配置
- APN的Diameter AAA组
status: active
---

# MOD UPAPNDIAMAAAG（修改APN的Diameter AAA服务器组）

## 功能

**适用NF：UPF**

![](修改APN的Diameter AAA服务器组（MOD UPAPNDIAMAAAG）_45432718.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该操作会修改Diameter AAA组与APN的绑定关系，可能会导致新激活的用户无可用Diameter AAA服务器而激活失败。

此命令用于修改对应的Diameter AAA组和APN的绑定关系。当新建立的会话需要到其他的Diameter AAA下进行鉴权时，操作员可以执行此命令修改该绑定关系。

## 注意事项

- 该命令执行后对新接入的会话生效。
- 当修改Diameter AAA组和APN的绑定关系时，已经建立的会话不受影响，但新建立的会话将按更新后的绑定关系进行关联Diameter AAA的选取。

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

根据网络规划，修改Diameter AAA组和APN的绑定关系，将名称为“diametergroup1”的Diameter AAA组绑定到名称为“apn”的APN实例下：

```
MOD UPAPNDIAMAAAG:APN="apn",GROUPNAME="diametergroup1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-UPAPNDIAMAAAG.md`
