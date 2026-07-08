---
id: UNC@20.15.2@ConfigObject@LCKWHITELST
type: ConfigObject
name: LCKWHITELST（锁定白名单记录）
nf: UNC
version: 20.15.2
object_name: LCKWHITELST
object_kind: entity
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
status: active
---

# LCKWHITELST（锁定白名单记录）

## 说明

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于增加锁定白名单记录。符合该白名单的用户不受LCK APN和LCK SESSIONACT命令的影响，能够创建会话或专载。

## 操作本对象的命令

- [ADD LCKWHITELST](command/UNC/20.15.2/ADD-LCKWHITELST.md)
- [LST LCKWHITELST](command/UNC/20.15.2/LST-LCKWHITELST.md)
- [RMV LCKWHITELST](command/UNC/20.15.2/RMV-LCKWHITELST.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除锁定白名单记录（RMV-LCKWHITELST）_94466596.md`
- 原始手册：`evidence/UNC/20.15.2/增加锁定白名单记录（ADD-LCKWHITELST）_29991961.md`
- 原始手册：`evidence/UNC/20.15.2/查询锁定白名单记录（LST-LCKWHITELST）_29906473.md`
