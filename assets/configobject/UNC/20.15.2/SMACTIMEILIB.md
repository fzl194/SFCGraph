---
id: UNC@20.15.2@ConfigObject@SMACTIMEILIB
type: ConfigObject
name: SMACTIMEILIB（IMEI库记录）
nf: UNC
version: 20.15.2
object_name: SMACTIMEILIB
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# SMACTIMEILIB（IMEI库记录）

## 说明

**适用网元：SGSN、MME**

此命令用于增加终端IMEI记录。终端IMEI记录为IMEI TAC和终端类型的对应关系表，用于按照IMEI TAC识别智能终端类型。

## 操作本对象的命令

- [ADD SMACTIMEILIB](command/UNC/20.15.2/ADD-SMACTIMEILIB.md)
- [LST SMACTIMEILIB](command/UNC/20.15.2/LST-SMACTIMEILIB.md)
- [RMV SMACTIMEILIB](command/UNC/20.15.2/RMV-SMACTIMEILIB.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IMEI库记录（RMV-SMACTIMEILIB）_72345261.md`
- 原始手册：`evidence/UNC/20.15.2/增加IMEI库记录（ADD-SMACTIMEILIB）_26305474.md`
- 原始手册：`evidence/UNC/20.15.2/查询IMEI库记录（LST-SMACTIMEILIB）_26145666.md`
