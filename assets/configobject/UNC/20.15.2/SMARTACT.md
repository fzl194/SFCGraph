---
id: UNC@20.15.2@ConfigObject@SMARTACT
type: ConfigObject
name: SMARTACT（激活抑制规则）
nf: UNC
version: 20.15.2
object_name: SMARTACT
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# SMARTACT（激活抑制规则）

## 说明

**适用网元：SGSN**

此命令用于添加基于用户终端类型的激活抑制规则。用户激活异常时，按照配置的激活抑制规则对其进行抑制。

当需要对频繁激活的用户进行信令抑制，减少SGSN信令负载时，需要执行此命令。

## 操作本对象的命令

- [ADD SMARTACT](command/UNC/20.15.2/ADD-SMARTACT.md)
- [LST SMARTACT](command/UNC/20.15.2/LST-SMARTACT.md)
- [MOD SMARTACT](command/UNC/20.15.2/MOD-SMARTACT.md)
- [RMV SMARTACT](command/UNC/20.15.2/RMV-SMARTACT.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改激活抑制规则（MOD-SMARTACT）_72345343.md`
- 原始手册：`evidence/UNC/20.15.2/删除激活抑制规则（RMV-SMARTACT）_26305552.md`
- 原始手册：`evidence/UNC/20.15.2/增加激活抑制规则（ADD-SMARTACT）_72225421.md`
- 原始手册：`evidence/UNC/20.15.2/查询激活抑制规则（LST-SMARTACT）_26145744.md`
