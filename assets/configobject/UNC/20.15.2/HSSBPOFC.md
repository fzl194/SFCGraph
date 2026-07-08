---
id: UNC@20.15.2@ConfigObject@HSSBPOFC
type: ConfigObject
name: HSSBPOFC（故障状态HSS）
nf: UNC
version: 20.15.2
object_name: HSSBPOFC
object_kind: entity
applicable_nf:
- MME
status: active
---

# HSSBPOFC（故障状态HSS）

## 说明

**适用网元：MME**

本命令用于添加故障状态HSS配置。当HSS处于全故障状态时，因特殊原因用户无法自动进入HSS BYPASS状态，可以通过该命令紧急触发用户进入HSS BYPASS状态。

## 操作本对象的命令

- [ADD HSSBPOFC](command/UNC/20.15.2/ADD-HSSBPOFC.md)
- [LST HSSBPOFC](command/UNC/20.15.2/LST-HSSBPOFC.md)
- [RMV HSSBPOFC](command/UNC/20.15.2/RMV-HSSBPOFC.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除故障状态HSS(RMV-HSSBPOFC)_21093317.md`
- 原始手册：`evidence/UNC/20.15.2/增加故障状态HSS(ADD-HSSBPOFC)_70093526.md`
- 原始手册：`evidence/UNC/20.15.2/查询故障状态HSS(LST-HSSBPOFC)_20653489.md`
