---
id: UNC@20.15.2@ConfigObject@APNACTNUM
type: ConfigObject
name: APNACTNUM（APN激活数目限制）
nf: UNC
version: 20.15.2
object_name: APNACTNUM
object_kind: entity
applicable_nf:
- MME
status: active
---

# APNACTNUM（APN激活数目限制）

## 说明

**适用网元：MME**

该命令用于增加APN激活数目限制配置。配置同一个用户相同APN可以建立的PDN连接最大数目和IP地址最大数目，当终端建立的PDN连接个数或分配的IP地址个数到达设置的阈值时，系统给终端回复PDN连接拒绝消息，携带配置的原因值。

## 操作本对象的命令

- [ADD APNACTNUM](command/UNC/20.15.2/ADD-APNACTNUM.md)
- [LST APNACTNUM](command/UNC/20.15.2/LST-APNACTNUM.md)
- [MOD APNACTNUM](command/UNC/20.15.2/MOD-APNACTNUM.md)
- [RMV APNACTNUM](command/UNC/20.15.2/RMV-APNACTNUM.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改APN激活数目限制(MOD-APNACTNUM)_26305468.md`
- 原始手册：`evidence/UNC/20.15.2/删除APN激活数目限制(RMV-APNACTNUM)_72225337.md`
- 原始手册：`evidence/UNC/20.15.2/增加APN激活数目限制(ADD-APNACTNUM)_26145656.md`
- 原始手册：`evidence/UNC/20.15.2/查询APN激活数目限制(LST-APNACTNUM)_72345255.md`
