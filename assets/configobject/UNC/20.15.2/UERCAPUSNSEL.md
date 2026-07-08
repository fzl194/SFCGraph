---
id: UNC@20.15.2@ConfigObject@UERCAPUSNSEL
type: ConfigObject
name: UERCAPUSNSEL（UE无线能力选择USN参数）
nf: UNC
version: 20.15.2
object_name: UERCAPUSNSEL
object_kind: entity
applicable_nf:
- MME
status: active
---

# UERCAPUSNSEL（UE无线能力选择USN参数）

## 说明

**适用网元：MME**

该命令用于配置根据UE无线能力选择USN的参数，在指定用户范围内并且UE无线能力信元长度小于指定阈值的用户，在存储UE无线能力内存的使用率超过阈值后开始自动迁移用户到USN（具体指USN9810/CloudUSN）网元。

指定用户范围的用户的UE无线能力长度小于指定阈值的用户在 [**STR OFFLOADBYENODEB**](../../../网络管理/迁移控制/启动eNodeB迁移任务(STR OFFLOADBYENODEB)_26305902.md) 和 [**STR OFFLOADBYMME**](../../../网络管理/迁移控制/启动MME迁移任务（STR OFFLOADBYMME）_72345693.md) 迁移用户的过程中迁移用户到USN网元。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-UERCAPUSNSEL]] · ADD UERCAPUSNSEL
- [[command/UNC/20.15.2/LST-UERCAPUSNSEL]] · LST UERCAPUSNSEL
- [[command/UNC/20.15.2/MOD-UERCAPUSNSEL]] · MOD UERCAPUSNSEL
- [[command/UNC/20.15.2/RMV-UERCAPUSNSEL]] · RMV UERCAPUSNSEL

## 证据

- 原始手册：`evidence/UNC/20.15.2/UERCAPUSNSEL.md`
- 原始手册：`evidence/UNC/20.15.2/UERCAPUSNSEL.md`
- 原始手册：`evidence/UNC/20.15.2/UERCAPUSNSEL.md`
- 原始手册：`evidence/UNC/20.15.2/UERCAPUSNSEL.md`
