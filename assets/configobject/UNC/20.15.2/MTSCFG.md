---
id: UNC@20.15.2@ConfigObject@MTSCFG
type: ConfigObject
name: MTSCFG（消息跟踪配置参数）
nf: UNC
version: 20.15.2
object_name: MTSCFG
object_kind: global_setting
status: active
---

# MTSCFG（消息跟踪配置参数）

## 说明

![](设置消息跟踪配置参数（SET MTSCFG）_75263640.assets/notice_3.0-zh-cn_2.png)

执行该命令会改变消息跟踪的配置，会对消息跟踪造成影响：当选择 “FLOW_CONTROL_SWITCH” 类型并执行时，可能会影响到跟踪任务的消息上报；当选择 “BASE_SUBHEALTH_SWITCH” 类型并执行时，可能会影响跟踪任务创建与任务运行，请慎重执行。

本命令用于设置消息跟踪的配置参数。

## 操作本对象的命令

- [LST MTSCFG](command/UNC/20.15.2/LST-MTSCFG.md)
- [SET MTSCFG](command/UNC/20.15.2/SET-MTSCFG.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询消息跟踪配置参数（LST-MTSCFG）_11983805.md`
- 原始手册：`evidence/UNC/20.15.2/设置消息跟踪配置参数（SET-MTSCFG）_75263640.md`
