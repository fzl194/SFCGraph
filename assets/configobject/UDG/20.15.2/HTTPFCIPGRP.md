---
id: UDG@20.15.2@ConfigObject@HTTPFCIPGRP
type: ConfigObject
name: HTTPFCIPGRP（HTTP流控组）
nf: UDG
version: 20.15.2
object_name: HTTPFCIPGRP
object_kind: entity
status: active
---

# HTTPFCIPGRP（HTTP流控组）

## 说明

该命令用于增加HTTP固定速率流控的IP地址组信息。出于可靠性目的，NF的服务化接口一般会通过多个HTTP链路和周边NF进行交互，每条链路会有自己的IP地址，在流控场景下，可以通过将多条链路绑定在一起（即流控组），系统对流控组执行统一的流控策略（如流控门限等）。

> **说明**
> - 该命令执行后立即生效。
>
> - 添加该命令后通过执行[**ADD HTTPFIXEDFC**](../HTTP流控组固定速率流控管理/增加HTTP流控组固定速率流控信息（ADD HTTPFIXEDFC）_83972180.md)命令设置对应的门限值。
>
> - 最多可输入4096条记录。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-HTTPFCIPGRP]] · ADD HTTPFCIPGRP
- [[command/UDG/20.15.2/LST-HTTPFCIPGRP]] · LST HTTPFCIPGRP
- [[command/UDG/20.15.2/MOD-HTTPFCIPGRP]] · MOD HTTPFCIPGRP
- [[command/UDG/20.15.2/RMV-HTTPFCIPGRP]] · RMV HTTPFCIPGRP

## 证据

- 原始手册：`evidence/UDG/20.15.2/HTTPFCIPGRP.md`
- 原始手册：`evidence/UDG/20.15.2/HTTPFCIPGRP.md`
- 原始手册：`evidence/UDG/20.15.2/HTTPFCIPGRP.md`
- 原始手册：`evidence/UDG/20.15.2/HTTPFCIPGRP.md`
