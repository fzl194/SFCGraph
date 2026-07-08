---
id: UNC@20.15.2@MMLCommand@ADD APNDIAMAAAGRP
type: MMLCommand
name: ADD APNDIAMAAAGRP（增加APN的Diameter AAA服务器组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APNDIAMAAAGRP
command_category: 配置类
applicable_nf:
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- Diameter AAA管理
- 服务器配置
- APN的Diameter AAA组
status: active
---

# ADD APNDIAMAAAGRP（增加APN的Diameter AAA服务器组）

## 功能

**适用NF：PGW-C**

此命令用于将Diameter AAA组绑定到指定APN上。当指定APN下需要建立non-3GPP会话时，操作员可以执行此命令将Diameter AAA组绑定到APN上，当该APN的用户激活时，系统选择将该分组下的Diameter AAA进行业务处理。

## 注意事项

- 该命令执行后对新接入的non-3GPP会话生效。

- 最多可输入20000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ' ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD APN**](../../../接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)<br>命令配置生成。 |
| GROUPNAME | Diameter AAA组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter AAA组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD DIAMAAAGRP**](../Diameter AAA组/增加Diameter AAA服务器组（ADD DIAMAAAGRP）_64343820.md)<br>命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNDIAMAAAGRP]] · APN的Diameter AAA服务器组（APNDIAMAAAGRP）

## 使用实例

根据网络规划，将名称为“diametergroup”的Diameter AAA组绑定到名称为“apn”的APN实例下：

```
ADD APNDIAMAAAGRP:APN="apn",GROUPNAME="diametergroup";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-APNDIAMAAAGRP.md`
