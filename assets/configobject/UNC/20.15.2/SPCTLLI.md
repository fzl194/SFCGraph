---
id: UNC@20.15.2@ConfigObject@SPCTLLI
type: ConfigObject
name: SPCTLLI（特殊随机TLLI配置）
nf: UNC
version: 20.15.2
object_name: SPCTLLI
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# SPCTLLI（特殊随机TLLI配置）

## 说明

**适用网元：SGSN**

如果现网很多手机使用固定的RANDOM TLLI附着会导致附着因TLLI冲突而失败。该命令用于对增加一项特殊RANDOM TLLI的记录，对该RANDOM TLLI的IMSI附着串行接入。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SPCTLLI]] · ADD SPCTLLI
- [[command/UNC/20.15.2/LST-SPCTLLI]] · LST SPCTLLI
- [[command/UNC/20.15.2/RMV-SPCTLLI]] · RMV SPCTLLI

## 证据

- 原始手册：`evidence/UNC/20.15.2/SPCTLLI.md`
- 原始手册：`evidence/UNC/20.15.2/SPCTLLI.md`
- 原始手册：`evidence/UNC/20.15.2/SPCTLLI.md`
