---
id: UDG@20.15.2@ConfigObject@DNSRULE
type: ConfigObject
name: DNSRULE（DNS规则）
nf: UDG
version: 20.15.2
object_name: DNSRULE
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# DNSRULE（DNS规则）

## 说明

**适用NF：PGW-U、UPF**

当系统为处于边缘节点的应用提供DNSLite业务时，该命令用于新增一条DNS规则，该DNS规则被称为静态DNS规则。

DNS规则是一种具有域名匹配功能的分流规则，包含了服务器域名和服务器 IP地址的对应关系。基于DNS规则分流可以实现以下功能：当数据流的报文中携带服务器的域名时，如果命中DNS Rule，则返回DNS响应，将服务器的IP地址返回给UE。当数据流的报文根据域名返回的IP地址发送数据报文时，支持基于服务器的IP地址命中DNS规则，将数据流本地分流到服务器。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-DNSRULE]] · ADD DNSRULE
- [[command/UDG/20.15.2/LST-DNSRULE]] · LST DNSRULE
- [[command/UDG/20.15.2/MOD-DNSRULE]] · MOD DNSRULE
- [[command/UDG/20.15.2/RMV-DNSRULE]] · RMV DNSRULE

## 证据

- 原始手册：`evidence/UDG/20.15.2/DNSRULE.md`
- 原始手册：`evidence/UDG/20.15.2/DNSRULE.md`
- 原始手册：`evidence/UDG/20.15.2/DNSRULE.md`
- 原始手册：`evidence/UDG/20.15.2/DNSRULE.md`
