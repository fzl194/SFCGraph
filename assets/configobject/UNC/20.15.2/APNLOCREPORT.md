---
id: UNC@20.15.2@ConfigObject@APNLOCREPORT
type: ConfigObject
name: APNLOCREPORT（基于APN的位置上报配置）
nf: UNC
version: 20.15.2
object_name: APNLOCREPORT
object_kind: entity
applicable_nf:
- PGW-C
- SMF
- GGSN
status: active
---

# APNLOCREPORT（基于APN的位置上报配置）

## 说明

**适用NF：PGW-C、SMF、GGSN**

该命令用于增加基于APN的位置上报配置。实时位置上报特性可以采用PCF/PCRF下发位置trigger的方式来触发，也可以采用SMF/PGW-C/GGSN本地配置位置trigger的方式来触发。SMF/PGW-C/GGSN可以通过本命令来配置基于APN的本地位置trigger。本配置受到全局位置上报功能（SET SMCOMMFUNC）和APN位置上报功能（ADD APN）的控制，并且有优先级高于全局位置上报配置（SET LOCATIONREPORT）。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-APNLOCREPORT]] · ADD APNLOCREPORT
- [[command/UNC/20.15.2/LST-APNLOCREPORT]] · LST APNLOCREPORT
- [[command/UNC/20.15.2/MOD-APNLOCREPORT]] · MOD APNLOCREPORT
- [[command/UNC/20.15.2/RMV-APNLOCREPORT]] · RMV APNLOCREPORT

## 证据

- 原始手册：`evidence/UNC/20.15.2/APNLOCREPORT.md`
- 原始手册：`evidence/UNC/20.15.2/APNLOCREPORT.md`
- 原始手册：`evidence/UNC/20.15.2/APNLOCREPORT.md`
- 原始手册：`evidence/UNC/20.15.2/APNLOCREPORT.md`
