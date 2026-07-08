---
id: UNC@20.15.2@ConfigObject@CHGHOLI
type: ConfigObject
name: CHGHOLI（节假日配置）
nf: UNC
version: 20.15.2
object_name: CHGHOLI
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# CHGHOLI（节假日配置）

## 说明

**适用网元：SGSN**

该命令用于配置普通计费属性用户、预付费计费属性用户、包月制计费属性用户或实时计费属性用户的节假日。该命令的配置是为了实现对S-CDR话单进行不同费率时段的计费。该命令与费率时段配置（ [**ADD CHGTARI**](../计费费率时段配置/增加费率时段配置(ADD CHGTARI)_26305208.md) ）相结合，进行灵活的费率时段控制。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-CHGHOLI]] · ADD CHGHOLI
- [[command/UNC/20.15.2/LST-CHGHOLI]] · LST CHGHOLI
- [[command/UNC/20.15.2/RMV-CHGHOLI]] · RMV CHGHOLI

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除节假日配置(RMV-CHGHOLI)_72225063.md`
- 原始手册：`evidence/UNC/20.15.2/增加节假日配置(ADD-CHGHOLI)_26145382.md`
- 原始手册：`evidence/UNC/20.15.2/查询节假日配置(LST-CHGHOLI)_26305198.md`
