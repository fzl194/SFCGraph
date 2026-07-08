---
id: UNC@20.15.2@ConfigObject@PRER8REMARK
type: ConfigObject
name: PRER8REMARK（Pre-R8 QoS到TOS/DSCP的映射规则）
nf: UNC
version: 20.15.2
object_name: PRER8REMARK
object_kind: entity
applicable_nf:
- GGSN
status: active
---

# PRER8REMARK（Pre-R8 QoS到TOS/DSCP的映射规则）

## 说明

**适用NF：GGSN**

该命令用来配置UNC全局的或者基于QosProfile的QoS映射规则。基于QosProfile的QoS映射规则可与APN实例绑定，用来控制此APN下会话的QoS映射规则。UNC支持将用户在会话激活或者更新过程中协商的QoS参数映射为IP报文头中的TOS（服务类型）域或者DSCP（区别服务编码点），这样用户的数据报文在传送过程中，UNC将映射出的TOS或者DSCP填写到用户数据报文的IP头中，该IP报文在传送过程将根据TOS或者DSCP编码获得不同的处理优先级，从而满足服务质量的要求。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PRER8REMARK]] · ADD PRER8REMARK
- [[command/UNC/20.15.2/LST-PRER8REMARK]] · LST PRER8REMARK
- [[command/UNC/20.15.2/MOD-PRER8REMARK]] · MOD PRER8REMARK
- [[command/UNC/20.15.2/RMV-PRER8REMARK]] · RMV PRER8REMARK

## 证据

- 原始手册：`evidence/UNC/20.15.2/PRER8REMARK.md`
- 原始手册：`evidence/UNC/20.15.2/PRER8REMARK.md`
- 原始手册：`evidence/UNC/20.15.2/PRER8REMARK.md`
- 原始手册：`evidence/UNC/20.15.2/PRER8REMARK.md`
