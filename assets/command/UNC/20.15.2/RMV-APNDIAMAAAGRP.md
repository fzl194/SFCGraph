---
id: UNC@20.15.2@MMLCommand@RMV APNDIAMAAAGRP
type: MMLCommand
name: RMV APNDIAMAAAGRP（删除APN的Diameter AAA服务器组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNDIAMAAAGRP
command_category: 配置类
applicable_nf:
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- Diameter AAA管理
- 服务器配置
- APN的Diameter AAA组
status: active
---

# RMV APNDIAMAAAGRP（删除APN的Diameter AAA服务器组）

## 功能

**适用NF：PGW-C**

此命令用于解除Diameter AAA组和APN的绑定关系。当指定APN下不需要建立non-3GPP会话时，操作员可以执行此命令解除该绑定关系。

## 注意事项

- 该命令执行后立即生效。

- 当解除Diameter AAA组和APN的绑定关系时，已经建立的non-3GPP会话不受影响，但后续新建立的non-3GPP会话将因为无法关联到Diameter AAA而失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ' ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD APN**](../../../接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>命令配置生成。 |

## 操作的配置对象

- [APN的Diameter AAA服务器组（APNDIAMAAAGRP）](configobject/UNC/20.15.2/APNDIAMAAAGRP.md)

## 使用实例

根据网络规划，删除名称为“apn”的APN实例和Diameter AAA组的绑定关系：

```
RMV APNDIAMAAAGRP:APN="apn";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除APN的Diameter-AAA服务器组（RMV-APNDIAMAAAGRP）_64343900.md`
