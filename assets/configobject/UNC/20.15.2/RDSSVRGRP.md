---
id: UNC@20.15.2@ConfigObject@RDSSVRGRP
type: ConfigObject
name: RDSSVRGRP（Radius服务器组）
nf: UNC
version: 20.15.2
object_name: RDSSVRGRP
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# RDSSVRGRP（Radius服务器组）

## 说明

**适用NF：PGW-C、SMF**

该命令用来配置RADIUS服务器组信息，具体为：

1、配置RADIUS服务器组名称。

2、配置RADIUS服务器组工作模式。

3、配置RADIUS服务器组可选计费消息属性。

4、配置RADIUS服务器组是否支持利用鉴权服务器计费特性。

5、配置RADIUS消息的超时时间和重发次数。

## 操作本对象的命令

- [ADD RDSSVRGRP](command/UNC/20.15.2/ADD-RDSSVRGRP.md)
- [LST RDSSVRGRP](command/UNC/20.15.2/LST-RDSSVRGRP.md)
- [MOD RDSSVRGRP](command/UNC/20.15.2/MOD-RDSSVRGRP.md)
- [RMV RDSSVRGRP](command/UNC/20.15.2/RMV-RDSSVRGRP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Radius服务器组（MOD-RDSSVRGRP）_09896731.md`
- 原始手册：`evidence/UNC/20.15.2/删除Radius服务器组（RMV-RDSSVRGRP）_09896732.md`
- 原始手册：`evidence/UNC/20.15.2/增加Radius服务器组（ADD-RDSSVRGRP）_09896730.md`
- 原始手册：`evidence/UNC/20.15.2/查询Radius服务器组（LST-RDSSVRGRP）_09896733.md`
