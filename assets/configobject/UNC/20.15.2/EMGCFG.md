---
id: UNC@20.15.2@ConfigObject@EMGCFG
type: ConfigObject
name: EMGCFG（运营商紧急呼叫功能配置）
nf: UNC
version: 20.15.2
object_name: EMGCFG
object_kind: entity
applicable_nf:
- MME
status: active
---

# EMGCFG（运营商紧急呼叫功能配置）

## 说明

**适用网元：MME**

该命令用于增加指定MNO/MVNO对应的紧急呼叫配置数据。运营商需要使用紧急呼叫业务时，通过此命令配置对应MNO或MVNO下的紧急呼叫的策略、紧急业务的APN和QoS相关配置。

## 操作本对象的命令

- [ADD EMGCFG](command/UNC/20.15.2/ADD-EMGCFG.md)
- [LST EMGCFG](command/UNC/20.15.2/LST-EMGCFG.md)
- [MOD EMGCFG](command/UNC/20.15.2/MOD-EMGCFG.md)
- [RMV EMGCFG](command/UNC/20.15.2/RMV-EMGCFG.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改运营商紧急呼叫功能配置（MOD-EMGCFG）_72345103.md`
- 原始手册：`evidence/UNC/20.15.2/删除运营商紧急呼叫功能配置（RMV-EMGCFG）_26145506.md`
- 原始手册：`evidence/UNC/20.15.2/增加运营商紧急呼叫功能配置（ADD-EMGCFG）_26305316.md`
- 原始手册：`evidence/UNC/20.15.2/查询运营商紧急呼叫功能配置（LST-EMGCFG）_72225187.md`
