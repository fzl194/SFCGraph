---
id: UNC@20.15.2@ConfigObject@APNCHARGECTRL
type: ConfigObject
name: APNCHARGECTRL（APN的计费配置）
nf: UNC
version: 20.15.2
object_name: APNCHARGECTRL
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# APNCHARGECTRL（APN的计费配置）

## 说明

**适用NF：SGW-C、PGW-C、SMF**

该命令用来为APN实例设置计费参数。

此命令可以为APN实例绑定离线计费模板、话单字段模板、计费属性模板、费率切换组、DCC模板、CCT模板以及配置在线计费、离线计费和融合计费方式。

## 操作本对象的命令

- [LST APNCHARGECTRL](command/UNC/20.15.2/LST-APNCHARGECTRL.md)
- [SET APNCHARGECTRL](command/UNC/20.15.2/SET-APNCHARGECTRL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN的计费配置（LST-APNCHARGECTRL）_09896818.md`
- 原始手册：`evidence/UNC/20.15.2/设置APN的计费配置（SET-APNCHARGECTRL）_09896817.md`
