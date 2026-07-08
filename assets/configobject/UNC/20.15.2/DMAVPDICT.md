---
id: UNC@20.15.2@ConfigObject@DMAVPDICT
type: ConfigObject
name: DMAVPDICT（Diameter数据字典中的AVP参数）
nf: UNC
version: 20.15.2
object_name: DMAVPDICT
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# DMAVPDICT（Diameter数据字典中的AVP参数）

## 说明

**适用网元：SGSN、MME**

该命令用于修改Diameter数据字典中的AVP参数。

当MME与HSS之间的协议版本不一致导致的对接失败时，可以执行此命令来修改Diameter数据字典中的AVP参数以解决HSS无法识别 UNC 发送的ULR消息的RAT-Type的信元问题。

## 操作本对象的命令

- [LST DMAVPDICT](command/UNC/20.15.2/LST-DMAVPDICT.md)
- [MOD DMAVPDICT](command/UNC/20.15.2/MOD-DMAVPDICT.md)
- [RMV DMAVPDICT](command/UNC/20.15.2/RMV-DMAVPDICT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Diameter数据字典中的AVP参数(MOD-DMAVPDICT)_26305668.md`
- 原始手册：`evidence/UNC/20.15.2/删除Diameter-AVP表(RMV-DMAVPDICT)_72345459.md`
- 原始手册：`evidence/UNC/20.15.2/查询Diameter-AVP表(LST-DMAVPDICT)_26145860.md`
