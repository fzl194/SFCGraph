---
id: UNC@20.15.2@ConfigObject@PNFSUPI
type: ConfigObject
name: PNFSUPI（对端NF的SUPI信息）
nf: UNC
version: 20.15.2
object_name: PNFSUPI
object_kind: entity
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
status: active
---

# PNFSUPI（对端NF的SUPI信息）

## 说明

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

- 该命令用于增加本地配置对端NF实例支持的SUPI的信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。
- 当NFINSTANCEID配置为"sbidialtest"时，该命令用于新增model-D或model-C间接路由拨测用户列表，通过起始SUPI和终止SUPI的方式，配置一组拨测用户，不支持PATTERN模式配置拨测用户。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PNFSUPI]] · ADD PNFSUPI
- [[command/UNC/20.15.2/LST-PNFSUPI]] · LST PNFSUPI
- [[command/UNC/20.15.2/RMV-PNFSUPI]] · RMV PNFSUPI

## 证据

- 原始手册：`evidence/UNC/20.15.2/PNFSUPI.md`
- 原始手册：`evidence/UNC/20.15.2/PNFSUPI.md`
- 原始手册：`evidence/UNC/20.15.2/PNFSUPI.md`
