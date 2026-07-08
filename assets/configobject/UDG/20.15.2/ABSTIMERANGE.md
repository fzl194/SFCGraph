---
id: UDG@20.15.2@ConfigObject@ABSTIMERANGE
type: ConfigObject
name: ABSTIMERANGE（绝对时间段）
nf: UDG
version: 20.15.2
object_name: ABSTIMERANGE
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
identifier_parameters:
- TIMERANGENAME
- ABSTIMERANGESEQ
status: active
---

# ABSTIMERANGE（绝对时间段）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用于配置绝对时间段信息，从设定的起始年月日时分到终止年月日时分之间的时间段，该时间段无法循环出现，也没有周期。设置绝对时间段的目的是保证系统的业务在该绝对时间段范围内生效。

## 操作本对象的命令

- [ADD ABSTIMERANGE](command/UDG/20.15.2/ADD-ABSTIMERANGE.md)
- [LST ABSTIMERANGE](command/UDG/20.15.2/LST-ABSTIMERANGE.md)
- [MOD ABSTIMERANGE](command/UDG/20.15.2/MOD-ABSTIMERANGE.md)
- [RMV ABSTIMERANGE](command/UDG/20.15.2/RMV-ABSTIMERANGE.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改绝对时间段（MOD-ABSTIMERANGE）_82837424.md`
- 原始手册：`evidence/UDG/20.15.2/删除绝对时间段（RMV-ABSTIMERANGE）_86527021.md`
- 原始手册：`evidence/UDG/20.15.2/增加绝对时间段（ADD-ABSTIMERANGE）_82837423.md`
- 原始手册：`evidence/UDG/20.15.2/查询绝对时间段（LST-ABSTIMERANGE）_82837426.md`
