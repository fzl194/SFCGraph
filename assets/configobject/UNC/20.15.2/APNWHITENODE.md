---
id: UNC@20.15.2@ConfigObject@APNWHITENODE
type: ConfigObject
name: APNWHITENODE（APN设备白名单）
nf: UNC
version: 20.15.2
object_name: APNWHITENODE
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# APNWHITENODE（APN设备白名单）

## 说明

**适用NF：PGW-C、SMF**

该命令用来配置APN跨省漫游流量限制设备白名单。支持配置SGW设备的IP地址段，以及SMF设备的NF实例标识。

## 操作本对象的命令

- [ADD APNWHITENODE](command/UNC/20.15.2/ADD-APNWHITENODE.md)
- [LST APNWHITENODE](command/UNC/20.15.2/LST-APNWHITENODE.md)
- [RMV APNWHITENODE](command/UNC/20.15.2/RMV-APNWHITENODE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除APN设备白名单（RMV-APNWHITENODE）_58542676.md`
- 原始手册：`evidence/UNC/20.15.2/增加APN设备白名单（ADD-APNWHITENODE）_08542633.md`
- 原始手册：`evidence/UNC/20.15.2/查询APN设备白名单列表（LST-APNWHITENODE）_58382748.md`
