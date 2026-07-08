---
id: UNC@20.15.2@ConfigObject@FAULTRANGRP
type: ConfigObject
name: FAULTRANGRP（N3接口故障RAN组）
nf: UNC
version: 20.15.2
object_name: FAULTRANGRP
object_kind: entity
applicable_nf:
- SGW-C
- SMF
status: active
---

# FAULTRANGRP（N3接口故障RAN组）

## 说明

**适用NF：SGW-C、SMF**

该命令用于添加N3接口故障RAN组，当N3接口出现故障，SMF在为通过该RAN组内的RAN接入的用户选择UPF时，会自动过滤掉与该RAN组绑定的UPF组内的UPF。

## 操作本对象的命令

- [ADD FAULTRANGRP](command/UNC/20.15.2/ADD-FAULTRANGRP.md)
- [LST FAULTRANGRP](command/UNC/20.15.2/LST-FAULTRANGRP.md)
- [MOD FAULTRANGRP](command/UNC/20.15.2/MOD-FAULTRANGRP.md)
- [RMV FAULTRANGRP](command/UNC/20.15.2/RMV-FAULTRANGRP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改N3接口故障RAN组（MOD-FAULTRANGRP）_52628648.md`
- 原始手册：`evidence/UNC/20.15.2/删除N3接口故障RAN组（RMV-FAULTRANGRP）_38182771.md`
- 原始手册：`evidence/UNC/20.15.2/增加N3接口故障RAN组（ADD-FAULTRANGRP）_38102753.md`
- 原始手册：`evidence/UNC/20.15.2/查询N3接口故障RAN组（LST-FAULTRANGRP）_93382802.md`
