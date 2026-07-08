---
id: UNC@20.15.2@ConfigObject@E2ETRCTSK
type: ConfigObject
name: E2ETRCTSK（端到端跟踪任务）
nf: UNC
version: 20.15.2
object_name: E2ETRCTSK
object_kind: entity
applicable_nf:
- AMF
- MME
status: active
---

# E2ETRCTSK（端到端跟踪任务）

## 说明

**适用NF：AMF、MME**

此命令用于增加端到端跟踪任务，用以模拟信令类端到端跟踪，AMF/MME把跟踪任务相关参数仅传递给NG-RAN/eNodeB。

端到端跟踪任务分为管理类和信令类，所谓管理类跟踪是由无线网络或者核心网的网管向网元下发的跟踪任务，网元之间不传输跟踪任务相关参数；而信令类则是由核心网网管下发给UDM/HSS，通过UDM/HSS将跟踪任务相关参数传递给AMF/MME，进而再传递给SMF、SGW、PCF、NG-RAN、eNodeB等周边网元的跟踪任务。

## 操作本对象的命令

- [ADD E2ETRCTSK](command/UNC/20.15.2/ADD-E2ETRCTSK.md)
- [LST E2ETRCTSK](command/UNC/20.15.2/LST-E2ETRCTSK.md)
- [MOD E2ETRCTSK](command/UNC/20.15.2/MOD-E2ETRCTSK.md)
- [RMV E2ETRCTSK](command/UNC/20.15.2/RMV-E2ETRCTSK.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改端到端跟踪任务（MOD-E2ETRCTSK）_09653754.md`
- 原始手册：`evidence/UNC/20.15.2/删除端到端跟踪任务（RMV-E2ETRCTSK）_09653046.md`
- 原始手册：`evidence/UNC/20.15.2/增加端到端跟踪任务（ADD-E2ETRCTSK）_09651835.md`
- 原始手册：`evidence/UNC/20.15.2/查询端到端跟踪任务（LST-E2ETRCTSK）_09653109.md`
