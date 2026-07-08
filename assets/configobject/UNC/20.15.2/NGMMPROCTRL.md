---
id: UNC@20.15.2@ConfigObject@NGMMPROCTRL
type: ConfigObject
name: NGMMPROCTRL（5G移动性管理流程控制参数）
nf: UNC
version: 20.15.2
object_name: NGMMPROCTRL
object_kind: global_setting
applicable_nf:
- AMF
status: active
---

# NGMMPROCTRL（5G移动性管理流程控制参数）

## 说明

![](设置5G移动性管理流程控制参数（SET NGMMPROCTRL）_09652386.assets/notice_3.0-zh-cn_2.png)

执行该命令配置的原因值不合理可能导致用户无法驻留网络，影响用户业务。

**适用NF：AMF**

在用户接入5G时，AMF可通过此命令控制MM流程进行特殊处理以及特殊场景下指定的原因值下发，以满足运营商实现对现网设备兼容性特殊控制的需求。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-NGMMPROCTRL]] · LST NGMMPROCTRL
- [[command/UNC/20.15.2/SET-NGMMPROCTRL]] · SET NGMMPROCTRL

## 证据

- 原始手册：`evidence/UNC/20.15.2/NGMMPROCTRL.md`
- 原始手册：`evidence/UNC/20.15.2/NGMMPROCTRL.md`
