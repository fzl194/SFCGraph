---
id: UNC@20.15.2@ConfigObject@PODMIGRATE
type: ConfigObject
name: PODMIGRATE（操作节点扩缩容与Pod迁移任务）
nf: UNC
version: 20.15.2
object_name: PODMIGRATE
object_kind: action
status: active
---

# PODMIGRATE（操作节点扩缩容与Pod迁移任务）

## 说明

该命令用于PBU-A等控制类服务所在节点扩缩容或OMU等运维类服务所在节点扩缩容，扩缩容过程中会进行Pod迁移。该命令主要用于现网需要从小规格部署形态向大规格部署形态变化的扩容场景。如果扩容时失败，把缩容回退作为逃生手段。

## 操作本对象的命令

- [OPR PODMIGRATE](command/UNC/20.15.2/OPR-PODMIGRATE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/操作节点扩缩容与Pod迁移任务（OPR-PODMIGRATE）_42938091.md`
