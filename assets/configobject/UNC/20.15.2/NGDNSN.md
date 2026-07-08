---
id: UNC@20.15.2@ConfigObject@NGDNSN
type: ConfigObject
name: NGDNSN（DNS NAPTR记录）
nf: UNC
version: 20.15.2
object_name: NGDNSN
object_kind: entity
applicable_nf:
- AMF
- SMF
status: active
---

# NGDNSN（DNS NAPTR记录）

## 说明

**适用NF：AMF、SMF**

该命令用于配置FQDN与网元接口的对应关系。

在4/5G切换流程中会涉及到“MME”、“5G NF”等网元的选择，并解析出网元的地址信息。

该命令可以配置FQDN与网元节点间多对多的对应关系。

对于Proxy SGW特性，作为调测目的，可以通过添加网元类型为MME、接口类型为N26的记录来实现本地解析域名获取归属地PGW-C地址的功能。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NGDNSN]] · ADD NGDNSN
- [[command/UNC/20.15.2/LST-NGDNSN]] · LST NGDNSN
- [[command/UNC/20.15.2/MOD-NGDNSN]] · MOD NGDNSN
- [[command/UNC/20.15.2/RMV-NGDNSN]] · RMV NGDNSN

## 证据

- 原始手册：`evidence/UNC/20.15.2/NGDNSN.md`
- 原始手册：`evidence/UNC/20.15.2/NGDNSN.md`
- 原始手册：`evidence/UNC/20.15.2/NGDNSN.md`
- 原始手册：`evidence/UNC/20.15.2/NGDNSN.md`
