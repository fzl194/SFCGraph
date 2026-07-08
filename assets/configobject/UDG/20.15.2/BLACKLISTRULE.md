---
id: UDG@20.15.2@ConfigObject@BLACKLISTRULE
type: ConfigObject
name: BLACKLISTRULE（黑名单规则）
nf: UDG
version: 20.15.2
object_name: BLACKLISTRULE
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# BLACKLISTRULE（黑名单规则）

## 说明

**适用NF：PGW-U、UPF**

此命令用于在配置业务策略的时候增加指定策略类型的黑名单规则，用于实现相应策略类型的黑名单规则。通过的报文经过流过滤器或流过滤器组的匹配基于优先级选择相应策略类型中优先级最高的规则，命中黑名单规则的业务流无需执行相应策略类型的策略。

## 操作本对象的命令

- [ADD BLACKLISTRULE](command/UDG/20.15.2/ADD-BLACKLISTRULE.md)

## 关联对象

- [FLOWFILTER](configobject/UDG/20.15.2/FLOWFILTER.md)
- [FLOWFILTERGRP](configobject/UDG/20.15.2/FLOWFILTERGRP.md)
- [TIMERANGE](configobject/UDG/20.15.2/TIMERANGE.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加黑名单规则（ADD-BLACKLISTRULE）_82837267.md`
