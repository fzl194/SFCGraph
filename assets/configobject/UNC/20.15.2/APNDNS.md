---
id: UNC@20.15.2@ConfigObject@APNDNS
type: ConfigObject
name: APNDNS（APN DNS域名策略）
nf: UNC
version: 20.15.2
object_name: APNDNS
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# APNDNS（APN DNS域名策略）

## 说明

**适用网元：SGSN、MME**

该命令用于增加一条APN DNS域名策略。

当选择上游网元GGSN/PGW时，需要根据APNNI和UE允许的接入能力确定使用.gprs后缀还是.org后缀组装APN域名。同时，DNS查询时，根据APNNI域名类型选择最多8个IP地址组成备选列表，进行负荷分担。当可用的IP地址权重少于阈值时，选择低优先级IP地址进行补充。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-APNDNS]] · ADD APNDNS
- [[command/UNC/20.15.2/LST-APNDNS]] · LST APNDNS
- [[command/UNC/20.15.2/MOD-APNDNS]] · MOD APNDNS
- [[command/UNC/20.15.2/RMV-APNDNS]] · RMV APNDNS

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改APN-DNS域名策略(MOD-APNDNS)_26305742.md`
- 原始手册：`evidence/UNC/20.15.2/删除APN-DNS域名策略(RMV-APNDNS)_72225611.md`
- 原始手册：`evidence/UNC/20.15.2/增加APN-DNS域名策略(ADD-APNDNS)_26145932.md`
- 原始手册：`evidence/UNC/20.15.2/查询APN-DNS域名策略(LST-APNDNS)_72345533.md`
