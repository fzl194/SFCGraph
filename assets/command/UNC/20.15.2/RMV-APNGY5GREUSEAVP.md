---
id: UNC@20.15.2@MMLCommand@RMV APNGY5GREUSEAVP
type: MMLCommand
name: RMV APNGY5GREUSEAVP（删除基于apn的Gy接口重用字段的填写方式）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNGY5GREUSEAVP
command_category: 配置类
applicable_nf:
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- 话单字段控制
- 5G用户话单重用字段控制
status: active
---

# RMV APNGY5GREUSEAVP（删除基于apn的Gy接口重用字段的填写方式）

## 功能

**适用NF：PGW-C**

该命令用于删除指定APN 5G用户接入时，Gy接口重用字段的填写方式。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指示APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>输入的APN名称需要符合APN命名规则，仅支持配置APN NI（Network Identifier），例如“huawei.com”；该参数取值应与ADD APN命令中参数“APN”保持一致，使用该前需通过ADD APN添加一组记录。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNGY5GREUSEAVP]] · 基于apn的Gy接口重用字段的填写方式（APNGY5GREUSEAVP）

## 使用实例

对指定APN的5G用户，当需要删除其Gy接口重用字段的填写方式时，使用该命令。

```
RMV APNGY5GREUSEAVP: APN="APNGY";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除基于apn的Gy接口重用字段的填写方式（RMV-APNGY5GREUSEAVP）_23622990.md`
