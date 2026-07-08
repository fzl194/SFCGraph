---
id: UDG@20.15.2@ConfigObject@SRVCOMMONPARA
type: ConfigObject
name: SRVCOMMONPARA（业务公共参数）
nf: UDG
version: 20.15.2
object_name: SRVCOMMONPARA
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# SRVCOMMONPARA（业务公共参数）

## 说明

**适用NF：PGW-U、UPF**

![](设置业务公共参数（SET SRVCOMMONPARA）_82837309.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，可能会影响业务。

该命令用来配置业务相关控制参数，如RTSP业务在暂停时是否收费的标识以及RTSP按照什么模式计费，业务可以使用的默认流量和时长配额等。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-SRVCOMMONPARA]] · LST SRVCOMMONPARA
- [[command/UDG/20.15.2/SET-SRVCOMMONPARA]] · SET SRVCOMMONPARA

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询业务公共参数（LST-SRVCOMMONPARA）_82837310.md`
- 原始手册：`evidence/UDG/20.15.2/设置业务公共参数（SET-SRVCOMMONPARA）_82837309.md`
