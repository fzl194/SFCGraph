---
id: UDG@20.15.2@ConfigObject@KPIMONSWITCH
type: ConfigObject
name: KPIMONSWITCH（KPI异常检测功能开关）
nf: UDG
version: 20.15.2
object_name: KPIMONSWITCH
object_kind: global_setting
status: active
---

# KPIMONSWITCH（KPI异常检测功能开关）

## 说明

![](设置KPI异常检测功能开关（SET KPIMONSWITCH）_35322753.assets/notice_3.0-zh-cn.png)

关闭开关会清理掉持久化数据，重新打开检测开关后，需要重新累积7天KPI数据才做检测。

该命令用于设置KPI异常检测功能开关。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SWITCH |
> | --- |
> | ON |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-KPIMONSWITCH]] · LST KPIMONSWITCH
- [[command/UDG/20.15.2/SET-KPIMONSWITCH]] · SET KPIMONSWITCH

## 证据

- 原始手册：`evidence/UDG/20.15.2/KPIMONSWITCH.md`
- 原始手册：`evidence/UDG/20.15.2/KPIMONSWITCH.md`
