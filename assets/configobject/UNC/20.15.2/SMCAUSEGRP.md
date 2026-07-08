---
id: UNC@20.15.2@ConfigObject@SMCAUSEGRP
type: ConfigObject
name: SMCAUSEGRP（SM原因值映射组配置）
nf: UNC
version: 20.15.2
object_name: SMCAUSEGRP
object_kind: entity
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
status: active
---

# SMCAUSEGRP（SM原因值映射组配置）

## 说明

**适用NF：SMF、PGW-C、SGW-C、GGSN**

此命令用于增加一个SM原因值映射组配置记录。每个原因值映射组表示一个原因值映射规则集合，通常将一个源接口和一个目标接口的原因值映射规则作为一个映射组，如N7 cause to GTPv2 cause。SMCAUSEGRP通常是一组SMCAUSEMAP的集合。

## 操作本对象的命令

- [ADD SMCAUSEGRP](command/UNC/20.15.2/ADD-SMCAUSEGRP.md)
- [LST SMCAUSEGRP](command/UNC/20.15.2/LST-SMCAUSEGRP.md)
- [MOD SMCAUSEGRP](command/UNC/20.15.2/MOD-SMCAUSEGRP.md)
- [RMV SMCAUSEGRP](command/UNC/20.15.2/RMV-SMCAUSEGRP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SM原因值映射组配置（MOD-SMCAUSEGRP）_09652650.md`
- 原始手册：`evidence/UNC/20.15.2/删除SM原因值映射组配置（RMV-SMCAUSEGRP）_09654432.md`
- 原始手册：`evidence/UNC/20.15.2/增加SM原因值映射组配置（ADD-SMCAUSEGRP）_09651511.md`
- 原始手册：`evidence/UNC/20.15.2/查询SM原因值映射组配置（LST-SMCAUSEGRP）_09653123.md`
