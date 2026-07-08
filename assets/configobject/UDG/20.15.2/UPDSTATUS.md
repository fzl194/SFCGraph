---
id: UDG@20.15.2@ConfigObject@UPDSTATUS
type: ConfigObject
name: UPDSTATUS（升级状态）
nf: UDG
version: 20.15.2
object_name: UPDSTATUS
object_kind: global_setting
status: active
---

# UPDSTATUS（升级状态）

## 说明

![](设置升级状态（SET UPDSTATUS）_87929894.assets/notice_3.0-zh-cn.png)

该命令属于高危命令，执行该命令会设置升级状态，某些服务的状态会受到影响。若错误设置某些服务的升级状态，可能会导致该服务升级失败。请谨慎使用。

该命令用于设置RU升级开始和结束。

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-UPDSTATUS]] · DSP UPDSTATUS
- [[command/UDG/20.15.2/SET-UPDSTATUS]] · SET UPDSTATUS

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示升级状态（DSP-UPDSTATUS）_88089822.md`
- 原始手册：`evidence/UDG/20.15.2/设置升级状态（SET-UPDSTATUS）_87929894.md`
