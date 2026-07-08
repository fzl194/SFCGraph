---
id: UNC@20.15.2@ConfigObject@EMMPROCTRL
type: ConfigObject
name: EMMPROCTRL（S1模式移动性管理流程控制参数）
nf: UNC
version: 20.15.2
object_name: EMMPROCTRL
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# EMMPROCTRL（S1模式移动性管理流程控制参数）

## 说明

![](设置S1模式移动性管理流程控制参数(SET EMMPROCTRL)_72225199.assets/notice_3.0-zh-cn_2.png)

通过该命令配置不合适的原因值下发给UE后，可能导致UE无法进行业务。

**适用网元：MME**

在用户接入S1模式时， UNC 可通过此命令控制MM流程进行特殊处理以及特殊场景下指定的原因值下发，以满足运营商实现对现网设备兼容性特殊控制的需求。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-EMMPROCTRL]] · LST EMMPROCTRL
- [[command/UNC/20.15.2/SET-EMMPROCTRL]] · SET EMMPROCTRL

## 证据

- 原始手册：`evidence/UNC/20.15.2/EMMPROCTRL.md`
- 原始手册：`evidence/UNC/20.15.2/EMMPROCTRL.md`
