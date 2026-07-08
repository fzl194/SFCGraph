---
id: UDG@20.15.2@ConfigObject@REFRESHSRV
type: ConfigObject
name: REFRESHSRV（业务刷新）
nf: UDG
version: 20.15.2
object_name: REFRESHSRV
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# REFRESHSRV（业务刷新）

## 说明

**适用NF：PGW-U、UPF**

![](业务刷新（SET REFRESHSRV）_82837355.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，可能会影响业务。

该命令用于刷新Filter、FilterGroup、Acl和AclNode配置，将新配置或修改的Filter、FilterGroup、Acl和AclNode置为生效。

## 操作本对象的命令

- [[command/UDG/20.15.2/SET-REFRESHSRV]] · SET REFRESHSRV

## 证据

- 原始手册：`evidence/UDG/20.15.2/REFRESHSRV.md`
