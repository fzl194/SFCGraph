---
id: UNC@20.15.2@ConfigObject@EPLMNGRP
type: ConfigObject
name: EPLMNGRP（等价PLMN组）
nf: UNC
version: 20.15.2
object_name: EPLMNGRP
object_kind: entity
applicable_nf:
- AMF
status: active
---

# EPLMNGRP（等价PLMN组）

## 说明

**适用NF：AMF**

该命令用于增加等价PLMN（Equivalent PLMN）组。在同一组内的PLMN互为等价PLMN。等价PLMN也叫对等PLMN，是指与UE当前选择的PLMN（即Registered PLMN，RPLMN）享有同等地位的PLMN。在PLMN选择过程中，RPLMN及其等价PLMN将被高优先选择。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-EPLMNGRP]] · ADD EPLMNGRP
- [[command/UNC/20.15.2/LST-EPLMNGRP]] · LST EPLMNGRP
- [[command/UNC/20.15.2/MOD-EPLMNGRP]] · MOD EPLMNGRP
- [[command/UNC/20.15.2/RMV-EPLMNGRP]] · RMV EPLMNGRP

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改等价PLMN组（MOD-EPLMNGRP）_09651849.md`
- 原始手册：`evidence/UNC/20.15.2/删除等价PLMN组（RMV-EPLMNGRP）_09651360.md`
- 原始手册：`evidence/UNC/20.15.2/增加等价PLMN组（ADD-EPLMNGRP）_09653623.md`
- 原始手册：`evidence/UNC/20.15.2/查询等价PLMN组（LST-EPLMNGRP）_09651354.md`
