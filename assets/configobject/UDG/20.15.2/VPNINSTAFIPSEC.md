---
id: UDG@20.15.2@ConfigObject@VPNINSTAFIPSEC
type: ConfigObject
name: VPNINSTAFIPSEC（L3VPN实例地址族）
nf: UDG
version: 20.15.2
object_name: VPNINSTAFIPSEC
object_kind: entity
status: active
---

# VPNINSTAFIPSEC（L3VPN实例地址族）

## 说明

该命令用于设置指定VPN实例下的地址族。

> **说明**
> - 该命令执行后立即生效。
>
> - 需要确保指定的VPN实例在设备上已经通过[**ADD L3VPNINSTIPSEC**](../L3VPN实例配置命令/增加L3VPN实例（ADD L3VPNINSTIPSEC）_25830689.md)增加。
> - 不能给VPN实例__mpp_vpn_inner__添加地址族。
>
> - 最多可输入1001条记录。

## 操作本对象的命令

- [ADD VPNINSTAFIPSEC](command/UDG/20.15.2/ADD-VPNINSTAFIPSEC.md)
- [LST VPNINSTAFIPSEC](command/UDG/20.15.2/LST-VPNINSTAFIPSEC.md)
- [RMV VPNINSTAFIPSEC](command/UDG/20.15.2/RMV-VPNINSTAFIPSEC.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除L3VPN实例地址族（RMV-VPNINSTAFIPSEC）_25912257.md`
- 原始手册：`evidence/UDG/20.15.2/增加L3VPN实例地址族（ADD-VPNINSTAFIPSEC）_26032191.md`
- 原始手册：`evidence/UDG/20.15.2/查询L3VPN实例地址族（LST-VPNINSTAFIPSEC）_26032197.md`
