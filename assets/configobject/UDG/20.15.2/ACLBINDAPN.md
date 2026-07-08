---
id: UDG@20.15.2@ConfigObject@ACLBINDAPN
type: ConfigObject
name: ACLBINDAPN（Acl绑定关系）
nf: UDG
version: 20.15.2
object_name: ACLBINDAPN
object_kind: binding
applicable_nf:
- SGW-U
- PGW-U
- UPF
identifier_parameters:
- APN
- DIRECTION
status: active
---

# ACLBINDAPN（Acl绑定关系）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用于增加对于APN，数据流四个方向的ACL绑定规则的配置。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-ACLBINDAPN]] · ADD ACLBINDAPN
- [[command/UDG/20.15.2/LST-ACLBINDAPN]] · LST ACLBINDAPN
- [[command/UDG/20.15.2/MOD-ACLBINDAPN]] · MOD ACLBINDAPN
- [[command/UDG/20.15.2/RMV-ACLBINDAPN]] · RMV ACLBINDAPN

## 关联对象

- [[configobject/UDG/20.15.2/APN]] · APN

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改Acl绑定关系（MOD-ACLBINDAPN）_82837725.md`
- 原始手册：`evidence/UDG/20.15.2/删除Acl绑定关系（RMV-ACLBINDAPN）_82837726.md`
- 原始手册：`evidence/UDG/20.15.2/增加Acl绑定关系（ADD-ACLBINDAPN）_82837724.md`
- 原始手册：`evidence/UDG/20.15.2/查询Acl绑定关系（LST-ACLBINDAPN）_82837727.md`
