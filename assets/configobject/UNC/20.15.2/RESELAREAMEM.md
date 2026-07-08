---
id: UNC@20.15.2@ConfigObject@RESELAREAMEM
type: ConfigObject
name: RESELAREAMEM（AMF重选功能区域成员）
nf: UNC
version: 20.15.2
object_name: RESELAREAMEM
object_kind: entity
applicable_nf:
- AMF
status: active
---

# RESELAREAMEM（AMF重选功能区域成员）

## 说明

**适用NF：AMF**

一个AMF重选功能的区域由若干个跟踪区组成，该命令用于为指定的区域增加跟踪区成员。

在大网和园区共享RAN场景下，大网AMF可以通过本地配置将园区用户请求通过RAN重定向给园区AMF；园区AMF可以通过本地配置将大网用户请求通过基站重定向给大网AMF。大网和园区以及园区（如园区1、园区2）之间共享RAN且园区1、2和大网失联时，园区1的AMF可以通过本地配置将园区2的用户请求通过RAN重定向到园区2的AMF; 园区2的AMF可以通过本地配置将园区1的用户请求通过RAN重定向到园区1的AMF。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-RESELAREAMEM]] · ADD RESELAREAMEM
- [[command/UNC/20.15.2/LST-RESELAREAMEM]] · LST RESELAREAMEM
- [[command/UNC/20.15.2/RMV-RESELAREAMEM]] · RMV RESELAREAMEM

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除AMF重选功能区域成员（RMV-RESELAREAMEM）_23623006.md`
- 原始手册：`evidence/UNC/20.15.2/增加AMF重选功能区域成员（ADD-RESELAREAMEM）_23782734.md`
- 原始手册：`evidence/UNC/20.15.2/查询AMF重选功能区域成员（LST-RESELAREAMEM）_70382333.md`
