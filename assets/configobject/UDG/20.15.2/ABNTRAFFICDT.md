---
id: UDG@20.15.2@ConfigObject@ABNTRAFFICDT
type: ConfigObject
name: ABNTRAFFICDT（异常流量检测开关）
nf: UDG
version: 20.15.2
object_name: ABNTRAFFICDT
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
identifier_parameters:
- APN
status: active
---

# ABNTRAFFICDT（异常流量检测开关）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用来使能APN下终端异常下行流量检测功能。

## 操作本对象的命令

- [ADD ABNTRAFFICDT](command/UDG/20.15.2/ADD-ABNTRAFFICDT.md)
- [LST ABNTRAFFICDT](command/UDG/20.15.2/LST-ABNTRAFFICDT.md)
- [MOD ABNTRAFFICDT](command/UDG/20.15.2/MOD-ABNTRAFFICDT.md)
- [RMV ABNTRAFFICDT](command/UDG/20.15.2/RMV-ABNTRAFFICDT.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改异常流量检测开关（MOD-ABNTRAFFICDT）_82837036.md`
- 原始手册：`evidence/UDG/20.15.2/删除异常流量检测开关（RMV-ABNTRAFFICDT）_82837037.md`
- 原始手册：`evidence/UDG/20.15.2/新增异常流量检测开关（ADD-ABNTRAFFICDT）_82837035.md`
- 原始手册：`evidence/UDG/20.15.2/查询异常流量功能开关（LST-ABNTRAFFICDT）_86526441.md`
