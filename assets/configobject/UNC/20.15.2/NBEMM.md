---
id: UNC@20.15.2@ConfigObject@NBEMM
type: ConfigObject
name: NBEMM（NB-S1模式MM协议参数）
nf: UNC
version: 20.15.2
object_name: NBEMM
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# NBEMM（NB-S1模式MM协议参数）

## 说明

**适用网元：MME**

该命令用于设置NB-S1模式MM（Mobility Management）协议参数。

当网络中有NB终端处于无线信号覆盖较差的区域导致业务流程成功率较低时，需调大定时器时长以改善业务成功率。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-NBEMM]] · LST NBEMM
- [[command/UNC/20.15.2/SET-NBEMM]] · SET NBEMM

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NB-S1模式MM协议参数（LST-NBEMM）_72345375.md`
- 原始手册：`evidence/UNC/20.15.2/设置NB-S1模式MM协议参数（SET-NBEMM）_26305584.md`
