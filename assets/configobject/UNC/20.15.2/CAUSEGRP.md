---
id: UNC@20.15.2@ConfigObject@CAUSEGRP
type: ConfigObject
name: CAUSEGRP（原因值映射组配置）
nf: UNC
version: 20.15.2
object_name: CAUSEGRP
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# CAUSEGRP（原因值映射组配置）

## 说明

**适用网元：SGSN、MME**

此命令用于增加一个原因值映射组配置记录。每个原因值映射组表示一个原因值映射规则集合，通常将一个源接口和一个目标接口的原因值映射规则作为一个映射组，如Gr Cause to L3 cause，GTPC cause to L3 cause。CAUSEGRP通常是一组CAUSEMAP的集合。

## 操作本对象的命令

- [ADD CAUSEGRP](command/UNC/20.15.2/ADD-CAUSEGRP.md)
- [LST CAUSEGRP](command/UNC/20.15.2/LST-CAUSEGRP.md)
- [MOD CAUSEGRP](command/UNC/20.15.2/MOD-CAUSEGRP.md)
- [RMV CAUSEGRP](command/UNC/20.15.2/RMV-CAUSEGRP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改原因值映射组配置(MOD-CAUSEGRP)_72345091.md`
- 原始手册：`evidence/UNC/20.15.2/删除原因值映射组配置(RMV-CAUSEGRP)_26305304.md`
- 原始手册：`evidence/UNC/20.15.2/增加原因值映射组配置(ADD-CAUSEGRP)_72225173.md`
- 原始手册：`evidence/UNC/20.15.2/查询原因值映射组配置(LST-CAUSEGRP)_26145494.md`
