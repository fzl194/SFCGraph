---
id: UNC@20.15.2@ConfigObject@ALIASAPN
type: ConfigObject
name: ALIASAPN（别名APN配置）
nf: UNC
version: 20.15.2
object_name: ALIASAPN
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# ALIASAPN（别名APN配置）

## 说明

**适用网元：SGSN、MME**

该命令用于增加别名APN(Access Point Name)转换配置。APN别名配置用于将原始APN映射为别名APN。APN别名映射功能是将签约数据匹配后的APN NI映射成配置的别名APN NI，使用新的APN NI发起DNS解析。这样可以屏蔽用户APN的差异以及降低用户关于APN的配置要求，用户可以随意配置或者不配置，但系统可以把这些映射成实际使用的通用APN。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-ALIASAPN]] · ADD ALIASAPN
- [[command/UNC/20.15.2/LST-ALIASAPN]] · LST ALIASAPN
- [[command/UNC/20.15.2/MOD-ALIASAPN]] · MOD ALIASAPN
- [[command/UNC/20.15.2/RMV-ALIASAPN]] · RMV ALIASAPN

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改别名APN配置(MOD-ALIASAPN)_72225365.md`
- 原始手册：`evidence/UNC/20.15.2/删除别名APN配置(RMV-ALIASAPN)_26145686.md`
- 原始手册：`evidence/UNC/20.15.2/增加别名APN配置(ADD-ALIASAPN)_72345281.md`
- 原始手册：`evidence/UNC/20.15.2/查询别名APN配置(LST-ALIASAPN)_26305496.md`
