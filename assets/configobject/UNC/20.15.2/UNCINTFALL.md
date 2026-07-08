---
id: UNC@20.15.2@ConfigObject@UNCINTFALL
type: ConfigObject
name: UNCINTFALL（UNC所有接口名称）
nf: UNC
version: 20.15.2
object_name: UNCINTFALL
object_kind: entity
applicable_nf:
- SGSN
- MME
- SGW-C
- AMF
- PGW-C
- SMF
- NRF
- NSSF
- GGSN
- SMSF
- NCG
status: active
---

# UNCINTFALL（UNC所有接口名称）

## 说明

![](删除UNC所有接口名称（RMV UNCINTFALL）_50572312.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作此命令会导致已上报至北向的网元的接口信息全部被删除，影响北向上报。

**适用NF：SGSN、MME、SGW-C、AMF、PGW-C、SMF、NRF、NSSF、GGSN、SMSF、NCG**

该命令用于删除已经上报至网管北向UNC网元的所有业务或者管理接口的名称。

## 操作本对象的命令

- [[command/UNC/20.15.2/RMV-UNCINTFALL]] · RMV UNCINTFALL

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除UNC所有接口名称（RMV-UNCINTFALL）_50572312.md`
