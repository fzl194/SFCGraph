---
id: UNC@20.15.2@ConfigObject@CAUSEMAP
type: ConfigObject
name: CAUSEMAP（原因值映射配置）
nf: UNC
version: 20.15.2
object_name: CAUSEMAP
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# CAUSEMAP（原因值映射配置）

## 说明

**适用网元：SGSN、MME**

此命令用于增加一个原因值映射配置记录。原因值映射就是将原接口消息中的原因值直接映射到目标接口消息中下发的原因值。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-CAUSEMAP]] · ADD CAUSEMAP
- [[command/UNC/20.15.2/LST-CAUSEMAP]] · LST CAUSEMAP
- [[command/UNC/20.15.2/MOD-CAUSEMAP]] · MOD CAUSEMAP
- [[command/UNC/20.15.2/RMV-CAUSEMAP]] · RMV CAUSEMAP

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改原因值映射配置(MOD-CAUSEMAP)_26305302.md`
- 原始手册：`evidence/UNC/20.15.2/删除原因值映射配置(RMV-CAUSEMAP)_72225171.md`
- 原始手册：`evidence/UNC/20.15.2/增加原因值映射配置(ADD-CAUSEMAP)_26145490.md`
- 原始手册：`evidence/UNC/20.15.2/查询原因值映射配置(LST-CAUSEMAP)_72345089.md`
