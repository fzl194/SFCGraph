---
id: UDG@20.15.2@ConfigObject@PAERESOVLDTRHD
type: ConfigObject
name: PAERESOVLDTRHD（PAE关键资源不足告警参数）
nf: UDG
version: 20.15.2
object_name: PAERESOVLDTRHD
object_kind: global_setting
status: active
---

# PAERESOVLDTRHD（PAE关键资源不足告警参数）

## 说明

该命令用于修改PAE关键资源不足告警的参数。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | RESTYPE | PERIOD | OVERLOADTHD | OVERLOADNUM | RECOVERTHD | RECOVERNUM |
> | --- | --- | --- | --- | --- | --- |
> | PAE_CHANNEL_QUE | 5 | 100 | 5 | 100 | 12 |
> | PAE_EXTPORT_QUE | 5 | 100 | 5 | 100 | 12 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-PAERESOVLDTRHD]] · LST PAERESOVLDTRHD
- [[command/UDG/20.15.2/SET-PAERESOVLDTRHD]] · SET PAERESOVLDTRHD

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询PAE关键资源不足告警参数（LST-PAERESOVLDTRHD）_25021333.md`
- 原始手册：`evidence/UDG/20.15.2/设置PAE关键资源不足告警参数（SET-PAERESOVLDTRHD）_53828096.md`
