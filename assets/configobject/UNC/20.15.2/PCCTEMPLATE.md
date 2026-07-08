---
id: UNC@20.15.2@ConfigObject@PCCTEMPLATE
type: ConfigObject
name: PCCTEMPLATE（PCC模板）
nf: UNC
version: 20.15.2
object_name: PCCTEMPLATE
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# PCCTEMPLATE（PCC模板）

## 说明

**适用NF：PGW-C、SMF**

该命令用于增加一个PCC模板配置。

当部署PCC业务时，希望不同的APN有不同的PCC配置，则可以通过该命令配置不同的PCC模板，以便于绑定到APN下，使得不同的APN可以有不同的PCC配置属性。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PCCTEMPLATE]] · ADD PCCTEMPLATE
- [[command/UNC/20.15.2/LST-PCCTEMPLATE]] · LST PCCTEMPLATE
- [[command/UNC/20.15.2/MOD-PCCTEMPLATE]] · MOD PCCTEMPLATE
- [[command/UNC/20.15.2/RMV-PCCTEMPLATE]] · RMV PCCTEMPLATE

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改PCC模板（MOD-PCCTEMPLATE）_09897065.md`
- 原始手册：`evidence/UNC/20.15.2/删除PCC模板（RMV-PCCTEMPLATE）_09897066.md`
- 原始手册：`evidence/UNC/20.15.2/增加PCC模板（ADD-PCCTEMPLATE）_09897064.md`
- 原始手册：`evidence/UNC/20.15.2/查询PCC模板（LST-PCCTEMPLATE）_09897067.md`
