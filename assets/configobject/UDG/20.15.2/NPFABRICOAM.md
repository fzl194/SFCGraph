---
id: UDG@20.15.2@ConfigObject@NPFABRICOAM
type: ConfigObject
name: NPFABRICOAM（全局OAM相关配置）
nf: UDG
version: 20.15.2
object_name: NPFABRICOAM
object_kind: global_setting
status: active
---

# NPFABRICOAM（全局OAM相关配置）

## 说明

![](设置全局OAM相关配置（SET NPFABRICOAM）_94730515.assets/notice_3.0-zh-cn.png)

如果修改Fabric-OAM开关，影响系统可靠性，如果修改检测间隔，间隔过小或者过大，会导致丢包率上升或者检测能力降低。

该命令用来设置全局OAM相关配置：包括OAM使能，OAM报文检测周期，OAM报文超时检测倍数。

> **说明**
> - 该命令执行后立即生效。
>
> - 如果修改Fabric-OAM检测间隔，需要注意：间隔过小，会影响性能，导致丢包率上升；间隔过大，会导致检测能力降低。
> - 该命令仅适用于NP卡加速模式场景。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | OAMSWITCH | OAMINTERVAL | OAMMULTIPLIER |
> | --- | --- | --- |
> | Enable | 100 | 30 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-NPFABRICOAM]] · LST NPFABRICOAM
- [[command/UDG/20.15.2/SET-NPFABRICOAM]] · SET NPFABRICOAM

## 证据

- 原始手册：`evidence/UDG/20.15.2/NPFABRICOAM.md`
- 原始手册：`evidence/UDG/20.15.2/NPFABRICOAM.md`
