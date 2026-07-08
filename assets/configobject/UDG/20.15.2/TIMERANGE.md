---
id: UDG@20.15.2@ConfigObject@TIMERANGE
type: ConfigObject
name: TIMERANGE（时间段）
nf: UDG
version: 20.15.2
object_name: TIMERANGE
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# TIMERANGE（时间段）

## 说明

**适用NF：PGW-U、UPF**

该命令用于配置一个时间段，描述一个特定的时间范围。当系统的业务需要在特定的时间段内生效时，使用此命令进行配置。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-TIMERANGE]] · ADD TIMERANGE
- [[command/UDG/20.15.2/LST-TIMERANGE]] · LST TIMERANGE
- [[command/UDG/20.15.2/RMV-TIMERANGE]] · RMV TIMERANGE

## 关联对象

- [[configobject/UDG/20.15.2/BLACKLISTRULE]] · BLACKLISTRULE
- [[configobject/UDG/20.15.2/BWMRULE]] · BWMRULE
- [[configobject/UDG/20.15.2/RULE]] · RULE

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除时间段（RMV-TIMERANGE）_82837420.md`
- 原始手册：`evidence/UDG/20.15.2/增加时间段（ADD-TIMERANGE）_82837419.md`
- 原始手册：`evidence/UDG/20.15.2/查询时间段（LST-TIMERANGE）_86526448.md`
