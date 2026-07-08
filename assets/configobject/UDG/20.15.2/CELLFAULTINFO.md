---
id: UDG@20.15.2@ConfigObject@CELLFAULTINFO
type: ConfigObject
name: CELLFAULTINFO（故障进程历史记录）
nf: UDG
version: 20.15.2
object_name: CELLFAULTINFO
object_kind: query_target
status: active
---

# CELLFAULTINFO（故障进程历史记录）

## 说明

该命令用于查询进程故障历史记录，支持基于进程名称查询或查询整系统。查询整系统时默认按故障发生时间排序，显示离查询时间最近的前100条记录。

> **说明**
> - 在hafg复位的情况下，无法查询到复位前的历史记录。
> - 该命令最多显示100条记录。
> - 该命令查询成功，但没有显示历史记录，不代表没有进程故障，只是历史数据被清理掉，需要通过告警观察进程故障历史记录。

## 操作本对象的命令

- [DSP CELLFAULTINFO](command/UDG/20.15.2/DSP-CELLFAULTINFO.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示故障进程历史记录（DSP-CELLFAULTINFO）_94730394.md`
