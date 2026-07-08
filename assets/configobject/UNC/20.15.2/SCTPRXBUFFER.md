---
id: UNC@20.15.2@ConfigObject@SCTPRXBUFFER
type: ConfigObject
name: SCTPRXBUFFER（SCTP接收缓冲区参数）
nf: UNC
version: 20.15.2
object_name: SCTPRXBUFFER
object_kind: global_setting
applicable_nf:
- SGSN
- MME
- AMF
status: active
---

# SCTPRXBUFFER（SCTP接收缓冲区参数）

## 说明

![](设置SCTP接收缓冲区参数(SET SCTPRXBUFFER)_50932653.assets/notice_3.0-zh-cn_2.png)

该命令会改变SCTP通信缓存的使用方式，触发SGP进程内存占用率变化，影响S1接口和N2接口链路的接入。系统稳定运行场景下请慎用本功能。

**适用NF：SGSN、MME、AMF**

该命令用于设置系统中SCTP接收端缓冲区参数。设置参数时区分大缓冲区和小缓冲区，缓冲区分块规格包含max块、med块和min块。使用大缓冲区的接口有M3UA类、Diameter类、SBc、SGs和SLs；使用小缓冲区的接口有S1-MME和N2。SCTP会将接收到的报文根据大小存放到合适的块内。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-SCTPRXBUFFER]] · LST SCTPRXBUFFER
- [[command/UNC/20.15.2/SET-SCTPRXBUFFER]] · SET SCTPRXBUFFER

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SCTP接收缓冲区参数(LST-SCTPRXBUFFER)_50732715.md`
- 原始手册：`evidence/UNC/20.15.2/设置SCTP接收缓冲区参数(SET-SCTPRXBUFFER)_50932653.md`
