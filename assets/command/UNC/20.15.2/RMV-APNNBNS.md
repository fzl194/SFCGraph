---
id: UNC@20.15.2@MMLCommand@RMV APNNBNS
type: MMLCommand
name: RMV APNNBNS（删除APN的NBNS属性）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNNBNS
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- DN网络DNS_NBNS选择管理
- NBNS选择管理
- APN的NBNS属性
status: active
---

# RMV APNNBNS（删除APN的NBNS属性）

## 功能

**适用NF：PGW-C、GGSN、SMF**

该命令用来删除APN实例的NBNS属性。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [APN的NBNS属性（APNNBNS）](configobject/UNC/20.15.2/APNNBNS.md)

## 使用实例

删除APN为“huawei.com”的NBNS属性：

```
RMV APNNBNS: APN="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除APN的NBNS属性（RMV-APNNBNS）_77037098.md`
