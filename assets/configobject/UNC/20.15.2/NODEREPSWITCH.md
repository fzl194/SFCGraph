---
id: UNC@20.15.2@ConfigObject@NODEREPSWITCH
type: ConfigObject
name: NODEREPSWITCH（节点查询自动修复开关）
nf: UNC
version: 20.15.2
object_name: NODEREPSWITCH
object_kind: global_setting
status: active
---

# NODEREPSWITCH（节点查询自动修复开关）

## 说明

![](节点设置自动修复开关（SET NODEREPSWITCH）_72291815.assets/notice_3.0-zh-cn_2.png)

I层虚拟机HA开关打开场景下，执行该命令打开Error节点故障自愈或Unknown节点故障自愈开关，可能会导致I层与网元故障自愈冲突，请谨慎使用。

本命令用于设置节点故障自愈开关状态。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-NODEREPSWITCH]] · LST NODEREPSWITCH
- [[command/UNC/20.15.2/SET-NODEREPSWITCH]] · SET NODEREPSWITCH

## 证据

- 原始手册：`evidence/UNC/20.15.2/节点查询自动修复开关（LST-NODEREPSWITCH）_72291814.md`
- 原始手册：`evidence/UNC/20.15.2/节点设置自动修复开关（SET-NODEREPSWITCH）_72291815.md`
