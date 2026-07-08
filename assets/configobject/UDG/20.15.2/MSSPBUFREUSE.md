---
id: UDG@20.15.2@ConfigObject@MSSPBUFREUSE
type: ConfigObject
name: MSSPBUFREUSE（PBUF重用信息）
nf: UDG
version: 20.15.2
object_name: MSSPBUFREUSE
object_kind: global_setting
status: active
---

# MSSPBUFREUSE（PBUF重用信息）

## 说明

![](设置PBUF重用检测开关（SET MSSPBUFREUSE）_92520004.assets/notice_3.0-zh-cn.png)

本命令用于使能PBUF重用检测，开启后会降低性能且在24小时之后会自动去使能，关闭后会恢复性能。此命令仅在SET PBUFREUSE5GC未设置时生效，可以通过LST PBUFREUSE5GC查询是否有设置。

此命令用于设置MSS的PBUF重用检测开关，重用检测功能用来检测多个进程是否同时在使用同一片PBUF。

用户打开开关后，系统收集运行信息，导致转发面性能下降。打开开关后24小时后会自动关闭。

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-MSSPBUFREUSE]] · DSP MSSPBUFREUSE
- [[command/UDG/20.15.2/SET-MSSPBUFREUSE]] · SET MSSPBUFREUSE

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示PBUF重用信息（DSP-MSSPBUFREUSE）_32207987.md`
- 原始手册：`evidence/UDG/20.15.2/设置PBUF重用检测开关（SET-MSSPBUFREUSE）_92520004.md`
