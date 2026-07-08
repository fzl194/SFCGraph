---
id: UNC@20.15.2@ConfigObject@EXTANINFO
type: ConfigObject
name: EXTANINFO（扩展的AN信息）
nf: UNC
version: 20.15.2
object_name: EXTANINFO
object_kind: query_target
applicable_nf:
- AMF
status: active
---

# EXTANINFO（扩展的AN信息）

## 说明

![](显示扩展的AN信息（DSP EXTANINFO）_70382305.assets/notice_3.0-zh-cn_2.png)

如果当前接入到AMF的gNB数量较多时，执行该命令会占用维护终端较长时间，进而导致用户无法继续使用该维护终端。

若连续多次执行该命令可能导致OMU虚机CPU使用率突增。

**适用NF：AMF**

该命令用于显示在指定的NGAP本端实体接入的NG-RAN基站的扩展信息，例如基站支持的RAT类型等。

## 操作本对象的命令

- [DSP EXTANINFO](command/UNC/20.15.2/DSP-EXTANINFO.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示扩展的AN信息（DSP-EXTANINFO）_70382305.md`
