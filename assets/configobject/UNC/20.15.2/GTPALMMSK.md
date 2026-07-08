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

- [[command/UNC/20.15.2/ADD-GTPALMMSK]] · ADD GTPALMMSK
- [[command/UNC/20.15.2/LST-GTPALMMSK]] · LST GTPALMMSK
- [[command/UNC/20.15.2/MOD-GTPALMMSK]] · MOD GTPALMMSK
- [[command/UNC/20.15.2/RMV-GTPALMMSK]] · RMV GTPALMMSK

## 证据

- 原始手册：`evidence/UNC/20.15.2/GTPALMMSK.md`
- 原始手册：`evidence/UNC/20.15.2/GTPALMMSK.md`
- 原始手册：`evidence/UNC/20.15.2/GTPALMMSK.md`
- 原始手册：`evidence/UNC/20.15.2/GTPALMMSK.md`
