---
id: UNC@20.15.2@ConfigObject@CHARGECHAR
type: ConfigObject
name: CHARGECHAR（对本地用户、漫游用户、拜访用户所采用的计费属性）
nf: UNC
version: 20.15.2
object_name: CHARGECHAR
object_kind: entity
applicable_nf:
- SGW-C
- PGW-C
- SMF
status: active
---

# CHARGECHAR（对本地用户、漫游用户、拜访用户所采用的计费属性）

## 说明

**适用NF：SGW-C、PGW-C、SMF**

此命令用来添加对本地用户、漫游用户、拜访用户所采用的计费属性。

计费属性指对用户所采用的计费类型，不同计费类型可以有不同的话单生成方式。用户的计费属性可以遵从SGSN/SGW上的属性配置，也可以遵从UNC上的属性配置。本地用户和漫游用户统称本PLMN（Public Land Mobile Network，运营商移动网络标识）的归属用户。UNC支持三种类型的用户：本地用户、漫游用户、拜访用户。

本地用户：指本PLMN网络上签约，未漫游到其他PLMN且在本UNC激活的用户。

漫游用户：指本PLMN网络上签约，漫游到其他PLMN且仍在本UNC激活的用户。

拜访用户：指其他PLMN网络上签约，漫游到本PLMN且使用本UNC激活的用户。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-CHARGECHAR]] · ADD CHARGECHAR
- [[command/UNC/20.15.2/LST-CHARGECHAR]] · LST CHARGECHAR
- [[command/UNC/20.15.2/MOD-CHARGECHAR]] · MOD CHARGECHAR
- [[command/UNC/20.15.2/RMV-CHARGECHAR]] · RMV CHARGECHAR

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改对本地用户、漫游用户、拜访用户所采用的计费属性（MOD-CHARGECHAR）_09896810.md`
- 原始手册：`evidence/UNC/20.15.2/删除对本地用户、漫游用户、拜访用户所采用的计费属性（RMV-CHARGECHAR）_09896811.md`
- 原始手册：`evidence/UNC/20.15.2/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD-CHARGECHAR）_09896809.md`
- 原始手册：`evidence/UNC/20.15.2/查询对本地用户、漫游用户、拜访用户所采用的计费属性（LST-CHARGECHAR）_09896812.md`
