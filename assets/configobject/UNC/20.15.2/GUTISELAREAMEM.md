---
id: UNC@20.15.2@ConfigObject@GUTISELAREAMEM
type: ConfigObject
name: GUTISELAREAMEM（GUTI选网功能区域成员）
nf: UNC
version: 20.15.2
object_name: GUTISELAREAMEM
object_kind: entity
applicable_nf:
- AMF
status: active
---

# GUTISELAREAMEM（GUTI选网功能区域成员）

## 说明

**适用NF：AMF**

一个GUTI选网功能的区域由若干个跟踪区组成，该命令用于为指定的区域增加跟踪区成员。

在大网和园区共享RAN场景下，大网AMF可以通过本地配置将园区用户在大网AMF注册成功后，通过分配给园区用户的GUTI中携带园区AMF的SET ID和POINTER的方式将园区用户重新注册到园区AMF上。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-GUTISELAREAMEM]] · ADD GUTISELAREAMEM
- [[command/UNC/20.15.2/LST-GUTISELAREAMEM]] · LST GUTISELAREAMEM
- [[command/UNC/20.15.2/RMV-GUTISELAREAMEM]] · RMV GUTISELAREAMEM

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除GUTI选网功能区域成员（RMV-GUTISELAREAMEM）_14059369.md`
- 原始手册：`evidence/UNC/20.15.2/增加GUTI选网功能区域成员（ADD-GUTISELAREAMEM）_77579544.md`
- 原始手册：`evidence/UNC/20.15.2/查询GUTI选网功能区域成员（LST-GUTISELAREAMEM）_13939877.md`
