---
id: UNC@20.15.2@ConfigObject@CHGCDPIP
type: ConfigObject
name: CHGCDPIP（计费相关的IP配置参数）
nf: UNC
version: 20.15.2
object_name: CHGCDPIP
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# CHGCDPIP（计费相关的IP配置参数）

## 说明

**适用网元：SGSN**

该命令用于对资源池内所有CDP进程配IP地址和端口号的组合，系统从该资源池中为每个CDP进程分配一个IP地址与端口号，作为向CG发送话单时的本端IP地址、端口号。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-CHGCDPIP]] · ADD CHGCDPIP
- [[command/UNC/20.15.2/DSP-CHGCDPIP]] · DSP CHGCDPIP
- [[command/UNC/20.15.2/LST-CHGCDPIP]] · LST CHGCDPIP
- [[command/UNC/20.15.2/RMV-CHGCDPIP]] · RMV CHGCDPIP

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除计费相关的IP配置参数(RMV-CHGCDPIP)_26145360.md`
- 原始手册：`evidence/UNC/20.15.2/增加计费相关的IP配置参数(ADD-CHGCDPIP)_72344961.md`
- 原始手册：`evidence/UNC/20.15.2/显示计费相关的IP配置参数(DSP-CHGCDPIP)_26305176.md`
- 原始手册：`evidence/UNC/20.15.2/查询计费相关的IP配置参数(LST-CHGCDPIP)_72225041.md`
