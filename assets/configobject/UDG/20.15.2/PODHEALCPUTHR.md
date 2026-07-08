---
id: UDG@20.15.2@ConfigObject@PODHEALCPUTHR
type: ConfigObject
name: PODHEALCPUTHR（对应PODTYPE下的阈值配置）
nf: UDG
version: 20.15.2
object_name: PODHEALCPUTHR
object_kind: entity
status: active
---

# PODHEALCPUTHR（对应PODTYPE下的阈值配置）

## 说明

当前版本此命令可正常下发，但配置不生效。

该命令用于增加对应PODTYPE下CPU的阈值配置。

> **说明**
> - 该命令执行后立即生效。
>
> - 不允许配置hafetcd-pod。可通过LST PODHEALCPUTHR查询已配置的Pod类型，避免配置冲突，只要输入的以“#”分隔的Pod类型在已有记录中就不允许配置。
>
> - 最多可输入1024条记录。

## 操作本对象的命令

- [ADD PODHEALCPUTHR](command/UDG/20.15.2/ADD-PODHEALCPUTHR.md)
- [LST PODHEALCPUTHR](command/UDG/20.15.2/LST-PODHEALCPUTHR.md)
- [MOD PODHEALCPUTHR](command/UDG/20.15.2/MOD-PODHEALCPUTHR.md)
- [RMV PODHEALCPUTHR](command/UDG/20.15.2/RMV-PODHEALCPUTHR.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改对应PODTYPE下的阈值配置（MOD-PODHEALCPUTHR）_60114921.md`
- 原始手册：`evidence/UDG/20.15.2/删除对应PODTYPE的配置记录（RMV-PODHEALCPUTHR）_24675206.md`
- 原始手册：`evidence/UDG/20.15.2/增加对应PODTYPE下CPU的阈值配置（ADD-PODHEALCPUTHR）_60073345.md`
- 原始手册：`evidence/UDG/20.15.2/查询对应PODTYPE的配置记录（LST-PODHEALCPUTHR）_24833370.md`
