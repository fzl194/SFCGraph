---
id: UNC@20.15.2@ConfigObject@MAINTAINIMSI
type: ConfigObject
name: MAINTAINIMSI（在线承载为保留承载）
nf: UNC
version: 20.15.2
object_name: MAINTAINIMSI
object_kind: global_setting
applicable_nf:
- PGW-C
- SGW-C
status: active
---

# MAINTAINIMSI（在线承载为保留承载）

## 说明

**适用NF：PGW-C、SGW-C**

该命令用于将指定的已经激活的并且支持MME Restoration功能或者支持SGW Restoration承载转变为保留承载。当现网调测MME故障恢复功能时在SGW-C上执行或者在调测SGW-C故障恢复功能时在PGW-C上执行。

## 操作本对象的命令

- [[command/UNC/20.15.2/SET-MAINTAINIMSI]] · SET MAINTAINIMSI

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置在线承载为保留承载（SET-MAINTAINIMSI）_31453526.md`
