---
id: UNC@20.15.2@ConfigObject@APNNIGROUP
type: ConfigObject
name: APNNIGROUP（APNNI组）
nf: UNC
version: 20.15.2
object_name: APNNIGROUP
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# APNNIGROUP（APNNI组）

## 说明

**适用网元：SGSN、MME**

该命令用于增加APNNI组信息。关联了该组的APNNI可以被基于延迟定时器的信令拥塞控制特性和Non-IP数据传输特性使用。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-APNNIGROUP]] · ADD APNNIGROUP
- [[command/UNC/20.15.2/LST-APNNIGROUP]] · LST APNNIGROUP
- [[command/UNC/20.15.2/RMV-APNNIGROUP]] · RMV APNNIGROUP

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除APNNI组(RMV-APNNIGROUP)_72345295.md`
- 原始手册：`evidence/UNC/20.15.2/增加APNNI组(ADD-APNNIGROUP)_26305508.md`
- 原始手册：`evidence/UNC/20.15.2/查询APNNI组(LST-APNNIGROUP)_26145700.md`
