---
id: UDG@20.15.2@ConfigObject@DDOS
type: ConfigObject
name: DDOS（DDoS防攻击流控阈值）
nf: UDG
version: 20.15.2
object_name: DDOS
object_kind: global_setting
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# DDOS（DDoS防攻击流控阈值）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用于设置DDoS攻击防护使用的流控阈值。DDoS攻击防护是通过对用户上行TCP SYN报文进行流控来实施的。

## 操作本对象的命令

- [LST DDOS](command/UDG/20.15.2/LST-DDOS.md)
- [SET DDOS](command/UDG/20.15.2/SET-DDOS.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询DDoS防攻击流控阈值（LST-DDOS）_82837755.md`
- 原始手册：`evidence/UDG/20.15.2/设置DDoS防攻击流控阈值（SET-DDOS）_82837754.md`
