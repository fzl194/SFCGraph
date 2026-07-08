---
id: UNC@20.15.2@ConfigObject@TRC_CFG
type: ConfigObject
name: TRC_CFG（跟踪参数）
nf: UNC
version: 20.15.2
object_name: TRC_CFG
object_kind: global_setting
applicable_nf:
- SGSN
- MME
status: active
---

# TRC_CFG（跟踪参数）

## 说明

**适用网元：SGSN、MME**

该命令用于设置GB、GB NS接口跟踪、随机用户跟踪和用户跟踪参数。用户跟踪表示跟踪以IMSI（International Mobile Subscriber Identity）或MSISDN（Mobile Station International ISDN Number）为标识的特定用户消息；随机用户跟踪表示基于设置的条件，随机性的选择满足触发条件的任何用户并上报其用户跟踪；接口跟踪表示跟踪接口的消息。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-TRC_CFG]] · LST TRC_CFG
- [[command/UNC/20.15.2/SET-TRC_CFG]] · SET TRC_CFG

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询跟踪参数(LST-TRC_CFG)_72344999.md`
- 原始手册：`evidence/UNC/20.15.2/设置跟踪参数(SET-TRC_CFG)_26305212.md`
