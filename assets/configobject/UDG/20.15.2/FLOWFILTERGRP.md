---
id: UDG@20.15.2@ConfigObject@FLOWFILTERGRP
type: ConfigObject
name: FLOWFILTERGRP（流过滤器组）
nf: UDG
version: 20.15.2
object_name: FLOWFILTERGRP
object_kind: entity
applicable_nf:
- PGW-U
- UPF
uniqueness_keys:
- - FLWFLTRGRPNAME
  - FLOWFILTERNAME
status: active
---

# FLOWFILTERGRP（流过滤器组）

## 说明

**适用NF：PGW-U、UPF**

该命令用于配置流过滤器组。当用户需要多个流过滤条件同时存在时，可以配置流过滤器组。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-FLOWFILTERGRP]] · ADD FLOWFILTERGRP
- [[command/UDG/20.15.2/LST-FLOWFILTERGRP]] · LST FLOWFILTERGRP
- [[command/UDG/20.15.2/RMV-FLOWFILTERGRP]] · RMV FLOWFILTERGRP

## 关联对象

- [[configobject/UDG/20.15.2/BLACKLISTRULE]] · BLACKLISTRULE
- [[configobject/UDG/20.15.2/RULE]] · RULE

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除流过滤器组（RMV-FLOWFILTERGRP）_82837385.md`
- 原始手册：`evidence/UDG/20.15.2/增加流过滤器组（ADD-FLOWFILTERGRP）_82837384.md`
- 原始手册：`evidence/UDG/20.15.2/查询流过滤器组（LST-FLOWFILTERGRP）_86528844.md`
