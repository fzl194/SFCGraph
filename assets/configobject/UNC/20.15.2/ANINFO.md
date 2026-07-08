---
id: UNC@20.15.2@ConfigObject@ANINFO
type: ConfigObject
name: ANINFO（AN信息）
nf: UNC
version: 20.15.2
object_name: ANINFO
object_kind: query_target
applicable_nf:
- AMF
status: active
---

# ANINFO（AN信息）

## 说明

![](显示AN信息（DSP ANINFO）_09653795.assets/notice_3.0-zh-cn_2.png)

如果选择“报告输出”，且当前接入到AMF的gNB数量较多时，执行该命令会占用维护终端较长时间，进而导致用户无法继续使用该维护终端。

若连续多次执行该命令可能导致OMU虚机CPU使用率突增。

**适用NF：AMF**

该命令用于显示在指定的NGAP/SFGAP本端实体接入的NG-RAN基站的信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-ANINFO]] · DSP ANINFO

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示AN信息（DSP-ANINFO）_09653795.md`
