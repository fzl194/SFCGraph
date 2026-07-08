---
id: UNC@20.15.2@ConfigObject@NGEMGCNUM
type: ConfigObject
name: NGEMGCNUM（紧急号码配置信息）
nf: UNC
version: 20.15.2
object_name: NGEMGCNUM
object_kind: entity
applicable_nf:
- AMF
status: active
---

# NGEMGCNUM（紧急号码配置信息）

## 说明

**适用NF：AMF**

此命令用于配置紧急呼叫号码。系统在给UE发送Registration Accept消息时，会将配置的MCC的紧急呼叫号码携带在消息中发送给UE。

## 操作本对象的命令

- [ADD NGEMGCNUM](command/UNC/20.15.2/ADD-NGEMGCNUM.md)
- [LST NGEMGCNUM](command/UNC/20.15.2/LST-NGEMGCNUM.md)
- [RMV NGEMGCNUM](command/UNC/20.15.2/RMV-NGEMGCNUM.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除紧急号码配置信息（RMV-NGEMGCNUM）_09654354.md`
- 原始手册：`evidence/UNC/20.15.2/增加紧急号码配置信息（ADD-NGEMGCNUM）_09652453.md`
- 原始手册：`evidence/UNC/20.15.2/查询紧急号码配置信息（LST-NGEMGCNUM）_09653760.md`
