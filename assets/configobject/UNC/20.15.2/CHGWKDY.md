---
id: UNC@20.15.2@ConfigObject@CHGWKDY
type: ConfigObject
name: CHGWKDY（星期配置）
nf: UNC
version: 20.15.2
object_name: CHGWKDY
object_kind: global_setting
applicable_nf:
- SGSN
status: active
---

# CHGWKDY（星期配置）

## 说明

**适用网元：SGSN**

该命令用于设置普通计费属性用户、预付费计费属性用户、包月制计费属性用户或实时计费属性用户的周一到周日的费率属性是正常工作日还是休息日。该命令与费率时段配置（ [**ADD CHGTARI**](../计费费率时段配置/增加费率时段配置(ADD CHGTARI)_26305208.md) ）相结合，进行灵活的费率时段控制。该命令的配置是为了实现对S-CDR话单进行不同费率时段的计费。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-CHGWKDY]] · LST CHGWKDY
- [[command/UNC/20.15.2/SET-CHGWKDY]] · SET CHGWKDY

## 证据

- 原始手册：`evidence/UNC/20.15.2/CHGWKDY.md`
- 原始手册：`evidence/UNC/20.15.2/CHGWKDY.md`
