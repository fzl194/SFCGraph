---
id: UDG@20.15.2@ConfigObject@TRUNKMEMBER
type: ConfigObject
name: TRUNKMEMBER（Trunk成员接口）
nf: UDG
version: 20.15.2
object_name: TRUNKMEMBER
object_kind: entity
status: active
---

# TRUNKMEMBER（Trunk成员接口）

## 说明

Trunk是一种捆绑技术。将多个物理接口捆绑成一个逻辑接口，这个逻辑接口就称为Trunk接口。捆绑在一起的每个物理接口称为成员接口。Trunk技术可以实现增加带宽、提高可靠性和负载分担的功能。当用户设备使用的是以太网接口，需要实现这些功能时，可以通过该命令创建Eth-Trunk接口，并通过该命令将以太网接口加入创建的Eth-Trunk接口中。

## 操作本对象的命令

- [ADD TRUNKMEMBER](command/UDG/20.15.2/ADD-TRUNKMEMBER.md)
- [DSP TRUNKMEMBER](command/UDG/20.15.2/DSP-TRUNKMEMBER.md)
- [LST TRUNKMEMBER](command/UDG/20.15.2/LST-TRUNKMEMBER.md)
- [RMV TRUNKMEMBER](command/UDG/20.15.2/RMV-TRUNKMEMBER.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除Trunk成员接口（RMV-TRUNKMEMBER）_49962066.md`
- 原始手册：`evidence/UDG/20.15.2/增加Trunk成员接口（ADD-TRUNKMEMBER）_50121754.md`
- 原始手册：`evidence/UDG/20.15.2/显示Trunk成员接口信息（DSP-TRUNKMEMBER）_50121638.md`
- 原始手册：`evidence/UDG/20.15.2/查询Trunk成员接口信息（LST-TRUNKMEMBER）_49802114.md`
