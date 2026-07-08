---
id: UNC@20.15.2@ConfigObject@UNCIPRESOUCE
type: ConfigObject
name: UNCIPRESOUCE（UNC接口IP地址）
nf: UNC
version: 20.15.2
object_name: UNCIPRESOUCE
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

# UNCIPRESOUCE（UNC接口IP地址）

## 说明

**适用NF：SGSN、MME、SGW-C、PGW-C、AMF、SMF、NRF、NSSF、GGSN、SMSF、NCG**

该命令用于增加需要上报给网管北向的UNC网元业务和管理接口的IP地址。需要在网管北向上查看UNC网元业务和管理接口的IP地址时，可以通过此命令进行配置。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-UNCIPRESOUCE]] · ADD UNCIPRESOUCE
- [[command/UNC/20.15.2/LST-UNCIPRESOUCE]] · LST UNCIPRESOUCE
- [[command/UNC/20.15.2/RMV-UNCIPRESOUCE]] · RMV UNCIPRESOUCE

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除UNC接口IP地址（RMV-UNCIPRESOUCE）_68625989.md`
- 原始手册：`evidence/UNC/20.15.2/增加UNC接口IP地址(ADD-UNCIPRESOUCE)_32393460.md`
- 原始手册：`evidence/UNC/20.15.2/查询UNC接口IP地址（LST-UNCIPRESOUCE）_17146834.md`
