---
id: UDG@20.15.2@ConfigObject@HTTPFCCONF
type: ConfigObject
name: HTTPFCCONF（HTTP流控属性）
nf: UDG
version: 20.15.2
object_name: HTTPFCCONF
object_kind: global_setting
status: active
---

# HTTPFCCONF（HTTP流控属性）

## 说明

![](设置HTTP流控属性（SET HTTPFCCONF）_00360897.assets/notice_3.0-zh-cn.png)

本命令为高危命令。关闭CPU跟踪流控功能，可能触发业务自保流控，导致业务受损；关闭跟踪流控功能，可能导致跟踪功能占用CPU比例过高，从而触发CPU跟踪流控导致跟踪功能失效。

该命令用于设置HTTP流控属性。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令只有一条记录，配置时因具有多个功能选项，需要多次配置，故配置导出时会导出多条。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | RETRYAFTERSW | MEMORYFCSW | FIRSTRATETHD | USERRATETHD | PROTOCOLBWTHD | INNERBWTHD | LARGEPKGTHD | INFRATETHD | TRACEFCSW | TRACECPUSW |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | OFF | ON | 100 | 300 | 1024 | 512 | 4096 | 40 | ON | ON |

## 操作本对象的命令

- [LST HTTPFCCONF](command/UDG/20.15.2/LST-HTTPFCCONF.md)
- [SET HTTPFCCONF](command/UDG/20.15.2/SET-HTTPFCCONF.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询HTTP流控属性（LST-HTTPFCCONF）_00360893.md`
- 原始手册：`evidence/UDG/20.15.2/设置HTTP流控属性（SET-HTTPFCCONF）_00360897.md`
