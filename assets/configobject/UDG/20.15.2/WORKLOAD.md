---
id: UDG@20.15.2@ConfigObject@WORKLOAD
type: ConfigObject
name: WORKLOAD（系统负载）
nf: UDG
version: 20.15.2
object_name: WORKLOAD
object_kind: query_target
status: active
---

# WORKLOAD（系统负载）

## 说明

该命令用来查看VNFC下所有ScaleGroup的负载。当前VNFC的负载是由多项指标（内存指标、CPU指标）中取最高值得到的。其中内存指标是业务上报的多个内存相关的百分比中的最高值；CPU指标为对应ScaleGroup下所有RU的CPU占用率的平均值。

该命令在合一KPI模式下使用，在多KPI模式下不使用。查询KPI模式，请通过命令查看。

## 操作本对象的命令

- [DSP WORKLOAD](command/UDG/20.15.2/DSP-WORKLOAD.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询系统负载(DSP-WORKLOAD)_29626911.md`
