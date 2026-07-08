---
id: UNC@20.15.2@ConfigObject@NFSERVICE
type: ConfigObject
name: NFSERVICE（NF服务实例）
nf: UNC
version: 20.15.2
object_name: NFSERVICE
object_kind: entity
applicable_nf:
- AMF
- SMF
- NSSF
- NRF
- NCG
- SMSF
status: active
---

# NFSERVICE（NF服务实例）

## 说明

**适用NF：AMF、SMF、NSSF、NRF、NCG、SMSF**

该命令用于添加NF的服务实例信息，即NFS（Network Function Service）。当前NF实例向NRF注册时，同时需要配置其所支持的NFS实例。

SBA架构下的每个NF可以具备多种能力，例如会话创建、数据订阅等。NF的这些能力就是通过NFS（Network Function Service，网络功能服务）来承载的。

ADD NFPROFILE命令用于配置NF整体实例信息，本命令则用于配置NF内具体的NFS实例信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NFSERVICE]] · ADD NFSERVICE
- [[command/UNC/20.15.2/LST-NFSERVICE]] · LST NFSERVICE
- [[command/UNC/20.15.2/MOD-NFSERVICE]] · MOD NFSERVICE
- [[command/UNC/20.15.2/RMV-NFSERVICE]] · RMV NFSERVICE

## 证据

- 原始手册：`evidence/UNC/20.15.2/NFSERVICE.md`
- 原始手册：`evidence/UNC/20.15.2/NFSERVICE.md`
- 原始手册：`evidence/UNC/20.15.2/NFSERVICE.md`
- 原始手册：`evidence/UNC/20.15.2/NFSERVICE.md`
