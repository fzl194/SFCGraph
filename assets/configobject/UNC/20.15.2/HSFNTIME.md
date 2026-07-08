---
id: UNC@20.15.2@ConfigObject@HSFNTIME
type: ConfigObject
name: HSFNTIME（H-SFN参考时间）
nf: UNC
version: 20.15.2
object_name: HSFNTIME
object_kind: global_setting
applicable_nf:
- MME
- AMF
status: active
---

# HSFNTIME（H-SFN参考时间）

## 说明

**适用网元：MME、AMF**

此命令用于设置eDRX特性中H-SFN=0的参考时间，该参考时间用于与eNodeB/gNodeB对齐H-SFN为0的起始时间。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-HSFNTIME]] · LST HSFNTIME
- [[command/UNC/20.15.2/SET-HSFNTIME]] · SET HSFNTIME

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询H-SFN参考时间(LST-HSFNTIME)_72345371.md`
- 原始手册：`evidence/UNC/20.15.2/设置H-SFN参考时间(SET-HSFNTIME)_26305580.md`
