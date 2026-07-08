---
id: UNC@20.15.2@ConfigObject@TWTIMER
type: ConfigObject
name: TWTIMER（TW定时器）
nf: UNC
version: 20.15.2
object_name: TWTIMER
object_kind: global_setting
applicable_nf:
- PGW-C
- SMF
status: active
---

# TWTIMER（TW定时器）

## 说明

**适用NF：PGW-C、SMF**

该命令用于配置Diameter TW定时器。当该定时器超时后，UNC会向OCS等Diameter对端发送DWR消息。并能控制DWR消息响应超时次数达到上限后，是否复位UNC和对端之间的链接。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-TWTIMER]] · LST TWTIMER
- [[command/UNC/20.15.2/SET-TWTIMER]] · SET TWTIMER

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询TW定时器（LST-TWTIMER）_09897239.md`
- 原始手册：`evidence/UNC/20.15.2/设置TW定时器（SET-TWTIMER）_09897238.md`
