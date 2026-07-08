---
id: UNC@20.15.2@ConfigObject@QOSGLOBAL
type: ConfigObject
name: QOSGLOBAL（全局QoS配置）
nf: UNC
version: 20.15.2
object_name: QOSGLOBAL
object_kind: global_setting
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
status: active
---

# QOSGLOBAL（全局QoS配置）

## 说明

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用来设置全局的QoS信息，当不需要基于APN粒度设置QoS信息时，所有APN都关联到该QoS信息。

## 操作本对象的命令

- [LST QOSGLOBAL](command/UNC/20.15.2/LST-QOSGLOBAL.md)
- [SET QOSGLOBAL](command/UNC/20.15.2/SET-QOSGLOBAL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局QoS配置（LST-QOSGLOBAL）_09652987.md`
- 原始手册：`evidence/UNC/20.15.2/设置全局QoS配置（SET-QOSGLOBAL）_09652976.md`
