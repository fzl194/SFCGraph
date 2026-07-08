---
id: UNC@20.15.2@ConfigObject@APNNILIB
type: ConfigObject
name: APNNILIB（APNNI库记录）
nf: UNC
version: 20.15.2
object_name: APNNILIB
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# APNNILIB（APNNI库记录）

## 说明

**适用网元：SGSN**

此命令用于增加APNNI库记录。APNNI库是用户请求的APNNI或签约数据中的APNNI和终端类型的对应关系表，用于通过用户请求的APNNI或签约数据中的APNNI识别智能终端类型。

当需要增加一条APNNI和终端类型的对应记录时，需要执行此命令。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-APNNILIB]] · ADD APNNILIB
- [[command/UNC/20.15.2/LST-APNNILIB]] · LST APNNILIB
- [[command/UNC/20.15.2/RMV-APNNILIB]] · RMV APNNILIB

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除APNNI库记录（RMV-APNNILIB）_72225415.md`
- 原始手册：`evidence/UNC/20.15.2/增加APNNI库记录（ADD-APNNILIB）_26145736.md`
- 原始手册：`evidence/UNC/20.15.2/查询APNNI库记录（LST-APNNILIB）_26305546.md`
