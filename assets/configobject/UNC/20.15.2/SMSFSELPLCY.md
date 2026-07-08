---
id: UNC@20.15.2@ConfigObject@SMSFSELPLCY
type: ConfigObject
name: SMSFSELPLCY（SMSF选择策略）
nf: UNC
version: 20.15.2
object_name: SMSFSELPLCY
object_kind: entity
applicable_nf:
- AMF
status: active
---

# SMSFSELPLCY（SMSF选择策略）

## 说明

**适用NF：AMF**

该命令用于对指定的用户（群）增加SMSF的选择策略。通过本配置，AMF可以对不同用户（群）使用差异化的条件选择到不同的SMSF，以满足运营商灵活部署网络的要求。当SUPISW开关打开时，NRF会返回满足SUPI号段的所有NF；当GPSISW开关打开时，NRF会返回满足GPSI号段的所有NF；两个开关都打开时，NRF会返回同时满足SUPI号段与GPSI号段的NF，若无同时满足SUPI号段与GPSI号段的NF，则NRF会返回空。

## 操作本对象的命令

- [ADD SMSFSELPLCY](command/UNC/20.15.2/ADD-SMSFSELPLCY.md)
- [LST SMSFSELPLCY](command/UNC/20.15.2/LST-SMSFSELPLCY.md)
- [MOD SMSFSELPLCY](command/UNC/20.15.2/MOD-SMSFSELPLCY.md)
- [RMV SMSFSELPLCY](command/UNC/20.15.2/RMV-SMSFSELPLCY.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SMSF选择策略（MOD-SMSFSELPLCY）_91819425.md`
- 原始手册：`evidence/UNC/20.15.2/删除SMSF选择策略（RMV-SMSFSELPLCY）_91699949.md`
- 原始手册：`evidence/UNC/20.15.2/增加SMSF选择策略（ADD-SMSFSELPLCY）_45020376.md`
- 原始手册：`evidence/UNC/20.15.2/查询SMSF选择策略（LST-SMSFSELPLCY）_91579981.md`
