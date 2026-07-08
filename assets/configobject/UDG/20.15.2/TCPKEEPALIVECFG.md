---
id: UDG@20.15.2@ConfigObject@TCPKEEPALIVECFG
type: ConfigObject
name: TCPKEEPALIVECFG（TCP保活参数）
nf: UDG
version: 20.15.2
object_name: TCPKEEPALIVECFG
object_kind: global_setting
status: active
---

# TCPKEEPALIVECFG（TCP保活参数）

## 说明

该命令用于设置TWAMP的Full模式TCP保活参数配置。

> **说明**
> - 该命令执行后在TCP链路重建时生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | KEEPALIVETIME | INTERVAL | RETRY |
> | --- | --- | --- |
> | 90 | 30 | 9 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-TCPKEEPALIVECFG]] · LST TCPKEEPALIVECFG
- [[command/UDG/20.15.2/SET-TCPKEEPALIVECFG]] · SET TCPKEEPALIVECFG

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询TCP保活参数（LST-TCPKEEPALIVECFG）_27102476.md`
- 原始手册：`evidence/UDG/20.15.2/设置TCP保活参数（SET-TCPKEEPALIVECFG）_27102484.md`
