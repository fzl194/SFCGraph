---
id: UDG@20.15.2@ConfigObject@HTTPGLBFIXEDBWFC
type: ConfigObject
name: HTTPGLBFIXEDBWFC（HTTP全局固定带宽流控）
nf: UDG
version: 20.15.2
object_name: HTTPGLBFIXEDBWFC
object_kind: global_setting
status: active
---

# HTTPGLBFIXEDBWFC（HTTP全局固定带宽流控）

## 说明

![](设置HTTP全局固定带宽流控（SET HTTPGLBFIXEDBWFC）_56474481.assets/notice_3.0-zh-cn.png)

门限值由本端和对端网元的消息处理能力决定。设置过低会导致消息被丢弃，设置过高起不到保护本端和对端网元不过载的作用。

该命令用于设置HTTP全局固定带宽流控门限等信息，设置后所有链路都使用相同的参数控制。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SENDFCSWITCH | RECVFCSWITCH | SENDTHD | RECVTHD | SENDBIGPKTTHD | RECVBIGPKTTHD | STATUSCODE |
> | --- | --- | --- | --- | --- | --- | --- |
> | OFF | OFF | 0 | 0 | 0 | 0 | TooManyRequests |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-HTTPGLBFIXEDBWFC]] · LST HTTPGLBFIXEDBWFC
- [[command/UDG/20.15.2/SET-HTTPGLBFIXEDBWFC]] · SET HTTPGLBFIXEDBWFC

## 证据

- 原始手册：`evidence/UDG/20.15.2/HTTPGLBFIXEDBWFC.md`
- 原始手册：`evidence/UDG/20.15.2/HTTPGLBFIXEDBWFC.md`
