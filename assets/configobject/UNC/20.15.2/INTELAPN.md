---
id: UNC@20.15.2@ConfigObject@INTELAPN
type: ConfigObject
name: INTELAPN（可按携带智能分流关键词进行处理的APN）
nf: UNC
version: 20.15.2
object_name: INTELAPN
object_kind: entity
applicable_nf:
- PGW-C
status: active
---

# INTELAPN（可按携带智能分流关键词进行处理的APN）

## 说明

**适用NF：PGW-C**

该命令用于增加APN名称中未携带智能分流关键词，但仍然可以按携带智能分流关键词进行处理的APN。APN配置智能分流关键词对应命令为ADD APNINTELSHUNT。

## 操作本对象的命令

- [ADD INTELAPN](command/UNC/20.15.2/ADD-INTELAPN.md)
- [LST INTELAPN](command/UNC/20.15.2/LST-INTELAPN.md)
- [RMV INTELAPN](command/UNC/20.15.2/RMV-INTELAPN.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除可按携带智能分流关键词进行处理的APN（RMV-INTELAPN）_87360200.md`
- 原始手册：`evidence/UNC/20.15.2/增加可按携带智能分流关键词进行处理的APN（ADD-INTELAPN）_87680052.md`
- 原始手册：`evidence/UNC/20.15.2/查询可按携带智能分流关键词进行处理的APN（LST-INTELAPN）_40119809.md`
