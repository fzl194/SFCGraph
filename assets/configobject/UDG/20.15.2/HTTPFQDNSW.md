---
id: UDG@20.15.2@ConfigObject@HTTPFQDNSW
type: ConfigObject
name: HTTPFQDNSW（HTTP是否支持FQDN）
nf: UDG
version: 20.15.2
object_name: HTTPFQDNSW
object_kind: global_setting
status: active
---

# HTTPFQDNSW（HTTP是否支持FQDN）

## 说明

该命令用于设置HTTP是否支持FQDN。

- 当前应用场景：控制HTTP是否使用响应报文中Location字段携带的FQDN。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | GLOBALSW | INDIRECTSW |
> | --- | --- |
> | OFF | OFF |

## 操作本对象的命令

- [LST HTTPFQDNSW](command/UDG/20.15.2/LST-HTTPFQDNSW.md)
- [SET HTTPFQDNSW](command/UDG/20.15.2/SET-HTTPFQDNSW.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询HTTP是否支持FQDN（LST-HTTPFQDNSW）_04291629.md`
- 原始手册：`evidence/UDG/20.15.2/设置HTTP是否支持FQDN（SET-HTTPFQDNSW）_54530882.md`
