---
id: UNC@20.15.2@ConfigObject@TCTIMER
type: ConfigObject
name: TCTIMER（TC定时器）
nf: UNC
version: 20.15.2
object_name: TCTIMER
object_kind: global_setting
applicable_nf:
- PGW-C
- SMF
status: active
---

# TCTIMER（TC定时器）

## 说明

**适用NF：PGW-C、SMF**

该命令用于配置Diameter TC定时器。设置定时器时长，用来控制当UNC与OCS等Diameter对端断链后，重建链接的间隔时长。当此定时器超时，UNC则会向OCS等Diameter对端重新发起建链请求。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-TCTIMER]] · LST TCTIMER
- [[command/UNC/20.15.2/SET-TCTIMER]] · SET TCTIMER

## 证据

- 原始手册：`evidence/UNC/20.15.2/TCTIMER.md`
- 原始手册：`evidence/UNC/20.15.2/TCTIMER.md`
