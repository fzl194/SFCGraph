---
id: UNC@20.15.2@ConfigObject@RESELAREACODE
type: ConfigObject
name: RESELAREACODE（AMF重选功能区域编码）
nf: UNC
version: 20.15.2
object_name: RESELAREACODE
object_kind: entity
applicable_nf:
- AMF
status: active
---

# RESELAREACODE（AMF重选功能区域编码）

## 说明

**适用NF：AMF**

AMF可基于运营商规划的区域进行AMF重选功能的差异化控制。AMF配置上述“区域”分为两个步骤，首先通过本命令定义区域编码（RESELAREACODE），其次通过ADD RESELAREAMEM为已定义的区域编码添加位置成员。

在大网和园区共享RAN场景下，大网AMF可以通过本地配置将园区用户请求通过RAN重定向给园区AMF；园区AMF可以通过本地配置将大网用户请求通过基站重定向给大网AMF。大网和园区以及园区（如园区1、园区2）之间共享RAN且园区1、2和大网失联时，园区1的AMF可以通过本地配置将园区2的用户请求通过RAN重定向到园区2的AMF; 园区2的AMF可以通过本地配置将园区1的用户请求通过RAN重定向到园区1的AMF。

## 操作本对象的命令

- [ADD RESELAREACODE](command/UNC/20.15.2/ADD-RESELAREACODE.md)
- [LST RESELAREACODE](command/UNC/20.15.2/LST-RESELAREACODE.md)
- [RMV RESELAREACODE](command/UNC/20.15.2/RMV-RESELAREACODE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除AMF重选功能区域编码（RMV-RESELAREACODE）_23782822.md`
- 原始手册：`evidence/UNC/20.15.2/增加AMF重选功能区域编码（ADD-RESELAREACODE）_70382293.md`
- 原始手册：`evidence/UNC/20.15.2/查询AMF重选功能区域编码（LST-RESELAREACODE）_70462557.md`
