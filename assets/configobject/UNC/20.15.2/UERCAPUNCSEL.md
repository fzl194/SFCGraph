---
id: UNC@20.15.2@ConfigObject@UERCAPUNCSEL
type: ConfigObject
name: UERCAPUNCSEL（UE无线能力选择UNC参数）
nf: UNC
version: 20.15.2
object_name: UERCAPUNCSEL
object_kind: entity
applicable_nf:
- MME
status: active
---

# UERCAPUNCSEL（UE无线能力选择UNC参数）

## 说明

**适用网元：MME**

该命令用于配置根据UE无线能力选择UNC的参数，指定用户范围的用户的UE无线能力长度大于指定阈值的用户在 [**STR OFFLOADBYENODEB**](../../../网络管理/迁移控制/启动eNodeB迁移任务(STR OFFLOADBYENODEB)_26305902.md) 和 [**STR OFFLOADBYMME**](../../../网络管理/迁移控制/启动MME迁移任务（STR OFFLOADBYMME）_72345693.md) 迁移用户的过程中迁移到UNC网元。

## 操作本对象的命令

- [ADD UERCAPUNCSEL](command/UNC/20.15.2/ADD-UERCAPUNCSEL.md)
- [LST UERCAPUNCSEL](command/UNC/20.15.2/LST-UERCAPUNCSEL.md)
- [MOD UERCAPUNCSEL](command/UNC/20.15.2/MOD-UERCAPUNCSEL.md)
- [RMV UERCAPUNCSEL](command/UNC/20.15.2/RMV-UERCAPUNCSEL.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改UE无线能力选择UNC参数(MOD-UERCAPUNCSEL)_25233190.md`
- 原始手册：`evidence/UNC/20.15.2/删除UE无线能力选择UNC参数(RMV-UERCAPUNCSEL)_72912941.md`
- 原始手册：`evidence/UNC/20.15.2/增加UE无线能力选择UNC参数(ADD-UERCAPUNCSEL)_25073810.md`
- 原始手册：`evidence/UNC/20.15.2/查询UE无线能力选择UNC参数(LST-UERCAPUNCSEL)_72753621.md`
