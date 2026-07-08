---
id: UNC@20.15.2@ConfigObject@BACKUPAMFCACHE
type: ConfigObject
name: BACKUPAMFCACHE（缓存的备用AMF信息）
nf: UNC
version: 20.15.2
object_name: BACKUPAMFCACHE
object_kind: action
applicable_nf:
- AMF
status: active
---

# BACKUPAMFCACHE（缓存的备用AMF信息）

## 说明

**适用NF：AMF**

该命令用于查询AMF缓存的备用AMF信息。

当AMF热备功能开启且AMF以3gpp-Sbi-Binding头域的形式向周边NF携带备用AMF信息时（通过SET AMFRESTOFUNC命令开启），AMF才会服务发现并缓存备用AMF的信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/CLR-BACKUPAMFCACHE]] · CLR BACKUPAMFCACHE
- [[command/UNC/20.15.2/DSP-BACKUPAMFCACHE]] · DSP BACKUPAMFCACHE

## 证据

- 原始手册：`evidence/UNC/20.15.2/BACKUPAMFCACHE.md`
- 原始手册：`evidence/UNC/20.15.2/BACKUPAMFCACHE.md`
