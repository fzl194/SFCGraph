---
id: UNC@20.15.2@ConfigObject@PNFLMFINFO
type: ConfigObject
name: PNFLMFINFO（对端LMF信息）
nf: UNC
version: 20.15.2
object_name: PNFLMFINFO
object_kind: entity
applicable_nf:
- AMF
status: active
---

# PNFLMFINFO（对端LMF信息）

## 说明

**适用NF：AMF**

该命令用于增加本地配置的对端LMF支持的外部客户端类型和LMF标识等信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 操作本对象的命令

- [ADD PNFLMFINFO](command/UNC/20.15.2/ADD-PNFLMFINFO.md)
- [LST PNFLMFINFO](command/UNC/20.15.2/LST-PNFLMFINFO.md)
- [MOD PNFLMFINFO](command/UNC/20.15.2/MOD-PNFLMFINFO.md)
- [RMV PNFLMFINFO](command/UNC/20.15.2/RMV-PNFLMFINFO.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改对端LMF信息（MOD-PNFLMFINFO）_02470584.md`
- 原始手册：`evidence/UNC/20.15.2/删除对端LMF信息（RMV-PNFLMFINFO）_02910212.md`
- 原始手册：`evidence/UNC/20.15.2/增加对端LMF的信息（ADD-PNFLMFINFO）_02870338.md`
- 原始手册：`evidence/UNC/20.15.2/查询对端LMF的信息（LST-PNFLMFINFO）_49390203.md`
