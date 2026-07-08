---
id: UNC@20.15.2@ConfigObject@PNFGROUPID
type: ConfigObject
name: PNFGROUPID（对端NF的群组信息）
nf: UNC
version: 20.15.2
object_name: PNFGROUPID
object_kind: entity
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
status: active
---

# PNFGROUPID（对端NF的群组信息）

## 说明

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于增加本地配置对端NF实例支持的群组信息，用于本端根据群组信息查询对端NF。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 操作本对象的命令

- [ADD PNFGROUPID](command/UNC/20.15.2/ADD-PNFGROUPID.md)
- [LST PNFGROUPID](command/UNC/20.15.2/LST-PNFGROUPID.md)
- [RMV PNFGROUPID](command/UNC/20.15.2/RMV-PNFGROUPID.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除对端NF的群组信息（RMV-PNFGROUPID）_09653640.md`
- 原始手册：`evidence/UNC/20.15.2/增加对端NF的群组信息（ADD-PNFGROUPID）_09653180.md`
- 原始手册：`evidence/UNC/20.15.2/查询对端NF的群组信息（LST-PNFGROUPID）_09652446.md`
