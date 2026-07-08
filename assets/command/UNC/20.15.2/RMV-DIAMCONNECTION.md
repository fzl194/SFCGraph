---
id: UNC@20.15.2@MMLCommand@RMV DIAMCONNECTION
type: MMLCommand
name: RMV DIAMCONNECTION（删除Diameter链路）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DIAMCONNECTION
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter连接
- Diameter链路
status: active
---

# RMV DIAMCONNECTION（删除Diameter链路）

## 功能

**适用NF：PGW-C、SMF**

![](删除Diameter链路（RMV DIAMCONNECTION）_09897268.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，删除Diameter链路信息可能导致Diameter链路中断，进而影响用户使用业务，比如用户被去活等。

该命令用于删除所有Diameter链路配置信息，或者删除指定Diameter链路组下的Diameter链路配置信息。

根据网络规划，需要删除UNC到对端网元的一条Diameter链路时，可以执行此命令。

## 注意事项

- 该命令执行后立即生效。
- 当未指定Diameter链路组名时，禁止执行该命令。若需要执行，需将软参BYTE976的值设置为169。
- 所有参数都不指定，则删除所有记录。
- 不指定LOCALPORT参数，表示删除由所有其他输入参数锁定的CONNECTION记录，包括系统指定端口或用户指定端口的记录；指定LOCALPORT参数为0时，表示删除系统指定端口CONNECTION记录；指定LOCALPORT参数为非0的有效值时，表示删除配置此端口的CONNECTION记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DIAMCONNGRP | Diameter链路组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路的Diameter链路组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：如果指定了其他参数，则必须指定Diameter链路组名。 |
| LOCINTERFACE | 本端接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路的本端接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| PEERADDRTYPE | 对端地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路的对端地址类型。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- IPv4：地址类型为IPv4。<br>- IPv6：地址类型为IPv6。<br>- SCTP：地址类型为SCTP端点。<br>默认值：无<br>配置原则：无 |
| PEERIPV4ADDR | 对端IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PEERADDRTYPE”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于指定IPv4地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。不支持0.0.0.0和255.255.255.255。<br>默认值：无<br>配置原则：无 |
| PEERIPV6ADDR | 对端IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PEERADDRTYPE”配置为“IPv6”时为必选参数。<br>参数含义：该参数用于指定IPv6地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。不支持全F。<br>默认值：无<br>配置原则：无 |
| PEERPORT | 对端端口号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PEERADDRTYPE”配置为“IPv4” 或 “IPv6”时为可选参数。<br>参数含义：该参数用于指定IP类地址的端口号。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为1～65534。<br>默认值：无<br>配置原则：无 |
| PEERSCTPENDPT | 对端SCTP端点名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PEERADDRTYPE”配置为“SCTP”时为必选参数。<br>参数含义：该参数用于指定SCTP端点名称。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| LOCALPORT | 本端端口 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链接的本端端口。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0，13200～13263，16400～16463，19765～19784。<br>默认值：无<br>配置原则：可配置端口范围按照应用进行区分：Gx应用端口范围16400~16463；Gy应用端口范围13200~13263；S6b应用端口范围19765~19784。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DIAMCONNECTION]] · Diameter链路（DIAMCONNECTION）

## 使用实例

根据网络规划，需要删除一个UNC到对端网元的Diameter链路，则可以按如下配置：

```
RMV DIAMCONNECTION:DIAMCONNGRP="Grp1",LOCINTERFACE="gxif1/0/0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DIAMCONNECTION.md`
