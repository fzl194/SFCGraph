---
id: UDG@20.15.2@ConfigObject@MASALMDETAIL
type: ConfigObject
name: MASALMDETAIL（5G告警详细信息）
nf: UDG
version: 20.15.2
object_name: MASALMDETAIL
object_kind: query_target
status: active
---

# MASALMDETAIL（5G告警详细信息）

## 说明

该命令用于显示批量告警包含的详细故障信息。

> **说明**
> - 当“告警类型”选择为特定告警时，系统内可能存在许多原始告警，导致该命令返回时间过长，可通过在命令中限定“起始时间”和“结束时间”来减少查询记录数。
> - 由于批量告警是在原始告警产生后按照一定周期合并的结果，所以原始告警的实际故障时间早于批量告警的产生时间。
> - 如果批量告警进行了刷新，原始告警和批量告警的时间可能相差很多，因此当根据某条批量告警产生时间作为查询条件时，建议将“批量告警产生时间”作为本命令的“结束时间”。

## 操作本对象的命令

- [DSP MASALMDETAIL](command/UDG/20.15.2/DSP-MASALMDETAIL.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示5G告警详细信息（DSP-MASALMDETAIL）_80432526.md`
