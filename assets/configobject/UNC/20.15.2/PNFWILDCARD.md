---
id: UNC@20.15.2@ConfigObject@PNFWILDCARD
type: ConfigObject
name: PNFWILDCARD（对端NF的通配策略）
nf: UNC
version: 20.15.2
object_name: PNFWILDCARD
object_kind: entity
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SMSF
- NCG
status: active
---

# PNFWILDCARD（对端NF的通配策略）

## 说明

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG**

该命令用于增加对端NF的通配策略。用于指示当本地配置中没有配置或缓存中不包含对端NF支持的特定属性信息时，用户携带该属性查询，此对端NF是否允许被服务发现。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-PNFWILDCARD]] · ADD PNFWILDCARD
- [[command/UNC/20.15.2/LST-PNFWILDCARD]] · LST PNFWILDCARD
- [[command/UNC/20.15.2/MOD-PNFWILDCARD]] · MOD PNFWILDCARD
- [[command/UNC/20.15.2/RMV-PNFWILDCARD]] · RMV PNFWILDCARD

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改对端NF的通配策略（MOD-PNFWILDCARD）_35374745.md`
- 原始手册：`evidence/UNC/20.15.2/删除对端NF的通配策略（RMV-PNFWILDCARD）_35519281.md`
- 原始手册：`evidence/UNC/20.15.2/增加对端NF的通配策略（ADD-PNFWILDCARD）_35374733.md`
- 原始手册：`evidence/UNC/20.15.2/查询对端NF的通配策略（LST-PNFWILDCARD）_35519275.md`
