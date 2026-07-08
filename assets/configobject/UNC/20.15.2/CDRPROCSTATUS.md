---
id: UNC@20.15.2@ConfigObject@CDRPROCSTATUS
type: ConfigObject
name: CDRPROCSTATUS（话单处理状态）
nf: UNC
version: 20.15.2
object_name: CDRPROCSTATUS
object_kind: query_target
applicable_nf:
- NCG
status: active
---

# CDRPROCSTATUS（话单处理状态）

## 说明

**适用NF：NCG**

该命令用于显示话单处理状态。 [**DSP CDRPROCSTATUS**](显示话单处理状态（DSP CDRPROCSTATUS）_51174315.md) 命令执行后，返回当前处理的原始话单文件名、上次处理的话单包信息、待合并队列信息、原始和最终话单缓冲区话单数量。

在系统新安装、健康检查或者故障处理时，可以使用该命令获取话单处理的状态信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-CDRPROCSTATUS]] · DSP CDRPROCSTATUS

## 证据

- 原始手册：`evidence/UNC/20.15.2/CDRPROCSTATUS.md`
