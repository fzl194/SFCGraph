---
id: UNC@20.15.2@ConfigObject@APNPAGINGPLCY
type: ConfigObject
name: APNPAGINGPLCY（APN寻呼策略参数配置）
nf: UNC
version: 20.15.2
object_name: APNPAGINGPLCY
object_kind: entity
applicable_nf:
- MME
status: active
---

# APNPAGINGPLCY（APN寻呼策略参数配置）

## 说明

**适用网元：MME**

该命令用于增加APN的寻呼策略。系统可以根据特定APN的参数配置来决定业务优先处理策略。 UNC 收到S-GW下发的DDN(Downlink Data Notification)/CBR(Create Bearer Request)/UBR(Update Bearer Request)消息，如果这些消息是针对特定APN的业务，则MME不对这些消息进行流控，并在上述消息触发的S1接口寻呼消息中携带寻呼优先级。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-APNPAGINGPLCY]] · ADD APNPAGINGPLCY
- [[command/UNC/20.15.2/LST-APNPAGINGPLCY]] · LST APNPAGINGPLCY
- [[command/UNC/20.15.2/MOD-APNPAGINGPLCY]] · MOD APNPAGINGPLCY
- [[command/UNC/20.15.2/RMV-APNPAGINGPLCY]] · RMV APNPAGINGPLCY

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改APN寻呼策略参数配置(MOD-APNPAGINGPLCY)_26305520.md`
- 原始手册：`evidence/UNC/20.15.2/删除APN寻呼策略参数配置(RMV-APNPAGINGPLCY)_72345307.md`
- 原始手册：`evidence/UNC/20.15.2/增加APN寻呼策略参数配置(ADD-APNPAGINGPLCY)_72225389.md`
- 原始手册：`evidence/UNC/20.15.2/查询APN寻呼策略参数配置(LST-APNPAGINGPLCY)_26145712.md`
