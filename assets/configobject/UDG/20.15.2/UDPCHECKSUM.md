---
id: UDG@20.15.2@ConfigObject@UDPCHECKSUM
type: ConfigObject
name: UDPCHECKSUM（UDP报文是否携带checksum）
nf: UDG
version: 20.15.2
object_name: UDPCHECKSUM
object_kind: global_setting
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# UDPCHECKSUM（UDP报文是否携带checksum）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

![](配置UDP报文中是否携带checksum（SET UDPCHECKSUM）_82837687.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，执行该命令时，开启UDP checksum功能前，需要确认对端支持程度，否则影响整机信令转发

该命令用来配置系统发送的UDP报文是否携带checksum。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-UDPCHECKSUM]] · LST UDPCHECKSUM
- [[command/UDG/20.15.2/SET-UDPCHECKSUM]] · SET UDPCHECKSUM

## 证据

- 原始手册：`evidence/UDG/20.15.2/UDPCHECKSUM.md`
- 原始手册：`evidence/UDG/20.15.2/UDPCHECKSUM.md`
