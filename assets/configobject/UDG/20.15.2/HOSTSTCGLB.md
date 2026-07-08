---
id: UDG@20.15.2@ConfigObject@HOSTSTCGLB
type: ConfigObject
name: HOSTSTCGLB（全局协议报文统计配置）
nf: UDG
version: 20.15.2
object_name: HOSTSTCGLB
object_kind: global_setting
status: active
---

# HOSTSTCGLB（全局协议报文统计配置）

## 说明

该命令用于设置全局协议报文统计配置。

该命令的优先级低于ADD HOSTSTCIF命令，如果接口上配置了接口协议报文统计配置，则对应接口的协议报文统计功能不受该命令的影响。

## 操作本对象的命令

- [LST HOSTSTCGLB](command/UDG/20.15.2/LST-HOSTSTCGLB.md)
- [SET HOSTSTCGLB](command/UDG/20.15.2/SET-HOSTSTCGLB.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询全局协议报文统计配置（LST-HOSTSTCGLB）_49802002.md`
- 原始手册：`evidence/UDG/20.15.2/设置全局协议报文统计配置（SET-HOSTSTCGLB）_00441557.md`
