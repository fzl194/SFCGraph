---
id: UNC@20.15.2@ConfigObject@NGUSRGRP
type: ConfigObject
name: NGUSRGRP（5G用户群）
nf: UNC
version: 20.15.2
object_name: NGUSRGRP
object_kind: entity
applicable_nf:
- AMF
status: active
---

# NGUSRGRP（5G用户群）

## 说明

**适用NF：AMF**

此命令用于增加5G用户群记录，同一个用户群中的用户具有相同的策略。

当将需要采用相同策略的不同的IMSI号段用户进行划分，作为一个用户群统一进行控制时，需要执行此命令。

群组内的用户标识列表通过ADD NGUSRGRPMEM进行添加。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NGUSRGRP]] · ADD NGUSRGRP
- [[command/UNC/20.15.2/LST-NGUSRGRP]] · LST NGUSRGRP
- [[command/UNC/20.15.2/MOD-NGUSRGRP]] · MOD NGUSRGRP
- [[command/UNC/20.15.2/RMV-NGUSRGRP]] · RMV NGUSRGRP

## 证据

- 原始手册：`evidence/UNC/20.15.2/NGUSRGRP.md`
- 原始手册：`evidence/UNC/20.15.2/NGUSRGRP.md`
- 原始手册：`evidence/UNC/20.15.2/NGUSRGRP.md`
- 原始手册：`evidence/UNC/20.15.2/NGUSRGRP.md`
