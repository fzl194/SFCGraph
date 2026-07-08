---
id: UNC@20.15.2@ConfigObject@ISMFDFTQOSCTRL
type: ConfigObject
name: ISMFDFTQOSCTRL（I-SMF的Default QoS Flow配置）
nf: UNC
version: 20.15.2
object_name: ISMFDFTQOSCTRL
object_kind: entity
applicable_nf:
- SMF
status: active
---

# ISMFDFTQOSCTRL（I-SMF的Default QoS Flow配置）

## 说明

**适用NF：SMF**

该命令用来增加I-SMF的Default QoS Flow配置。在I-SMF插入或改变流程中，I-SMF收到H-SMF返回的QoS参数之后，跟本地配置的Default Qos参数进行比较，如果H-SMF传递的QoS参数的5QI不在允许列表，则I-SMF拒绝插入；如果H-SMF传递QoS参数的Session-AMBR等超出最大值，I-SMF根据配置进行带宽降速或者拒绝I-SMF插入或改变流程。

## 操作本对象的命令

- [ADD ISMFDFTQOSCTRL](command/UNC/20.15.2/ADD-ISMFDFTQOSCTRL.md)
- [LST ISMFDFTQOSCTRL](command/UNC/20.15.2/LST-ISMFDFTQOSCTRL.md)
- [MOD ISMFDFTQOSCTRL](command/UNC/20.15.2/MOD-ISMFDFTQOSCTRL.md)
- [RMV ISMFDFTQOSCTRL](command/UNC/20.15.2/RMV-ISMFDFTQOSCTRL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改I-SMF的Default-QoS-Flow配置（MOD-ISMFDFTQOSCTRL）_14280398.md`
- 原始手册：`evidence/UNC/20.15.2/删除I-SMF的Default-QoS-Flow配置（RMV-ISMFDFTQOSCTRL）_13960450.md`
- 原始手册：`evidence/UNC/20.15.2/增加I-SMF的Default-QoS-Flow配置（ADD-ISMFDFTQOSCTRL）_58800303.md`
- 原始手册：`evidence/UNC/20.15.2/查询I-SMF的Default-QoS-Flow配置（LST-ISMFDFTQOSCTRL）_59000289.md`
