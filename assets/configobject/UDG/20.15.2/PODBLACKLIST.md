---
id: UDG@20.15.2@ConfigObject@PODBLACKLIST
type: ConfigObject
name: PODBLACKLIST（Pod自愈黑名单）
nf: UDG
version: 20.15.2
object_name: PODBLACKLIST
object_kind: entity
status: active
---

# PODBLACKLIST（Pod自愈黑名单）

## 说明

该命令用于增加指定Pod类型到Pod自愈黑名单中。增加到Pod自愈黑名单中的Pod不支持自愈功能。

> **说明**
> - 该命令执行后立即生效。
>
> - 最多可输入1024条记录。

## 操作本对象的命令

- [ADD PODBLACKLIST](command/UDG/20.15.2/ADD-PODBLACKLIST.md)
- [LST PODBLACKLIST](command/UDG/20.15.2/LST-PODBLACKLIST.md)
- [RMV PODBLACKLIST](command/UDG/20.15.2/RMV-PODBLACKLIST.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除Pod自愈黑名单（RMV-PODBLACKLIST）_09587924.md`
- 原始手册：`evidence/UDG/20.15.2/增加Pod自愈黑名单（ADD-PODBLACKLIST）_09587923.md`
- 原始手册：`evidence/UDG/20.15.2/查询Pod自愈黑名单（LST-PODBLACKLIST）_09587374.md`
