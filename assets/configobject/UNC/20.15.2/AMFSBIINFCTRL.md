---
id: UNC@20.15.2@ConfigObject@AMFSBIINFCTRL
type: ConfigObject
name: AMFSBIINFCTRL（AMF的SBI接口控制参数）
nf: UNC
version: 20.15.2
object_name: AMFSBIINFCTRL
object_kind: global_setting
applicable_nf:
- AMF
status: active
---

# AMFSBIINFCTRL（AMF的SBI接口控制参数）

## 说明

**适用NF：AMF**

该命令用于设置AMF的SBI接口控制参数。

若期望AMF向周边网元携带信元location及callbackUri中的Schema可基于对端请求的Schema或所选定的服务Schema动态设置，可通过本命令开启Schema自适应功能。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-AMFSBIINFCTRL]] · LST AMFSBIINFCTRL
- [[command/UNC/20.15.2/SET-AMFSBIINFCTRL]] · SET AMFSBIINFCTRL

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF的SBI接口控制参数（LST-AMFSBIINFCTRL）_08368061.md`
- 原始手册：`evidence/UNC/20.15.2/设置AMF的SBI接口控制参数（SET-AMFSBIINFCTRL）_72448426.md`
