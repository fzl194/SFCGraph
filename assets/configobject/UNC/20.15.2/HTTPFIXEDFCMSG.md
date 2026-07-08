---
id: UNC@20.15.2@ConfigObject@HTTPFIXEDFCMSG
type: ConfigObject
name: HTTPFIXEDFCMSG（HTTP指定消息类型固定速率流控信息）
nf: UNC
version: 20.15.2
object_name: HTTPFIXEDFCMSG
object_kind: global_setting
status: active
---

# HTTPFIXEDFCMSG（HTTP指定消息类型固定速率流控信息）

## 说明

![](设置HTTP指定消息类型固定速率流控信息（SET HTTPFIXEDFCMSG）_84132110.assets/notice_3.0-zh-cn_2.png)

流控阈值设置过低可能会导致流程失败，设置过高可能导致系统不能对消息进行合理流控。

该命令用于设置指定消息类型的固定速率门限，减少其它网元对本网元的冲击，以及本网元对其它网元的冲击。

## 操作本对象的命令

- [LST HTTPFIXEDFCMSG](command/UNC/20.15.2/LST-HTTPFIXEDFCMSG.md)
- [SET HTTPFIXEDFCMSG](command/UNC/20.15.2/SET-HTTPFIXEDFCMSG.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询HTTP指定消息类型固定速率流控信息（LST-HTTPFIXEDFCMSG）_83972186.md`
- 原始手册：`evidence/UNC/20.15.2/设置HTTP指定消息类型固定速率流控信息（SET-HTTPFIXEDFCMSG）_84132110.md`
