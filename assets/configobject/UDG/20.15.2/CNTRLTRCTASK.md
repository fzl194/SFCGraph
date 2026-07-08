---
id: UDG@20.15.2@ConfigObject@CNTRLTRCTASK
type: ConfigObject
name: CNTRLTRCTASK（跨层统一联动跟踪任务）
nf: UDG
version: 20.15.2
object_name: CNTRLTRCTASK
object_kind: action
status: active
---

# CNTRLTRCTASK（跨层统一联动跟踪任务）

## 说明

该命令用于停止跨层统一联动跟踪任务。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令仅在虚机场景下支持，并且仅支持FusionSphere用户态EVS和用户态OVS组网。
> - 该命令会触发PAE和FusionSphere跟踪任务停止，当PAE或FusionSphere的停止跟踪任务返回失败时，如PAE或FusionSphere跟踪任务已经异常停止，该命令会执行失败。

## 操作本对象的命令

- [DSP CNTRLTRCTASK](command/UDG/20.15.2/DSP-CNTRLTRCTASK.md)
- [STP CNTRLTRCTASK](command/UDG/20.15.2/STP-CNTRLTRCTASK.md)
- [STR CNTRLTRCTASK](command/UDG/20.15.2/STR-CNTRLTRCTASK.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/停止跨层统一联动跟踪任务（STP-CNTRLTRCTASK）_73335361.md`
- 原始手册：`evidence/UDG/20.15.2/启动跨层统一联动跟踪任务（STR-CNTRLTRCTASK）_28855492.md`
- 原始手册：`evidence/UDG/20.15.2/显示跨层统一联动跟踪任务信息（DSP-CNTRLTRCTASK）_73575097.md`
