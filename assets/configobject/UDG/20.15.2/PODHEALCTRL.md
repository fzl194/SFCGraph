---
id: UDG@20.15.2@ConfigObject@PODHEALCTRL
type: ConfigObject
name: PODHEALCTRL（自愈功能配置信息）
nf: UDG
version: 20.15.2
object_name: PODHEALCTRL
object_kind: global_setting
status: active
---

# PODHEALCTRL（自愈功能配置信息）

## 说明

该命令用于设置是否启动pod自愈，若开关打开，则按照 [**SET PODHEALPLY**](设置Pod自愈策略（SET PODHEALPLY）_09587937.md) 命令配置的pod自愈策略进行自愈；若开关关闭，则不进行pod自愈。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SWITCH |
> | --- |
> | ENABLE |

## 操作本对象的命令

- [LST PODHEALCTRL](command/UDG/20.15.2/LST-PODHEALCTRL.md)
- [SET PODHEALCTRL](command/UDG/20.15.2/SET-PODHEALCTRL.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询自愈功能配置信息（LST-PODHEALCTRL）_09587931.md`
- 原始手册：`evidence/UDG/20.15.2/设置自愈功能开关状态（SET-PODHEALCTRL）_09587383.md`
