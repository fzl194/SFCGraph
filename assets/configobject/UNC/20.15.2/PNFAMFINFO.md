---
id: UNC@20.15.2@ConfigObject@PNFAMFINFO
type: ConfigObject
name: PNFAMFINFO（对端AMF信息）
nf: UNC
version: 20.15.2
object_name: PNFAMFINFO
object_kind: entity
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
status: active
---

# PNFAMFINFO（对端AMF信息）

## 说明

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于增加本地配置对端AMF的信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 操作本对象的命令

- [ADD PNFAMFINFO](command/UNC/20.15.2/ADD-PNFAMFINFO.md)
- [LST PNFAMFINFO](command/UNC/20.15.2/LST-PNFAMFINFO.md)
- [MOD PNFAMFINFO](command/UNC/20.15.2/MOD-PNFAMFINFO.md)
- [RMV PNFAMFINFO](command/UNC/20.15.2/RMV-PNFAMFINFO.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改对端AMF信息（MOD-PNFAMFINFO）_09652259.md`
- 原始手册：`evidence/UNC/20.15.2/删除对端AMF信息（RMV-PNFAMFINFO）_09651512.md`
- 原始手册：`evidence/UNC/20.15.2/增加对端AMF信息（ADD-PNFAMFINFO）_09653234.md`
- 原始手册：`evidence/UNC/20.15.2/查询对端AMF信息（LST-PNFAMFINFO）_09652470.md`
