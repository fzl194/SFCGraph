---
id: UDG@20.15.2@ConfigObject@AFPOLICYALL
type: ConfigObject
name: AFPOLICYALL（所有防欺诈策略配置）
nf: UDG
version: 20.15.2
object_name: AFPOLICYALL
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# AFPOLICYALL（所有防欺诈策略配置）

## 说明

**适用NF：PGW-U、UPF**

![](删除所有防欺诈策略配置（RMV AFPOLICYALL）_08772495.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除所有的防欺诈配置后，功能可能不正常，不要一次性删除所有的防欺诈配置。

该命令用于删除所有判断出欺诈行为后的处理策略。

## 操作本对象的命令

- [[command/UDG/20.15.2/RMV-AFPOLICYALL]] · RMV AFPOLICYALL

## 证据

- 原始手册：`evidence/UDG/20.15.2/AFPOLICYALL.md`
