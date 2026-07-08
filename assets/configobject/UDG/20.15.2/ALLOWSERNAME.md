---
id: UDG@20.15.2@ConfigObject@ALLOWSERNAME
type: ConfigObject
name: ALLOWSERNAME（基于地址的白名单）
nf: UDG
version: 20.15.2
object_name: ALLOWSERNAME
object_kind: entity
status: active
---

# ALLOWSERNAME（基于地址的白名单）

## 说明

该命令用于增加基于IP地址过滤的允许访问的服务白名单，当系统作为服务端时，添加到白名单中的指定IP地址的服务，只允许白名单中指定的对端地址的服务访问。未添加到白名单的服务则允许所有对端访问。

> **说明**
> - 该命令执行后立即生效。
>
> - 如果配置了该白名单，白名单中的服务不允许白名单以外的NF的业务访问。
>
> - 最多可输入256条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-ALLOWSERNAME]] · ADD ALLOWSERNAME
- [[command/UDG/20.15.2/LST-ALLOWSERNAME]] · LST ALLOWSERNAME
- [[command/UDG/20.15.2/RMV-ALLOWSERNAME]] · RMV ALLOWSERNAME

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除基于地址的白名单（RMV-ALLOWSERNAME）_29213289.md`
- 原始手册：`evidence/UDG/20.15.2/增加基于地址的白名单（ADD-ALLOWSERNAME）_83813626.md`
- 原始手册：`evidence/UDG/20.15.2/查询基于地址的白名单（LST-ALLOWSERNAME）_83653656.md`
