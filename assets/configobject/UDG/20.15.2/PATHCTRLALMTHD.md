---
id: UDG@20.15.2@ConfigObject@PATHCTRLALMTHD
type: ConfigObject
name: PATHCTRLALMTHD（大量路径断告警告警阈值）
nf: UDG
version: 20.15.2
object_name: PATHCTRLALMTHD
object_kind: global_setting
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# PATHCTRLALMTHD（大量路径断告警告警阈值）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

系统对接海量的eNodeB/gNodeB，如果出现大量路径断，需要设置ALM-81100 GTPU大量路径断告警的上报阈值和恢复阈值，避免告警风暴。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-PATHCTRLALMTHD]] · LST PATHCTRLALMTHD
- [[command/UDG/20.15.2/SET-PATHCTRLALMTHD]] · SET PATHCTRLALMTHD

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询大量路径断告警告警阈值（LST-PATHCTRLALMTHD）_82837860.md`
- 原始手册：`evidence/UDG/20.15.2/设置大量路径断告警的告警阈值（SET-PATHCTRLALMTHD）_82837861.md`
