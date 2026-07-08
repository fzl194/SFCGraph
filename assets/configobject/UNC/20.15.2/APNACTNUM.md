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

- [[command/UNC/20.15.2/ADD-APNACTNUM]] · ADD APNACTNUM
- [[command/UNC/20.15.2/LST-APNACTNUM]] · LST APNACTNUM
- [[command/UNC/20.15.2/MOD-APNACTNUM]] · MOD APNACTNUM
- [[command/UNC/20.15.2/RMV-APNACTNUM]] · RMV APNACTNUM

## 证据

- 原始手册：`evidence/UNC/20.15.2/APNACTNUM.md`
- 原始手册：`evidence/UNC/20.15.2/APNACTNUM.md`
- 原始手册：`evidence/UNC/20.15.2/APNACTNUM.md`
- 原始手册：`evidence/UNC/20.15.2/APNACTNUM.md`
