---
id: UNC@20.15.2@ConfigObject@GTPCFIXEDFC
type: ConfigObject
name: GTPCFIXEDFC（指定消息类型固定速率流控信息）
nf: UNC
version: 20.15.2
object_name: GTPCFIXEDFC
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# GTPCFIXEDFC（指定消息类型固定速率流控信息）

## 说明

![](设置指定消息类型固定速率流控信息（SET GTPCFIXEDFC）_35636465.assets/notice_3.0-zh-cn_2.png)

存在较大操作风险，执行不当会导致业务受损或中断。

**适用NF：SGW-C、PGW-C**

设置指定消息类型的固定速率门限，超过门限的消息将会被UNC丢弃，以减少其它网元对UNC的信令冲击，以及UNC对周边网元的信令冲击。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-GTPCFIXEDFC]] · LST GTPCFIXEDFC
- [[command/UNC/20.15.2/SET-GTPCFIXEDFC]] · SET GTPCFIXEDFC

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询指定消息类型固定速率流控信息（LST-GTPCFIXEDFC）_88377440.md`
- 原始手册：`evidence/UNC/20.15.2/设置指定消息类型固定速率流控信息（SET-GTPCFIXEDFC）_35636465.md`
