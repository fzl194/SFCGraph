---
id: UNC@20.15.2@ConfigObject@SGSLKS
type: ConfigObject
name: SGSLKS（SGs链路集）
nf: UNC
version: 20.15.2
object_name: SGSLKS
object_kind: entity
applicable_nf:
- MME
status: active
---

# SGSLKS（SGs链路集）

## 说明

**适用网元：MME**

此命令用于增加SGs链路集。

当需要配置到一个MSC/VLR的链接时，首先通过执行此命令配置一个管理到MSC/VLR的所有链路的集合，然后通过 [**ADD SGSLNK**](../SGsAP链路管理/增加SGs链路(ADD SGSLNK)_72345031.md) 命令配置多条并行链路。

## 操作本对象的命令

- [ADD SGSLKS](command/UNC/20.15.2/ADD-SGSLKS.md)
- [LST SGSLKS](command/UNC/20.15.2/LST-SGSLKS.md)
- [MOD SGSLKS](command/UNC/20.15.2/MOD-SGSLKS.md)
- [RMV SGSLKS](command/UNC/20.15.2/RMV-SGSLKS.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SGs链路集(MOD-SGSLKS)_72225119.md`
- 原始手册：`evidence/UNC/20.15.2/删除SGs链路集(RMV-SGSLKS)_26145436.md`
- 原始手册：`evidence/UNC/20.15.2/增加SGs链路集(ADD-SGSLKS)_72345035.md`
- 原始手册：`evidence/UNC/20.15.2/查询SGs链路集(LST-SGSLKS)_26305250.md`
