---
id: UNC@20.15.2@ConfigObject@FAULTUPBINDGRP
type: ConfigObject
name: FAULTUPBINDGRP（N3接口故障UPF与UPF组的绑定关系）
nf: UNC
version: 20.15.2
object_name: FAULTUPBINDGRP
object_kind: binding
applicable_nf:
- SGW-C
- SMF
status: active
---

# FAULTUPBINDGRP（N3接口故障UPF与UPF组的绑定关系）

## 说明

**适用NF：SGW-C、SMF**

该命令用于添加N3接口故障UPF与故障UPF组的绑定关系，当N3接口出现故障，如果故障UPF与UPF组绑定，SMF在为通过与UPF组绑定的故障RAN组内的RAN接入的用户选择UPF时，会自动过滤掉该故障UPF。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-FAULTUPBINDGRP]] · ADD FAULTUPBINDGRP
- [[command/UNC/20.15.2/LST-FAULTUPBINDGRP]] · LST FAULTUPBINDGRP
- [[command/UNC/20.15.2/RMV-FAULTUPBINDGRP]] · RMV FAULTUPBINDGRP

## 证据

- 原始手册：`evidence/UNC/20.15.2/FAULTUPBINDGRP.md`
- 原始手册：`evidence/UNC/20.15.2/FAULTUPBINDGRP.md`
- 原始手册：`evidence/UNC/20.15.2/FAULTUPBINDGRP.md`
