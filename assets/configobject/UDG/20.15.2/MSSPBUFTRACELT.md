---
id: UDG@20.15.2@ConfigObject@MSSPBUFTRACELT
type: ConfigObject
name: MSSPBUFTRACELT（PBUF轨迹开关状态和持续时间）
nf: UDG
version: 20.15.2
object_name: MSSPBUFTRACELT
object_kind: global_setting
status: active
---

# MSSPBUFTRACELT（PBUF轨迹开关状态和持续时间）

## 说明

![](设置PBUF轨迹开关和持续时间（SET MSSPBUFTRACELT）_45801325.assets/notice_3.0-zh-cn.png)

本命令用于使能PBUF轨迹开关，开启后会降低性能且在用户指定的时间后会自动去使能，关闭后会恢复性能。默认时间是24小时。

该命令用于设置MSS的PBUF轨迹开关和持续时间。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | TRACESWITCH | TIME |
> | --- | --- |
> | ON | 1440 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-MSSPBUFTRACELT]] · LST MSSPBUFTRACELT
- [[command/UDG/20.15.2/SET-MSSPBUFTRACELT]] · SET MSSPBUFTRACELT

## 证据

- 原始手册：`evidence/UDG/20.15.2/MSSPBUFTRACELT.md`
- 原始手册：`evidence/UDG/20.15.2/MSSPBUFTRACELT.md`
