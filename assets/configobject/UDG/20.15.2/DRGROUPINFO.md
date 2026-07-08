---
id: UDG@20.15.2@ConfigObject@DRGROUPINFO
type: ConfigObject
name: DRGROUPINFO（容灾组信息）
nf: UDG
version: 20.15.2
object_name: DRGROUPINFO
object_kind: entity
status: active
---

# DRGROUPINFO（容灾组信息）

## 说明

该命令用于增加容灾组信息。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令只用于在UEG-L/UEN网元采用主备（冷备）容灾模式下执行。
> - 该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。
> - 在两个有容灾关系的网元上配置容灾组信息时，容灾组标识、容灾组名称要相同，本端与对端的容灾实例标识要相对应，否则容灾功能无法使用。
> - 在同一个网元下，不允许增加具有相同容灾组标识的容灾组信息，对于错误的容灾组信息，应先进行删除操作，再重新增加正确的容灾组信息。
>
> - 最多可输入1条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-DRGROUPINFO]] · ADD DRGROUPINFO
- [[command/UDG/20.15.2/LST-DRGROUPINFO]] · LST DRGROUPINFO
- [[command/UDG/20.15.2/RMV-DRGROUPINFO]] · RMV DRGROUPINFO

## 证据

- 原始手册：`evidence/UDG/20.15.2/DRGROUPINFO.md`
- 原始手册：`evidence/UDG/20.15.2/DRGROUPINFO.md`
- 原始手册：`evidence/UDG/20.15.2/DRGROUPINFO.md`
