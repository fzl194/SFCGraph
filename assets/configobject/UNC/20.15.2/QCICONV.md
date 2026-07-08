---
id: UNC@20.15.2@ConfigObject@QCICONV
type: ConfigObject
name: QCICONV（扩展QCI转换关系）
nf: UNC
version: 20.15.2
object_name: QCICONV
object_kind: entity
applicable_nf:
- MME
status: active
---

# QCICONV（扩展QCI转换关系）

## 说明

**适用网元：MME**

该命令用于增加扩展QCI（QoS Class Identifier）向标准QCI的转换关系配置表。扩展QCI是指取值大于9并小于255的QCI，当UE不支持扩展QCI时，则需要将扩展QCI转换为标准QCI（取值为1～9）。

当在承载创建和承载修改的流程中，会对QCI的值进行标准化转换。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-QCICONV]] · ADD QCICONV
- [[command/UNC/20.15.2/LST-QCICONV]] · LST QCICONV
- [[command/UNC/20.15.2/MOD-QCICONV]] · MOD QCICONV
- [[command/UNC/20.15.2/RMV-QCICONV]] · RMV QCICONV

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改扩展QCI转换关系(MOD-QCICONV)_72345813.md`
- 原始手册：`evidence/UNC/20.15.2/删除扩展QCI转换关系(RMV-QCICONV)_26146214.md`
- 原始手册：`evidence/UNC/20.15.2/增加扩展QCI转换关系(ADD-QCICONV)_26306024.md`
- 原始手册：`evidence/UNC/20.15.2/查询扩展QCI转换关系(LST-QCICONV)_72225893.md`
