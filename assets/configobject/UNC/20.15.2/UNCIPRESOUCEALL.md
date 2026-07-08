---
id: UNC@20.15.2@ConfigObject@UNCIPRESOUCEALL
type: ConfigObject
name: UNCIPRESOUCEALL（UNC所有接口的IP地址）
nf: UNC
version: 20.15.2
object_name: UNCIPRESOUCEALL
object_kind: entity
applicable_nf:
- SGSN
- MME
- SGW-C
- PGW-C
- AMF
- SMF
- NRF
- NSSF
- GGSN
- SMSF
- NCG
status: active
---

# UNCIPRESOUCEALL（UNC所有接口的IP地址）

## 说明

![](删除UNC所有接口的IP地址（RMV UNCIPRESOUCEALL）_23324806.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作此命令会导致已上报至北向的网元的IP资源信息全部被删除，影响北向上报。

**适用NF：SGSN、MME、SGW-C、PGW-C、AMF、SMF、NRF、NSSF、GGSN、SMSF、NCG**

该命令用于删除已经上报给网管北向UNC网元的所有业务和管理接口的IP地址。

## 操作本对象的命令

- [[command/UNC/20.15.2/RMV-UNCIPRESOUCEALL]] · RMV UNCIPRESOUCEALL

## 证据

- 原始手册：`evidence/UNC/20.15.2/UNCIPRESOUCEALL.md`
