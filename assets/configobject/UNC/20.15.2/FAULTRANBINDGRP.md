---
id: UNC@20.15.2@ConfigObject@FAULTRANBINDGRP
type: ConfigObject
name: FAULTRANBINDGRP（N3接口故障RAN与RAN组的绑定关系）
nf: UNC
version: 20.15.2
object_name: FAULTRANBINDGRP
object_kind: binding
applicable_nf:
- SGW-C
- SMF
status: active
---

# FAULTRANBINDGRP（N3接口故障RAN与RAN组的绑定关系）

## 说明

**适用NF：SGW-C、SMF**

该命令用于添加N3接口故障RAN与故障RAN组的绑定关系，当N3接口出现故障，SMF在为通过和故障RAN组绑定的RAN接入的用户选择UPF时，会自动过滤掉与该RAN组绑定的UPF组内的UPF。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-FAULTRANBINDGRP]] · ADD FAULTRANBINDGRP
- [[command/UNC/20.15.2/LST-FAULTRANBINDGRP]] · LST FAULTRANBINDGRP
- [[command/UNC/20.15.2/MOD-FAULTRANBINDGRP]] · MOD FAULTRANBINDGRP
- [[command/UNC/20.15.2/RMV-FAULTRANBINDGRP]] · RMV FAULTRANBINDGRP

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改N3接口故障RAN与RAN组的绑定关系（MOD-FAULTRANBINDGRP）_39737007.md`
- 原始手册：`evidence/UNC/20.15.2/删除N3接口故障RAN与RAN组的绑定关系（RMV-FAULTRANBINDGRP）_40016985.md`
- 原始手册：`evidence/UNC/20.15.2/增加N3接口故障RAN与RAN组的绑定关系（ADD-FAULTRANBINDGRP）_39777019.md`
- 原始手册：`evidence/UNC/20.15.2/查询N3接口故障RAN与RAN组的绑定关系（LST-FAULTRANBINDGRP）_94897066.md`
