---
id: UNC@20.15.2@ConfigObject@ICMPSECURITY
type: ConfigObject
name: ICMPSECURITY（ICMP安全配置）
nf: UNC
version: 20.15.2
object_name: ICMPSECURITY
object_kind: entity
status: active
---

# ICMPSECURITY（ICMP安全配置）

## 说明

该命令用于新增ICMP安全配置。

在网络正常的情况下，可以正确收发ICMP报文。但是，在网络流量较大时，如果频繁出现主机不可达、端口不可达的现象，则路由设备会收发大量的ICMP报文，这样会增大网络的流量负担，明显降低路由设备的性能。同时，网络攻击者经常利用ICMP差错报文非法刺探网络内部结构。

因此为了提高网络的性能和增强网络的安全，可以使用该命令去使能系统收发ICMP报文的功能，防止针对这些ICMP报文的安全攻击。

如果用户不需要系统发送ICMP时间戳报文，在确认无其他业务使用该报文的前提下，可通过创建全局ICMP安全配置去使能系统发送ICMP时间戳报文的功能。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-ICMPSECURITY]] · ADD ICMPSECURITY
- [[command/UNC/20.15.2/LST-ICMPSECURITY]] · LST ICMPSECURITY
- [[command/UNC/20.15.2/MOD-ICMPSECURITY]] · MOD ICMPSECURITY
- [[command/UNC/20.15.2/RMV-ICMPSECURITY]] · RMV ICMPSECURITY

## 证据

- 原始手册：`evidence/UNC/20.15.2/ICMPSECURITY.md`
- 原始手册：`evidence/UNC/20.15.2/ICMPSECURITY.md`
- 原始手册：`evidence/UNC/20.15.2/ICMPSECURITY.md`
- 原始手册：`evidence/UNC/20.15.2/ICMPSECURITY.md`
