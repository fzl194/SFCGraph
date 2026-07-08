---
id: UDG@20.15.2@ConfigObject@MSSPBUFTRACE
type: ConfigObject
name: MSSPBUFTRACE（PBUF轨迹设置的开关）
nf: UDG
version: 20.15.2
object_name: MSSPBUFTRACE
object_kind: global_setting
status: active
---

# MSSPBUFTRACE（PBUF轨迹设置的开关）

## 说明

![](设置PBUF轨迹设置的开关（SET MSSPBUFTRACE）_85410312.assets/notice_3.0-zh-cn.png)

本命令用于使能PBUF轨迹开关，开启后会降低性能且在用户指定的时间之后会自动去使能，关闭后会恢复性能。默认时间是24小时。

此命令用于设置MSS的PBUF轨迹设置开关，轨迹功能用来记录该PBUF所经过的各种操作。

用户打开开关后，系统收集运行信息，导致转发面性能下降。打开开关后在用户指定的时间自动关闭，默认时间是24小时。

## 操作本对象的命令

- [SET MSSPBUFTRACE](command/UDG/20.15.2/SET-MSSPBUFTRACE.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置PBUF轨迹设置的开关（SET-MSSPBUFTRACE）_85410312.md`
