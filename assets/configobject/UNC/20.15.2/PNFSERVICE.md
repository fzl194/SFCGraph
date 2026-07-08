---
id: UNC@20.15.2@ConfigObject@PNFSERVICE
type: ConfigObject
name: PNFSERVICE（对端NF服务实例信息）
nf: UNC
version: 20.15.2
object_name: PNFSERVICE
object_kind: entity
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
status: active
---

# PNFSERVICE（对端NF服务实例信息）

## 说明

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于增加本地配置对端NF实例支持的服务实例信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PNFSERVICE]] · ADD PNFSERVICE
- [[command/UNC/20.15.2/LST-PNFSERVICE]] · LST PNFSERVICE
- [[command/UNC/20.15.2/MOD-PNFSERVICE]] · MOD PNFSERVICE
- [[command/UNC/20.15.2/RMV-PNFSERVICE]] · RMV PNFSERVICE

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改对端NF服务实例信息（MOD-PNFSERVICE）_09653155.md`
- 原始手册：`evidence/UNC/20.15.2/删除对端NF服务实例信息（RMV-PNFSERVICE）_09651474.md`
- 原始手册：`evidence/UNC/20.15.2/增加对端NF服务实例信息（ADD-PNFSERVICE）_09652978.md`
- 原始手册：`evidence/UNC/20.15.2/查询对端NF服务实例信息（LST-PNFSERVICE）_09654415.md`
