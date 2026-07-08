---
id: UDG@20.15.2@ConfigObject@ECHOIPLIST
type: ConfigObject
name: ECHOIPLIST（GTP路径管理IP地址）
nf: UDG
version: 20.15.2
object_name: ECHOIPLIST
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# ECHOIPLIST（GTP路径管理IP地址）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用来增加对端网元所属的GTP数据面IP地址段，即配置GTP路径管理黑白名单中的地址段。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-ECHOIPLIST]] · ADD ECHOIPLIST
- [[command/UDG/20.15.2/LST-ECHOIPLIST]] · LST ECHOIPLIST
- [[command/UDG/20.15.2/RMV-ECHOIPLIST]] · RMV ECHOIPLIST

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除GTP路径管理IP地址（RMV-ECHOIPLIST）_82837220.md`
- 原始手册：`evidence/UDG/20.15.2/查询GTP路径管理IP地址（LST-ECHOIPLIST）_82837221.md`
- 原始手册：`evidence/UDG/20.15.2/配置GTP路径管理IP地址（ADD-ECHOIPLIST）_82837219.md`
