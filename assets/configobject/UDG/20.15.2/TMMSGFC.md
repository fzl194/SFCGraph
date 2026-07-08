---
id: UDG@20.15.2@ConfigObject@TMMSGFC
type: ConfigObject
name: TMMSGFC（跟踪消息流控状态）
nf: UDG
version: 20.15.2
object_name: TMMSGFC
object_kind: global_setting
status: active
---

# TMMSGFC（跟踪消息流控状态）

## 说明

该命令用于设置跟踪消息流控状态。

从跟踪服务到Web客户端的消息流控操作前后，均能够以每秒500条的消息推送。

> **说明**
> 由于跟踪能力提升，跟踪推送消息默认条数基线从100条增加到500条。

> **说明**
> - 该命令存在系统初始记录，参数“客户端启用流控”的初始设定值为“YES(是)”。
> - 当客户端启用流控设置为“NO(否)”时，会导致在线跟踪功能性能下降。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-TMMSGFC]] · LST TMMSGFC
- [[command/UDG/20.15.2/SET-TMMSGFC]] · SET TMMSGFC

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询跟踪消息流控状态（LST-TMMSGFC）_91175914.md`
- 原始手册：`evidence/UDG/20.15.2/设置跟踪消息流控状态（SET-TMMSGFC）_37693591.md`
