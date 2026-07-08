---
id: UNC@20.15.2@ConfigObject@LDMINNERDATA
type: ConfigObject
name: LDMINNERDATA（LDM诊断信息）
nf: UNC
version: 20.15.2
object_name: LDMINNERDATA
object_kind: query_target
status: active
---

# LDMINNERDATA（LDM诊断信息）

## 说明

该命令用于查询LDM诊断信息。不指定CID参数时，查询所有LDM的诊断信息，当指定CID参数时，查询指定LDM诊断信息。当内部数据类型为TCP_CONTROL_PACKET时，若SOCKID、PORTNUM不指定时，默认为0，不显示诊断信息数据。

## 操作本对象的命令

- [DSP LDMINNERDATA](command/UNC/20.15.2/DSP-LDMINNERDATA.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询LDM诊断信息（DSP-LDMINNERDATA）_50281178.md`
