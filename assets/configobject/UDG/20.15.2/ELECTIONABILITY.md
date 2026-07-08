---
id: UDG@20.15.2@ConfigObject@ELECTIONABILITY
type: ConfigObject
name: ELECTIONABILITY（业务进程选举能力）
nf: UDG
version: 20.15.2
object_name: ELECTIONABILITY
object_kind: global_setting
status: active
---

# ELECTIONABILITY（业务进程选举能力）

## 说明

该命令已废弃。

该命令用于设置业务进程选举能力的开关。仅当无损升级脚本不可用时，手动执行该命令设置业务进程的选举能力。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | MODE |
> | --- |
> | ENABLE |

## 操作本对象的命令

- [LST ELECTIONABILITY](command/UDG/20.15.2/LST-ELECTIONABILITY.md)
- [SET ELECTIONABILITY](command/UDG/20.15.2/SET-ELECTIONABILITY.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询业务进程选举能力（LST-ELECTIONABILITY）_42938063.md`
- 原始手册：`evidence/UDG/20.15.2/设置业务进程选举能力（SET-ELECTIONABILITY）_42938110.md`
