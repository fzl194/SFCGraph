---
id: UNC@20.15.2@ConfigObject@NGDNSS
type: ConfigObject
name: NGDNSS（DNS服务器）
nf: UNC
version: 20.15.2
object_name: NGDNSS
object_kind: entity
applicable_nf:
- AMF
status: active
---

# NGDNSS（DNS服务器）

## 说明

**适用NF：AMF**

该命令用于服务化接口查询域名时增加一个DNS域名解析服务器。DNS服务器是网络中专门提供域名解析服务的服务器。

网元通过向DNS服务器发送域名解析请求，获得域名所对应IP地址。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NGDNSS]] · ADD NGDNSS
- [[command/UNC/20.15.2/LST-NGDNSS]] · LST NGDNSS
- [[command/UNC/20.15.2/MOD-NGDNSS]] · MOD NGDNSS
- [[command/UNC/20.15.2/RMV-NGDNSS]] · RMV NGDNSS

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改DNS服务器（MOD-NGDNSS）_25121198.md`
- 原始手册：`evidence/UNC/20.15.2/删除DNS服务器（RMV-NGDNSS）_25121204.md`
- 原始手册：`evidence/UNC/20.15.2/增加DNS服务器（ADD-NGDNSS）_25120874.md`
- 原始手册：`evidence/UNC/20.15.2/查询DNS服务器（LST-NGDNSS）_25120888.md`
