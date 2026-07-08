---
id: UNC@20.15.2@MMLCommand@RMV APNLOCREPORT
type: MMLCommand
name: RMV APNLOCREPORT（删除基于APN的位置上报配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNLOCREPORT
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 位置上报管理
- APN用户位置信息上报开关
status: active
---

# RMV APNLOCREPORT（删除基于APN的位置上报配置）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除基于APN的位置上报配置。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数必须已经通过命令ADD APN配置。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNLOCREPORT]] · 基于APN的位置上报配置（APNLOCREPORT）

## 使用实例

删除“APN”为“HUAWEI.COM”的位置上报配置：

```
RMV APNLOCREPORT: APN="HUAWEI.COM"
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-APNLOCREPORT.md`
