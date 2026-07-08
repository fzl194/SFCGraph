---
id: UDG@20.15.2@ConfigObject@SCALINGSWITCH
type: ConfigObject
name: SCALINGSWITCH（扩缩容开关）
nf: UDG
version: 20.15.2
object_name: SCALINGSWITCH
object_kind: global_setting
status: active
---

# SCALINGSWITCH（扩缩容开关）

## 说明

此命令用于设置扩缩容开关，监控周期和取样周期。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SCALINGMETHOD | MONITORINGCYCLE | SAMPLINGPERIOD | TIMEUNIT |
> | --- | --- | --- | --- |
> | VNFM | 50 | 2 | Sec |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-SCALINGSWITCH]] · LST SCALINGSWITCH
- [[command/UDG/20.15.2/SET-SCALINGSWITCH]] · SET SCALINGSWITCH

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询扩缩容开关（LST-SCALINGSWITCH）_09587929.md`
- 原始手册：`evidence/UDG/20.15.2/设置扩缩容开关（SET-SCALINGSWITCH）_09587379.md`
