---
id: UDG@20.15.2@ConfigObject@GCSMOOTHSWITCH
type: ConfigObject
name: GCSMOOTHSWITCH（GC平滑开关）
nf: UDG
version: 20.15.2
object_name: GCSMOOTHSWITCH
object_kind: global_setting
status: active
---

# GCSMOOTHSWITCH（GC平滑开关）

## 说明

该命令用于设置GC（Garbage Collection）平滑开关，决定流控模块计算CPU时是否需要刨除GC。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | STATUS | DURATION | TOKEN |
> | --- | --- | --- |
> | ON | 60 | 10 |

## 操作本对象的命令

- [LST GCSMOOTHSWITCH](command/UDG/20.15.2/LST-GCSMOOTHSWITCH.md)
- [SET GCSMOOTHSWITCH](command/UDG/20.15.2/SET-GCSMOOTHSWITCH.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询GC平滑开关（LST-GCSMOOTHSWITCH）_43960919.md`
- 原始手册：`evidence/UDG/20.15.2/设置GC平滑开关（SET-GCSMOOTHSWITCH）_44040889.md`
