---
id: UNC@20.15.2@ConfigObject@NGPAGING
type: ConfigObject
name: NGPAGING（5G寻呼表）
nf: UNC
version: 20.15.2
object_name: NGPAGING
object_kind: query_target
applicable_nf:
- AMF
status: active
---

# NGPAGING（5G寻呼表）

## 说明

![](显示5G寻呼表（DSP NGPAGING）_09651526.assets/notice_3.0-zh-cn_2.png)

如果选择“全量查询”，且当前接入到AMF的gNB数量较多时，执行该命令会占用维护终端较长时间，进而导致用户无法继续使用该维护终端。

若连续多次执行该命令可能导致OMU虚机CPU使用率突增。

**适用NF：AMF**

该命令用于查询UNC系统的NG寻呼表信息。NG寻呼表记录了接入到UNC的接入网设备及其支持的TAI信息。

## 操作本对象的命令

- [DSP NGPAGING](command/UNC/20.15.2/DSP-NGPAGING.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示5G寻呼表（DSP-NGPAGING）_09651526.md`
