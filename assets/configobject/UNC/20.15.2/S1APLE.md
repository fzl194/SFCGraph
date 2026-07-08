---
id: UNC@20.15.2@ConfigObject@S1APLE
type: ConfigObject
name: S1APLE（S1AP本地实体）
nf: UNC
version: 20.15.2
object_name: S1APLE
object_kind: entity
applicable_nf:
- MME
status: active
---

# S1APLE（S1AP本地实体）

## 说明

**适用网元：MME**

此命令用于增加S1AP链路本地实体。

此命令为S1口基本配置，在MME与eNodeB对接的时候必须配置。配置完S1AP本地实体后，需要eNodeB主动发起建链流程才能完成S1链路的建立。

## 操作本对象的命令

- [ADD S1APLE](command/UNC/20.15.2/ADD-S1APLE.md)
- [LST S1APLE](command/UNC/20.15.2/LST-S1APLE.md)
- [MOD S1APLE](command/UNC/20.15.2/MOD-S1APLE.md)
- [RMV S1APLE](command/UNC/20.15.2/RMV-S1APLE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改S1AP本地实体(MOD-S1APLE)_72225933.md`
- 原始手册：`evidence/UNC/20.15.2/删除S1AP本地实体(RMV-S1APLE)_26306066.md`
- 原始手册：`evidence/UNC/20.15.2/增加S1AP本地实体(ADD-S1APLE)_26146254.md`
- 原始手册：`evidence/UNC/20.15.2/查询S1AP本地实体(LST-S1APLE)_72345855.md`
