---
id: UNC@20.15.2@ConfigObject@RGRCACT
type: ConfigObject
name: RGRCACT（RG级异常返回码处理动作）
nf: UNC
version: 20.15.2
object_name: RGRCACT
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# RGRCACT（RG级异常返回码处理动作）

## 说明

**适用NF：PGW-C、SMF**

该命令用于增加RG级异常返回码的处理动作配置。当CHF返回的Charging Data Response消息携带RG级异常返回码时，根据此配置进行处理。

## 操作本对象的命令

- [ADD RGRCACT](command/UNC/20.15.2/ADD-RGRCACT.md)
- [LST RGRCACT](command/UNC/20.15.2/LST-RGRCACT.md)
- [MOD RGRCACT](command/UNC/20.15.2/MOD-RGRCACT.md)
- [RMV RGRCACT](command/UNC/20.15.2/RMV-RGRCACT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改RG级异常返回码处理动作（MOD-RGRCACT）_09651367.md`
- 原始手册：`evidence/UNC/20.15.2/删除RG级异常返回码处理动作（RMV-RGRCACT）_09652671.md`
- 原始手册：`evidence/UNC/20.15.2/增加RG级异常返回码处理动作（ADD-RGRCACT）_09654186.md`
- 原始手册：`evidence/UNC/20.15.2/查询RG级异常返回码处理动作（LST-RGRCACT）_09652230.md`
