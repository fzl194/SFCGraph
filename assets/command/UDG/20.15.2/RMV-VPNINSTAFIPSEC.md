---
id: UDG@20.15.2@MMLCommand@RMV VPNINSTAFIPSEC
type: MMLCommand
name: RMV VPNINSTAFIPSEC（删除L3VPN实例地址族）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: VPNINSTAFIPSEC
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- VPN管理
- L3VPN管理
- VPN实例地址族配置命令
status: active
---

# RMV VPNINSTAFIPSEC（删除L3VPN实例地址族）

## 功能

![](删除L3VPN实例地址族（RMV VPNINSTAFIPSEC）_25912257.assets/notice_3.0-zh-cn.png)

该操作会删除所有该VPN实例地址族下的关联配置。请谨慎使用。

该命令用于删除指定L3VPN实例下的地址族。

> **说明**
> - 该命令执行后立即生效。
>
> - 不能删除VPN实例 _public_、__mpp_vpn_inner__ 的地址族。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户增加地址族的L3VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：<br>不支持空格。使用<br>[**LST L3VPNINSTIPSEC**](../L3VPN实例配置命令/查询L3VPN实例（LST L3VPNINSTIPSEC）_25912249.md)<br>命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置指定VPN实例下的地址族。<br>数据来源：本端规划<br>取值范围：<br>- “Ipv4uni（IPv4地址族）”：IPv4地址族<br>- “Ipv6uni（IPv6地址族）”：IPv6地址族<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@VPNINSTAFIPSEC]] · L3VPN实例地址族（VPNINSTAFIPSEC）

## 使用实例

删除名称为“vrf1”的VPN实例下的IPv4单播地址族：

```
RMV VPNINSTAFIPSEC:VRFNAME="vrf1", AFTYPE=Ipv4uni;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-VPNINSTAFIPSEC.md`
