---
id: UNC@20.15.2@ConfigObject@SYSTIMER
type: ConfigObject
name: SYSTIMER（系统定时器）
nf: UNC
version: 20.15.2
object_name: SYSTIMER
object_kind: global_setting
applicable_nf:
- NCG
status: active
---

# SYSTIMER（系统定时器）

## 说明

**适用NF：NCG**

该命令用于设置NCG的系统定时器时长。其中系统定时器包括统计2G/3G的PDP信息老化定时器、统计4G的Bearer信息老化定时器。对超过定时器时长的信息执行老化操作，防止无用数据对统计准确性的干扰。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-SYSTIMER]] · LST SYSTIMER
- [[command/UNC/20.15.2/SET-SYSTIMER]] · SET SYSTIMER

## 证据

- 原始手册：`evidence/UNC/20.15.2/SYSTIMER.md`
- 原始手册：`evidence/UNC/20.15.2/SYSTIMER.md`
