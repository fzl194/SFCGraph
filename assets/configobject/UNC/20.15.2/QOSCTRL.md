---
id: UNC@20.15.2@ConfigObject@QOSCTRL
type: ConfigObject
name: QOSCTRL（QoS控制配置）
nf: UNC
version: 20.15.2
object_name: QOSCTRL
object_kind: global_setting
applicable_nf:
- SMF
- SGW-C
- PGW-C
status: active
---

# QOSCTRL（QoS控制配置）

## 说明

**适用NF：SMF、SGW-C、PGW-C**

该命令用于为指定漫游属性和无线接入类型的用户配置带宽控制的全局开关。当配置该功能后，UNC会对指定的漫游属性和接入类型的用户进行带宽控制，向UPF下发用户签约以及SMF本地配置协商的QoS带宽控制参数。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-QOSCTRL]] · LST QOSCTRL
- [[command/UNC/20.15.2/SET-QOSCTRL]] · SET QOSCTRL

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询QoS控制配置（LST-QOSCTRL）_09652687.md`
- 原始手册：`evidence/UNC/20.15.2/设置QoS控制配置（SET-QOSCTRL）_09653269.md`
