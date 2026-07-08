---
id: UNC@20.15.2@ConfigObject@IUSMPROCTRL
type: ConfigObject
name: IUSMPROCTRL（Iu模式SM流程控制参数）
nf: UNC
version: 20.15.2
object_name: IUSMPROCTRL
object_kind: global_setting
applicable_nf:
- SGSN
status: active
---

# IUSMPROCTRL（Iu模式SM流程控制参数）

## 说明

![](设置Iu模式SM流程控制参数（SET IUSMPROCTRL）_72345289.assets/notice_3.0-zh-cn_2.png)

下发不合适的原因值可能导致UE无法进行业务。

**适用网元：SGSN**

该命令用于设置Iu模式SM流程控制参数。在用户接入Iu模式时， UNC 可通过该命令控制SM流程进行特殊处理以及特殊场景下指定的原因值下发，以满足运营商实现对现网设备兼容性特殊控制的需求。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-IUSMPROCTRL]] · LST IUSMPROCTRL
- [[command/UNC/20.15.2/SET-IUSMPROCTRL]] · SET IUSMPROCTRL

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Iu模式SM流程控制参数（LST-IUSMPROCTRL）_26145694.md`
- 原始手册：`evidence/UNC/20.15.2/设置Iu模式SM流程控制参数（SET-IUSMPROCTRL）_72345289.md`
