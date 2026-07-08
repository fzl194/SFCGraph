---
id: UDG@20.15.2@ConfigObject@MEASTREND
type: ConfigObject
name: MEASTREND（话统指标统计趋势）
nf: UDG
version: 20.15.2
object_name: MEASTREND
object_kind: query_target
status: active
---

# MEASTREND（话统指标统计趋势）

## 说明

该命令用于查询网元的话统指标统计趋势。

> **说明**
> - 当系统处于存储故障状态时，只支持查询KPI类型的指标统计趋势，查询结果不支持“最近一周同时间段(按时间倒序)”数据的对比。
> - 网元升级后未结束升级观察期期间，支持查询高低版本指标统计趋势；结束升级观察期后，普通域仅支持查询高版本指标统计趋势。
> - 该命令返回结果条数存在如下限制：最多返回1000条。

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-MEASTREND]] · DSP MEASTREND

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询话统指标统计趋势(DSP-MEASTREND)_08447970.md`
