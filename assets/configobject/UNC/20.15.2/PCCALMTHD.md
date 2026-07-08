---
id: UNC@20.15.2@ConfigObject@PCCALMTHD
type: ConfigObject
name: PCCALMTHD（PCC告警阈值）
nf: UNC
version: 20.15.2
object_name: PCCALMTHD
object_kind: global_setting
applicable_nf:
- PGW-C
- SMF
status: active
---

# PCCALMTHD（PCC告警阈值）

## 说明

**适用NF：PGW-C、SMF**

此命令支持Gx接口消息交互超时告警，对于PCRF由于性能问题回响应慢，或者PCRF的应用层发生故障不回响应的情况，可以进行更好的监控。使用该命令可以控制连续超时的CCA消息数累加到门限值时触发告警，连续收到CCA消息数累加到门限值时恢复告警。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-PCCALMTHD]] · LST PCCALMTHD
- [[command/UNC/20.15.2/SET-PCCALMTHD]] · SET PCCALMTHD

## 证据

- 原始手册：`evidence/UNC/20.15.2/PCCALMTHD.md`
- 原始手册：`evidence/UNC/20.15.2/PCCALMTHD.md`
