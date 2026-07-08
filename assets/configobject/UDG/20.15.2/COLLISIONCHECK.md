---
id: UDG@20.15.2@ConfigObject@COLLISIONCHECK
type: ConfigObject
name: COLLISIONCHECK（冲突检测结果）
nf: UDG
version: 20.15.2
object_name: COLLISIONCHECK
object_kind: query_target
applicable_nf:
- PGW-U
- UPF
status: active
---

# COLLISIONCHECK（冲突检测结果）

## 说明

**适用NF：PGW-U、UPF**

该命令用于显示对配置的Filter、Rule、UserProfile进行冲突检测的结果信息。仅支持检测简单IPv4的Filter中的协议、IP地址和Port是否存在冲突。如果Filter中有IPLIST或者IPv6的Filter，不参与冲突检测，并提示存在不参与冲突检测的Filter信息。

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-COLLISIONCHECK]] · DSP COLLISIONCHECK

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询冲突检测结果（DSP-COLLISIONCHECK）_82837304.md`
