---
id: UNC@20.15.2@ConfigObject@INTPDUPLCY
type: ConfigObject
name: INTPDUPLCY（异网漫游PDU会话重建策略）
nf: UNC
version: 20.15.2
object_name: INTPDUPLCY
object_kind: entity
applicable_nf:
- AMF
status: active
---

# INTPDUPLCY（异网漫游PDU会话重建策略）

## 说明

**适用NF：AMF**

该命令用于增加异网漫游用户的PDU会话重建策略。异网漫游用户在拜访网络内跨POOL移动时，可能造成HR模式会话的V-SMF和H-SMF跨省且跨运营商交互。增加该配置后，AMF可以对指定范围内的用户在指定条件下重建会话，为UE重新选择在同一省份内的V-SMF和H-SMF。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-INTPDUPLCY]] · ADD INTPDUPLCY
- [[command/UNC/20.15.2/LST-INTPDUPLCY]] · LST INTPDUPLCY
- [[command/UNC/20.15.2/MOD-INTPDUPLCY]] · MOD INTPDUPLCY
- [[command/UNC/20.15.2/RMV-INTPDUPLCY]] · RMV INTPDUPLCY

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改异网漫游PDU会话重建策略（MOD-INTPDUPLCY）_63626149.md`
- 原始手册：`evidence/UNC/20.15.2/删除异网漫游PDU会话重建策略（RMV-INTPDUPLCY）_15146278.md`
- 原始手册：`evidence/UNC/20.15.2/增加异网漫游PDU会话重建策略（ADD-INTPDUPLCY）_15306282.md`
- 原始手册：`evidence/UNC/20.15.2/查询异网漫游PDU会话重建策略（LST-INTPDUPLCY）_63346301.md`
