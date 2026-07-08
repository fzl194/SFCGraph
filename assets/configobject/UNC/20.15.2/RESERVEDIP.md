---
id: UNC@20.15.2@ConfigObject@RESERVEDIP
type: ConfigObject
name: RESERVEDIP（预留IP资源）
nf: UNC
version: 20.15.2
object_name: RESERVEDIP
object_kind: entity
applicable_nf:
- NCG
status: active
---

# RESERVEDIP（预留IP资源）

## 说明

**适用NF：NCG**

该命令用于IP资源预埋，以便新增RU后有IP资源可以迁移到新RU上，减少用户对接NCG新规划RU的工作 。

以下情况时，需要增加预留IP资源：

新开局只配置了少量RU，为后续扩容需要预埋IP资源。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-RESERVEDIP]] · ADD RESERVEDIP
- [[command/UNC/20.15.2/LST-RESERVEDIP]] · LST RESERVEDIP
- [[command/UNC/20.15.2/MOD-RESERVEDIP]] · MOD RESERVEDIP
- [[command/UNC/20.15.2/RMV-RESERVEDIP]] · RMV RESERVEDIP

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改预留IP资源（MOD-RESERVEDIP）_80629560.md`
- 原始手册：`evidence/UNC/20.15.2/删除预留IP资源（RMV-RESERVEDIP）_32789633.md`
- 原始手册：`evidence/UNC/20.15.2/增加预留IP资源（ADD-RESERVEDIP）_80594246.md`
- 原始手册：`evidence/UNC/20.15.2/查询预留IP资源（LST-RESERVEDIP）_80309656.md`
