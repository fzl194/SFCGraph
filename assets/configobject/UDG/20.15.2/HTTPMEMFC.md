---
id: UDG@20.15.2@ConfigObject@HTTPMEMFC
type: ConfigObject
name: HTTPMEMFC（HTTP内存流控）
nf: UDG
version: 20.15.2
object_name: HTTPMEMFC
object_kind: global_setting
status: active
---

# HTTPMEMFC（HTTP内存流控）

## 说明

设置HTTP Body内存分区的内存流控。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | MEMFCSWITCH | MEMFCSTARTTHD | MEMFCSTOPTHD | MEMFCBIGPKTTHD |
> | --- | --- | --- | --- |
> | TRUE | 30 | 50 | 512 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-HTTPMEMFC]] · LST HTTPMEMFC
- [[command/UDG/20.15.2/SET-HTTPMEMFC]] · SET HTTPMEMFC

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询HTTP内存流控（LST-HTTPMEMFC）_01544146.md`
- 原始手册：`evidence/UDG/20.15.2/设置HTTP内存流控（SET-HTTPMEMFC）_01384198.md`
