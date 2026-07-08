---
id: UDG@20.15.2@ConfigObject@GYONESHOT
type: ConfigObject
name: GYONESHOT（Gy一次重定向参数）
nf: UDG
version: 20.15.2
object_name: GYONESHOT
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# GYONESHOT（Gy一次重定向参数）

## 说明

**适用NF：PGW-U、UPF**

该命令用于配置Gy接口一次重定向的URL白名单列表，并配置是否包含重定向携带信息。匹配上该白名单的报文将被重定向到OCS下发的URL。

## 操作本对象的命令

- [LST GYONESHOT](command/UDG/20.15.2/LST-GYONESHOT.md)
- [SET GYONESHOT](command/UDG/20.15.2/SET-GYONESHOT.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Gy一次重定向参数（LST-GYONESHOT）_86528909.md`
- 原始手册：`evidence/UDG/20.15.2/设置Gy一次重定向参数（SET-GYONESHOT）_82837567.md`
