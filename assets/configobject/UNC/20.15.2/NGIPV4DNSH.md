---
id: UNC@20.15.2@ConfigObject@NGIPV4DNSH
type: ConfigObject
name: NGIPV4DNSH（IPv4 DNS Hostfile记录）
nf: UNC
version: 20.15.2
object_name: NGIPV4DNSH
object_kind: entity
applicable_nf:
- AMF
status: active
---

# NGIPV4DNSH（IPv4 DNS Hostfile记录）

## 说明

**适用NF：AMF**

该命令用于配置网元接口所对应的IPv4地址信息，该信息用于网元选择时DNS查询功能。

如果配置了多个IP地址，域名解析结果中将会根据“PRIORITY（优先级）”和“WEIGHT（权重）”进行先后次序排列：

- 优先级别高的排前面。
- 同一优先级别的再按照权重来选择，权重越大，则排在前面的概率越高。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NGIPV4DNSH]] · ADD NGIPV4DNSH
- [[command/UNC/20.15.2/LST-NGIPV4DNSH]] · LST NGIPV4DNSH
- [[command/UNC/20.15.2/MOD-NGIPV4DNSH]] · MOD NGIPV4DNSH
- [[command/UNC/20.15.2/RMV-NGIPV4DNSH]] · RMV NGIPV4DNSH

## 证据

- 原始手册：`evidence/UNC/20.15.2/NGIPV4DNSH.md`
- 原始手册：`evidence/UNC/20.15.2/NGIPV4DNSH.md`
- 原始手册：`evidence/UNC/20.15.2/NGIPV4DNSH.md`
- 原始手册：`evidence/UNC/20.15.2/NGIPV4DNSH.md`
