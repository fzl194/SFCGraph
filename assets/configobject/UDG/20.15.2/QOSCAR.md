---
id: UDG@20.15.2@ConfigObject@QOSCAR
type: ConfigObject
name: QOSCAR（QosCar配置）
nf: UDG
version: 20.15.2
object_name: QOSCAR
object_kind: global_setting
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# QOSCAR（QosCar配置）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用于配置用户上下行QoSCar功能的全局开关。可以指定无线接入类型、漫游属性来配置用户上下行CAR功能。当使能CAR功能后，对于E-UTRAN接入的非GBR承载，系统会根据用户协商后的APN-AMBR对用户的报文发送速率做控制；对于E-UTRAN接入的GBR承载和其他接入方式下的承载，系统会根据用户协商后的上下行最大带宽和保证带宽对用户的报文发送速率做控制。当用户的报文发送速率超过最大带宽或APN-AMBR允许的值后，超过部分的数据包会被系统丢弃。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-QOSCAR]] · LST QOSCAR
- [[command/UDG/20.15.2/SET-QOSCAR]] · SET QOSCAR

## 证据

- 原始手册：`evidence/UDG/20.15.2/QOSCAR.md`
- 原始手册：`evidence/UDG/20.15.2/QOSCAR.md`
