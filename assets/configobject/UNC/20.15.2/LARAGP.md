---
id: UNC@20.15.2@ConfigObject@LARAGP
type: ConfigObject
name: LARAGP（位置区群组）
nf: UNC
version: 20.15.2
object_name: LARAGP
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# LARAGP（位置区群组）

## 说明

**适用网元：SGSN**

此命令用于增加位置区和路由区的区域群记录，为区域群成员提供区域群标识，同一个区域群中的成员具有相同的接入控制策略。

如果需要对多个区域采用相同的接入控制策略时，需要执行此命令。

## 操作本对象的命令

- [ADD LARAGP](command/UNC/20.15.2/ADD-LARAGP.md)
- [LST LARAGP](command/UNC/20.15.2/LST-LARAGP.md)
- [MOD LARAGP](command/UNC/20.15.2/MOD-LARAGP.md)
- [RMV LARAGP](command/UNC/20.15.2/RMV-LARAGP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改位置区群组(MOD-LARAGP)_26145482.md`
- 原始手册：`evidence/UNC/20.15.2/删除位置区群组(RMV-LARAGP)_72345079.md`
- 原始手册：`evidence/UNC/20.15.2/增加位置区群组(ADD-LARAGP)_26305292.md`
- 原始手册：`evidence/UNC/20.15.2/查询位置区群组(LST-LARAGP)_72225163.md`
