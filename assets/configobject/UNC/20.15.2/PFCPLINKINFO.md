---
id: UNC@20.15.2@ConfigObject@PFCPLINKINFO
type: ConfigObject
name: PFCPLINKINFO（PFCP链路当前及历史状态）
nf: UNC
version: 20.15.2
object_name: PFCPLINKINFO
object_kind: query_target
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
status: active
---

# PFCPLINKINFO（PFCP链路当前及历史状态）

## 说明

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于查询PFCP链路当前及历史状态记录，包括接口类型、链路状态变更、变更时间戳、以及本端对端地址等信息。当前支持每个进程最多显示100条历史链路。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-PFCPLINKINFO]] · DSP PFCPLINKINFO

## 证据

- 原始手册：`evidence/UNC/20.15.2/PFCPLINKINFO.md`
