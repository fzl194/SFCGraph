---
id: UNC@20.15.2@ConfigObject@CHGDCHAR
type: ConfigObject
name: CHGDCHAR（缺省计费属性参数）
nf: UNC
version: 20.15.2
object_name: CHGDCHAR
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# CHGDCHAR（缺省计费属性参数）

## 说明

**适用网元：SGSN**

该命令用于增加缺省计费属性参数。缺省计费属性是指当外网用户签约的HLR没有为外网用户指定计费属性时，SGSN将会按照该外网用户的MCC和MNC对应的缺省计费方式对该外网用户实施计费。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-CHGDCHAR]] · ADD CHGDCHAR
- [[command/UNC/20.15.2/LST-CHGDCHAR]] · LST CHGDCHAR
- [[command/UNC/20.15.2/RMV-CHGDCHAR]] · RMV CHGDCHAR

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除缺省计费属性参数(RMV-CHGDCHAR)_72225061.md`
- 原始手册：`evidence/UNC/20.15.2/增加缺省计费属性参数(ADD-CHGDCHAR)_26145380.md`
- 原始手册：`evidence/UNC/20.15.2/查询缺省计费属性参数(LST-CHGDCHAR)_26305196.md`
