---
id: UDG@20.15.2@ConfigObject@PODHEALPLY
type: ConfigObject
name: PODHEALPLY（Pod自愈策略）
nf: UDG
version: 20.15.2
object_name: PODHEALPLY
object_kind: global_setting
status: active
---

# PODHEALPLY（Pod自愈策略）

## 说明

该命令用于设置Pod自愈策略。

> **说明**
> - 该命令执行后立即生效。
>
> - 若HAFG服务发生了主备切换，需要重新计算Pod自愈升级到Node自愈前的Pod自愈次数，当满足参数“自愈次数”的设置值时，才能升级到Node自愈。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | STATUS | PREWAITTIME | HEALWAITTIME | HEALNUM |
> | --- | --- | --- | --- |
> | NORMAL | 300 | 210 | 3 |
> | FAULT | 300 | 420 | 3 |

## 操作本对象的命令

- [LST PODHEALPLY](command/UDG/20.15.2/LST-PODHEALPLY.md)
- [SET PODHEALPLY](command/UDG/20.15.2/SET-PODHEALPLY.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Pod自愈策略（LST-PODHEALPLY）_09587873.md`
- 原始手册：`evidence/UDG/20.15.2/设置Pod自愈策略（SET-PODHEALPLY）_09587937.md`
