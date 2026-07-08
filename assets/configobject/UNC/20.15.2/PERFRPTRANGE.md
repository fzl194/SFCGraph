---
id: UNC@20.15.2@ConfigObject@PERFRPTRANGE
type: ConfigObject
name: PERFRPTRANGE（性能指标上报范围）
nf: UNC
version: 20.15.2
object_name: PERFRPTRANGE
object_kind: entity
applicable_nf:
- SMF
- PGW-C
- GGSN
- AMF
status: active
---

# PERFRPTRANGE（性能指标上报范围）

## 说明

**适用NF：SMF、PGW-C、GGSN、AMF**

该命令用于配置AMF或SMF性能统计上报的性能统计指标范围。UNC预先定义一些话统指标为关键指标和基础指标，当在网管上下发测量对象失败，提示“下发对象失败”等错误信息，且DSP MEASSPECS命令查询实际预估原始指标量接近原始指标量规格，可以通过本命令修改网元向网管上报的实际性能统计范围。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PERFRPTRANGE]] · ADD PERFRPTRANGE
- [[command/UNC/20.15.2/LST-PERFRPTRANGE]] · LST PERFRPTRANGE
- [[command/UNC/20.15.2/MOD-PERFRPTRANGE]] · MOD PERFRPTRANGE
- [[command/UNC/20.15.2/RMV-PERFRPTRANGE]] · RMV PERFRPTRANGE

## 证据

- 原始手册：`evidence/UNC/20.15.2/PERFRPTRANGE.md`
- 原始手册：`evidence/UNC/20.15.2/PERFRPTRANGE.md`
- 原始手册：`evidence/UNC/20.15.2/PERFRPTRANGE.md`
- 原始手册：`evidence/UNC/20.15.2/PERFRPTRANGE.md`
