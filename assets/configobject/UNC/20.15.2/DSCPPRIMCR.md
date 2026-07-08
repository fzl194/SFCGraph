---
id: UNC@20.15.2@ConfigObject@DSCPPRIMCR
type: ConfigObject
name: DSCPPRIMCR（DSCP映射优先级配置表）
nf: UNC
version: 20.15.2
object_name: DSCPPRIMCR
object_kind: entity
applicable_nf:
- MME
status: active
---

# DSCPPRIMCR（DSCP映射优先级配置表）

## 说明

**适用网元：MME**

本命令用于增加DSCP映射优先级表。DSCP映射优先级表是调度模块决定报文入队列的依据。 UNC 网元将报文映射为四个优先级，不同DSCP值的报文将按照DSCP映射优先级表入不同优先级的队列，找不到映射关系的报文将入“优先级4”的队列。

相关命令:

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-DSCPPRIMCR]] · ADD DSCPPRIMCR
- [[command/UNC/20.15.2/LST-DSCPPRIMCR]] · LST DSCPPRIMCR
- [[command/UNC/20.15.2/MOD-DSCPPRIMCR]] · MOD DSCPPRIMCR
- [[command/UNC/20.15.2/RMV-DSCPPRIMCR]] · RMV DSCPPRIMCR

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSCPPRIMCR.md`
- 原始手册：`evidence/UNC/20.15.2/DSCPPRIMCR.md`
- 原始手册：`evidence/UNC/20.15.2/DSCPPRIMCR.md`
- 原始手册：`evidence/UNC/20.15.2/DSCPPRIMCR.md`
