---
id: UNC@20.15.2@ConfigObject@CDFTOKENPOLICY
type: ConfigObject
name: CDFTOKENPOLICY（CDF token策略）
nf: UNC
version: 20.15.2
object_name: CDFTOKENPOLICY
object_kind: global_setting
applicable_nf:
- NCG
status: active
---

# CDFTOKENPOLICY（CDF token策略）

## 说明

![](设置CDF token策略（SET CDFTOKENPOLICY）_14295033.assets/notice_3.0-zh-cn_2.png)

当CDFTOKENPOLICY开关配置为使能且设置cdf token权重时，会影响各个cgfa-pod与cgfb-pod或cgfa2-pod与cgfb2-pod之间的token权重分配，从而影响话务量均衡。

**适用NF：NCG**

该命令用于设置cdf token权重上报开关。

当需要上报cdf token权重时，可配置cdf权重开关为使能。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-CDFTOKENPOLICY]] · LST CDFTOKENPOLICY
- [[command/UNC/20.15.2/SET-CDFTOKENPOLICY]] · SET CDFTOKENPOLICY

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CDF-token策略（LST-CDFTOKENPOLICY）_66773960.md`
- 原始手册：`evidence/UNC/20.15.2/设置CDF-token策略（SET-CDFTOKENPOLICY）_14295033.md`
