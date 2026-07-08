---
id: UNC@20.15.2@ConfigObject@PNFTAIRANGE
type: ConfigObject
name: PNFTAIRANGE（对端NF的TAI范围）
nf: UNC
version: 20.15.2
object_name: PNFTAIRANGE
object_kind: entity
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
- PGW-C
- SGW-C
status: active
---

# PNFTAIRANGE（对端NF的TAI范围）

## 说明

**适用NF：AMF、SMF、NSSF、SMSF、NCG、PGW-C、SGW-C**

该命令用于增加本地配置的对端NF实例支持的TAI范围信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PNFTAIRANGE]] · ADD PNFTAIRANGE
- [[command/UNC/20.15.2/LST-PNFTAIRANGE]] · LST PNFTAIRANGE
- [[command/UNC/20.15.2/MOD-PNFTAIRANGE]] · MOD PNFTAIRANGE
- [[command/UNC/20.15.2/RMV-PNFTAIRANGE]] · RMV PNFTAIRANGE

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改对端NF的TAI范围（MOD-PNFTAIRANGE）_09651786.md`
- 原始手册：`evidence/UNC/20.15.2/删除对端NF的TAI范围（RMV-PNFTAIRANGE）_09653128.md`
- 原始手册：`evidence/UNC/20.15.2/增加对端NF的TAI范围（ADD-PNFTAIRANGE）_09652649.md`
- 原始手册：`evidence/UNC/20.15.2/查询对端NF的TAI范围（LST-PNFTAIRANGE）_09651561.md`
