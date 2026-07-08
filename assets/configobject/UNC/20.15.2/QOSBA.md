---
id: UNC@20.15.2@ConfigObject@QOSBA
type: ConfigObject
name: QOSBA（QoS BA）
nf: UNC
version: 20.15.2
object_name: QOSBA
object_kind: global_setting
status: active
---

# QOSBA（QoS BA）

## 说明

该命令将指定DS域的上行IP报文DSCP值或者上行VLAN报文802.1p的值映射成路由器内部的服务等级，并对报文着色；接收报文时，其原先的外部优先级标记将被映射为内部优先级；对来自上游设备且携带DSCP优先级的IP报文进行QoS调度的时候，可以通过本命令配置报文的DSCP优先级到路由器内部服务等级之间的映射，并为报文着色；对来自上游设备的VLAN报文进行QoS调度的时候，可以通过本命令配置DS域中VLAN报文的802.1p优先级到路由器内部服务等级之间的映射，并为报文着色。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-QOSBA]] · LST QOSBA
- [[command/UNC/20.15.2/SET-QOSBA]] · SET QOSBA

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询QoS-BA（LST-QOSBA）_00441337.md`
- 原始手册：`evidence/UNC/20.15.2/设置QoS-BA（SET-QOSBA）_00441521.md`
