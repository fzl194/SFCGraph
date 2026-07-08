---
id: UNC@20.15.2@ConfigObject@NFREGNRF
type: ConfigObject
name: NFREGNRF（本端NF和对端NRF实例的注册关系）
nf: UNC
version: 20.15.2
object_name: NFREGNRF
object_kind: entity
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
- CBCF
status: active
---

# NFREGNRF（本端NF和对端NRF实例的注册关系）

## 说明

**适用NF：AMF、SMF、NRF、NSSF、NCG、CBCF**

该命令用于增加本端NF和对端NRF实例的注册关系。

该命令应用场景如下：

- NF（包括AMF、SMF、NSSF、BSF）和NRF共部署时，该命令用于指定本端NF和NRF分别向哪些对端NRF实例（ADD NRF配置）注册。
- 仅部署NRF时，该命令用于指定本端NRF向哪些对端NRF实例注册。
- 仅部署NF（包括AMF、SMF、NSSF、BSF）时，该命令无需配置。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NFREGNRF]] · ADD NFREGNRF
- [[command/UNC/20.15.2/LST-NFREGNRF]] · LST NFREGNRF
- [[command/UNC/20.15.2/MOD-NFREGNRF]] · MOD NFREGNRF
- [[command/UNC/20.15.2/RMV-NFREGNRF]] · RMV NFREGNRF

## 证据

- 原始手册：`evidence/UNC/20.15.2/NFREGNRF.md`
- 原始手册：`evidence/UNC/20.15.2/NFREGNRF.md`
- 原始手册：`evidence/UNC/20.15.2/NFREGNRF.md`
- 原始手册：`evidence/UNC/20.15.2/NFREGNRF.md`
