---
id: UDG@20.15.2@ConfigObject@CSLOGFC
type: ConfigObject
name: CSLOGFC（日志流控开关）
nf: UDG
version: 20.15.2
object_name: CSLOGFC
object_kind: global_setting
status: active
---

# CSLOGFC（日志流控开关）

## 说明

![](设置日志流控开关（SET CSLOGFC）_09587953.assets/notice_3.0-zh-cn.png)

当日志级别为ERR以下时，关闭日志流控，会造成CPU升高，可能触发进程复位，导致业务呼损等严重后果，不建议操作。

此命令用于设置日志流控开关。

日志流控是指同一文件同一行的日志在1分钟之内打印数量不能超过10条，超过10条将进行流控，同一文件同一行的日志不进行打印。

> **说明**
> - 该命令执行后立即生效。
>
> - 日志流控只流控ERR级别以下的日志。在流控开关关闭时，不进行流控，此时如果日志级别调整为ERR以下，可能会导致CPU和内存升高。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | FCSWITCH |
> | --- |
> | ON |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-CSLOGFC]] · LST CSLOGFC
- [[command/UDG/20.15.2/SET-CSLOGFC]] · SET CSLOGFC

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询日志流控开关（LST-CSLOGFC）_09587860.md`
- 原始手册：`evidence/UDG/20.15.2/设置日志流控开关（SET-CSLOGFC）_09587953.md`
