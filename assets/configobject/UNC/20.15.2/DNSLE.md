---
id: UNC@20.15.2@ConfigObject@DNSLE
type: ConfigObject
name: DNSLE（DNS Client IP与DNS实体的绑定关系）
nf: UNC
version: 20.15.2
object_name: DNSLE
object_kind: entity
applicable_nf:
- SGSN
- MME
- AMF
status: active
---

# DNSLE（DNS Client IP与DNS实体的绑定关系）

## 说明

**适用网元：SGSN、MME** **、AMF**

该命令用于增加DNS本端实体，包括：IP地址、端口、VPN名称，以便和DNS服务器进行通信。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-DNSLE]] · ADD DNSLE
- [[command/UNC/20.15.2/LST-DNSLE]] · LST DNSLE
- [[command/UNC/20.15.2/RMV-DNSLE]] · RMV DNSLE

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DNS-Client-IP与DNS实体的绑定关系(RMV-DNSLE)_26305698.md`
- 原始手册：`evidence/UNC/20.15.2/增加DNS实体绑定DNS-Client-IP(ADD-DNSLE)_72225567.md`
- 原始手册：`evidence/UNC/20.15.2/查询DNS-Client-IP与DNS实体的绑定关系(LST-DNSLE)_72345489.md`
