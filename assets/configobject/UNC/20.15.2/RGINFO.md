---
id: UNC@20.15.2@ConfigObject@RGINFO
type: ConfigObject
name: RGINFO（费率组信息）
nf: UNC
version: 20.15.2
object_name: RGINFO
object_kind: entity
applicable_nf:
- NCG
status: active
---

# RGINFO（费率组信息）

## 说明

**适用NF：NCG**

该命令用于删除已添加的话单费率组。

执行任务之前，可执行 [**LST RGINFO**](显示费率组信息（LST RGINFO）_51174324.md) 命令查询当前系统中的费率组信息，找到对应的费率组ID。

## 操作本对象的命令

- [LST RGINFO](command/UNC/20.15.2/LST-RGINFO.md)
- [RMV RGINFO](command/UNC/20.15.2/RMV-RGINFO.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除费率组信息（RMV-RGINFO）_51174323.md`
- 原始手册：`evidence/UNC/20.15.2/显示费率组信息（LST-RGINFO）_51174324.md`
