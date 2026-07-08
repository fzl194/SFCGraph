---
id: UNC@20.15.2@ConfigObject@MSSCOMMSTAT
type: ConfigObject
name: MSSCOMMSTAT（通信模块规则匹配统计信息）
nf: UNC
version: 20.15.2
object_name: MSSCOMMSTAT
object_kind: query_target
status: active
---

# MSSCOMMSTAT（通信模块规则匹配统计信息）

## 说明

该命令用于查询COMM规则匹配统计计数信息。

COMM消息、报文的正常流程或者异常流程的规则匹配开关默认关闭，当开关关闭时，查询信息无统计计数。

例如，当发现丢包时，可打开规则匹配开关，并设置匹配规则，然后执行该命令查询COMM规则匹配统计计数，判断是否是COMM丢包。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-MSSCOMMSTAT]] · DSP MSSCOMMSTAT

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询通信模块规则匹配统计信息（DSP-MSSCOMMSTAT）_50120646.md`
