---
id: UNC@20.15.2@ConfigObject@MDTPLMN
type: ConfigObject
name: MDTPLMN（基于管理的最小化路测的PLMN）
nf: UNC
version: 20.15.2
object_name: MDTPLMN
object_kind: entity
applicable_nf:
- MME
status: active
---

# MDTPLMN（基于管理的最小化路测的PLMN）

## 说明

**适用网元：MME**

该命令用于增加基于管理的最小化路测（MDT）的PLMN。MME通过本地配置和是否签约MDT授权，决策在HANDOVER REQUEST和INITIAL CONTEXT SETUP REQUEST消息中是否携带Management Based MDT PLMN List信元给eNodeB。

该命令的使用场景：该命令主要应用于小区无线质量的测量，旨在针对特定范围内（如Cell ID、TA等）的UE进行MDT的数据采集和分析。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-MDTPLMN]] · ADD MDTPLMN
- [[command/UNC/20.15.2/LST-MDTPLMN]] · LST MDTPLMN
- [[command/UNC/20.15.2/MOD-MDTPLMN]] · MOD MDTPLMN
- [[command/UNC/20.15.2/RMV-MDTPLMN]] · RMV MDTPLMN

## 证据

- 原始手册：`evidence/UNC/20.15.2/MDTPLMN.md`
- 原始手册：`evidence/UNC/20.15.2/MDTPLMN.md`
- 原始手册：`evidence/UNC/20.15.2/MDTPLMN.md`
- 原始手册：`evidence/UNC/20.15.2/MDTPLMN.md`
