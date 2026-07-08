---
id: UNC@20.15.2@ConfigObject@NGAREATZ
type: ConfigObject
name: NGAREATZ（5G区域时区参数）
nf: UNC
version: 20.15.2
object_name: NGAREATZ
object_kind: entity
applicable_nf:
- AMF
status: active
---

# NGAREATZ（5G区域时区参数）

## 说明

**适用NF：AMF**

此命令用于增加5G区域时区记录。即增加特定区域与时区标识的映射关系。该时区标识对应的时区和夏令时信息通过ADD NGTZLST命令配置。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NGAREATZ]] · ADD NGAREATZ
- [[command/UNC/20.15.2/LST-NGAREATZ]] · LST NGAREATZ
- [[command/UNC/20.15.2/MOD-NGAREATZ]] · MOD NGAREATZ
- [[command/UNC/20.15.2/RMV-NGAREATZ]] · RMV NGAREATZ

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改5G区域时区参数（MOD-NGAREATZ）_72153845.md`
- 原始手册：`evidence/UNC/20.15.2/删除5G区域时区参数（RMV-NGAREATZ）_20993738.md`
- 原始手册：`evidence/UNC/20.15.2/增加5G区域时区参数（ADD-NGAREATZ）_20674118.md`
- 原始手册：`evidence/UNC/20.15.2/查询5G区域时区参数（LST-NGAREATZ）_20833786.md`
