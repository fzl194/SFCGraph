---
id: UDG@20.15.2@ConfigObject@APNTRFCDFDSWITCH
type: ConfigObject
name: APNTRFCDFDSWITCH（APN大流量攻击防护配置）
nf: UDG
version: 20.15.2
object_name: APNTRFCDFDSWITCH
object_kind: global_setting
applicable_nf:
- UPF
status: active
---

# APNTRFCDFDSWITCH（APN大流量攻击防护配置）

## 说明

**适用NF：UPF**

![](设置大流量攻击防护APN开关（SET APNTRFCDFDSWITCH）_86530451.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，请确认TrfcDfdPara配置合理，否则可能导致用户丢包或去活。

该命令用于配置指定APN下大流量攻击检测开关是否开启。某一周期内某用户下行报文数与上行报文数之比大于TRFCDFDPARA命令设定的阈值，则认为该用户存在下行大流量攻击行为。对这种大流量攻击行为的检测即为大流量攻击检测。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-APNTRFCDFDSWITCH]] · LST APNTRFCDFDSWITCH
- [[command/UDG/20.15.2/SET-APNTRFCDFDSWITCH]] · SET APNTRFCDFDSWITCH

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询APN大流量攻击防护配置（LST-APNTRFCDFDSWITCH）_86530452.md`
- 原始手册：`evidence/UDG/20.15.2/设置大流量攻击防护APN开关（SET-APNTRFCDFDSWITCH）_86530451.md`
