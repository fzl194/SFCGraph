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

- [[command/UNC/20.15.2/ADD-FAULTRANGRP]] · ADD FAULTRANGRP
- [[command/UNC/20.15.2/LST-FAULTRANGRP]] · LST FAULTRANGRP
- [[command/UNC/20.15.2/MOD-FAULTRANGRP]] · MOD FAULTRANGRP
- [[command/UNC/20.15.2/RMV-FAULTRANGRP]] · RMV FAULTRANGRP

## 证据

- 原始手册：`evidence/UNC/20.15.2/FAULTRANGRP.md`
- 原始手册：`evidence/UNC/20.15.2/FAULTRANGRP.md`
- 原始手册：`evidence/UNC/20.15.2/FAULTRANGRP.md`
- 原始手册：`evidence/UNC/20.15.2/FAULTRANGRP.md`
