---
id: UDG@20.15.2@ConfigObject@CUINCONSPOLICY
type: ConfigObject
name: CUINCONSPOLICY（CP和UP关键配置不一致的处理策略）
nf: UDG
version: 20.15.2
object_name: CUINCONSPOLICY
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# CUINCONSPOLICY（CP和UP关键配置不一致的处理策略）

## 说明

**适用NF：PGW-U、UPF**

![](设置CP和UP关键配置不一致的处理策略（SET CUINCONSPOLICY）_64015288.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该命令仅用于紧急情况下的故障恢复，执行该命令可能会导致一定的计费误差，请谨慎使用。执行该命令将改变失败处理的原则，请确认已经进行了必要的预检查，并已获得了执行该命令的权限。

设置SMF/PGW-C和UPF/PGW-U关键配置不一致的处理策略。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-CUINCONSPOLICY]] · LST CUINCONSPOLICY
- [[command/UDG/20.15.2/SET-CUINCONSPOLICY]] · SET CUINCONSPOLICY

## 证据

- 原始手册：`evidence/UDG/20.15.2/CUINCONSPOLICY.md`
- 原始手册：`evidence/UDG/20.15.2/CUINCONSPOLICY.md`
