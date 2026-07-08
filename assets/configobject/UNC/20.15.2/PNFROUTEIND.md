---
id: UNC@20.15.2@ConfigObject@PNFROUTEIND
type: ConfigObject
name: PNFROUTEIND（对端NF的路由指示信息）
nf: UNC
version: 20.15.2
object_name: PNFROUTEIND
object_kind: entity
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
status: active
---

# PNFROUTEIND（对端NF的路由指示信息）

## 说明

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

- 该命令用于增加本地配置对端NF实例支持的路由指示信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。
- 当NFINSTANCEID配置为"sbidialtest"时，该命令用于新增model-D或model-C间接路由拨测用户列表，通过配置PNFPLMN及PNFROUTEIND的方式，配置一组拨测用户。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PNFROUTEIND]] · ADD PNFROUTEIND
- [[command/UNC/20.15.2/LST-PNFROUTEIND]] · LST PNFROUTEIND
- [[command/UNC/20.15.2/RMV-PNFROUTEIND]] · RMV PNFROUTEIND

## 证据

- 原始手册：`evidence/UNC/20.15.2/PNFROUTEIND.md`
- 原始手册：`evidence/UNC/20.15.2/PNFROUTEIND.md`
- 原始手册：`evidence/UNC/20.15.2/PNFROUTEIND.md`
