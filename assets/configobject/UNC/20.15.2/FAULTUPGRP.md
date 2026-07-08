---
id: UNC@20.15.2@ConfigObject@FAULTUPGRP
type: ConfigObject
name: FAULTUPGRP（N3接口故障UPF组）
nf: UNC
version: 20.15.2
object_name: FAULTUPGRP
object_kind: entity
applicable_nf:
- SGW-C
- SMF
status: active
---

# FAULTUPGRP（N3接口故障UPF组）

## 说明

**适用NF：SGW-C、SMF**

该命令用于添加N3接口故障UPF组，当N3接口出现故障，如果该故障UPF组与故障RAN组绑定，SMF在为通过RAN组内的RAN接入的用户选择UPF时，会自动过滤掉该UPF组内的UPF。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-FAULTUPGRP]] · ADD FAULTUPGRP
- [[command/UNC/20.15.2/LST-FAULTUPGRP]] · LST FAULTUPGRP
- [[command/UNC/20.15.2/RMV-FAULTUPGRP]] · RMV FAULTUPGRP

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除N3接口故障UPF组（RMV-FAULTUPGRP）_38422729.md`
- 原始手册：`evidence/UNC/20.15.2/增加N3接口故障UPF组（ADD-FAULTUPGRP）_93702766.md`
- 原始手册：`evidence/UNC/20.15.2/查询N3接口故障UPF组（LST-FAULTUPGRP）_38102755.md`
