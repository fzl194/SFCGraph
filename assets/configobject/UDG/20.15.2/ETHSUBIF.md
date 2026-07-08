---
id: UDG@20.15.2@ConfigObject@ETHSUBIF
type: ConfigObject
name: ETHSUBIF（子接口配置）
nf: UDG
version: 20.15.2
object_name: ETHSUBIF
object_kind: entity
status: active
---

# ETHSUBIF（子接口配置）

## 说明

该命令用于配置子接口关联VLAN。

为了实现VLAN间通信，可在接入用户终端的接口上通过创建子接口并关联VLAN实现二层网络接入三层网络，从而实现不同网段、不同VLAN间的通信。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-ETHSUBIF]] · ADD ETHSUBIF
- [[command/UDG/20.15.2/LST-ETHSUBIF]] · LST ETHSUBIF
- [[command/UDG/20.15.2/RMV-ETHSUBIF]] · RMV ETHSUBIF

## 关联对象

- [[configobject/UDG/20.15.2/INTERFACE]] · INTERFACE

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除子接口配置（RMV-ETHSUBIF）_00866281.md`
- 原始手册：`evidence/UDG/20.15.2/增加子接口配置（ADD-ETHSUBIF）_49801486.md`
- 原始手册：`evidence/UDG/20.15.2/查询子接口配置信息（LST-ETHSUBIF）_49961422.md`
