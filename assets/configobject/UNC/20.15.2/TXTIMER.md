---
id: UNC@20.15.2@ConfigObject@TXTIMER
type: ConfigObject
name: TXTIMER（DCC模板Tx定时器）
nf: UNC
version: 20.15.2
object_name: TXTIMER
object_kind: global_setting
applicable_nf:
- PGW-C
- SMF
status: active
---

# TXTIMER（DCC模板Tx定时器）

## 说明

**适用NF：PGW-C、SMF**

![](设置DCC模板Tx定时器（SET TXTIMER）_09896927.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，执行命令配置超时时长不合理可能导致在超时场景下，激活响应的总时长过长，这可能会导致用户激活失败。在前期规划时，建议1：产品配置的等待右侧网元的最大时长小于产品ADD GTPCT3N3命令配置的T3N3时长及左侧（MME/SGSN等）的T3N3时长。建议2：产品配置的等待右侧网元的最大时长小于产品SET SMCOMMTIMER命令配置的TCHARGING（等待计费网关响应定时器）的时长。

该命令用于设置DCC在线计费模板Tx定时器。

## 操作本对象的命令

- [SET TXTIMER](command/UNC/20.15.2/SET-TXTIMER.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置DCC模板Tx定时器（SET-TXTIMER）_09896927.md`
