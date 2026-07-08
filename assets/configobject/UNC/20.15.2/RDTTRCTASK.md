---
id: UNC@20.15.2@ConfigObject@RDTTRCTASK
type: ConfigObject
name: RDTTRCTASK（重定向跟踪任务）
nf: UNC
version: 20.15.2
object_name: RDTTRCTASK
object_kind: query_target
applicable_nf:
- SGSN
- MME
status: active
---

# RDTTRCTASK（重定向跟踪任务）

## 说明

**适用网元：SGSN、MME**

该命令用于查询指定VNFC下已经建立的重定向跟踪任务信息。其中重定向跟踪任务为用户在跟踪建立时选择了重定向标记并指定重定向索引的跟踪任务，系统中存在该类任务会主动将跟踪上报消息以Pcap格式上报到第三方服务器。

## 操作本对象的命令

- [DSP RDTTRCTASK](command/UNC/20.15.2/DSP-RDTTRCTASK.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示重定向跟踪任务(DSP-RDTTRCTASK)_72345011.md`
