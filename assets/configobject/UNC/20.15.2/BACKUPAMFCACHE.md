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

- [CLR BACKUPAMFCACHE](command/UNC/20.15.2/CLR-BACKUPAMFCACHE.md)
- [DSP BACKUPAMFCACHE](command/UNC/20.15.2/DSP-BACKUPAMFCACHE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示缓存的备用AMF信息（DSP-BACKUPAMFCACHE）_83021417.md`
- 原始手册：`evidence/UNC/20.15.2/清除备用AMF缓存信息（CLR-BACKUPAMFCACHE）_82661413.md`
