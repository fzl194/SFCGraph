---
id: UNC@20.15.2@ConfigObject@APNALIAS
type: ConfigObject
name: APNALIAS（APN别名配置）
nf: UNC
version: 20.15.2
object_name: APNALIAS
object_kind: entity
applicable_nf:
- PGW-C
- SMF
- GGSN
status: active
---

# APNALIAS（APN别名配置）

## 说明

**适用NF：PGW-C、SMF、GGSN**

该命令用于增加别名APN配置。为了兼容多个APN使用完全相同资源的情况，使用该命令配置APN的转换关系，在用户激活时，将用户请求的APN（称为别名APN）转换为新的APN（称为转换APN）。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-APNALIAS]] · ADD APNALIAS
- [[command/UNC/20.15.2/LCK-APNALIAS]] · LCK APNALIAS
- [[command/UNC/20.15.2/LST-APNALIAS]] · LST APNALIAS
- [[command/UNC/20.15.2/RMV-APNALIAS]] · RMV APNALIAS

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除APN别名配置（RMV-APNALIAS）_28567655.md`
- 原始手册：`evidence/UNC/20.15.2/增加APN别名配置（ADD-APNALIAS）_28567622.md`
- 原始手册：`evidence/UNC/20.15.2/查询APN别名配置（LST-APNALIAS）_28567626.md`
- 原始手册：`evidence/UNC/20.15.2/锁定APN别名配置（LCK-APNALIAS）_28567625.md`
