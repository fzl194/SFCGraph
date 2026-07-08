---
id: UNC@20.15.2@ConfigObject@SELCHFGBIMSISEG
type: ConfigObject
name: SELCHFGBIMSISEG（IMSI号段与CHF组的绑定关系）
nf: UNC
version: 20.15.2
object_name: SELCHFGBIMSISEG
object_kind: entity
applicable_nf:
- PGW-C
- SMF
- GGSN
status: active
---

# SELCHFGBIMSISEG（IMSI号段与CHF组的绑定关系）

## 说明

**适用NF：PGW-C、SMF、GGSN**

该命令用于增加IMSI号段与CHF组的绑定关系。SMF选择NCG/CHF时，可基于指定的IMSI号段选择CHF组，将不同IMSI号段的用户的计费信息送到不同NCG/CHF组。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SELCHFGBIMSISEG]] · ADD SELCHFGBIMSISEG
- [[command/UNC/20.15.2/LST-SELCHFGBIMSISEG]] · LST SELCHFGBIMSISEG
- [[command/UNC/20.15.2/MOD-SELCHFGBIMSISEG]] · MOD SELCHFGBIMSISEG
- [[command/UNC/20.15.2/RMV-SELCHFGBIMSISEG]] · RMV SELCHFGBIMSISEG

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IMSI号段与CHF组的绑定关系（MOD-SELCHFGBIMSISEG）_58190040.md`
- 原始手册：`evidence/UNC/20.15.2/删除IMSI号段与CHF组的绑定关系（RMV-SELCHFGBIMSISEG）_58110152.md`
- 原始手册：`evidence/UNC/20.15.2/增加IMSI号段与CHF组的绑定关系（ADD-SELCHFGBIMSISEG）_05630193.md`
- 原始手册：`evidence/UNC/20.15.2/查询IMSI号段和该号段绑定的主备CHF组（LST-SELCHFGBIMSISEG）_58229980.md`
