---
id: UNC@20.15.2@ConfigObject@PNFDNN
type: ConfigObject
name: PNFDNN（对端NF的DNN信息）
nf: UNC
version: 20.15.2
object_name: PNFDNN
object_kind: entity
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
- SGW-C
- PGW-C
- GGSN
status: active
---

# PNFDNN（对端NF的DNN信息）

## 说明

**适用NF：AMF、SMF、NSSF、SMSF、NCG、SGW-C、PGW-C、GGSN**

该命令用于增加本地配置的对端NF实例支持的DNN及其归属切片的信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PNFDNN]] · ADD PNFDNN
- [[command/UNC/20.15.2/LST-PNFDNN]] · LST PNFDNN
- [[command/UNC/20.15.2/MOD-PNFDNN]] · MOD PNFDNN
- [[command/UNC/20.15.2/RMV-PNFDNN]] · RMV PNFDNN

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改对端NF的DNN信息（MOD-PNFDNN）_05497114.md`
- 原始手册：`evidence/UNC/20.15.2/删除对端NF的DNN信息（RMV-PNFDNN）_09653190.md`
- 原始手册：`evidence/UNC/20.15.2/增加对端NF的DNN信息（ADD-PNFDNN）_09654342.md`
- 原始手册：`evidence/UNC/20.15.2/查询对端NF的DNN信息（LST-PNFDNN）_09652972.md`
