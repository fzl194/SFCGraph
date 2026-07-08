---
id: UNC@20.15.2@ConfigObject@RRCINACTPLCY
type: ConfigObject
name: RRCINACTPLCY（RRC Inactive策略）
nf: UNC
version: 20.15.2
object_name: RRCINACTPLCY
object_kind: entity
applicable_nf:
- AMF
status: active
---

# RRCINACTPLCY（RRC Inactive策略）

## 说明

**适用NF：AMF**

该命令用于配置RRC Inactive功能的开启策略。开启RRC Inactive功能后，支持RRC Inactive的终端可以快速从RRC_INACTIVE状态恢复到RRC_CONNECTED状态，缩短用户接入时延。该功能依赖于终端和无线的配合，如果配合不当，可能影响被叫业务。为避免所有用户均开启RRC Inactive功能的影响过大，建议通过此命令配置针对部分用户在特定区域开启RRC Inactive功能，确定影响可控后，可通过此配置命令逐步扩大范围。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-RRCINACTPLCY]] · ADD RRCINACTPLCY
- [[command/UNC/20.15.2/LST-RRCINACTPLCY]] · LST RRCINACTPLCY
- [[command/UNC/20.15.2/MOD-RRCINACTPLCY]] · MOD RRCINACTPLCY
- [[command/UNC/20.15.2/RMV-RRCINACTPLCY]] · RMV RRCINACTPLCY

## 证据

- 原始手册：`evidence/UNC/20.15.2/RRCINACTPLCY.md`
- 原始手册：`evidence/UNC/20.15.2/RRCINACTPLCY.md`
- 原始手册：`evidence/UNC/20.15.2/RRCINACTPLCY.md`
- 原始手册：`evidence/UNC/20.15.2/RRCINACTPLCY.md`
