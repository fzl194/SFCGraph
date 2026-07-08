---
id: UNC@20.15.2@ConfigObject@USRLOCATIONGRP
type: ConfigObject
name: USRLOCATIONGRP（用户位置组）
nf: UNC
version: 20.15.2
object_name: USRLOCATIONGRP
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# USRLOCATIONGRP（用户位置组）

## 说明

**适用NF：PGW-C、SMF**

该命令用于增加位置组。位置组是一种初始接入位置的位置组定义。当需要将多个位置信息组合起来对外呈现时，可将其绑定到同一位置组。该位置组可以在ADD UPBINDUPG命令中用于UsrProfGroup下的UserProfile的策略选择。

## 操作本对象的命令

- [ADD USRLOCATIONGRP](command/UNC/20.15.2/ADD-USRLOCATIONGRP.md)
- [LST USRLOCATIONGRP](command/UNC/20.15.2/LST-USRLOCATIONGRP.md)
- [RMV USRLOCATIONGRP](command/UNC/20.15.2/RMV-USRLOCATIONGRP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除用户位置组（RMV-USRLOCATIONGRP）_09897149.md`
- 原始手册：`evidence/UNC/20.15.2/增加用户位置组（ADD-USRLOCATIONGRP）_09897148.md`
- 原始手册：`evidence/UNC/20.15.2/查询用户位置组（LST-USRLOCATIONGRP）_09897150.md`
