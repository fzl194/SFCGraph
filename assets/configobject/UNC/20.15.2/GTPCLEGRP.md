---
id: UNC@20.15.2@ConfigObject@GTPCLEGRP
type: ConfigObject
name: GTPCLEGRP（GTP-C本地实体组）
nf: UNC
version: 20.15.2
object_name: GTPCLEGRP
object_kind: entity
applicable_nf:
- SGW-C
- PGW-C
- AMF
- GGSN
status: active
---

# GTPCLEGRP（GTP-C本地实体组）

## 说明

**适用NF：SGW-C、PGW-C、AMF、GGSN**

该命令用于增加一个GTP-C本地实体组，一个实体组内可以包含多个实体，便于管理。实体组配合ADD GTPCLEGRPMEM使用生成WLR路由。

## 操作本对象的命令

- [ADD GTPCLEGRP](command/UNC/20.15.2/ADD-GTPCLEGRP.md)
- [LST GTPCLEGRP](command/UNC/20.15.2/LST-GTPCLEGRP.md)
- [MOD GTPCLEGRP](command/UNC/20.15.2/MOD-GTPCLEGRP.md)
- [RMV GTPCLEGRP](command/UNC/20.15.2/RMV-GTPCLEGRP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改GTP-C本地实体组（MOD-GTPCLEGRP）_09653033.md`
- 原始手册：`evidence/UNC/20.15.2/删除GTP-C本地实体组（RMV-GTPCLEGRP）_09653192.md`
- 原始手册：`evidence/UNC/20.15.2/增加GTP-C本地实体组（ADD-GTPCLEGRP）_09651623.md`
- 原始手册：`evidence/UNC/20.15.2/查询GTP-C本地实体组（LST-GTPCLEGRP）_09653069.md`
