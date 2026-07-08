---
id: UDG@20.15.2@ConfigObject@TWAMPFLOWCTLCFG
type: ConfigObject
name: TWAMPFLOWCTLCFG（跟踪流控配置）
nf: UDG
version: 20.15.2
object_name: TWAMPFLOWCTLCFG
object_kind: global_setting
status: active
---

# TWAMPFLOWCTLCFG（跟踪流控配置）

## 说明

该命令用于设置TWAMP功能的跟踪流控配置参数。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | FCSWITCH | RECOVERLIMIT | TRIGGERLIMIT | TRACETHD |
> | --- | --- | --- | --- |
> | OPEN | 60 | 70 | 60 |

## 操作本对象的命令

- [LST TWAMPFLOWCTLCFG](command/UDG/20.15.2/LST-TWAMPFLOWCTLCFG.md)
- [SET TWAMPFLOWCTLCFG](command/UDG/20.15.2/SET-TWAMPFLOWCTLCFG.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询跟踪流控配置（LST-TWAMPFLOWCTLCFG）_07287404.md`
- 原始手册：`evidence/UDG/20.15.2/设置跟踪流控参数配置（SET-TWAMPFLOWCTLCFG）_42846237.md`
