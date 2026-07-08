---
id: UNC@20.15.2@ConfigObject@SMFNONDFTQOSCTL
type: ConfigObject
name: SMFNONDFTQOSCTL（SMF的非Default QoS Flow配置）
nf: UNC
version: 20.15.2
object_name: SMFNONDFTQOSCTL
object_kind: entity
applicable_nf:
- SMF
status: active
---

# SMFNONDFTQOSCTL（SMF的非Default QoS Flow配置）

## 说明

**适用NF：SMF**

该命令用来增加I-SMF/V-SMF的非Default QoS Flow配置。在I-SMF/V-SMF插入或改变流程中，I-SMF/V-SMF收到H-SMF返回的QoS参数之后，跟本地配置的非Default Qos参数进行比较，如果H-SMF传递的QoS参数的5QI不在允许列表，则I-SMF/V-SMF拒绝插入；如果H-SMF传递QoS参数的Session-AMBR等超出最大值，I-SMF/V-SMF根据配置进行带宽降速或者拒绝I-SMF/V-SMF插入或改变流程。

## 操作本对象的命令

- [ADD SMFNONDFTQOSCTL](command/UNC/20.15.2/ADD-SMFNONDFTQOSCTL.md)
- [LST SMFNONDFTQOSCTL](command/UNC/20.15.2/LST-SMFNONDFTQOSCTL.md)
- [MOD SMFNONDFTQOSCTL](command/UNC/20.15.2/MOD-SMFNONDFTQOSCTL.md)
- [RMV SMFNONDFTQOSCTL](command/UNC/20.15.2/RMV-SMFNONDFTQOSCTL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SMF的非Default-QoS-Flow配置（MOD-SMFNONDFTQOSCTL）_13800470.md`
- 原始手册：`evidence/UNC/20.15.2/删除SMF的非Default-QoS-Flow配置（RMV-SMFNONDFTQOSCTL）_58800311.md`
- 原始手册：`evidence/UNC/20.15.2/增加SMF的非Default-QoS-Flow配置（ADD-SMFNONDFTQOSCTL）_14120432.md`
- 原始手册：`evidence/UNC/20.15.2/查询SMF的非Default-QoS-Flow配置（LST-SMFNONDFTQOSCTL）_58680355.md`
