---
id: UNC@20.15.2@ConfigObject@UEDNSBINDUPGRP
type: ConfigObject
name: UEDNSBINDUPGRP（UPF组的DNS属性）
nf: UNC
version: 20.15.2
object_name: UEDNSBINDUPGRP
object_kind: binding
applicable_nf:
- GGSN
- PGW-C
- SMF
status: active
---

# UEDNSBINDUPGRP（UPF组的DNS属性）

## 说明

**适用NF：GGSN、PGW-C、SMF**

该命令用来配置指定UPF组的DNS属性和DNS64属性。用户需要配置UPF组下的主、备DNS地址或者主、备DNS64地址时，使用该命令。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-UEDNSBINDUPGRP]] · ADD UEDNSBINDUPGRP
- [[command/UNC/20.15.2/LST-UEDNSBINDUPGRP]] · LST UEDNSBINDUPGRP
- [[command/UNC/20.15.2/MOD-UEDNSBINDUPGRP]] · MOD UEDNSBINDUPGRP
- [[command/UNC/20.15.2/RMV-UEDNSBINDUPGRP]] · RMV UEDNSBINDUPGRP

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改UPF组的DNS属性（MOD-UEDNSBINDUPGRP）_73321241.md`
- 原始手册：`evidence/UNC/20.15.2/删除UPF组的DNS属性（RMV-UEDNSBINDUPGRP）_73321246.md`
- 原始手册：`evidence/UNC/20.15.2/增加UPF组的DNS属性（ADD-UEDNSBINDUPGRP）_73321229.md`
- 原始手册：`evidence/UNC/20.15.2/查询UPF组的DNS属性（LST-UEDNSBINDUPGRP）_73321237.md`
