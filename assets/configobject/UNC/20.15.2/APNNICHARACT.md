---
id: UNC@20.15.2@ConfigObject@APNNICHARACT
type: ConfigObject
name: APNNICHARACT（APNNI属性配置信息）
nf: UNC
version: 20.15.2
object_name: APNNICHARACT
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# APNNICHARACT（APNNI属性配置信息）

## 说明

**适用网元：SGSN、MME**

该命令用于配置在非活动用户（指已附着，但不进行业务活动的用户）分离流程中需要进行特殊处理的APN。它主要实现了在非活动用户分离流程中，“基于APN的保护”与“基于APN配置定时器”的功能。

## 操作本对象的命令

- [ADD APNNICHARACT](command/UNC/20.15.2/ADD-APNNICHARACT.md)
- [LST APNNICHARACT](command/UNC/20.15.2/LST-APNNICHARACT.md)
- [MOD APNNICHARACT](command/UNC/20.15.2/MOD-APNNICHARACT.md)
- [RMV APNNICHARACT](command/UNC/20.15.2/RMV-APNNICHARACT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改APNNI属性配置信息(MOD-APNNICHARACT)_72225349.md`
- 原始手册：`evidence/UNC/20.15.2/删除APNNI属性配置信息(RMV-APNNICHARACT)_26145670.md`
- 原始手册：`evidence/UNC/20.15.2/增加APNNI属性配置信息(ADD-APNNICHARACT)_72345265.md`
- 原始手册：`evidence/UNC/20.15.2/查询APNNI属性配置信息(LST-APNNICHARACT)_26305480.md`
