---
id: UNC@20.15.2@ConfigObject@GTPCSTATUSINFO
type: ConfigObject
name: GTPCSTATUSINFO（GTP-C路径当前及历史状态）
nf: UNC
version: 20.15.2
object_name: GTPCSTATUSINFO
object_kind: query_target
applicable_nf:
- SGW-C
- PGW-C
- AMF
- GGSN
status: active
---

# GTPCSTATUSINFO（GTP-C路径当前及历史状态）

## 说明

**适用NF：SGW-C、PGW-C、AMF、GGSN**

该命令用于查询GTP-C路径当前及历史状态记录，包括接口类型、路径状态变更、变更时间戳、以及本端对端地址等信息。当前支持每个进程最多显示100条历史路径。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-GTPCSTATUSINFO]] · DSP GTPCSTATUSINFO

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示GTP-C路径当前及历史状态（DSP-GTPCSTATUSINFO）_28955836.md`
