---
id: UNC@20.15.2@ConfigObject@DMPE
type: ConfigObject
name: DMPE（Diameter对端实体）
nf: UNC
version: 20.15.2
object_name: DMPE
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# DMPE（Diameter对端实体）

## 说明

**适用网元：SGSN、MME**

该命令用于增加Diameter对端实体的配置。Diameter协议用于支持MME与HSS（Home Subscriber Server）传递签约及鉴权数据；或用于检查MME与EIR（Equipment Identity Register）用户设备标识是否合法，以授权用户接入EPS（Evolved Packet System）网络；或用于支持MME与DRA（Diameter Routing Agent）转接其他对端实体。

UNC 需增加的Diameter对端实体为HSS、EIR或DRA时，需要执行此命令。

## 操作本对象的命令

- [ADD DMPE](command/UNC/20.15.2/ADD-DMPE.md)
- [DSP DMPE](command/UNC/20.15.2/DSP-DMPE.md)
- [LST DMPE](command/UNC/20.15.2/LST-DMPE.md)
- [MOD DMPE](command/UNC/20.15.2/MOD-DMPE.md)
- [RMV DMPE](command/UNC/20.15.2/RMV-DMPE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Diameter对端实体(MOD-DMPE)_72345885.md`
- 原始手册：`evidence/UNC/20.15.2/删除Diameter对端实体(RMV-DMPE)_26306096.md`
- 原始手册：`evidence/UNC/20.15.2/增加Diameter对端实体(ADD-DMPE)_72225963.md`
- 原始手册：`evidence/UNC/20.15.2/显示Diameter对端实体(DSP-DMPE)_72225965.md`
- 原始手册：`evidence/UNC/20.15.2/查询Diameter对端实体(LST-DMPE)_26146286.md`
