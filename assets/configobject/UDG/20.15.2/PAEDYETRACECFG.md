---
id: UDG@20.15.2@ConfigObject@PAEDYETRACECFG
type: ConfigObject
name: PAEDYETRACECFG（PAE染色流控开关及阈值参数）
nf: UDG
version: 20.15.2
object_name: PAEDYETRACECFG
object_kind: global_setting
status: active
---

# PAEDYETRACECFG（PAE染色流控开关及阈值参数）

## 说明

![](设置PAE染色流控开关及阈值参数（SET PAEDYETRACECFG）_20679422.assets/notice_3.0-zh-cn.png)

该命令是高危命令。染色流控开关关闭后，染色跟踪流控功能失效，可能会对现有业务造成影响，请谨慎操作。

该命令用于修改PAE染色跟踪流控开关及阈值参数。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | FLOWSWITCH | STARTFLOW_X86 | STOPFLOW_X86 | STARTFLOW_ARM | STOPFLOW_ARM | DYECPUPERFLMT |
> | --- | --- | --- | --- | --- | --- |
> | ON | 880 | 800 | 1000 | 900 | 40 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-PAEDYETRACECFG]] · LST PAEDYETRACECFG
- [[command/UDG/20.15.2/SET-PAEDYETRACECFG]] · SET PAEDYETRACECFG

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询PAE染色流控开关及阈值参数（LST-PAEDYETRACECFG）_20521310.md`
- 原始手册：`evidence/UDG/20.15.2/设置PAE染色流控开关及阈值参数（SET-PAEDYETRACECFG）_20679422.md`
