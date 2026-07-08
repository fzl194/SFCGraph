---
id: UNC@20.15.2@ConfigObject@PGWNODE
type: ConfigObject
name: PGWNODE（P-GW局向）
nf: UNC
version: 20.15.2
object_name: PGWNODE
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# PGWNODE（P-GW局向）

## 说明

**适用网元：SGSN、MME**

该命令用于增加P-GW局向。配置PGW Node Name后缀的列表，只有在列表中的才能开启MME支持基于P-GW Back-off timer的APN级流控功能。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PGWNODE]] · ADD PGWNODE
- [[command/UNC/20.15.2/LST-PGWNODE]] · LST PGWNODE
- [[command/UNC/20.15.2/RMV-PGWNODE]] · RMV PGWNODE

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除P-GW局向(RMV-PGWNODE)_26305518.md`
- 原始手册：`evidence/UNC/20.15.2/增加P-GW局向(ADD-PGWNODE)_72225387.md`
- 原始手册：`evidence/UNC/20.15.2/查询P-GW局向(LST-PGWNODE)_72345305.md`
