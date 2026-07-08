---
id: UNC@20.15.2@ConfigObject@BLACKLIST
type: ConfigObject
name: BLACKLIST（黑名单地址列表）
nf: UNC
version: 20.15.2
object_name: BLACKLIST
object_kind: entity
applicable_nf:
- PGW-C
- SMF
- GGSN
status: active
---

# BLACKLIST（黑名单地址列表）

## 说明

**适用NF：PGW-C、SMF、GGSN**

该命令用于将指定的IP地址段设置为黑名单，禁止携带该地址段内IP地址的用户入网。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-BLACKLIST]] · ADD BLACKLIST
- [[command/UNC/20.15.2/LST-BLACKLIST]] · LST BLACKLIST
- [[command/UNC/20.15.2/RMV-BLACKLIST]] · RMV BLACKLIST

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除黑名单地址列表（RMV-BLACKLIST）_44007543.md`
- 原始手册：`evidence/UNC/20.15.2/增加黑名单地址列表（ADD-BLACKLIST）_44006355.md`
- 原始手册：`evidence/UNC/20.15.2/查询黑名单地址列表（LST-BLACKLIST）_44006827.md`
