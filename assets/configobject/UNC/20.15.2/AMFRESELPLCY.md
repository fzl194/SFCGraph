---
id: UNC@20.15.2@ConfigObject@AMFRESELPLCY
type: ConfigObject
name: AMFRESELPLCY（AMF重选控制策略）
nf: UNC
version: 20.15.2
object_name: AMFRESELPLCY
object_kind: entity
applicable_nf:
- AMF
status: active
---

# AMFRESELPLCY（AMF重选控制策略）

## 说明

**适用NF：AMF**

该命令用于增加AMF重选功能控制策略。AMF可基于用户的号段，控制在用户新接入AMF时，是否需要将用户通过重定向方式重选至指定的AMF。

在特性新开通等场景，只在特定AMF试开通，Pool内其他AMF可通过本命令将指定的开通用户重选到特性AMF上。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-AMFRESELPLCY]] · ADD AMFRESELPLCY
- [[command/UNC/20.15.2/LST-AMFRESELPLCY]] · LST AMFRESELPLCY
- [[command/UNC/20.15.2/MOD-AMFRESELPLCY]] · MOD AMFRESELPLCY
- [[command/UNC/20.15.2/RMV-AMFRESELPLCY]] · RMV AMFRESELPLCY

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改AMF重选控制策略（MOD-AMFRESELPLCY）_98333332.md`
- 原始手册：`evidence/UNC/20.15.2/删除AMF重选控制策略（RMV-AMFRESELPLCY）_98493196.md`
- 原始手册：`evidence/UNC/20.15.2/增加AMF重选控制策略（ADD-AMFRESELPLCY）_98333328.md`
- 原始手册：`evidence/UNC/20.15.2/查询AMF重选控制策略（LST-AMFRESELPLCY）_38212805.md`
