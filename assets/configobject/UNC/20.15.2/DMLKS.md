---
id: UNC@20.15.2@ConfigObject@DMLKS
type: ConfigObject
name: DMLKS（Diameter链路集配置）
nf: UNC
version: 20.15.2
object_name: DMLKS
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# DMLKS（Diameter链路集配置）

## 说明

**适用网元：SGSN、MME**

该命令用于增加一条Diameter链路集。Diameter链路集是MME与HSS之间的链路集，用来唯一关联一个本端与一个对端。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-DMLKS]] · ADD DMLKS
- [[command/UNC/20.15.2/DSP-DMLKS]] · DSP DMLKS
- [[command/UNC/20.15.2/LST-DMLKS]] · LST DMLKS
- [[command/UNC/20.15.2/MOD-DMLKS]] · MOD DMLKS
- [[command/UNC/20.15.2/RMV-DMLKS]] · RMV DMLKS

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Diameter链路集配置(MOD-DMLKS)_72345879.md`
- 原始手册：`evidence/UNC/20.15.2/删除Diameter链路集配置(RMV-DMLKS)_26306090.md`
- 原始手册：`evidence/UNC/20.15.2/增加Diameter链路集配置(ADD-DMLKS)_72225957.md`
- 原始手册：`evidence/UNC/20.15.2/显示Diameter链路集状态(DSP-DMLKS)_72225959.md`
- 原始手册：`evidence/UNC/20.15.2/查询Diameter链路集配置(LST-DMLKS)_26146280.md`
