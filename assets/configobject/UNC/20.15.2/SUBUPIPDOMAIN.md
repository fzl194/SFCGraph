---
id: UNC@20.15.2@ConfigObject@SUBUPIPDOMAIN
type: ConfigObject
name: SUBUPIPDOMAIN（当前UPF扩展类型绑定的IP域）
nf: UNC
version: 20.15.2
object_name: SUBUPIPDOMAIN
object_kind: entity
applicable_nf:
- PGW-C
- SMF
status: active
---

# SUBUPIPDOMAIN（当前UPF扩展类型绑定的IP域）

## 说明

**适用NF：PGW-C、SMF**

该命令用于将指定UPF通过扩展类型绑定到特定的IPDomain，当该UPF作为会话主锚点UPF时，SMF内部会在UE IP前加上该IPDomain前缀，并带给PCF，用于扩展地址池。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SUBUPIPDOMAIN]] · ADD SUBUPIPDOMAIN
- [[command/UNC/20.15.2/LST-SUBUPIPDOMAIN]] · LST SUBUPIPDOMAIN
- [[command/UNC/20.15.2/MOD-SUBUPIPDOMAIN]] · MOD SUBUPIPDOMAIN
- [[command/UNC/20.15.2/RMV-SUBUPIPDOMAIN]] · RMV SUBUPIPDOMAIN

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改当前UPF扩展类型绑定的IP域（MOD-SUBUPIPDOMAIN）_72004513.md`
- 原始手册：`evidence/UNC/20.15.2/删除当前UPF扩展类型绑定的IP域（RMV-SUBUPIPDOMAIN）_23804526.md`
- 原始手册：`evidence/UNC/20.15.2/增加当前UPF扩展类型绑定的IP域（ADD-SUBUPIPDOMAIN）_71924421.md`
- 原始手册：`evidence/UNC/20.15.2/查询当前UPF扩展类型绑定的IP域（LST-SUBUPIPDOMAIN）_23484622.md`
