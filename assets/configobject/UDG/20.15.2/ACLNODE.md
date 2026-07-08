---
id: UDG@20.15.2@ConfigObject@ACLNODE
type: ConfigObject
name: ACLNODE（ACL节点）
nf: UDG
version: 20.15.2
object_name: ACLNODE
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# ACLNODE（ACL节点）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

![](增加ACL节点（ADD ACLNODE）_82837729.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致性能下降明显，请谨慎使用并联系华为技术支持协助操作。

该命令用于增加ACL节点，即配置filter过滤条件及对应的动作。配置完的ACL节点将作为ACL的一个配置项。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-ACLNODE]] · ADD ACLNODE
- [[command/UDG/20.15.2/LST-ACLNODE]] · LST ACLNODE
- [[command/UDG/20.15.2/MOD-ACLNODE]] · MOD ACLNODE
- [[command/UDG/20.15.2/RMV-ACLNODE]] · RMV ACLNODE

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改ACL节点（MOD-ACLNODE）_86526702.md`
- 原始手册：`evidence/UDG/20.15.2/删除ACL节点（RMV-ACLNODE）_82837731.md`
- 原始手册：`evidence/UDG/20.15.2/增加ACL节点（ADD-ACLNODE）_82837729.md`
- 原始手册：`evidence/UDG/20.15.2/查询ACL节点（LST-ACLNODE）_86526723.md`
