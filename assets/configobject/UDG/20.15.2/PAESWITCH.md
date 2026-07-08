---
id: UDG@20.15.2@ConfigObject@PAESWITCH
type: ConfigObject
name: PAESWITCH（PAE开关信息）
nf: UDG
version: 20.15.2
object_name: PAESWITCH
object_kind: global_setting
status: active
---

# PAESWITCH（PAE开关信息）

## 说明

该命令用于设置PAE隔离核查询开关，若打开，则计算VM/容器CPU利用率包括PAE隔离核；若关闭，则计算VM/容器CPU利用率不包括PAE隔离核。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SWITCH |
> | --- |
> | DISABLE |

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-PAESWITCH]] · DSP PAESWITCH
- [[command/UDG/20.15.2/SET-PAESWITCH]] · SET PAESWITCH

## 证据

- 原始手册：`evidence/UDG/20.15.2/PAESWITCH.md`
- 原始手册：`evidence/UDG/20.15.2/PAESWITCH.md`
