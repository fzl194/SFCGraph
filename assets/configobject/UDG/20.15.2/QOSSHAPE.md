---
id: UDG@20.15.2@ConfigObject@QOSSHAPE
type: ConfigObject
name: QOSSHAPE（QosShape配置）
nf: UDG
version: 20.15.2
object_name: QOSSHAPE
object_kind: global_setting
applicable_nf:
- UPF
- SGW-U
- PGW-U
status: active
---

# QOSSHAPE（QosShape配置）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用于配置用户上下行shaping功能的全局开关，可以指定无线接入类型、漫游属性来配置用户上下行shaping功能，当使能shaping功能后，系统会根据用户协商后的上下行最大带宽和保证带宽对用户的报文发送速率做控制。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-QOSSHAPE]] · LST QOSSHAPE
- [[command/UDG/20.15.2/SET-QOSSHAPE]] · SET QOSSHAPE

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询QosShape配置（LST-QOSSHAPE）_82837672.md`
- 原始手册：`evidence/UDG/20.15.2/设置QosShape配置（SET-QOSSHAPE）_82837671.md`
