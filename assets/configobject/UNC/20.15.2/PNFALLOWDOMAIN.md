---
id: UNC@20.15.2@ConfigObject@PNFALLOWDOMAIN
type: ConfigObject
name: PNFALLOWDOMAIN（对端NF允许的域名信息）
nf: UNC
version: 20.15.2
object_name: PNFALLOWDOMAIN
object_kind: entity
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
status: active
---

# PNFALLOWDOMAIN（对端NF允许的域名信息）

## 说明

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于增加对端NF服务支持的允许访问的域名。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 操作本对象的命令

- [ADD PNFALLOWDOMAIN](command/UNC/20.15.2/ADD-PNFALLOWDOMAIN.md)
- [LST PNFALLOWDOMAIN](command/UNC/20.15.2/LST-PNFALLOWDOMAIN.md)
- [RMV PNFALLOWDOMAIN](command/UNC/20.15.2/RMV-PNFALLOWDOMAIN.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除对端NF允许的域名信息（RMV-PNFALLOWDOMAIN）_09652469.md`
- 原始手册：`evidence/UNC/20.15.2/增加对端NF允许的域名信息（ADD-PNFALLOWDOMAIN）_09653836.md`
- 原始手册：`evidence/UNC/20.15.2/查询对端NF允许的域名信息（LST-PNFALLOWDOMAIN）_09652089.md`
