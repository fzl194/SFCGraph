---
id: UDG@20.15.2@ConfigObject@SECICMPREPLY
type: ConfigObject
name: SECICMPREPLY（ICMP快回）
nf: UDG
version: 20.15.2
object_name: SECICMPREPLY
object_kind: global_setting
status: active
---

# SECICMPREPLY（ICMP快回）

## 说明

该命令用于设置ICMP快回使能配置。

当业务繁忙时，网络流量增大，Device的负载增大，这时会导致Device发送Ping报文应答延时较大。可以使用该命令使能设备Ping快回功能，达到避免Ping报文延时的目的。

## 操作本对象的命令

- [LST SECICMPREPLY](command/UDG/20.15.2/LST-SECICMPREPLY.md)
- [SET SECICMPREPLY](command/UDG/20.15.2/SET-SECICMPREPLY.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ICMP快回（LST-SECICMPREPLY）_49802478.md`
- 原始手册：`evidence/UDG/20.15.2/设置ICMP快回配置（SET-SECICMPREPLY）_00601101.md`
