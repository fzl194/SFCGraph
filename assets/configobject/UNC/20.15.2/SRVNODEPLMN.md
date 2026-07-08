---
id: UNC@20.15.2@ConfigObject@SRVNODEPLMN
type: ConfigObject
name: SRVNODEPLMN（SGSN/SGW/PGW地址段和PLMN标识之间的映射关系）
nf: UNC
version: 20.15.2
object_name: SRVNODEPLMN
object_kind: entity
applicable_nf:
- PGW-C
- SGW-C
- GGSN
status: active
---

# SRVNODEPLMN（SGSN/SGW/PGW地址段和PLMN标识之间的映射关系）

## 说明

**适用NF：PGW-C、SGW-C、GGSN**

该命令用来配置SGSN/SGW/PGW IP与PLMN标识的映射关系表。在根据SGSN/SGW的IP地址映射PLMN时，需要用到映射表。获取SGSN/SGW/PGW PLMN标识用于判断用户的本地、漫游和拜访属性。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SRVNODEPLMN]] · ADD SRVNODEPLMN
- [[command/UNC/20.15.2/LST-SRVNODEPLMN]] · LST SRVNODEPLMN
- [[command/UNC/20.15.2/MOD-SRVNODEPLMN]] · MOD SRVNODEPLMN
- [[command/UNC/20.15.2/RMV-SRVNODEPLMN]] · RMV SRVNODEPLMN

## 证据

- 原始手册：`evidence/UNC/20.15.2/SRVNODEPLMN.md`
- 原始手册：`evidence/UNC/20.15.2/SRVNODEPLMN.md`
- 原始手册：`evidence/UNC/20.15.2/SRVNODEPLMN.md`
- 原始手册：`evidence/UNC/20.15.2/SRVNODEPLMN.md`
