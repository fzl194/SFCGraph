---
id: UNC@20.15.2@ConfigObject@RABPARA
type: ConfigObject
name: RABPARA（RAB参数协商配置）
nf: UNC
version: 20.15.2
object_name: RABPARA
object_kind: global_setting
applicable_nf:
- SGSN
status: active
---

# RABPARA（RAB参数协商配置）

## 说明

**适用网元：SGSN**

此命令用于设置RAB参数协商配置涉及到的参数。在进行RAB指派时，RNC可能会返回因QoS不支持导致的失败的RAB Assignment Response，SGSN需要进行降速率处理，对QoS进行重协商，可协商的Qos参数，分为最大速率、保证速率与最大和保证速率。

## 操作本对象的命令

- [LST RABPARA](command/UNC/20.15.2/LST-RABPARA.md)
- [SET RABPARA](command/UNC/20.15.2/SET-RABPARA.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询RAB参数协商配置(LST-RABPARA)_26146228.md`
- 原始手册：`evidence/UNC/20.15.2/设置RAB参数协商配置(SET-RABPARA)_72345827.md`
