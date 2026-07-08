---
id: UDG@20.15.2@ConfigObject@DRGROUPABLEMENT
type: ConfigObject
name: DRGROUPABLEMENT（是否使能热备容灾组）
nf: UDG
version: 20.15.2
object_name: DRGROUPABLEMENT
object_kind: global_setting
status: active
---

# DRGROUPABLEMENT（是否使能热备容灾组）

## 说明

该命令用于设置是否使能热备容灾组。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | DRGROUPABLEMENT | ISAUTOACTIVE |
> | --- | --- |
> | DISABLE | FALSE |

## 操作本对象的命令

- [LST DRGROUPABLEMENT](command/UDG/20.15.2/LST-DRGROUPABLEMENT.md)
- [SET DRGROUPABLEMENT](command/UDG/20.15.2/SET-DRGROUPABLEMENT.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询是否使能热备容灾组（LST-DRGROUPABLEMENT）_00761578.md`
- 原始手册：`evidence/UDG/20.15.2/设置是否使能热备容灾组（SET-DRGROUPABLEMENT）_01081370.md`
