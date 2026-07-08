---
id: UDG@20.15.2@ConfigObject@APNADDRESSATTR
type: ConfigObject
name: APNADDRESSATTR（ApnAddressAttr配置）
nf: UDG
version: 20.15.2
object_name: APNADDRESSATTR
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# APNADDRESSATTR（ApnAddressAttr配置）

## 说明

**适用NF：PGW-U、UPF**

![](设置ApnAddressAttr配置（SET APNADDRESSATTR）_82837173.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该操作会配置APN的地址分配属性，可能会导致用户激活失败。

SET APNADDRESSATTR命令可以对APN地址分配属性进行配置。当用户接入时，需要给用户分配地址，此时需要对APN地址分配属性进行配置。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-APNADDRESSATTR]] · LST APNADDRESSATTR
- [[command/UDG/20.15.2/SET-APNADDRESSATTR]] · SET APNADDRESSATTR

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ApnAddressAttr配置（LST-APNADDRESSATTR）_86527108.md`
- 原始手册：`evidence/UDG/20.15.2/设置ApnAddressAttr配置（SET-APNADDRESSATTR）_82837173.md`
