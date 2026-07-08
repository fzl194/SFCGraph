---
id: UDG@20.15.2@ConfigObject@HTTPHTRCFG
type: ConfigObject
name: HTTPHTRCFG（HTR流控全局配置）
nf: UDG
version: 20.15.2
object_name: HTTPHTRCFG
object_kind: global_setting
status: active
---

# HTTPHTRCFG（HTR流控全局配置）

## 说明

该命令用于设置HTR流控全局配置。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SWITCH | STARTTHD | STOPTHD | TARGETTHD | PERIOD | STARTTIMES | STOPTIMES | TIMEOUT | DECRATIO | INCRATIO1 | INCRATIO2 |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | ON | 12 | 1 | 6 | 5 | 4 | 8 | 2000 | 10 | 5 | 18 |

## 操作本对象的命令

- [LST HTTPHTRCFG](command/UDG/20.15.2/LST-HTTPHTRCFG.md)
- [SET HTTPHTRCFG](command/UDG/20.15.2/SET-HTTPHTRCFG.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询HTR流控全局配置（LST-HTTPHTRCFG）_35550174.md`
- 原始手册：`evidence/UDG/20.15.2/设置HTR流控全局配置（SET-HTTPHTRCFG）_35071002.md`
