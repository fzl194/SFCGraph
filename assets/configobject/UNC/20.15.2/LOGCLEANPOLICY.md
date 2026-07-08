---
id: UNC@20.15.2@ConfigObject@LOGCLEANPOLICY
type: ConfigObject
name: LOGCLEANPOLICY（日志老化策略）
nf: UNC
version: 20.15.2
object_name: LOGCLEANPOLICY
object_kind: global_setting
status: active
---

# LOGCLEANPOLICY（日志老化策略）

## 说明

本命令用于设置审计日志老化策略。

日志老化策略包括日志存留期和日志占用空间，用于设置系统对日志的最大存留时长和最大占用空间大小。当日志超过最大存留时长或者最大占用空间大小时，系统按照日志产生时间，删除最老的日志。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-LOGCLEANPOLICY]] · LST LOGCLEANPOLICY
- [[command/UNC/20.15.2/SET-LOGCLEANPOLICY]] · SET LOGCLEANPOLICY

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询日志老化策略（LST-LOGCLEANPOLICY）_36328275.md`
- 原始手册：`evidence/UNC/20.15.2/设置日志老化策略（SET-LOGCLEANPOLICY）_89791758.md`
