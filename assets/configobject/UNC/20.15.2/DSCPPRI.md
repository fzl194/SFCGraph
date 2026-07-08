---
id: UNC@20.15.2@ConfigObject@DSCPPRI
type: ConfigObject
name: DSCPPRI（DSCP映射优先级配置表）
nf: UNC
version: 20.15.2
object_name: DSCPPRI
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# DSCPPRI（DSCP映射优先级配置表）

## 说明

**适用网元：SGSN、MME**

本命令用于增加DSCP映射优先级表。DSCP映射优先级表是调度模块决定报文入队列的依据。 UNC 网元将报文映射为四个优先级，不同DSCP值的报文将按照DSCP映射优先级表入不同优先级的队列，找不到映射关系的报文将入“优先级4”的队列。

相关命令: [**SET IFDSCP**](../接口DSCP管理/设置接口DSCP配置(SET IFDSCP)_26306022.md)

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-DSCPPRI]] · ADD DSCPPRI
- [[command/UNC/20.15.2/LST-DSCPPRI]] · LST DSCPPRI
- [[command/UNC/20.15.2/MOD-DSCPPRI]] · MOD DSCPPRI
- [[command/UNC/20.15.2/RMV-DSCPPRI]] · RMV DSCPPRI

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSCPPRI.md`
- 原始手册：`evidence/UNC/20.15.2/DSCPPRI.md`
- 原始手册：`evidence/UNC/20.15.2/DSCPPRI.md`
- 原始手册：`evidence/UNC/20.15.2/DSCPPRI.md`
