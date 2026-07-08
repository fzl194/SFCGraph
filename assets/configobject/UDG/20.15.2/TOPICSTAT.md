---
id: UDG@20.15.2@ConfigObject@TOPICSTAT
type: ConfigObject
name: TOPICSTAT（topic状态）
nf: UDG
version: 20.15.2
object_name: TOPICSTAT
object_kind: query_target
status: active
---

# TOPICSTAT（topic状态）

## 说明

该命令用于查询topic分区的详细信息，kafka各分区副本之间数据同步是否正常，以及分区leader是否正常选举等信息。

> **说明**
> - 支持输入参数为空时的全量查询，支持按照topic名称查询时进行模糊匹配。
> - 对部分不需要对外展示的topic信息（如拨测）会进行过滤。

## 操作本对象的命令

- [DSP TOPICSTAT](command/UDG/20.15.2/DSP-TOPICSTAT.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询topic状态（DSP-TOPICSTAT）_20988593.md`
