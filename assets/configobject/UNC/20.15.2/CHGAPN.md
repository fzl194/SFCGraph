---
id: UNC@20.15.2@ConfigObject@CHGAPN
type: ConfigObject
name: CHGAPN（APN计费属性）
nf: UNC
version: 20.15.2
object_name: CHGAPN
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# CHGAPN（APN计费属性）

## 说明

**适用网元：SGSN**

该命令用于当要求忽略HLR签约的APN计费属性时（通过命令 [**SET CHGCDR**](../计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md) 设置参数 “IGNOREFLG” 的取值），配置基于APN的计费属性信息。

## 操作本对象的命令

- [ADD CHGAPN](command/UNC/20.15.2/ADD-CHGAPN.md)
- [LST CHGAPN](command/UNC/20.15.2/LST-CHGAPN.md)
- [MOD CHGAPN](command/UNC/20.15.2/MOD-CHGAPN.md)
- [RMV CHGAPN](command/UNC/20.15.2/RMV-CHGAPN.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改APN计费属性(MOD-CHGAPN)_72225045.md`
- 原始手册：`evidence/UNC/20.15.2/删除APN计费属性(RMV-CHGAPN)_26145364.md`
- 原始手册：`evidence/UNC/20.15.2/增加APN计费属性(ADD-CHGAPN)_72344965.md`
- 原始手册：`evidence/UNC/20.15.2/查询APN计费属性(LST-CHGAPN)_26305180.md`
