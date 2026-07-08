---
id: UNC@20.15.2@ConfigObject@S1PAGINGRULE
type: ConfigObject
name: S1PAGINGRULE（S1寻呼规则）
nf: UNC
version: 20.15.2
object_name: S1PAGINGRULE
object_kind: entity
applicable_nf:
- MME
status: active
---

# S1PAGINGRULE（S1寻呼规则）

## 说明

**适用网元：MME**

此命令用于增加S1寻呼规则。根据规划针对网络部署WSFD- 206001 LTE精准寻呼功能时，通过此命令配置LTE精准寻呼的规则集，比如指定使用LTE精准寻呼的用户群、业务类型、使用的寻呼动作组合等。通过部署LTE精准寻呼，缩小寻呼范围，减少eNodeB的寻呼负荷，节省网络资源。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-S1PAGINGRULE]] · ADD S1PAGINGRULE
- [[command/UNC/20.15.2/LST-S1PAGINGRULE]] · LST S1PAGINGRULE
- [[command/UNC/20.15.2/MOD-S1PAGINGRULE]] · MOD S1PAGINGRULE
- [[command/UNC/20.15.2/RMV-S1PAGINGRULE]] · RMV S1PAGINGRULE

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改S1寻呼规则(MOD-S1PAGINGRULE)_26146248.md`
- 原始手册：`evidence/UNC/20.15.2/删除S1寻呼规则(RMV-S1PAGINGRULE)_72345847.md`
- 原始手册：`evidence/UNC/20.15.2/增加S1寻呼规则(ADD-S1PAGINGRULE)_26306058.md`
- 原始手册：`evidence/UNC/20.15.2/查询S1寻呼规则(LST-S1PAGINGRULE)_72225927.md`
