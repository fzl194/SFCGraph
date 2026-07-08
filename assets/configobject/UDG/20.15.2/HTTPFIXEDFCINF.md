---
id: UDG@20.15.2@ConfigObject@HTTPFIXEDFCINF
type: ConfigObject
name: HTTPFIXEDFCINF（HTTP接口类型固定速率流控信息）
nf: UDG
version: 20.15.2
object_name: HTTPFIXEDFCINF
object_kind: entity
status: active
---

# HTTPFIXEDFCINF（HTTP接口类型固定速率流控信息）

## 说明

![](增加HTTP接口类型固定速率流控信息（ADD HTTPFIXEDFCINF）_52121330.assets/notice_3.0-zh-cn.png)

该命令中是否携带Retry-After消息头参数可能会导致对端网元不发请求消息，需慎用。

该命令用于增加HTTP接口类型固定速率流控门限值等信息，可以单独配置客户端和服务端的流控门限值。

> **说明**
> - 该命令执行后立即生效。
>
> - 添加该命令前需要执行[**ADD HTTPOFC**](../../HTTP管理/HTTP局向管理/增加HTTP局向（ADD HTTPOFC）_35230482.md)增加局向信息。
> - 此命令配置的发送消息流控门限或接收消息流控门限为整机粒度，门限值会均分到所有HTTP进程，即单HTTP进程流控门限=设置流控门限/sbim-pod数/单sbim-pod内HTTP进程数。
> - 使用约束与建议：（1）网元作为客户端：到对端局向网元采用每进程建链的方式，且每条链路的负载相对均衡的场景，流控能达到比较好的效果，与设定的流控门限接近；到对端网元建立的链路数量采用整系统方式控制或链路负载不均的场景，流控效果会低于甚至远低于设置预期流控门限。（2）网元作为服务端：由对端网元决定建链位置与单链路的负载，在建链位置均匀分布在sbim进程且单链路流量均衡的场景，流控效果较好，与设定的流控门限接近。反之，会低于甚至远低于设置的预期流控门限。
>
> - 最多可输入4096条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-HTTPFIXEDFCINF]] · ADD HTTPFIXEDFCINF
- [[command/UDG/20.15.2/LST-HTTPFIXEDFCINF]] · LST HTTPFIXEDFCINF
- [[command/UDG/20.15.2/MOD-HTTPFIXEDFCINF]] · MOD HTTPFIXEDFCINF
- [[command/UDG/20.15.2/RMV-HTTPFIXEDFCINF]] · RMV HTTPFIXEDFCINF

## 证据

- 原始手册：`evidence/UDG/20.15.2/HTTPFIXEDFCINF.md`
- 原始手册：`evidence/UDG/20.15.2/HTTPFIXEDFCINF.md`
- 原始手册：`evidence/UDG/20.15.2/HTTPFIXEDFCINF.md`
- 原始手册：`evidence/UDG/20.15.2/HTTPFIXEDFCINF.md`
