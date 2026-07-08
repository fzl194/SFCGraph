---
id: UNC@20.15.2@ConfigObject@VLROFFLOADLAILST
type: ConfigObject
name: VLROFFLOADLAILST（位置区列表）
nf: UNC
version: 20.15.2
object_name: VLROFFLOADLAILST
object_kind: entity
applicable_nf:
- MME
status: active
---

# VLROFFLOADLAILST（位置区列表）

## 说明

**适用网元：MME**

本命令用于增加一个待处理的LAI，当执行 [**STR VLROFFLOADBYLAI**](../基于LAI的IMSI分离业务/启动IMSI分离4G用户任务(STR VLROFFLOADBYLAI)_26305240.md) 命令后，系统会对该LAI对应的TAI下面联合附着的4G用户执行IMSI分离操作。本命令可用于将BSC/RNC设备从一个MSC POOL下割接到另一个MSC POOL下时CSFB业务主动恢复场景。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-VLROFFLOADLAILST]] · ADD VLROFFLOADLAILST
- [[command/UNC/20.15.2/LST-VLROFFLOADLAILST]] · LST VLROFFLOADLAILST
- [[command/UNC/20.15.2/RMV-VLROFFLOADLAILST]] · RMV VLROFFLOADLAILST

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除位置区列表(RMV-VLROFFLOADLAILST)_72345029.md`
- 原始手册：`evidence/UNC/20.15.2/增加位置区列表(ADD-VLROFFLOADLAILST)_26305242.md`
- 原始手册：`evidence/UNC/20.15.2/查询位置区列表(LST-VLROFFLOADLAILST)_26145428.md`
