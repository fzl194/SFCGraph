---
id: UDG@20.15.2@ConfigObject@PCCPOLICYGRP
type: ConfigObject
name: PCCPOLICYGRP（PCC策略组）
nf: UDG
version: 20.15.2
object_name: PCCPOLICYGRP
object_kind: entity
applicable_nf:
- PGW-U
- UPF
uniqueness_keys:
- - PCCPOLICYGRPNM
status: active
---

# PCCPOLICYGRP（PCC策略组）

## 说明

**适用NF：PGW-U、UPF**

此命令用于增加PCC策略组配置。可以通过命令，配置PCC策略组，包括使用量上报规则组、PCC动作属性、扩展属性等构成策略集，同时支持基于ServiceProp选择不同的非默认策略集。

## 操作本对象的命令

- [ADD PCCPOLICYGRP](command/UDG/20.15.2/ADD-PCCPOLICYGRP.md)
- [LST PCCPOLICYGRP](command/UDG/20.15.2/LST-PCCPOLICYGRP.md)
- [MOD PCCPOLICYGRP](command/UDG/20.15.2/MOD-PCCPOLICYGRP.md)
- [RMV PCCPOLICYGRP](command/UDG/20.15.2/RMV-PCCPOLICYGRP.md)

## 关联对象

- [EXTENDPROP](configobject/UDG/20.15.2/EXTENDPROP.md)
- [PCCACTIONPROP](configobject/UDG/20.15.2/PCCACTIONPROP.md)
- [QOSPROP](configobject/UDG/20.15.2/QOSPROP.md)
- [URRGROUP](configobject/UDG/20.15.2/URRGROUP.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改PCC策略组（MOD-PCCPOLICYGRP）_86528530.md`
- 原始手册：`evidence/UDG/20.15.2/删除PCC策略组（RMV-PCCPOLICYGRP）_82837608.md`
- 原始手册：`evidence/UDG/20.15.2/增加PCC策略组（ADD-PCCPOLICYGRP）_82837606.md`
- 原始手册：`evidence/UDG/20.15.2/查询PCC策略组（LST-PCCPOLICYGRP）_82837609.md`
