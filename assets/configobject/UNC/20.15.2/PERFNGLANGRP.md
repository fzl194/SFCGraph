---
id: UNC@20.15.2@ConfigObject@PERFNGLANGRP
type: ConfigObject
name: PERFNGLANGRP（用于性能统计的5G LAN群组）
nf: UNC
version: 20.15.2
object_name: PERFNGLANGRP
object_kind: entity
applicable_nf:
- SMF
status: active
---

# PERFNGLANGRP（用于性能统计的5G LAN群组）

## 说明

**适用NF：SMF**

该命令用于配置性能统计的5G LAN群组。当激活一个5G LAN组会话时，SMF会判断该组会话的5G LAN组ID是否与该命令中的5G LAN组ID一致。如果一致，则会对该5G LAN群组进行性能统计。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PERFNGLANGRP]] · ADD PERFNGLANGRP
- [[command/UNC/20.15.2/LST-PERFNGLANGRP]] · LST PERFNGLANGRP
- [[command/UNC/20.15.2/RMV-PERFNGLANGRP]] · RMV PERFNGLANGRP

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除用于性能统计的5G-LAN群组（RMV-PERFNGLANGRP）_79575224.md`
- 原始手册：`evidence/UNC/20.15.2/增加用于性能统计的5G-LAN群组（ADD-PERFNGLANGRP）_25214873.md`
- 原始手册：`evidence/UNC/20.15.2/查询用于性能统计的5G-LAN群组（LST-PERFNGLANGRP）_79256716.md`
