---
id: UNC@20.15.2@ConfigObject@MPSARP
type: ConfigObject
name: MPSARP（MPS ARP配置）
nf: UNC
version: 20.15.2
object_name: MPSARP
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# MPSARP（MPS ARP配置）

## 说明

**适用网元：MME**

此命令用于设置MPS ARP配置。即通过此命令打开MPS功能，并配置MPS的ARP优先级临界值。优先级高于临界值的用户在MPS功能打开的情况下，将不会被流控接入限制，并且可以在下发寻呼的时候获得较高的寻呼优先级。

## 操作本对象的命令

- [LST MPSARP](command/UNC/20.15.2/LST-MPSARP.md)
- [SET MPSARP](command/UNC/20.15.2/SET-MPSARP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询MPS-ARP配置(LST-MPSARP)_72345099.md`
- 原始手册：`evidence/UNC/20.15.2/设置MPS-ARP配置(SET-MPSARP)_26305312.md`
