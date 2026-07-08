---
id: UDG@20.15.2@ConfigObject@ACLDEFAULT
type: ConfigObject
name: ACLDEFAULT（缺省Acl绑定）
nf: UDG
version: 20.15.2
object_name: ACLDEFAULT
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
identifier_parameters:
- DIRECTION
status: active
---

# ACLDEFAULT（缺省Acl绑定）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用于增加默认的ACL。默认ACL是在APN下没有配置任何ACL时，如果APN需要使用ACL，则会使用默认ACL。

## 操作本对象的命令

- [ADD ACLDEFAULT](command/UDG/20.15.2/ADD-ACLDEFAULT.md)
- [LST ACLDEFAULT](command/UDG/20.15.2/LST-ACLDEFAULT.md)
- [MOD ACLDEFAULT](command/UDG/20.15.2/MOD-ACLDEFAULT.md)
- [RMV ACLDEFAULT](command/UDG/20.15.2/RMV-ACLDEFAULT.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改缺省Acl绑定（MOD-ACLDEFAULT）_82837740.md`
- 原始手册：`evidence/UDG/20.15.2/删除缺省Acl绑定（RMV-ACLDEFAULT）_82837741.md`
- 原始手册：`evidence/UDG/20.15.2/增加缺省Acl绑定（ADD-ACLDEFAULT）_82837739.md`
- 原始手册：`evidence/UDG/20.15.2/查询缺省Acl绑定（LST-ACLDEFAULT）_82837742.md`
