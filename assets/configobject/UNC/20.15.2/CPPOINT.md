---
id: UNC@20.15.2@ConfigObject@CPPOINT
type: ConfigObject
name: CPPOINT（CP端点信息）
nf: UNC
version: 20.15.2
object_name: CPPOINT
object_kind: entity
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
status: active
---

# CPPOINT（CP端点信息）

## 说明

**适用NF：SMF、SGW-C、PGW-C、GGSN**

在初始配置时，该命令用于在建立会话前增加一个CP端点即控制面SMF端点，包含了该CP端点的信息以及所属的CP节点即控制面SMF节点的索引。一个CP端点归属于一个CP节点，一个CP节点下可以有多个CP端点。比如CP节点相当于一个主机，那么CP端点就相当于其中的一个端口。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-CPPOINT]] · ADD CPPOINT
- [[command/UNC/20.15.2/LST-CPPOINT]] · LST CPPOINT
- [[command/UNC/20.15.2/RMV-CPPOINT]] · RMV CPPOINT

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除CP端点信息（RMV-CPPOINT）_09654362.md`
- 原始手册：`evidence/UNC/20.15.2/增加CP端点信息（ADD-CPPOINT）_09653065.md`
- 原始手册：`evidence/UNC/20.15.2/查询CP端点信息（LST-CPPOINT）_09654424.md`
