---
id: UNC@20.15.2@ConfigObject@SPECIFICAPNVAL
type: ConfigObject
name: SPECIFICAPNVAL（用户APN与消息交互使用APN的映射关系）
nf: UNC
version: 20.15.2
object_name: SPECIFICAPNVAL
object_kind: entity
applicable_nf:
- SMF
- PGW-C
- GGSN
status: active
---

# SPECIFICAPNVAL（用户APN与消息交互使用APN的映射关系）

## 说明

**适用NF：SMF、PGW-C、GGSN**

该命令用于增加用户使用的APN与信令流程中使用的指定APN的映射关系。用户使用的APN包括：别名APN、虚拟APN或真实APN，信令流程包括：PCRF交互、PCF交互、CG话单、同AAA鉴权交互、计费交互以及同OCS和CHF交互。

## 操作本对象的命令

- [ADD SPECIFICAPNVAL](command/UNC/20.15.2/ADD-SPECIFICAPNVAL.md)
- [LST SPECIFICAPNVAL](command/UNC/20.15.2/LST-SPECIFICAPNVAL.md)
- [MOD SPECIFICAPNVAL](command/UNC/20.15.2/MOD-SPECIFICAPNVAL.md)
- [RMV SPECIFICAPNVAL](command/UNC/20.15.2/RMV-SPECIFICAPNVAL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改用户APN与消息交互使用APN的映射关系（MOD-SPECIFICAPNVAL）_09653218.md`
- 原始手册：`evidence/UNC/20.15.2/删除用户APN与消息交互使用APN的映射关系（RMV-SPECIFICAPNVAL）_09652261.md`
- 原始手册：`evidence/UNC/20.15.2/增加用户APN与消息交互使用APN的映射关系（ADD-SPECIFICAPNVAL）_09653027.md`
- 原始手册：`evidence/UNC/20.15.2/查询用户APN与消息交互使用APN的映射关系（LST-SPECIFICAPNVAL）_09653635.md`
