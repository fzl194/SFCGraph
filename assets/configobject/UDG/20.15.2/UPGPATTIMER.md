---
id: UDG@20.15.2@ConfigObject@UPGPATTIMER
type: ConfigObject
name: UPGPATTIMER（升级补丁定时器）
nf: UDG
version: 20.15.2
object_name: UPGPATTIMER
object_kind: global_setting
status: active
---

# UPGPATTIMER（升级补丁定时器）

## 说明

该命令用于修改升级/补丁对应定时器的时长值。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> > **说明**
> > 此处仅展示前20条初始记录值，您可以通过相关查询命令查看全部记录值。
>
> | NAME | VALUE |
> | --- | --- |
> | UpgradeStackUpdateTimer | 40 |
> | PatchStackUpdateTimer | 20 |
> | PodDeleteTimer | 10 |
> | OSPatchPushTimer | 15 |
> | UpgradeCommonTimer1 | 5 |
> | UpgradeCommonTimer2 | 5 |
> | UpgradeCommonTimer3 | 5 |
> | UpgradeCommonTimer4 | 5 |
> | UpgradeCommonTimer5 | 5 |
> | UpgradeCommonTimer6 | 5 |
> | UpgradeCommonTimer7 | 5 |
> | UpgradeCommonTimer8 | 5 |
> | UpgradeCommonTimer9 | 5 |
> | UpgradeCommonTimer10 | 5 |
> | UpgradeCommonTimer11 | 10 |
> | UpgradeCommonTimer12 | 10 |
> | UpgradeCommonTimer13 | 10 |
> | UpgradeCommonTimer14 | 10 |
> | UpgradeCommonTimer15 | 10 |
> | UpgradeCommonTimer16 | 10 |

## 操作本对象的命令

- [LST UPGPATTIMER](command/UDG/20.15.2/LST-UPGPATTIMER.md)
- [SET UPGPATTIMER](command/UDG/20.15.2/SET-UPGPATTIMER.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改升级补丁定时器（SET-UPGPATTIMER）_30310144.md`
- 原始手册：`evidence/UDG/20.15.2/查询升级补丁定时器（LST-UPGPATTIMER）_30310142.md`
