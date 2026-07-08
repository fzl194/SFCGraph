---
id: UDG@20.15.2@ConfigObject@SPECURRGRPLIST
type: ConfigObject
name: SPECURRGRPLIST（特殊URR组列表）
nf: UDG
version: 20.15.2
object_name: SPECURRGRPLIST
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# SPECURRGRPLIST（特殊URR组列表）

## 说明

**适用NF：PGW-U、UPF**

该命令用于配置特殊的使用量上报规则组列表，其他功能可以使用该列表内容决策当前业务流是否需要做特殊处理。如HTTP计费防欺诈功能，使用该列表内容决策当前业务流是否需要做防欺诈处理。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-SPECURRGRPLIST]] · ADD SPECURRGRPLIST
- [[command/UDG/20.15.2/LST-SPECURRGRPLIST]] · LST SPECURRGRPLIST
- [[command/UDG/20.15.2/RMV-SPECURRGRPLIST]] · RMV SPECURRGRPLIST

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除特殊URR组列表（RMV-SPECURRGRPLIST）_82837644.md`
- 原始手册：`evidence/UDG/20.15.2/增加特殊URR组列表（ADD-SPECURRGRPLIST）_82837643.md`
- 原始手册：`evidence/UDG/20.15.2/查询特殊URR组列表（LST-SPECURRGRPLIST）_82837645.md`
