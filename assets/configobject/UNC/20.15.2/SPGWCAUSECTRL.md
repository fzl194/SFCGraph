---
id: UNC@20.15.2@ConfigObject@SPGWCAUSECTRL
type: ConfigObject
name: SPGWCAUSECTRL（SGW-C/PGW-C原因值控制参数）
nf: UNC
version: 20.15.2
object_name: SPGWCAUSECTRL
object_kind: entity
applicable_nf:
- PGW-C
- SGW-C
status: active
---

# SPGWCAUSECTRL（SGW-C/PGW-C原因值控制参数）

## 说明

**适用NF：PGW-C、SGW-C**

该命令用于增加PGW-C或融合的SGW-C/PGW-C的原因值控制参数。当用户接入PGW-C或融合的SGW-C/PGW-C时，可通过该命令控制SM流程特殊场景下发送的原因值，以满足运营商实现对现网设备兼容性特殊控制的需求。

## 操作本对象的命令

- [ADD SPGWCAUSECTRL](command/UNC/20.15.2/ADD-SPGWCAUSECTRL.md)
- [LST SPGWCAUSECTRL](command/UNC/20.15.2/LST-SPGWCAUSECTRL.md)
- [MOD SPGWCAUSECTRL](command/UNC/20.15.2/MOD-SPGWCAUSECTRL.md)
- [RMV SPGWCAUSECTRL](command/UNC/20.15.2/RMV-SPGWCAUSECTRL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SGW-C_PGW-C原因值控制参数（MOD-SPGWCAUSECTRL）_09652982.md`
- 原始手册：`evidence/UNC/20.15.2/删除SGW-C_PGW-C原因值控制参数（RMV-SPGWCAUSECTRL）_09652355.md`
- 原始手册：`evidence/UNC/20.15.2/增加SGW-C_PGW-C原因值控制参数（ADD-SPGWCAUSECTRL）_09653621.md`
- 原始手册：`evidence/UNC/20.15.2/查询SGW-C_PGW-C原因值控制参数（LST-SPGWCAUSECTRL）_09652447.md`
