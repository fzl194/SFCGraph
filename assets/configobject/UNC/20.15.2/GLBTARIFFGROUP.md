---
id: UNC@20.15.2@ConfigObject@GLBTARIFFGROUP
type: ConfigObject
name: GLBTARIFFGROUP（全局费率切换组）
nf: UNC
version: 20.15.2
object_name: GLBTARIFFGROUP
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# GLBTARIFFGROUP（全局费率切换组）

## 说明

**适用NF：SGW-C、PGW-C、SMF**

该命令用于绑定全局费率切换组，UNC优先选择user-profile实例、APN实例绑定的费率切换组，当上述两者都没有绑定时，UNC选择全局配置的费率切换组。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-GLBTARIFFGROUP]] · LST GLBTARIFFGROUP
- [[command/UNC/20.15.2/SET-GLBTARIFFGROUP]] · SET GLBTARIFFGROUP

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局费率切换组（LST-GLBTARIFFGROUP）_09896841.md`
- 原始手册：`evidence/UNC/20.15.2/配置全局费率切换组（SET-GLBTARIFFGROUP）_09896840.md`
