---
id: UNC@20.15.2@ConfigObject@CELLGEO
type: ConfigObject
name: CELLGEO（CELLID与地理坐标对应关系）
nf: UNC
version: 20.15.2
object_name: CELLGEO
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# CELLGEO（CELLID与地理坐标对应关系）

## 说明

**适用网元：SGSN**

此命令用于增加小区标识CID与地理位置经纬度坐标的对应关系。SGSN利用这个对应关系完成CID与地理位置经纬度坐标之间的转换，提供给LCS MT/NI流程使用。

## 操作本对象的命令

- [ADD CELLGEO](command/UNC/20.15.2/ADD-CELLGEO.md)
- [LST CELLGEO](command/UNC/20.15.2/LST-CELLGEO.md)
- [MOD CELLGEO](command/UNC/20.15.2/MOD-CELLGEO.md)
- [RMV CELLGEO](command/UNC/20.15.2/RMV-CELLGEO.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改CELLID与地理坐标对应关系(MOD-CELLGEO)_26145790.md`
- 原始手册：`evidence/UNC/20.15.2/删除CELLID与地理坐标对应关系(RMV-CELLGEO)_72345389.md`
- 原始手册：`evidence/UNC/20.15.2/增加CELLID与地理坐标对应关系(ADD-CELLGEO)_26305598.md`
- 原始手册：`evidence/UNC/20.15.2/查询CELLID与地理坐标对应关系(LST-CELLGEO)_72225469.md`
