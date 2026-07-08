---
id: UNC@20.15.2@ConfigObject@MNCLEN
type: ConfigObject
name: MNCLEN（MNC长度信息）
nf: UNC
version: 20.15.2
object_name: MNCLEN
object_kind: entity
applicable_nf:
- SMF
status: active
---

# MNCLEN（MNC长度信息）

## 说明

**适用NF：SMF**

该命令用于增加指定MCC号对应的MNC长度。SMF上需配置各MCC值所对应的MNC长度，用于解析移动用户的IMSI中MNC的长度，或用于解析SGSN发送的RAI（Routing Area Identity，路由区识别码）中MNC长度，以判别用户是属于本地、漫游还是拜访用户。在配置本命令后，系统依然优先从NGHPLMN中获取MNC长度信息，如果获取不到，才会从本命令的配置中获取。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-MNCLEN]] · ADD MNCLEN
- [[command/UNC/20.15.2/LST-MNCLEN]] · LST MNCLEN
- [[command/UNC/20.15.2/MOD-MNCLEN]] · MOD MNCLEN
- [[command/UNC/20.15.2/RMV-MNCLEN]] · RMV MNCLEN

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改MNC长度信息（MOD-MNCLEN）_09651551.md`
- 原始手册：`evidence/UNC/20.15.2/删除MNC长度信息（RMV-MNCLEN）_09652299.md`
- 原始手册：`evidence/UNC/20.15.2/增加MNC长度信息（ADD-MNCLEN）_09651501.md`
- 原始手册：`evidence/UNC/20.15.2/查询MNC长度信息（LST-MNCLEN）_09652662.md`
