---
id: UNC@20.15.2@ConfigObject@LICCTRLALM
type: ConfigObject
name: LICCTRLALM（License容量告警配置）
nf: UNC
version: 20.15.2
object_name: LICCTRLALM
object_kind: global_setting
status: active
---

# LICCTRLALM（License容量告警配置）

## 说明

该命令用于设置系统的License容量告警配置。

当资源项使用率超过配置的故障告警门限，且持续超过“持续时间”时，则上报故障告警ALM-100046 资源达到LICENSE扩容门限；当资源项使用率低于配置的恢复告警门限，且持续超过“持续时间”时，则恢复此告警。

当用户需要修改告警门限和告警采样时间时，需要执行此命令。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-LICCTRLALM]] · LST LICCTRLALM
- [[command/UNC/20.15.2/SET-LICCTRLALM]] · SET LICCTRLALM

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询License容量告警配置（LST-LICCTRLALM）_09653686.md`
- 原始手册：`evidence/UNC/20.15.2/设置License容量告警配置（SET-LICCTRLALM）_09652489.md`
