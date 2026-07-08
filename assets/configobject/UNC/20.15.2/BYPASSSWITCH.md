---
id: UNC@20.15.2@ConfigObject@BYPASSSWITCH
type: ConfigObject
name: BYPASSSWITCH（节点自动进入BYPASS开关）
nf: UNC
version: 20.15.2
object_name: BYPASSSWITCH
object_kind: global_setting
status: active
---

# BYPASSSWITCH（节点自动进入BYPASS开关）

## 说明

![](设置节点自动进入BYPASS开关（SET BYPASSSWITCH）_97531594.assets/notice_3.0-zh-cn_2.png)

在存储故障场景，节点在磁盘故障后可能无法自动进入BYPASS状态，导致业务数据无法访问或业务中断，请慎重使用该命令。

本命令用于设置存储故障时，节点是否自动进入BYPASS状态。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-BYPASSSWITCH]] · DSP BYPASSSWITCH
- [[command/UNC/20.15.2/SET-BYPASSSWITCH]] · SET BYPASSSWITCH

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询节点自动进入BYPASS开关（DSP-BYPASSSWITCH）_97531593.md`
- 原始手册：`evidence/UNC/20.15.2/设置节点自动进入BYPASS开关（SET-BYPASSSWITCH）_97531594.md`
