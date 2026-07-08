---
id: UNC@20.15.2@ConfigObject@VIRTUALAPNRULE
type: ConfigObject
name: VIRTUALAPNRULE（虚拟APN映射策略配置）
nf: UNC
version: 20.15.2
object_name: VIRTUALAPNRULE
object_kind: entity
applicable_nf:
- SMF
- PGW-C
- GGSN
status: active
---

# VIRTUALAPNRULE（虚拟APN映射策略配置）

## 说明

**适用NF：SMF、PGW-C、GGSN**

该命令用于配置指定虚拟APN的映射规则。虚拟APN功能是指多个用户访问不同的PDN时，可携带相同的APN，此APN作为虚拟APN，通过本命令配置的虚拟APN映射规则，匹配到用户的真实APN，从而接入不同的PDN。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-VIRTUALAPNRULE]] · ADD VIRTUALAPNRULE
- [[command/UNC/20.15.2/LST-VIRTUALAPNRULE]] · LST VIRTUALAPNRULE
- [[command/UNC/20.15.2/RMV-VIRTUALAPNRULE]] · RMV VIRTUALAPNRULE

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除虚拟APN映射策略配置（RMV-VIRTUALAPNRULE）_09652430.md`
- 原始手册：`evidence/UNC/20.15.2/增加虚拟APN映射策略配置（ADD-VIRTUALAPNRULE）_09652380.md`
- 原始手册：`evidence/UNC/20.15.2/查询虚拟APN映射策略配置（LST-VIRTUALAPNRULE）_09653739.md`
