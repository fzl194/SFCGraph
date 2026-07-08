---
id: UDG@20.15.2@ConfigObject@GLOBALIMS
type: ConfigObject
name: GLOBALIMS（全局IMS配置）
nf: UDG
version: 20.15.2
object_name: GLOBALIMS
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# GLOBALIMS（全局IMS配置）

## 说明

**适用NF：PGW-U、UPF**

![](设置全局IMS配置（SET GLOBALIMS）_82837830.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，系统只配置了语音APN才能打开该开关。

该命令用来配置IMS互通相关的设置。当IMS使能开关打开时，才可以对IMS信令空口增强开关以及P-CSCF缺省组进行配置。当运营商需要控制IMS互通相关的参数时，可使用该命令对全局IMS配置参数进行配置。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-GLOBALIMS]] · LST GLOBALIMS
- [[command/UDG/20.15.2/SET-GLOBALIMS]] · SET GLOBALIMS

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询全局IMS配置（LST-GLOBALIMS）_82837831.md`
- 原始手册：`evidence/UDG/20.15.2/设置全局IMS配置（SET-GLOBALIMS）_82837830.md`
