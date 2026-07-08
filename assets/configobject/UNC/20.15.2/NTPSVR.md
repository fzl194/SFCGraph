---
id: UNC@20.15.2@ConfigObject@NTPSVR
type: ConfigObject
name: NTPSVR（NTP服务器）
nf: UNC
version: 20.15.2
object_name: NTPSVR
object_kind: entity
status: active
---

# NTPSVR（NTP服务器）

## 说明

本命令用于增加一条NTP服务器数据记录。

本命令的使用场景为：日常维护活动中，使用本命令增加NTP服务器。NTP服务器用于提供时钟同步源，各类设备通过外接NTP服务器来同步修正自身的时间，使其自身的时间更准确、精度更高。

在本命令中，以下参数需要与NTP服务器端协商：

- IP地址
- 身份验证标志
- 身份验证密钥号
- 密钥类型
- 密钥串

> **说明**
> 执行命令新增NTP服务器后，同步状态更新需等待约三个同步周期（默认一个同步周期为一分钟）。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NTPSVR]] · ADD NTPSVR
- [[command/UNC/20.15.2/LST-NTPSVR]] · LST NTPSVR
- [[command/UNC/20.15.2/MOD-NTPSVR]] · MOD NTPSVR
- [[command/UNC/20.15.2/RMV-NTPSVR]] · RMV NTPSVR

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改NTP服务器(MOD-NTPSVR)_67551556.md`
- 原始手册：`evidence/UNC/20.15.2/删除NTP服务器(RMV-NTPSVR)_54491177.md`
- 原始手册：`evidence/UNC/20.15.2/增加NTP服务器(ADD-NTPSVR)_54491176.md`
- 原始手册：`evidence/UNC/20.15.2/查询NTP服务器(LST-NTPSVR)_54491178.md`
