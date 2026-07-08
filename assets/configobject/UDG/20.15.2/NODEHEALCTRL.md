---
id: UDG@20.15.2@ConfigObject@NODEHEALCTRL
type: ConfigObject
name: NODEHEALCTRL（Node自愈策略控制参数）
nf: UDG
version: 20.15.2
object_name: NODEHEALCTRL
object_kind: global_setting
status: active
---

# NODEHEALCTRL（Node自愈策略控制参数）

## 说明

该命令用于设置Node自愈策略控制参数。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令中部分功能在第三方CaaS场景下不可使用。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | BONDINGHEALSW | STGFAULTSWPSW | PODPRTUGDHLSW | PODALLUGDHLSW | TOPOCHECKHLSW | FABRICFAULTSW | NPLINKFAULTSW | VFFAULTHEALSW | OVERLOADHLSW |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | ENABLE | ENABLE | DISABLE | ENABLE | ENABLE | DISABLE | DISABLE | ENABLE | DISABLE |

## 操作本对象的命令

- [LST NODEHEALCTRL](command/UDG/20.15.2/LST-NODEHEALCTRL.md)
- [SET NODEHEALCTRL](command/UDG/20.15.2/SET-NODEHEALCTRL.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Node自愈策略控制参数（LST-NODEHEALCTRL）_48332254.md`
- 原始手册：`evidence/UDG/20.15.2/设置Node自愈策略控制参数（SET-NODEHEALCTRL）_48332256.md`
