---
id: UNC@20.15.2@ConfigObject@ICMPOPTSECURITY
type: ConfigObject
name: ICMPOPTSECURITY（ICMP选项安全配置）
nf: UNC
version: 20.15.2
object_name: ICMPOPTSECURITY
object_kind: entity
status: active
---

# ICMPOPTSECURITY（ICMP选项安全配置）

## 说明

该命令用于增加ICMP选项安全配置，丢弃TTL=1的ICMP报文。

设备收到IP数据报文后，如果报文的目的地不是本地且报文的TTL字段是1，则会发送TTL超时ICMP差错报文。攻击者通常会利用这一点发送TTL=1的报文攻击设备，设备接收到大量需要发送ICMP差错报文的恶意攻击报文，会因为处理大量该类报文而导致性能降低。此时可以通过icmp ttl-exceeded drop命令丢弃TTL=1的ICMP报文，减轻设备处理ICMP报文的压力，提高网络的性能和增强网络的安全。

## 操作本对象的命令

- [ADD ICMPOPTSECURITY](command/UNC/20.15.2/ADD-ICMPOPTSECURITY.md)
- [LST ICMPOPTSECURITY](command/UNC/20.15.2/LST-ICMPOPTSECURITY.md)
- [RMV ICMPOPTSECURITY](command/UNC/20.15.2/RMV-ICMPOPTSECURITY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除ICMP选项安全配置（RMV-ICMPOPTSECURITY）_00865857.md`
- 原始手册：`evidence/UNC/20.15.2/增加ICMP选项安全配置（ADD-ICMPOPTSECURITY）_49801634.md`
- 原始手册：`evidence/UNC/20.15.2/查询ICMP选项安全配置（LST-ICMPOPTSECURITY）_00440761.md`
