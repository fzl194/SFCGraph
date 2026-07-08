---
id: UNC@20.15.2@ConfigObject@PGWRNSI
type: ConfigObject
name: PGWRNSI（PGW重定向配置）
nf: UNC
version: 20.15.2
object_name: PGWRNSI
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# PGWRNSI（PGW重定向配置）

## 说明

**适用网元：SGSN、MME**

该命令用于MME在选择网关时开启PGW重定向功能，当用户在4G切换到5G场景下，需要保证业务连续性时开启该功能。

## 操作本对象的命令

- [ADD PGWRNSI](command/UNC/20.15.2/ADD-PGWRNSI.md)
- [LST PGWRNSI](command/UNC/20.15.2/LST-PGWRNSI.md)
- [MOD PGWRNSI](command/UNC/20.15.2/MOD-PGWRNSI.md)
- [RMV PGWRNSI](command/UNC/20.15.2/RMV-PGWRNSI.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改PGW重定向配置(MOD-PGWRNSI)_66890937.md`
- 原始手册：`evidence/UNC/20.15.2/删除PGW重定向配置(RMV-PGWRNSI)_66930905.md`
- 原始手册：`evidence/UNC/20.15.2/增加PGW重定向配置(ADD-PGWRNSI)_18730832.md`
- 原始手册：`evidence/UNC/20.15.2/查询PGW重定向配置(LST-PGWRNSI)_18410968.md`
