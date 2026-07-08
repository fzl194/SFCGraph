---
id: UNC@20.15.2@ConfigObject@GLBCGGROUP
type: ConfigObject
name: GLBCGGROUP（全局CG组）
nf: UNC
version: 20.15.2
object_name: GLBCGGROUP
object_kind: global_setting
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# GLBCGGROUP（全局CG组）

## 说明

**适用NF：SGW-C、PGW-C、SMF**

该命令用于设置全局CG组，UNC优先选择离线计费模板下绑定的CG组，当离线计费模板下没有绑定CG组或根据号段未匹配到CG组时，UNC选择全局配置的CG组。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-GLBCGGROUP]] · LST GLBCGGROUP
- [[command/UNC/20.15.2/SET-GLBCGGROUP]] · SET GLBCGGROUP

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局CG组（LST-GLBCGGROUP）_09896862.md`
- 原始手册：`evidence/UNC/20.15.2/设置全局CG组（SET-GLBCGGROUP）_09896861.md`
