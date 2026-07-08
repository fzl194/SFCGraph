---
id: UNC@20.15.2@ConfigObject@AMFMBSSESSION
type: ConfigObject
name: AMFMBSSESSION（AMF组播广播会话）
nf: UNC
version: 20.15.2
object_name: AMFMBSSESSION
object_kind: action
applicable_nf:
- AMF
status: active
---

# AMFMBSSESSION（AMF组播广播会话）

## 说明

![](去激活AMF组播广播会话（DEA AMFMBSSESSION）_87947654.assets/notice_3.0-zh-cn_2.png)

执行该命令，AMF会通知广播区域下所有基站释放广播会话，且删除本地广播上下文。

该操作可能会导致AMF和MB-SMF上广播会话状态不一致，同时AMF和基站、MB-SMF间交互消息量增大，待会话删除完成后，系统会恢复正常。

**适用NF：AMF**

该命令用于去激活AMF组播广播会话。

## 操作本对象的命令

- [[command/UNC/20.15.2/DEA-AMFMBSSESSION]] · DEA AMFMBSSESSION

## 证据

- 原始手册：`evidence/UNC/20.15.2/去激活AMF组播广播会话（DEA-AMFMBSSESSION）_87947654.md`
