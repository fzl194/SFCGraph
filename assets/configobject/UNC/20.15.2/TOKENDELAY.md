---
id: UNC@20.15.2@ConfigObject@TOKENDELAY
type: ConfigObject
name: TOKENDELAY（Token延时迁移时间）
nf: UNC
version: 20.15.2
object_name: TOKENDELAY
object_kind: global_setting
status: active
---

# TOKENDELAY（Token延时迁移时间）

## 说明

![](设置Token延时迁移时间（SET TOKENDELAY）_79244269.assets/notice_3.0-zh-cn_2.png)

执行此命令可能导致系统没有可用的实例。

执行此命令可能导致扩容、服务实例故障恢复的时间延长。

本次命令将修改TokenDelay，请务必在华为技术支持人员的指导下使用该命令。

该命令用于修改Token的延时迁移时间，对整系统生效。可以用于在某个服务实例状态转为Normal，并准备分配或迁移Token时，实现延时定时器功能。当超过定时器时长时，再将Token迁入到该实例。

Token可以理解为NF内部服务使用的短期令牌，当且仅当手持令牌时，才能获取所需服务。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-TOKENDELAY]] · LST TOKENDELAY
- [[command/UNC/20.15.2/SET-TOKENDELAY]] · SET TOKENDELAY

## 证据

- 原始手册：`evidence/UNC/20.15.2/TOKENDELAY.md`
- 原始手册：`evidence/UNC/20.15.2/TOKENDELAY.md`
