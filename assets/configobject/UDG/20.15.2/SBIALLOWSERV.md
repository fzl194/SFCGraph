---
id: UDG@20.15.2@ConfigObject@SBIALLOWSERV
type: ConfigObject
name: SBIALLOWSERV（基于服务的白名单）
nf: UDG
version: 20.15.2
object_name: SBIALLOWSERV
object_kind: entity
status: active
---

# SBIALLOWSERV（基于服务的白名单）

## 说明

该命令用于增加基于服务类型的白名单，当系统作为服务端时，添加到白名单的服务只允许白名单中指定的网元类型的对端访问。未添加到白名单的服务则允许所有对端访问。

> **说明**
> - 该命令执行后立即生效。
>
> - 命令中的网元实例ID参数目前不生效。
>
> - 最多可输入255条记录。

## 操作本对象的命令

- [ADD SBIALLOWSERV](command/UDG/20.15.2/ADD-SBIALLOWSERV.md)
- [LST SBIALLOWSERV](command/UDG/20.15.2/LST-SBIALLOWSERV.md)
- [RMV SBIALLOWSERV](command/UDG/20.15.2/RMV-SBIALLOWSERV.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除基于服务的白名单（RMV-SBIALLOWSERV）_83972194.md`
- 原始手册：`evidence/UDG/20.15.2/增加基于服务的白名单（ADD-SBIALLOWSERV）_83653652.md`
- 原始手册：`evidence/UDG/20.15.2/查询基于服务的白名单（LST-SBIALLOWSERV）_84132102.md`
