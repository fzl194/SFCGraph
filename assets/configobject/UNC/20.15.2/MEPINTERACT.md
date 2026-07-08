---
id: UNC@20.15.2@ConfigObject@MEPINTERACT
type: ConfigObject
name: MEPINTERACT（MEP_SMF联动功能开关）
nf: UNC
version: 20.15.2
object_name: MEPINTERACT
object_kind: global_setting
applicable_nf:
- SMF
status: active
---

# MEPINTERACT（MEP_SMF联动功能开关）

## 说明

**适用NF：SMF**

该命令用来控制MEP_SMF联动处理，使能开关时，SMF向MEP订阅并接受MEP推送的分流规则和DNS重定向规则，去使能开关时，SMF向MEP去订阅。

## 操作本对象的命令

- [LST MEPINTERACT](command/UNC/20.15.2/LST-MEPINTERACT.md)
- [SET MEPINTERACT](command/UNC/20.15.2/SET-MEPINTERACT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询MEP_SMF联动功能开关（LST-MEPINTERACT）_09652273.md`
- 原始手册：`evidence/UNC/20.15.2/设置MEP_SMF联动功能开关（SET-MEPINTERACT）_09652370.md`
