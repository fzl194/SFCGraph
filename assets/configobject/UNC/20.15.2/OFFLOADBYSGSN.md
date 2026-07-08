---
id: UNC@20.15.2@ConfigObject@OFFLOADBYSGSN
type: ConfigObject
name: OFFLOADBYSGSN（SGSN迁移任务）
nf: UNC
version: 20.15.2
object_name: OFFLOADBYSGSN
object_kind: action
applicable_nf:
- SGSN
status: active
---

# OFFLOADBYSGSN（SGSN迁移任务）

## 说明

**适用网元：SGSN**

此命令用于启动SGSN迁移任务：

1. 启动以SGSN为单位的迁移任务，如指定目的SGSN则将本SGSN上的用户按设定的迁入百分比迁移到各个目的SGSN中。
2. 未指定目的SGSN则由RAN侧选择目的SGSN。

## 操作本对象的命令

- [[command/UNC/20.15.2/STR-OFFLOADBYSGSN]] · STR OFFLOADBYSGSN

## 证据

- 原始手册：`evidence/UNC/20.15.2/OFFLOADBYSGSN.md`
