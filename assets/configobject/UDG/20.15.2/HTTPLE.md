---
id: UDG@20.15.2@ConfigObject@HTTPLE
type: ConfigObject
name: HTTPLE（HTTP本端实体）
nf: UDG
version: 20.15.2
object_name: HTTPLE
object_kind: entity
status: active
---

# HTTPLE（HTTP本端实体）

## 说明

该命令用于增加HTTP本端实体。HTTP是Hyper Text Transfer Protocol协议的缩写，是一个基于TCP/IP通讯协议来传递数据的传输协议，工作于客户端-服务端架构上。NF实例既可能是客户端形态也可能是服务端形态，可通过本命令配置该协议的本端地址、端口号并指定为客户端还是服务端。

> **说明**
> - 该命令执行后立即生效。
>
> - 客户端和服务端相同IP地址时，服务端端口号不能在[24576,32767]范围内。
> - 本端实体类型配置为客户端时，同一个IP地址只能配置一条记录。如果没有配置“TLSIDX”，而实际建立的是HTTPs链路，则使用系统缺省TLS参数创建链路。如果配置了“TLSIDX”，而实际建立的是HTTP链路，则“TLSIDX”不生效。
> - 本端实体类型配置为服务端时，同一个IP地址和端口号只能配置一条记录。
> - IP地址相同的记录，“HTTP本端实体组标识”、“VPN名称”及“路由标记” 必须相同。
> - 本端实体类型配置为客户端时，若配置了"TLSIDX"字段，则需要保证相同本端实体组内所有客户端配置的"TLSIDX"字段的值相同。
> - 本端实体类型为客户端时，若相同本端实体组内，存在其他VPN的客户端配置，则需要通过[**ADD HTTPVPNMAP**](../HTTP VPN映射管理/增加HTTP VPN映射关系（ADD HTTPVPNMAP）_46111673.md)配置该本端实体组内所有VPN的映射关系。
>
> - 最多可输入128条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-HTTPLE]] · ADD HTTPLE
- [[command/UDG/20.15.2/LST-HTTPLE]] · LST HTTPLE
- [[command/UDG/20.15.2/MOD-HTTPLE]] · MOD HTTPLE
- [[command/UDG/20.15.2/RMV-HTTPLE]] · RMV HTTPLE

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改HTTP本端实体（MOD-HTTPLE）_28971845.md`
- 原始手册：`evidence/UDG/20.15.2/删除HTTP本端实体（RMV-HTTPLE）_28971847.md`
- 原始手册：`evidence/UDG/20.15.2/增加HTTP本端实体（ADD-HTTPLE）_84132094.md`
- 原始手册：`evidence/UDG/20.15.2/查询HTTP本端实体（LST-HTTPLE）_29291769.md`
