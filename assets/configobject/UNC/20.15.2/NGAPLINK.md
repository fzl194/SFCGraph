---
id: UNC@20.15.2@ConfigObject@NGAPLINK
type: ConfigObject
name: NGAPLINK（NGAP链路信息）
nf: UNC
version: 20.15.2
object_name: NGAPLINK
object_kind: query_target
applicable_nf:
- AMF
status: active
---

# NGAPLINK（NGAP链路信息）

## 说明

![](显示NGAP链路信息（DSP NGAPLINK）_09651404.assets/notice_3.0-zh-cn_2.png)

如果选择“报告输出”，且当前接入到AMF的gNB数量较多时，执行该命令会占用维护终端较长时间，进而导致用户无法继续使用该维护终端。若连续多次执行该命令可能导致OMU虚机CPU使用率突增。

**适用NF：AMF**

该命令用于查询NGAP链路信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-NGAPLINK]] · DSP NGAPLINK

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示NGAP链路信息（DSP-NGAPLINK）_09651404.md`
