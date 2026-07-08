---
id: UNC@20.15.2@ConfigObject@S1SMPROCTRL
type: ConfigObject
name: S1SMPROCTRL（S1模式SM流程控制参数）
nf: UNC
version: 20.15.2
object_name: S1SMPROCTRL
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# S1SMPROCTRL（S1模式SM流程控制参数）

## 说明

![](设置S1模式SM流程控制参数(SET S1SMPROCTRL)_26305504.assets/notice_3.0-zh-cn_2.png)

通过该命令配置不合适的原因值下发给UE后，可能导致UE无法进行业务。

**适用网元：MME**

该命令用于设置S1模式SM流程控制参数。当用户接入S1模式时， UNC 可通过该命令控制SM流程进行特殊处理以及特殊场景下指定的原因值下发，以满足运营商实现对现网设备兼容性特殊控制的需求。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-S1SMPROCTRL]] · LST S1SMPROCTRL
- [[command/UNC/20.15.2/SET-S1SMPROCTRL]] · SET S1SMPROCTRL

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询S1模式SM流程控制参数(LST-S1SMPROCTRL)_72345291.md`
- 原始手册：`evidence/UNC/20.15.2/设置S1模式SM流程控制参数(SET-S1SMPROCTRL)_26305504.md`
