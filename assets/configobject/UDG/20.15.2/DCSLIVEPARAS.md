---
id: UDG@20.15.2@ConfigObject@DCSLIVEPARAS
type: ConfigObject
name: DCSLIVEPARAS（DCS直播参数）
nf: UDG
version: 20.15.2
object_name: DCSLIVEPARAS
object_kind: global_setting
status: active
---

# DCSLIVEPARAS（DCS直播参数）

## 说明

该命令用于设置DCS直播参数。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | READBEHINDTHRES | PUBTIMEOUT | PUBVERIFYPERIOD | SUBVERIFYPERIOD | LIVEAGINGPERIOD |
> | --- | --- | --- | --- | --- |
> | 3 | 200 | 30 | 30 | 30 |

## 操作本对象的命令

- [LST DCSLIVEPARAS](command/UDG/20.15.2/LST-DCSLIVEPARAS.md)
- [SET DCSLIVEPARAS](command/UDG/20.15.2/SET-DCSLIVEPARAS.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询DCS直播参数（LST-DCSLIVEPARAS）_76289642.md`
- 原始手册：`evidence/UDG/20.15.2/设置DCS直播参数（SET-DCSLIVEPARAS）_76129918.md`
