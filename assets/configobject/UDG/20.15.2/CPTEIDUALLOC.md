---
id: UDG@20.15.2@ConfigObject@CPTEIDUALLOC
type: ConfigObject
name: CPTEIDUALLOC（CP分配TEID-U开关）
nf: UDG
version: 20.15.2
object_name: CPTEIDUALLOC
object_kind: global_setting
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# CPTEIDUALLOC（CP分配TEID-U开关）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用于配置是否支持CP分配TEID-U功能。当前产品仅支持UP本地分配TEID-U，不支持CP分配TEID-U，如果配置错误，可能导致用户激活失败。

## 操作本对象的命令

- [LST CPTEIDUALLOC](command/UDG/20.15.2/LST-CPTEIDUALLOC.md)
- [SET CPTEIDUALLOC](command/UDG/20.15.2/SET-CPTEIDUALLOC.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询CP分配TEID-U开关（LST-CPTEIDUALLOC）_86527096.md`
- 原始手册：`evidence/UDG/20.15.2/配置CP分配TEID-U开关（SET-CPTEIDUALLOC）_82837177.md`
