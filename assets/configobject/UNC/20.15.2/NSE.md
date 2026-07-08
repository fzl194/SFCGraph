---
id: UNC@20.15.2@ConfigObject@NSE
type: ConfigObject
name: NSE（信令实体）
nf: UNC
version: 20.15.2
object_name: NSE
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# NSE（信令实体）

## 说明

**适用网元：SGSN**

该命令用于增加一个网络服务实体（Network service Entity，NSE），在PCU侧新增一个NSE时，在SGSN要增加相应的NSE。信令实体分别位于BSS侧和SGSN侧，用于提供Gb接口操作所需的网络管理功能。请参考3GPP TS 48.016。

## 操作本对象的命令

- [ADD NSE](command/UNC/20.15.2/ADD-NSE.md)
- [DSP NSE](command/UNC/20.15.2/DSP-NSE.md)
- [LST NSE](command/UNC/20.15.2/LST-NSE.md)
- [MOD NSE](command/UNC/20.15.2/MOD-NSE.md)
- [RMV NSE](command/UNC/20.15.2/RMV-NSE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改信令实体(MOD-NSE)_26305838.md`
- 原始手册：`evidence/UNC/20.15.2/删除信令实体(RMV-NSE)_72225707.md`
- 原始手册：`evidence/UNC/20.15.2/增加信令实体(ADD-NSE)_26146028.md`
- 原始手册：`evidence/UNC/20.15.2/显示NSE属性信息（DSP-NSE）_26146030.md`
- 原始手册：`evidence/UNC/20.15.2/查询信令实体（LST-NSE）_72345629.md`
