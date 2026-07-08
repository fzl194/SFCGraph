---
id: UNC@20.15.2@ConfigObject@CHGPLMNCG
type: ConfigObject
name: CHGPLMNCG（PLMN-CG配置参数）
nf: UNC
version: 20.15.2
object_name: CHGPLMNCG
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# CHGPLMNCG（PLMN-CG配置参数）

## 说明

**适用网元：SGSN**

该命令用于为PLMN配置CG IP地址。该PLMN上产生的话单会优先发往这些已配置过的CG。

SGSN和CG之间互通时，需要配置该命令。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-CHGPLMNCG]] · ADD CHGPLMNCG
- [[command/UNC/20.15.2/LST-CHGPLMNCG]] · LST CHGPLMNCG
- [[command/UNC/20.15.2/MOD-CHGPLMNCG]] · MOD CHGPLMNCG
- [[command/UNC/20.15.2/RMV-CHGPLMNCG]] · RMV CHGPLMNCG

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改PLMN-CG配置参数(MOD-CHGPLMNCG)_72344989.md`
- 原始手册：`evidence/UNC/20.15.2/删除PLMN-CG配置参数(RMV-CHGPLMNCG)_26305202.md`
- 原始手册：`evidence/UNC/20.15.2/增加PLMN-CG配置参数（ADD-CHGPLMNCG）_72225067.md`
- 原始手册：`evidence/UNC/20.15.2/查询PLMN-CG配置参数(LST-CHGPLMNCG)_26145388.md`
