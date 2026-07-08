---
id: UNC@20.15.2@ConfigObject@PNFSMFSERAREA
type: ConfigObject
name: PNFSMFSERAREA（对端NF的SMF服务区域信息）
nf: UNC
version: 20.15.2
object_name: PNFSMFSERAREA
object_kind: entity
applicable_nf:
- SMF
- NCG
- SGW-C
- GGSN
- PGW-C
status: active
---

# PNFSMFSERAREA（对端NF的SMF服务区域信息）

## 说明

**适用NF：SMF、NCG、SGW-C、GGSN、PGW-C**

该命令用于增加本地配置对端UPF实例支持的为SMF提供服务区域的信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 操作本对象的命令

- [ADD PNFSMFSERAREA](command/UNC/20.15.2/ADD-PNFSMFSERAREA.md)
- [LST PNFSMFSERAREA](command/UNC/20.15.2/LST-PNFSMFSERAREA.md)
- [MOD PNFSMFSERAREA](command/UNC/20.15.2/MOD-PNFSMFSERAREA.md)
- [RMV PNFSMFSERAREA](command/UNC/20.15.2/RMV-PNFSMFSERAREA.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改对端NF的SMF服务区域信息（MOD-PNFSMFSERAREA）_52137135.md`
- 原始手册：`evidence/UNC/20.15.2/删除对端NF的SMF服务区域信息（RMV-PNFSMFSERAREA）_09653186.md`
- 原始手册：`evidence/UNC/20.15.2/增加对端NF的SMF服务区域信息（ADD-PNFSMFSERAREA）_09653019.md`
- 原始手册：`evidence/UNC/20.15.2/查询对端NF的SMF服务区域信息（LST-PNFSMFSERAREA）_09652242.md`
