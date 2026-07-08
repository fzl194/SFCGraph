---
id: UNC@20.15.2@ConfigObject@UDPCHECKSUM
type: ConfigObject
name: UDPCHECKSUM（UNC发送的UDP报文是否携带checksum）
nf: UNC
version: 20.15.2
object_name: UDPCHECKSUM
object_kind: global_setting
applicable_nf:
- PGW-C
- GGSN
- SMF
status: active
---

# UDPCHECKSUM（UNC发送的UDP报文是否携带checksum）

## 说明

**适用NF：PGW-C、GGSN、SMF**

该命令用来配置UNC发送的UDP报文是否携带checksum。

## 操作本对象的命令

- [LST UDPCHECKSUM](command/UNC/20.15.2/LST-UDPCHECKSUM.md)
- [SET UDPCHECKSUM](command/UNC/20.15.2/SET-UDPCHECKSUM.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询UNC发送的UDP报文是否携带checksum（LST-UDPCHECKSUM）_94059550.md`
- 原始手册：`evidence/UNC/20.15.2/设置UNC发送的UDP报文中是否携带checksum（SET-UDPCHECKSUM）_93899600.md`
