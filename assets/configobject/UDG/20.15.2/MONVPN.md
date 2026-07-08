---
id: UDG@20.15.2@ConfigObject@MONVPN
type: ConfigObject
name: MONVPN（监控VPN实例）
nf: UDG
version: 20.15.2
object_name: MONVPN
object_kind: entity
status: active
---

# MONVPN（监控VPN实例）

## 说明

该命令用于增加监控VPN实例。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。
> - 添加监控VPN实例后，如果监控中的单个VPN实例的邻居全部异常则上报告警ALM-100545容灾组中监控VPN邻居状态异常。
> - 在运行状态为主的容灾实例中，如果任意一个VPN组内所有监控的VPN实例内邻居全部异常，则自动发起容灾实例的主备倒换。
> - 在运行状态为备的容灾实例中，如果任意一个VPN组内所有监控的VPN实例内邻居全部异常，则收到运行主容灾实例的倒换请求后将回应不允许倒换。
> - 该命令执行前，请确保ISLINKED设置正确，否则可能造成误隔离。
>
> - 最多可输入160条记录。

## 操作本对象的命令

- [ADD MONVPN](command/UDG/20.15.2/ADD-MONVPN.md)
- [LST MONVPN](command/UDG/20.15.2/LST-MONVPN.md)
- [RMV MONVPN](command/UDG/20.15.2/RMV-MONVPN.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除监控VPN实例（RMV-MONVPN）_50801297.md`
- 原始手册：`evidence/UDG/20.15.2/增加监控VPN实例（ADD-MONVPN）_00921390.md`
- 原始手册：`evidence/UDG/20.15.2/查询监控VPN实例（LST-MONVPN）_51081641.md`
