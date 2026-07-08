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

- [ADD MNCLEN](command/UDG/20.15.2/ADD-MNCLEN.md)
- [LST MNCLEN](command/UDG/20.15.2/LST-MNCLEN.md)
- [MOD MNCLEN](command/UDG/20.15.2/MOD-MNCLEN.md)
- [RMV MNCLEN](command/UDG/20.15.2/RMV-MNCLEN.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改MNC长度信息（MOD-MNCLEN）_44865462.md`
- 原始手册：`evidence/UDG/20.15.2/删除MNC长度信息（RMV-MNCLEN）_44865463.md`
- 原始手册：`evidence/UDG/20.15.2/显示MNC长度信息（LST-MNCLEN）_44865464.md`
- 原始手册：`evidence/UDG/20.15.2/设置MNC长度信息（ADD-MNCLEN）_44865461.md`
