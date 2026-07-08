---
id: UDG@20.15.2@ConfigObject@POOLGRPMAP
type: ConfigObject
name: POOLGRPMAP（地址池组映射关系）
nf: UDG
version: 20.15.2
object_name: POOLGRPMAP
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# POOLGRPMAP（地址池组映射关系）

## 说明

**适用NF：PGW-U、UPF**

该命令用于添加TAC-Group/LAC-Group、APN、SMF到地址池组的映射规则。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-POOLGRPMAP]] · ADD POOLGRPMAP
- [[command/UDG/20.15.2/LST-POOLGRPMAP]] · LST POOLGRPMAP
- [[command/UDG/20.15.2/RMV-POOLGRPMAP]] · RMV POOLGRPMAP

## 关联对象

- [[configobject/UDG/20.15.2/APN]] · APN
- [[configobject/UDG/20.15.2/LACGROUP]] · LACGROUP
- [[configobject/UDG/20.15.2/POOLGROUP]] · POOLGROUP
- [[configobject/UDG/20.15.2/TACGROUP]] · TACGROUP

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示地址池组映射关系（LST-POOLGRPMAP）_82837150.md`
- 原始手册：`evidence/UDG/20.15.2/添加地址池组映射关系（ADD-POOLGRPMAP）_82837148.md`
- 原始手册：`evidence/UDG/20.15.2/移除地址池组映射关系（RMV-POOLGRPMAP）_82837149.md`
