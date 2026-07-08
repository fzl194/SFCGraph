---
id: UNC@20.15.2@ConfigObject@PNFPLMNRANGE
type: ConfigObject
name: PNFPLMNRANGE（对端NF的PLMN范围）
nf: UNC
version: 20.15.2
object_name: PNFPLMNRANGE
object_kind: entity
applicable_nf:
- AMF
- SMF
- NSSF
- NCG
status: active
---

# PNFPLMNRANGE（对端NF的PLMN范围）

## 说明

**适用NF：AMF、SMF、NSSF、NCG**

该命令用于增加本地配置的对端NF实例支持的PLMN范围信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PNFPLMNRANGE]] · ADD PNFPLMNRANGE
- [[command/UNC/20.15.2/LST-PNFPLMNRANGE]] · LST PNFPLMNRANGE
- [[command/UNC/20.15.2/MOD-PNFPLMNRANGE]] · MOD PNFPLMNRANGE
- [[command/UNC/20.15.2/RMV-PNFPLMNRANGE]] · RMV PNFPLMNRANGE

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改对端NF的PLMN范围（MOD-PNFPLMNRANGE）_09653187.md`
- 原始手册：`evidence/UNC/20.15.2/删除对端NF的PLMN范围（RMV-PNFPLMNRANGE）_09652099.md`
- 原始手册：`evidence/UNC/20.15.2/增加对端NF的PLMN范围（ADD-PNFPLMNRANGE）_09651357.md`
- 原始手册：`evidence/UNC/20.15.2/查询对端NF的PLMN范围（LST-PNFPLMNRANGE）_09653224.md`
