---
id: UNC@20.15.2@ConfigObject@EMTCBEMM
type: ConfigObject
name: EMTCBEMM（S1模式eMTC MM协议参数）
nf: UNC
version: 20.15.2
object_name: EMTCBEMM
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# EMTCBEMM（S1模式eMTC MM协议参数）

## 说明

**适用网元：MME**

该命令用于设置S1模式CE Mode B(一种eMTC终端)用户的MM协议参数。

当网络中有CE Mode B终端处于无线信号覆盖较差的区域导致业务流程成功率较低时，可通过本命令调大定时器时长以改善业务成功率。

## 操作本对象的命令

- [LST EMTCBEMM](command/UNC/20.15.2/LST-EMTCBEMM.md)
- [SET EMTCBEMM](command/UNC/20.15.2/SET-EMTCBEMM.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询S1模式eMTC-MM协议参数（LST-EMTCBEMM）_72225457.md`
- 原始手册：`evidence/UNC/20.15.2/设置S1模式eMTC-MM协议参数（SET-EMTCBEMM）_26145778.md`
