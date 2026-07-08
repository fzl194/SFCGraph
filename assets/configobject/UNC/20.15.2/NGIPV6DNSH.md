---
id: UNC@20.15.2@ConfigObject@NGIPV6DNSH
type: ConfigObject
name: NGIPV6DNSH（IPv6 DNS Hostfile记录）
nf: UNC
version: 20.15.2
object_name: NGIPV6DNSH
object_kind: entity
applicable_nf:
- AMF
status: active
---

# NGIPV6DNSH（IPv6 DNS Hostfile记录）

## 说明

**适用NF：AMF**

该命令用于配置网元接口所对应的IPv6地址信息，该信息用于网元选择时DNS查询功能。

如果配置了多个IP地址，域名解析结果中将会根据“PRIORITY（优先级）”和“WEIGHT（权重）”进行先后次序排列：

- 优先级别高的排前面。
- 同一优先级别的再按照权重来选择，权重越大，则排在前面的概率越高。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NGIPV6DNSH]] · ADD NGIPV6DNSH
- [[command/UNC/20.15.2/LST-NGIPV6DNSH]] · LST NGIPV6DNSH
- [[command/UNC/20.15.2/MOD-NGIPV6DNSH]] · MOD NGIPV6DNSH
- [[command/UNC/20.15.2/RMV-NGIPV6DNSH]] · RMV NGIPV6DNSH

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IPv6-DNS-Hostfile记录（MOD-NGIPV6DNSH）_09652953.md`
- 原始手册：`evidence/UNC/20.15.2/删除IPv6-DNS-Hostfile记录（RMV-NGIPV6DNSH）_09653120.md`
- 原始手册：`evidence/UNC/20.15.2/增加IPv6-DNS-Hostfile记录（ADD-NGIPV6DNSH）_09652334.md`
- 原始手册：`evidence/UNC/20.15.2/查询IPv6-DNS-Hostfile记录（LST-NGIPV6DNSH）_09653303.md`
