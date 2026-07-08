---
id: UNC@20.15.2@ConfigObject@HTTPGLBFIXEDBWFC
type: ConfigObject
name: HTTPGLBFIXEDBWFC（HTTP全局固定带宽流控）
nf: UNC
version: 20.15.2
object_name: HTTPGLBFIXEDBWFC
object_kind: global_setting
status: active
---

# HTTPGLBFIXEDBWFC（HTTP全局固定带宽流控）

## 说明

![](设置HTTP全局固定带宽流控（SET HTTPGLBFIXEDBWFC）_56474481.assets/notice_3.0-zh-cn_2.png)

门限值由本端和对端网元的消息处理能力决定。设置过低会导致消息被丢弃，设置过高起不到保护本端和对端网元不过载的作用。

该命令用于设置HTTP全局固定带宽流控门限等信息，设置后所有链路都使用相同的参数控制。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-HTTPGLBFIXEDBWFC]] · LST HTTPGLBFIXEDBWFC
- [[command/UNC/20.15.2/SET-HTTPGLBFIXEDBWFC]] · SET HTTPGLBFIXEDBWFC

## 证据

- 原始手册：`evidence/UNC/20.15.2/HTTPGLBFIXEDBWFC.md`
- 原始手册：`evidence/UNC/20.15.2/HTTPGLBFIXEDBWFC.md`
