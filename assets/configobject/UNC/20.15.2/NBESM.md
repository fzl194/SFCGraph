---
id: UNC@20.15.2@ConfigObject@NBESM
type: ConfigObject
name: NBESM（NB-S1模式SM协议参数）
nf: UNC
version: 20.15.2
object_name: NBESM
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# NBESM（NB-S1模式SM协议参数）

## 说明

**适用网元：MME**

该命令用于设置NB-S1模式SM（Session Management）协议参数。

当网络中有NB终端处于无线信号覆盖较差的区域导致业务流程成功率较低时，需调大定时器时长以改善业务成功率。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-NBESM]] · LST NBESM
- [[command/UNC/20.15.2/SET-NBESM]] · SET NBESM

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NB-S1模式SM协议参数（LST-NBESM）_26305586.md`
- 原始手册：`evidence/UNC/20.15.2/设置NB-S1模式SM协议参数（SET-NBESM）_72225455.md`
