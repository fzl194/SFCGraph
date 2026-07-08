---
id: UDG@20.15.2@ConfigObject@MNCLEN
type: ConfigObject
name: MNCLEN（MNC长度信息）
nf: UDG
version: 20.15.2
object_name: MNCLEN
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# MNCLEN（MNC长度信息）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用于增加指定MCC号对应的MNC长度。UPF上需配置各MCC值所对应的MNC长度，用于解析移动用户的IMSI中MNC的长度，或用于解析SGSN发送的RAI（Routing Area Identity，路由区识别码）中MNC长度，以判别用户是属于本地、漫游还是拜访用户。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-MNCLEN]] · ADD MNCLEN
- [[command/UDG/20.15.2/LST-MNCLEN]] · LST MNCLEN
- [[command/UDG/20.15.2/MOD-MNCLEN]] · MOD MNCLEN
- [[command/UDG/20.15.2/RMV-MNCLEN]] · RMV MNCLEN

## 证据

- 原始手册：`evidence/UDG/20.15.2/MNCLEN.md`
- 原始手册：`evidence/UDG/20.15.2/MNCLEN.md`
- 原始手册：`evidence/UDG/20.15.2/MNCLEN.md`
- 原始手册：`evidence/UDG/20.15.2/MNCLEN.md`
