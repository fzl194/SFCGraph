---
id: UDG@20.15.2@ConfigObject@APNACCESSWAL
type: ConfigObject
name: APNACCESSWAL（Apn接入速率配置）
nf: UDG
version: 20.15.2
object_name: APNACCESSWAL
object_kind: global_setting
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# APNACCESSWAL（Apn接入速率配置）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

![](设置Apn接入速率配置（SET APNACCESSWAL）_06054797.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，配置合理的用户接入速率取值，否则无法保护自身及后端网元或用户激活失败。

该命令用来配置APN的接入速率。当需要限制APN的接入速率时使用此配置，比如可以用来防止APN相关的网元故障导致的激活信令突增造成对其他网元的冲击。

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-APNACCESSWAL]] · LST APNACCESSWAL
- [[command/UDG/20.15.2/SET-APNACCESSWAL]] · SET APNACCESSWAL

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Apn接入速率配置（LST-APNACCESSWAL）_06054798.md`
- 原始手册：`evidence/UDG/20.15.2/设置Apn接入速率配置（SET-APNACCESSWAL）_06054797.md`
