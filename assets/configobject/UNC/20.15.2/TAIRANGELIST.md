---
id: UNC@20.15.2@ConfigObject@TAIRANGELIST
type: ConfigObject
name: TAIRANGELIST（NF TAI区域信息）
nf: UNC
version: 20.15.2
object_name: TAIRANGELIST
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

# TAIRANGELIST（NF TAI区域信息）

## 说明

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG**

该命令用于添加NF实例支持的TAI信息。

- 当NF实例只支持为某些TAI服务时，需要对支持的TAI进行配置。
- 当SMF向NRF注册时，如果BINDSMFINFOID不为空或者“null”，则必须在ADD SMFINFOEXT中配置ID与BINDSMFINFOID相同的记录，否则该命令将不生效。
- 当NWDAF向NRF注册时，如果BINDNWDAFINFOID不为空或者“null”，则必须在ADD NWDAFINFOEXT中配置ID与BINDNWDAFINFOID相同的记录，否则该命令将不生效。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-TAIRANGELIST]] · ADD TAIRANGELIST
- [[command/UNC/20.15.2/LST-TAIRANGELIST]] · LST TAIRANGELIST
- [[command/UNC/20.15.2/RMV-TAIRANGELIST]] · RMV TAIRANGELIST

## 证据

- 原始手册：`evidence/UNC/20.15.2/TAIRANGELIST.md`
- 原始手册：`evidence/UNC/20.15.2/TAIRANGELIST.md`
- 原始手册：`evidence/UNC/20.15.2/TAIRANGELIST.md`
