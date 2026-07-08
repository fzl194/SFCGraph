---
id: UNC@20.15.2@ConfigObject@VLRRESET
type: ConfigObject
name: VLRRESET（触发VLR向MME发送RESET消息）
nf: UNC
version: 20.15.2
object_name: VLRRESET
object_kind: action
applicable_nf:
- SMSF
status: active
---

# VLRRESET（触发VLR向MME发送RESET消息）

## 说明

![](触发VLR向MME发送RESET消息（SND VLRRESET）_11430785.assets/notice_3.0-zh-cn_2.png)

执行此命令后，指定MME在VLR下的用户关联状态置为不可信，将影响用户正在进行的短消息业务。

**适用NF：SMSF**

该命令用于触发VLR向MME发送SGsAP-RESET-INDICATION消息，其中携带“MMENAME”与“VLRNAME”，用于指示“MMENAME”对应的MME注册在“VLRNAME”对应的VLR下的用户关联状态不可信。MME收到处理后返回SGsAP-RESET-ACK消息。

## 操作本对象的命令

- [SND VLRRESET](command/UNC/20.15.2/SND-VLRRESET.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/触发VLR向MME发送RESET消息（SND-VLRRESET）_11430785.md`
