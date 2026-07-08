---
id: UDG@20.15.2@ConfigObject@GLOBALFABRICOAM
type: ConfigObject
name: GLOBALFABRICOAM（OAM全局配置）
nf: UDG
version: 20.15.2
object_name: GLOBALFABRICOAM
object_kind: global_setting
status: active
---

# GLOBALFABRICOAM（OAM全局配置）

## 说明

![](设置OAM全局配置（SET GLOBALFABRICOAM）_92520017.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致性能下降，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置全局OAM（Operation Administration and Maintenance）相关配置：包括OAM使能，OAM报文检测周期，OAM报文超时检测倍数。

报文转发时，需要根据链路状态进行快速选路、负载分担等，因此需要OAM功能检测Fabric口间的链路通断状态并提供依据。

设置全局OAM配置可以使能去使能Fabric OAM功能。OAM功能用来检测链路状态，建议开启，默认情况下也是开启的。

## 操作本对象的命令

- [LST GLOBALFABRICOAM](command/UDG/20.15.2/LST-GLOBALFABRICOAM.md)
- [SET GLOBALFABRICOAM](command/UDG/20.15.2/SET-GLOBALFABRICOAM.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OAM全局配置（LST-GLOBALFABRICOAM）_92520025.md`
- 原始手册：`evidence/UDG/20.15.2/设置OAM全局配置（SET-GLOBALFABRICOAM）_92520017.md`
