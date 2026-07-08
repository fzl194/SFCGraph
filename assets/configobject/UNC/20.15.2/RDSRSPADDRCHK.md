---
id: UNC@20.15.2@ConfigObject@RDSRSPADDRCHK
type: ConfigObject
name: RDSRSPADDRCHK（全局RADIUS响应消息源端口检查配置）
nf: UNC
version: 20.15.2
object_name: RDSRSPADDRCHK
object_kind: global_setting
applicable_nf:
- PGW-C
- SMF
status: active
---

# RDSRSPADDRCHK（全局RADIUS响应消息源端口检查配置）

## 说明

**适用NF：PGW-C、SMF**

该命令用来设置全局RADIUS响应消息源IP/端口检查配置。使能该检查功能，如果RADIUS响应消息的源IP或者端口号与UNC配置的不一致，UNC将丢弃此消息。

## 操作本对象的命令

- [LST RDSRSPADDRCHK](command/UNC/20.15.2/LST-RDSRSPADDRCHK.md)
- [SET RDSRSPADDRCHK](command/UNC/20.15.2/SET-RDSRSPADDRCHK.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局RADIUS响应消息源端口检查配置（LST-RDSRSPADDRCHK）_09896745.md`
- 原始手册：`evidence/UNC/20.15.2/设置全局RADIUS响应消息源IP_端口检查配置（SET-RDSRSPADDRCHK）_09896744.md`
