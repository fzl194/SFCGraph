---
id: UDG@20.15.2@ConfigObject@AFDNSCHECKTYPE
type: ConfigObject
name: AFDNSCHECKTYPE（需要进行防欺诈检查的DNS报文类型）
nf: UDG
version: 20.15.2
object_name: AFDNSCHECKTYPE
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# AFDNSCHECKTYPE（需要进行防欺诈检查的DNS报文类型）

## 说明

**适用NF：PGW-U、UPF**

该命令用于增加需要进行DNS防欺诈检查的DNS报文类型值，例如要对DNS头域“type”字段取值为10的DNS报文做防欺诈检查，则通过此命令增加type为10的记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-AFDNSCHECKTYPE]] · ADD AFDNSCHECKTYPE
- [[command/UDG/20.15.2/LST-AFDNSCHECKTYPE]] · LST AFDNSCHECKTYPE
- [[command/UDG/20.15.2/RMV-AFDNSCHECKTYPE]] · RMV AFDNSCHECKTYPE

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除需要进行防欺诈检查的DNS报文类型（RMV-AFDNSCHECKTYPE）_82837804.md`
- 原始手册：`evidence/UDG/20.15.2/增加需要进行防欺诈检查的DNS报文类型（ADD-AFDNSCHECKTYPE）_82837803.md`
- 原始手册：`evidence/UDG/20.15.2/查询需要进行防欺诈检查的DNS报文类型（LST-AFDNSCHECKTYPE）_82837805.md`
