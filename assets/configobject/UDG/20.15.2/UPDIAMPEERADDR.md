---
id: UDG@20.15.2@ConfigObject@UPDIAMPEERADDR
type: ConfigObject
name: UPDIAMPEERADDR（Diameter对端地址）
nf: UDG
version: 20.15.2
object_name: UPDIAMPEERADDR
object_kind: entity
applicable_nf:
- UPF
status: active
---

# UPDIAMPEERADDR（Diameter对端地址）

## 说明

**适用NF：UPF**

该命令用于增加Diameter链路对端的地址信息，配置Diameter链路对端的地址类型、IP、端口号或端点信息。

该命令和DRA等Diameter主机配合使用，指定这些服务器的地址信息，地址分为IP地址和SCTP端点地址。

## 操作本对象的命令

- [ADD UPDIAMPEERADDR](command/UDG/20.15.2/ADD-UPDIAMPEERADDR.md)
- [LST UPDIAMPEERADDR](command/UDG/20.15.2/LST-UPDIAMPEERADDR.md)
- [RMV UPDIAMPEERADDR](command/UDG/20.15.2/RMV-UPDIAMPEERADDR.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除Diameter对端地址（RMV-UPDIAMPEERADDR）_97080149.md`
- 原始手册：`evidence/UDG/20.15.2/增加Diameter对端地址（ADD-UPDIAMPEERADDR）_45195172.md`
- 原始手册：`evidence/UDG/20.15.2/查询Diameter对端地址（LST-UPDIAMPEERADDR）_45432688.md`
