---
id: UNC@20.15.2@ConfigObject@UPCCTX
type: ConfigObject
name: UPCCTX（用户面控制上下文）
nf: UNC
version: 20.15.2
object_name: UPCCTX
object_kind: action
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
status: active
---

# UPCCTX（用户面控制上下文）

## 说明

![](去激活用户面控制上下文（DEA UPCCTX）_72615136.assets/notice_3.0-zh-cn_2.png)

该命令会去激活指定的签约用户。因为去活用户需要通知周边网元清除相关资源，所以当去活速率过高时，网络上会产生大量消息需要CPU进行处理，导致CPU使用率升高。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于去激活用户面控制上下文。

## 操作本对象的命令

- [[command/UNC/20.15.2/DEA-UPCCTX]] · DEA UPCCTX

## 证据

- 原始手册：`evidence/UNC/20.15.2/去激活用户面控制上下文（DEA-UPCCTX）_72615136.md`
