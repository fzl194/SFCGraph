---
id: UNC@20.15.2@ConfigObject@PGWGROUP
type: ConfigObject
name: PGWGROUP（P-GW组）
nf: UNC
version: 20.15.2
object_name: PGWGROUP
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# PGWGROUP（P-GW组）

## 说明

**适用网元：SGSN、MME**

该命令用于增加P-GW组。使用P-GW组是更精细化的管理P-GW局向。MME支持基于P-GW Back-off timer的APN级流控功能会使用到本命令。

## 操作本对象的命令

- [ADD PGWGROUP](command/UNC/20.15.2/ADD-PGWGROUP.md)
- [LST PGWGROUP](command/UNC/20.15.2/LST-PGWGROUP.md)
- [RMV PGWGROUP](command/UNC/20.15.2/RMV-PGWGROUP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除P-GW组(RMV-PGWGROUP)_26305516.md`
- 原始手册：`evidence/UNC/20.15.2/增加P-GW组(ADD-PGWGROUP)_72225385.md`
- 原始手册：`evidence/UNC/20.15.2/查询P-GW组(LST-PGWGROUP)_72345303.md`
