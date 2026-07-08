---
id: UNC@20.15.2@ConfigObject@QOSREMARK
type: ConfigObject
name: QOSREMARK（全局QoS到TOS/DSCP的映射规则）
nf: UNC
version: 20.15.2
object_name: QOSREMARK
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
status: active
---

# QOSREMARK（全局QoS到TOS/DSCP的映射规则）

## 说明

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于配置系统上下行QoS映射功能开关。QoS映射功能表示将会话中QoS信息映射为用户上行或者下行IP数据报文头中的DSCP/ToS值，以满足报文在转发过程中的优先级与会话上下文中QoS定义的优先级保持一致。

该命令支持配置下行和上行两个方向的开关功能。从MS/UE到远程访问主机的数据流方向称为上行数据流，从远程访问主机到MS/UE的数据流方向称为下行数据流。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-QOSREMARK]] · LST QOSREMARK
- [[command/UNC/20.15.2/SET-QOSREMARK]] · SET QOSREMARK

## 证据

- 原始手册：`evidence/UNC/20.15.2/QOSREMARK.md`
- 原始手册：`evidence/UNC/20.15.2/QOSREMARK.md`
