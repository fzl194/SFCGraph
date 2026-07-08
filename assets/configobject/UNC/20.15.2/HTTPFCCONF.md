---
id: UNC@20.15.2@ConfigObject@HTTPFCCONF
type: ConfigObject
name: HTTPFCCONF（HTTP流控属性）
nf: UNC
version: 20.15.2
object_name: HTTPFCCONF
object_kind: global_setting
status: active
---

# HTTPFCCONF（HTTP流控属性）

## 说明

![](设置HTTP流控属性（SET HTTPFCCONF）_00360897.assets/notice_3.0-zh-cn_2.png)

本命令为高危命令。关闭CPU跟踪流控功能，可能触发业务自保流控，导致业务受损；关闭跟踪流控功能，可能导致跟踪功能占用CPU比例过高，从而触发CPU跟踪流控导致跟踪功能失效。

该命令用于设置HTTP流控属性。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-HTTPFCCONF]] · LST HTTPFCCONF
- [[command/UNC/20.15.2/SET-HTTPFCCONF]] · SET HTTPFCCONF

## 证据

- 原始手册：`evidence/UNC/20.15.2/HTTPFCCONF.md`
- 原始手册：`evidence/UNC/20.15.2/HTTPFCCONF.md`
