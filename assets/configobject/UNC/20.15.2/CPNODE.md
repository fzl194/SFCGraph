---
id: UNC@20.15.2@ConfigObject@CPNODE
type: ConfigObject
name: CPNODE（CP节点信息）
nf: UNC
version: 20.15.2
object_name: CPNODE
object_kind: entity
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
status: active
---

# CPNODE（CP节点信息）

## 说明

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于在初始配置时使用该命令添加一个CP节点即控制面节点的信息，包含CP节点的索引、IP地址等信息。

CP节点用于PFCP建立偶联时唯一标识控制面的SMF。

在运营商新增部署SMF时，通过此命令配置控制节点信息，用于实现和UP节点即用户面节点UPF的对接。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-CPNODE]] · ADD CPNODE
- [[command/UNC/20.15.2/LST-CPNODE]] · LST CPNODE
- [[command/UNC/20.15.2/MOD-CPNODE]] · MOD CPNODE
- [[command/UNC/20.15.2/RMV-CPNODE]] · RMV CPNODE

## 证据

- 原始手册：`evidence/UNC/20.15.2/CPNODE.md`
- 原始手册：`evidence/UNC/20.15.2/CPNODE.md`
- 原始手册：`evidence/UNC/20.15.2/CPNODE.md`
- 原始手册：`evidence/UNC/20.15.2/CPNODE.md`
