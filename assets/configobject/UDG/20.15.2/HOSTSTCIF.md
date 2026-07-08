---
id: UDG@20.15.2@ConfigObject@HOSTSTCIF
type: ConfigObject
name: HOSTSTCIF（接口协议报文统计配置）
nf: UDG
version: 20.15.2
object_name: HOSTSTCIF
object_kind: entity
status: active
---

# HOSTSTCIF（接口协议报文统计配置）

## 说明

该命令用于新增接收方向接口协议报文统计配置。接口名称可以通过LST INTERFACE命令获取。

该命令的优先级高于SET HOSTSTCGLB命令，如果接口上添加了接口协议报文统计配置，则对应接口的协议报文统计功能不受SET HOSTSTCGLB命令的影响。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-HOSTSTCIF]] · ADD HOSTSTCIF
- [[command/UDG/20.15.2/LST-HOSTSTCIF]] · LST HOSTSTCIF
- [[command/UDG/20.15.2/RMV-HOSTSTCIF]] · RMV HOSTSTCIF

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除接口协议报文统计配置（RMV-HOSTSTCIF）_49802518.md`
- 原始手册：`evidence/UDG/20.15.2/增加接口协议报文统计配置（ADD-HOSTSTCIF）_49961322.md`
- 原始手册：`evidence/UDG/20.15.2/查询接口协议报文统计配置（LST-HOSTSTCIF）_00440561.md`
