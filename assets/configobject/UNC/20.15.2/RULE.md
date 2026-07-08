---
id: UNC@20.15.2@ConfigObject@RULE
type: ConfigObject
name: RULE（规则）
nf: UNC
version: 20.15.2
object_name: RULE
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# RULE（规则）

## 说明

**适用NF：PGW-C、SMF**

该命令用于配置业务策略规则，也就是下文提到的Rule。具体包含规则名称、策略类型、以及全局优先级等。SMF通过信令流程从PCRF/PCF获取预定义规则后会和该命令配置的rule进行匹配，如果匹配上会给UPF下发对应的Rule名称。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-RULE]] · ADD RULE
- [[command/UNC/20.15.2/LST-RULE]] · LST RULE
- [[command/UNC/20.15.2/MOD-RULE]] · MOD RULE
- [[command/UNC/20.15.2/RMV-RULE]] · RMV RULE

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改规则（MOD-RULE）_09897202.md`
- 原始手册：`evidence/UNC/20.15.2/删除规则（RMV-RULE）_09897203.md`
- 原始手册：`evidence/UNC/20.15.2/增加规则（ADD-RULE）_09897200.md`
- 原始手册：`evidence/UNC/20.15.2/查询规则（LST-RULE）_09897204.md`
