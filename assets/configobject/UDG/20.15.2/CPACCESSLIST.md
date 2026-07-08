---
id: UDG@20.15.2@ConfigObject@CPACCESSLIST
type: ConfigObject
name: CPACCESSLIST（CP白名单）
nf: UDG
version: 20.15.2
object_name: CPACCESSLIST
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# CPACCESSLIST（CP白名单）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用来配置CP的白名单列表。白名单可以是CP的NodeID也可以为CP发送消息的源IP地址。

## 操作本对象的命令

- [ADD CPACCESSLIST](command/UDG/20.15.2/ADD-CPACCESSLIST.md)
- [LST CPACCESSLIST](command/UDG/20.15.2/LST-CPACCESSLIST.md)
- [RMV CPACCESSLIST](command/UDG/20.15.2/RMV-CPACCESSLIST.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除CP白名单（RMV-CPACCESSLIST）_86530486.md`
- 原始手册：`evidence/UDG/20.15.2/查询CP白名单（LST-CPACCESSLIST）_86530487.md`
- 原始手册：`evidence/UDG/20.15.2/添加CP白名单（ADD-CPACCESSLIST）_86530485.md`
