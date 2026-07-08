---
id: UNC@20.15.2@MMLCommand@RMV LOCUPDQOS
type: MMLCommand
name: RMV LOCUPDQOS（删除本地更新QoS值）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LOCUPDQOS
command_category: 配置类
applicable_nf:
- GGSN
- PGW-C
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 本地更新QOS
status: active
---

# RMV LOCUPDQOS（删除本地更新QoS值）

## 功能

**适用NF：GGSN、PGW-C、SGW-C**

该命令用于删除本地配置的更新QoS值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数必须已经通过命令ADD APN配置。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LOCUPDQOS]] · 本地更新QoS值（LOCUPDQOS）

## 使用实例

删除本地更新QoS值，“APN名称”为“HUAWEI.COM”：

```
RMV LOCUPDQOS: APN="HUAWEI.COM";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-LOCUPDQOS.md`
