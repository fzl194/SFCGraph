---
id: UNC@20.15.2@ConfigObject@SMFADDRLOCWL
type: ConfigObject
name: SMFADDRLOCWL（位置区域地址分配用户白名单）
nf: UNC
version: 20.15.2
object_name: SMFADDRLOCWL
object_kind: entity
applicable_nf:
- PGW-C
- SMF
- GGSN
status: active
---

# SMFADDRLOCWL（位置区域地址分配用户白名单）

## 说明

**适用NF：PGW-C、SMF、GGSN**

该命令用于增加位置区域地址分配用户白名单，加入白名单的用户不受基于位置地址分配开关控制，不基于位置区域分配地址，即针对该用户，SET IPALLOCBYLOCSW命令中的SWITCH参数相当于DISABLE。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SMFADDRLOCWL]] · ADD SMFADDRLOCWL
- [[command/UNC/20.15.2/LST-SMFADDRLOCWL]] · LST SMFADDRLOCWL
- [[command/UNC/20.15.2/RMV-SMFADDRLOCWL]] · RMV SMFADDRLOCWL

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除位置区域地址分配用户白名单（RMV-SMFADDRLOCWL）_35636463.md`
- 原始手册：`evidence/UNC/20.15.2/增加位置区域地址分配用户白名单（ADD-SMFADDRLOCWL）_35273615.md`
- 原始手册：`evidence/UNC/20.15.2/查询位置区域地址分配用户白名单（LST-SMFADDRLOCWL）_35636457.md`
