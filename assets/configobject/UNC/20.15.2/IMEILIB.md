---
id: UNC@20.15.2@ConfigObject@IMEILIB
type: ConfigObject
name: IMEILIB（IMEI库记录）
nf: UNC
version: 20.15.2
object_name: IMEILIB
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# IMEILIB（IMEI库记录）

## 说明

**适用网元：SGSN、MME**

此命令用于增加IMEI库记录。IMEI库为IMEI TAC和终端类型的对应关系表，用于按照IMEI TAC识别智能终端类型。

当需要增加一条IMEI TAC和终端类型的对应记录时，需要执行此命令。

## 操作本对象的命令

- [ADD IMEILIB](command/UNC/20.15.2/ADD-IMEILIB.md)
- [LST IMEILIB](command/UNC/20.15.2/LST-IMEILIB.md)
- [RMV IMEILIB](command/UNC/20.15.2/RMV-IMEILIB.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IMEI库记录（RMV-IMEILIB）_72225413.md`
- 原始手册：`evidence/UNC/20.15.2/增加IMEI库记录（ADD-IMEILIB）_26145734.md`
- 原始手册：`evidence/UNC/20.15.2/查询IMEI库记录（LST-IMEILIB）_26305544.md`
