---
id: UNC@20.15.2@ConfigObject@FASTRECOVERY
type: ConfigObject
name: FASTRECOVERY（全局业务快速恢复配置）
nf: UNC
version: 20.15.2
object_name: FASTRECOVERY
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
status: active
---

# FASTRECOVERY（全局业务快速恢复配置）

## 说明

**适用NF：SGW-C、PGW-C**

该命令主要用于配置快速恢复功能。如果配置成功，当网络侧、MME、SGW发生故障或重启时可以快速恢复业务。

## 操作本对象的命令

- [LST FASTRECOVERY](command/UNC/20.15.2/LST-FASTRECOVERY.md)
- [SET FASTRECOVERY](command/UNC/20.15.2/SET-FASTRECOVERY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局业务快速恢复配置（LST-FASTRECOVERY）_31453514.md`
- 原始手册：`evidence/UNC/20.15.2/设置全局业务快速恢复配置（SET-FASTRECOVERY）_31453525.md`
