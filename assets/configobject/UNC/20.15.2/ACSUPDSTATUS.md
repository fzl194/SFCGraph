---
id: UNC@20.15.2@ConfigObject@ACSUPDSTATUS
type: ConfigObject
name: ACSUPDSTATUS（升级状态）
nf: UNC
version: 20.15.2
object_name: ACSUPDSTATUS
object_kind: global_setting
status: active
---

# ACSUPDSTATUS（升级状态）

## 说明

![](设置升级状态（SET ACSUPDSTATUS）_34280051.assets/notice_3.0-zh-cn_2.png)

该命令属于高危命令，执行该命令会设置升级状态，某些服务的状态会受到影响。若错误设置某些服务的升级状态，可能会导致该服务升级失败。请谨慎使用。

该命令用于设置RU升级开始和结束。

本命令只适用于ACS服务，其他微服务请使用SET UPDSTATUS命令。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-ACSUPDSTATUS]] · DSP ACSUPDSTATUS
- [[command/UNC/20.15.2/SET-ACSUPDSTATUS]] · SET ACSUPDSTATUS

## 证据

- 原始手册：`evidence/UNC/20.15.2/ACSUPDSTATUS.md`
- 原始手册：`evidence/UNC/20.15.2/ACSUPDSTATUS.md`
