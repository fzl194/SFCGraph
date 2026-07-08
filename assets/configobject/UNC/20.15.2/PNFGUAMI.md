---
id: UNC@20.15.2@ConfigObject@PNFGUAMI
type: ConfigObject
name: PNFGUAMI（对端AMF的GUAMI信息）
nf: UNC
version: 20.15.2
object_name: PNFGUAMI
object_kind: entity
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
status: active
---

# PNFGUAMI（对端AMF的GUAMI信息）

## 说明

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于增加本地配置的对端AMF实例支持的GUAMI信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PNFGUAMI]] · ADD PNFGUAMI
- [[command/UNC/20.15.2/LST-PNFGUAMI]] · LST PNFGUAMI
- [[command/UNC/20.15.2/RMV-PNFGUAMI]] · RMV PNFGUAMI

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除对端AMF的GUAMI信息（RMV-PNFGUAMI）_09654193.md`
- 原始手册：`evidence/UNC/20.15.2/增加对端AMF的GUAMI信息（ADD-PNFGUAMI）_09653092.md`
- 原始手册：`evidence/UNC/20.15.2/查询对端AMF的GUAMI信息（LST-PNFGUAMI）_09653685.md`
