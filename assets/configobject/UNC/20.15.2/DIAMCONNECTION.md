---
id: UNC@20.15.2@ConfigObject@DIAMCONNECTION
type: ConfigObject
name: DIAMCONNECTION（Diameter链路）
nf: UNC
version: 20.15.2
object_name: DIAMCONNECTION
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# DIAMCONNECTION（Diameter链路）

## 说明

**适用NF：PGW-C、SMF**

此命令用于增加Diameter链路。

根据网络规划，需要增加UNC到对端网元的一条Diameter链路时，可以在执行完ADD DIAMPEERADDR和ADD DIAMCONNGRP等命令后，执行此命令增加Diameter链路。

## 操作本对象的命令

- [ADD DIAMCONNECTION](command/UNC/20.15.2/ADD-DIAMCONNECTION.md)
- [LST DIAMCONNECTION](command/UNC/20.15.2/LST-DIAMCONNECTION.md)
- [MOD DIAMCONNECTION](command/UNC/20.15.2/MOD-DIAMCONNECTION.md)
- [RMV DIAMCONNECTION](command/UNC/20.15.2/RMV-DIAMCONNECTION.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Diameter链路（MOD-DIAMCONNECTION）_09897267.md`
- 原始手册：`evidence/UNC/20.15.2/删除Diameter链路（RMV-DIAMCONNECTION）_09897268.md`
- 原始手册：`evidence/UNC/20.15.2/增加Diameter链路（ADD-DIAMCONNECTION）_09897266.md`
- 原始手册：`evidence/UNC/20.15.2/查询Diameter链路（LST-DIAMCONNECTION）_09897269.md`
