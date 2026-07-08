---
id: UNC@20.15.2@ConfigObject@GLOBALIMS
type: ConfigObject
name: GLOBALIMS（全局IMS互通配置信息）
nf: UNC
version: 20.15.2
object_name: GLOBALIMS
object_kind: global_setting
applicable_nf:
- PGW-C
- SMF
- GGSN
- SGW-C
status: active
---

# GLOBALIMS（全局IMS互通配置信息）

## 说明

**适用NF：PGW-C、SMF、GGSN、SGW-C**

该命令用来配置IMS互通相关的设置。包括：IMS功能开关、IMS信令空口增强开关、配置P-CSCF的缺省组。当IMS功能开关打开时，才可以对IMS信令空口增强开关以及P-CSCF缺省组进行配置。当运营商需要控制IMS互通相关的参数时，可使用该命令对全局IMS配置参数进行配置。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-GLOBALIMS]] · LST GLOBALIMS
- [[command/UNC/20.15.2/SET-GLOBALIMS]] · SET GLOBALIMS

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局IMS互通配置信息（LST-GLOBALIMS）_09654168.md`
- 原始手册：`evidence/UNC/20.15.2/设置全局IMS互通配置信息（SET-GLOBALIMS）_09653684.md`
