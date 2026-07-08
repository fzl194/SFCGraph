---
id: UDG@20.15.2@ConfigObject@HAFFUNC
type: ConfigObject
name: HAFFUNC（HAF服务内部功能的参数）
nf: UDG
version: 20.15.2
object_name: HAFFUNC
object_kind: global_setting
status: active
---

# HAFFUNC（HAF服务内部功能的参数）

## 说明

当前版本配置此命令不生效。

该命令用于设置HAF服务内部功能的相关参数。

> **说明**
> - 该命令执行后立即生效。
>
> - 当前版本参数MCENHANCED的配置不生效。
> - 为避免频繁执行对系统性能产生冲击，该命令在三分钟之内只能执行一次。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | DOMAINFAULT | MCENHANCED |
> | --- | --- |
> | ON | ON |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-HAFFUNC]] · LST HAFFUNC
- [[command/UDG/20.15.2/SET-HAFFUNC]] · SET HAFFUNC

## 证据

- 原始手册：`evidence/UDG/20.15.2/HAFFUNC.md`
- 原始手册：`evidence/UDG/20.15.2/HAFFUNC.md`
