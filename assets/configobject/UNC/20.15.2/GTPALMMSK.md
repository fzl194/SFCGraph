---
id: UNC@20.15.2@ConfigObject@GTPALMMSK
type: ConfigObject
name: GTPALMMSK（GTP路径断告警屏蔽记录）
nf: UNC
version: 20.15.2
object_name: GTPALMMSK
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# GTPALMMSK（GTP路径断告警屏蔽记录）

## 说明

**适用网元：SGSN、MME**

该命令通过增加IP地址/网段/IP地址范围以达到屏蔽GTP路径告警的目的。GTP路径告警包括GTPC路径故障告警（告警ID=80610，参见 **ALM-80610 GTPC路径故障** 告警处理），GTPU路径故障告警（告警ID=80661，参见 **ALM-80661 GTPU路径故障** 告警处理）。

## 操作本对象的命令

- [ADD GTPALMMSK](command/UNC/20.15.2/ADD-GTPALMMSK.md)
- [LST GTPALMMSK](command/UNC/20.15.2/LST-GTPALMMSK.md)
- [MOD GTPALMMSK](command/UNC/20.15.2/MOD-GTPALMMSK.md)
- [RMV GTPALMMSK](command/UNC/20.15.2/RMV-GTPALMMSK.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改GTP路径断告警屏蔽记录(MOD-GTPALMMSK)_72345509.md`
- 原始手册：`evidence/UNC/20.15.2/删除GTP路径断告警屏蔽记录(RMV-GTPALMMSK)_26305718.md`
- 原始手册：`evidence/UNC/20.15.2/增加GTP路径断告警屏蔽记录(ADD-GTPALMMSK)_72225587.md`
- 原始手册：`evidence/UNC/20.15.2/查询GTP路径断告警屏蔽记录(LST-GTPALMMSK)_26145910.md`
