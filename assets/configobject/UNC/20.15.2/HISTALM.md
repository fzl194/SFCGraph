---
id: UNC@20.15.2@ConfigObject@HISTALM
type: ConfigObject
name: HISTALM（历史告警）
nf: UNC
version: 20.15.2
object_name: HISTALM
object_kind: query_target
status: active
---

# HISTALM（历史告警）

## 说明

本命令用于查询系统内历史告警，可以通过OM Portal的 “ 监控分析 > 告警管理 > 历史告警 ” 进行查看，查询结果为最新产生的告警。

> **说明**
> 该MML除能查到OM Portal的 “ 监控分析 > 告警管理 > 历史告警 ” 的故障告警外，还支持查询 “事件告警” 和 “未确定告警” 。故障告警对系统有不同程度影响，而 “事件告警” 对系统无影响， “未确定告警” 则对系统影响程度无法确定，因此不会在OM Portal界面呈现。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-HISTALM]] · LST HISTALM

## 证据

- 原始手册：`evidence/UNC/20.15.2/HISTALM.md`
