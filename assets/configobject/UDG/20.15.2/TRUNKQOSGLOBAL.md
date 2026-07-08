---
id: UDG@20.15.2@ConfigObject@TRUNKQOSGLOBAL
type: ConfigObject
name: TRUNKQOSGLOBAL（宽带集群QosGlobal配置）
nf: UDG
version: 20.15.2
object_name: TRUNKQOSGLOBAL
object_kind: global_setting
applicable_nf:
- SGW-U
- PGW-U
status: active
---

# TRUNKQOSGLOBAL（宽带集群QosGlobal配置）

## 说明

**适用NF：SGW-U、PGW-U**

该命令用于设置整机的宽带集群Qos功能。如果开启QosCar功能，则系统将会对集群用户的报文进行Qos控制。如果开QosRemark功能，则系统将会对集群用户的报文进行remark处理。

## 操作本对象的命令

- [LST TRUNKQOSGLOBAL](command/UDG/20.15.2/LST-TRUNKQOSGLOBAL.md)
- [SET TRUNKQOSGLOBAL](command/UDG/20.15.2/SET-TRUNKQOSGLOBAL.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询宽带集群QosGlobal配置（LST-TRUNKQOSGLOBAL）_68723525.md`
- 原始手册：`evidence/UDG/20.15.2/设置宽带集群QosGlobal配置（SET-TRUNKQOSGLOBAL）_70282536.md`
