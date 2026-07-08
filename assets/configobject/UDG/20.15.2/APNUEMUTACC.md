---
id: UDG@20.15.2@ConfigObject@APNUEMUTACC
type: ConfigObject
name: APNUEMUTACC（APN下用户互访控制配置）
nf: UDG
version: 20.15.2
object_name: APNUEMUTACC
object_kind: global_setting
applicable_nf:
- UPF
- PGW-U
status: active
---

# APNUEMUTACC（APN下用户互访控制配置）

## 说明

**适用NF：UPF、PGW-U**

![](设置APN下用户互访控制配置（SET APNUEMUTACC）_82837776.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，APN下终端互访控制功能开启后，所有此APN内或者和其它APN之间的终端互访将无法进行。 当修改INNERAPNS_S5S8P、INNERAPNS_N9A、INTERAPNS_S5S8P、INTERAPNS_N9A等参数时，需要使用ADD UEMUTWLISTBIND命令绑定白名单，否则会导致UE互访业务不通。

本命令仅适用于同一UPF网元内不同UE会话的互访控制，如果需要跨UPF网元的不同UE会话的互访控制，需要在UPF上配置ACL规则。

该命令用于配置指定APN下用户互访禁止功能开关是否开启，包括APN间的用户互访及APN内的用户互访。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-APNUEMUTACC]] · LST APNUEMUTACC
- [[command/UDG/20.15.2/SET-APNUEMUTACC]] · SET APNUEMUTACC

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询APN下用户互访控制配置（LST-APNUEMUTACC）_82837777.md`
- 原始手册：`evidence/UDG/20.15.2/设置APN下用户互访控制配置（SET-APNUEMUTACC）_82837776.md`
