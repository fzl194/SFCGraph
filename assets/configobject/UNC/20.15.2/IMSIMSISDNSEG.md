---
id: UNC@20.15.2@ConfigObject@IMSIMSISDNSEG
type: ConfigObject
name: IMSIMSISDNSEG（IMSI和MSISDN号段）
nf: UNC
version: 20.15.2
object_name: IMSIMSISDNSEG
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# IMSIMSISDNSEG（IMSI和MSISDN号段）

## 说明

**适用NF：PGW-C、SMF**

该命令用于配置IMSI/MSISDN号码段。设置号段后，可以通过ADD SUBSCRIBERIDSEGGRP命令配置到号段组。最终可以达到根据号段组选择USERPROFILE作为本地策略、根据号段选择OCS、根据号段选择OCS组以及在线计费模板、根据号段选择CG组、根据号段选择SGW离线计费方式等业务功能。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-IMSIMSISDNSEG]] · ADD IMSIMSISDNSEG
- [[command/UNC/20.15.2/LCK-IMSIMSISDNSEG]] · LCK IMSIMSISDNSEG
- [[command/UNC/20.15.2/LST-IMSIMSISDNSEG]] · LST IMSIMSISDNSEG
- [[command/UNC/20.15.2/MOD-IMSIMSISDNSEG]] · MOD IMSIMSISDNSEG
- [[command/UNC/20.15.2/RMV-IMSIMSISDNSEG]] · RMV IMSIMSISDNSEG

## 证据

- 原始手册：`evidence/UNC/20.15.2/IMSIMSISDNSEG.md`
- 原始手册：`evidence/UNC/20.15.2/IMSIMSISDNSEG.md`
- 原始手册：`evidence/UNC/20.15.2/IMSIMSISDNSEG.md`
- 原始手册：`evidence/UNC/20.15.2/IMSIMSISDNSEG.md`
- 原始手册：`evidence/UNC/20.15.2/IMSIMSISDNSEG.md`
