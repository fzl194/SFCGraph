---
id: UNC@20.15.2@ConfigObject@PSCSIMSI
type: ConfigObject
name: PSCSIMSI（联合接入IMSI白名单）
nf: UNC
version: 20.15.2
object_name: PSCSIMSI
object_kind: entity
applicable_nf:
- MME
status: active
---

# PSCSIMSI（联合接入IMSI白名单）

## 说明

**适用网元：MME**

该命令用于增加联合接入IMSI白名单。当 [SET PSCSPLCY](设置联合接入策略(SET PSCSPLCY)_31833948.md) 中SUBPLCY参数设置为IMSI_IDENT时需要通过本命令添加白名单中的用户。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PSCSIMSI]] · ADD PSCSIMSI
- [[command/UNC/20.15.2/LST-PSCSIMSI]] · LST PSCSIMSI
- [[command/UNC/20.15.2/RMV-PSCSIMSI]] · RMV PSCSIMSI

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除联合接入IMSI白名单(RMV-PSCSIMSI)_86673117.md`
- 原始手册：`evidence/UNC/20.15.2/增加联合接入IMSI白名单(ADD-PSCSIMSI)_36193194.md`
- 原始手册：`evidence/UNC/20.15.2/查询联合接入IMSI白名单(LST-PSCSIMSI)_86793085.md`
