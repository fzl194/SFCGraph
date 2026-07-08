---
id: UDG@20.15.2@ConfigObject@DCSSDPARA
type: ConfigObject
name: DCSSDPARA（DCS直通存储慢盘检测参数）
nf: UDG
version: 20.15.2
object_name: DCSSDPARA
object_kind: global_setting
status: active
---

# DCSSDPARA（DCS直通存储慢盘检测参数）

## 说明

该命令用于设置DCS直通存储慢盘检测参数。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SWITCH | SAMPLE | PERIOD | SVCTMTHD | UTILTHD | SDALMTHD | SDRCVTHD |
> | --- | --- | --- | --- | --- | --- | --- |
> | ON | 30 | 1 | 30 | 98 | 70 | 50 |

## 操作本对象的命令

- [LST DCSSDPARA](command/UDG/20.15.2/LST-DCSSDPARA.md)
- [SET DCSSDPARA](command/UDG/20.15.2/SET-DCSSDPARA.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询DCS直通存储慢盘检测参数（LST-DCSSDPARA）_41105089.md`
- 原始手册：`evidence/UDG/20.15.2/设置DCS直通存储慢盘检测参数（SET-DCSSDPARA）_41185261.md`
