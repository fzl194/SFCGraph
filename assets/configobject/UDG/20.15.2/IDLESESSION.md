---
id: UDG@20.15.2@ConfigObject@IDLESESSION
type: ConfigObject
name: IDLESESSION（空闲会话）
nf: UDG
version: 20.15.2
object_name: IDLESESSION
object_kind: action
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# IDLESESSION（空闲会话）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

![](去激活空闲会话（DEA IDLESESSION）_77631308.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，若不指定APNTYPE或CPNODEIDTYPE，将去活所有空闲会话。

该命令用于去激活系统的空闲会话。当会话空闲时长超过了指定的空闲时长阈值，需要手动去激活空闲会话时，使用该命令。可以基于APNTYPE或者CPNODEIDTYPE去激活。

## 操作本对象的命令

- [[command/UDG/20.15.2/DEA-IDLESESSION]] · DEA IDLESESSION

## 证据

- 原始手册：`evidence/UDG/20.15.2/IDLESESSION.md`
