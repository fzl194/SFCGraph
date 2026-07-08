---
id: UDG@20.15.2@ConfigObject@SPECIFICAPNVAL
type: ConfigObject
name: SPECIFICAPNVAL（用户APN与消息交互使用APN的映射关系）
nf: UDG
version: 20.15.2
object_name: SPECIFICAPNVAL
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# SPECIFICAPNVAL（用户APN与消息交互使用APN的映射关系）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用于新增用户使用的别名APN、虚拟APN或真实APN与交互消息中使用的指定的APN之间的映射关系。其中交互消息包括：头增强交互消息。在用户需要设置新的APN映射关系时使用该命令。

## 操作本对象的命令

- [ADD SPECIFICAPNVAL](command/UDG/20.15.2/ADD-SPECIFICAPNVAL.md)
- [LST SPECIFICAPNVAL](command/UDG/20.15.2/LST-SPECIFICAPNVAL.md)
- [MOD SPECIFICAPNVAL](command/UDG/20.15.2/MOD-SPECIFICAPNVAL.md)
- [RMV SPECIFICAPNVAL](command/UDG/20.15.2/RMV-SPECIFICAPNVAL.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改用户APN与消息交互使用APN的映射关系（MOD-SPECIFICAPNVAL）_07016801.md`
- 原始手册：`evidence/UDG/20.15.2/删除用户APN与消息交互使用APN的映射关系（RMV-SPECIFICAPNVAL）_07016802.md`
- 原始手册：`evidence/UDG/20.15.2/增加用户APN与消息交互使用APN的映射关系（ADD-SPECIFICAPNVAL）_07016800.md`
- 原始手册：`evidence/UDG/20.15.2/查询用户APN与消息交互使用APN的映射关系（LST-SPECIFICAPNVAL）_07016803.md`
