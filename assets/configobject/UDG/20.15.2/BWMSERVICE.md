---
id: UDG@20.15.2@ConfigObject@BWMSERVICE
type: ConfigObject
name: BWMSERVICE（带宽管理业务）
nf: UDG
version: 20.15.2
object_name: BWMSERVICE
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# BWMSERVICE（带宽管理业务）

## 说明

**适用NF：PGW-U、UPF**

该命令用于增加一条带宽管理的业务范围，实现业务区分。该命令支持TOS类型业务，用报文的TOS区分业务，也支持非TOS类型业务，为带宽管理业务绑定一个分类属性、或者指定7层协议、或者绑定一个协议组来区分业务。

## 操作本对象的命令

- [ADD BWMSERVICE](command/UDG/20.15.2/ADD-BWMSERVICE.md)
- [LST BWMSERVICE](command/UDG/20.15.2/LST-BWMSERVICE.md)
- [MOD BWMSERVICE](command/UDG/20.15.2/MOD-BWMSERVICE.md)
- [RMV BWMSERVICE](command/UDG/20.15.2/RMV-BWMSERVICE.md)

## 关联对象

- [BWMRULE](configobject/UDG/20.15.2/BWMRULE.md)
- [CATEGORYPROP](configobject/UDG/20.15.2/CATEGORYPROP.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改带宽管理业务（MOD-BWMSERVICE）_82837474.md`
- 原始手册：`evidence/UDG/20.15.2/删除带宽管理业务（RMV-BWMSERVICE）_82837475.md`
- 原始手册：`evidence/UDG/20.15.2/增加带宽管理业务（ADD-BWMSERVICE）_82837473.md`
- 原始手册：`evidence/UDG/20.15.2/查询带宽管理业务（LST-BWMSERVICE）_82837476.md`
