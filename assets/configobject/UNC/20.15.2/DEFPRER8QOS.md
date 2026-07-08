---
id: UNC@20.15.2@ConfigObject@DEFPRER8QOS
type: ConfigObject
name: DEFPRER8QOS（缺省的Pre-R8 QoS参数）
nf: UNC
version: 20.15.2
object_name: DEFPRER8QOS
object_kind: global_setting
applicable_nf:
- GGSN
status: active
---

# DEFPRER8QOS（缺省的Pre-R8 QoS参数）

## 说明

**适用NF：GGSN**

该命令用于设置UNC的QoS参数。 这些参数决定了UNC能够为每个PDP上下文提供的QoS范围，关于这些参数的具体含义参见协议3GPP TS 23.107。对于各业务类型的相关QoS参数，如果UE请求的QoS属性值为非法值，协商值等于UNC配置的参数值，否则协商值等于请求值；对于各业务类型不涉及的QoS参数，协商值等于请求值。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-DEFPRER8QOS]] · LST DEFPRER8QOS
- [[command/UNC/20.15.2/SET-DEFPRER8QOS]] · SET DEFPRER8QOS

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询缺省的Pre-R8-QoS参数（LST-DEFPRER8QOS）_09651521.md`
- 原始手册：`evidence/UNC/20.15.2/设置缺省的Pre-R8-QoS参数（SET-DEFPRER8QOS）_09654401.md`
