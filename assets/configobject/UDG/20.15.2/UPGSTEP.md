---
id: UDG@20.15.2@ConfigObject@UPGSTEP
type: ConfigObject
name: UPGSTEP（灰度升级Pod滚动步长）
nf: UDG
version: 20.15.2
object_name: UPGSTEP
object_kind: global_setting
status: active
---

# UPGSTEP（灰度升级Pod滚动步长）

## 说明

灰度升级流程中，执行此命令，用于设置灰度升级Pod滚动步长。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | PODTYPE | REDUNDANCY |
> | --- | --- |
> | Service | 25 |
> | Link | 25 |
> | Lbf | 25 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-UPGSTEP]] · LST UPGSTEP
- [[command/UDG/20.15.2/SET-UPGSTEP]] · SET UPGSTEP

## 证据

- 原始手册：`evidence/UDG/20.15.2/UPGSTEP.md`
- 原始手册：`evidence/UDG/20.15.2/UPGSTEP.md`
