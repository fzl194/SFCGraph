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

- [[command/UNC/20.15.2/ADD-CAUSEGRP]] · ADD CAUSEGRP
- [[command/UNC/20.15.2/LST-CAUSEGRP]] · LST CAUSEGRP
- [[command/UNC/20.15.2/MOD-CAUSEGRP]] · MOD CAUSEGRP
- [[command/UNC/20.15.2/RMV-CAUSEGRP]] · RMV CAUSEGRP

## 证据

- 原始手册：`evidence/UNC/20.15.2/CAUSEGRP.md`
- 原始手册：`evidence/UNC/20.15.2/CAUSEGRP.md`
- 原始手册：`evidence/UNC/20.15.2/CAUSEGRP.md`
- 原始手册：`evidence/UNC/20.15.2/CAUSEGRP.md`
