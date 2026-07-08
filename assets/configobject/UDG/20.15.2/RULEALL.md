---
id: UDG@20.15.2@ConfigObject@RULEALL
type: ConfigObject
name: RULEALL（所有规则）
nf: UDG
version: 20.15.2
object_name: RULEALL
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# RULEALL（所有规则）

## 说明

**适用NF：PGW-U、UPF**

![](删除所有规则（RMV RULEALL）_06014580.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，会删除规则下所有绑定关系，并且会导致正在使用此规则的用户出现规则匹配错误、计费错误等现象。

该命令用于删除所有规则。

## 操作本对象的命令

- [[command/UDG/20.15.2/RMV-RULEALL]] · RMV RULEALL

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除所有规则（RMV-RULEALL）_06014580.md`
