---
id: UNC@20.15.2@ConfigObject@GUTISELAREACODE
type: ConfigObject
name: GUTISELAREACODE（GUTI选网功能区域编码）
nf: UNC
version: 20.15.2
object_name: GUTISELAREACODE
object_kind: entity
applicable_nf:
- AMF
status: active
---

# GUTISELAREACODE（GUTI选网功能区域编码）

## 说明

**适用NF：AMF**

AMF可基于运营商规划的区域进行GUTI选网功能的差异化控制。AMF配置上述“区域”分为两个步骤，首先通过本命令定义区域编码（GUTISELAREACODE），其次通过ADD GUTISELAREAMEM为已定义的区域编码添加位置成员。

在大网和园区共享RAN场景下，大网AMF可以通过本地配置将园区用户在大网AMF注册成功后，通过分配给园区用户的GUTI中携带园区AMF的SET ID和POINTER的方式将园区用户重新注册到园区AMF上。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-GUTISELAREACODE]] · ADD GUTISELAREACODE
- [[command/UNC/20.15.2/LST-GUTISELAREACODE]] · LST GUTISELAREACODE
- [[command/UNC/20.15.2/RMV-GUTISELAREACODE]] · RMV GUTISELAREACODE

## 证据

- 原始手册：`evidence/UNC/20.15.2/GUTISELAREACODE.md`
- 原始手册：`evidence/UNC/20.15.2/GUTISELAREACODE.md`
- 原始手册：`evidence/UNC/20.15.2/GUTISELAREACODE.md`
