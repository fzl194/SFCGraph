---
id: UDG@20.15.2@ConfigObject@URRGROUP
type: ConfigObject
name: URRGROUP（URR组）
nf: UDG
version: 20.15.2
object_name: URRGROUP
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# URRGROUP（URR组）

## 说明

**适用NF：PGW-U、UPF**

该命令用于新增使用量上报规则组，通过该命令可以指定上下行发起使用的URR名称，即指定上下行报文如何计费。

## 操作本对象的命令

- [ADD URRGROUP](command/UDG/20.15.2/ADD-URRGROUP.md)
- [LST URRGROUP](command/UDG/20.15.2/LST-URRGROUP.md)
- [MOD URRGROUP](command/UDG/20.15.2/MOD-URRGROUP.md)
- [RMV URRGROUP](command/UDG/20.15.2/RMV-URRGROUP.md)

## 关联对象

- [PCCPOLICYGRP](configobject/UDG/20.15.2/PCCPOLICYGRP.md)
- [URR](configobject/UDG/20.15.2/URR.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改URR组（MOD-URRGROUP）_82837635.md`
- 原始手册：`evidence/UDG/20.15.2/删除URR组（RMV-URRGROUP）_86528311.md`
- 原始手册：`evidence/UDG/20.15.2/增加URR组（ADD-URRGROUP）_82837634.md`
- 原始手册：`evidence/UDG/20.15.2/查询URR组（LST-URRGROUP）_82837637.md`
