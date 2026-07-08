---
id: UNC@20.15.2@ConfigObject@TZLST
type: ConfigObject
name: TZLST（多时区参数）
nf: UNC
version: 20.15.2
object_name: TZLST
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# TZLST（多时区参数）

## 说明

**适用网元：SGSN、MME**

该命令用于增加位置区对应的时区和夏令时信息。当设备所在的国家或地区实行夏令时制度时，为确保时间信息的准确性，操作员应使用本命令配置夏令时的自动调整参数。

## 操作本对象的命令

- [ADD TZLST](command/UNC/20.15.2/ADD-TZLST.md)
- [DSP TZLST](command/UNC/20.15.2/DSP-TZLST.md)
- [LST TZLST](command/UNC/20.15.2/LST-TZLST.md)
- [MOD TZLST](command/UNC/20.15.2/MOD-TZLST.md)
- [RMV TZLST](command/UNC/20.15.2/RMV-TZLST.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改多时区参数(MOD-TZLST)_26145590.md`
- 原始手册：`evidence/UNC/20.15.2/删除多时区参数(RMV-TZLST)_72345187.md`
- 原始手册：`evidence/UNC/20.15.2/增加多时区参数(ADD-TZLST)_26305400.md`
- 原始手册：`evidence/UNC/20.15.2/显示多时区参数(DSP-TZLST)_26305402.md`
- 原始手册：`evidence/UNC/20.15.2/查询多时区参数(LST-TZLST)_72225271.md`
