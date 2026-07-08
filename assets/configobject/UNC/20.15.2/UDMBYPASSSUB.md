---
id: UNC@20.15.2@ConfigObject@UDMBYPASSSUB
type: ConfigObject
name: UDMBYPASSSUB（UDM Bypass最小签约数据配置）
nf: UNC
version: 20.15.2
object_name: UDMBYPASSSUB
object_kind: entity
applicable_nf:
- AMF
status: active
---

# UDMBYPASSSUB（UDM Bypass最小签约数据配置）

## 说明

**适用NF：AMF**

该命令用于对指定的用户（群）增加UDM Bypass最小签约数据配置。用户处于UDM BYPASS状态之后，AMF无法从UDM获取用户签约数据，如果系统内无用户历史签约数据，使用该命令手动配置用户最小签约数据，保证业务惯性运行。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-UDMBYPASSSUB]] · ADD UDMBYPASSSUB
- [[command/UNC/20.15.2/LST-UDMBYPASSSUB]] · LST UDMBYPASSSUB
- [[command/UNC/20.15.2/MOD-UDMBYPASSSUB]] · MOD UDMBYPASSSUB
- [[command/UNC/20.15.2/RMV-UDMBYPASSSUB]] · RMV UDMBYPASSSUB

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改UDM-Bypass最小签约数据配置（MOD-UDMBYPASSSUB）_32414327.md`
- 原始手册：`evidence/UNC/20.15.2/删除UDM-Bypass最小签约数据配置（RMV-UDMBYPASSSUB）_32335887.md`
- 原始手册：`evidence/UNC/20.15.2/增加UDM-Bypass最小签约数据配置（ADD-UDMBYPASSSUB）_86856256.md`
- 原始手册：`evidence/UNC/20.15.2/查询UDM-Bypass最小签约数据配置（LST-UDMBYPASSSUB）_32654395.md`
