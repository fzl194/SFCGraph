---
id: UNC@20.15.2@ConfigObject@PROCFAULTALM
type: ConfigObject
name: PROCFAULTALM（进程故障告警上报模式）
nf: UNC
version: 20.15.2
object_name: PROCFAULTALM
object_kind: global_setting
status: active
---

# PROCFAULTALM（进程故障告警上报模式）

## 说明

设置进程故障告警上报模式。进程故障告警快速上报使能位开启时，出现一次进程异常就立刻上报告警。进程故障告警快速上报使能位关闭时，在1分钟内出现3次进程故障才会上报告警。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-PROCFAULTALM]] · LST PROCFAULTALM
- [[command/UNC/20.15.2/SET-PROCFAULTALM]] · SET PROCFAULTALM

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询进程故障告警上报模式（LST-PROCFAULTALM）_59103884.md`
- 原始手册：`evidence/UNC/20.15.2/设置进程故障告警上报模式（SET-PROCFAULTALM）_59103391.md`
