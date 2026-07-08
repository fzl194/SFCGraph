---
id: UNC@20.15.2@MMLCommand@RMV DIAMETERAAA
type: MMLCommand
name: RMV DIAMETERAAA（删除Diameter AAA服务器）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DIAMETERAAA
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
- Diameter AAA信息
status: active
---

# RMV DIAMETERAAA（删除Diameter AAA服务器）

## 功能

![](删除Diameter AAA服务器（RMV DIAMETERAAA）_64343904.assets/notice_3.0-zh-cn_2.png)

删除Diameter AAA服务器后，可能会导致non-3GPP用户无法找到Diameter AAA服务器而认证失败。

**适用NF：PGW-C**

此命令用于删除Diameter AAA服务器。当PGW-C不需要往该Diameter AAA服务器发送鉴权消息时，可以执行该命令。

## 注意事项

- 该命令执行后立即生效。

- 如果该DIAMETERAAA已经被绑定到DIAMAAAGRP中，不允许删除。需要从DIAMAAABNDGRP配置中解除绑定才允许删除。
- 如果本设备是最后一个使用该HostName的Diameter应用的设备，则同时删除该HostName对应的Diameter对端地址DIAMPEERADDR。
- 如果该HostName已经被Diameter链路组DIAMCONNGRP引用，则同时删除该Diameter链路组配置；如果被删除的Diameter链路组被Diameter链路引用，则同时删除Diameter链路DIAMCONNECTION。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter AAA服务器的主机名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，由软参BIT150控制是否区分大小写。BIT150值为0时，不区分大小写；值为1时，区分大小写，但不允许配置多个仅大小写不同的host-name或realm-name。BIT150详细信息请参见产品文档中的《UNC软件参数》。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DIAMETERAAA]] · Diameter AAA服务器（DIAMETERAAA）

## 使用实例

根据网络规划，需要删除名称为“diameteraaa1”的Diameter AAA服务器：

```
RMV DIAMETERAAA:HOSTNAME="diameteraaa1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DIAMETERAAA.md`
