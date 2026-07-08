---
id: UDG@20.15.2@ConfigObject@RESCHKSWITCH
type: ConfigObject
name: RESCHKSWITCH（RCF核查开关状态）
nf: UDG
version: 20.15.2
object_name: RESCHKSWITCH
object_kind: global_setting
status: active
---

# RESCHKSWITCH（RCF核查开关状态）

## 说明

![](设置RCF核查开关状态（SET RESCHKSWITCH）_03794482.assets/notice_3.0-zh-cn.png)

关闭RCF核查开关，可能会导致服务间数据不一致。请务必在华为技术支持的指导下使用该命令。

该命令用于开启或关闭RCF核查功能。

> **说明**
> - 如果当前有核查任务正在执行，不会中断当前任务，下次任务再生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SWITCH |
> | --- |
> | ON |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-RESCHKSWITCH]] · LST RESCHKSWITCH
- [[command/UDG/20.15.2/SET-RESCHKSWITCH]] · SET RESCHKSWITCH

## 证据

- 原始手册：`evidence/UDG/20.15.2/RESCHKSWITCH.md`
- 原始手册：`evidence/UDG/20.15.2/RESCHKSWITCH.md`
