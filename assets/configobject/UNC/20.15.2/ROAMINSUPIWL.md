---
id: UNC@20.15.2@ConfigObject@ROAMINSUPIWL
type: ConfigObject
name: ROAMINSUPIWL（漫入场景SUPI白名单）
nf: UNC
version: 20.15.2
object_name: ROAMINSUPIWL
object_kind: entity
applicable_nf:
- NRF
status: active
---

# ROAMINSUPIWL（漫入场景SUPI白名单）

## 说明

**适用NF：NRF**

该命令用于增加漫入场景SUPI白名单。

该命令与漫入SUPI服务发现白名单开关SET NRFINTERFUNC中的ROAMINSUPIWLSW配合使用，ROAMINSUPIWLSW为FUNC_ON时基于白名单用户SUPI号码或SUPI号段列表配置I-NRF允许服务发现他网AUSF/UDM。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-ROAMINSUPIWL]] · ADD ROAMINSUPIWL
- [[command/UNC/20.15.2/LST-ROAMINSUPIWL]] · LST ROAMINSUPIWL
- [[command/UNC/20.15.2/RMV-ROAMINSUPIWL]] · RMV ROAMINSUPIWL

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除漫入场景SUPI白名单（RMV-ROAMINSUPIWL）_70382385.md`
- 原始手册：`evidence/UNC/20.15.2/增加漫入场景SUPI白名单（ADD-ROAMINSUPIWL）_70462521.md`
- 原始手册：`evidence/UNC/20.15.2/查询漫入场景SUPI白名单（LST-ROAMINSUPIWL）_23622958.md`
