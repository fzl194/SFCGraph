---
id: UNC@20.15.2@MMLCommand@ADD APNRDSSVRGRP
type: MMLCommand
name: ADD APNRDSSVRGRP（设置APN Radius服务器组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APNRDSSVRGRP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 10000
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 连接管理
- APN Radius服务器
status: active
---

# ADD APNRDSSVRGRP（设置APN Radius服务器组）

## 功能

**适用NF：PGW-C、SMF**

该命令用来添加指定APN实例下绑定的RADIUS服务器组。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为10000。
- 一个APN只能绑定一个RADIUS服务器组。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| RDSSVRGRPNAME | RADIUS Server Group名称 | 可选必选说明：必选参数<br>参数含义：RADIUS服务器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：该参数使用ADD RDSSVRGRP命令配置生成。 |
| COPYINTERIMUPD | 抄送Interim-Update Request | 可选必选说明：可选参数<br>参数含义：配置是否抄送中间话单。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：DISABLE<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNRDSSVRGRP]] · APN Radius服务器组（APNRDSSVRGRP）

## 使用实例

添加APN Radius服务器组，APN为apntest，Radius服务器组名为rgtest，命令为：

```
ADD APNRDSSVRGRP:APN="apntest",RDSSVRGRPNAME="rgtest";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-APNRDSSVRGRP.md`
