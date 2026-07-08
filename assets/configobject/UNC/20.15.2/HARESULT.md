---
id: UNC@20.15.2@ConfigObject@HARESULT
type: ConfigObject
name: HARESULT（HA选举结果）
nf: UNC
version: 20.15.2
object_name: HARESULT
object_kind: query_target
applicable_nf:
- SGSN
- MME
status: active
---

# HARESULT（HA选举结果）

## 说明

**适用网元：SGSN、MME**

该命令用于显示参与HA选举的关键功能模块的主控信息。

HA选举是用于从多个同类进程中选举出主进程和备进程的一套选举机制。

系统管理支持两种控制模式：分布控制模式和全局控制模式。分布控制是指系统内各个进程的资源独立管理，多个进程间松耦合。全局控制是指系统中部署主控模块，同类进程的资源在主控模块中统一管理。

全局控制模式中会将主控模块部署在HA选举的主进程和备进程中，正常运行时只有主进程中的主控模块参与全局管理，备进程作为主进程的备份不参与全局管理。当主进程故障时，备进程中的主控模块接替主进程中的主控模块参与全局管理。

## 操作本对象的命令

- [DSP HARESULT](command/UNC/20.15.2/DSP-HARESULT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示HA选举结果(DSP-HARESULT)_72345473.md`
