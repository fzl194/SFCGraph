---
id: UNC@20.15.2@ConfigObject@HTRIMSICFG
type: ConfigObject
name: HTRIMSICFG（HTR号段）
nf: UNC
version: 20.15.2
object_name: HTRIMSICFG
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# HTRIMSICFG（HTR号段）

## 说明

**适用网元：SGSN**

该命令用于添加一个HTR局向的具体IMSI号段。只有当HTROFC配置表中 “HTR局向索引” 对应的 “局向流控开关” 为 “YES” 时，本命令所配置的各个IMSI号段才进行流控，可执行 [**LST HTROFC**](../配置局向/查询HTR局向(LST HTROFC)_26305964.md) 进行查看。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-HTRIMSICFG]] · ADD HTRIMSICFG
- [[command/UNC/20.15.2/LST-HTRIMSICFG]] · LST HTRIMSICFG
- [[command/UNC/20.15.2/MOD-HTRIMSICFG]] · MOD HTRIMSICFG
- [[command/UNC/20.15.2/RMV-HTRIMSICFG]] · RMV HTRIMSICFG

## 证据

- 原始手册：`evidence/UNC/20.15.2/HTRIMSICFG.md`
- 原始手册：`evidence/UNC/20.15.2/HTRIMSICFG.md`
- 原始手册：`evidence/UNC/20.15.2/HTRIMSICFG.md`
- 原始手册：`evidence/UNC/20.15.2/HTRIMSICFG.md`
