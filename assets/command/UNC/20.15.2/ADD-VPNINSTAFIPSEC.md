---
id: UNC@20.15.2@MMLCommand@ADD VPNINSTAFIPSEC
type: MMLCommand
name: ADD VPNINSTAFIPSEC（增加L3VPN实例地址族）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: VPNINSTAFIPSEC
command_category: 配置类
effect_mode: 立即生效
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

# ADD VPNINSTAFIPSEC（增加L3VPN实例地址族）

## 功能

该命令用于设置指定VPN实例下的地址族。

## 注意事项

- 该命令执行后立即生效。

- 需要确保指定的VPN实例在设备上已经通过[**ADD L3VPNINSTIPSEC**](../L3VPN实例配置命令/增加L3VPN实例（ADD L3VPNINSTIPSEC）_25830689.md)增加。
- 不能给VPN实例__mpp_vpn_inner__添加地址族。

- 最多可输入1001条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户增加地址族的L3VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：<br>不支持空格。使用<br>[**LST L3VPNINSTIPSEC**](../L3VPN实例配置命令/查询L3VPN实例（LST L3VPNINSTIPSEC）_25912249.md)<br>命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置指定VPN实例下的地址族。<br>数据来源：本端规划<br>取值范围：<br>- “Ipv4uni（IPv4地址族）”：IPv4地址族<br>- “Ipv6uni（IPv6地址族）”：IPv6地址族<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VPNINSTAFIPSEC]] · L3VPN实例地址族（VPNINSTAFIPSEC）

## 使用实例

增加名称为“vrf1”的VPN实例下的IPv4单播地址族：

```
ADD VPNINSTAFIPSEC:VRFNAME="vrf1", AFTYPE=Ipv4uni;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加L3VPN实例地址族（ADD-VPNINSTAFIPSEC）_26032191.md`
