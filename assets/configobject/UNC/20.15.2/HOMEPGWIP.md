---
id: UNC@20.15.2@ConfigObject@HOMEPGWIP
type: ConfigObject
name: HOMEPGWIP（归属地PGW-C IP地址）
nf: UNC
version: 20.15.2
object_name: HOMEPGWIP
object_kind: entity
applicable_nf:
- SGW-C
status: active
---

# HOMEPGWIP（归属地PGW-C IP地址）

## 说明

**适用NF：SGW-C**

该命令用于Proxy S-GW特性中指定用户的归属地PGW-C IP地址。如果用户在本配置中指定了归属地PGW-C的IP地址，则不再通过DNS解析来获取归属地PGW-C的IP地址。

## 操作本对象的命令

- [ADD HOMEPGWIP](command/UNC/20.15.2/ADD-HOMEPGWIP.md)
- [LST HOMEPGWIP](command/UNC/20.15.2/LST-HOMEPGWIP.md)
- [MOD HOMEPGWIP](command/UNC/20.15.2/MOD-HOMEPGWIP.md)
- [RMV HOMEPGWIP](command/UNC/20.15.2/RMV-HOMEPGWIP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改归属地PGW-C-IP地址（MOD-HOMEPGWIP）_06399920.md`
- 原始手册：`evidence/UNC/20.15.2/删除归属地PGW-C-IP地址（RMV-HOMEPGWIP）_06399925.md`
- 原始手册：`evidence/UNC/20.15.2/增加归属地PGW-C-IP地址（ADD-HOMEPGWIP）_06399905.md`
- 原始手册：`evidence/UNC/20.15.2/查询归属地PGW-C-IP地址（LST-HOMEPGWIP）_06399912.md`
