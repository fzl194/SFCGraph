---
id: UNC@20.15.2@ConfigObject@R8QOSMAP
type: ConfigObject
name: R8QOSMAP（EPS QoS参数到Pre-R8 QoS参数映射规则）
nf: UNC
version: 20.15.2
object_name: R8QOSMAP
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# R8QOSMAP（EPS QoS参数到Pre-R8 QoS参数映射规则）

## 说明

**适用网元：MME**

此命令用于设置EPS QoS参数到Pre-R8 QoS参数的映射规则。在GUL互操作中，从4G网络向2/3G网络切换的时候，MME会根据配置的映射规则，将4G中使用的EPS QoS参数映射成适用于2/3G中使用的Pre-R8 QoS参数，以保证网络切换后，不影响业务服务质量。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-R8QOSMAP]] · LST R8QOSMAP
- [[command/UNC/20.15.2/SET-R8QOSMAP]] · SET R8QOSMAP

## 证据

- 原始手册：`evidence/UNC/20.15.2/R8QOSMAP.md`
- 原始手册：`evidence/UNC/20.15.2/R8QOSMAP.md`
