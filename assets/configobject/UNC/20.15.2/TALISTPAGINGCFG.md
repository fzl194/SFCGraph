---
id: UNC@20.15.2@ConfigObject@TALISTPAGINGCFG
type: ConfigObject
name: TALISTPAGINGCFG（TALIST寻呼不重发TAC区间）
nf: UNC
version: 20.15.2
object_name: TALISTPAGINGCFG
object_kind: entity
applicable_nf:
- MME
status: active
---

# TALISTPAGINGCFG（TALIST寻呼不重发TAC区间）

## 说明

**适用网元：MME**

该命令用于设置S1模式TALIST寻呼不重发的TAC区间。

当部分TAC下的eNodeB寻呼提前过载，则使用本命令进行TAC区间配置。通过判断当前用户所在TALIST的TAC是否在配置的ADD TALISTPAGINGCFG里面，如果TALIST中的任意一个TAC在，则用户基于TALIST寻呼不进行重发。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-TALISTPAGINGCFG]] · ADD TALISTPAGINGCFG
- [[command/UNC/20.15.2/LST-TALISTPAGINGCFG]] · LST TALISTPAGINGCFG
- [[command/UNC/20.15.2/RMV-TALISTPAGINGCFG]] · RMV TALISTPAGINGCFG

## 证据

- 原始手册：`evidence/UNC/20.15.2/TALISTPAGINGCFG.md`
- 原始手册：`evidence/UNC/20.15.2/TALISTPAGINGCFG.md`
- 原始手册：`evidence/UNC/20.15.2/TALISTPAGINGCFG.md`
