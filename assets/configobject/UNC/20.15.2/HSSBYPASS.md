---
id: UNC@20.15.2@ConfigObject@HSSBYPASS
type: ConfigObject
name: HSSBYPASS（HSS故障Bypass功能控制参数）
nf: UNC
version: 20.15.2
object_name: HSSBYPASS
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# HSSBYPASS（HSS故障Bypass功能控制参数）

## 说明

**适用网元：MME**

该命令用于设置HSS故障Bypass功能控制参数。开启HSS全故障智能业务逃生功能开关后，在HSS全故障状态下业务可以惯性运行。

## 操作本对象的命令

- [LST HSSBYPASS](command/UNC/20.15.2/LST-HSSBYPASS.md)
- [SET HSSBYPASS](command/UNC/20.15.2/SET-HSSBYPASS.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询HSS故障Bypass功能控制参数(LST-HSSBYPASS)_09911473.md`
- 原始手册：`evidence/UNC/20.15.2/设置HSS故障Bypass功能控制参数(SET-HSSBYPASS)_62871280.md`
