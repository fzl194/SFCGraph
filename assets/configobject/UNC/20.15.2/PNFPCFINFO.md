---
id: UNC@20.15.2@ConfigObject@PNFPCFINFO
type: ConfigObject
name: PNFPCFINFO（对端PCF信息）
nf: UNC
version: 20.15.2
object_name: PNFPCFINFO
object_kind: entity
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
status: active
---

# PNFPCFINFO（对端PCF信息）

## 说明

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于增加本地配置的对端PCF实例信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 操作本对象的命令

- [ADD PNFPCFINFO](command/UNC/20.15.2/ADD-PNFPCFINFO.md)
- [LST PNFPCFINFO](command/UNC/20.15.2/LST-PNFPCFINFO.md)
- [RMV PNFPCFINFO](command/UNC/20.15.2/RMV-PNFPCFINFO.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除对端PCF信息（RMV-PNFPCFINFO）_09654343.md`
- 原始手册：`evidence/UNC/20.15.2/增加对端PCF信息（ADD-PNFPCFINFO）_09652989.md`
- 原始手册：`evidence/UNC/20.15.2/查询对端PCF信息（LST-PNFPCFINFO）_09653010.md`
