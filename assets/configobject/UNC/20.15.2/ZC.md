---
id: UNC@20.15.2@ConfigObject@ZC
type: ConfigObject
name: ZC（区域码）
nf: UNC
version: 20.15.2
object_name: ZC
object_kind: entity
applicable_nf:
- SGSN
- MME
status: active
---

# ZC（区域码）

## 说明

**适用网元：SGSN、MME**

此命令用于增加区域码记录。区域码用于定义允许或者禁止用户漫游的区域，借助一个完全的区域码列表，运营商可以确定用户是否能在此区域漫游。用户不允许在此区域漫游的情况下， UNC 回复给用户的拒绝消息中携带的原因值可通过软参配置，2G/3G用户可使用软参BYTE_EX64配置，4G用户可使用软参BYTE_EX209配置。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-ZC]] · ADD ZC
- [[command/UNC/20.15.2/LST-ZC]] · LST ZC
- [[command/UNC/20.15.2/RMV-ZC]] · RMV ZC

## 证据

- 原始手册：`evidence/UNC/20.15.2/ZC.md`
- 原始手册：`evidence/UNC/20.15.2/ZC.md`
- 原始手册：`evidence/UNC/20.15.2/ZC.md`
