---
id: UDG@20.15.2@ConfigObject@FAULTCHECKBYFABRIC
type: ConfigObject
name: FAULTCHECKBYFABRIC（故障快速检测配置信息）
nf: UDG
version: 20.15.2
object_name: FAULTCHECKBYFABRIC
object_kind: global_setting
status: active
---

# FAULTCHECKBYFABRIC（故障快速检测配置信息）

## 说明

![](设置故障快速检测配置（SET FAULTCHECKBYFABRIC）_76431669.assets/notice_3.0-zh-cn.png)

该命令仅适用于单域模式下的指定网元，使用前需明确该功能是否适用于当前网元，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置基于Fabric链路状态的故障快速检测参数配置。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | ENABLE | PROTECTDURATION | WAITRPTDURATION |
> | --- | --- | --- |
> | OFF | 10 | 3000 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-FAULTCHECKBYFABRIC]] · LST FAULTCHECKBYFABRIC
- [[command/UDG/20.15.2/SET-FAULTCHECKBYFABRIC]] · SET FAULTCHECKBYFABRIC

## 证据

- 原始手册：`evidence/UDG/20.15.2/FAULTCHECKBYFABRIC.md`
- 原始手册：`evidence/UDG/20.15.2/FAULTCHECKBYFABRIC.md`
