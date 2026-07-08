---
id: UNC@20.15.2@ConfigObject@PNFALLOWEDPLMN
type: ConfigObject
name: PNFALLOWEDPLMN（对端NF允许的PLMN信息）
nf: UNC
version: 20.15.2
object_name: PNFALLOWEDPLMN
object_kind: entity
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
status: active
---

# PNFALLOWEDPLMN（对端NF允许的PLMN信息）

## 说明

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于增加对端NF服务支持的允许访问的PLMN。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 操作本对象的命令

- [ADD PNFALLOWEDPLMN](command/UNC/20.15.2/ADD-PNFALLOWEDPLMN.md)
- [LST PNFALLOWEDPLMN](command/UNC/20.15.2/LST-PNFALLOWEDPLMN.md)
- [RMV PNFALLOWEDPLMN](command/UNC/20.15.2/RMV-PNFALLOWEDPLMN.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除对端NF允许的PLMN信息（RMV-PNFALLOWEDPLMN）_09653099.md`
- 原始手册：`evidence/UNC/20.15.2/增加对端NF允许的PLMN信息（ADD-PNFALLOWEDPLMN）_09652467.md`
- 原始手册：`evidence/UNC/20.15.2/查询对端NF允许的PLMN信息（LST-PNFALLOWEDPLMN）_09653673.md`
