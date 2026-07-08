---
id: UDG@20.15.2@ConfigObject@NPWATCHDOG
type: ConfigObject
name: NPWATCHDOG（喂狗功能相关配置）
nf: UDG
version: 20.15.2
object_name: NPWATCHDOG
object_kind: global_setting
status: active
---

# NPWATCHDOG（喂狗功能相关配置）

## 说明

![](设置喂狗功能配置（SET NPWATCHDOG）_18818232.assets/notice_3.0-zh-cn.png)

如果修改喂狗检测周期，周期值过大或者过小，可能影响系统的可靠性。

该命令用于设置喂狗相关配置：包括喂狗检测周期，喂狗超时时长。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令仅适用于NP卡加速模式场景。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | INTERVAL | TIMEOUT |
> | --- | --- |
> | 500 | 24 |

## 操作本对象的命令

- [LST NPWATCHDOG](command/UDG/20.15.2/LST-NPWATCHDOG.md)
- [SET NPWATCHDOG](command/UDG/20.15.2/SET-NPWATCHDOG.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询喂狗功能相关配置（LST-NPWATCHDOG）_18818230.md`
- 原始手册：`evidence/UDG/20.15.2/设置喂狗功能配置（SET-NPWATCHDOG）_18818232.md`
