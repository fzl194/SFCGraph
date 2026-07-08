---
id: UNC@20.15.2@ConfigObject@PSEUDONYPOLICY
type: ConfigObject
name: PSEUDONYPOLICY（CHR假名化本地策略）
nf: UNC
version: 20.15.2
object_name: PSEUDONYPOLICY
object_kind: global_setting
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SGSN
- MME
- SGW-C
- PGW-C
- NCG
- SMSF
status: active
---

# PSEUDONYPOLICY（CHR假名化本地策略）

## 说明

**适用NF：AMF、SMF、NRF、NSSF、SGSN、MME、SGW-C、PGW-C、NCG、SMSF**

该命令用于设置CHR假名化本地策略，UNC的CHR假名化功能可以通过该命令配置本地策略，也可以通过网管集中配置。当UNC未连接网管，或已连接网管但网管上未进行假名化功能设置时，根据该命令配置判断是否做CHR假名化处理。当UNC已连接网管且网管上已有假名化功能配置时，根据网管上配置的假名化功能状态判断是否做CHR假名化处理。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-PSEUDONYPOLICY]] · LST PSEUDONYPOLICY
- [[command/UNC/20.15.2/SET-PSEUDONYPOLICY]] · SET PSEUDONYPOLICY

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CHR假名化本地策略（LST-PSEUDONYPOLICY）_51175629.md`
- 原始手册：`evidence/UNC/20.15.2/设置CHR假名化本地策略（SET-PSEUDONYPOLICY）_51175645.md`
