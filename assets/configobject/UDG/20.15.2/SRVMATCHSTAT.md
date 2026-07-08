---
id: UDG@20.15.2@ConfigObject@SRVMATCHSTAT
type: ConfigObject
name: SRVMATCHSTAT（业务匹配统计参数）
nf: UDG
version: 20.15.2
object_name: SRVMATCHSTAT
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# SRVMATCHSTAT（业务匹配统计参数）

## 说明

**适用NF：PGW-U、UPF**

该命令用于配置是否开启业务匹配的统计功能。功能开启，当业务匹配到规则的时候，将对应规则的匹配计数加1。功能关闭则不进行规则匹配计数的统计。运营商需要进行规则匹配次数的监控时，可以开启该功能。

## 操作本对象的命令

- [LST SRVMATCHSTAT](command/UDG/20.15.2/LST-SRVMATCHSTAT.md)
- [SET SRVMATCHSTAT](command/UDG/20.15.2/SET-SRVMATCHSTAT.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询业务匹配统计参数（LST-SRVMATCHSTAT）_35373581.md`
- 原始手册：`evidence/UDG/20.15.2/设置业务匹配统计参数（SET-SRVMATCHSTAT）_35373580.md`
