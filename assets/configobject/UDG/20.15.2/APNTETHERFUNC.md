---
id: UDG@20.15.2@ConfigObject@APNTETHERFUNC
type: ConfigObject
name: APNTETHERFUNC（APN Tethering检测开关）
nf: UDG
version: 20.15.2
object_name: APNTETHERFUNC
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# APNTETHERFUNC（APN Tethering检测开关）

## 说明

**适用NF：PGW-U、UPF**

![](设置APN Tethering检测开关（SET APNTETHERFUNC）_82837441.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该命令会导致用户匹配范围发生变化，可能导致性能下降。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。

该命令用于在APN下配置该APN是否启用Tethering检测功能。如果该APN是专属于支持Tethering的用户接入，则配置为使能，所有该APN接入用户都会被识别为Tethering用户。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-APNTETHERFUNC]] · LST APNTETHERFUNC
- [[command/UDG/20.15.2/SET-APNTETHERFUNC]] · SET APNTETHERFUNC

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询APN-Tethering检测开关（LST-APNTETHERFUNC）_82837442.md`
- 原始手册：`evidence/UDG/20.15.2/设置APN-Tethering检测开关（SET-APNTETHERFUNC）_82837441.md`
