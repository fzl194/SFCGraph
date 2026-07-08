---
id: UNC@20.15.2@MMLCommand@RMV APNUPFINFO
type: MMLCommand
name: RMV APNUPFINFO（删除指定APN的UPF节点信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNUPFINFO
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- APN UPF信息管理
status: active
---

# RMV APNUPFINFO（删除指定APN的UPF节点信息）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于删除指定APN的UPF节点信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数表示APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与ADD APN命令中参数“APN”保持一致，使用该前需通过ADD APN添加一组记录。 |
| UPFINSTANCEID | UPF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数表示UPF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。该参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与ADD UPNODE中参数“NFINSTANCENAME”保持一致，使用该前需通过ADD UPNODE添加一组记录。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNUPFINFO]] · 指定APN的UPF节点信息（APNUPFINFO）

## 使用实例

删除UPF实例标识为upf1的位置特征，对应的APN名称为huawei.com：

```
RMV APNUPFINFO:APN="huawei.com",UPFINSTANCEID="upf1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-APNUPFINFO.md`
