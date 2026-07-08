---
id: UDG@20.15.2@ConfigObject@UPN4UPATH
type: ConfigObject
name: UPN4UPATH（N4U路径相关属性）
nf: UDG
version: 20.15.2
object_name: UPN4UPATH
object_kind: global_setting
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# UPN4UPATH（N4U路径相关属性）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

![](设置N4U路径相关属性（SET UPN4UPATH）_18761567.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，配置UPF主动向SMF发送GTP请求消息的重发时间间隔和最大尝试发送次数，如果配置不合理，可能导致用户激活失败或资源残留。

该命令用来设置N4U路径的Echo探测属性。

## 操作本对象的命令

- [LST UPN4UPATH](command/UDG/20.15.2/LST-UPN4UPATH.md)
- [SET UPN4UPATH](command/UDG/20.15.2/SET-UPN4UPATH.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询N4U路径相关属性（LST-UPN4UPATH）_18404303.md`
- 原始手册：`evidence/UDG/20.15.2/设置N4U路径相关属性（SET-UPN4UPATH）_18761567.md`
