---
id: UDG@20.15.2@ConfigObject@VNFEVICTION
type: ConfigObject
name: VNFEVICTION（网元重调度策略）
nf: UDG
version: 20.15.2
object_name: VNFEVICTION
object_kind: global_setting
status: active
---

# VNFEVICTION（网元重调度策略）

## 说明

![](设置网元重调度开关（SET VNFEVICTION）_26089552.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当可能会导致业务受损，请谨慎使用并联系华为支持协助操作。

该命令用于设置网元的重调度开关。

开启重调度开关，在虚拟机故障、升级、资源不足等场景下，该虚拟机上的容器会被调度到其他虚拟机节点上。

在I层分批升级时，通过关闭网元的重调度开关，在升级完成后，重新打开网元的重调度开关，保证升级前后的容器仍在原虚拟机节点。

> **说明**
> 该命令仅在 Full-stack 虚机场景下支持。

## 操作本对象的命令

- [LST VNFEVICTION](command/UDG/20.15.2/LST-VNFEVICTION.md)
- [SET VNFEVICTION](command/UDG/20.15.2/SET-VNFEVICTION.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询网元重调度策略（LST-VNFEVICTION）_26089553.md`
- 原始手册：`evidence/UDG/20.15.2/设置网元重调度开关（SET-VNFEVICTION）_26089552.md`
