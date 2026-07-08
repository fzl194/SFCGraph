---
id: UNC@20.15.2@ConfigObject@PNFPLMN
type: ConfigObject
name: PNFPLMN（对端NF的PLMN信息）
nf: UNC
version: 20.15.2
object_name: PNFPLMN
object_kind: entity
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
status: active
---

# PNFPLMN（对端NF的PLMN信息）

## 说明

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

- 该命令用于增加本地配置的对端NF实例支持的PLMN信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。
- 当NFINSTANCEID配置为"sbidialtest"时，该命令用于新增model-D或model-C间接路由拨测用户列表，通过配置PNFPLMN及PNFROUTEIND的方式，配置一组拨测用户。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PNFPLMN]] · ADD PNFPLMN
- [[command/UNC/20.15.2/LST-PNFPLMN]] · LST PNFPLMN
- [[command/UNC/20.15.2/RMV-PNFPLMN]] · RMV PNFPLMN

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除对端NF的PLMN信息（RMV-PNFPLMN）_09651592.md`
- 原始手册：`evidence/UNC/20.15.2/增加对端NF的PLMN信息（ADD-PNFPLMN）_09651368.md`
- 原始手册：`evidence/UNC/20.15.2/查询对端NF的PLMN信息（LST-PNFPLMN）_09651621.md`
