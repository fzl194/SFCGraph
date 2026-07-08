---
id: UNC@20.15.2@ConfigObject@IPAREAGP
type: ConfigObject
name: IPAREAGP（IP区域群）
nf: UNC
version: 20.15.2
object_name: IPAREAGP
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# IPAREAGP（IP区域群）

## 说明

**适用网元：SGSN、MME**

IP区域群是“基于位置的IP地址重分配”功能的一个基本概念，是指一组TAC或者LAC，在同一个IP区域群中的用户具有相同的IP地址分配策略。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-IPAREAGP]] · ADD IPAREAGP
- [[command/UNC/20.15.2/LST-IPAREAGP]] · LST IPAREAGP
- [[command/UNC/20.15.2/MOD-IPAREAGP]] · MOD IPAREAGP
- [[command/UNC/20.15.2/RMV-IPAREAGP]] · RMV IPAREAGP

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IP区域群(MOD-IPAREAGP)_72345199.md`
- 原始手册：`evidence/UNC/20.15.2/删除IP区域群(RMV-IPAREAGP)_26145602.md`
- 原始手册：`evidence/UNC/20.15.2/增加IP区域群(ADD-IPAREAGP)_26305412.md`
- 原始手册：`evidence/UNC/20.15.2/查询IP区域群(LST-IPAREAGP)_72225283.md`
