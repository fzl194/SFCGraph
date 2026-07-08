---
id: UDG@20.15.2@ConfigObject@APNDROPFINALPKT
type: ConfigObject
name: APNDROPFINALPKT（指定APN配额耗尽末包动作）
nf: UDG
version: 20.15.2
object_name: APNDROPFINALPKT
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# APNDROPFINALPKT（指定APN配额耗尽末包动作）

## 说明

**适用NF：PGW-U、UPF**

本命令用于基于指定APN配置，当配额耗尽时，UPF是否阻塞最后一个超出配额范围的数据报文。

## 操作本对象的命令

- [LST APNDROPFINALPKT](command/UDG/20.15.2/LST-APNDROPFINALPKT.md)
- [SET APNDROPFINALPKT](command/UDG/20.15.2/SET-APNDROPFINALPKT.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示指定APN配额耗尽末包动作（LST-APNDROPFINALPKT）_93973679.md`
- 原始手册：`evidence/UDG/20.15.2/配置指定APN配额耗尽末包动作（SET-APNDROPFINALPKT）_94212265.md`
