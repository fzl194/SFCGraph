---
id: UNC@20.15.2@MMLCommand@ADD DHCPSERVERGRP
type: MMLCommand
name: ADD DHCPSERVERGRP（增加DHCP服务器组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DHCPSERVERGRP
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
- DHCP服务器组
status: active
---

# ADD DHCPSERVERGRP（增加DHCP服务器组）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于创建DHCP服务器组。

## 注意事项

- 该命令执行后立即生效。

- 通过ADD DHCPSERVER可以设置DHCP服务器具体信息。
- 通过ADD DHCPBINDPOOLGRP可以设置地址池组与DHCP服务器组绑定关系。UNC通过绑定关系选择对应DHCP服务器组。

- 最多可输入1000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | DHCP服务器组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DHCP服务器组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4地址类型）<br>- IPV6（IPv6地址类型）<br>默认值：无<br>配置原则：无 |
| REQLEASETIME | 租约时间(小时) | 可选必选说明：可选参数<br>参数含义：该参数用于指定DHCP服务器组的地址租期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0，16~192，单位是小时。<br>默认值：0<br>配置原则：无 |
| RETRYINTVAL | DHCP消息超时重发时间(秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定向DHCP服务器发送消息的超时时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~10，单位是秒。<br>默认值：3<br>配置原则：无 |
| RETRYTIMES | DHCP重发次数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定向DHCP服务器发送消息的重发次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~5。<br>默认值：3<br>配置原则：无 |
| HASVPN | 绑定VPN | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否绑定VPN实例。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：DISABLE<br>配置原则：无 |
| VPNINSTANCE | VPN实例名 | 可选必选说明：该参数在"HASVPN"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数用于指定VPN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不支持空格，区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD VPNINST命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DHCPSERVERGRP]] · DHCP服务器组（DHCPSERVERGRP）

## 使用实例

当需要UNC上激活DHCP服务器分配地址的用户时，使用该命令配置DHCP服务器组：

```
ADD DHCPSERVERGRP:GROUPNAME="testgrp",IPVERSION=IPV4,HASVPN=DISABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-DHCPSERVERGRP.md`
