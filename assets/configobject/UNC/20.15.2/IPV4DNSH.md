---
id: UNC@20.15.2@ConfigObject@IPV4DNSH
type: ConfigObject
name: IPV4DNSH（IPV4 DNS Hostfile记录）
nf: UNC
version: 20.15.2
object_name: IPV4DNSH
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# IPV4DNSH（IPV4 DNS Hostfile记录）

## 说明

**适用网元：SGSN、MME**

该命令用于配置网元接口所对应的IPv4地址信息，该信息用于网元选择时DNS查询功能。

进行域名解析可以使用两种手段：使用DNS服务器或使用本地主机信息表（Hostfile），通常主要使用DNS服务器进行域名解析，Hostfile作为辅助手段。本命令用于配置本地主机信息表Hostfile。

如果配置了多个IP地址，域名解析结果中将会根据 “PRIORITY（优先级）” 和 “WEIGHT（权重）” 进行先后次序排列：

1. 优先级别高的排前面。
2. 同一优先级别的再按照权重来选择，权重越大，则排在前面的概率越高。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-IPV4DNSH]] · ADD IPV4DNSH
- [[command/UNC/20.15.2/LST-IPV4DNSH]] · LST IPV4DNSH
- [[command/UNC/20.15.2/MOD-IPV4DNSH]] · MOD IPV4DNSH
- [[command/UNC/20.15.2/RMV-IPV4DNSH]] · RMV IPV4DNSH

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IPV4-DNS-Hostfile记录(MOD-IPV4DNSH)_26305694.md`
- 原始手册：`evidence/UNC/20.15.2/删除IPV4-DNS-Hostfile记录(RMV-IPV4DNSH)_72225563.md`
- 原始手册：`evidence/UNC/20.15.2/增加IPV4-DNS-Hostfile记录(ADD-IPV4DNSH)_26145884.md`
- 原始手册：`evidence/UNC/20.15.2/查询IPV4-DNS-Hostfile记录(LST-IPV4DNSH)_72345485.md`
