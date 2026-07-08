---
id: UDG@20.15.2@ConfigObject@DRAUTOACTIVE
type: ConfigObject
name: DRAUTOACTIVE（冷备容灾自动升主功能参数）
nf: UDG
version: 20.15.2
object_name: DRAUTOACTIVE
object_kind: global_setting
status: active
---

# DRAUTOACTIVE（冷备容灾自动升主功能参数）

## 说明

该命令用于冷备容灾场景下，设置自动升主功能。

> **说明**
> - 该命令执行后立即生效。
>
> - 此命令只在冷备容灾模式下生效。
> - 此命令只能在配置主网元执行。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | ISAUTOACTIVE | STBYTOACTTIME | NOAUTOTIME |
> | --- | --- | --- |
> | TRUE | 15 | 60 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-DRAUTOACTIVE]] · LST DRAUTOACTIVE
- [[command/UDG/20.15.2/SET-DRAUTOACTIVE]] · SET DRAUTOACTIVE

## 证据

- 原始手册：`evidence/UDG/20.15.2/DRAUTOACTIVE.md`
- 原始手册：`evidence/UDG/20.15.2/DRAUTOACTIVE.md`
