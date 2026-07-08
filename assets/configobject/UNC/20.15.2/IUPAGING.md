---
id: UNC@20.15.2@ConfigObject@IUPAGING
type: ConfigObject
name: IUPAGING（Iu接口寻呼数据）
nf: UNC
version: 20.15.2
object_name: IUPAGING
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# IUPAGING（Iu接口寻呼数据）

## 说明

**适用网元：SGSN**

该命令用于在触发3G寻呼时，利用此信息根据RAI或者LAI定位RNC。用户进行附着或路由区更新时根据此表判断是否为SGSN间的流程。

## 操作本对象的命令

- [ADD IUPAGING](command/UNC/20.15.2/ADD-IUPAGING.md)
- [LST IUPAGING](command/UNC/20.15.2/LST-IUPAGING.md)
- [RMV IUPAGING](command/UNC/20.15.2/RMV-IUPAGING.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Iu接口寻呼数据(RMV-IUPAGING)_72345635.md`
- 原始手册：`evidence/UNC/20.15.2/增加Iu接口寻呼数据(ADD-IUPAGING)_26305844.md`
- 原始手册：`evidence/UNC/20.15.2/查询Iu接口寻呼数据(LST-IUPAGING)_26146036.md`
