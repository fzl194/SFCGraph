---
id: UDG@20.15.2@ConfigObject@AFPOLICY
type: ConfigObject
name: AFPOLICY（防欺诈策略配置）
nf: UDG
version: 20.15.2
object_name: AFPOLICY
object_kind: entity
applicable_nf:
- PGW-U
- UPF
status: active
---

# AFPOLICY（防欺诈策略配置）

## 说明

**适用NF：PGW-U、UPF**

该命令用于增加判断出欺诈行为后的处理策略。如果AFPolicy没有配置参数，无法匹配选择到欺诈策略，则欺诈业务流会使用正常配置的处理策略，不会做策略切换。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-AFPOLICY]] · ADD AFPOLICY
- [[command/UDG/20.15.2/LST-AFPOLICY]] · LST AFPOLICY
- [[command/UDG/20.15.2/MOD-AFPOLICY]] · MOD AFPOLICY
- [[command/UDG/20.15.2/RMV-AFPOLICY]] · RMV AFPOLICY

## 证据

- 原始手册：`evidence/UDG/20.15.2/AFPOLICY.md`
- 原始手册：`evidence/UDG/20.15.2/AFPOLICY.md`
- 原始手册：`evidence/UDG/20.15.2/AFPOLICY.md`
- 原始手册：`evidence/UDG/20.15.2/AFPOLICY.md`
