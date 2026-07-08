---
id: UNC@20.15.2@ConfigObject@EXEMPTSERVICE
type: ConfigObject
name: EXEMPTSERVICE（豁免业务）
nf: UNC
version: 20.15.2
object_name: EXEMPTSERVICE
object_kind: entity
applicable_nf:
- PGW-C
- SMF
- GGSN
status: active
---

# EXEMPTSERVICE（豁免业务）

## 说明

**适用NF：PGW-C、SMF、GGSN**

该命令用于增加豁免业务。豁免业务（3GPP PS data off Exempt Services）不受3GPP PS data off能力控制，即使3GPP PS data off能力使能，这类业务也不受影响。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-EXEMPTSERVICE]] · ADD EXEMPTSERVICE
- [[command/UNC/20.15.2/LST-EXEMPTSERVICE]] · LST EXEMPTSERVICE
- [[command/UNC/20.15.2/RMV-EXEMPTSERVICE]] · RMV EXEMPTSERVICE

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除豁免业务（RMV-EXEMPTSERVICE）_35439600.md`
- 原始手册：`evidence/UNC/20.15.2/增加豁免业务（ADD-EXEMPTSERVICE）_81558909.md`
- 原始手册：`evidence/UNC/20.15.2/查询豁免业务（LST-EXEMPTSERVICE）_81398991.md`
