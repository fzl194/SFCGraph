---
id: UNC@20.15.2@ConfigObject@ACLGROUP
type: ConfigObject
name: ACLGROUP（ACL规则匹配计数）
nf: UNC
version: 20.15.2
object_name: ACLGROUP
object_kind: entity
status: active
---

# ACLGROUP（ACL规则匹配计数）

## 说明

该命令用于增加ACL规则组。ACL是一种IP包过滤技术，通过对IP报文的源地址/通配位、报文目的地址/通配位、协议号、源端口号、目的端口号（上述5个字段一般称为五元组，其中源端口号和目的端口号只对TCP和UDP协议有作用）等信息对照ACL规则进行匹配，符合某一规则集合的数据包视为同一数据流，将按照ACL规则集合中规定的动作采取相同的处理策略，其动作包括允许（Permit）、拒绝（Deny）等。使用ACL技术时，需要先配置ACL规则组。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-ACLGROUP]] · ADD ACLGROUP
- [[command/UNC/20.15.2/LST-ACLGROUP]] · LST ACLGROUP
- [[command/UNC/20.15.2/MOD-ACLGROUP]] · MOD ACLGROUP
- [[command/UNC/20.15.2/RMV-ACLGROUP]] · RMV ACLGROUP
- [[command/UNC/20.15.2/RTR-ACLGROUP]] · RTR ACLGROUP

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除ACL规则匹配计数（RTR-ACLGROUP）_49801670.md`
- 原始手册：`evidence/UNC/20.15.2/修改ACL规则组（MOD-ACLGROUP）_49961874.md`
- 原始手册：`evidence/UNC/20.15.2/删除ACL规则组（RMV-ACLGROUP）_50280806.md`
- 原始手册：`evidence/UNC/20.15.2/增加ACL规则组（ADD-ACLGROUP）_50280682.md`
- 原始手册：`evidence/UNC/20.15.2/查询ACL规则组配置（LST-ACLGROUP）_00841277.md`
