---
id: UNC@20.15.2@ConfigObject@NGAREARESELCTRL
type: ConfigObject
name: NGAREARESELCTRL（AMF区域重选功能控制参数）
nf: UNC
version: 20.15.2
object_name: NGAREARESELCTRL
object_kind: global_setting
applicable_nf:
- AMF
status: active
---

# NGAREARESELCTRL（AMF区域重选功能控制参数）

## 说明

**适用NF：AMF**

该命令用于设置AMF区域重选功能控制参数。

在大网和园区共享RAN场景下，大网AMF可以通过本地配置将园区用户请求通过RAN重定向给园区AMF；园区AMF可以通过本地配置将大网用户请求通过基站重定向给大网AMF。大网和园区以及园区（如园区1、园区2）之间共享RAN且园区1、2和大网失联时，园区1的AMF可以通过本地配置将园区2的用户请求通过RAN重定向到园区2的AMF; 园区2的AMF可以通过本地配置将园区1的用户请求通过RAN重定向到园区1的AMF。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-NGAREARESELCTRL]] · LST NGAREARESELCTRL
- [[command/UNC/20.15.2/SET-NGAREARESELCTRL]] · SET NGAREARESELCTRL

## 证据

- 原始手册：`evidence/UNC/20.15.2/NGAREARESELCTRL.md`
- 原始手册：`evidence/UNC/20.15.2/NGAREARESELCTRL.md`
