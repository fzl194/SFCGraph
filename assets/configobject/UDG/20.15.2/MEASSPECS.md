---
id: UDG@20.15.2@ConfigObject@MEASSPECS
type: ConfigObject
name: MEASSPECS（话统规格）
nf: UDG
version: 20.15.2
object_name: MEASSPECS
object_kind: query_target
status: active
---

# MEASSPECS（话统规格）

## 说明

通过DSP MEASSPECS命令可获得当前版本支持的话统总指标量，各网元各个周期已使用的指标量以及话统测量结果存储时长信息。

> **说明**
> 该接口查询结果为指标量预估值，部分场景下指标量计算结果可能存在一定误差，如全局对象实例增删或测量任务变更后指标量计算结果需等待1个测量周期查询较为准确。

## 操作本对象的命令

- [DSP MEASSPECS](command/UDG/20.15.2/DSP-MEASSPECS.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询话统规格(DSP-MEASSPECS)_01454532.md`
