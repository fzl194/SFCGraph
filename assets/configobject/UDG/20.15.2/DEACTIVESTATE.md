---
id: UDG@20.15.2@ConfigObject@DEACTIVESTATE
type: ConfigObject
name: DEACTIVESTATE（去活操作状态）
nf: UDG
version: 20.15.2
object_name: DEACTIVESTATE
object_kind: query_target
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# DEACTIVESTATE（去活操作状态）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询手动批量去激活命令的执行情况。指定IMSI、MSISDN、或IMEI的用户去激活无法被查询。

执行该命令时，Remain Time (hour)实际时间受CPU占用率影响。CPU占用率越高，实际Remain Time可能会比预期的计算时间长。

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-DEACTIVESTATE]] · DSP DEACTIVESTATE

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示去活操作状态（DSP-DEACTIVESTATE）_97358674.md`
