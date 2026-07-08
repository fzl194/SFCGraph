---
id: UDG@20.15.2@ConfigObject@COMTASK
type: ConfigObject
name: COMTASK（SDR通信质量检测任务）
nf: UDG
version: 20.15.2
object_name: COMTASK
object_kind: action
status: active
---

# COMTASK（SDR通信质量检测任务）

## 说明

![](停止SDR通信质量检测任务（STP COMTASK）_63673353.assets/notice_3.0-zh-cn.png)

该命令是高危命令，操作不当可能会影响性能，请谨慎使用并联系华为技术支持协助操作。

该命令用于强制停止SDR通信质量检测任务。

> **说明**
> - 该命令执行后立即生效。
>
> - 如需确认检测任务是否已经停止，可通过[**DSP COMTASKSUMM**](显示SDR通信质量检测结果概要（DSP COMTASKSUMM）_63673343.md)查询SDR通信质量检测结果概要，若对应检测任务的停止时间不为空，则检测任务已经停止成功。
> - SRCID不存在时，停止命令执行成功，但停止任务不生效。

## 操作本对象的命令

- [[command/UDG/20.15.2/STP-COMTASK]] · STP COMTASK

## 证据

- 原始手册：`evidence/UDG/20.15.2/停止SDR通信质量检测任务（STP-COMTASK）_63673353.md`
