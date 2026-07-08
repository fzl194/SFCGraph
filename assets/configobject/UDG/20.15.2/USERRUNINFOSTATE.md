---
id: UDG@20.15.2@ConfigObject@USERRUNINFOSTATE
type: ConfigObject
name: USERRUNINFOSTATE（指定用户的运行信息）
nf: UDG
version: 20.15.2
object_name: USERRUNINFOSTATE
object_kind: action
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# USERRUNINFOSTATE（指定用户的运行信息）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用于显示当前进行用户收集运行信息的所有用户，或者查询指定用户的运行信息。

用于查询指定用户的运行信息，输出用户使用静态规则时各种rule信息的匹配次数统计、该rule下的流量统计。或者使用动态规则时的flow信息，各种rule信息的匹配次数统计、该rule下的流量统计，用户业务car/shaping的信息，用户当前使用的五元组信息，用户访问业务的协议信息。或者输出动态和预定义ADC规则匹配次数统计。Rule group information统计项只对PCC用户生效。User profile and Common-Policy统计项只针对非PCC用户生效。

## 操作本对象的命令

- [CLR USERRUNINFOSTATE](command/UDG/20.15.2/CLR-USERRUNINFOSTATE.md)
- [DSP USERRUNINFOSTATE](command/UDG/20.15.2/DSP-USERRUNINFOSTATE.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询指定用户的运行信息（DSP-USERRUNINFOSTATE）_86526349.md`
- 原始手册：`evidence/UDG/20.15.2/清除指定用户全部的运行信息记录（CLR-USERRUNINFOSTATE）_82837076.md`
