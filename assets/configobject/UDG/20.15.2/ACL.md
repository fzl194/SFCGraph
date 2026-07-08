---
id: UDG@20.15.2@ConfigObject@ACL
type: ConfigObject
name: ACL
nf: UDG
version: 20.15.2
object_name: ACL
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
identifier_parameters:
- ACLNAME
status: active
---

# ACL

## 说明

**适用NF：SGW-U、PGW-U、UPF**

![](增加ACL（ADD ACL）_82837747.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致性能下降明显，请谨慎使用并联系华为技术支持协助操作。

该命令用于有新的增加ACL需求情况下增加ACL名称及ACL节点的匹配方式。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-ACL]] · ADD ACL
- [[command/UDG/20.15.2/LST-ACL]] · LST ACL
- [[command/UDG/20.15.2/MOD-ACL]] · MOD ACL
- [[command/UDG/20.15.2/RMV-ACL]] · RMV ACL

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改ACL（MOD-ACL）_86526661.md`
- 原始手册：`evidence/UDG/20.15.2/删除ACL（RMV-ACL）_82837749.md`
- 原始手册：`evidence/UDG/20.15.2/增加ACL（ADD-ACL）_82837747.md`
- 原始手册：`evidence/UDG/20.15.2/查询ACL（LST-ACL）_82837750.md`
