---
id: UDG@20.15.2@ConfigObject@PCCACTIONPROP
type: ConfigObject
name: PCCACTIONPROP（PCC动作属性）
nf: UDG
version: 20.15.2
object_name: PCCACTIONPROP
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# PCCACTIONPROP（PCC动作属性）

## 说明

**适用NF：PGW-U、UPF**

此命令用于增加PCC动作属性。可以通过命令，配置PCC策略相关的动作属性，包括Gate、URL Redirect动作。支持配置不同业务发起端定义不同的上下行报文处理动作。

## 操作本对象的命令

- [ADD PCCACTIONPROP](command/UDG/20.15.2/ADD-PCCACTIONPROP.md)
- [LST PCCACTIONPROP](command/UDG/20.15.2/LST-PCCACTIONPROP.md)
- [MOD PCCACTIONPROP](command/UDG/20.15.2/MOD-PCCACTIONPROP.md)
- [RMV PCCACTIONPROP](command/UDG/20.15.2/RMV-PCCACTIONPROP.md)

## 关联对象

- [PCCPOLICYGRP](configobject/UDG/20.15.2/PCCPOLICYGRP.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改PCC动作属性（MOD-PCCACTIONPROP）_82837602.md`
- 原始手册：`evidence/UDG/20.15.2/删除PCC动作属性（RMV-PCCACTIONPROP）_86528583.md`
- 原始手册：`evidence/UDG/20.15.2/增加PCC动作属性（ADD-PCCACTIONPROP）_82837601.md`
- 原始手册：`evidence/UDG/20.15.2/查询PCC动作属性（LST-PCCACTIONPROP）_82837604.md`
