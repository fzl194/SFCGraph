---
id: UDG@20.15.2@ConfigObject@BGPPEERAF
type: ConfigObject
name: BGPPEERAF（BGP对等体地址族）
nf: UDG
version: 20.15.2
object_name: BGPPEERAF
object_kind: entity
status: active
---

# BGPPEERAF（BGP对等体地址族）

## 说明

对等体可以有多个地址族，该命令用于添加BGP IPv4或IPv6对等体地址族。

公网下的对等体创建时会默认创建IPv4对等体地址族。

![](增加BGP对等体地址族（ADD BGPPEERAF）_50121606.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该操作会导致对等体重新连接。

## 操作本对象的命令

- [ADD BGPPEERAF](command/UDG/20.15.2/ADD-BGPPEERAF.md)
- [LST BGPPEERAF](command/UDG/20.15.2/LST-BGPPEERAF.md)
- [MOD BGPPEERAF](command/UDG/20.15.2/MOD-BGPPEERAF.md)
- [RMV BGPPEERAF](command/UDG/20.15.2/RMV-BGPPEERAF.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改BGP对等体地址族（MOD-BGPPEERAF）_00440493.md`
- 原始手册：`evidence/UDG/20.15.2/删除BGP对等体地址族（RMV-BGPPEERAF）_00441309.md`
- 原始手册：`evidence/UDG/20.15.2/增加BGP对等体地址族（ADD-BGPPEERAF）_50121606.md`
- 原始手册：`evidence/UDG/20.15.2/查询BGP对等体地址族（LST-BGPPEERAF）_00840717.md`
