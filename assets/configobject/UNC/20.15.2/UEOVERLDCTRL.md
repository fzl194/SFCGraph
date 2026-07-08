---
id: UNC@20.15.2@ConfigObject@UEOVERLDCTRL
type: ConfigObject
name: UEOVERLDCTRL（UE重载控制策略）
nf: UNC
version: 20.15.2
object_name: UEOVERLDCTRL
object_kind: entity
applicable_nf:
- AMF
status: active
---

# UEOVERLDCTRL（UE重载控制策略）

## 说明

**适用NF：AMF**

该命令用于为指定的用户（群）配置重载控制策略参数。

该命令的使用场景：若基站需要通过MPS和MCS能力实行重载控制功能，可通过本命令控制AMF是否将UDM签约或本地配置的MPS和MCS能力携带给基站。

## 操作本对象的命令

- [ADD UEOVERLDCTRL](command/UNC/20.15.2/ADD-UEOVERLDCTRL.md)
- [LST UEOVERLDCTRL](command/UNC/20.15.2/LST-UEOVERLDCTRL.md)
- [MOD UEOVERLDCTRL](command/UNC/20.15.2/MOD-UEOVERLDCTRL.md)
- [RMV UEOVERLDCTRL](command/UNC/20.15.2/RMV-UEOVERLDCTRL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改UE重载控制策略（MOD-UEOVERLDCTRL）_91226954.md`
- 原始手册：`evidence/UNC/20.15.2/删除UE重载控制策略（RMV-UEOVERLDCTRL）_26746345.md`
- 原始手册：`evidence/UNC/20.15.2/增加UE重载控制策略（ADD-UEOVERLDCTRL）_91067090.md`
- 原始手册：`evidence/UNC/20.15.2/查询UE重载控制策略（LST-UEOVERLDCTRL）_26826613.md`
