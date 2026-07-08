---
id: UNC@20.15.2@ConfigObject@PGWBACKOFF
type: ConfigObject
name: PGWBACKOFF（P-GW Back-off流控参数）
nf: UNC
version: 20.15.2
object_name: PGWBACKOFF
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# PGWBACKOFF（P-GW Back-off流控参数）

## 说明

**适用网元：MME**

该命令用于设置P-GW Back-off流控功能的相关参数。MME支持基于P-GW Back-off timer的APN级流控功能会使用到本命令。

## 操作本对象的命令

- [LST PGWBACKOFF](command/UNC/20.15.2/LST-PGWBACKOFF.md)
- [SET PGWBACKOFF](command/UNC/20.15.2/SET-PGWBACKOFF.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询P-GW-Back-off流控参数(LST-PGWBACKOFF)_26146162.md`
- 原始手册：`evidence/UNC/20.15.2/设置P-GW-Back-off流控参数(SET-PGWBACKOFF)_72345761.md`
