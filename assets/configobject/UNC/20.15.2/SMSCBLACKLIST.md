---
id: UNC@20.15.2@ConfigObject@SMSCBLACKLIST
type: ConfigObject
name: SMSCBLACKLIST（SMSC黑名单记录）
nf: UNC
version: 20.15.2
object_name: SMSCBLACKLIST
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# SMSCBLACKLIST（SMSC黑名单记录）

## 说明

**适用网元：SGSN**

此命令用于增加SMSC黑名单记录。用于短消息通信中黑名单拒绝的功能，即如果手机短消息中携带的请求SMSC地址在黑名单中，将中止该短消息流程。

## 操作本对象的命令

- [ADD SMSCBLACKLIST](command/UNC/20.15.2/ADD-SMSCBLACKLIST.md)
- [LST SMSCBLACKLIST](command/UNC/20.15.2/LST-SMSCBLACKLIST.md)
- [RMV SMSCBLACKLIST](command/UNC/20.15.2/RMV-SMSCBLACKLIST.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SMSC黑名单记录(RMV-SMSCBLACKLIST)_26305536.md`
- 原始手册：`evidence/UNC/20.15.2/增加SMSC黑名单记录(ADD-SMSCBLACKLIST)_72225405.md`
- 原始手册：`evidence/UNC/20.15.2/查询SMSC黑名单记录(LST-SMSCBLACKLIST)_72345323.md`
