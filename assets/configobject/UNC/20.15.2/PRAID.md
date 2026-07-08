---
id: UNC@20.15.2@ConfigObject@PRAID
type: ConfigObject
name: PRAID（PRA标识）
nf: UNC
version: 20.15.2
object_name: PRAID
object_kind: entity
applicable_nf:
- MME
status: active
---

# PRAID（PRA标识）

## 说明

**适用网元：MME**

该命令用于配置PRA区域基本信息，包括PRA区域标识、PRA区域内本网异地用户的可用属性，以及PRA区域描述信息。PRA可分为核心网预定义PRA（Core Network predefined PRA）和UE专属PRA（UE-dedicated PRA）两种。其中在MME上配置的PRA都是核心网预定义PRA。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PRAID]] · ADD PRAID
- [[command/UNC/20.15.2/LST-PRAID]] · LST PRAID
- [[command/UNC/20.15.2/MOD-PRAID]] · MOD PRAID
- [[command/UNC/20.15.2/RMV-PRAID]] · RMV PRAID

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改PRA标识(MOD-PRAID)_72345193.md`
- 原始手册：`evidence/UNC/20.15.2/删除PRA标识(RMV-PRAID)_26305406.md`
- 原始手册：`evidence/UNC/20.15.2/增加PRA标识(ADD-PRAID)_72225275.md`
- 原始手册：`evidence/UNC/20.15.2/查询PRA标识(LST-PRAID)_26145596.md`
