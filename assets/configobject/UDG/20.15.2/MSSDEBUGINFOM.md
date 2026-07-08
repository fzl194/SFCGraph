---
id: UDG@20.15.2@ConfigObject@MSSDEBUGINFOM
type: ConfigObject
name: MSSDEBUGINFOM（维测开关状态）
nf: UDG
version: 20.15.2
object_name: MSSDEBUGINFOM
object_kind: query_target
status: active
---

# MSSDEBUGINFOM（维测开关状态）

## 说明

该命令用于显示维测开关状态信息。

维测开关包括调度、保序和定时器维测开关，默认是关闭的。

例如，当需要定位调度线程是否异常切换，打开调度轨迹维测开关后通过查询维测命令查看开关是否打开。

## 操作本对象的命令

- [DSP MSSDEBUGINFOM](command/UDG/20.15.2/DSP-MSSDEBUGINFOM.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示维测开关状态（DSP-MSSDEBUGINFOM）_92520034.md`
