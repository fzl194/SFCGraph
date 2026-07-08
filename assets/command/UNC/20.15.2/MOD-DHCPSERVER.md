---
id: UNC@20.15.2@MMLCommand@MOD DHCPSERVER
type: MMLCommand
name: MOD DHCPSERVER（修改DHCP服务器）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: DHCPSERVER
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- DHCP管理
- DHCP服务器
status: active
---

# MOD DHCPSERVER（修改DHCP服务器）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于修改DHCP服务器配置。

## 注意事项

- 该命令执行后立即生效。

- 如果DHCP服务器组已经与远端地址池组绑定（通过LST DHCPBINDPOOLGRP查询），则不允许修改DHCP服务器的配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | DHCP服务器组名称 | 可选必选说明：必选参数<br>参数含义：该参数指定DHCP服务器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD DHCPSERVERGRP命令配置生成。 |
| ISPRIMARY | 是否是主DHCP服务器 | 可选必选说明：必选参数<br>参数含义：该参数指定是否为主DHCP服务器。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数指定DHCP服务器的IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4地址类型）<br>- IPV6（IPv6地址类型）<br>默认值：无<br>配置原则：无 |
| V4IPADDRESS | DHCPv4服务器IP地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数指定DHCP服务器的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>同一个服务器组下的主、备服务器IPv4地址不能相同。 |
| V6IPADDRESS | DHCPv6服务器IP地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数指定DHCP服务器的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。除了组播地址、链路本地地址、环回地址或未指定的地址为非法地址外，其他都为合法地址。<br>默认值：无<br>配置原则：<br>同一个服务器组下的主、备服务器IPv6子网前缀不能相同。 |
| WALVALUE | WAL值 | 可选必选说明：可选参数<br>参数含义：该参数表示整机（UNC）每秒发送给该DHCP服务器的最大消息数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：<br>缺省为0，表示不控制消息数。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DHCPSERVER]] · DHCP服务器（DHCPSERVER）

## 使用实例

当需要修改DHCP服务器组group1的主DHCP服务器IP地址为10.1.1.2时，使用该命令：

```
MOD DHCPSERVER:GROUPNAME="group1",ISPRIMARY=ENABLE,IPVERSION=IPV4,V4IPADDRESS="10.1.1.2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-DHCPSERVER.md`
