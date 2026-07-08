---
id: UNC@20.15.2@ConfigObject@BYPASSSTATUS
type: ConfigObject
name: BYPASSSTATUS（BYPASS状态）
nf: UNC
version: 20.15.2
object_name: BYPASSSTATUS
object_kind: global_setting
status: active
---

# BYPASSSTATUS（BYPASS状态）

## 说明

![](设置BYPASS状态（SET BYPASSSTATUS）_74020103.assets/notice_3.0-zh-cn_2.png)

设置进入BYPASS状态后，仅最小维护通道功能可用；设置退出BYPASS状态前请确认ALM-135644 节点存储亚健康告警已经恢复，请慎重使用该命令。

该功能仅支持华为虚拟化层软件FusionSphere，不支持第三方虚拟化层软件。

本命令用于手动设置部署的节点当前BYPASS状态。

若需要设置指定节点的BYPASS状态，需要输入“网元ID”和“节点名称”参数。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 操作本对象的命令

- [DSP BYPASSSTATUS](command/UNC/20.15.2/DSP-BYPASSSTATUS.md)
- [SET BYPASSSTATUS](command/UNC/20.15.2/SET-BYPASSSTATUS.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询BYPASS状态（DSP-BYPASSSTATUS）_74020102.md`
- 原始手册：`evidence/UNC/20.15.2/设置BYPASS状态（SET-BYPASSSTATUS）_74020103.md`
