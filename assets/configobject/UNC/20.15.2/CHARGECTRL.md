---
id: UNC@20.15.2@ConfigObject@CHARGECTRL
type: ConfigObject
name: CHARGECTRL（计费控制配置）
nf: UNC
version: 20.15.2
object_name: CHARGECTRL
object_kind: global_setting
applicable_nf:
- PGW-C
- SMF
status: active
---

# CHARGECTRL（计费控制配置）

## 说明

**适用NF：PGW-C、SMF**

![](设置计费控制配置（SET CHARGECTRL）_09896792.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，此操作会影响新激活用户的计费方式(在线、离线、融合)，可能导致用户无法计费。

本命令用来控制是否基于用户漫游、拜访、本地属性来提供在线计费、离线计费和融合计费功能。

## 操作本对象的命令

- [LST CHARGECTRL](command/UNC/20.15.2/LST-CHARGECTRL.md)
- [SET CHARGECTRL](command/UNC/20.15.2/SET-CHARGECTRL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询计费控制配置（LST-CHARGECTRL）_09896793.md`
- 原始手册：`evidence/UNC/20.15.2/设置计费控制配置（SET-CHARGECTRL）_09896792.md`
