---
id: UDG@20.15.2@ConfigObject@RULE
type: ConfigObject
name: RULE（规则）
nf: UDG
version: 20.15.2
object_name: RULE
object_kind: entity
applicable_nf:
- PGW-U
- UPF
uniqueness_keys:
- - RULENAME
  - POLICYTYPE
status: active
---

# RULE（规则）

## 说明

**适用NF：PGW-U、UPF**

该命令用于在配置业务策略的时候增加规则，其中包含策略类型、流过滤器、流过滤器组、策略信息、生效时间段以及优先级等。通过运营商的报文匹配流过滤器获取相应规则的策略信息。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-RULE]] · ADD RULE
- [[command/UDG/20.15.2/LST-RULE]] · LST RULE
- [[command/UDG/20.15.2/MOD-RULE]] · MOD RULE
- [[command/UDG/20.15.2/RMV-RULE]] · RMV RULE

## 关联对象

- [[configobject/UDG/20.15.2/FLOWFILTER]] · FLOWFILTER
- [[configobject/UDG/20.15.2/FLOWFILTERGRP]] · FLOWFILTERGRP
- [[configobject/UDG/20.15.2/TIMERANGE]] · TIMERANGE

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改规则（MOD-RULE）_82837268.md`
- 原始手册：`evidence/UDG/20.15.2/删除规则（RMV-RULE）_82837269.md`
- 原始手册：`evidence/UDG/20.15.2/增加规则（ADD-RULE）_82837266.md`
- 原始手册：`evidence/UDG/20.15.2/查询规则（LST-RULE）_82837270.md`
