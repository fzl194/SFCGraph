---
id: UDG@20.15.2@ConfigObject@HTTPSTATS
type: ConfigObject
name: HTTPSTATS（HTTP统计信息）
nf: UDG
version: 20.15.2
object_name: HTTPSTATS
object_kind: action
status: active
---

# HTTPSTATS（HTTP统计信息）

## 说明

该命令用于显示HTTP相关的统计信息。HTTP相关模块包括了SBILINK、HTTPLINK。

> **说明**
> - 该命令中起始索引和终止索引用于命令后续扩展，使用需要注意起始索引必须小于等于终止索引，当起始索引等于终止索引时，即指定单个索引的统计结果输出。
> - 该命令中附加过滤条件为预留参数，便于后续输出过滤条件扩展使用。
> - 查询模块类型为HTTPLINK、子模块类型为HTTP并添加过滤条件时，MML的回显计数为0，将统计结果写入运行日志中。

## 操作本对象的命令

- [CLR HTTPSTATS](command/UDG/20.15.2/CLR-HTTPSTATS.md)
- [DSP HTTPSTATS](command/UDG/20.15.2/DSP-HTTPSTATS.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示HTTP统计信息（DSP-HTTPSTATS）_83972184.md`
- 原始手册：`evidence/UDG/20.15.2/清除HTTP统计信息（CLR-HTTPSTATS）_29291765.md`
