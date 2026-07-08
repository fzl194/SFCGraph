---
id: UDG@20.15.2@ConfigObject@PLCYCKTIMERINR
type: ConfigObject
name: PLCYCKTIMERINR（策略类型和核查间隔）
nf: UDG
version: 20.15.2
object_name: PLCYCKTIMERINR
object_kind: global_setting
status: active
---

# PLCYCKTIMERINR（策略类型和核查间隔）

## 说明

该命令用于设置策略类型和核查间隔。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | POLICYTYPE | INTERVAL |
> | --- | --- |
> | Inner | 1 |
> | Outer | 10 |

## 操作本对象的命令

- [LST PLCYCKTIMERINR](command/UDG/20.15.2/LST-PLCYCKTIMERINR.md)
- [SET PLCYCKTIMERINR](command/UDG/20.15.2/SET-PLCYCKTIMERINR.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询策略类型和核查间隔（LST-PLCYCKTIMERINR）_94850110.md`
- 原始手册：`evidence/UDG/20.15.2/设置策略类型和核查间隔（SET-PLCYCKTIMERINR）_95010102.md`
