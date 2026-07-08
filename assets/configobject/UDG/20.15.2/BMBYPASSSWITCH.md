---
id: UDG@20.15.2@ConfigObject@BMBYPASSSWITCH
type: ConfigObject
name: BMBYPASSSWITCH（裸机节点自动进入BYPASS开关）
nf: UDG
version: 20.15.2
object_name: BMBYPASSSWITCH
object_kind: global_setting
status: active
---

# BMBYPASSSWITCH（裸机节点自动进入BYPASS开关）

## 说明

![](设置裸机节点自动进入BYPASS开关（SET BMBYPASSSWITCH）_58120294.assets/notice_3.0-zh-cn.png)

在存储故障场景，节点可能无法自动进入BYPASS状态，请慎重使用该命令。

本命令用于设置存储故障时，裸机节点是否自动进入BYPASS状态。

> **说明**
> 该命令仅在Full-stack裸机场景下支持。

> **说明**
> - 如果关闭此开关，存储故障修复后，存储故障告警无法自动恢复，需要通过手工进入、退出BYPASS触发恢复流程或重启节点修复存储故障告警。
> - 该命令存在系统初始记录，参数的初始设置值如下：
>
> | 参数名称 | 初始设置值 |
> | --- | --- |
> | 自动进入BYPASS开关 | 开启 |

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-BMBYPASSSWITCH]] · DSP BMBYPASSSWITCH
- [[command/UDG/20.15.2/SET-BMBYPASSSWITCH]] · SET BMBYPASSSWITCH

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询裸机节点自动进入BYPASS开关（DSP-BMBYPASSSWITCH）_08719037.md`
- 原始手册：`evidence/UDG/20.15.2/设置裸机节点自动进入BYPASS开关（SET-BMBYPASSSWITCH）_58120294.md`
