---
id: UNC@20.15.2@ConfigObject@EMGCNUM
type: ConfigObject
name: EMGCNUM（紧急号码信息表记录）
nf: UNC
version: 20.15.2
object_name: EMGCNUM
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# EMGCNUM（紧急号码信息表记录）

## 说明

**适用网元：SGSN、MME**

此命令用于配置紧急呼叫号码。系统在给MS发送ATTACH ACCEPT消息和TAU ACCEPT消息时，会将配置的MCC的紧急呼叫号码携带在消息中发送给MS。

## 操作本对象的命令

- [ADD EMGCNUM](command/UNC/20.15.2/ADD-EMGCNUM.md)
- [LST EMGCNUM](command/UNC/20.15.2/LST-EMGCNUM.md)
- [RMV EMGCNUM](command/UNC/20.15.2/RMV-EMGCNUM.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除紧急号码信息表记录(RMV-EMGCNUM)_72345101.md`
- 原始手册：`evidence/UNC/20.15.2/增加紧急号码配置信息(ADD-EMGCNUM)_26305314.md`
- 原始手册：`evidence/UNC/20.15.2/查询紧急号码配置信息(LST-EMGCNUM)_26145504.md`
