---
id: UDG@20.15.2@ConfigObject@SBIAPLE
type: ConfigObject
name: SBIAPLE（服务化接口本端实体）
nf: UDG
version: 20.15.2
object_name: SBIAPLE
object_kind: entity
status: active
---

# SBIAPLE（服务化接口本端实体）

## 说明

该命令用于增加本端服务化接口接入点信息，即本端服务化接口实体，供基于服务化接口的业务使用。当本端NF需要和目的NF之间建立服务化连接时，需要添加本配置。

> **说明**
> - 该命令执行后立即生效。
>
> - 本端服务化接口实体（SBIAPLE）引用的HTTP本端实体组（HTTPLEGRP）内必须存在一个作为Server端的HTTP本端实体和一个作为Client端的HTTP本端实体。
> - 如果不配置对端NF信息（目的NF类型、目的NF服务、CHF的目的NF类型），则只能配置一个服务化接口实体。
> - 如果配置对端NF信息（目的NF类型、目的NF服务、CHF的目的NF类型），则针对同一对端NF，只能配置一个服务化接口实体。
>
> - 最多可输入128条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-SBIAPLE]] · ADD SBIAPLE
- [[command/UDG/20.15.2/LST-SBIAPLE]] · LST SBIAPLE
- [[command/UDG/20.15.2/MOD-SBIAPLE]] · MOD SBIAPLE
- [[command/UDG/20.15.2/RMV-SBIAPLE]] · RMV SBIAPLE

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改服务化接口本端实体（MOD-SBIAPLE）_83813638.md`
- 原始手册：`evidence/UDG/20.15.2/删除服务化接口本端实体（RMV-SBIAPLE）_84132108.md`
- 原始手册：`evidence/UDG/20.15.2/增加服务化接口本端实体（ADD-SBIAPLE）_28971835.md`
- 原始手册：`evidence/UDG/20.15.2/查询服务化接口本端实体（LST-SBIAPLE）_29213285.md`
