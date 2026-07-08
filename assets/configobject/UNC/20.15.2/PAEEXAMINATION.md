---
id: UNC@20.15.2@ConfigObject@PAEEXAMINATION
type: ConfigObject
name: PAEEXAMINATION（PAE故障检测使能配置）
nf: UNC
version: 20.15.2
object_name: PAEEXAMINATION
object_kind: global_setting
status: active
---

# PAEEXAMINATION（PAE故障检测使能配置）

## 说明

该命令用于开启或关闭PAE故障检测功能。

PAE故障检测功能提供了转发线程死循环、通道过载、通道破坏、队列过载等检测能力。

使能PAE故障检测时，当PAE检测到故障后，会根据业务订阅的故障类型，将对应的故障上报给业务，同时PAE会根据故障恢复策略执行故障恢复。

在故障检测去使能的情况下，PAE不会对故障做检测。

建议保持该开关为默认的使能状态。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-PAEEXAMINATION]] · LST PAEEXAMINATION
- [[command/UNC/20.15.2/SET-PAEEXAMINATION]] · SET PAEEXAMINATION

## 证据

- 原始手册：`evidence/UNC/20.15.2/PAEEXAMINATION.md`
- 原始手册：`evidence/UNC/20.15.2/PAEEXAMINATION.md`
