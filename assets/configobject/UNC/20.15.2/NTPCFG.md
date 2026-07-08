---
id: UNC@20.15.2@ConfigObject@NTPCFG
type: ConfigObject
name: NTPCFG（NTP时间同步参数）
nf: UNC
version: 20.15.2
object_name: NTPCFG
object_kind: global_setting
status: active
---

# NTPCFG（NTP时间同步参数）

## 说明

![](配置NTP时间同步参数(SET NTPCFG)_67679933.assets/notice_3.0-zh-cn_2.png)

修改时间同步告警阈值参数会影响NTP相关告警的上报。

系统开启自动同步策略后，每个同步周期会无条件与NTP服务器同步一次时间。

本命令用于设置NTP时间同步参数。

本命令的使用场景为：在开局或日常的操作维护活动中，操作员可使用本命令配置NTP服务器时间同步参数。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-NTPCFG]] · LST NTPCFG
- [[command/UNC/20.15.2/SET-NTPCFG]] · SET NTPCFG

## 证据

- 原始手册：`evidence/UNC/20.15.2/NTPCFG.md`
- 原始手册：`evidence/UNC/20.15.2/NTPCFG.md`
