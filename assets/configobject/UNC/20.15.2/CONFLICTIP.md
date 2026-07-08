---
id: UNC@20.15.2@ConfigObject@CONFLICTIP
type: ConfigObject
name: CONFLICTIP（冲突地址）
nf: UNC
version: 20.15.2
object_name: CONFLICTIP
object_kind: entity
applicable_nf:
- GGSN
- SMF
- PGW-C
status: active
---

# CONFLICTIP（冲突地址）

## 说明

**适用NF：GGSN、SMF、PGW-C**

该命令用于在本地地址池中标识指定地址为冲突状态。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-CONFLICTIP]] · ADD CONFLICTIP
- [[command/UNC/20.15.2/LST-CONFLICTIP]] · LST CONFLICTIP
- [[command/UNC/20.15.2/RMV-CONFLICTIP]] · RMV CONFLICTIP

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除冲突地址（RMV-CONFLICTIP）_64343901.md`
- 原始手册：`evidence/UNC/20.15.2/增加冲突地址（ADD-CONFLICTIP）_64343818.md`
- 原始手册：`evidence/UNC/20.15.2/查询冲突地址（LST-CONFLICTIP）_64343878.md`
