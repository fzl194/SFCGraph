---
id: UNC@20.15.2@ConfigObject@LOCCOMMPOLICY
type: ConfigObject
name: LOCCOMMPOLICY（本地Common Policy配置）
nf: UNC
version: 20.15.2
object_name: LOCCOMMPOLICY
object_kind: entity
applicable_nf:
- SMF
- PGW-C
- GGSN
status: active
---

# LOCCOMMPOLICY（本地Common Policy配置）

## 说明

**适用NF：SMF、PGW-C、GGSN**

该命令用于增加本地Common Policy配置。在激活时，根据PCF下发的多个PccRule与SMF本地配置的UserProfile和LocalCommPolicy选择优先级最高的UserProfile作为最终的Common Policy携带给UDG。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-LOCCOMMPOLICY]] · ADD LOCCOMMPOLICY
- [[command/UNC/20.15.2/LST-LOCCOMMPOLICY]] · LST LOCCOMMPOLICY
- [[command/UNC/20.15.2/MOD-LOCCOMMPOLICY]] · MOD LOCCOMMPOLICY
- [[command/UNC/20.15.2/RMV-LOCCOMMPOLICY]] · RMV LOCCOMMPOLICY

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改本地Common-Policy配置（MOD-LOCCOMMPOLICY）_34100981.md`
- 原始手册：`evidence/UNC/20.15.2/删除本地Common-Policy配置（RMV-LOCCOMMPOLICY）_84260806.md`
- 原始手册：`evidence/UNC/20.15.2/增加本地Common-Policy配置（ADD-LOCCOMMPOLICY）_84420770.md`
- 原始手册：`evidence/UNC/20.15.2/查询本地Common-Policy配置（LST-LOCCOMMPOLICY）_34300569.md`
