---
id: UNC@20.15.2@ConfigObject@HLRBPFAULTCODE
type: ConfigObject
name: HLRBPFAULTCODE（HLR BYPASS故障状态码）
nf: UNC
version: 20.15.2
object_name: HLRBPFAULTCODE
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# HLRBPFAULTCODE（HLR BYPASS故障状态码）

## 说明

**适用网元：SGSN**

本命令用于添加HLR BYPASS故障状态码配置。当希望HLR全故障后，系统收到HLR/DRA返回某个特定原因值时，用户进入HLR BYPASS状态，可通过此命令配置该原因值为HLR BYPASS原因值。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-HLRBPFAULTCODE]] · ADD HLRBPFAULTCODE
- [[command/UNC/20.15.2/LST-HLRBPFAULTCODE]] · LST HLRBPFAULTCODE
- [[command/UNC/20.15.2/RMV-HLRBPFAULTCODE]] · RMV HLRBPFAULTCODE

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除HLR-BYPASS故障状态码(RMV-HLRBPFAULTCODE)_04932762.md`
- 原始手册：`evidence/UNC/20.15.2/增加HLR-BYPASS故障状态码(ADD-HLRBPFAULTCODE)_04923686.md`
- 原始手册：`evidence/UNC/20.15.2/查询HLR-BYPASS故障状态码(LST-HLRBPFAULTCODE)_54937361.md`
