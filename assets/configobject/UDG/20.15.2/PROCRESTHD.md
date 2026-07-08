---
id: UDG@20.15.2@ConfigObject@PROCRESTHD
type: ConfigObject
name: PROCRESTHD（进程资源告警阈值）
nf: UDG
version: 20.15.2
object_name: PROCRESTHD
object_kind: global_setting
status: active
---

# PROCRESTHD（进程资源告警阈值）

## 说明

![](设置进程资源告警阈值（SET PROCRESTHD）_07986436.assets/notice_3.0-zh-cn.png)

告警阈值的调整会影响告警的触发条件，请注意设置合理的告警阈值。

该命令用于设置进程的资源告警上报、清除阈值。

> **说明**
> 告警阈值会持久化到Gauss数据库中，各进程阈值更新会有一定的延迟，可通过 **[DSP PROCRESSTAT](查询进程资源信息（DSP PROCRESSTAT）_08146288.md)** 命令进行查看。
>
> 本命令若按照“进程类型”配置后再次按照“网元级”配置，则不覆盖该网元下的“进程类型”的配置。

## 操作本对象的命令

- [[command/UDG/20.15.2/SET-PROCRESTHD]] · SET PROCRESTHD

## 证据

- 原始手册：`evidence/UDG/20.15.2/PROCRESTHD.md`
