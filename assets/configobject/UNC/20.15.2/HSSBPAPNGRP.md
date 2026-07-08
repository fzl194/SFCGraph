---
id: UNC@20.15.2@ConfigObject@HSSBPAPNGRP
type: ConfigObject
name: HSSBPAPNGRP（HSS BYPASS最小APN签约数据群组）
nf: UNC
version: 20.15.2
object_name: HSSBPAPNGRP
object_kind: entity
applicable_nf:
- MME
status: active
---

# HSSBPAPNGRP（HSS BYPASS最小APN签约数据群组）

## 说明

**适用网元：MME**

此命令用于新增HSS BYPASS最小APN签约数据群组。

用户处于HSS BYPASS状态之后，无法从HSS获取用户签约数据，如果系统内无用户历史签约数据，使用该命令手动配置用户最小APN签约数据群组，保证业务惯性运行。

## 操作本对象的命令

- [ADD HSSBPAPNGRP](command/UNC/20.15.2/ADD-HSSBPAPNGRP.md)
- [LST HSSBPAPNGRP](command/UNC/20.15.2/LST-HSSBPAPNGRP.md)
- [MOD HSSBPAPNGRP](command/UNC/20.15.2/MOD-HSSBPAPNGRP.md)
- [RMV HSSBPAPNGRP](command/UNC/20.15.2/RMV-HSSBPAPNGRP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改HSS-BYPASS最小APN签约数据群组-(MOD-HSSBPAPNGRP)_64021102.md`
- 原始手册：`evidence/UNC/20.15.2/删除HSS-BYPASS最小APN签约数据群组-(RMV-HSSBPAPNGRP)_11541145.md`
- 原始手册：`evidence/UNC/20.15.2/增加HSS-BYPASS最小APN签约数据群组-(ADD-HSSBPAPNGRP)_64181038.md`
- 原始手册：`evidence/UNC/20.15.2/查询HSS-BYPASS最小APN签约数据群组-(LST-HSSBPAPNGRP)_63701290.md`
