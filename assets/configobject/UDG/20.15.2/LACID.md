---
id: UDG@20.15.2@ConfigObject@LACID
type: ConfigObject
name: LACID（从LAC组内删除一个LAC）
nf: UDG
version: 20.15.2
object_name: LACID
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# LACID（从LAC组内删除一个LAC）

## 说明

**适用NF：PGW-U、UPF**

该命令用来在LAC组内绑定LAC号段。当需要在指定LAC组内绑定某个LAC号段时，使用该命令。

## 操作本对象的命令

- [ADD LACID](command/UDG/20.15.2/ADD-LACID.md)
- [LST LACID](command/UDG/20.15.2/LST-LACID.md)
- [RMV LACID](command/UDG/20.15.2/RMV-LACID.md)

## 关联对象

- [LACGROUP](configobject/UDG/20.15.2/LACGROUP.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/从LAC组内删除一个LAC（RMV-LACID）_82837198.md`
- 原始手册：`evidence/UDG/20.15.2/在LAC组内添加一个LAC（ADD-LACID）_82837197.md`
- 原始手册：`evidence/UDG/20.15.2/查看LAC与LAC组的绑定关系（LST-LACID）_82837199.md`
