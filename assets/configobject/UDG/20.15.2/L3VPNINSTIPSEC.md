---
id: UDG@20.15.2@ConfigObject@L3VPNINSTIPSEC
type: ConfigObject
name: L3VPNINSTIPSEC（L3VPN实例）
nf: UDG
version: 20.15.2
object_name: L3VPNINSTIPSEC
object_kind: entity
status: active
---

# L3VPNINSTIPSEC（L3VPN实例）

## 说明

该命令用于增加L3VPN实例。

> **说明**
> - 该命令执行后立即生效。
>
> - 不能增加VPN实例 _public_、__mpp_vpn_inner__ 。
>
> - 最多可输入1001条记录。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | VRFNAME |
> | --- |
> | _public_ |

## 操作本对象的命令

- [ADD L3VPNINSTIPSEC](command/UDG/20.15.2/ADD-L3VPNINSTIPSEC.md)
- [LST L3VPNINSTIPSEC](command/UDG/20.15.2/LST-L3VPNINSTIPSEC.md)
- [RMV L3VPNINSTIPSEC](command/UDG/20.15.2/RMV-L3VPNINSTIPSEC.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除L3VPN实例（RMV-L3VPNINSTIPSEC）_80751074.md`
- 原始手册：`evidence/UDG/20.15.2/增加L3VPN实例（ADD-L3VPNINSTIPSEC）_25830689.md`
- 原始手册：`evidence/UDG/20.15.2/查询L3VPN实例（LST-L3VPNINSTIPSEC）_25912249.md`
