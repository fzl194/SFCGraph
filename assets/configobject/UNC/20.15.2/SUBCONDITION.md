---
id: UNC@20.15.2@ConfigObject@SUBCONDITION
type: ConfigObject
name: SUBCONDITION（NF订阅条件）
nf: UNC
version: 20.15.2
object_name: SUBCONDITION
object_kind: entity
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SMSF
- NCG
status: active
---

# SUBCONDITION（NF订阅条件）

## 说明

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG**

该命令用于增加订阅的目标NF的条件等信息。当源NF向NRF发送订阅请求时，请求消息中包含订阅信息（目标NF类型、订阅条件和通知事件类型）。当目标NF触发订阅条件和通知事件时，NRF向源NF发送通知。

## 操作本对象的命令

- [ADD SUBCONDITION](command/UNC/20.15.2/ADD-SUBCONDITION.md)
- [LST SUBCONDITION](command/UNC/20.15.2/LST-SUBCONDITION.md)
- [MOD SUBCONDITION](command/UNC/20.15.2/MOD-SUBCONDITION.md)
- [RMV SUBCONDITION](command/UNC/20.15.2/RMV-SUBCONDITION.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改NF订阅条件（MOD-SUBCONDITION）_09652286.md`
- 原始手册：`evidence/UNC/20.15.2/删除NF订阅条件（RMV-SUBCONDITION）_09653711.md`
- 原始手册：`evidence/UNC/20.15.2/增加NF订阅条件（ADD-SUBCONDITION）_09651488.md`
- 原始手册：`evidence/UNC/20.15.2/查询NF订阅条件（LST-SUBCONDITION）_09653783.md`
