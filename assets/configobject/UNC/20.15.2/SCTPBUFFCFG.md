---
id: UNC@20.15.2@ConfigObject@SCTPBUFFCFG
type: ConfigObject
name: SCTPBUFFCFG（SCTP缓冲区参数源）
nf: UNC
version: 20.15.2
object_name: SCTPBUFFCFG
object_kind: global_setting
applicable_nf:
- SGSN
- MME
- AMF
status: active
---

# SCTPBUFFCFG（SCTP缓冲区参数源）

## 说明

![](设置SCTP缓冲区参数源(SET SCTPBUFFCFG)_03932862.assets/notice_3.0-zh-cn_2.png)

该命令会改变SCTP通信缓存的使用方式，触发SGP进程内存占用率变化，影响S1接口和N2接口链路的接入。系统稳定运行场景下请慎用本功能。

**适用NF：SGSN、MME、AMF**

该命令用于设置在SCTP初始化时分配缓冲区的参数来源。当前参数来源支持系统内置和用户自定义。系统内置参数源不可更改，用户自定义参数源可以通过 [SET SCTPRXBUFFER](设置SCTP接收缓冲区参数(SET SCTPRXBUFFER)_50932653.md) 和 [SET SCTPTXBUFFER](设置SCTP发送缓冲区参数(SET SCTPTXBUFFER)_81290310.md) 控制。

## 操作本对象的命令

- [LST SCTPBUFFCFG](command/UNC/20.15.2/LST-SCTPBUFFCFG.md)
- [SET SCTPBUFFCFG](command/UNC/20.15.2/SET-SCTPBUFFCFG.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SCTP缓冲区参数源(LST-SCTPBUFFCFG)_50812805.md`
- 原始手册：`evidence/UNC/20.15.2/设置SCTP缓冲区参数源(SET-SCTPBUFFCFG)_03932862.md`
