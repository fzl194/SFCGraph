---
id: UNC@20.15.2@ConfigObject@PNFDNAI
type: ConfigObject
name: PNFDNAI（对端NF的DNAI信息）
nf: UNC
version: 20.15.2
object_name: PNFDNAI
object_kind: entity
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
- PGW-C
status: active
---

# PNFDNAI（对端NF的DNAI信息）

## 说明

**适用NF：AMF、SMF、NSSF、SMSF、NCG、PGW-C**

该命令用于增加本地配置的对端NF实例支持的数据网络接入标识（Data Network Access Identity），以下简称DNAI。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PNFDNAI]] · ADD PNFDNAI
- [[command/UNC/20.15.2/LST-PNFDNAI]] · LST PNFDNAI
- [[command/UNC/20.15.2/MOD-PNFDNAI]] · MOD PNFDNAI
- [[command/UNC/20.15.2/RMV-PNFDNAI]] · RMV PNFDNAI

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改对端NF的DNAI信息（MOD-PNFDNAI）_09653103.md`
- 原始手册：`evidence/UNC/20.15.2/删除对端NF的DNAI信息（RMV-PNFDNAI）_09652252.md`
- 原始手册：`evidence/UNC/20.15.2/增加对端NF的DNAI信息（ADD-PNFDNAI）_09652965.md`
- 原始手册：`evidence/UNC/20.15.2/查询对端NF的DNAI信息（LST-PNFDNAI）_09654447.md`
