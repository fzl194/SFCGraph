---
id: UNC@20.15.2@ConfigObject@IFICMPSECURITY
type: ConfigObject
name: IFICMPSECURITY（接口下ICMP安全配置）
nf: UNC
version: 20.15.2
object_name: IFICMPSECURITY
object_kind: entity
status: active
---

# IFICMPSECURITY（接口下ICMP安全配置）

## 说明

该命令用于新增接口下ICMP安全配置。接口名称可以通过LST INTERFACE命令获取。

在网络正常的情况下，可以正确收发ICMP报文。但是，在网络流量较大时，如果频繁出现主机不可达、端口不可达的现象，则路由设备会收发大量的ICMP报文，这样会增大网络的流量负担，明显降低路由设备的性能。同时，网络攻击者经常利用ICMP差错报文非法刺探网络内部结构。

因此为了提高网络的性能和增强网络的安全，可以使用该命令去使能某个接口收发ICMP报文的功能，防止针对该接口的这些ICMP报文的安全攻击。

如果用户不需要某个接口发送ICMP时间戳报文，在确认无其他业务使用该报文的前提下，可通过创建ICMP安全配置去使能某个接口发送ICMP时间戳报文的功能。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-IFICMPSECURITY]] · ADD IFICMPSECURITY
- [[command/UNC/20.15.2/LST-IFICMPSECURITY]] · LST IFICMPSECURITY
- [[command/UNC/20.15.2/MOD-IFICMPSECURITY]] · MOD IFICMPSECURITY
- [[command/UNC/20.15.2/RMV-IFICMPSECURITY]] · RMV IFICMPSECURITY

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改接口下ICMP安全配置（MOD-IFICMPSECURITY）_50280786.md`
- 原始手册：`evidence/UNC/20.15.2/删除接口下ICMP安全配置（RMV-IFICMPSECURITY）_49802334.md`
- 原始手册：`evidence/UNC/20.15.2/新增接口下ICMP安全配置（ADD-IFICMPSECURITY）_00441149.md`
- 原始手册：`evidence/UNC/20.15.2/查询接口下ICMP安全配置（LST-IFICMPSECURITY）_00865849.md`
