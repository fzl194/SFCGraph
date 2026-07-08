---
id: UNC@20.15.2@ConfigObject@HTTPFCIPGRP
type: ConfigObject
name: HTTPFCIPGRP（HTTP流控组）
nf: UNC
version: 20.15.2
object_name: HTTPFCIPGRP
object_kind: entity
status: active
---

# HTTPFCIPGRP（HTTP流控组）

## 说明

该命令用于增加HTTP固定速率流控的IP地址组信息。出于可靠性目的，NF的服务化接口一般会通过多个HTTP链路和周边NF进行交互，每条链路会有自己的IP地址，在流控场景下，可以通过将多条链路绑定在一起（即流控组），系统对流控组执行统一的流控策略（如流控门限等）。

## 操作本对象的命令

- [ADD HTTPFCIPGRP](command/UNC/20.15.2/ADD-HTTPFCIPGRP.md)
- [LST HTTPFCIPGRP](command/UNC/20.15.2/LST-HTTPFCIPGRP.md)
- [MOD HTTPFCIPGRP](command/UNC/20.15.2/MOD-HTTPFCIPGRP.md)
- [RMV HTTPFCIPGRP](command/UNC/20.15.2/RMV-HTTPFCIPGRP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改HTTP流控组（MOD-HTTPFCIPGRP）_29291773.md`
- 原始手册：`evidence/UNC/20.15.2/删除HTTP流控组（RMV-HTTPFCIPGRP）_29291775.md`
- 原始手册：`evidence/UNC/20.15.2/增加HTTP流控组（ADD-HTTPFCIPGRP）_29053323.md`
- 原始手册：`evidence/UNC/20.15.2/查询HTTP流控组（LST-HTTPFCIPGRP）_83813632.md`
