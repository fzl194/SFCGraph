---
id: UDG@20.15.2@ConfigObject@UPDIAMCONN
type: ConfigObject
name: UPDIAMCONN（Diameter链路）
nf: UDG
version: 20.15.2
object_name: UPDIAMCONN
object_kind: entity
applicable_nf:
- UPF
status: active
---

# UPDIAMCONN（Diameter链路）

## 说明

**适用NF：UPF**

此命令用于增加Diameter链路。

根据网络规划，需要增加UPF到对端网元的一条Diameter链路时，可以在执行完ADD UPDIAMPEERADDR和ADD UPDIAMCONNGRP等命令后，执行此命令增加Diameter链路。

## 操作本对象的命令

- [ADD UPDIAMCONN](command/UDG/20.15.2/ADD-UPDIAMCONN.md)
- [LST UPDIAMCONN](command/UDG/20.15.2/LST-UPDIAMCONN.md)
- [MOD UPDIAMCONN](command/UDG/20.15.2/MOD-UPDIAMCONN.md)
- [RMV UPDIAMCONN](command/UDG/20.15.2/RMV-UPDIAMCONN.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改Diameter链路（MOD-UPDIAMCONN）_97080153.md`
- 原始手册：`evidence/UDG/20.15.2/删除Diameter链路（RMV-UPDIAMCONN）_97314557.md`
- 原始手册：`evidence/UDG/20.15.2/增加Diameter链路（ADD-UPDIAMCONN）_45195178.md`
- 原始手册：`evidence/UDG/20.15.2/查询Diameter链路（LST-UPDIAMCONN）_45432692.md`
