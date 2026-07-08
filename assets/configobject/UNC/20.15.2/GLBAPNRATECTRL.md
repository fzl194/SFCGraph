---
id: UNC@20.15.2@ConfigObject@GLBAPNRATECTRL
type: ConfigObject
name: GLBAPNRATECTRL（全局APN速率控制配置）
nf: UNC
version: 20.15.2
object_name: GLBAPNRATECTRL
object_kind: global_setting
applicable_nf:
- PGW-C
status: active
---

# GLBAPNRATECTRL（全局APN速率控制配置）

## 说明

![](设置全局APN速率控制配置（SET GLBAPNRATECTRL）_64343915.assets/notice_3.0-zh-cn_2.png)

如果开启全局APN速率控制功能且配置速率过小，会导致用户业务丢包，同时PGW会发送大量Update Bearer Request消息，可能会对周边网元造成信令冲击。

**适用NF：PGW-C**

该命令用于配置全局APN速率控制功能。当网络部署了APN速率控制功能，且规划设置全局默认速率时，使用此命令。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-GLBAPNRATECTRL]] · LST GLBAPNRATECTRL
- [[command/UNC/20.15.2/SET-GLBAPNRATECTRL]] · SET GLBAPNRATECTRL

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局APN速率控制配置（LST-GLBAPNRATECTRL）_64343885.md`
- 原始手册：`evidence/UNC/20.15.2/设置全局APN速率控制配置（SET-GLBAPNRATECTRL）_64343915.md`
