---
id: UNC@20.15.2@ConfigObject@GBSMPROCTRL
type: ConfigObject
name: GBSMPROCTRL（Gb模式SM流程控制参数）
nf: UNC
version: 20.15.2
object_name: GBSMPROCTRL
object_kind: global_setting
applicable_nf:
- SGSN
status: active
---

# GBSMPROCTRL（Gb模式SM流程控制参数）

## 说明

![](设置Gb模式SM流程控制参数（SET GBSMPROCTRL）_26145692.assets/notice_3.0-zh-cn_2.png)

通过该命令配置不合适的原因值下发给MS后，可能导致MS无法进行业务。

**适用网元：SGSN**

该命令用于设置Gb模式SM流程控制参数。在用户接入Gb模式时， UNC 可通过该命令控制SM流程进行特殊处理以及特殊场景下指定的原因值下发，以满足运营商实现对现网设备兼容性特殊控制的需求。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-GBSMPROCTRL]] · LST GBSMPROCTRL
- [[command/UNC/20.15.2/SET-GBSMPROCTRL]] · SET GBSMPROCTRL

## 证据

- 原始手册：`evidence/UNC/20.15.2/GBSMPROCTRL.md`
- 原始手册：`evidence/UNC/20.15.2/GBSMPROCTRL.md`
