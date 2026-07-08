---
id: UDG@20.15.2@ConfigObject@RULEBINDING
type: ConfigObject
name: RULEBINDING（用户模板和规则的绑定关系）
nf: UDG
version: 20.15.2
object_name: RULEBINDING
object_kind: binding
applicable_nf:
- PGW-U
- UPF
status: active
---

# RULEBINDING（用户模板和规则的绑定关系）

## 说明

**适用NF：PGW-U、UPF**

该命令用于增加用户模板与规则绑定关系，当用户数据报文可以匹配到多个规则时，需要将多个规则绑定到用户模板下。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-RULEBINDING]] · ADD RULEBINDING
- [[command/UDG/20.15.2/LST-RULEBINDING]] · LST RULEBINDING
- [[command/UDG/20.15.2/RMV-RULEBINDING]] · RMV RULEBINDING

## 关联对象

- [[configobject/UDG/20.15.2/USERPROFILE]] · USERPROFILE

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除用户模板和规则的绑定关系（RMV-RULEBINDING）_82837274.md`
- 原始手册：`evidence/UDG/20.15.2/增加用户模板和规则的绑定关系（ADD-RULEBINDING）_82837272.md`
- 原始手册：`evidence/UDG/20.15.2/查询用户模板和规则的绑定关系（LST-RULEBINDING）_86526204.md`
