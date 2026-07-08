---
id: UNC@20.15.2@ConfigObject@AMFCAP
type: ConfigObject
name: AMFCAP（操作AMF相对容量）
nf: UNC
version: 20.15.2
object_name: AMFCAP
object_kind: action
applicable_nf:
- AMF
status: active
---

# AMFCAP（操作AMF相对容量）

## 说明

![](操作AMF相对容量（OPR AMFCAP）_84726346.assets/notice_3.0-zh-cn_2.png)

该命令仅适用于存储bypass场景，通过该命令修改的AMF相对容量信息不会进行持久化。如果修改AMF相对容量时，当前系统未处于存储bypass状态，请使用MOD AMFINFO修改AMF相对容量信息。

**适用NF：AMF**

该命令用于系统进入存储bypass状态下，修改AMF相对容量信息。

## 操作本对象的命令

- [DSP AMFCAP](command/UNC/20.15.2/DSP-AMFCAP.md)
- [OPR AMFCAP](command/UNC/20.15.2/OPR-AMFCAP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/操作AMF相对容量（OPR-AMFCAP）_84726346.md`
- 原始手册：`evidence/UNC/20.15.2/显示AMF相对容量信息（DSP-AMFCAP）_30167479.md`
