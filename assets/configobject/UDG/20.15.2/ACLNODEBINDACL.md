---
id: UDG@20.15.2@ConfigObject@ACLNODEBINDACL
type: ConfigObject
name: ACLNODEBINDACL（Acl节点绑定关系）
nf: UDG
version: 20.15.2
object_name: ACLNODEBINDACL
object_kind: binding
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# ACLNODEBINDACL（Acl节点绑定关系）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用于增加ACL节点和ACL的绑定关系。

基于APN做ACL业务控制的场景，需要将ACL节点绑定到ACL下，再将ACL绑定到APN下。这样用户接入在该APN下时，就可以使用ACL节点下配置的策略进行业务控制。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-ACLNODEBINDACL]] · ADD ACLNODEBINDACL
- [[command/UDG/20.15.2/LST-ACLNODEBINDACL]] · LST ACLNODEBINDACL
- [[command/UDG/20.15.2/MOD-ACLNODEBINDACL]] · MOD ACLNODEBINDACL
- [[command/UDG/20.15.2/RMV-ACLNODEBINDACL]] · RMV ACLNODEBINDACL

## 证据

- 原始手册：`evidence/UDG/20.15.2/ACLNODEBINDACL.md`
- 原始手册：`evidence/UDG/20.15.2/ACLNODEBINDACL.md`
- 原始手册：`evidence/UDG/20.15.2/ACLNODEBINDACL.md`
- 原始手册：`evidence/UDG/20.15.2/ACLNODEBINDACL.md`
