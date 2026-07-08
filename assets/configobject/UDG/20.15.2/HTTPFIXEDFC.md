---
id: UDG@20.15.2@ConfigObject@HTTPFIXEDFC
type: ConfigObject
name: HTTPFIXEDFC（HTTP流控组固定速率流控信息）
nf: UDG
version: 20.15.2
object_name: HTTPFIXEDFC
object_kind: entity
status: active
---

# HTTPFIXEDFC（HTTP流控组固定速率流控信息）

## 说明

![](增加HTTP流控组固定速率流控信息（ADD HTTPFIXEDFC）_83972180.assets/notice_3.0-zh-cn.png)

该命令中是否携带Retry-After消息头参数可能会导致对端网元不发请求消息，需慎用。

该命令用于增加HTTP基于IP流控组固定速率流控门限值等信息，可以同时配置或单独配置客户端和服务端的流控门限值。

> **说明**
> - 该命令执行后立即生效。
>
> - 添加该命令前需要执行[**ADD HTTPFCIPGRP**](../HTTP流控组管理/增加HTTP流控组（ADD HTTPFCIPGRP）_29053323.md)增加流控组信息。在配置接收消息流控场景时需要注意无法做到只流控首消息。
> - 配置的阈值为GLBSENDTHD或GLBRECVTHD时，配置为整机流控，整机流控场景使用约束与建议：（1）网元作为客户端：到对端局向网元采用每进程建链的方式，且每条链路的负载相对均匀的场景，整机流控能达到比较好的效果，与设定的流控阈值接近；到对端网元建立的链路数量采用整系统方式控制或链路负载不均的场景，整机流控效果会低于甚至远低于设置预期流控阈值。（2）网元作为服务端：由对端网元决定建链位置与单链路的负载，在建链位置均匀分布在sbim进程且单链路流量均匀的场景，流控效果较好，与设定的流控阈值接近。反之，会低于甚至远低于设置的预期流控阈值。
>
> - 最多可输入4096条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-HTTPFIXEDFC]] · ADD HTTPFIXEDFC
- [[command/UDG/20.15.2/LST-HTTPFIXEDFC]] · LST HTTPFIXEDFC
- [[command/UDG/20.15.2/MOD-HTTPFIXEDFC]] · MOD HTTPFIXEDFC
- [[command/UDG/20.15.2/RMV-HTTPFIXEDFC]] · RMV HTTPFIXEDFC

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改HTTP流控组固定速率流控信息（MOD-HTTPFIXEDFC）_83653662.md`
- 原始手册：`evidence/UDG/20.15.2/删除HTTP流控组固定速率流控信息（RMV-HTTPFIXEDFC）_83653664.md`
- 原始手册：`evidence/UDG/20.15.2/增加HTTP流控组固定速率流控信息（ADD-HTTPFIXEDFC）_83972180.md`
- 原始手册：`evidence/UDG/20.15.2/查询HTTP流控组固定速率流控信息（LST-HTTPFIXEDFC）_29053329.md`
