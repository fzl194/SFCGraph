---
id: UDG@20.15.2@ConfigObject@DRCOUPLINGRESET
type: ConfigObject
name: DRCOUPLINGRESET（负荷分担容灾功能开启信息）
nf: UDG
version: 20.15.2
object_name: DRCOUPLINGRESET
object_kind: global_setting
status: active
---

# DRCOUPLINGRESET（负荷分担容灾功能开启信息）

## 说明

![](设置是否开启负荷分担容灾功能（SET DRCOUPLINGRESET）_74474841.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，开启前请确认主备容灾已关闭，否则可能会导致业务呼损。请谨慎使用。

该命令用于设置是否开启负荷分担容灾功能。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令只用于在UEG-M/UEG-L/UEG采用负荷分担容灾模式下执行。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | COUPLINGRESET |
> | --- |
> | NO |

## 操作本对象的命令

- [LST DRCOUPLINGRESET](command/UDG/20.15.2/LST-DRCOUPLINGRESET.md)
- [SET DRCOUPLINGRESET](command/UDG/20.15.2/SET-DRCOUPLINGRESET.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询负荷分担容灾功能开启信息（LST-DRCOUPLINGRESET）_74474837.md`
- 原始手册：`evidence/UDG/20.15.2/设置是否开启负荷分担容灾功能（SET-DRCOUPLINGRESET）_74474841.md`
