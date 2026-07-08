---
id: UDG@20.15.2@ConfigObject@PAEDEBUGSWITCH
type: ConfigObject
name: PAEDEBUGSWITCH（使能或去使能PAE转发日志）
nf: UDG
version: 20.15.2
object_name: PAEDEBUGSWITCH
object_kind: global_setting
status: active
---

# PAEDEBUGSWITCH（使能或去使能PAE转发日志）

## 说明

![](使能或去使能PAE转发日志（SET PAEDEBUGSWITCH）_92520051.assets/notice_3.0-zh-cn.png)

本功能使能会降低性能，去使能之后性能恢复，使能后在120分钟后自动去使能。

该命令用来打开和关闭PAE转发流程记录日志的功能。

在PAE转发流程的异常分支中，由转发日志开关控制是否记录异常日志。

转发日志开关默认是关闭的。

## 操作本对象的命令

- [[command/UDG/20.15.2/SET-PAEDEBUGSWITCH]] · SET PAEDEBUGSWITCH

## 证据

- 原始手册：`evidence/UDG/20.15.2/PAEDEBUGSWITCH.md`
