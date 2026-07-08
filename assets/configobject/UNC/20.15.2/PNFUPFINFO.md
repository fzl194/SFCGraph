---
id: UNC@20.15.2@ConfigObject@PNFUPFINFO
type: ConfigObject
name: PNFUPFINFO（对端UPF信息）
nf: UNC
version: 20.15.2
object_name: PNFUPFINFO
object_kind: entity
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
status: active
---

# PNFUPFINFO（对端UPF信息）

## 说明

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于增加本地配置的对端UPF实例的相关信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PNFUPFINFO]] · ADD PNFUPFINFO
- [[command/UNC/20.15.2/LST-PNFUPFINFO]] · LST PNFUPFINFO
- [[command/UNC/20.15.2/MOD-PNFUPFINFO]] · MOD PNFUPFINFO
- [[command/UNC/20.15.2/RMV-PNFUPFINFO]] · RMV PNFUPFINFO

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改对端UPF信息（MOD-PNFUPFINFO）_09654383.md`
- 原始手册：`evidence/UNC/20.15.2/删除对端UPF信息（RMV-PNFUPFINFO）_09654161.md`
- 原始手册：`evidence/UNC/20.15.2/增加对端UPF信息（ADD-PNFUPFINFO）_09653643.md`
- 原始手册：`evidence/UNC/20.15.2/查询对端UPF信息（LST-PNFUPFINFO）_09652150.md`
