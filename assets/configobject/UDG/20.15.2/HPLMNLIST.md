---
id: UDG@20.15.2@ConfigObject@HPLMNLIST
type: ConfigObject
name: HPLMNLIST（UPF设备的归属PLMN）
nf: UDG
version: 20.15.2
object_name: HPLMNLIST
object_kind: entity
applicable_nf:
- SGW-U
- PGW-U
- UPF
status: active
---

# HPLMNLIST（UPF设备的归属PLMN）

## 说明

**适用NF：SGW-U、PGW-U、UPF**

该命令用于增加UPF设备的一个归属PLMN。

增加UPF的归属PLMN（即HPLMN）的目的是：

区分用户是本地用户、拜访用户还是漫游用户。

在UPF发给AAA的计费消息中携带UPF的归属PLMN信息。

UPF支持三种类型的用户：本地用户、漫游用户、拜访用户。

本地用户：就是本PLMN网络上签约，未漫游到其他PLMN且在本UPF激活的用户。

漫游用户：就是本PLMN网络上签约，漫游到其他PLMN内且仍在本UPF激活的用户。

拜访用户：就是其他PLMN网络上签约，漫游到本PLMN内，使用本UPF激活的用户。

本地用户和漫游用户统称本PLMN的归属用户。

## 操作本对象的命令

- [[command/UDG/20.15.2/ADD-HPLMNLIST]] · ADD HPLMNLIST
- [[command/UDG/20.15.2/LST-HPLMNLIST]] · LST HPLMNLIST
- [[command/UDG/20.15.2/RMV-HPLMNLIST]] · RMV HPLMNLIST

## 证据

- 原始手册：`evidence/UDG/20.15.2/HPLMNLIST.md`
- 原始手册：`evidence/UDG/20.15.2/HPLMNLIST.md`
- 原始手册：`evidence/UDG/20.15.2/HPLMNLIST.md`
