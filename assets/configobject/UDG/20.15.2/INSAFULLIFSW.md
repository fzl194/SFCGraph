---
id: UDG@20.15.2@ConfigObject@INSAFULLIFSW
type: ConfigObject
name: INSAFULLIFSW（全量智能SA识别开关）
nf: UDG
version: 20.15.2
object_name: INSAFULLIFSW
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# INSAFULLIFSW（全量智能SA识别开关）

## 说明

**适用NF：PGW-U、UPF**

![](设置全量智能SA识别开关（SET INSAFULLIFSW）_56405098.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，当开启开关后，此命令会对ISU资源和性能影响产生极大挑战，开启后可能会发生CPU过载。

设置全量非可信流量上送TPU推理。

## 操作本对象的命令

- [LST INSAFULLIFSW](command/UDG/20.15.2/LST-INSAFULLIFSW.md)
- [SET INSAFULLIFSW](command/UDG/20.15.2/SET-INSAFULLIFSW.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询全量智能SA识别开关（LST-INSAFULLIFSW）_06564543.md`
- 原始手册：`evidence/UDG/20.15.2/设置全量智能SA识别开关（SET-INSAFULLIFSW）_56405098.md`
