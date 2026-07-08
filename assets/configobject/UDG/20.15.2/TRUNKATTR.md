---
id: UDG@20.15.2@ConfigObject@TRUNKATTR
type: ConfigObject
name: TRUNKATTR（宽带集群属性配置）
nf: UDG
version: 20.15.2
object_name: TRUNKATTR
object_kind: global_setting
applicable_nf:
- SGW-U
- PGW-U
status: active
---

# TRUNKATTR（宽带集群属性配置）

## 说明

**适用NF：SGW-U、PGW-U**

该命令用于控制是否对长时间处于空闲状态的集群用户进行去活处理，以及配置GTP-U消息头中是否携带Sequence Number字段。

## 操作本对象的命令

- [LST TRUNKATTR](command/UDG/20.15.2/LST-TRUNKATTR.md)
- [SET TRUNKATTR](command/UDG/20.15.2/SET-TRUNKATTR.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询宽带集群属性配置（LST-TRUNKATTR）_68962483.md`
- 原始手册：`evidence/UDG/20.15.2/设置宽带集群属性配置（SET-TRUNKATTR）_69122701.md`
