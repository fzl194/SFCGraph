---
id: UNC@20.15.2@ConfigObject@DIAMPEERADDR
type: ConfigObject
name: DIAMPEERADDR（Diameter对端地址）
nf: UNC
version: 20.15.2
object_name: DIAMPEERADDR
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# DIAMPEERADDR（Diameter对端地址）

## 说明

**适用NF：PGW-C、SMF**

该命令用于增加Diameter链路对端的地址信息，配置Diameter链路对端的地址类型、IP、端口号或端点信息。

该命令和PCRF/OCS/DRA等Diameter主机配合使用，指定这些服务器的地址信息，地址分为IP地址和SCTP端点地址。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-DIAMPEERADDR]] · ADD DIAMPEERADDR
- [[command/UNC/20.15.2/LST-DIAMPEERADDR]] · LST DIAMPEERADDR
- [[command/UNC/20.15.2/RMV-DIAMPEERADDR]] · RMV DIAMPEERADDR

## 证据

- 原始手册：`evidence/UNC/20.15.2/DIAMPEERADDR.md`
- 原始手册：`evidence/UNC/20.15.2/DIAMPEERADDR.md`
- 原始手册：`evidence/UNC/20.15.2/DIAMPEERADDR.md`
