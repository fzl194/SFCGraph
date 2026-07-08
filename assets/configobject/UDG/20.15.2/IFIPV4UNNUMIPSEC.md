---
id: UDG@20.15.2@ConfigObject@IFIPV4UNNUMIPSEC
type: ConfigObject
name: IFIPV4UNNUMIPSEC（接口IPv4借用地址）
nf: UDG
version: 20.15.2
object_name: IFIPV4UNNUMIPSEC
object_kind: entity
status: active
---

# IFIPV4UNNUMIPSEC（接口IPv4借用地址）

## 说明

该命令用于配置接口的借用IPv4地址。当IP地址资源紧张（不能为每一个接口分配一个IP地址）或接口只是偶尔使用不需要长期独占一个IP地址时，配置接口借用其他接口的IP地址，以节约地址资源。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令的必选参数IFNAME可通过[**LST INTERFACEIPSEC**](../接口配置/查询接口（LST INTERFACEIPSEC）_80592504.md)命令查询到。
> - 借用方不能为以太网接口。
> - 被借用方接口的IP地址本身不能为借用来的IP地址。
> - 被借用方的IP地址可以借给多个接口。
> - 如果被借用接口有多个IP地址，则只能借用主IP地址。
> - 如果被借用接口没有配置IP地址，则接口借用到的IP地址为0.0.0.0。
> - 虚拟的Loopback接口的IP地址可被其他接口借用，但Loopback接口不能借用其他接口的IP地址。
>
> - 最多可输入65535条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-IFIPV4UNNUMIPSEC]] · ADD IFIPV4UNNUMIPSEC
- [[command/UDG/20.15.2/LST-IFIPV4UNNUMIPSEC]] · LST IFIPV4UNNUMIPSEC
- [[command/UDG/20.15.2/MOD-IFIPV4UNNUMIPSEC]] · MOD IFIPV4UNNUMIPSEC
- [[command/UDG/20.15.2/RMV-IFIPV4UNNUMIPSEC]] · RMV IFIPV4UNNUMIPSEC

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改接口IPv4借用地址（MOD-IFIPV4UNNUMIPSEC）_80432532.md`
- 原始手册：`evidence/UDG/20.15.2/删除接口IPv4借用地址（RMV-IFIPV4UNNUMIPSEC）_80751072.md`
- 原始手册：`evidence/UDG/20.15.2/增加接口IPv4借用地址（ADD-IFIPV4UNNUMIPSEC）_25830687.md`
- 原始手册：`evidence/UDG/20.15.2/查询接口IPv4借用地址（LST-IFIPV4UNNUMIPSEC）_80910990.md`
