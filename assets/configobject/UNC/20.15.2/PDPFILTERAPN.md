---
id: UNC@20.15.2@ConfigObject@PDPFILTERAPN
type: ConfigObject
name: PDPFILTERAPN（APN优先级配置）
nf: UNC
version: 20.15.2
object_name: PDPFILTERAPN
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# PDPFILTERAPN（APN优先级配置）

## 说明

**适用网元：SGSN**

该命令用于增加APN优先级配置。APN优先级可以用于在RAU或者RELOCATION流程中指示新侧保留PDP的顺序。高优先级APN对应的PDP会优先保留，低优先级APN对应的PDP会在切换后主动删掉。

在GU网络存在无线侧PDP能力不足的情况下，可通过此命令配置APN优先级，当系统通过RAU或者Relocation流程切换到GU网络后主动去激活低优先级的PDP，从而确保高优先级PDP业务不受影响。如不配置APN优先级，无线侧将可能随机删除重要的PDP，造成重要业务中断。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PDPFILTERAPN]] · ADD PDPFILTERAPN
- [[command/UNC/20.15.2/LST-PDPFILTERAPN]] · LST PDPFILTERAPN
- [[command/UNC/20.15.2/MOD-PDPFILTERAPN]] · MOD PDPFILTERAPN
- [[command/UNC/20.15.2/RMV-PDPFILTERAPN]] · RMV PDPFILTERAPN

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改APN优先级配置(MOD-PDPFILTERAPN)_26145690.md`
- 原始手册：`evidence/UNC/20.15.2/删除APN优先级配置(RMV-PDPFILTERAPN)_72345285.md`
- 原始手册：`evidence/UNC/20.15.2/增加APN优先级配置(ADD-PDPFILTERAPN)_26305498.md`
- 原始手册：`evidence/UNC/20.15.2/查询APN优先级配置(LST-PDPFILTERAPN)_72225369.md`
