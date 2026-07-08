---
id: UDG@20.15.2@MMLCommand@RMV VPNINSTAF
type: MMLCommand
name: RMV VPNINSTAF（删除L3VPN实例地址族）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: VPNINSTAF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VPN管理
- L3VPN管理
- L3VPN实例地址族
status: active
---

# RMV VPNINSTAF（删除L3VPN实例地址族）

## 功能

![](删除L3VPN实例地址族（RMV VPNINSTAF）_00440685.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会删除所有该VPN实例地址族下的关联配置，请谨慎使用并联系华为技术支持协助操作。

该命令用于删除指定L3VPN实例下的地址族。

## 注意事项

- 该命令执行后立即生效。
- 该操作会删除所有该VPN实例地址族下的关联配置。
- 不能删除VPN实例_public_、__mpp_vpn_inner__、__mpp_vpn_inner_server__的地址族。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定L3VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN实例下的地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv6uni：IPv6地址族。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/VPNINSTAF]] · L3VPN实例地址族（VPNINSTAF）

## 使用实例

删除名称为“vrf1”的VPN实例下的IPv4单播地址族：

```
RMV VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-VPNINSTAF.md`
