---
id: UNC@20.15.2@ConfigObject@IPPOOLALMTHD
type: ConfigObject
name: IPPOOLALMTHD（本地地址池组使用率告警阈值）
nf: UNC
version: 20.15.2
object_name: IPPOOLALMTHD
object_kind: global_setting
applicable_nf:
- PGW-C
- GGSN
- SMF
status: active
---

# IPPOOLALMTHD（本地地址池组使用率告警阈值）

## 说明

**适用NF：PGW-C、GGSN、SMF**

UNC支持将若干个地址池绑定为一个地址池组，并基于该地址池组为UE动态分配地址。为了即时监控地址池组中IP地址的使用率，UNC提供了“地址池组使用率超阈值”告警。该命令用于设置该地址池组使用率告警的产生阈值和恢复阈值。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-IPPOOLALMTHD]] · LST IPPOOLALMTHD
- [[command/UNC/20.15.2/SET-IPPOOLALMTHD]] · SET IPPOOLALMTHD

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询本地地址池组使用率告警阈值（LST-IPPOOLALMTHD）_64343886.md`
- 原始手册：`evidence/UNC/20.15.2/设置本地地址池组使用率告警阈值（SET-IPPOOLALMTHD）_64343916.md`
