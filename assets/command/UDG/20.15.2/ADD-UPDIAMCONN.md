---
id: UDG@20.15.2@MMLCommand@ADD UPDIAMCONN
type: MMLCommand
name: ADD UPDIAMCONN（增加Diameter链路）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: UPDIAMCONN
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 200
category_path:
- 用户面服务管理
- Diameter管理
- Diameter连接
- Diameter链路
status: active
---

# ADD UPDIAMCONN（增加Diameter链路）

## 功能

**适用NF：UPF**

此命令用于增加Diameter链路。

根据网络规划，需要增加UPF到对端网元的一条Diameter链路时，可以在执行完ADD UPDIAMPEERADDR和ADD UPDIAMCONNGRP等命令后，执行此命令增加Diameter链路。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为200。
- 对于同一对ConnGrp和LocInterface，允许多条记录存在，每条记录的地址必须不同。
- 指定地址时，系统根据配置生成一条记录，如果配置重复，则配置失败。
- 配置DiamConnection之后，再增加Addr不会自动增加链路，而是必须配置DiamConnection才会建链。
- 指定地址但不指定对端端口号时，系统根据指定的地址，查找对应的DiamPeerAddr，自动生成多条记录，如果新生成的记录在表中已经存在，则跳过该条记录，如果DiamConnection表规格不足够容纳全部新增记录的时候，则配置失败。
- 不指定地址时，系统根据Diameter链路组中的Hostname，查找对应的DiamPeerAddr，自动生成多条记录，如果新生成的记录在表中已经存在，则跳过该条记录，如果DiamConnection表规格不足够容纳全部新增记录的时候，则配置失败。
- 如果本端接口的VPN和Diameter链路组中peer绑定的VPN不一致，则配置失败。
- 如果需要实现链路在不同POD上的负荷分担，则配置链路时必须为链路指定不同的本端接口。
- Swm等单个应用在整机中允许的最大链接数为200。
- 不配置LocalPort参数或LocalPort参数配置为0，都表示配置系统指定端口的Connection。
- LocalPort配置为0只在LOCAL_IP_PEER模式下生效，LocalPort配置为非0在LOCALPORT模式下生效。
- LocalPort参数配置为非0的有效值时，表示建链时使用的本端端口号为配置的值，不使用系统指定的端口号。
- 当配置LocalPort参数为非0值，但是集中点模式为非LOCALPORT模式时，也允许配置下发，但是不会建链。
- 一个DIAMCONNGRP最多支持配置32个DIAMCONNECTION实例。
- 同一个peer的不同Local Host不能使用相同的LocInterface。
- Swm等单个应用在整机中允许的最大SCTP链接数为60。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DIAMCONNGRP | Diameter链路组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter链路的Diameter链路组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD UPDIAMCONNGRP命令配置生成。 |
| LOCINTERFACE | 本端接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter链路的本端接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| PEERADDRTYPE | 对端地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路的对端地址类型。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- IPv4：地址类型为IPv4。<br>- IPv6：地址类型为IPv6。<br>- SCTP：地址类型为SCTP端点。<br>默认值：无<br>配置原则：无 |
| PEERIPV4ADDR | 对端IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PEERADDRTYPE”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于指定IPv4地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。不支持0.0.0.0和255.255.255.255。<br>默认值：无<br>配置原则：无 |
| PEERIPV6ADDR | 对端IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PEERADDRTYPE”配置为“IPv6”时为必选参数。<br>参数含义：该参数用于指定IPv6地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。不支持全F。<br>默认值：无<br>配置原则：无 |
| PEERPORT | 对端端口号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PEERADDRTYPE”配置为“IPv4” 或 “IPv6”时为可选参数。<br>参数含义：该参数用于指定IP类地址的端口号。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为1～65534。<br>默认值：无<br>配置原则：无 |
| PEERSCTPENDPT | 对端SCTP端点名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PEERADDRTYPE”配置为“SCTP”时为必选参数。<br>参数含义：该参数用于指定SCTP端点名称。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD UPSCTPENDPOINT命令配置生成。 |
| REVERSEIP | SCTP建链交换本端IP地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PEERADDRTYPE”配置为“SCTP”时为可选参数。<br>参数含义：该参数用于指定SCTP建链是否交换本端IP地址。1个本端逻辑接口可以配置主IP地址和子IP地址，当该参数配置为ENABLE时，本地逻辑接口的子IP作为偶联的主用IP，本地逻辑接口的主IP作为偶联的从IP。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- DISABLE：不使能SCTP建链交换本端IP地址。<br>- ENABLE：使能SCTP建链交换本端IP地址。<br>默认值：DISABLE<br>配置原则：根据实际规划选择对应的枚举值。 |
| LOCALPORT | 本端端口 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链接的本端端口。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0，19865～19928。<br>默认值：0<br>配置原则：可配置端口范围按照应用进行区分：Swm应用端口范围19865~19928。 |

## 操作的配置对象

- [Diameter链路（UPDIAMCONN）](configobject/UDG/20.15.2/UPDIAMCONN.md)

## 使用实例

根据网络规划，需要新增一个UPF到对端网元的Diameter链路，则可以按如下配置：

```
ADD UPDIAMCONN: DIAMCONNGRP="Grp1", LOCINTERFACE="swmif1/0/0", PEERADDRTYPE=IPv4, PEERIPV4ADDR="10.10.10.11", PEERPORT=3868;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加Diameter链路（ADD-UPDIAMCONN）_45195178.md`
