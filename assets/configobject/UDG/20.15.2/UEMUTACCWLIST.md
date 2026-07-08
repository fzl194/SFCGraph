---
id: UDG@20.15.2@ConfigObject@UEMUTACCWLIST
type: ConfigObject
name: UEMUTACCWLIST（PA口UE互访白名单）
nf: UDG
version: 20.15.2
object_name: UEMUTACCWLIST
object_kind: entity
applicable_nf:
- UPF
- PGW-U
status: active
---

# UEMUTACCWLIST（PA口UE互访白名单）

## 说明

**适用NF：UPF、PGW-U**

企业专用DNN漫游场景，增加PA口UE互访白名单。

该命令用于配置漫游场景下UE互访的I-UPF、SGW白名单，对于APNUEMUTACC命令下的InnerAPNS_S5S8P、InnerAPNS_N9A、InterAPNS_S5S8P、InterAPNS_N9A参数，需要开启后生效。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-UEMUTACCWLIST]] · ADD UEMUTACCWLIST
- [[command/UDG/20.15.2/LST-UEMUTACCWLIST]] · LST UEMUTACCWLIST
- [[command/UDG/20.15.2/RMV-UEMUTACCWLIST]] · RMV UEMUTACCWLIST

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除PA口UE互访白名单（RMV-UEMUTACCWLIST）_72322910.md`
- 原始手册：`evidence/UDG/20.15.2/增加PA口UE互访白名单（ADD-UEMUTACCWLIST）_31719863.md`
- 原始手册：`evidence/UDG/20.15.2/查询PA口UE互访白名单（LST-UEMUTACCWLIST）_72561940.md`
