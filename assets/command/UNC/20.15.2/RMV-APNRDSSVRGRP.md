---
id: UNC@20.15.2@MMLCommand@RMV APNRDSSVRGRP
type: MMLCommand
name: RMV APNRDSSVRGRP（删除APN Radius服务器组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNRDSSVRGRP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 连接管理
- APN Radius服务器
status: active
---

# RMV APNRDSSVRGRP（删除APN Radius服务器组）

## 功能

**适用NF：PGW-C、SMF**

![](删除APN Radius服务器组（RMV APNRDSSVRGRP）_09896737.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，执行命令时若APN实例下有用户存在时，如果删除原服务器组的绑定关系，RADIUS服务器可能会收不到计费停止请求导致计费错误。

该命令用来删除指定APN实例下绑定的RADIUS服务器组。不支持批量删除。

## 注意事项

- 该命令执行后立即生效。
- APN实例下有用户存在时，如果删除原服务器组的绑定关系，RADIUS服务器可能因为收不到计费停止请求消息导致计费错误。
- 对于已在线用户，如果执行该命令后，会导致已在线用户无法发送消息给该RADIUS服务器，重新配置服务器组后，已激活的用户，会将消息发送到新的RADIUS服务器。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNRDSSVRGRP]] · APN Radius服务器组（APNRDSSVRGRP）

## 使用实例

删除APN Radius服务器组，APN为apntest，命令为：

```
RMV APNRDSSVRGRP:APN="apntest";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-APNRDSSVRGRP.md`
