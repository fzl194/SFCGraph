---
id: UNC@20.15.2@ConfigObject@NGHPLMN
type: ConfigObject
name: NGHPLMN（5G Home PLMN）
nf: UNC
version: 20.15.2
object_name: NGHPLMN
object_kind: entity
applicable_nf:
- AMF
- SMF
- NRF
- SGW-C
- PGW-C
- GGSN
- NSSF
- SMSF
status: active
---

# NGHPLMN（5G Home PLMN）

## 说明

**适用NF：AMF、SMF、NRF、SGW-C、PGW-C、GGSN、NSSF、SMSF**

该命令用于增加运营商的Home PLMN。所谓Home PLMN是指签约用户的归属PLMN。一个大型运营商可能有多个Home PLMN。该命令属于基础配置，AMF、SMF、SGW-C、PGW-C、GGSN、NRF、NSSF、SMSF通过用户标识（SUPI/SUCI）中的PLMN和本命令配置数据，识别用户是否本网签约用户。

## 操作本对象的命令

- [ADD NGHPLMN](command/UNC/20.15.2/ADD-NGHPLMN.md)
- [LST NGHPLMN](command/UNC/20.15.2/LST-NGHPLMN.md)
- [MOD NGHPLMN](command/UNC/20.15.2/MOD-NGHPLMN.md)
- [RMV NGHPLMN](command/UNC/20.15.2/RMV-NGHPLMN.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改5G-Home-PLMN（MOD-NGHPLMN）_09652653.md`
- 原始手册：`evidence/UNC/20.15.2/删除5G-Home-PLMN（RMV-NGHPLMN）_09653738.md`
- 原始手册：`evidence/UNC/20.15.2/增加5G-Home-PLMN（ADD-NGHPLMN）_09651693.md`
- 原始手册：`evidence/UNC/20.15.2/查询5G-Home-PLMN（LST-NGHPLMN）_09653743.md`
