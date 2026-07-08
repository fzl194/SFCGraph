---
id: UNC@20.15.2@ConfigObject@DMLE
type: ConfigObject
name: DMLE（Diameter本端实体）
nf: UNC
version: 20.15.2
object_name: DMLE
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# DMLE（Diameter本端实体）

## 说明

**适用网元：SGSN、MME**

该命令用于增加Diameter链路本端实体信息。Diameter协议用于支持MME与HSS（Home Subscriber Server）传递签约及鉴权数据；或用于检查MME与EIR（Equipment Identity Register）用户设备标识是否合法，以授权用户接入EPS（Evolved Packet System）网络。

## 操作本对象的命令

- [ADD DMLE](command/UNC/20.15.2/ADD-DMLE.md)
- [DSP DMLE](command/UNC/20.15.2/DSP-DMLE.md)
- [LST DMLE](command/UNC/20.15.2/LST-DMLE.md)
- [MOD DMLE](command/UNC/20.15.2/MOD-DMLE.md)
- [RMV DMLE](command/UNC/20.15.2/RMV-DMLE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Diameter本端实体(MOD-DMLE)_72225961.md`
- 原始手册：`evidence/UNC/20.15.2/删除Diameter本端实体(RMV-DMLE)_26146282.md`
- 原始手册：`evidence/UNC/20.15.2/增加Diameter本端实体(ADD-DMLE)_72345881.md`
- 原始手册：`evidence/UNC/20.15.2/显示Diameter本端实体(DSP-DMLE)_72345883.md`
- 原始手册：`evidence/UNC/20.15.2/查询Diameter本端实体(LST-DMLE)_26306094.md`
