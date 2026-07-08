---
id: UNC@20.15.2@ConfigObject@NRRATVALUE
type: ConfigObject
name: NRRATVALUE（5G接入用户的RAT填写值）
nf: UNC
version: 20.15.2
object_name: NRRATVALUE
object_kind: global_setting
applicable_nf:
- SMF
- PGW-C
status: active
---

# NRRATVALUE（5G接入用户的RAT填写值）

## 说明

**适用NF：SMF、PGW-C**

设置5G用户接入时携带真实RAT（RAT参数取值为REALVALUE）时，RAT的真实取值根据SET/LST NRRATVALUE设置的命令进行携带。

## 操作本对象的命令

- [LST NRRATVALUE](command/UNC/20.15.2/LST-NRRATVALUE.md)
- [SET NRRATVALUE](command/UNC/20.15.2/SET-NRRATVALUE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G接入用户的RAT填写值（LST-NRRATVALUE）_52071370.md`
- 原始手册：`evidence/UNC/20.15.2/设置5G接入用户的RAT填写值（SET-NRRATVALUE）_52071376.md`
