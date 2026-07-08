---
id: UNC@20.15.2@ConfigObject@APNACCESSWAL
type: ConfigObject
name: APNACCESSWAL（APN接入速率）
nf: UNC
version: 20.15.2
object_name: APNACCESSWAL
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
status: active
---

# APNACCESSWAL（APN接入速率）

## 说明

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于配置基于APN的用户接入速率，保证APN下的用户平稳接入，不会因为此APN下的接入速率过快冲击网元或者影响其他APN的接入速率。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-APNACCESSWAL]] · LST APNACCESSWAL
- [[command/UNC/20.15.2/SET-APNACCESSWAL]] · SET APNACCESSWAL

## 证据

- 原始手册：`evidence/UNC/20.15.2/APNACCESSWAL.md`
- 原始手册：`evidence/UNC/20.15.2/APNACCESSWAL.md`
