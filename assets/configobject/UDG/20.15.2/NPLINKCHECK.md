---
id: UDG@20.15.2@ConfigObject@NPLINKCHECK
type: ConfigObject
name: NPLINKCHECK（全局NP交换网口检测配置）
nf: UDG
version: 20.15.2
object_name: NPLINKCHECK
object_kind: global_setting
status: active
---

# NPLINKCHECK（全局NP交换网口检测配置）

## 说明

![](设置NP交换网口检测配置（SET NPLINKCHECK）_94730516.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，请合理设置相关参数，关闭网口检测开关会影响系统可靠性，检测周期太短会导致误检，检测周期太长会导致端口故障无法及时隔离，请谨慎使用并联系华为技术支持协助操作。

该命令用来设置NP交换网口检测配置：包括端口检测使能、端口检测周期、端口检测超时检测倍数。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令仅适用于NP卡加速模式场景。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SWITCH | INTERVAL | MULTIPLIER |
> | --- | --- | --- |
> | Enable | 100 | 15 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-NPLINKCHECK]] · LST NPLINKCHECK
- [[command/UDG/20.15.2/SET-NPLINKCHECK]] · SET NPLINKCHECK

## 证据

- 原始手册：`evidence/UDG/20.15.2/NPLINKCHECK.md`
- 原始手册：`evidence/UDG/20.15.2/NPLINKCHECK.md`
