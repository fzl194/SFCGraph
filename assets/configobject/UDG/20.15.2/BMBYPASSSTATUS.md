---
id: UDG@20.15.2@ConfigObject@BMBYPASSSTATUS
type: ConfigObject
name: BMBYPASSSTATUS（裸机BYPASS状态）
nf: UDG
version: 20.15.2
object_name: BMBYPASSSTATUS
object_kind: global_setting
status: active
---

# BMBYPASSSTATUS（裸机BYPASS状态）

## 说明

![](设置裸机BYPASS状态（SET BMBYPASSSTATUS）_58599098.assets/notice_3.0-zh-cn.png)

设置进入BYPASS状态后，仅最小维护通道功能可用；设置退出BYPASS状态前请确认 [ALM-135552 节点存储亚健康](../../../../../../网络运维/故障处理/Framework告警/ALM-135552 节点存储亚健康_57945194.md) 告警已经恢复，请慎重使用该命令。

本命令用于手动设置裸机场景下Pod当前BYPASS状态。

- 若需要设置所有裸机场景下Pod的BYPASS状态，只需要输入“网元ID”即可。
- 若需要设置指定裸机场景下Pod的BYPASS状态，需要输入“网元ID”和“Pod名称”参数。

> **说明**
> 该命令仅在Full-stack裸机场景下支持。

> **说明**
> - 该命令仅限系统管理员可以执行。
> - BYPASS状态存在系统初始记录，参数的初始设置值如下：
>
> | 参数名称 | 设置初始值 |
> | --- | --- |
> | BYPASS状态 | Normal |

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-BMBYPASSSTATUS]] · DSP BMBYPASSSTATUS
- [[command/UDG/20.15.2/SET-BMBYPASSSTATUS]] · SET BMBYPASSSTATUS

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询裸机BYPASS状态（DSP-BMBYPASSSTATUS）_58439178.md`
- 原始手册：`evidence/UDG/20.15.2/设置裸机BYPASS状态（SET-BMBYPASSSTATUS）_58599098.md`
