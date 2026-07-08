---
id: UDG@20.15.2@ConfigObject@HTTPFCMSG
type: ConfigObject
name: HTTPFCMSG（HTTP流控消息类型）
nf: UDG
version: 20.15.2
object_name: HTTPFCMSG
object_kind: entity
status: active
---

# HTTPFCMSG（HTTP流控消息类型）

## 说明

![](增加HTTP流控消息类型（ADD HTTPFCMSG）_01544142.assets/notice_3.0-zh-cn.png)

新增流控消息需谨慎，建议只针对业务流程首消息开启流控，避免影响E2E业务成功率。

该命令用于增加HTTP流控消息类型。

> **说明**
> - 该命令执行后立即生效。
>
> - 参数FCTYPE取值为TCPBPFC时，执行该命令会导致TCP CPU反压流控暂时停止。
>
> - 最多可输入512条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-HTTPFCMSG]] · ADD HTTPFCMSG
- [[command/UDG/20.15.2/LST-HTTPFCMSG]] · LST HTTPFCMSG
- [[command/UDG/20.15.2/MOD-HTTPFCMSG]] · MOD HTTPFCMSG
- [[command/UDG/20.15.2/RMV-HTTPFCMSG]] · RMV HTTPFCMSG

## 证据

- 原始手册：`evidence/UDG/20.15.2/HTTPFCMSG.md`
- 原始手册：`evidence/UDG/20.15.2/HTTPFCMSG.md`
- 原始手册：`evidence/UDG/20.15.2/HTTPFCMSG.md`
- 原始手册：`evidence/UDG/20.15.2/HTTPFCMSG.md`
