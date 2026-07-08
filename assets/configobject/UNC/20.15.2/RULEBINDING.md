---
id: UNC@20.15.2@ConfigObject@RULEBINDING
type: ConfigObject
name: RULEBINDING（用户模板和规则的绑定关系）
nf: UNC
version: 20.15.2
object_name: RULEBINDING
object_kind: binding
applicable_nf:
- PGW-C
- SMF
status: active
---

# RULEBINDING（用户模板和规则的绑定关系）

## 说明

**适用NF：PGW-C、SMF**

该命令用于增加用户模板与规则的绑定关系，当用户数据报文可以匹配到多个规则时，需要将多个规则绑定到用户模板下。SMF给UPF下发规则时，下发用户模板即可使多个规则同时生效。

## 操作本对象的命令

- [ADD RULEBINDING](command/UNC/20.15.2/ADD-RULEBINDING.md)
- [LST RULEBINDING](command/UNC/20.15.2/LST-RULEBINDING.md)
- [RMV RULEBINDING](command/UNC/20.15.2/RMV-RULEBINDING.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除用户模板和规则的绑定关系（RMV-RULEBINDING）_09897217.md`
- 原始手册：`evidence/UNC/20.15.2/增加用户模板和规则的绑定关系（ADD-RULEBINDING）_09897216.md`
- 原始手册：`evidence/UNC/20.15.2/查询用户模板和规则的绑定关系（LST-RULEBINDING）_09897218.md`
