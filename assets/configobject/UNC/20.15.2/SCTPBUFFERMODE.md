---
id: UNC@20.15.2@ConfigObject@SCTPBUFFERMODE
type: ConfigObject
name: SCTPBUFFERMODE（SCTP缓冲区模式）
nf: UNC
version: 20.15.2
object_name: SCTPBUFFERMODE
object_kind: global_setting
applicable_nf:
- SGSN
- MME
- AMF
status: active
---

# SCTPBUFFERMODE（SCTP缓冲区模式）

## 说明

![](设置SCTP缓冲区模式(SET SCTPBUFFERMODE)_04252670.assets/notice_3.0-zh-cn_2.png)

该命令会改变SCTP通信缓存的使用方式，触发SGP进程内存占用率变化，影响S1接口和N2接口链路的接入。系统稳定运行场景下请慎用本功能。

**适用NF：SGSN、MME、AMF**

该命令用于设置系统中SCTP缓冲区的模式。当前模式支持共享模式和私有模式。私有模式表示每个偶联有自己单独的缓冲区，共享模式表示单个SGP进程内的偶联共用一块内存。共享模式相比私有模式可以减少内存开销。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-SCTPBUFFERMODE]] · LST SCTPBUFFERMODE
- [[command/UNC/20.15.2/SET-SCTPBUFFERMODE]] · SET SCTPBUFFERMODE

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SCTP缓冲区模式(LST-SCTPBUFFERMODE)_50612759.md`
- 原始手册：`evidence/UNC/20.15.2/设置SCTP缓冲区模式(SET-SCTPBUFFERMODE)_04252670.md`
