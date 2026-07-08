---
id: UNC@20.15.2@ConfigObject@FAULTDETECT
type: ConfigObject
name: FAULTDETECT（故障策略信息）
nf: UNC
version: 20.15.2
object_name: FAULTDETECT
object_kind: global_setting
status: active
---

# FAULTDETECT（故障策略信息）

## 说明

![](设置故障策略配置（SET FAULTDETECT）_59103724.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，如果使能该功能且OMU双离线将导致资源单元强制软复位，操作不当会使得资源单元承载的业务受影响，请谨慎使用并联系华为技术支持协助操作。

该命令用于配置故障策略信息。

故障快速上报功能用于OMU快速感知业务单元故障，进程间通信检查功能用于检查进程间的通信质量。

故障快速上报功能和进程间通信检查功能默认打开，如果关闭对于业务可靠性有影响，这两个功能主要用于调试使用，建议谨慎操作。

OMU双离线强制复位资源单元功能用于OMU双离线后，配置资源单元强制复位。复位开关使能时，默认强制软复位。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-FAULTDETECT]] · LST FAULTDETECT
- [[command/UNC/20.15.2/SET-FAULTDETECT]] · SET FAULTDETECT

## 证据

- 原始手册：`evidence/UNC/20.15.2/FAULTDETECT.md`
- 原始手册：`evidence/UNC/20.15.2/FAULTDETECT.md`
