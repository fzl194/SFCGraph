---
id: UNC@20.15.2@MMLCommand@RMV UEDNSBINDUPGRP
type: MMLCommand
name: RMV UEDNSBINDUPGRP（删除UPF组的DNS属性）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: UEDNSBINDUPGRP
command_category: 配置类
applicable_nf:
- GGSN
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- DN网络DNS_NBNS选择管理
- DNS选择管理
- UPF组DNS域名策略
status: active
---

# RMV UEDNSBINDUPGRP（删除UPF组的DNS属性）

## 功能

**适用NF：GGSN、PGW-C、SMF**

该命令用于删除指定UPF组的DNS属性和DNS64属性。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGRPNAME | UPF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD UEDNSUPGROUP命令生成。 |
| APNTYPE | APN类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN类型。<br>数据来源：本端规划<br>取值范围：<br>- ALL_APN（所有APN）<br>- APN_GROUP（APN组）<br>- SPECIAL_APN（指定APN）<br>默认值：无<br>配置原则：<br>优先级从高到低：“SPECIAL_APN”、“APN_GROUP”、“ALL_APN”。 |
| APNGRPNAME | APN组名 | 可选必选说明：该参数在"APNTYPE"配置为"APN_GROUP"时为条件必选参数。<br>参数含义：该参数用于指定APN组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无<br>配置原则：<br>该参数使用ADD SMFAPNGRP命令配置生成。<br>该参数在“APNTYPE”参数配置为“APN_GROUP”后生效。 |
| APN | APN名称 | 可选必选说明：该参数在"APNTYPE"配置为"SPECIAL_APN"时为条件必选参数。<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。<br>该参数在“APNTYPE”参数配置为“SPECIAL_APN”后生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UEDNSBINDUPGRP]] · UPF组的DNS属性（UEDNSBINDUPGRP）

## 使用实例

当APNTYPE为ALL_APN时，删除UPF组upfgrp1的DNS属性和DNS64属性：

```
RMV UEDNSBINDUPGRP: UPFGRPNAME="upfgrp1",APNTYPE=ALL_APN;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-UEDNSBINDUPGRP.md`
