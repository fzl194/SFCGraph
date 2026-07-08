---
id: UNC@20.15.2@ConfigObject@GULIWKPLCY
type: ConfigObject
name: GULIWKPLCY（GUL互操作本地策略）
nf: UNC
version: 20.15.2
object_name: GULIWKPLCY
object_kind: entity
applicable_nf:
- MME
status: active
---

# GULIWKPLCY（GUL互操作本地策略）

## 说明

**适用网元：MME**

- 此命令用于增加GUL互操作本地策略。该配置生效后会影响234G互操作相关指标。
- 该命令执行后不会对正在进行信令流程的用户立即生效，该命令中的限制会在用户的下一次信令流程中生效。

## 操作本对象的命令

- [ADD GULIWKPLCY](command/UNC/20.15.2/ADD-GULIWKPLCY.md)
- [LST GULIWKPLCY](command/UNC/20.15.2/LST-GULIWKPLCY.md)
- [MOD GULIWKPLCY](command/UNC/20.15.2/MOD-GULIWKPLCY.md)
- [RMV GULIWKPLCY](command/UNC/20.15.2/RMV-GULIWKPLCY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改GUL互操作本地策略-(MOD-GULIWKPLCY)_68470433.md`
- 原始手册：`evidence/UNC/20.15.2/删除GUL互操作本地策略-(RMV-GULIWKPLCY)_68230973.md`
- 原始手册：`evidence/UNC/20.15.2/增加GUL互操作本地策略-(ADD-GULIWKPLCY)_68175773.md`
- 原始手册：`evidence/UNC/20.15.2/查询GUL互操作本地策略-(LST-GULIWKPLCY)_68484737.md`
