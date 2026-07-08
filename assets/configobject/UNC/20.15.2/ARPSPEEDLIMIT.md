---
id: UNC@20.15.2@ConfigObject@ARPSPEEDLIMIT
type: ConfigObject
name: ARPSPEEDLIMIT（速率限制）
nf: UNC
version: 20.15.2
object_name: ARPSPEEDLIMIT
object_kind: global_setting
status: active
---

# ARPSPEEDLIMIT（速率限制）

## 说明

该命令用于设置ARP报文或者ARP Miss消息的抑制速率。非法用户使用大量的ARP报文对目标设备攻击时，将导致设备将大量资源浪费在处理ARP报文上，影响设备对其他业务的处理；或者非法用户利用工具扫描本网段内的主机或者跨网段进行扫描时，会导致设备因目的IP地址对应的MAC地址不存在，而产生大量的ARP Miss消息，导致设备大量的资源都浪费在处理ARP Miss消息上，影响设备对其他业务的处理。为了解决该问题，用户可以配置基于IP地址对ARP报文或者ARP-Miss消息进行限速，在一定时间内处理指定数目以内的ARP报文或ARP-Miss消息，保证业务的正常运行。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-ARPSPEEDLIMIT]] · LST ARPSPEEDLIMIT
- [[command/UNC/20.15.2/SET-ARPSPEEDLIMIT]] · SET ARPSPEEDLIMIT

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询速率限制（LST-ARPSPEEDLIMIT）_00441141.md`
- 原始手册：`evidence/UNC/20.15.2/配置速率限制（SET-ARPSPEEDLIMIT）_00840941.md`
