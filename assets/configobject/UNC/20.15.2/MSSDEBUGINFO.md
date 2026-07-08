---
id: UNC@20.15.2@ConfigObject@MSSDEBUGINFO
type: ConfigObject
name: MSSDEBUGINFO（维测开关状态）
nf: UNC
version: 20.15.2
object_name: MSSDEBUGINFO
object_kind: query_target
status: active
---

# MSSDEBUGINFO（维测开关状态）

## 说明

该命令用于查询维测开关状态信息。

维测开关包括调度、保序和定时器维测开关，默认是关闭的。

例如，当需要定位调度线程是否异常切换，打开调度轨迹开关后通过查询维测命令查看开关是否打开。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-MSSDEBUGINFO]] · DSP MSSDEBUGINFO

## 证据

- 原始手册：`evidence/UNC/20.15.2/MSSDEBUGINFO.md`
