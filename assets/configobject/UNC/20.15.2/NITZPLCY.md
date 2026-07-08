---
id: UNC@20.15.2@ConfigObject@NITZPLCY
type: ConfigObject
name: NITZPLCY（NITZ策略）
nf: UNC
version: 20.15.2
object_name: NITZPLCY
object_kind: entity
applicable_nf:
- AMF
status: active
---

# NITZPLCY（NITZ策略）

## 说明

**适用NF：AMF**

该命令用于为指定区域和指定用户群配置NITZ（Network Identity and Time Zone）策略。所谓NITZ策略是指AMF根据配置向UE下发系统时间、本地时区、夏令时及网络标识等信息。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NITZPLCY]] · ADD NITZPLCY
- [[command/UNC/20.15.2/LST-NITZPLCY]] · LST NITZPLCY
- [[command/UNC/20.15.2/MOD-NITZPLCY]] · MOD NITZPLCY
- [[command/UNC/20.15.2/RMV-NITZPLCY]] · RMV NITZPLCY

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改NITZ策略（MOD-NITZPLCY）_09653096.md`
- 原始手册：`evidence/UNC/20.15.2/删除NITZ策略（RMV-NITZPLCY）_09652658.md`
- 原始手册：`evidence/UNC/20.15.2/增加NITZ策略（ADD-NITZPLCY）_09652255.md`
- 原始手册：`evidence/UNC/20.15.2/查询NITZ策略（LST-NITZPLCY）_09653785.md`
