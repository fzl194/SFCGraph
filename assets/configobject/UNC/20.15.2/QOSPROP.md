---
id: UNC@20.15.2@ConfigObject@QOSPROP
type: ConfigObject
name: QOSPROP（QoS属性）
nf: UNC
version: 20.15.2
object_name: QOSPROP
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# QOSPROP（QoS属性）

## 说明

**适用NF：PGW-C、SMF**

该命令主要用于配置PCC预定义规则的QoS参数，可以通过ADD PCCPOLICYGRP的QOSPROPNAME参数将QoS参数关联到PCC Rule，PCC动态规则只能是L3/4层，所以PCC动态规则的QoS-information只能作用于L3/4层规则。

该命令可以配置PCC预定义规则的L3/4层规则的QoS，也可以配置PCC预定义规则的L7层规则的QoS参数。

该命令可以通过ADD L2RULE的QOSPROPNAME参数将Qos参数关联到层二规则。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-QOSPROP]] · ADD QOSPROP
- [[command/UNC/20.15.2/LST-QOSPROP]] · LST QOSPROP
- [[command/UNC/20.15.2/MOD-QOSPROP]] · MOD QOSPROP
- [[command/UNC/20.15.2/RMV-QOSPROP]] · RMV QOSPROP

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改QoS属性（MOD-QOSPROP）_09897164.md`
- 原始手册：`evidence/UNC/20.15.2/删除QoS属性（RMV-QOSPROP）_09897165.md`
- 原始手册：`evidence/UNC/20.15.2/增加QoS属性（ADD-QOSPROP）_09897163.md`
- 原始手册：`evidence/UNC/20.15.2/查询QoS属性（LST-QOSPROP）_09897166.md`
