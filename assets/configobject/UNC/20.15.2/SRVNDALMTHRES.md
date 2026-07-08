---
id: UNC@20.15.2@ConfigObject@SRVNDALMTHRES
type: ConfigObject
name: SRVNDALMTHRES（业务节点资源不足告警阈值）
nf: UNC
version: 20.15.2
object_name: SRVNDALMTHRES
object_kind: global_setting
applicable_nf:
- GGSN
- SGW-C
- PGW-C
- SMF
status: active
---

# SRVNDALMTHRES（业务节点资源不足告警阈值）

## 说明

**适用NF：GGSN、SGW-C、PGW-C、SMF**

该命令用于配置业务节点告警阈值和恢复告警阈值。当业务节点资源使用率超过配置的告警门限时产生告警。当使用率低于配置的恢复门限时恢复告警。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-SRVNDALMTHRES]] · LST SRVNDALMTHRES
- [[command/UNC/20.15.2/SET-SRVNDALMTHRES]] · SET SRVNDALMTHRES

## 证据

- 原始手册：`evidence/UNC/20.15.2/SRVNDALMTHRES.md`
- 原始手册：`evidence/UNC/20.15.2/SRVNDALMTHRES.md`
