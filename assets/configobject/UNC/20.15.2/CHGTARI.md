---
id: UNC@20.15.2@ConfigObject@CHGTARI
type: ConfigObject
name: CHGTARI（费率时段配置）
nf: UNC
version: 20.15.2
object_name: CHGTARI
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# CHGTARI（费率时段配置）

## 说明

**适用网元：SGSN**

该命令用于设置普通计费属性用户、预付费计费属性用户、包月制计费属性用户或实时计费属性用户的某天（含工作日、周休日和节假日）的费率时段。该命令与星期表配置（ [**SET CHGWKDY**](../计费星期配置/设置星期配置(SET CHGWKDY)_26305210.md) ）和节假日配置（ [**ADD CHGHOLI**](../计费节假日配置/增加节假日配置(ADD CHGHOLI)_26145382.md) ）相结合，进行灵活的费率时段配置。该命令的配置是为了实现对S-CDR话单进行不同费率时段的计费。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-CHGTARI]] · ADD CHGTARI
- [[command/UNC/20.15.2/LST-CHGTARI]] · LST CHGTARI
- [[command/UNC/20.15.2/RMV-CHGTARI]] · RMV CHGTARI

## 证据

- 原始手册：`evidence/UNC/20.15.2/CHGTARI.md`
- 原始手册：`evidence/UNC/20.15.2/CHGTARI.md`
- 原始手册：`evidence/UNC/20.15.2/CHGTARI.md`
