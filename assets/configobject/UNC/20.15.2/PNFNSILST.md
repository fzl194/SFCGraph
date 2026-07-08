---
id: UNC@20.15.2@ConfigObject@PNFNSILST
type: ConfigObject
name: PNFNSILST（对端NF实例网络切片标识）
nf: UNC
version: 20.15.2
object_name: PNFNSILST
object_kind: entity
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
status: active
---

# PNFNSILST（对端NF实例网络切片标识）

## 说明

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于增加本地配置的对端NF实例支持的网络切片标识（Network Slice Identity），以下简称NSI。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PNFNSILST]] · ADD PNFNSILST
- [[command/UNC/20.15.2/LST-PNFNSILST]] · LST PNFNSILST
- [[command/UNC/20.15.2/RMV-PNFNSILST]] · RMV PNFNSILST

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除对端NF实例网络切片标识（RMV-PNFNSILST）_09653278.md`
- 原始手册：`evidence/UNC/20.15.2/增加对端NF实例网络切片标识（ADD-PNFNSILST）_09651458.md`
- 原始手册：`evidence/UNC/20.15.2/查询对端NF实例网络切片标识（LST-PNFNSILST）_09652554.md`
