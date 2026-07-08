---
id: UDG@20.15.2@ConfigObject@TRFCDFDSWITCH
type: ConfigObject
name: TRFCDFDSWITCH（大流量攻击防护配置）
nf: UDG
version: 20.15.2
object_name: TRFCDFDSWITCH
object_kind: global_setting
applicable_nf:
- UPF
status: active
---

# TRFCDFDSWITCH（大流量攻击防护配置）

## 说明

**适用NF：UPF**

![](设置大流量攻击防护功能（SET TRFCDFDSWITCH）_82837760.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，请确认Set TrfcDfdPara配置合理，否则可能导致用户丢包或去活。

该命令用来配置整机粒度是否开启大流量攻击检测功能。某一周期内某用户流量超过大流量攻击防护参数（SET TRFCDFDPARA）设定的阈值，则认为该用户存在大流量攻击行为。对这种大流量攻击行为的检测即为大流量攻击检测。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-TRFCDFDSWITCH]] · LST TRFCDFDSWITCH
- [[command/UDG/20.15.2/SET-TRFCDFDSWITCH]] · SET TRFCDFDSWITCH

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询大流量攻击防护配置（LST-TRFCDFDSWITCH）_82837761.md`
- 原始手册：`evidence/UDG/20.15.2/设置大流量攻击防护功能（SET-TRFCDFDSWITCH）_82837760.md`
