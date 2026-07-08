---
id: UDG@20.15.2@ConfigObject@MONNFTHR
type: ConfigObject
name: MONNFTHR（正常状态网元的占比阈值）
nf: UDG
version: 20.15.2
object_name: MONNFTHR
object_kind: global_setting
status: active
---

# MONNFTHR（正常状态网元的占比阈值）

## 说明

该命令用于配置与当前网元具有容灾关系的其他网元中，状态正常的网元数目在所有网元数目的占比阈值。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | NFNORMALTHR |
> | --- |
> | 100 |

## 操作本对象的命令

- [LST MONNFTHR](command/UDG/20.15.2/LST-MONNFTHR.md)
- [SET MONNFTHR](command/UDG/20.15.2/SET-MONNFTHR.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询正常状态网元的占比阈值（LST-MONNFTHR）_02844813.md`
- 原始手册：`evidence/UDG/20.15.2/设置正常状态网元的占比阈值（SET-MONNFTHR）_66605040.md`
