---
id: UNC@20.15.2@ConfigObject@CPFLOWFILTER
type: ConfigObject
name: CPFLOWFILTER（CP流过滤器）
nf: UNC
version: 20.15.2
object_name: CPFLOWFILTER
object_kind: entity
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
status: active
---

# CPFLOWFILTER（CP流过滤器）

## 说明

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于增加SMF和UPF之间的消息流过滤器。比如IPv6 ND消息。

## 操作本对象的命令

- [ADD CPFLOWFILTER](command/UNC/20.15.2/ADD-CPFLOWFILTER.md)
- [LST CPFLOWFILTER](command/UNC/20.15.2/LST-CPFLOWFILTER.md)
- [RMV CPFLOWFILTER](command/UNC/20.15.2/RMV-CPFLOWFILTER.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除CP流过滤器（RMV-CPFLOWFILTER）_96805497.md`
- 原始手册：`evidence/UNC/20.15.2/增加CP流过滤器（ADD-CPFLOWFILTER）_96805375.md`
- 原始手册：`evidence/UNC/20.15.2/查询CP流过滤器（LST-CPFLOWFILTER）_96805383.md`
