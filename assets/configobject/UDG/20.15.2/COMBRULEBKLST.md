---
id: UDG@20.15.2@ConfigObject@COMBRULEBKLST
type: ConfigObject
name: COMBRULEBKLST（组合规则黑名单）
nf: UDG
version: 20.15.2
object_name: COMBRULEBKLST
object_kind: global_setting
applicable_nf:
- PGW-U
- UPF
status: active
---

# COMBRULEBKLST（组合规则黑名单）

## 说明

**适用NF：PGW-U、UPF**

该命令用于配置如果同时存在组合rule和拆分rule，组合rule type中未配置，且组合rule优先级低，则网关当做是的blacklist的策略类型。

## 操作本对象的命令

- [LST COMBRULEBKLST](command/UDG/20.15.2/LST-COMBRULEBKLST.md)
- [SET COMBRULEBKLST](command/UDG/20.15.2/SET-COMBRULEBKLST.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示组合规则黑名单（LST-COMBRULEBKLST）_86530160.md`
- 原始手册：`evidence/UDG/20.15.2/设置组合规则黑名单（SET-COMBRULEBKLST）_86530161.md`
