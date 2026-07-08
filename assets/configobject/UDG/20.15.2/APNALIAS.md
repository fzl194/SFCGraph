---
id: UDG@20.15.2@ConfigObject@APNALIAS
type: ConfigObject
name: APNALIAS（ApnAlias配置）
nf: UDG
version: 20.15.2
object_name: APNALIAS
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# APNALIAS（ApnAlias配置）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用于添加ApnAlias配置。为了兼容多个APN使用完全相同资源的情况，使用该命令配置APN别名，把它映射到真实APN上，这样多个别名APN就能共用一个真实APN的系统资源。别名APN主要适用于以下两种场景：

1、运营商合并和重组时，为了兼容现网中使用相同资源的多个APN，可将某APN的业务映射到另一APN上。

2、网络改建时新规划了APN，为了不影响原规划APN的使用，只需将原规划的APN映射到新规划APN上即可。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-APNALIAS]] · ADD APNALIAS
- [[command/UDG/20.15.2/LST-APNALIAS]] · LST APNALIAS
- [[command/UDG/20.15.2/RMV-APNALIAS]] · RMV APNALIAS

## 证据

- 原始手册：`evidence/UDG/20.15.2/APNALIAS.md`
- 原始手册：`evidence/UDG/20.15.2/APNALIAS.md`
- 原始手册：`evidence/UDG/20.15.2/APNALIAS.md`
