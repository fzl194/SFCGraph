---
id: UNC@20.15.2@ConfigObject@DEACTIVERATE
type: ConfigObject
name: DEACTIVERATE（去激活用户承载的速率）
nf: UNC
version: 20.15.2
object_name: DEACTIVERATE
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
status: active
---

# DEACTIVERATE（去激活用户承载的速率）

## 说明

![](设置去激活用户承载的速率（SET DEACTIVERATE）_09652156.assets/notice_3.0-zh-cn_2.png)

如果配置速率过低，则用户去活时间较长，如果配置速率过高，会导致UNC负荷过高，CPU占用率升高，影响用户业务恢复。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于配置UNC主动触发去激活用户的速率，包括但不限于周边NF复位、链路故障、OM或会话空闲定时器超时等场景。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-DEACTIVERATE]] · LST DEACTIVERATE
- [[command/UNC/20.15.2/SET-DEACTIVERATE]] · SET DEACTIVERATE

## 证据

- 原始手册：`evidence/UNC/20.15.2/DEACTIVERATE.md`
- 原始手册：`evidence/UNC/20.15.2/DEACTIVERATE.md`
