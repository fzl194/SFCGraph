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

- [ADD PERFRPTRANGE](command/UNC/20.15.2/ADD-PERFRPTRANGE.md)
- [LST PERFRPTRANGE](command/UNC/20.15.2/LST-PERFRPTRANGE.md)
- [MOD PERFRPTRANGE](command/UNC/20.15.2/MOD-PERFRPTRANGE.md)
- [RMV PERFRPTRANGE](command/UNC/20.15.2/RMV-PERFRPTRANGE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改性能指标上报范围（MOD-PERFRPTRANGE）_15559494.md`
- 原始手册：`evidence/UNC/20.15.2/删除性能指标上报范围（RMV-PERFRPTRANGE）_59999367.md`
- 原始手册：`evidence/UNC/20.15.2/增加性能指标上报范围（ADD-PERFRPTRANGE）_59879437.md`
- 原始手册：`evidence/UNC/20.15.2/查询性能指标上报范围（LST-PERFRPTRANGE）_15399534.md`
