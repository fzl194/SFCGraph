---
id: UDG@20.15.2@ConfigObject@SPECTRAFURRGRP
type: ConfigObject
name: SPECTRAFURRGRP（全局缺省费率的流量使用量上报规则组）
nf: UDG
version: 20.15.2
object_name: SPECTRAFURRGRP
object_kind: entity
applicable_nf:
- UPF
- PGW-U
status: active
---

# SPECTRAFURRGRP（全局缺省费率的流量使用量上报规则组）

## 说明

**适用NF：PGW-U、UPF**

![](设置全局缺省费率的流量使用量上报规则组（SET SPECTRAFURRGRP）_36146715.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，修改URRGROUPNAME参数会导致计费使用的全局缺省费率变化或业务不计费，造成运营商计费损失。

本命令用于设置全局缺省费率的流量使用量上报规则组。

1、BIT1232软参值设置为1时，特殊流量通过该规则组进行计费。

特殊流量是指当某些业务报文丢失，未能完成七层精确匹配时，已经转发的流量。

例如，在线计费用户下线时，业务流只有信令报文，没有业务报文。在这种场景下，已经转发的信令报文的流量称为特殊流量。

2、对于没有配置任何费率的业务场景，通过该规则组进行计费。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-SPECTRAFURRGRP]] · LST SPECTRAFURRGRP
- [[command/UDG/20.15.2/RMV-SPECTRAFURRGRP]] · RMV SPECTRAFURRGRP
- [[command/UDG/20.15.2/SET-SPECTRAFURRGRP]] · SET SPECTRAFURRGRP

## 证据

- 原始手册：`evidence/UDG/20.15.2/SPECTRAFURRGRP.md`
- 原始手册：`evidence/UDG/20.15.2/SPECTRAFURRGRP.md`
- 原始手册：`evidence/UDG/20.15.2/SPECTRAFURRGRP.md`
