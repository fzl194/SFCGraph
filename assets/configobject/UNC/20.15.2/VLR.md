---
id: UNC@20.15.2@ConfigObject@VLR
type: ConfigObject
name: VLR（VLR配置信息）
nf: UNC
version: 20.15.2
object_name: VLR
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# VLR（VLR配置信息）

## 说明

**适用网元：SGSN、MME**

增加一个与本局 UNC 相连的VLR。

此命令有一个参数POOLNM，POOLNM唯一标识一个MSC POOL。MSC POOL的作用是将多个MSC组成一个POOL，当POOL中某个MSC不可用的时候，可以将此MSC上的用户迁移到POOL中其他的MSC上。

## 操作本对象的命令

- [ADD VLR](command/UNC/20.15.2/ADD-VLR.md)
- [DSP VLR](command/UNC/20.15.2/DSP-VLR.md)
- [LST VLR](command/UNC/20.15.2/LST-VLR.md)
- [MOD VLR](command/UNC/20.15.2/MOD-VLR.md)
- [RMV VLR](command/UNC/20.15.2/RMV-VLR.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改VLR配置信息(MOD-VLR)_26145444.md`
- 原始手册：`evidence/UNC/20.15.2/删除VLR配置信息(RMV-VLR)_72345041.md`
- 原始手册：`evidence/UNC/20.15.2/增加VLR配置信息(ADD-VLR)_26305254.md`
- 原始手册：`evidence/UNC/20.15.2/显示VLR迁移进度(DSP-VLR)_26305256.md`
- 原始手册：`evidence/UNC/20.15.2/查询VLR配置信息(LST-VLR)_72225125.md`
