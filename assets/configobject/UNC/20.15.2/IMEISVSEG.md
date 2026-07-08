---
id: UNC@20.15.2@ConfigObject@IMEISVSEG
type: ConfigObject
name: IMEISVSEG（IMEISV号段）
nf: UNC
version: 20.15.2
object_name: IMEISVSEG
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# IMEISVSEG（IMEISV号段）

## 说明

**适用NF：PGW-C、SMF**

该命令用于配置IMEISVSEG号码段。设置号段后，可以通过ADD SUBSCRIBERIDSEGGRP命令配置到号段组。最终可以达到通过号段组选择USERPROFILE作为本地策略、根据号段选择OCS、用户根据号段选择OCS组以及在线计费模板、根据号段选择CG组、根据号段选择SGW离线计费方式等业务功能。

## 操作本对象的命令

- [ADD IMEISVSEG](command/UNC/20.15.2/ADD-IMEISVSEG.md)
- [LST IMEISVSEG](command/UNC/20.15.2/LST-IMEISVSEG.md)
- [MOD IMEISVSEG](command/UNC/20.15.2/MOD-IMEISVSEG.md)
- [RMV IMEISVSEG](command/UNC/20.15.2/RMV-IMEISVSEG.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IMEISV号段（MOD-IMEISVSEG）_09897139.md`
- 原始手册：`evidence/UNC/20.15.2/删除IMEISV号段（RMV-IMEISVSEG）_09897140.md`
- 原始手册：`evidence/UNC/20.15.2/增加IMEISV号段（ADD-IMEISVSEG）_09897138.md`
- 原始手册：`evidence/UNC/20.15.2/查询IMEISV号段（LST-IMEISVSEG）_09897141.md`
