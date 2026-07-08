---
id: UNC@20.15.2@ConfigObject@BSFINFO
type: ConfigObject
name: BSFINFO（BSF信息）
nf: UNC
version: 20.15.2
object_name: BSFINFO
object_kind: entity
applicable_nf:
- SMF
status: active
---

# BSFINFO（BSF信息）

## 说明

**适用NF：SMF**

该命令用于配置BSF（Binding Support Function）实例信息。在SMF内置BSF的场景下，可以通过该命令配置BSF名称等基础信息。在BSF向NRF注册时，会携带该命令的配置数据，用于NF注册和后续的NF发现。

## 操作本对象的命令

- [ADD BSFINFO](command/UNC/20.15.2/ADD-BSFINFO.md)
- [LST BSFINFO](command/UNC/20.15.2/LST-BSFINFO.md)
- [RMV BSFINFO](command/UNC/20.15.2/RMV-BSFINFO.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除BSF信息（RMV-BSFINFO）_09652302.md`
- 原始手册：`evidence/UNC/20.15.2/增加BSF信息（ADD-BSFINFO）_09653792.md`
- 原始手册：`evidence/UNC/20.15.2/查询BSF信息（LST-BSFINFO）_09653008.md`
