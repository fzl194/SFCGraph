---
id: UDG@20.15.2@ConfigObject@RULECHECK
type: ConfigObject
name: RULECHECK（规则检测结果）
nf: UDG
version: 20.15.2
object_name: RULECHECK
object_kind: query_target
applicable_nf:
- PGW-U
- UPF
status: active
---

# RULECHECK（规则检测结果）

## 说明

**适用NF：PGW-U、UPF**

该命令用于对指定规则或所有规则的IP版本一致性进行检查；查询名称相同策略类型不同的规则；当特征库升级发生了协议名称变更时，查询进行过自动配置转换的命令，或查询进行自动配置转换协议名称冲突的命令；确认接受自动配置转换结果，并消除告警。规则的IP版本一致性检查指的是规则下的过滤器或者过滤器组配置过的IP版本是否包含了策略组下配置过的IP版本；如果不包含，则算异常；包含则算正常。

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-RULECHECK]] · DSP RULECHECK

## 证据

- 原始手册：`evidence/UDG/20.15.2/RULECHECK.md`
