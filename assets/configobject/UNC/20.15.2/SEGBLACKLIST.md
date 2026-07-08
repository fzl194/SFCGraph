---
id: UNC@20.15.2@ConfigObject@SEGBLACKLIST
type: ConfigObject
name: SEGBLACKLIST（导入号段黑名单）
nf: UNC
version: 20.15.2
object_name: SEGBLACKLIST
object_kind: entity
applicable_nf:
- NRF
status: active
---

# SEGBLACKLIST（导入号段黑名单）

## 说明

**适用NF：NRF**

该命令已废弃。

该命令用于新增导入号段黑名单，命令中配置的号段数据将在NRF导入号段数据中失效。例如，NRF通过导入号段方式定义UDM支持的IMSI号段的范围为123456~234567，345678~456789，通过此命令配置UDM的IMSI黑名单范围为123456~234567，则UDM通过导入号段方式实际支持的IMSI号段范围123456~234567失效，345678~456789仍然有效。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-SEGBLACKLIST]] · ADD SEGBLACKLIST
- [[command/UNC/20.15.2/LST-SEGBLACKLIST]] · LST SEGBLACKLIST
- [[command/UNC/20.15.2/RMV-SEGBLACKLIST]] · RMV SEGBLACKLIST

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除导入号段黑名单（RMV-SEGBLACKLIST）_96242990.md`
- 原始手册：`evidence/UNC/20.15.2/增加导入号段黑名单（ADD-SEGBLACKLIST）_73321228.md`
- 原始手册：`evidence/UNC/20.15.2/查询导入号段黑名单（LST-SEGBLACKLIST）_96242447.md`
