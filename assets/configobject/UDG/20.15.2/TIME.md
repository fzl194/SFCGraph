---
id: UDG@20.15.2@ConfigObject@TIME
type: ConfigObject
name: TIME（系统时间）
nf: UDG
version: 20.15.2
object_name: TIME
object_kind: global_setting
status: active
---

# TIME（系统时间）

## 说明

![](设置系统时间（SET TIME）_87176066.assets/notice_3.0-zh-cn.png)

修改系统时间可能会影响话务统计、告警、日志等数据记录中时间信息的准确性，导致计费时间错乱，证书、License以及用户数据过期，系统瘫痪等，请慎重使用。

本命令用于设置网元系统的当前时间。

> **说明**
> - 新设置的时间需要与网元系统当前时间间隔不超过30秒。
> - 禁止在升级、打补丁、回退过程中、升级观察期内设置系统时间。
> - 在集群时间同步正常的情况下，修改时间后会被同步成NFV_FusionStage的时间。

## 操作本对象的命令

- [DSP TIME](command/UDG/20.15.2/DSP-TIME.md)
- [SET TIME](command/UDG/20.15.2/SET-TIME.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询系统时间（DSP-TIME）_33844132.md`
- 原始手册：`evidence/UDG/20.15.2/设置系统时间（SET-TIME）_87176066.md`
