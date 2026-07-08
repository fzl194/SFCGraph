---
id: UDG@20.15.2@ConfigObject@PRTGRPINFO
type: ConfigObject
name: PRTGRPINFO（保护组信息）
nf: UDG
version: 20.15.2
object_name: PRTGRPINFO
object_kind: query_target
status: active
---

# PRTGRPINFO（保护组信息）

## 说明

该命令用于显示保护组信息。

外部网关路由器只与保护组内ISU/APU之间建立BFD会话，备路由也只到保护组内ISU/APU的ECMP路由。

> **说明**
> - 此命令仅在虚机场景下支持。
> - 仅ISU/APU场景支持显示保护组信息。

## 操作本对象的命令

- [DSP PRTGRPINFO](command/UDG/20.15.2/DSP-PRTGRPINFO.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示保护组信息（DSP-PRTGRPINFO）_01765324.md`
